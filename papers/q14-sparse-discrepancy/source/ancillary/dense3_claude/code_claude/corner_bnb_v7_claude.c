/* Corner branch-and-bound for the HMMS-residual problem of sparse families (C port of
 * q14paper_claude/ancillary/small_n_check/sparse_bnb_dfs.py, same necessary conditions):
 *
 *  For a pattern (j fractional items, each read by 1 or 2 of n functions), a product
 *  distribution w(p) on {0,1}^j with p in [0,1/2]^j (WLOG by negating coordinates), and
 *  2-Lipschitz mean-zero functions h_i on {0,1}^{J_i}, if no corner is good at threshold c
 *  then for every i the bad set is U_i^+ u U_i^- (local patterns) with
 *     d(U+,U-) >= floor(c)+1,  and for each nonempty part U:  E_w[d(X_{J_i},U)] > c/2,
 *  and the lifts of all bad sets cover {0,1}^j  (Lemma lem:necessaryc of the paper).
 *  The condition E_w[...] > c/2 is multilinear in p, so if it fails at all vertices of a box
 *  it fails on the box.  A box is CLEARED if no cover exists using only parts that satisfy
 *  the condition at some box vertex (sound relaxation).  Boxes are bisected along the longest
 *  side (first index on ties) down to maxdepth.  All arithmetic is exact (128-bit integers).
 *
 *  input (stdin): one pattern per line: "j a1 b1 a2 b2 ... aj bj"  (b=-1: private item)
 *  usage: ./corner_bnb n c_num c_den maxdepth
 *  output: one line per pattern: "P <line no> boxes <B> fails <F>" ; uncleared boxes listed.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

typedef __int128 i128;
typedef unsigned __int128 u128;

#define MAXJ 7
#define MAXN 8
#define MAXL (1 << MAXJ)

static int n, j, maxdepth, dmix, dmixv[MAXN];
static long long cnumv[MAXN];
static long long cnum, cden; /* c = cnum/cden ; threshold c/2 */
static int Jl[MAXN][MAXJ], dl[MAXN], NLc[MAXN];
static int proj[MAXN][MAXL];
static u128 lift[MAXN][MAXL];
static int active[MAXN], nact;
static u128 fullmask;
static int pop7[MAXL];
static int samenext[MAXJ];
static long long skipped_boxes;

/* weights for current box */
static i128 W[MAXN][MAXL][MAXL]; /* W[i][vertex][localcorner] */
static int nW[MAXN];
static i128 scale[MAXN]; /* DEN^{d_i} */

/* DFS state */
static u128 smask[MAXN][2];
static unsigned char dmin[MAXN][2][MAXL];
static int sne[MAXN][2]; /* nonempty flags */

static long long DEN;

/* ---- v7: alive-vertex tracking + incremental feasibility tables (same search, same results) ----
 * For a nonempty set U = U_i^s we keep the list of box vertices v with S_v(U) > thr, where
 * S_v(U) = sum_z W_v(z) dist(z,U) (scaled); S_v only decreases when U grows, so dead vertices stay dead.
 * okt[i][s][y] = 1 iff adding y to U_i^s keeps (C1) and (C2)-at-some-vertex.  When y is added to U_i^s,
 * only the tables of (i,s) (recomputed) and (i,1-s) (entries within distance < dmix of y zeroed) change. */
static long long dfs_nodes;
static int prev_same[MAXN];
static int opened[MAXN];
static unsigned char okt[MAXN][2][MAXL];
static int nalive[MAXN][2];
static unsigned char alive[MAXN][2][MAXL];
static i128 Sv[MAXN][2][MAXL];       /* S_v(U) for the alive vertices, indexed by position */
static i128 basev[MAXN][MAXL][MAXL];  /* basev[i][v][y] = S_v({y}) */
static i128 thrv[MAXN];               /* S > thr  <=>  2*cden*S > cnum*scale */

static inline int above(int i, i128 s) { return (i128)2 * cden * s > thrv[i]; }

