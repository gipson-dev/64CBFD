# Dual record callback and animation updater recovered and byte matched

Date: 2026-11-07. Continues [Note 2161](2161-game-record-animation-update-match-20261107.md)
from consumer `51ce11d52b51bf00379bec1a67e1272c3136560e` and tools
`241f2fa3221f60716a18f5899c712c7b41018f1e`. One Game recovery advances the
active 80% total goal. No host-port or frozen Release changes.

## Recovered body and callback contract

`void func_1513CFE4(u8 *record)` in `conker/src/game_169510.c` replaces the
false s32 zero-return placeholder. All **195 words / 780 bytes** match at
VA0x1513CFE4..0x1513D2F0, ROM0x16A494..0x16A7A0. The existing O2/g3,
MIPS2/O32 profile emits the original32-byte frame, RA atSP+0x14, signed
remove byte atSP+0x1B and incoming pointer home atSP+0x20. No saved S
registers or floating-point instructions are added.

1. Word+0x10 bit0 gates the routine. Flags+0x58 bit0 decrements signed16
   timer+0x1C by live D_800BE9E4 ticks, narrows it, then requests removal
   when the stored timer is negative.
2. Nonzero byte+0x70 selects D_80089CB8; byte+0x71 selects D_80089D60.
   **Both services execute in order even if the first requests removal.**
   A zero result requests removal. Each call saves/reloads the pointer and
   signed byte home; the second selector is read after the first callback.
3. Flags0x08000000/0x10000000 gate fades while removal is clear and signed16
   timer+0x1C is below signed16 threshold+0x6C. Multiply signed16 scale+0x6E
   by timer; both tests compare against byte+0x5C. Store the narrowed result
   into+0x5C or+0x2B. Reload flags after the possible first store.
4. Nonzero signed32 rate+0x24 advances cursor+0x20 by low32 rate*ticks.
   D_80090B64[byte18*12] gives the frame count; limit=`(frames << 16)-1`.
   Above limit,0x800 requests removal and0x400 reflects/reverses. Below zero,
   0x1000 removes and0x400 reflects/reverses. Otherwise repeatedly subtract
   or add the limit. This variant has no stop/clamp arms. Keep signed
   remainder, wrap arithmetic and the original four software trap guards.
5. If removal remains requested, byte+0x72 selects D_80089E10. **A nonzero
   result vetoes removal**; zero retains the request. An absent callback also
   retains it. Call func_1516972C only when the final signed byte is nonzero.

Local byte-offset views and three typed callback table declarations preserve
the packed field layout without broad shared-structure edits. The existing
frame-table declaration is reused. Source includes a concise behavior comment;
retained original assembly stays available.

## Closed normalization and proof boundaries

The selected complete C body emits195 words and the correct frame/homes.
Raw SHA-256 is `b24b9c8d5994b3af984a6d9c5937b6b36cac1d27f8ec93d2221c5c1cf5cccce6`.
All **13 relocation bindings** remain literal. Four guards move the closed
early flags lifetime fromA2 toA1: words49,50,68,70. Word90 overwritesA2 with
rate; word96 overwritesA1 with the frame-table address before reuse.

Eight guards cover two ordinary-RAM self-store loops at words135..139 and
167..170. At each edge,V0 equals the word in RAM[A0+0x20]; A0 andV1 stay
fixed and the only mutation is that cursor store. Forwarding the preceding
store and copying the new cursor in the branch delay preserves low32
arithmetic, signed comparisons, loop count and public result. The unchanged
branch displacements and complete raw/binding fingerprints pin both windows.
Six closed-loop checks and two effective broken-invariant counterexamples
record the precondition. No instruction insertion/deletion or branch retarget.

**Raw C is qualified for public memory, calls and termination in ordinary
mapped RAM without concurrent, volatile, atomic or MMIO effects.** Its
redundant reads are not claimed private-register, access-prefix or fault
equivalent. Separately, normalized output matches retail's full private
machine state and memory-access prefixes. Signed division overflow uses a
bounded guest convention followed by retained software BREAK6; no hardware
exception or portable-C exceptional-arithmetic claim is made.

Two complete-owner source shapes (compound/explicit narrowed timer) produce
the identical selected raw body and12 differences. Cursor-variable variants
produce193 words and70 differences and were rejected. Private screens remain
in the adjacent ignored directory; none received separate matching credit.

## Actual tables, original caller and focused checks

Retained callback table lengths are42,44 and3 words at D_80089CB8,
D_80089D60 and D_80089E10, ROM0x22E778/0x22E820/0x22E8D0. Each starts
with the absent-callback entry. The following D_80089E1C pool is not included.
Target0x150CD17C appears in both update tables (indices19/29); stage-aware
providers and independent answers prevent that duplicate from conflating
service semantics.

