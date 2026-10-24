# Four Character Effect Pairs Direct C Match

Date: 2026-10-24. Consumer predecessor `3b50daeb`; tools predecessor
`af5ead1e`. Qualification tools committed first as
`7ed14440b7c2efb3b6e6788bd39179b5e8bd2ffc`. No push requested/performed.

## Recovered Family

Owner: `conker/src/game/generated_179F30.c`. Four related callbacks each
emit their complete 176-byte / 44-word body, frame 48, six bindings,
directly from semantic C. No new instruction guards, profile changes,
insertions, omissions or alignment-tail substitutions.

| Function | VA Start | ROM Start | Descriptor | Attachment Key | Table Slot |
| --- | --- | --- | --- | --- | --- |
| `func_1514E508` | `0x1514E508` | `0x17B9B8` | `D_800A58D0` | `0xD` | 6 |
| `func_1514E5B8` | `0x1514E5B8` | `0x17BA68` | `D_800A58E4` | `0xD` | 4 |
| `func_1514E668` | `0x1514E668` | `0x17BB18` | `D_800A58F8` | `0xD` | 5 |
| `func_1514E718` | `0x1514E718` | `0x17BBC8` | `D_800A590C` | `0xE` | 7 |

The descriptor strings in `asm/data/24A360.rodata.s` identify character
effects 0, -1, 1 and 2, respectively. Keep canonical function/symbol names
and add a short semantic comment; do not rename guessed internal APIs.

Use the actual one-pointer, void callback interface. Each routine:

1. Calls `func_1518D1C0(owner, 5, 0, 1, 255, 1, descriptor)`.
2. Attaches the returned word using `func_1514EC1C(result, owner, key)`,
   including when the factory returns zero.
3. Forms owner+0x14, passes its arithmetic signed high half and unsigned
   low half to `func_1515D5F8(-32768, high, low, 5, 255, 255, 255, 255, 0, 0)`.
4. Attaches that returned word with key 0x18, again unconditionally.

Preserve the incoming owner-home reload after each helper, full-width
factory returns, exact call order and both NULL-result paths. The unused
attachment return does not become the callback's C return contract.

Shared declarations recover the factory's existing local pointer/word/byte
interface and the companion's ten arguments. Add explicit pointer casts to
the two existing `func_1518D1C0` call sites in `func_1514E7C8` and
`func_1514F44C`; all their emitted code remains byte-identical. Keep existing
owner diagnostics unchanged after normalizing shifted source line numbers.
No cross-project headers or helper definitions change.

Raw C SHA-256, first three callbacks:
`993aa0814e41ba7afeb4b07c677ccef9d34a9f0f4257e549245414a256a05f50`.
The descriptor bindings differ even though those raw relocation words agree.
Fourth callback raw SHA-256:
`c2469f13e6cf4619b6feef76437d3e692de2c64293586d2445728e0e9cb9d769`.
Bindings: descriptor HI16/LO16 at +0xC/+0x10, factory JAL +0x34,
attachment JAL +0x44, companion JAL +0x88 and attachment JAL +0x98.

## Caller And Helper Boundaries

The sole aligned literal reference for each callback is its listed slot in
the 23-entry `D_8008AA70` table, ROM `0x22F530`. No aligned direct target JALs
occur. The four pointer slots are `0x8008AA88`, `0x8008AA80`, `0x8008AA84`
and `0x8008AA8C`, in function order above.

Original parent `func_1514D15C` has three relevant indirect-call windows:
`0x1514D230..0x1514D270`, `0x1514D270..0x1514D2AC` and
`0x1514D2AC..0x1514D2F8`, with the final NULL path ending at 0x1514D2FC.
Execute those original windows with the actual table entries, both stack
phases, gates and zero selectors. The boundary markers stop before synthetic
instructions execute. This is original caller-window qualification, not a
complete parent execution or native C-parent recovery: its live C remains
the existing zero-return placeholder, unchanged and uncredited.

Execute all 49 words of original `func_1514EC1C`: NULL input, node-allocation
success/failure, empty/nonempty old head, keys 13/14/24 and destructor
selection -1/0/2. Verify insertion stores, head/prev updates, cleanup calls
and returned node. Its current live C still returns zero; this match neither
reconstructs it nor claims working live attachment/list closure.

`func_1515D5F8` remains original assembly in `generated_18A8F0.c`, already
byte-exact across all 41 words. Exercise both lower-allocation outcomes,
every emitted byte/halfword, all four color bytes and returned word.
`func_1515D520` is an explicit bounded provider here.

`func_1518D1C0` remains its existing typed C placeholder. Its observed retail
entry/argument handling and local declaration establish the call interface,
not a recovered native factory pipeline. Native callback tests use bounded
C probes for the factory, attachment and companion. Keep these boundaries
visible: no new helper credit, full heap/effect closure, hardware or gameplay
acceptance is inferred from the four callback matches.

## Focused Qualification

Both tools copies pass eight fresh tests before and after installation,
zero errors/failures/skips, no reused checks. Primary/mirror pre-install:
11.619s / 11.317s; installed: 12.903s / 13.873s. Both shared project tools
checks exit zero. Reuse the proven MIPS interpreter, frame/fault tracking,
native compiler flags and object parsers.