static void recompute_table(int i, int sg) {
    int NL = NLc[i];
    u128 om = smask[i][1 - sg];
    for (int y = 0; y < NL; y++) {
        unsigned char ok = 0;
        if (!((smask[i][sg] >> y) & 1)) {
            int bad = 0;
            if (om) for (int x = 0; x < NL; x++)
                if (((om >> x) & 1) && pop7[x ^ y] < dmixv[i]) { bad = 1; break; }
            if (!bad) {
                if (!sne[i][sg]) {
                    for (int v = 0; v < nW[i]; v++) if (above(i, basev[i][v][y])) { ok = 1; break; }
                } else {
                    for (int a = 0; a < nalive[i][sg]; a++) {
                        int v = alive[i][sg][a];
                        i128 s = Sv[i][sg][a];
                        for (int z = 0; z < NL; z++) {
                            int dd = pop7[y ^ z], dm = dmin[i][sg][z];
                            if (dd < dm) s -= W[i][v][z] * (i128)(dm - dd);
                        }
                        if (above(i, s)) { ok = 1; break; }
                    }
                }
            }
        }
        okt[i][sg][y] = ok;
    }
}

static long long box_nodes, node_budget = 0; static int budget_hit;
static int dfs(u128 cov) {
    if (cov == fullmask) return 1;
    dfs_nodes++; box_nodes++;
    if (node_budget && box_nodes > node_budget) { budget_hit = 1; return 1; }
    int lab_i[2 * MAXN], lab_s[2 * MAXN], nl = 0;
    for (int a = 0; a < nact; a++) {
        int i = active[a];
        if (opened[i]) {
            lab_i[nl] = i; lab_s[nl++] = 0;
            lab_i[nl] = i; lab_s[nl++] = 1;
        } else {
            int ps = prev_same[i];
            if (ps >= 0 && !opened[ps]) continue;
            lab_i[nl] = i; lab_s[nl++] = 0;   /* first sign of a function is '+' */
        }
    }
    int Nj = 1 << j, bestx = -1, bestc = 1 << 30;
    for (int x = 0; x < Nj; x++) {
        if ((cov >> x) & 1) continue;
        int cnt = 0;
        for (int l = 0; l < nl; l++) {
            int i = lab_i[l];
            if (okt[i][lab_s[l]][proj[i][x]]) cnt++;
        }
        if (cnt < bestc) { bestc = cnt; bestx = x; if (cnt == 0) return 0; }
    }
    int x = bestx;
    for (int l = 0; l < nl; l++) {
        int i = lab_i[l], sg = lab_s[l];
        int y = proj[i][x];
        if (!okt[i][sg][y]) continue;
        int NL = NLc[i];
        /* save state of (i,0),(i,1) */
        unsigned char sav_okt[2][MAXL], sav_dmin[MAXL], sav_alive[MAXL];
        i128 sav_S[MAXL];
        memcpy(sav_okt[0], okt[i][0], NL); memcpy(sav_okt[1], okt[i][1], NL);
        memcpy(sav_dmin, dmin[i][sg], NL);
        int sav_nal = nalive[i][sg];
        memcpy(sav_alive, alive[i][sg], sav_nal);
        memcpy(sav_S, Sv[i][sg], sizeof(i128) * sav_nal);
        u128 savedmask = smask[i][sg];
        int savedne = sne[i][sg], savedop = opened[i];
        /* new alive list and S values */
        unsigned char nal_idx[MAXL]; i128 nS[MAXL]; int nal = 0;
        if (!sne[i][sg]) {
            for (int v = 0; v < nW[i]; v++) if (above(i, basev[i][v][y])) { nal_idx[nal] = (unsigned char)v; nS[nal++] = basev[i][v][y]; }
            for (int z = 0; z < NL; z++) dmin[i][sg][z] = (unsigned char)pop7[y ^ z];
        } else {
            for (int a = 0; a < sav_nal; a++) {
                int v = sav_alive[a]; i128 s = sav_S[a];
                for (int z = 0; z < NL; z++) {
                    int dd = pop7[y ^ z], dm = sav_dmin[z];
                    if (dd < dm) s -= W[i][v][z] * (i128)(dm - dd);
                }
                if (above(i, s)) { nal_idx[nal] = (unsigned char)v; nS[nal++] = s; }
            }
            for (int z = 0; z < NL; z++) { int dd = pop7[y ^ z]; if (dd < dmin[i][sg][z]) dmin[i][sg][z] = (unsigned char)dd; }
        }
        if (nal == 0) { fprintf(stderr, "internal error: no alive vertex\n"); exit(4); }
        memcpy(alive[i][sg], nal_idx, nal); memcpy(Sv[i][sg], nS, sizeof(i128) * nal); nalive[i][sg] = nal;
        smask[i][sg] |= ((u128)1) << y;
        sne[i][sg] = 1;
        opened[i] = 1;
        recompute_table(i, sg);
        for (int yy = 0; yy < NL; yy++) if (pop7[yy ^ y] < dmixv[i]) okt[i][1 - sg][yy] = 0;
        int ok = dfs(cov | lift[i][y]);
        /* restore */
        memcpy(okt[i][0], sav_okt[0], NL); memcpy(okt[i][1], sav_okt[1], NL);
        memcpy(dmin[i][sg], sav_dmin, NL);
        nalive[i][sg] = sav_nal; memcpy(alive[i][sg], sav_alive, sav_nal); memcpy(Sv[i][sg], sav_S, sizeof(i128) * sav_nal);
        smask[i][sg] = savedmask;
        sne[i][sg] = savedne;
        opened[i] = savedop;
        if (ok) return 1;
    }
    return 0;
}

