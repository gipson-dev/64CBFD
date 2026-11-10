# Game actor byte-selection guarded match - 2026-11-09

`func_15075650` now matches all **141 words / 564 bytes** with its natural
**0x20 frame**. Semantic C emits the complete 141-word body. Two expected-word
guards close one temporary actor-pointer register role; no insertion, omission,
source padding, compiler-profile change or shared declaration change.

Fresh actual-ELF totals: **4,299 / 5,513 (77.98%)**, Game **3,626 / 4,840
(74.92%)**, Init 492/492, Debugger 181/181, zero drift, **1,214** still different.
The active 80% goal needs **112** more accepted matches to 4,411/5,513.
README changes only the two aggregate rows.

## Recovered selection and publication

Owner `conker/src/game_A28B0.c`; VA 15075650..15075884,
ROM A2B00..A2D34. The no-argument, void function uses the current actor through
`D_800D154C` and the byte table pointer `D_800D2108`.

- Preserve the byte upper limit from table[id]-1, with a nonzero actor override.
  Compute a separate wrapped byte span after subtracting the actor minimum.
- Selector FF chooses an unsigned RNG remainder plus the live minimum. FE
  chooses similarly but rejects a byte predecessor; when current <= minimum,
  that predecessor is **upper limit - 1**, before span reduction.
- State 13 suppresses random selection, including a zero span. Other selector
  bytes are direct assignments. Retain retail's redundant unreachable FF arm.
- Clear state byte 223, publish halfword timer 21C as config byte *100, and
  update float 44 unless rate=255. Unit rate 1.0 becomes 0.5. Clamp current21E
  to minimum220, then call the original flag updater `func_15075498`.
- Preserve current-actor/minimum reloads after the RNG and pointer reloads after
  stores. The final helper updates signed halfword 244 and word F4.

Concrete old-source defect: table=11, no override, minimum=current=3, FE,
RNG=6 gives upper10/span7 and sampled9. Retail excludes9 and retains3; the
old C excludes6 and stores9. Recovered names `span`, `selection`, `excluded`
and `actor` replace the misleading phi names and the stale nonmatching comment.

## Compiler, guards and image scope

The old raw C body emitted139 words; the accepted source emits141. Natural
byte-variable, branch-edge and actor-local experiments recover139 of141 words
directly. The final two guards are:

| Byte offset | IDO | Retail | Meaning |
| --- | --- | --- | --- |
| 0x144 | 0x8D020000 | 0x8D030000 | Reload actor through t0 into v1 rather than v0 |
| 0x14C | 0xA0400223 | 0xA0600223 | Clear actor223 through that same pointer |

The intervening branch, its delay-slot store, effective address, width and all
relocations are unchanged. Both temporary values die before their next uses.
The normalizer requires the exact raw SHA, full141-word payload, owner,
function and17 relocation sites. It is not a general register substitution.

All210 raw and padded neighbors, owner pools and register-use metadata stay
fixed. The existing overflowing neighbor `func_150768DC` and retained assembly
`func_15079B30` are preserved by the ordinary owner route. No unrelated neighbor
is removed, repaired or excluded. Thirteen inherited CFE diagnostics remain
identical after line/path normalization; the target adds none.

Actual Make executes its five-command asm-processor/IDO/postprocess/pad/assemble
route and equals the independent padded-owner prediction. The separately
assembled target and both target padding routes agree with original assembly.
Strict whole-ELF prediction accounts for **459 changed bytes**, entirely this
slot and size metadata556->564, with **zero unexplained bytes or exclusions**.
All6051 linked function addresses stay fixed; all189088 protected data bytes
across720 owners remain exact. Guard history is an unchanged prefix plus two
rows; conversion CSV and Makefile are unchanged.

## Fresh behavior and caller evidence

The six-check target suite passes before and after installation in the mounted
tools checkout and a read-only overlay using sibling tools helpers. The sibling's
2439 dirty paths and its existing files are preserved. Exactly fingerprinted
shared regression receipts are reused explicitly; shared smoke checks are fresh
in both environments. Claude calls:0; routine compiler/model evidence suffices.

- Guest: **5536 executions/body**, **16608 total**, across raw, normalized and
  original bodies; **4662 trap-prefix executions**,72 independent rebases.
  All selector, rate and flag bytes, wrapped spans, overrides, lock states,
  unsigned RNG extremes, call mutations, live reloads, stack-home mutations
  and a physical rate/pointer alias are exercised.
- The original18-word RNG, including its64-bit GPR/seed operations, and the
  original44-word flag helper are byte-verified and connected. The RNG remains
  handwritten assembly and receives no new C credit. Scripted call mutations
  are labeled extensions. Zero-divisor checks stop at retail `break 7`, with
  three explicit opaque DIVU-zero HI values; undefined native division is excluded.
- Normal/trap entry reaches134 of141 words in each body. Unreachable indices
  **84,87,88,89,111,112,113** are preserved statically: redundant FF code and
  unsigned-byte float correction. No full dynamic-word coverage claim.
- Native SDK32: **3961 defined cases/profile**, O0/O2/O3 with UBSan traps;
  full actor fields, retained bytes and canaries match an independent model.
  Twelve effective semantic controls are rejected at each profile. Physical
  guest aliases and incoming-frame mutations are excluded from portable C claims.
- IDO:12 independently compiled effective source controls. Both padders reject
  four stale expected-word/relocation guards each;141 corrupt payloads and six
  whole-image corruptions are rejected. Four actual GNU rebases execute48 cases.
  Compiler/interpreter/sanitizer errors are never credited as semantic witnesses.
- All three direct callers are already exact C wrappers: `func_15075B8C`,
  `func_150761C8`, `func_150779A8`. Their full33 original words execute in648
  cases across all three target bodies, preserving O32 saved state and reloading
  the actor after the call before setting state10/5/11. Fresh ROM JALs are at
  A3044/A3680/A4E60; there are no direct tail jumps.
- One aligned literal pointer occurs at ROM22B388, VA800868C8 in protected data;
  its surrounding bytes are uniquely located in the predecessor ELF and remain
  unchanged. The indirect dispatcher itself is not claimed executed.

Fixture corrections were validated before acceptance: the first private actor
map overlapped the inherited stack address; it was relocated to distinct arenas.
Native initial halfwords were initialized explicitly across host endianness.
An ineffective wide-comparison control was discarded because the final minimum
clamp masked its final-state effect; the accepted control set has12 actual
semantic witnesses. These were test issues, with no installed source change.

## Banking and continuation

The ordinary `make all` checksum exit2 and duplicate generated_12D630 recipe
warnings are inherited. Target ELF, independent image, recount and data gates
pass. This is retail static/guest/native qualification, not hardware or host
gameplay acceptance. The separate host port and frozen Release are untouched.

Graphify refresh is scoped to this owner and six new tools modules, retaining
old nodes outside changed paths. All210 active C source locations and the one
retained assembly function are audited; excluded existing corpus nodes remain
retained, with no full-corpus semantic extraction claim. Tools commit precedes
the consumer source/docs/guard/pin commit. Local commits only; no push.

Ignored evidence: `conker/build/game-actor-selection-15075650-match/` contains
687 frozen inputs, shape/layout/register probes, normalization/qualification,
guest/native/control/caller receipts, both pre/post environment logs, production
hashes/recount, graph retention, review diffs and final handoff.

Next: `func_150450CC` in `conker/src/game/generated_71820.c`,144 retail words.
Fresh screening still finds76 real differences. Inspect its complete retail
routine, caller interface and compiler shape from the new bank before probing.
The hard private `func_1510D404` candidate stays uncredited. Keep the80% goal open.
