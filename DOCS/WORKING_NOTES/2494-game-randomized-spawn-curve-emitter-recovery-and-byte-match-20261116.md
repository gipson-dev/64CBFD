# Randomized spawn curve emitter recovery and byte match - 2026-11-16

`func_151A1998` now has a complete typed C recovery and matches all **295
retail words / frame 0xF0**, VA `0x151A1998..0x151A1E34`, ROM
`0x1CEE48..0x1CF2E4`. It replaces the zero-return placeholder with the actual
randomized particle emitter and its curve of ten signed shorts.

The production recount is **4,517 / 5,514 (81.92%)**, Game
**3,844 / 4,841 (79.41%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, 997 different. This adds **one qualified match**; the
active 85% goal needs **170** more at this denominator. Conversion remains
5,514 / 6,048 (91.17%), covering 86.19% of function bytes.

## Behavior and actual interface

The signature is `void func_151A1998(struct260 *record)`, matching the
`D_8008A4E8[3]` update callback under the actual 45-word `func_15149264`.
The table pointer is VA `0x8008A4F4`, ROM `0x22EFB4`. The unchanged preceding
factory `func_151A18DC` selects update index3 and captures a 32-byte payload
with initial phase zero. This is distinct from the preceding slot2 emitter
and the following `func_151A1EE8` factory's index4/36-byte payload.

The function advances phase by rate times `D_800BE9A4`, emitting while phase
is strictly greater than1. Every emission keeps six integer RNG calls, four
trigonometric samples, one real RNG sample, packet submission and an optional
20-byte curve copy. The target coordinates are randomized spawn positions;
there is no velocity curve as in the preceding `func_151A11E4` recovery.

The 56-byte submission packet uses fractionScale17, flags0xC0001, a persistent
curve-flags word and the descriptor `D_80090D34`. The two random flag bits
accumulate across emissions and opaque calls may retain/mutate the passed
packet and curve. Coordinates are captured before later RNG providers can
change the record; lifetime/size ranges, mode and owner are read at their
original boundaries. Two unsigned remainder operations and five signed
divisions build the intensity and size ramps. A nullable pointer return
controls the exact20-byte copy to `created+0x50`; phase is then reloaded and
decremented before the next strict comparison.

The helper pointer-return prerequisite was restored in
[Note2492](2492-game-packet-allocator-nullable-return-and-direct-match-20261115.md).
The unchanged following `func_151A1E34` consumes these ten shorts. Parent
fixtures also exercise independent expiry-slot3 cases; they do not infer that
the preserved factory's `-1` argument selects expiry3.

## Source shape and guarded normalization

Semantic C emits **293 words / frame0xF0**, raw SHA256
`d5d581559adcd98843454bad34ba42d162dca050b2995163847d00a43930c797`.
Named signed16 half/quarter values recover the ordered FP schedule. A
four-byte scratch union shares genuinely disjoint angle/RNG and nullable
pointer-result lifetimes without reading an inactive member. It avoids an
extra eight-byte frame while retaining the original typed calculations.

The first17 frame/save words match retail directly. Packet56bytes is at
incomingSP-60, curve20bytes at -80 and cached randomized Z at -112. Raw code
uses S2 for the state pointer and loop head0x108, versus retail S0/0x104;
the instruction relation explicitly relates these live roles.

The projection conserves every source operation except one path-exclusive
saved-RA restore coalesced into the common restore epilogue. It changes the
prefix branch from likely to ordinary with that common return, adds two GPR
copies and reloads the freshly stored signed half-lifetime curve cell.
All other opcodes, literals, memory offsets and binding identities are
conserved under allocation/scheduling. All **22 FP operations preserve their
value operands, order and FCSR evolution**; no FP reordering is accepted.

There are **293 expected-word guards, three insertions and one omission**.
CSV rows are output carriers, not per-row semantic operation origins. The
independent full-function relation establishes the correctness of CFG/RA
coalescing and signed-short reuse. Both complete owner padders emit all295
original words/bindings and preserve all38 other functions and constant pools.

## Qualification

Eight maintained files use `game_spawn_curve_151a1998` under
`tools/experiments` and `tools/tests`. From the prepared consumer root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools.tests.test_game_spawn_curve_151a1998_recovery -v
```

Fresh primary, isolated sibling-tools and installed primary runs each passed
all five tests with zero failures/errors/skips, using identical task-file
fingerprints and retained actual imported-helper origins. The sibling's
2,434 dirty paths, HEAD/status digest and301 scoped helper files were unchanged;
the task overlay did not write into that checkout.

- The instruction relation covers **2 entry / 256 inductive loop paths**,
  all281 normal raw and283 normal retail words. Its explicit normal-DIV
  domain excludes only the12 BREAK instructions per stream. It compares
  ordered FP/FCSR, provider arguments/effects, arbitrary public aliases in
  the model, saved GPR/FPR/RA, full private frame at every provider and return,
  retained passed-range mutation and incidental return R2/R3.
- Exact integer canonical identities were checked on all65,536 signed16
  values and32 shift amounts (2,097,152 single-origin pairs), plus100,000
  32-bit mask inputs. Independent-origin overflow, unbounded values and
  invalid shifts remain effective counterexamples. The identities combine
  an equivalent quarter predicate; no reachable normal instruction is dropped.
- An independent T0/T1 allocation passes. Wrong private-gap writes, mode
  byte offset, curve threshold cell and FP operand order are rejected as
  actual relation differences, not unsupported instructions or timeouts.
- Guest checks run **1,920 cases per retail/raw/padded stream**, comparing
  complete packet/curve bytes, exposed homes, calls and public memory.
- The actual C passes **1,920 native32 cases at each of O0/O2** with UB and
  float-cast traps. Resetting persistent flags, copying18bytes instead of20
  and using the wrong position fraction are effective failures. Native
  comparisons use defined fields; guest/proof evidence covers padding bytes.
- The original parent runs **256 cases per stream**, all45 words and all
  eight update/expiry/free combinations, including callback timer/slot
  reload, expiry rescue and signed timer wrap.
- Both actual owner padders,293 raw-word and19 binding corruptions, and
  ten real stale-CSV controls pass. The omitted RA row is checked too.
  Three independent symbol maps move providers/data across HI/LO carries;
  raw and padded whole-function relations pass under each map.

The proof concerns normal, nonfaulting compiled instruction execution, not a
claim that every abstract C input is defined. It excludes code/return-PC or
unpassed-local inspection. These tests do not establish hardware fault or
gameplay acceptance. One bounded, tools-disabled advisory supplied a shift
lifetime hypothesis; Codex compiled and independently qualified the result.

## Linked image and production audit

A new immutable **1,243-input** baseline starts at consumer189da39a and
tools c122ab4f. Both older895/1235 snapshots and their adoption overlays remain
untouched. Only four frozen input paths change: owner source, guard CSV,
the owner object and linked ELF. The other1,239 frozen inputs remain exact.

An independent five-command real Make shadow agrees with direct compilation
for all39 owner functions. The literal whole-image predictor explains
**846 ELF byte changes with zero exclusions and no metadata permutation**:
the target slot and its12-to1180-byte function-size metadata. All other6,050
linked bodies and every address remain unchanged. Of698 production objects,
only `generated_1CC440.c.o` changes. Source conversion classifications do not.

All **189,088 protected bytes / 720 owners** stay exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Source and guards were installed first; actual production Make generated the
object/ELF, without copying prebuilt objects. The result equals the predicted
ELF byte-for-byte. Production progress and project-tool checks also pass.

Production ELF SHA256:
`ef4f22fe09f1169be3288bce106d8cbc08f8fe5175fb037bac73bb483db53b06`.

Private receipts are retained under
`conker/build/game-next-151a1998-private/adoption/`. Earlier whole-owner
receipts remain historical; unchanged neighbor semantics are reused only
with their exact raw/padded/pool fingerprints and this fresh complete image
audit. No older whole-owner pin was weakened or silently re-frozen.

Detailed updates remain in this note and concise indexes. Root README changes
only its Total/Game aggregate rows. Graphify uses a retained-ID scoped AST
refresh, not a full-corpus extraction claim. Tools are banked before the
consumer pin/source/docs. No push or host Release/save changes are included.
Next candidate: `func_151A1FB4`; the wider85% matching goal remains active.