/* box: lo[k], hi[k] are numerators over DEN */
static int cleared(const long long *lo, const long long *hi) {
    for (int a = 0; a < nact; a++) {
        int i = active[a];
        int d = dl[i], NL = NLc[i];
        /* vertices of the projected box (dedup when lo==hi) */
        int nv = 0;
        for (int vm = 0; vm < (1 << d); vm++) {
            /* skip duplicates: if lo==hi on coordinate kk, only allow bit 0 */
            int dup = 0;
            for (int kk = 0; kk < d; kk++) {
                int k = Jl[i][kk];
                if (((vm >> kk) & 1) && lo[k] == hi[k]) { dup = 1; break; }
            }
            if (dup) continue;
            long long pv[MAXJ];
            for (int kk = 0; kk < d; kk++) {
                int k = Jl[i][kk];
                pv[kk] = ((vm >> kk) & 1) ? hi[k] : lo[k];
            }
            for (int y = 0; y < NL; y++) {
                i128 prod = 1;
                for (int kk = 0; kk < d; kk++)
                    prod *= ((y >> kk) & 1) ? (i128)pv[kk] : (i128)(DEN - pv[kk]);
                W[i][nv][y] = prod;
            }
            nv++;
        }
        nW[i] = nv;
        if (getenv("FAST")) {
            /* sound envelope: UB(y) = prod_k max over the box of (p_k or 1-p_k) >= w_p(y) for all p in the box */
            for (int y = 0; y < NL; y++) {
                i128 prod = 1;
                for (int kk = 0; kk < d; kk++) {
                    int k = Jl[i][kk];
                    prod *= ((y >> kk) & 1) ? (i128)hi[k] : (i128)(DEN - lo[k]);
                }
                W[i][0][y] = prod;
            }
            nW[i] = 1;
        }
        i128 sc = 1;
        for (int kk = 0; kk < d; kk++) sc *= DEN;
        scale[i] = sc;
        smask[i][0] = smask[i][1] = 0;
        sne[i][0] = sne[i][1] = 0;
        opened[i] = 0;
        nalive[i][0] = nalive[i][1] = 0;
        thrv[i] = (i128)cnumv[i] * scale[i];
        for (int v = 0; v < nW[i]; v++)
            for (int y = 0; y < NL; y++) {
                i128 s = 0;
                for (int z = 0; z < NL; z++) s += W[i][v][z] * (i128)pop7[y ^ z];
                basev[i][v][y] = s;
            }
        recompute_table(i, 0); recompute_table(i, 1);
    }
    box_nodes = 0; budget_hit = 0;
    return !dfs(0);
}

