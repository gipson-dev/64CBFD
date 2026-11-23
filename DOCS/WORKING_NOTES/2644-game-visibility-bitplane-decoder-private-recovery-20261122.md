# 2644 - Visibility bit-plane decoder private recovery

Date: 2026-11-22. The total 85% matching goal remains active. This work banks
a reproducible semantic recovery, **not an installed C match**. Production
remains **4,625 / 5,528 (83.66%) total**, **3,952 / 4,855 (81.40%) Game**,
with zero address drift, 903 different and **74 more matches to 85%**.
Init remains 492/492 and Debugger 181/181. Root README aggregate rows remain
correct and unchanged; this narrative belongs here.

## Target, ownership and the recovered behavior

`func_150A6760`, owner `conker/src/game/generated_D3040.c`, occupies the
64-word retail slot VA `150A6760..150A6860`, ROM `D3C10..D3D10`. The last
two words are alignment NOPs; all 62 executable words run in the bounded
guest suite. Retail uses no stack frame or saved registers and makes no calls.
Original source evidence is `conker/asm/D3040.s`, starting at line 818.

The decoder selects a signed halfword entry from `D_800DBE30` using its word
plane argument, then uses that entry to index four-byte cursor records through
`D_800BE5D4`. Each cursor contains an unsigned halfword byte offset and signed
halfword remaining-bit count. `D_800BE5D0` is the stream pointer; a null stream
returns before reading any other global. With a non-null stream, retail reads
the cursor, first stream byte and tree pointer even when the output head is null.

Signed tree-node values and signed byte offsets in `D_800BE5D8` decode a leaf
symbol. Negative values select children using successive most-significant bits
of the stream byte; consuming the boundary advances the stream and resets the
bit position to seven. A nonnegative leaf supplies eight output bits, one per
linked output node. The routine clears and replaces the selected plane in each
node's flags without changing other flag bits. It reads both signed relative
links, primary at `+0xC` and alternate at `+4`, preferring a nonzero primary.
The measured local node view is 16 bytes; unread fields remain opaque.

`func_150A67D0` is an interior label at offset `0x70`, the repeated tree-node
load in the same routine. Production ELF represents it as an absolute symbol
at `150A67D0`, rather than a second progress/layout slot. The raw generated
owner still has two false C placeholders; this screen preserves both, including
the orphan raw stub, and preserves all 16 other compiled owner functions.
Do not treat the interior label as an ordinary separately callable C function.

The pinned ROM's literal direct-edge census finds one internal J at ROM
`D3CB4` to that label and one external JAL at ROM `13D198`, VA `1510FCE8`,
from `func_1510FC34` to the main entry. No aligned exact-word pointer to either
address appears. The caller supplies its original first argument through S0
and A0, stores the selected signed-halfword map in the JAL delay slot and
does not consume a decoder return value. These observations support a void
leaf interface, but do not exclude computed/materialized pointers or establish
the caller's complete legal plane domain or complete caller behavior.

## Source screens and the remaining matching boundary

All complete-owner screens use the existing O2/g3 profile, leave all 16 other
compiled functions and normalized pools unchanged, and preserve diagnostics.

| Private form | Raw words | Frame bytes | Retail slot words |
| --- | ---: | ---: | ---: |
| Initial structured decoder | 77 | 24 | 64 |
| Captured cursor and explicit decode/next-node loops | 71 | 24 | 64 |
| Same loops with an initialized symbol carrier | 70 | 0 | 64 |

The final form restores frame zero but still has six more words than the
complete retail slot, or eight more than its executable body. It also differs
in register allocation, control flow and access scheduling. There are 63
differences among the first 64 positions; this is not a two-word scheduling
finish. All three candidates differ from retail's public access trace in all
432 sampled cases, despite matching final public memory. No broad word
normalizer, new guard, source installation, layout/profile change or matching
credit is justified by this result. Handwritten provenance has not been proven.

## Fresh bounded qualification

Five focused gates pass in the mounted tools checkout and in a disposable
sibling-tools overlay. Both runs are fresh, with identical task files, manifest
and imported dependency fingerprints. The real sibling checkout's HEAD, dirty
paths and all 353 retained dependency hashes remain unchanged.

