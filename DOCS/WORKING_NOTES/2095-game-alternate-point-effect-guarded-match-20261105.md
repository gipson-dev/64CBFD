# Alternate point/height effect callback recovered

Date: 2026-11-05. Target `func_15146D60`, owner `generated_173D40`.
Source `conker/src/game/generated_173D40.c`; original `conker/asm/173D40.s`.

## Outcome and scope

All nine pre-install and nine fresh installed qualification checks pass.
Actual Make and the complete-image predictor agree byte for byte. The
fresh installed nine-test suite passes in **72.814 seconds**.

The complete routine is 73 words / 292 bytes, VA
`0x15146D60..0x15146E84`, ROM `0x174210..0x174334`, frame88, six bindings
and no alignment tail. Both compact and padded owners preserve all twelve
neighbors, their bindings and normalized pools. The existing point helper
and randomized burst callback are unchanged. No shared header, compiler
profile, Makefile, layout or unrelated conversion is added.

## Recovered behavior and ABI

The callback is `void(u8 *actor, s32 mode, s32 amount)`. It captures the low
unsigned mode byte, then checks the actor's attached-object word at `+0x1D4`.
A zero word returns without reading the tag or either float constant. With
an attached object, it asks `func_15146890` for a position and a 36-byte
height/interval result. A zero helper return suppresses the effect.

On a nonzero helper return, the callback reloads the signed full-width amount
and actor pointer from their incoming homes. It sends effect slot10, the
interval bytes, `(f32)amount * D_800A5728`, an unsigned byte converted from
the live actor float at `+0x40` times `D_800A572C`, the position, and the
captured mode to `func_15141F78`. The mode snapshot can be overwritten by a
provider's explicit private-stack mutation; the final reload uses that live
snapshot word. The tag, amount and scale must not be cached before the
point-helper call.

Actual constant words are `0x3C40C0C1` and `0x3F360B61` at
`D_800A5728/D_800A572C`, ROM `0x24A1E8/0x24A1EC`, in
`conker/asm/data/24A190.rodata.s`. The effect callback is the alternate-point
member of the family already recovered for `func_150EB090`; the shape is
reused while this owner, constants, helper, registration and emitted body
are independently qualified.

The local `HeightResult71820` definition is completed to its measured
36-byte layout so the C can allocate it: height, nine vertex halfwords,
padding halfword, metadata, flag/state bytes, padding halfword and value.
Existing helper code uses pointers to the same structure and emits unchanged
bytes after completing the local type.

## Saved-mode derivation and rejected direct candidate

The selected body names the required low-byte snapshot as a word local.
O2/g3 emits the complete 73-word routine and retail frame naturally. Only
the snapshot's stack position differs:

| Offset | Natural instruction | Retail instruction |
| --- | --- | --- |
| `+0x034` | `sw a3,0x20(sp)` | `sw a3,0x24(sp)` |
| `+0x0F8` | `lw t3,0x20(sp)` | `lw t3,0x24(sp)` |

The normalizer derives those two operations by scanning all SP-based word
loads/stores of `+0x20`. The exact raw hash and six complete bindings must
match, the closed access set must be exactly the two rows, and all normalized
words must equal retail after masking only the bound relocation fields.
Neither correction changes a register, relocation, frame, instruction count
or control-flow edge.

A private experiment gave `func_15146890` a complete ANSI byte-mode
declaration. That made this callback emit all retail words directly and kept
the helper's 56 words exact, but the wider owner audit showed that it also
changed `func_15147040`, the existing randomized burst callback. That candidate
was rejected. The accepted source preserves the original helper declarations
and all neighboring code. Explicit casts, byte/word locals, declaration
orders and temporary status shapes were bounded source screens; no filler
locals, profile changes or broad regeneration are adopted.

The natural and fitted bodies agree for ordinary inputs and bounded public
provider effects. Artificial aliases involving the compiler-private saved
mode word distinguish its two positions. Those cases and fired access-prefix
checks qualify original/fitted instructions, not portable C stack/fault
semantics or natural private-stack alias parity.

