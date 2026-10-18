# Route Neighbor Preference Byte Match

Date: 2026-10-18. Consumer predecessor **2207e1a8**; tools predecessor
**3bd5e4e**, new tools checkpoint **2c94753** banked first. Recover
**func_1508907C**, owner `generated_B3020`, VA **0x1508907C..0x150891E8**,
ROM **0xB652C..0xB6698**, **91 words /364 bytes /frame8**.
The complete semantic C body replaces a false zero-return placeholder.
All 91 linked words match retail after 52 independently qualified guards.
The wider Game matching goal remains active.

## Recovered Contract

Use `u8 func_1508907C(u8 id, u8 type, u8 excluded, u8 preferred)`, preserving
the address-based symbol and a concise preference/fallback comment. The callee
stores all four incoming 32-bit argument words in their caller homes before
truncating to bytes. Its private frame saves only S0 at entry-SP-4.

Compare the byte index against signed-halfword D_80087290. An invalid index,
including every index with a nonpositive count, returns FF without reading
the table pointer. Otherwise capture D_800D2350 and address 16-byte records.
Visit exactly five neighbor IDs at offsets9..D. Ignore FF and the excluded ID;
neighbor IDs themselves are not validated against the current count.

Always read the candidate's unsigned type byte at E before considering the
type-FF wildcard. Remember the last accepted type match as fallback, but
return the first accepted candidate whose class byte at F equals preferred.
Preferred FF is a literal class value, not a wildcard. With no accepted
candidate, return FF. There are no helper calls or external writes beyond the original
argument homes and S0 save. The explicit first-slot/two-slot-loop C preserves
retail's partial unrolling under the established owner no-unroll profile.
No Makefile/profile change or inline assembly is introduced.

The alternate source supplied a control-flow clue, not trusted C: its word
loads for byte metadata are incorrect. The installed widths, interfaces,
conditions and ordered accesses are established against the retail routine.

## Closed Normalization

The complete raw C emits 91 words/frame8 with 52 word differences and the
correct four argument homes and S0 save. Raw SHA-256:
`56420d7eed4509cd27f499eed1a6cb0dfc703b0ad64ad42462fc4388d2608593`.
The independently frozen retail slot SHA-256 is
`60e1615185f9976a87f2fcb3b5def95ec6945b70a0bad06807aab3f180b68a89`.

`tools/experiments/game_route_neighbor_preference.py` derives the normalized
words from an explicit scalar register map, moves one global HI16 binding
from relative80 to68, removes an opening identity copy, and consolidates two
likely-delay lifetimes. The count HI/LO pair at56/60 and table LO at92 stay
fixed. No words are inserted or omitted; no retail assembly body is substituted.
All 52 CSV rows have exact expected words and relocation descriptors.

The proof checks the independent retail hash/vector, then compares **4,688
symbolic CFG paths** from raw code against that retail vector. Preserve every
ordered read, every store, the full return word and saved integer ABI. Constant
loop limits are evaluated; an unknown/nonterminating path fails the250-step
bound. The complete 91-word source and retail slots are retained.

Explicit structural gates require the opening copy/use and each duplicated
delay instruction at its shared target. Versioned read-after-stores terms are
congruent for any ordinary byte-memory interpretation, including partial
aliases; no external/frame disjointness is assumed. Equality need not simplify
each aliased read to a concrete value. Concrete byte-memory fixtures separately
exercise these overlaps. Raw dead/caller-saved GPR values at fault boundaries
are outside the C ABI claim and demonstrably differ.

## Fresh Qualification

```sh
python3 -m unittest tools.tests.test_game_route_neighbor_preference -v
python3 -m tools.experiments.game_route_neighbor_preference --predict
```

Seven final pre-install tests pass in **27.254s**; seven installed tests pass
in **36.230s**. Sources, objects, prediction, packet and JSON receipts are
ignored artifacts under `conker/build/game-route-neighbor-preference/`.

- **7,826 three-way raw/padded/retail guest cases** compare complete memory,
  including private homes, exact ordered traces, return values and ABI state.
  Cover all3,125 five-slot outcome patterns for normal and wildcard type,
  signed count boundaries, upper argument bits, every byte value for each
  argument/type/class field, both stack phases and five guest aliases. All
  91 words are visited in each body. Integer-only code preserves all FPRs.
- **71,786 native32 cases per O2/O0 UBSan profile**, including all65,536
  signed count values, preserve input arrays, pointer and canaries. Seven
  effective semantic controls exit wrong-result23, not crashes. Native tests
  use valid arrays, not forged global/private-frame aliases.
- **593 three-way fault prefixes across48 fixtures** compare all memory and
  ordered access traces, including the four argument stores and S0 save.
  Dead raw GPR fault state is explicitly unequal; no such equality is inferred.
- **Nine independent GNU links /288 three-way rebased cases** exercise code,
  count/table globals and both sides of HI16/LO16 carry boundaries. Repeat
  the symbolic proof against independently assembled retail at each placement.
  The real padder produces all91 retail words and the correct moved binding.