- 9,600 guest phases cover all four complete bodies, boundary owner words,
  carry across the signed address boundary, zero/poison/full-width helper
  returns, ordered calls, caller-saved clobbers and late incoming-home
  mutations. All 176 root words are visited. Private guest-home aliases
  are not claimed to be portable native C.
- Native32 O0/O2/O3 with trap UBSan: 786,432 selected cases per function
  per optimization, or 3,145,728 across the family. Use real allocated
  buffers, every low-half offset, four NULL-result modes, and mappings on
  both sides of the signed address boundary. Twelve defined wrong-C controls
  per function fail effectively, including a logical instead of arithmetic
  high-half shift. Invoke the actual recovered C through callback pointers;
  do not claim execution of the unrecovered C parent or factory.
- 96 original caller-window phases validate each registration, both gate
  states, zero selectors and callback arguments. Other parent paths are
  outside this bounded claim.
- 74 helper phases visit all 49 original attachment words and all 41 retained
  companion words, with independent expected stores/returns/provider calls.
- 36 independent GNU links cover original, qualified padded and actual Make
  objects at three placements per callback. 384 rebase phases include
  HI16/LO16 carry boundaries. All 256 fired root-access prefixes preserve
  complete state, PC and delay origin. Eleven strict-image corruptions and
  a bounded metadata-order corruption are rejected.

Initial fixture failures were corrected before adoption: a helper result
buffer unintentionally occupied guest STACK, one caller window needed its
incoming V0 flags, and callback returns needed a nonexecuted boundary marker
present in the code map. The native ELF entry had no C caller and therefore
needed explicit stack realignment before optimized SSE code. Apply
`force_align_arg_pointer` only to that disposable entry wrapper; do not
disable UBSan, alter recovered C or weaken the assertions.

## Production And Preservation

The complete 78-function owner preserves all 74 non-target raw/padded
bodies and owner pools, including the two explicitly cast legacy calls.
Actual shadow Make uses the ordinary three commands and IDO `-O2 -g3`;
its entire padded object equals the independently qualified object.
The isolated callback diagnostics are empty; inherited owner warnings are
unchanged, not silently treated as new warnings.

Seal 15,930 initial native files and add the two owned qualification files
in both tools copies: 15,934 files / 33 focused inputs. Cover all 1,454
linker objects. Verify every static/non-target byte in both Linux cache and
native checkout, allowing only source, target object and ELF overrides.
Use checked native streams, not project reads through DrvFS.

The entire independent ELF prediction and production image agree exactly:
624 changed bytes = 544 target-code bytes + 80 metadata bytes. Four metadata
bytes update the target extents from 12 to 176 bytes. The other 76 account
for three bounded symbol/string-order rotations, without changing named
definitions, values, types or section ownership:

- `D_800A58E4`, `D_80097BB4`.
- `D_800A58F8`, `func_1507B8F4`, `D_80097BC8`.
- `D_800A590C`, `D_800A1B5C`, `D_800A5E5C`.

Pin each original contiguous group, rotate left once, rebuild only its
symbol/string serialization and verify canonical named definitions remain
identical. Do not ignore the symbol table or accept arbitrary metadata.
There are zero image exclusions. All other 6,051 bodies, every one of
6,055 addresses and protected Game data remain fixed: 720 owners / 189,088
bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The entire historical guard CSV is byte-identical; no rows are added.

Production Make exits zero in 0.573s and reproduces the independently
predicted image and complete object. Run both eight-test installed suites,
then audit all 15,934 native manifest entries before/after adopting the exact
generated outputs. Recapture the actual adopted live ELF for a fresh recount.

Installed ELF SHA-256:
`347ed481fc3d8f167970c2dad5436f5840fddf604604d5cb90b6aa70ed64c290`.
Installed object SHA-256:
`5beb6155c86833d4365696a8bd1959b356e31ddef5b57cba3a853567ff839679`.

Preserve all 1,594 previous dirty older-mirror paths, statuses, hashes and
HEAD; only the two owned files are added there, leaving 1,596 dirty paths.
Do not reset or commit that independent mirror. Host Release, saves,
configuration, private ROM inputs, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,767 / 5,505 (68.43%) | 0 | 1,738 |
| Game | 3,094 / 4,832 (64.03%) | 0 | 1,738 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove exactly these four functions from the live-ELF-pinned remaining queue.
Remaining source screens: 1,607 placeholders, 122 semantic/other definitions
and nine parser-unlocated entries. `func_1510D8C0` is actually existing
`Gfx *` C missed by that simple parser; its private screen and
`func_1518C850` remain unmatched/uncredited. Continue the 44-word queue and
keep the 862-word `func_1508CAD8` stub separate.

The 75% target remains 4,129 exact C functions: 362 more, goal not complete.
The root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify worker receipts and audit changed-file indexing and
all old-node retention without forcing a reduced-corpus rebuild.

Ignored evidence: `conker/build/game-character-effect-pair/qualified/`.
Tools: `tools/experiments/game_character_effect_pair.py` and
`tools/tests/test_game_character_effect_pair.py`.