## Registration, dispatcher and original helper

An aligned census of the full prepared retail code binary finds no direct
JAL/tail-J reference and exactly one pointer literal at ROM `0x22EB8C`, VA
`0x8008A0CC`. It is entry3, stride8, of `D_8008A0B4`, paired with the real
positive count85. The complete 43-word registry and the selected pair are
checked against `conker/asm/data/22EB40.rodata.s`.

Both original `func_15141A7C` dispatch windows are connected to this callback:
five words at `0x15141B4C..0x15141B60`, and eight words at
`0x15141BAC..0x15141BCC`. Each has 96 cases per body, testing the unsigned
mode, signed record amount, disabled/enabled actor gate and helper return,
both stack phases and actual delay slots. The first window is a direct
dispatch boundary test. A separate original fourteen-word window at
`0x15141B28` proves that this registry's real +85 count takes the timed-record
registration route instead; it submits `(actor,3)` to `func_15141E38`.
No complete parent or timed-record subsystem is claimed.

Forty-eight cases per body connect the full original 56-word
`func_15146890`, including its live actor/result homes and return gate.
Modes1/2 select point indices19/23; other modes return zero. Resolver,
surface initializer and interval query providers are bounded models, with
their arguments, position/interval snapshots and returned values checked
against an independent reference. There is no new matching credit for the
already exact helper or any provider implementation.

## Focused checks and model boundaries

The nine-test pre-install suite passes in **42.258 seconds**. After adding
the two actual-padder preimage controls, the affected qualification check is
rerun and passes in **24.926 seconds**. Fresh checks include:

* 3,328 original/fitted guest cases covering every mode byte, gate and helper
  return, signed amount extremes, live tag/scale, bounded FCSR conversions
  and all 72 reachable words. The duplicate `mfc1` at `0x15146E48` is
  unreachable, but remains in the complete 73-word byte comparison.
* 144 private-home/ordered-alias cases per original/fitted body, including
  actor/amount changes, mode-snapshot writes, tag overlap with position,
  interval or mode, and two redirected returns.
* The full original point helper, both dispatcher interfaces and the real
  positive-count registration route described above.
* 92 fired access prefixes with complete original/fitted partial state,
  delay-slot and trace equality. The disabled path needs no tag or constants.
* Nine GNU links across three layouts, all six bindings, both HI/LO carry
  directions, exact original/fitted words and the independently checked
  two-offset natural form. Forty-eight rebased cases per body pass.
* Native32 O0/O2/O3, each with 480 direct and 480 typed indirect executions:
  2,880 positive executions total. UBSan and float-cast-overflow traps are
  enabled within the finite unsigned-word tag-conversion domain. Values
  crossing byte256 and the unsigned high half are included.
* Eight effective native controls and the same eight actual IDO controls:
  actor gate, point mode, helper predicate, slot, amount scale, tag scale,
  final mode and prematurely cached tag. Each IDO control has a guest
  counterexample.
* All 292 changed target bytes and six bad bindings fail the natural-body
  guard. Both wrong expected-word preimages fail through the actual owner
  padder. Whole-file corruptions and four named symbol/string corruptions
  fail the strict predictor.

The bounded guest model preserves/restores its supplied FCSR and models
nontrapping conversion outcomes, including exceptional float inputs. Native
fixtures use only defined finite unsigned32 conversion inputs. These do not
claim hardware exception flags, trapping behavior, arithmetic NaN payloads,
portable C out-of-range conversion behavior or gameplay acceptance.

The shared nineteen padder, relocation, matcher and protected-layout checks
pass in **6.578 seconds**, and `make tools-check` passes. No shared oracle is
changed. Family fixtures are reused with this function's actual helper,
constants, point indices, callback index3 and count85, and all current-target
checks are freshly executed. Unchanged neighbor-suite receipts are reused
only through byte, binding and pool identity.

## Complete-image prediction and fingerprints

