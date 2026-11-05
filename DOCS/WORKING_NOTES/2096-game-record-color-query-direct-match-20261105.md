# Packed record color query directly recovered

Date: 2026-11-05. Target `func_1515E43C`, owner `generated_18A8F0`.
Source `conker/src/game/generated_18A8F0.c`; original `conker/asm/18A8F0.s`.

## Outcome and recovered interface

All nine pre-install checks pass in **57.373 seconds**; the nine fresh
installed checks pass in **53.449 seconds**. Actual Make and the
complete-image predictor agree byte for byte.

The routine emits all 66 words / 264 bytes directly, with frame32, eleven
bindings, no alignment tail and no guards. Both compact and padded owners
preserve all 34 neighbors, their bindings and normalized pools. Its span is
VA `0x1515E43C..0x1515E544`, ROM `0x18B8EC..0x18B9F4`.

The interface is `void(s32 x, s32 y, s32 z, s32 unused, u8 *primary,
u8 *secondary, u8 *secondaryExtra, u8 *primaryExtra)`. The fourth input is
homed but not forwarded. `func_1515EB84` receives the three complete signed
coordinate words, mask0 and a captured `D_800DCD84` list head. Both actual
callers ignore the wrapper's returned V0; the C interface is void.

## Packed words, fallback bytes and access order

A non-null record result selects two live unsigned words at `+0x18/+0x1C`.
The first word supplies primary bytes0/1/2 from bits0/8/16. The second
supplies secondary bytes0/1/2 in the same order, then its high byte supplies
`secondaryExtra`; the first word's high byte supplies `primaryExtra` last.
Each extraction explicitly masks `& 0xFF` and rereads its source word after
preceding output stores. Byte outputs may alias either source word, so a
single cached packed value is incorrect.

A null result copies three live bytes from `D_800DCD24`, then three from
`D_800DCD28`, followed by `D_800DCD3C` and `D_800DCD3D`. Every source read
occurs after previous output stores, preserving overlapping forward copies.
The three-byte outputs may overlap each other, defaults or packed records;
the extra-byte destinations may overlap any earlier destination or source.

The primary output home is loaded in the result branch's delay slot and
loaded again on the found path. The secondary output pointer is captured
before the first primary store. Both extra output pointers are loaded later,
immediately before their stores. Provider mutations of incoming homes are
therefore observed at the correct time. Private-home aliases qualify the
emitted ABI, not portable C access to compiler-owned parameter storage.

The plain unmasked expressions already emitted 66 words/frame32 but had
44 temporary-register differences. Masking all eight extracted bytes gives
the complete direct match. Six bounded source screens compare masks, casts
and the unused parameter's width; the accepted form adds no volatile filler,
register directives, special profile, padder rule or source-line trick.

## Original callers and connected record search

An aligned census of the complete prepared retail code binary finds exactly
two direct calls, at ROM `0x18AE50` and `0x18B810`, and no pointer literal or
tail jump to this function.

* `func_1515D914` window `0x1515D968..0x1515D9A8` checks flag bit2 and
  supplies all eight arguments. Outputs are parent SP+`0xB0`, `0xAC`,
  `0xAB` and `0xAA`. The disabled route ends at `0x1515DA34`.
* `func_1515E278` window `0x1515E328..0x1515E368` checks flag bit0x10 and
  supplies outputs at parent SP+`0x4C`, `0x48`, `0x47` and `0x46`. The
  disabled route ends at `0x1515E42C`.

Sixteen cases per body cover both original windows, both gate outcomes,
both stack phases, found/default paths and actual argument delay slots.
The parent routines after these named boundaries are not qualified here.

Sixty-four cases per body connect the full original 61-word
`func_1515EB84` at ROM `0x18C034`, frame0x360. They cover empty lists,
disabled records, type/high-bit filtering, predicate rejection, second-node
success, all-rejected fallback and the live node-record reload after the
predicate. The wrapper always supplies mask0, so the helper's nonzero-mask
routes are outside this connected interface's scope.

The predicate `func_150A1DA0` is a bounded provider. Its zero flag, record
pointer and seven query float fields are checked against signed coordinate
conversions. The already recovered helper and predicate receive no new
matching credit. This adds no full collision, rendering or gameplay claim.

## Fresh qualification and controls

All nine pre-install checks pass, including:

* 1,152 original/C guest cases covering coordinate and unused-word widths,
  null/two distinct record returns, provider mutations, both stack phases,
  all eight arguments and every one of 66 reachable words.
* 228 ordered alias cases per body, including packed-word overlap, live
  default overlap, coincident/reversed outputs and safe private-home overlap.
  An independent sequential reference checks public memory and call traces;
  complete original/C machine states also agree.
* Both original caller windows and the connected original search described
  above, with independent query snapshots and list-selection expectations.
* 77 fired access prefixes with complete original/C partial-state and trace
  equality. Removing all unused fallback sources on a found result, or the
  packed source words on a default result, still succeeds.
* Nine GNU links across three layouts, all eleven bindings, both HI/LO carry
  directions and exact original/raw/padded words. Thirty-six rebased cases
  per body pass.
* 13,056 native32 positive executions at O0/O2/O3, using direct and typed
  eight-argument calls, 17 alias layouts, two provider outcomes, mutation and
  defined unsigned-char aliases of aligned word objects. UBSan is enabled.
