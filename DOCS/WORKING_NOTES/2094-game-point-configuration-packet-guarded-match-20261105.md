# Position configuration packet wrapper recovered

Date: 2026-11-05. Target `func_1513A48C`, owner `game_161520`.
Source `conker/src/game_161520.c`; original
`conker/asm/nonmatchings/game_161520/func_1513A48C.s`.

## Outcome and scope

The recovered C passes all nine private and nine fresh installed checks.
Actual Make and the literal complete-image predictor agree byte for byte;
the fresh installed nine-test suite passes in **132.718 seconds**.

The complete slot is 66 words / 264 bytes at VA
`0x1513A48C..0x1513A594`, ROM `0x16793C..0x167A44`. It has frame104,
thirteen bindings and no alignment tail. Sixteen expected-word corrections
derive from two instruction permutations; there are no added or omitted
instructions, frame changes, compiler-profile changes or shared-header edits.
All 63 primary compact neighbors, 64 padded neighbors, their bindings and
normalized pools remain fixed. The extra padded function comes from the
existing `func_15138BC0` translation-unit override.

## Recovered packet and interface

The interface is `void(Position161520 *position, u8 channel, s32 context)`.
The routine submits a local 60-byte configuration to `func_15152190`:

| Packet offset | Width | Value |
| --- | --- | --- |
| `+0x00` | word | Count 8 |
| `+0x04` | word | Count range 4 |
| `+0x08..+0x10` | three words | Copied input position, preserving float bits |
| `+0x14` | signed halfword | Angle 0 |
| `+0x16` | signed halfword | Angle range 255 |
| `+0x18` | signed halfword | Pitch -55 |
| `+0x1A` | signed halfword | Pitch range 32 |
| `+0x1C` | float | Speed 10.0 |
| `+0x20` | float | Speed range 9.0 |
| `+0x24` | float bits | `D_800A4954` |
| `+0x28` | float bits | `D_800A4958` |
| `+0x2C` | signed halfword | Lifetime 40 |
| `+0x2E` | signed halfword | Lifetime range 20 |
| `+0x30` and `+0x34` | float bits | One captured `D_800A4950` value |
| `+0x38` | float bits | `D_800A495C` |

The eight-argument handoff is packet, `&D_800A4260`, `&D_800A4264`, one
selector/scale entry, float zero, mode1, the unsigned channel byte and the
full context word. These are global selector/scale pointers, not copied
locals. The function reloads the channel from the low byte of its incoming
argument home. The provider may mutate the packet, globals and input point;
there is no subsequent packet or position read in this wrapper. Both actual
callers ignore the provider's returned V0.

The packet structure reuses the field layout already recovered for
`func_1519EA78`, with local type names for this owner. Its layout and this
routine's distinct values are checked independently. The input is copied by
three word loads/stores, so zero, signed zero, subnormal, finite, infinity
and NaN bit patterns are transported without floating arithmetic.

## Scheduling derivation

Natural O2/g3 already produces 66 words and the retail frame. A named local
captures `D_800A4950` once before constructing the packet. Fourteen bounded
source/profile screens were attempted, including declaration order,
register/const locals, same-line statements and a volatile read. The volatile
read grows to 67 words; O2 without g3 emits 65. The O1 whole-owner processor
route is unsupported and stops before compilation. A const-position variant
also fails against the existing typed owner prototype. These are private screens,
not accepted profiles or matching credit.

The accepted normalizer preserves every instruction and derives only these
closed destination/source index permutations (zero-based word indices):

| Destination indices | Source indices | Purpose |
| --- | --- | --- |
| `1..9` | `6,9,1,2,3,4,5,7,8` | Read the scale snapshot before argument homes and saved RA |
| `46..52` | `51,52,46,47,48,49,50` | Store both captured scale fields before independent outgoing setup |

The complete normalized object is compared against all retail words after
masking only explicitly bound relocation fields. The first permutation moves
the scale HI16/LO16 from `+0x18/+0x24` to `+0x04/+0x08`. The second moves
`D_800A4264`'s LO16 from `+0xBC` to `+0xC4` and `D_800A4260`'s LO16 from
`+0xC0` to `+0xC8`. The thirteen complete bindings are checked before and
after padding; relocation metadata moves with each instruction.