- **112 three-way retained call/delay windows across seven actual JAL sites**
  execute the real helper with its actual delay-slot effects. Check forwarded
  arguments, full memory, result and preserved caller state. These are bounded
  two-word windows, not complete executions of the two unfinished parents.
- Preserve all **72 raw owner neighbors and relative bindings**, including
  the live spline caller, plus normalized pools. Reject91 raw-word corruptions,
  four missing bindings, an altered independent retail vector and26 live or
  snapshot input alterations. Six independent symbolic word controls are
  effective; a partial-byte alias control retains its preceding word store.

The first test launch exposed a class-assertion setup mistake. Native initially
lacked `_start` under the existing freestanding flags; adding the established
exit wrapper fixed the harness, and empty compiler/linker diagnostics are now
required. The predecessor symbol is measured as12 bytes, not an assumed8.
These were fixture corrections, not production defects or matching credit.

## Advisory Reconciliation

One packet-only Claude Code Pro call completed with effective tools=[] and
mcp_servers=[], existing claude.ai/firstParty auth, no provider/account switch.
Packet SHA-256:
`b1a780caabd585bcff22ed8c284c6dc561f04afb9e5d6798c93c553d57c4b269`.
The review was critical; its answer is not treated as approval.

Accept and independently validate an explicit frozen-retail proof argument
and structural duplicate-delay gates. The real padder already compared retail;
the proof API now makes that independent binding explicit too. Reject the
claimed non-executable renamer: the packet omitted the local import alias,
whereas the actual callable is `game_table_fade_match.registers`, imported as
`rename_general`, and executes successfully. Original sent packet/receipt are
retained unchanged. Partial-alias simplification is not required for congruent
versioned memory terms; concrete overlaps and an additional symbolic alias
control validate the declared scope. Dead GPR equality remains explicitly
excluded, while normalized words are independently byte-exact. No second call.

## Linked Audit And Bank

The actual whole ELF equals the immutable first prediction: **263 changed
bytes**, comprising261 target instruction bytes and two target-size bytes.
Every other ELF byte is fixed. All **6,057 function addresses**, all other
bodies/definitions, existing guards and protected Game data stay unchanged:
**189,088 bytes /720 owners /zero differences**. No broad rebuild is inferred
from the focused owner/link/progress build. The existing duplicate12D630 recipe
warning remains; target compilation itself has no diagnostics.

| Successor | SHA-256 |
| --- | --- |
| Whole ELF | 4b8ab8ed1c080b5f392f60ddf05d2902229e3b4baa6cc880f006881538b7f9ea |
| B3020 C owner | f7db991ff588fad0fcfde4d10e0b234221abb82c829bea68c8ec5be954e1e17f |
| Guard manifest | c40fe51b50da9855fb73bc86bb2d0562e42365dc8afb1eb2c3603018040073a9 |

Fresh official totals: **Game2,985/4,828 (61.83%)**, **total3,658/5,501
(66.50%)**, Init492/492, Debugger181/181, **1,843 different /zero drift**.
Conversion counts/bytes are unchanged because the old stub already counted
as C. Root README receives aggregate matching rows only.

Shared padder/PC16 tests pass eleven per tools copy, both smoke checks and
consumer tools-check pass. Four copied task files pass ASCII/AST checks;
both pairs are byte-identical. Standalone mirror HEAD **ddbdd16** is unchanged:
preserve all **1,224 prior dirty hashes**, adding only two absent task files
for1,226. No mirror commit/reset, push, host or frozen Release action.

## Resume Here

Next recover **func_150891E8**, VA150891E8..150896EC,321 words/frame0x78.
Establish its actual incoming interface and full ordered behavior from retail;
it contains two of the newly qualified selector's call sites. The remaining
five sites belong to the still-unfinished func_150896EC. Full parent/helper
and gameplay acceptance are not implied by the bounded call-window tests.

Vector **func_15088F30** remains uninstalled: its correct two-save invariant
contract is still open. Six additional ignored local-register-hint probes
emit the same target bytes/bindings as Note1548's two rejected families; do
not repeat them. No new vector qualification or matching credit is claimed.
Its older physical pins now predate this source/ELF/guard successor as well;
use a deliberately verified predecessor view or a new strict checkpoint,
never silently replace historical fingerprints. Wider Game queues stay open.

Scoped Graphify refresh: **42,564 nodes /82,635 links /4,131 communities**.
Preserve19,398 nodes from2,972 excluded-but-existing files. All42,551 other
old IDs remain; three line-disambiguated UPDATE_LOG heading IDs relocate by
the eleven added lines with labels/files retained. This note adds eight
nodes; the actual C definitions are indexed at lines837 and887. Tools remain
subject to the configured submodule exclusion, not a fresh graph AST-coverage
claim for the new Python files. Original graph and ID audit are ignored task
artifacts; no full-scan purge, committed graph output or history rewrite.