* Eight effective native controls and eight actual IDO controls: lookup
  mask, list head, packed source word, store order, cached packed value,
  fallback source, swapped extras and omitted/duplicated byte output. Every
  compiled control has an observed counterexample.
* Every one of 264 changed raw target bytes and eleven bad bindings is
  rejected. Whole-file header, neighboring-byte and tail corruptions fail
  the literal image prediction. The guard manifest has no target rows.

The initial native O2 crash was a fixture entry-point alignment issue. GDB
stopped at `_start+39`, `0x080494E7`, on `movaps %xmm0,0x50(%esp)` with
ESP `0xFFFFD2F4`; the aligned store address was not 16-byte aligned. The
fixture now uses `-mstackrealign`, as other freestanding native fixtures do.
Positive O0/O2/O3 then pass. A distinct non-overwritten little-endian alias
witness was added for the native store-order control; the big-endian guest
control has its own witness. Production C was not changed to bypass either
fixture issue. Native alias expectations use native word order; MIPS alias
expectations use big-endian word order.

The shared nineteen padder, relocation, matcher and protected-layout checks
pass in **7.347 seconds**, and `make tools-check` passes. No shared oracle
is changed. Unchanged neighbor suites are reused through verified byte,
binding and pool identity rather than claimed freshly executed.

## Complete-image prediction and fingerprints

The qualified image changes exactly one function body and keeps every one
of 6,052 function addresses fixed. All 189,088 protected Game bytes across
720 owners remain exact. The literal complete-file predictor changes only
the target slot and its symbol extent: **197 bytes**, zero exclusions and
no symbol-order or other metadata correction. The guard manifest stays
byte-identical; no target row or compiler-profile change is introduced.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `d054a96fa4add2cb132003f47826802017ab23b8cab7e2708f0a2252ef0789cb` |
| Retail target | `71f1c40a6bb036aed83d69b19cf8fd675f6b9d16112a4789e78f834fee4d0c69` |
| Frozen predecessor ELF | `fbec38e46735bda7ddea0c9f35d6664febae8668b86d8b9cf786e55491b63257` |
| Qualified padded owner | `3cb7cfc75f2294adbc048c4fbd430496d45e5cadb6668a5f40bc7c9452e2e601` |
| Qualified complete ELF | `6f1eb8121a4c21b123b88b0dc068ae30fd930ba3a03d112117fdf40a7510f71b` |
| Production code binary | `15bc17fd524e87dc498a8ede1734cb002d8c39de24c32427019b98055194d75d` |
| Unchanged guard CSV working bytes | `87a70532340ab80357051ae8b6e0b77d09b65d08c2af717f3b1cf32b35e8b3ce` |

Ignored artifacts live in
`conker/build/game-record-color-query-1515E43C-match/`, with adjacent private
source screens. The immutable snapshot contains 92 files, including the
complete headers, retail input, original assembly/callers/helper, source,
object, ELF, code binary, guard history, layout, Makefile, linker and graph.

Main baseline is `8ad0a8ba3c1a2450fe5a57832cf65a88ac7d3a64`; mounted tools
baseline is `2931ef14939ecb87abbe2939d1564551ec367986`. Both start clean.
The separate sibling tools checkout remains at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with six tracked changes and
2,428 untracked files. It is untouched, and no fresh sibling qualification
is claimed. No host-port or frozen Release changes are made.

## Production and continuation

The four-job actual Make rebuild returns zero. Its owner is byte-identical
to the qualified padded object, and the complete ELF equals the independent
197-byte prediction. Only the target slot and symbol extent change, with
zero excluded bytes or metadata substitutions. The guard manifest, frozen
headers, retail input, original assembly, layout, Makefile and linker stay
byte-identical. Make still reports its inherited duplicate
`generated_12D630` recipe warning; no new target warning is introduced.

`make -C conker all` generates the code binary and returns 2 only at the
expected overall retail SHA mismatch for the incomplete decompilation.
The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,167 / 5,512 | 75.60% | 0 | 1,345 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,494 / 4,839 | 72.21% | 0 | 1,345 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046. Root README edits are aggregate rows
only. The 80% threshold is 4,410/5,512, leaving 243 more exact functions.
Actual ranking selects `func_15167B44`, 69 words and 65 real differences, as
the next ordinary target. Keep `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC` and
`func_150A6760` as the separate documented boundary cases.

Mounted tools are committed first as
`ef757f6e3632b6f08a26e1df8f67b3c7f280ff53`
(`test(game): qualify packed record color query and aliases`). The consumer
includes that pointer, the direct C and documentation. Keep the wider 80%
matching goal open.

The standard Graphify update refused a reduced 24,904-node extraction
against the existing 58,697-node graph, preserving the larger graph. The
seven-path scoped refresh retains 58,694 old nodes, relocates three existing
`DOCS/UPDATE_LOG.md` headings and adds eight headings from this note plus
the `LinkedNode` type reference: 58,706 nodes, 112,465 links and 5,155
communities. No node outside the changed paths is removed. The retention
receipt records SHA-256
`ac81e63ba9fe0edb94acfc6596ffa13a472d4f700401738c3465c6311ad6e693`.
The 31,816 retained nodes from 3,754 still-existing files outside the current
scan corpus are preservation evidence, not a fresh full-corpus extraction
claim. The ignored `graph-retention.json` receipt is retained in the
qualification directory.