typedef struct { long long lo[MAXJ], hi[MAXJ]; int dd; } Box;

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage\n"); return 1; }
    n = atoi(argv[1]); cnum = atoll(argv[2]); cden = atoll(argv[3]); maxdepth = atoi(argv[4]);
    dmix = (int)(cnum / cden) + 1;
    /* per-function thresholds: env LEVELS="l0,l1,..." gives c_v = l_v + (cnum/cden - floor(cnum/cden)) */
    for (int i = 0; i < MAXN; i++) { cnumv[i] = cnum; dmixv[i] = dmix; }
    if (getenv("LEVELS")) {
        char buf[256]; strncpy(buf, getenv("LEVELS"), 255); buf[255] = 0;
        char *q = buf; long long frac = cnum - (cnum / cden) * cden;
        for (int i = 0; i < n; i++) {
            long long l = strtoll(q, &q, 10); if (*q == ',') q++;
            cnumv[i] = l * cden + frac; dmixv[i] = (int)l + 1;
            fprintf(stderr, "function %d: c = %lld/%lld, dmix %d\n", i, cnumv[i], cden, dmixv[i]);
        }
    }
    if (argc > 5) node_budget = atoll(argv[5]);
    /* per-coordinate bisection depth <= maxdepth/j + 1 (longest-side rule); DEN chosen per pattern below */
    for (int x = 0; x < MAXL; x++) pop7[x] = __builtin_popcount(x);
    char line[4096];
    int lineno = 0;
    long long totfails = 0, totboxes = 0;
    Box *stack = malloc(sizeof(Box) * 200000);
    while (fgets(line, sizeof line, stdin)) {
        lineno++;
        char *p = line;
        int a[2 * MAXJ];
        j = (int)strtol(p, &p, 10);
        if (j <= 0) continue;
        for (int k = 0; k < 2 * j; k++) a[k] = (int)strtol(p, &p, 10);
        for (int i = 0; i < n; i++) dl[i] = 0;
        for (int k = 0; k + 1 < j; k++) samenext[k] = (a[2*k] == a[2*k+2] && a[2*k+1] == a[2*k+3]);
        samenext[j-1] = 0;
        if (getenv("NOSORT")) for (int k = 0; k < j; k++) samenext[k] = 0;
        if (getenv("FULL")) {
            /* non-sparse mode: every function reads every item (pattern line only gives j) */
            for (int i = 0; i < n; i++) { dl[i] = 0; for (int k = 0; k < j; k++) Jl[i][dl[i]++] = k; }
            for (int k = 0; k < j; k++) samenext[k] = (k + 1 < j) && !getenv("NOSORT");
        } else
        for (int k = 0; k < j; k++) {
            int u = a[2 * k], v = a[2 * k + 1];
            Jl[u][dl[u]++] = k;
            if (v >= 0) Jl[v][dl[v]++] = k;
        }
        int Nj = 1 << j;
        {
            int E = maxdepth / j + 3;
            int dmax = 0;
            for (int i = 0; i < n; i++) if (dl[i] > dmax) dmax = dl[i];
            if (E * dmax + 20 > 126 || E > 60) { fprintf(stderr, "overflow risk: E=%d dmax=%d\n", E, dmax); exit(2); }
            DEN = 1LL << E;
        }
        fullmask = (Nj == 128) ? ~(u128)0 : ((((u128)1) << Nj) - 1);
        nact = 0;
        for (int i = 0; i < n; i++) {
            NLc[i] = 1 << dl[i];
            for (int y = 0; y < NLc[i]; y++) lift[i][y] = 0;
            for (int g = 0; g < Nj; g++) {
                int y = 0;
                for (int kk = 0; kk < dl[i]; kk++) if ((g >> Jl[i][kk]) & 1) y |= 1 << kk;
                proj[i][g] = y;
                lift[i][y] |= ((u128)1) << g;
            }
            if (dl[i] > 0) active[nact++] = i;
        }
        /* symmetry breaking: functions with identical item sets are opened in index order */
        for (int i = 0; i < n; i++) {
            prev_same[i] = -1;
            for (int i2 = i - 1; i2 >= 0; i2--) {
                if (dl[i2] != dl[i]) continue;
                if (cnumv[i2] != cnumv[i] || dmixv[i2] != dmixv[i]) continue; /* interchangeable only with equal thresholds */
                int same = 1;
                for (int kk = 0; kk < dl[i]; kk++) if (Jl[i2][kk] != Jl[i][kk]) { same = 0; break; }
                if (same) { prev_same[i] = i2; break; }
            }
        }
        if (getenv("POINT")) {
            long long lo[MAXJ], hi[MAXJ];
            char buf[512]; strncpy(buf, getenv("POINT"), 511); buf[511] = 0;
            char *q = buf;
            for (int k = 0; k < j; k++) { lo[k] = hi[k] = strtoll(q, &q, 10); if (*q == ',') q++; }
            dfs_nodes = 0;
            int cl = cleared(lo, hi);
            printf("POINT line %d cleared %d dfsnodes %lld budget_hit %d\n", lineno, cl, dfs_nodes, budget_hit);
            fflush(stdout);
            continue;
        }
        /* branch and bound */
        int sp = 0;
        for (int k = 0; k < j; k++) { stack[0].lo[k] = 0; stack[0].hi[k] = DEN / 2; }
        stack[0].dd = 0; sp = 1;
        long long boxes = 0, fails = 0;
        while (sp > 0) {
            Box b = stack[--sp];
            { int dis = 0; for (int k = 0; k + 1 < j; k++) if (samenext[k] && b.lo[k] > b.hi[k + 1]) { dis = 1; break; }
              if (dis) { skipped_boxes++; continue; } }
            boxes++; if (getenv("VERB") && boxes % 200 == 0) { fprintf(stderr, "boxes %lld sp %d dd %d dfsnodes %lld\n", boxes, sp, b.dd, dfs_nodes); }
            if (cleared(b.lo, b.hi)) continue;
            if (b.dd >= maxdepth) {
                fails++;
                printf("UNCLEARED%s line %d box", budget_hit ? "(budget)" : "", lineno);
                for (int k = 0; k < j; k++) printf(" [%lld/%lld,%lld/%lld]", b.lo[k], DEN, b.hi[k], DEN);
                printf("\n");
                if (getenv("STOPFIRST")) { sp = 0; }
                continue;
            }
            int kb = 0;
            for (int k = 1; k < j; k++) if (b.hi[k] - b.lo[k] > b.hi[kb] - b.lo[kb]) kb = k;
            if ((b.lo[kb] + b.hi[kb]) % 2) { fprintf(stderr, "non-dyadic split (DEN too small)\n"); exit(3); }
            long long mid = (b.lo[kb] + b.hi[kb]) / 2;
            Box b1 = b, b2 = b;
            b1.hi[kb] = mid; b2.lo[kb] = mid;
            b1.dd = b2.dd = b.dd + 1;
            stack[sp++] = b1; stack[sp++] = b2;
        }
        totboxes += boxes; totfails += fails;
        printf("P %d boxes %lld fails %lld\n", lineno, boxes, fails);
        fflush(stdout);
    }
    printf("TOTAL patterns %d boxes %lld uncleared %lld dfsnodes %lld skipped %lld\n", lineno, totboxes, totfails, dfs_nodes, skipped_boxes);
    return 0;
}
