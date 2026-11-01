interface A { readonly next: A; readonly payload: never }
interface B { readonly next: B; readonly payload: unknown }
declare const a: A;
declare const b: B;
const good: B = a;
// @ts-expect-error unknown payload is not assignable to never
const bad: A = b;
