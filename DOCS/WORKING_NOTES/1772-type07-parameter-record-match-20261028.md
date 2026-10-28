# 1772 - Type-7 Parameter-Record Constructor Match - 2026-10-28

The adopted Native ELF measures **3,850/5,506 exact C functions (69.92%)**,
Game **3,177/4,833 (65.74%)**, zero address drift and 1,656 different.
Only `func_151B9BF0` gains matching credit. The unchanged 75% threshold is
4,130 exact C functions, requiring **280 more**.

## Recovered routine and interface

`func_151B9BF0` in `generated_1E6B40.c` occupies VA
`0x151B9BF0..0x151B9CB0`, ROM `0x1E70A0..0x1E7160`: 48 words, a
32-byte frame and one J26 binding to `func_15167A68` at +52. It emits
directly from semantic C, with no guards or profile changes.

The recovered interface returns void and takes sixteen O32 arguments:
two signed words narrowed to byte fields, eleven signed halfword parameters,
one unsigned word value, one byte view and one signed context. The local
`Type07ParameterRecord` is exactly 44 bytes: value at +16, bytes at +20/+21,
and eleven halfwords at +22 through +42. Field names remain descriptive
without inventing an unproven gameplay interpretation.

The factory receives `(7, context, 0x2C, 0, view, 1)`. On success, preserve
the two byte stores, eleven halfword stores and final value-word store in
that order. Retail reloads argument homes after the factory, so provider
mutations and overlapping output/home storage affect later reads. On failure
there are no record stores; the branch delay still loads the first incoming
argument word. Other parameter homes can be unmapped after provider failure.
The view/context have already been read before that call.

An initial pointer-return screen emitted 50 words. Five original call sites
support the corrected void interface, which emits the exact 48-word body.
The incidental guest V0 value is still compared as part of complete machine
state; it does not establish a pointer-return C contract.

## Original callers and retained helpers

| Original parent | JAL site | Qualified setup window | Words |
| --- | --- | --- | --- |
| `func_150265CC` | `0x15026AE0` | `0x15026A70..0x15026AF0` | 32 |
| `func_150265CC` | `0x15026BA0` | `0x15026B30..0x15026BB0` | 32 |
| `func_150C3994` | `0x150C3A5C` | `0x150C39C8..0x150C3A6C` | 41 |
| `func_150C3994` | `0x150C3BB4` | `0x150C3B1C..0x150C3BBC` | 40 |
| `func_150C3D5C` | `0x150C3DF8` | `0x150C3D6C..0x150C3E00` | 37 |

The complete ROM census finds those five direct sites and no target pointer
literals. Execute actual setup, narrowing and float-coordinate truncation,
including caller gate paths and the observed return boundaries. All three
current parents remain zero-return placeholders; this does not credit them
or claim full-parent or gameplay acceptance.

The current factory `func_15167A68` (28 words) and list initializer
`func_15168A4C` (20 words) already equal retail. The connected guest tests
execute all 48 helper words with empty/nonempty heads and allocation failure.
The lower heap provider remains bounded. Native tests compile the actual
factory C with an explicit 32-bit cast for its legacy s32 heap return; their
list initializer is bounded. No shared-header or helper repair is included.

## Complete owner and image

All three neighboring functions, raw/padded pools and bindings remain fixed.
The actual three-command generated Make recipe uses normal O2/g3, compiles
the complete owner, pads and assembles it with zero diagnostics. There are
no GLOBAL_ASM routines in this owner. The guard CSV remains unchanged.

Strict independent prediction permits exactly **143 changed image bytes**:
142 target code bytes and one target symbol-size byte (12 to 192), with zero
exclusions. Production reproduces that image. All 6,056 disassembly addresses,
all 6,055 other bodies, named ELF definitions, section geometry, map and
C inventory remain fixed. All 720 Game data owners / 189,088 bytes remain
exact. The inherited duplicate generated_12D630 Make warning persists.

## Behavioral qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production reruns two installed methods per copy; six semantic checks are
reused only after exact input, module and artifact fingerprint comparison.

- 3,136 guest cases cover all sixteen arguments and high bits, all byte
  encodings, eight overlapping incoming-home layouts, provider mutations,
  allocation failure, outgoing-home and volatile-register clobbers. All
  48 words are visited; complete state and ordered traces agree.
- 160 original caller-window cases include 128 target calls across all five
  direct sites. Another 32 cases execute both retained helpers, including
  list-head insertion, row-byte narrowing and failure.
- Native32 O0/O2/O3 each pass 262,144 cases through the actual sixteen-input
  function-pointer type, with trapped UBSan, whole-storage fences and all
  encodings of each halfword input. All nineteen semantic negatives fail.
  Guest stack aliases remain separate from native C storage claims.
- 392 fired fault-prefix pairs preserve state, trace, PC and delay context.
  The NULL case explicitly leaves only its required late first-word home.
- Three GNU relocation layouts pass 24 execution cases. Real padder
  reproduction, three raw/binding rejection controls, four actually compiled
  IDO negatives and six complete-image corruptions reject changed behavior
  or evidence. The cached-argument negative uses a volatile local: a plain
  local was optimized back to the correct late load and was not accepted
  as an effective negative.

## Bank and continuation

Baseline consumer `5076f3ca`, tools `6425b76`. Tools are committed first as
`b93ec4035ab413e670be0cb7ceec0e5d25ca310f`. The seal verifies 16,295 files and
299 focused inputs. The initial 291-input screen was extended by eight
existing sealed caller/helper sources and objects; its earlier snapshot is
retained. Preserve all 1,757 inherited dirty paths in the independent tools
mirror, adding only the three target modules there. No mirror commit or
push is requested. Host Release stays frozen.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | `d3d212c4d0df5199bf1e879e50cb841e4b9819db44b4178c6592353d6eb0493f` |
| Padded owner | `dfde6b5cef03a9dc1245129485c3b2ef530da99347997fcf9127acbd9316fd5c` |
| Recovered source | `df8a99f25b28a2629de79a6119f6607a40cf07eb1266c193504c62079d2beee7` |
| Raw original/compiler body | `3d489eca752b1e2bd49bfbbe31f19288ca0bb98fbd1f55f696cd76f5cd60ed21` |
| Complete retail body | `c08a81cc88b1e35e9477230732855646f5c54c3337c73bde481c59101bdca084` |
| Unchanged guard CSV | `20131e428c071ea6d2cbee21968f122274bc71fb167a2a356b3033ff5582f8b9` |

Scoped Graphify closeout refreshes eleven changed C/Markdown/tool files.
Retain all 45,945 old nodes and account for all 94,228 old relationship
contexts, retiring only the target placeholder false s32 return. Preserve
outside-scope manifest freshness and historical communities. Validate all
sixteen parameters, the factory binding and original caller windows without
inventing current caller edges or claiming a full-corpus extraction.

Next inspect the 48-word `func_1509F4E8`. The remaining queue contains
1,527 placeholders, 120 semantic/other entries and nine unlocated screens;
it is triage only. Keep `func_1514E920` parked and uncredited and the 75%
goal open. Routine Claude calls: zero.

Prepared-checkout command:

```sh
python3 -m unittest tools.tests.test_game_type07_parameter_record_match -v
```