Ordinary source inputs agree for natural and fitted bodies. Artificial
aliases between external symbols and compiler-private homes can distinguish
the natural scheduling. Those aliases and fired fault prefixes qualify the
original/fitted instructions only. They are not claims of portable C fault
semantics or natural private-stack alias parity.

## Callers and bounded original callee

An aligned census of the entire prepared retail code binary finds exactly
two direct calls at ROM `0x1643E8` and `0x164EA0`, with no pointer literal or
tail jump to this entry. The original caller windows are:

* `func_15136C3C`: VA `0x15136EEC..0x15136F44`, including its gate,
  alternate-effect route, copied position at parent SP+`0xAC`, channel load,
  context load in the JAL delay slot and post-call saved-RA load.
* `func_1513783C`: VA `0x151379C4..0x151379F8`, including its table-byte
  gate, position at parent SP+`0xD4`, channel/context loads and saved-byte
  store in the JAL delay slot. The skipped route ends at `0x15137C4C`.

Twenty-four cases per body cover both windows, both stack phases, skip,
alternate and taken routes, and two independent provider returns. Boundary
markers end at the named retail control-flow points; this does not qualify
the complete parent functions.

Six connected runs also execute the original callee's first 56 words,
VA `0x15152190..0x15152270`, through its first random-number call, including
the delay slot. The actual initialization consumes mode1 from the outgoing
home and builds its `0x1029E8` flags. The complete random particle loop is
outside this wrapper's qualification. `func_15152190` remains an explicit
unrecovered zero-return C placeholder; no full provider behavior, audio,
graphics, host-port gameplay or hardware acceptance is added here.

## Focused checks and negative controls

All nine pre-install tests pass in **77.726 seconds**:

* 720 cases for each of retail, natural C and fitted bodies, checking all
  66 reachable words, complete packets, pointer arguments, context widths,
  provider mutations and arbitrary returned V0.
* 2,560 further cases per original/fitted body cover every channel byte and
  ten raw float patterns, including input/global overlap.
* 80 private-stack/global aliases compare complete original/fitted states;
  the alias programs are independently rebound to each selected layout.
* 111 fired access prefixes compare original/fitted partial state and trace.
* Both original caller windows and the original callee prefix described above.
* Nine GNU links across three independent layouts exercise all thirteen
  bindings, both HI/LO carry directions and moved relocation sites; 36
  rebased original/fitted cases check packet values and provider effects.
* 15,360 native32 positive executions across O0/O2/O3 use direct and typed
  indirect calls, all channel bytes, packet-layout assertions, raw float
  transport and provider mutations. Eight distinct native controls fail.
* The same eight changed semantic bodies compile with IDO and each produces
  a guest counterexample: count, pitch, scale source, channel, mode, context,
  scale pointer and position copy. No ineffective control is credited.
* Every one of 264 target-byte changes and thirteen bad bindings is rejected.
  Sixteen wrong expected-word preimages fail through the actual special
  owner padder. Five complete-ELF corruptions, including symbol/string
  bookkeeping, fail the literal image predictor.

The shared nineteen padder, relocation, matching and data-layout checks pass
in **9.777 seconds**. `make tools-check` passes. Old neighbor suites are
reused only through unchanged object bytes, bindings and pools, not claimed
as freshly executed. The initial failed run exposed fixture corrections:
the mutation expectation needed to distinguish a global input alias; alias
programs needed actual rebinding; caller return boundaries needed code-map
entries; and the callee prefix needed its final delay word. Production C was
not changed to bypass those failures.

## Complete-image and owner audit

The special owner recipe retains its original selector rodata binding
`jtbl_800A4350_game` and typed `func_15138BC0` override. Both are compiled
and used by the qualification padder, then checked against the production
recipe. The qualified ELF has exactly one changed body and all 6,052
function addresses fixed. All 189,088 protected Game bytes across 720 owners
are exact. The literal complete-file prediction changes 310 bytes with no
excluded section, symbol or metadata.

Seven closed symbol-pair permutations arise from GNU-ld hash serialization:

| First predecessor name | Second predecessor name | First symbol-record offset |
| --- | --- | --- |
| `D_800A495C` | `D_800A045C` | `0x29D50C` |
| `D_800A4260` | `D_8009F0B0` | `0x2A357C` |
| `.L1514CC14_game_data` | `D_8009E5B0` | `0x2A39CC` |
| `D_800990B0` | `D_8009E5E0` | `0x2CA10C` |
| `D_800A4958` | `D_800A0458` | `0x2D1A7C` |
| `D_800A4950` | `D_800A0450` | `0x2D56DC` |
| `D_800A4954` | `D_800A0454` | `0x2D5E9C` |

