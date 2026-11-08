# Actor Effect Choice Switch Match - 2026-11-07

`func_15146970` replaces its zero-return placeholder with the complete nine-way
actor effect classifier. All **74 instruction words emit directly from C**,
including the original **48-byte frame**. Two relocation-only guards bind its
five-ID initializer to preserved retail data; they change no instruction word.
The switch table keeps its original retail owner and entries.

Fresh count: **4241/5512 = 76.94%**, Game **3568/4839 = 73.73%**,
Init 492/492, Debugger 181/181, zero drift. **169 more** exact functions reach
4410/5512 and 80%. The conversion denominator and progress CSV are unchanged.

## Function and caller recovery

Entry 15146970..15146A98, retail ROM 173E20..173F48, 296 bytes. Source:
`conker/src/game/generated_173D40.c`; normal IDO 5.3 O2/g3, MIPS2/O32.
Interface: `s32 func_15146970(s32 kind, u8 *actor)`.

| Kind | Result or action |
| --- | --- |
| 0, 2, 3, 4, 5 | Return the same integer |
| 1 | Return 1 outside world 4; in world 4, return 6 when the actor predicate is nonzero, otherwise 3 |
| 6 | Copy IDs 401D..4021, compute the signed actor index, and query all five; return -1 on lookup -1, otherwise 6 |
| 7, 8 | Return 15, 16 respectively |
| Other full-word selector | Return -1 |

The actor index uses 32-bit wrapped subtraction from D_800CC2D0, then signed
division by 0x32C with truncation toward zero. The ID words retain their high
flag bits; the original lookup performs its own low-12-bit extraction.

The whole retail image contains no direct JAL to this function, one entry
pointer at ROM22EB44 (D_8008A084 slot0), and exactly nine interior pointers in
its own switch table. `func_15141A7C` loads this classifier, passes the full-word
classification result and actor pointer, and consumes the s32 return. Its
complete 100-word linked body is literal checked; the original ten-word
indirect-call/return window executes in 13 focused cases. Its existing typed
`GameEffectClassifier` interface already agrees, so no caller/header edit.

## Direct emission, pools and whole-image proof

Predecessor consumer 349e5c9bb7fe8636462766b13a662791cbc2d491; tools
14e47f61963583f6c495acc2d74d8ee3bb4540a4. The preparation freezes 102
source/header/compiler/input files.

The initial external-structure copy has 74 words/frame48 but ten independent
scheduling differences. The natural five-element array initializer recovers
all original words, SHA-256
`33a60e3269401a1a71955da67358facfaa2a268a73ea6c22ed0a55ec7652b0bf`.
No schedule, register, frame or extent normalization is needed.

IDO emits a 32-byte initializer pool and a 48-byte switch pool. Their useful
contents are exactly five words at D_800A56D0 and nine R_MIPS_32 entries at
jtbl_800A56E4_game; each compiler pool has a separately checked 12-byte zero
alignment tail. Retail packs the 20 useful initializer bytes directly before
the switch. Independent GNU links use those useful extents with assembler
tail-padding disabled; retaining both compiler tails would overlap the pools.
The initial independent-link fixture caught that packing error and was fixed.

The existing padder uses a new owner-specific Makefile rodata anchor. Two
expected-word guards at +A8/+AC translate only initializer HI16/LO16 bindings
from `.data` to D_800A56D0, with expected and replacement words identical.
No compiler pool is appended to runtime data. Every prior allocatable pool
remains unchanged, and all new useful values, table targets and padding are
validated before the preserved retail owners are used. Effective corruptions
of an initializer value, initializer padding and switch target are rejected
while target instruction bytes remain unchanged.

All 12 raw/padded neighbors and their bindings remain unchanged. The strict
layout padder and assembly-slice padder agree on all 13 functions and pools.
The latter additionally retains nine original global case labels; every name,
address, zero extent, binding and section is explicitly accounted for. The
actual three-command Make recipe reproduces the qualified complete owner.

The independent whole-ELF prediction equals the actual production image after
**257 changed bytes, zero exclusions**:

- `.game`: 202 instruction bytes in this function only.
- `.symtab`: 23 bytes, comprising its size update and two named pair swaps.
- `.strtab`: 32 bytes from those exact, length-preserving name permutations.

The bounded permutations are D_800A56D0/D_80096214 at symbol offset2740844 and
func_151A0F28/D_8009D7C0 at2816700. Complete named definitions remain identical
except the target's 12-to-296-byte size. No metadata section is excluded.
All 6052 function addresses, every other linked body, and all 189088 protected
data bytes across 720 owners remain fixed. Guard history retains its complete
prior byte prefix and appends exactly two relocation-only rows.

## Qualification and limits

Both mounted and sibling configurations pass six fresh tests before and after
installation. The sibling run overlays only the three new modules, records
the existing missing-pool-helper fallback, and preserves all 2434 inherited
dirty paths. Both shared smoke checks are fresh; three unchanged shared
regressions per copy are explicitly reused by exact helper/test fingerprints.

| Check | Result |
| --- | --- |
| Independent guest model | 449 cases; all 74 target instructions reached; full literal state agrees |
| Original helpers | 34-word predicate and 110-word lookup control flow; mask/64-bit shift and collision paths exercised |
| Native32 | 345 valid-arena cases at each of O0/O2/O3, SDK widths, typed callback and trapping UBSan |
| Effective source negatives | Stub, byte selector, wrong world, positive-only predicate, wrong actor stride, ID, count and lookup sentinel |
| Executed access cuts | 74 literal-state comparisons |
| Independent GNU links | Original and rebased code, all ten code bindings, nine table entries, five initializer words and signed LO16 carry |
| Corruption controls | Raw words, all ten bindings, guard prefix, three compiler-pool corruptions and eight full-image corruptions rejected |

The native source uses valid actor-arena offsets and original initializer
constants. Arbitrary wrapped addresses, relocated initializer memory and
private/fault states are guest contracts. The original lookup's shift and
collision services are bounded provider models; their full hardware/gameplay
behavior is not claimed. `func_150A2AEC` remains a production placeholder:
executing its original ROM instructions for this qualification does not adopt
or credit it. The complete rendering/effect dispatcher is not runtime-qualified
by the bounded classifier window. Routine task: zero Claude calls.

Actual production Make emits one O2/g3 compiler invocation and no C warnings.
The duplicate generated_12D630 recipe warnings remain. `make all` reaches its
expected development-image checksum rejection; the ELF, binary and explicit
NON_MATCHING recount are independently verified.

Production ELF SHA-256:
`e04d595457a7e17046de946708ebc905988a0a19792e7a30d29a1bf87f0a89d7`.
Binary: `01231b07c33d0892f7ab2b2b0b9c133192073d6c3a5e0348d140b107d15f7f9c`.
Owner: `6944ec1751320d1e6228e63eea9bcfcdf669427894d0a14350d2b5d21d7dc52d`.

Reproduce from the consumer root under prepared WSL:
`python3 -m unittest tools.tests.test_game_actor_choice_15146970_match -v`.
Canonical receipts: `conker/build/game-actor-choice-15146970-match/`, including
`pool-controls.json`. Tools first, then source/Make binding/two guards/docs/pin
are committed locally. No push or host/frozen Release changes.

Next reconstruct `func_150A2AEC`: its original 110-word body and both lookup
paths now have connected evidence, but it still needs its own C/source/ABI,
caller, raw/padded owner, native, whole-image, actual Make and adoption gates.
Keep the full 80% goal active. The unresolved `func_1513FAB4` study remains
uninstalled and uncredited at [Note 2171](2171-game-triangle-facing-match-20261107.md).
