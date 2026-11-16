# Growth and one-shot curve emitter recovery and byte match - 2026-11-16

`func_151A1FB4` now has a complete typed C recovery and matches all **317
retail words / frame 0x100**, VA `0x151A1FB4..0x151A24A8`, ROM
`0x1CF464..0x1CF958`. Its zero-return placeholder is replaced by the actual
randomized particle emitter with a curve of fourteen signed shorts.

The production recount is **4,518 / 5,514 (81.94%)**, Game
**3,845 / 4,841 (79.43%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, 996 different. This adds one qualified match; the
active 85% goal needs **169** more at this denominator. Conversion remains
5,514 / 6,048 (91.17%), covering 86.19% of function bytes.

## Behavior and actual interface

The signature is `void func_151A1FB4(struct260 *record)`. The actual
`D_8008A4E8[4]` update callback pointer is VA `0x8008A4F8`, ROM `0x22EFB8`.
It runs under the original 45-word `func_15149264`. The unchanged preceding
`func_151A1EE8` factory selects update index 4 and captures a 36-byte payload
with six signed-short parameters and initial phase zero.

Phase advances by rate times `D_800BE9A4`; the emitter loops while phase is
strictly greater than 1. Each emission keeps eight integer RNG calls, four
trigonometric samples, one real RNG sample, packet submission and an optional
28-byte copy to `created+0x50`. Randomized target coordinates are spawn
positions, captured before subsequent random providers can change the record.

The 56-byte packet uses fractionScale 18, initial red/green/blue 5/0/0,
flags 0xC0001, a persistent curve-flags word and descriptor `D_80090D34`.
The curve contains intensity/size ramps, live size growth and a one-shot
parameter switch. Its later draws use the third signed range pair and
unsigned RNG remainder modulo 81 plus 80. The packet age is reloaded after
the growth RNG call before computing curve[12]; caching the earlier half
does not preserve a provider's retained packet mutation.

The following `func_151A24A8` consumes all fourteen cells. Nullable pointer
submission uses the return ABI restored in
[Note 2492](2492-game-packet-allocator-nullable-return-and-direct-match-20261115.md).
The parent fixture's independent expiry-slot 3 cases are distinct from update
slot 4 and do not assert that the factory's preserved -1 argument selects expiry 3.

## Source and checked normalization

Semantic C emits **314 words / frame 0x100**, raw SHA256
`6e18882e9bab689a0a1dda445dcabe08da660e1f27b2f37ca3640d4dfc9c4b1d`.
Signed16 peak/half and a signed32 quarter preserve the original narrow-value
operations without two redundant quarter extensions. A four-byte scratch
union shares disjoint integer RNG/angle and nullable result-pointer lifetimes;
no inactive member is read.

The first 18 frame/save words agree directly. The 56-byte packet is at incoming
SP-60, the 28-byte curve at SP-88, and cached randomized Z at SP-120. Raw C uses S2
for the state pointer, retail S0; both loop heads are at offset 0x104. The
whole-function relation checks all live roles and saved-state lifetimes.

All **314 source operations are conserved**. The projection changes only
register allocation, scheduling and branch displacement, adding three GPR
copies. No operations, memory offsets, literals, binding identities or branch
forms are removed or substituted. All **22 FP operations preserve their
ordered value operands and FCSR transitions**. There are **314 expected-word
guards / three insertions / zero omissions**. CSV rows carry emissions;
they are not per-row semantic operation origins.

## Qualification and fixture correction

Eight maintained `game_growth_curve_151a1fb4` files cover source, fitting,
guest/native, instruction relation and actual parent. From the prepared root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools.tests.test_game_growth_curve_151a1fb4_recovery -v
```

Fresh primary, isolated sibling-tools and installed primary runs each pass
all five tests, zero errors/failures/skips, at identical task fingerprints.
Actual imported helper origins are sealed. The sibling's existing 2,434
dirty paths and301 scoped helper bytes are unchanged; only the isolated task
overlay supplies the new files.

- The instruction relation covers **2 entry / 256 inductive loop paths**,
  all 300 normal raw words and 303 normal retail words. Only 14 BREAK instructions
  per stream lie outside its explicit normal nonzero-DIV/signed-overflow
  domain. Ordered FP/FCSR, public memory aliases in the model, every private
  frame byte at calls/return, retained passed-range mutation and saved GPR/FPR/RA
  agree. Incidental R2/R3 at return are checked too.
- Exact signed16 identities cover all 65,536 values times 32 shifts, 2,097,152
  pairs, plus 100,000 32-bit mask inputs. Independent-origin overflow,
  unbounded input and invalid shifts remain effective counterexamples.
- An independent T0/T1 allocation passes. Wrong private-gap writes, mode byte,
  curve cell and FP operand order are effective relation failures.
- Guest checks pass **3,840 cases per retail/raw/padded stream** with full
  packet/curve/public-memory/call comparison and exact exposed homes.
- Actual C passes **3,840 native32 cases each at O0/O2**, with UB/float-cast
  traps. Five changed-source controls exit 3: reset persistent flags, copy 26
  instead of 28 bytes, cache half before RNG, use the wrong growth range,
  or use the wrong position fraction. Native checks use defined fields;
  separate guest/proof checks cover private padding bytes.
- The original parent passes **256 cases per stream**, all 45 words and all
  eight update/expiry/free routes, including callback timer/slot reload,
  expiry rescue and signed timer wrap.
- Both complete owner padders preserve 38 neighbors and pools. All 314 raw-word
  and 21 binding corruptions, ten actual stale-CSV controls, and three
  independent provider/data rebases across HI/LO carries are checked.

The first private fixture repeated its eight RNG values exactly once per
emission, so its reset-flags negative was ineffective. That failed suite and
immutable 1,251-input snapshot remain under `adoption/`. The RNG now advances
its seed cycle each emission; `adoption-v2/` has a fresh immutable baseline
and all five negative controls fail as required. No failed receipt is credited
and neither earlier snapshot nor any predecessor freeze was overwritten.

This is normal, nonfaulting compiled-instruction evidence, not a claim that
every abstract C input is defined or that hardware/gameplay acceptance passed.
No Claude call was needed for this routine recovery.

## Linked image and production

The accepted immutable **1,251-input** baseline begins at consumer `f54185be` /
tools `ab30be5c`. Only four installed inputs change: owner source, guard CSV,
owner object and ELF; the other 1,247 remain exact. Older 895/1235/1243 freezes
and their explicit overlays, plus the failed first packet, remain preserved.

The independent five-command real Make shadow agrees for all 39 owner raw
functions and predicts the complete production image. The literal audit
explains **901 ELF byte changes with zero exclusions and no metadata permutation**.
All other 6,050 bodies and every function address stay fixed. Only one of 698
production objects changes. All **189,088 protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Source and guards are installed before actual production Make generates the
object/ELF, without copying prebuilt objects. The production ELF equals the
independent prediction byte-for-byte, SHA256
`defe443a186bf250ea57168c81f9e5c73a9f3f1a3500719de025d65e96c3f92c`.
Production progress and project-tool checks pass. Earlier whole-owner receipts remain historical; unchanged neighbor
semantics are reused only with fresh raw/padded/pool and full-image identity.

Receipts: `conker/build/game-next-151a1fb4-private/adoption-v2/`.
Root README changes only its Total/Game aggregate rows and verification date. Graphify uses a
retained-ID scoped AST merge, not a full-corpus extraction claim. Tools are
committed before consumer pin/source/docs. No push, host Release or save change
is included. Next candidate: `func_151A2F0C`; the wider 85% goal remains active.