Each pair swaps complete records and names reconstructed from the pinned
predecessor. The unequal-length local-label pair also moves the second
`st_name` inside its unchanged combined string interval. Every named symbol
retains its value, size, binding and section identity; this is bookkeeping,
not a code guard or a metadata exclusion.

## Fingerprints and retained scope

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `18262aef893cab06c15b31b0935825ddd158ed6574993b752b66456b7c9df73b` |
| Retail target | `c4afdd83fa086c8d6bc121a3f216001a33f5b70399683c0471e7d5859bb2db3d` |
| Frozen predecessor ELF | `426d61d5a54e30dffc620cd594ba46e49d11042889663ef9fb24295bc0ada0fc` |
| Qualified padded owner | `abf6d16873cacfb3d04532043edd8d8583ee7add26c0fc74fad02d4bb7b3853a` |
| Qualified complete ELF | `743cca9727fe79f2058b52f709599e21ee5ea32a28647a72ba8582124f89b95a` |
| Production code binary | `98a64a347a2a37aebb296ca89f4c9803417530672d7e31e16c3295558a2e3fbf` |
| Guard CSV working bytes after sixteen rows | `7e5de67365676f7f3b163f60e83d1a2741b4275f6f9bf4fed372446e0648a687` |

Ignored artifacts are retained under
`conker/build/game-point-configuration-1513A48C-match/`, with adjacent private
candidate screens. The immutable input snapshot contains 96 files, including
retail code, complete headers, original target/callers/callee, layout,
Makefile, guard history, owner object, ELF, code binary and graph.

Main baseline is `c9eff9b5d4a6e544f042a028baf3f9bbd1dfccce`; mounted tools
baseline is `07974169b42b61e52aff2faf03183752b424c663`. Both were clean before
this work. The separate sibling tools checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked edits and 2,428
untracked files. It is untouched; no fresh sibling-copy qualification is
claimed. No host-port source, frozen Release output or private input changes.

## Production and continuation

The four-job actual Make rebuild returns zero. The complete production ELF
equals the independent 310-byte prediction: 212 target/extent bytes and 98
named symbol/string serialization bytes, with no exclusions. Its owner is
byte-identical to the qualified special-recipe object. The old guard file is
an exact byte prefix plus sixteen rows; frozen headers, retail input, layout,
Makefile, linker script, effect override and original assembly remain fixed.
Inherited owner pointer/integer warnings, SDK warnings and the duplicate
`generated_12D630` recipe warning remain; no new target warning is introduced.

`make -C conker all` generates the code binary and returns 2 solely at the
expected overall retail SHA mismatch for the incomplete decompilation. The
fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,165 / 5,512 | 75.56% | 0 | 1,347 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,492 / 4,839 | 72.16% | 0 | 1,347 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046. Root README changes are aggregate rows
only; the recovery narrative belongs here. The 80% threshold is 4,410/5,512,
leaving 245 more exact functions. Actual production ranking selects
`func_15146D60`, 73 words and 65 real differences, as the next ordinary target.
Retain `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC` and `func_150A6760` as separate boundary cases.

The standard Graphify update refused a reduced 24,887-node extraction against
the existing 58,677-node graph, preserving the larger graph. The eight-path
scoped refresh retains 58,674 old nodes, relocates three existing
`DOCS/UPDATE_LOG.md` headings and adds ten headings from this note plus the
`Position161520` type node: 58,688 nodes, 112,446 links and 5,127 communities.
No node outside the changed paths is removed. The retention receipt records
SHA-256 `ef8be5c7e79fcc90cc7f9d2d826d7697077da1e677e45a90dac2a22420eb5afd`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. The ignored receipt is `graph-retention.json` in the qualification
directory.

Mounted tools are committed first as
`80d906d441e5215c3afbd0d2fc7f1028f844ce89`
(`test(game): qualify position configuration packet wrapper`). The consumer
includes that pointer, the recovered C, sixteen checked rows and docs. Keep
the wider 80% matching goal open.