- Original and three private MIPS streams each agree with an independent
  big-endian memory model on **432 cases**. Cases cover planes 0, 1, 7, 11,
  15 and 31 with explicitly allocated backing, empty and 1/7/8/9/17-node
  chains, three tree shapes, zero/seven remaining-bit boundaries, signed
  negative cursor indexes and tree offsets, unsigned byte offset `0x8001`,
  forward/backward relative node links, alternate-only edges and primary
  precedence when both links are nonzero. All public bytes compare, including
  opaque/untouched nodes. A null stream returns at planes 0 and 31 without
  touching the intentionally absent other globals.
- Retail's complete public memory-access trace agrees with the independent
  model in all cases. Each C candidate's trace differs in all 432 cases. This
  result is retained as a rejection boundary, not suppressed in the tests.
  Three deliberately altered retail controls for map signedness, stream-byte
  boundary and link precedence fail through output or invalid-memory checks.
- The selected frame-zero C body passes **432 cases at each native SDK32
  O0/O2/O3 profile**, with strict aliasing and UBSan. Assertions establish
  pointer/long widths, cursor/node extents and both link offsets. Checks compare
  all 17 nodes' numeric fields and opaque bytes, output canaries, tree/stream/
  cursor inputs and global pointers. Three C source controls fail through
  output comparison: wrong plane mask, wrong eight-node symbol grouping and
  wrong stream boundary. Null-stream cases also execute natively.
- The existing guest interpreter is reused. A target-local NOR and variable
  shift adapter is checked against ten explicit ISA vectors, including shift
  counts 31, 32 and 63, signed right shifts and untouched registers. No shared
  interpreter implementation is changed.
- `make tools-check` passes. A fresh recount of the unchanged production ELF
  confirms the totals above. All **2,935 starting inputs** are audited: 2,929 remain byte-identical;
  five concise documentation index additions and the single graph-cache update
  are checked explicitly. Production source, complete owner object, guard CSV,
  conversion rows, layout, Makefile and linked ELF remain byte-identical.

This is finite allocated-fixture evidence, not unrestricted C aliasing, private
GPR/stack lifetime, full caller execution, instruction-fault prefixes, hardware
or gameplay acceptance. Plane 31 is a backing/shift-width test, not proof that
production callers use it. The native checks cover the initialized carrier
form only. No full Make or production-image rebuild was needed because no
production source or build input changed.

## Neighboring frontier and next work

The 55-word `func_150AE280` slot mixes a handwritten coroutine-resume fragment
with a separate unlabeled ordinary callback at `150AE2A0`. Its ownership must
be resolved before attempting one C body. It was inspected, not changed.

The adjacent private probe of `func_15022024` reproduces [Note 2408](2408-game-group-output-lookup-private-screen-20261114.md):
its output-access-preserving form remains 88 words/frame 8 against retail's
91 words/frame 16. Integer/void argument representations do not change that
emitted body. Its owner's actual profile is O2/g3 with loop unrolling disabled;
the temporary compiler fixture was corrected to keep that compiler-only option
out of asm-processor arguments. No production configuration was defective or
changed. These private probes add no new credit.

Continue `func_150A6760` by recovering its original access/control/register
shape from the checked semantic body and investigating the actual caller's
plane/table domain. Before adoption it still needs full ABI/caller, private
state/fault, both-padder/rebase, actual Make, independent strict-image and
production recount gates. If evidence establishes handwritten provenance,
restore it explicitly under the assembly policy and account for that separately
instead of manufacturing a C match.

```sh
python3 -m unittest tools.tests.test_game_visibility_bitplane_150a6760_screen -v
```

Private artifacts: `conker/build/game-state-handler-150a6760-private/` and
`conker/build/game-actor-range-query-15022024-private/`. The new tools manifest
retains the C bodies, rejected shapes and 98 relevant source/compiler/header/
retail fingerprints; it contains no ROM or compiled binary. Routine Claude
calls: 0. No push, provider change, host import/build or Release change.

Graphify's normal update refused a smaller 27,696-node result and left the
complete 71,819-node graph byte-identical. A scoped AST merge of the four new
Python files adds explicit private-recovery references while retaining every
old ID and qualification. This is not a full-corpus re-extraction. The existing
skill-version and zero-node devcontainer warnings remain. Actual post-commit
producer completion is checked before the final retention audit.

Production ELF SHA256 remains
`b5a050548b5e10f903f01558f1f60c93434b969050f66cfe3989687f2aab8578`.