The qualified image contains exactly one changed body, with all 6,052
function addresses fixed and all 189,088 protected Game bytes across 720
owners exact. The literal complete-file prediction changes 216 bytes with
zero exclusions. Besides the target slot and symbol size, one GNU-ld hash
bucket swaps `D_800A572C` and `D_800A142C`. Complete symbol records at file
`0x2C34CC/0x2C34DC` and names at `0x303567/0x303572` are reconstructed from
the pinned predecessor. Values, bindings, sizes and section identities stay
fixed. This is explicit bookkeeping, not a code guard or metadata exclusion.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `bc4108e0ebcb78c2c5c2066836ebed1b8ba02f29e918a4ef76bcfba09e6b5022` |
| Retail target | `cfdedfd0303caa2072e57265adf78596f9fda86aad4930e4aaab63e5db7e8919` |
| Frozen predecessor ELF | `743cca9727fe79f2058b52f709599e21ee5ea32a28647a72ba8582124f89b95a` |
| Qualified padded owner | `3ae57e5a414deb0da430c4fa3d754999ec92a89f8c69122f6b9a1b79c2b9a629` |
| Qualified complete ELF | `fbec38e46735bda7ddea0c9f35d6664febae8668b86d8b9cf786e55491b63257` |
| Production code binary | `cd4269b2b77b47b8896f374ea3272919ba4d6dce2e0b1410dfdac84c1ff763c7` |
| Guard CSV working bytes after two rows | `87a70532340ab80357051ae8b6e0b77d09b65d08c2af717f3b1cf32b35e8b3ce` |

Ignored artifacts are retained in
`conker/build/game-alternate-point-effect-15146D60-match/`, with adjacent
candidate screens. The initial immutable snapshot contains 94 inputs; the
actual constant-assembly file is added as a separate one-file immutable
supplement without recapturing the original snapshot. Inputs include full
headers, retail code, assembly, registry, layout, guards, Makefile, linker,
source, object, ELF, code binary and graph.

Main baseline is `f59bdb42684ff4af41df151d2508f9ffa057e26c`; mounted tools
baseline is `80d906d441e5215c3afbd0d2fc7f1028f844ce89`. Both start clean. The
separate sibling tools checkout stays at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked changes and
2,428 untracked files; it is untouched and no fresh sibling qualification is
claimed. No host-port or frozen Release work is added.

## Production and continuation

The four-job actual Make rebuild returns zero. Its owner matches the
qualified padded object byte for byte. The complete production ELF equals
the independent 216-byte prediction: 210 target/extent bytes and six named
symbol/string serialization bytes, with no exclusions. The old guard file
is an exact byte prefix plus two rows. Frozen headers, retail input,
constant assembly, registry, original code, layout, Makefile and linker
remain fixed. Inherited SDK and duplicate `generated_12D630` recipe warnings
remain; no new target warning is introduced.

`make -C conker all` generates the code binary and returns 2 only at the
expected overall retail SHA mismatch for the incomplete decompilation.
The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,166 / 5,512 | 75.58% | 0 | 1,346 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,493 / 4,839 | 72.18% | 0 | 1,346 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes are aggregate
rows only. The 80% threshold is 4,410/5,512, leaving 244 more exact functions.
Actual ranking selects `func_1515E43C`, 66 words and 65 real differences, as
the next ordinary target. Keep `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC` and
`func_150A6760` as the separate documented boundary cases.

The standard Graphify update refused a reduced 24,896-node extraction
against the existing 58,688-node graph, preserving the larger graph. Mounted
tools are committed first as
`2931ef14939ecb87abbe2939d1564551ec367986`
(`test(game): qualify alternate point and height effect callback`). The
consumer includes that pointer, the recovered C, two checked rows and docs.
Keep the wider 80% goal open.

The eight-path scoped graph refresh retains 58,685 old nodes, relocates three
existing `DOCS/UPDATE_LOG.md` headings and adds nine headings from this note:
58,697 nodes, 112,454 links and 5,200 communities. No node outside the
changed paths is removed. The retention receipt records SHA-256
`120ae12a053a7bb7a00999b21e74ac400f879141f7267e48d129654e6eb06c16`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. The ignored `graph-retention.json` receipt is retained in the
qualification directory.