An aligned retained-ROM census finds zero direct JALs, three entry pointers
atROM0x230518/0x230E3C/0x2310E0 (VA0x8008BA58/0x8008C37C/0x8008C620),
and no interior pointers. They are registry slot0 for kinds0x1C/0x49/0x56
in D_8008B4A8's52-byte entries. Existing func_1513D2F0 selects these kinds.
The full original **74-word func_151670C0** passes one record pointer and
ignoresV0. All74 words execute across **120 connected cases per body**,
covering three kinds, two banks, one/two records, depth0/1 and mutations.
The next link is stored before JALR. **Production's dispatcher is still an
unrestored stub**; this qualifies its original interface, not its restoration.

Seven target checks pass before and after installation for both tools copies:

* **733 guest cases per body**, for retail/normalized/raw, agree with the
  independent integer model. Cover both callback outcomes/order, all actual
  nonzero table selectors, exit veto, live selector/flag/time/frame mutations,
  signed homes, record/global aliases, timer narrowing and cursor boundaries.
* **192 words execute; all195 compare**. Literal trap words125/131/157 are
  unreachable: all256 frame bytes yield a nonzero limit, and the positive
  branch cannot have INT_MIN/-1. The negative-overflow software trap fires.
  A disabled record needs only the active word and actual private frame.
* **71 fired access cuts**, including15 delay cuts, compare normalized/retail
  full private memory, GPR/FPR/HI/LO, PC, traces and saved/home lifetimes.
* Native32 O0/O2/O3 each pass **712 ordinary-record cases** with SDK types,
  pointer32, typed void updater/s32 table entries, disjoint banks and trapping
  UBSan. Twelve compiled negative controls all reject with exit1, including
  short-circuiting the second callback, reversing either callback or exit
  result, wrong fade/period/reflection/reversal and stale flags.
* Two independent GNU links verify all13 bindings and signed LO16 carries.
  Raw/binding/history/pool corruptions and six whole-image corruptions reject.

Callback/release behavior remains explicit bounded-provider coverage; live
gameplay acceptance is not inferred. Aliases, private-home writes and
exceptional arithmetic are guest-only. The first native fixture lacked the
shared frame-table declaration already present in production's owner; adding
that fixture declaration resolved compilation, then all target gates reran.
No Claude call was needed for this routine.

## Production, linked image and progress

All181 frozen inputs,58 raw/padded neighbors, pools, register masks/options,
and43 inherited compiler warnings remain fixed. The padder uses the existing
`jtbl_800A5188_game` anchor. Actual Make recompiles only game_169510.c and
equals the independent complete-image prediction: **540 changed bytes,
zero exclusions** (539 Game-body bytes and one symbol-extent byte). There
is no symbol/string ordering change; only the target extent grows12->780.

All6,052 addresses and **189,088 protected Game bytes across720 owners**
remain exact. Exactly12 guard rows append; prior guards, progress CSV and
Makefile remain unchanged. Compile/link pass; the still-nonmatching whole-ROM
checksum retains expected exit2 and inherited duplicate-recipe warning.
Both tools copies pass fresh smoke checks; three fingerprinted unchanged
shared regressions per copy are explicitly reused. A disposable overlay and
hashed read-only missing-helper fallback preserve all2,434 sibling dirty paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,232 / 5,512 | 76.78% | 0 | 1280 |
| Game | 3,559 / 4,839 | 73.55% | 0 | 1280 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**178 more exact functions** remain to4,410/80%. Root README gets aggregate
rows only; four concise index leads preserve all historical content. Refresh
Graphify on changed paths with fail-closed legacy-node retention, without a
fresh full-corpus claim. Commit tools before consumer source/docs/pin and
verify the fresh post-commit hook terminal and stable production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `0fc69d0e3506cb9ac7307f37d787c8895a5183b5a2023a64067f157999359fd5` |
| Production binary | `a6af626bdba1569dd7f7ba3df1e54ebd5210e6cbeff1bd52ce6a796b462bdddf` |
| Padded owner | `0d2ba0002ec7aacf0f2848c0d1aa69e823b5804b8fce377508b71f7870f82c1f` |
| Guard manifest | `3cac0eb5aeb58c3d77c9a52374a6707ff9bc3c8d426b8f1f1e135ead4847f776` |

Ignored receipts: `conker/build/game-dual-record-animation-update-1513CFE4-match/`.
Next: **func_1513E6E8**, the85-word leaf callback atVA0x1513E6E8..0x1513E83C,
ROM0x16BB98..0x16BCEC and index1 of the first table. Inspect its four gated
motion/field groups and final byte reset, then qualify independently. Keep
other private candidates uncredited and the80% goal active; preserve frozen
handwritten/hidden-ABI boundaries, private inputs, saves and host Release.
