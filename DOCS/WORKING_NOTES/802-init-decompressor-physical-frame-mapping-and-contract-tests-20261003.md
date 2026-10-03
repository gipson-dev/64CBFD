# Init Decompressor Physical Frame Mapping And Contract Tests

Date: 2026-10-03. HEAD before this work: `47f7ce85`.

## Result

The experimental decompressor now has an explicit physical retail frame view
and nine new tests connecting its scratch arrays to the retained instruction
model. Native C and both IDO guest profiles agree on the complete `0xA88`
layout. This advances the ABI/frame prerequisite identified in
[Note 801](801-init-post-pause-assembly-conversion-assessment-20261003.md).

`tools/experiments/init_decompressor_frame.h` describes physical cells using
fixed-width-on-the-guest integer words, including address/save cells rather
than native host pointers. It is a reference view, not an executable adapter.
The existing semantic candidate still owns a separate explicit state object;
no cast of that state to this frame is valid or introduced.

No production Init owner is changed. Init remains 492 C / 47 assembly rows;
both candidate text sizes remain over the retained decompressor region.
Pending Game recovery source/tests are preserved outside this checkpoint.

## Physical Frame

Offsets below are relative to the shared frame's stack pointer. The core
and fixed initializer each allocate `0xA88`; internal decoder/builder calls
use that same frame rather than allocating ordinary callee frames.

| Offset | Extent | Recovered role |
| --- | ---: | --- |
| `0x000` | 17 words | Length histogram (`counts`) |
| `0x044` | 16 words | Active table addresses (`tables`) |
| `0x084` | 288 words | Sorted symbol indices (`sorted`) |
| `0x504` | 17 words | Canonical offsets / per-level code prefixes (`offsets`) |
| `0x548` | 316 words | Dynamic lengths and fixed-initializer staging |
| `0xA38`, `0xA3A` | Two halfwords | Dynamic literal/code root and distance root |
| `0xA3C`, `0xA40` | Two words | Dynamic root widths |
| `0xA44` | One word | Dynamic/fixed wrapper return address |
| `0xA48` | Eight words | Entry's saved `s0..s7` |
| `0xA68` | One word | Block-dispatcher return address |
| `0xA6C` | One word | Stream-loop return address |
| `0xA70` | One word | BFINAL output |
| `0xA74` | One word | Fixed wrapper's saved workspace |
| `0xA78`, `0xA7C` | Two words | Core entry's saved `fp`, `gp` |
| `0xA80` | One word | Core/initializer entry return address |
| `0xA84` | Four bytes | Trailing space; no semantic field is invented |

The fixed initializer uses only the first 288 length cells for its literal
lengths. Its root/width outputs at `0x9C8`, `0x9CC`, `0x9D0`, and `0x9D4`
overlay length cells 288..291. The header represents this lifetime-dependent
reuse with a union, rather than pretending those are separate allocations.

This explains a concrete difference from the existing candidate: its arrays
have 17 table cells and 320 length cells, totaling twenty more scratch bytes
than the physical regions. It also stores eight scalar fields explicitly,
where retail keeps the connected state in registers/FPRs. Similar overall
object size is not evidence of compatible layout or stack lifetime.

## Register And Representation Mapping

| Candidate field | Retained state | Translation / qualification |
| --- | --- | --- |
| `input` | `s7` | Guest input byte address, not a host pointer value |
| `workspace` | `s6` | Guest table base, temporarily replaced by fixed wrapper |
| `reservoir` | `gp` | Low-word bit reservoir |
| `bits` | `fp` | Available bit count |
| `output` | Integer bits in `f16` | Output base, not a floating value |
| `produced` | Integer bits in `f17` | Published output count |
| `limit` | Integer bits in `f18` | Signed overlap-derived bound |
| `allocated` | Integer bits in `f19` | Four-byte table allocation index |
| `tables[level]` | `sp+0x44+4*level` | Candidate index versus retail `workspace+4*index` pointer |

The scratch tests compare all histogram, sorted, and offset cells; all 316
physical length cells when applicable; and all sixteen table cells after
explicit guest-pointer/index normalization. Extra candidate cells remain
untouched. Cases include empty/all-zero/incomplete/oversubscribed builders,
nonzero allocation append, two dynamic streams, and partial dynamic failure.
These bounded fixtures do not establish arbitrary malformed-tree, capacity,
physical-alias, high-register-word, or FPU-context equivalence.

## Fixture State Correction

The first dynamic scratch comparison failed because `StreamFixture` prepares
fixed tables using a builder that leaves scratch in the same synthetic frame.
The C fixture prepares fixed tables with a separate state, then starts its
stream state with `0xA5` scratch. Unused sorted cells therefore began unequal,
although existing output/state comparisons passed.

The semantic test helper now accepts an explicit scratch seed for this new
comparison. The new calls reset only the model's `0..0xA37` scratch bytes to
the candidate's existing `0xA5` seed after fixed-table setup, before executing
the stream. Fixed workspace contents, register state, return/save cells, and
production code are not altered. Existing tests keep their prior default.
The equal-entry-seed comparison passes; this is a fixture correction, not a
discovered production decompressor algorithm bug.

## Entry And Stack Evidence

A direct J/JAL scan of the pristine Init code interval finds exactly three
transfers from outside `0x10006240..0x100071C7` into that region:

| ROM call offset | Target | Role |
| --- | --- | --- |
| `0x1234` | `func_1000709C` | Startup fixed-table initialization |
| `0x1308` | `func_10006240` | Startup ordinary wrapper |
| `0x5F2C` | `func_1000625C` | TLB/exception caller enters core directly |

This rules out another direct Init transfer to an internal entry in that
scanned interval. It does not cover indirect transfers, other overlays,
external/debugger callers, or reachability of all interior labels.

Instruction-model tests preserve the core's saved cells and distinguish
the three nested return cells. The original fixed initializer's actual words
publish roots/widths `1/7` and `626/5`, finish with allocation index 658, and
restore saved `s0..s7` and its stack pointer. It does not save `gp/fp` to the
core's memory cells; builder FPR saves preserve them along this tested path.

Measured stack low-water across direct/wrapped core paths for reserved-error,
empty-stored, and dynamic streams is `0xA88` / `0xA98` bytes respectively.
This is the bounded instruction-model call chain, not the whole exception
caller, stack ownership, or the nested stack cost of the experimental C.

## Exception FPR Boundary

Static word tests pin the exception caller's additional `0x88` frame and its
sixteen doubleword save/load slots for `f0..f11` and `f16..f19`.
The CU1-set branch at `0x10005EC8` skips the save sequence. After decoding,
the ordinary BNE at `0x10005F40` skips most restores when CU1 was set, but
the `ldc1 f0,0(sp)` at `0x10005F44` is its unconditional delay instruction.
Do not silently treat that instruction as branch-likely or skip it in an
adapter contract. This is a pinned instruction/control-flow observation,
not hardware execution, an established bug, or a repair proposal.

The bounded decoder oracle models low-word integer FPR transfers only.
Original 64-bit FPR state, CU1/FR mode, exception stack ownership, and the
unconditional load's actual contents remain separate qualification gates.

## Reproduction And Verification

```sh
python3 -m unittest tools.tests.test_init_decompressor_frame -v
python3 -m unittest discover -s tools/tests -p 'test_init*.py'
python3 tools/experiments/compile_init_decompressor.py
make tools-check
make -C conker NON_MATCHING=1 all match-progress -j4
```

- Nine new frame/interface tests; all 76 Init tests pass (43.764 seconds).
- Both IDO profiles export all 24 size/offset values correctly. The driver
  rejects a guest layout that differs from the recovered offsets.
- Candidate text remains 4,928 bytes (`-O2 -g3`) / 5,328 bytes (`-O1`),
  entry record four bytes, explicit state 2,668 bytes. Compiler logs are empty.
- Python syntax checks, project tool checks, and whitespace checks pass.
- All 551 project tool tests pass (189.563 seconds), including the preserved
  pending Game tests. This does not finish that Game recovery's own handoff.
- The production build is up to date. Fresh matching remains Init 492/492,
  total 3,271/5,463, Game 2,598/4,790, and Debugger 181/181, with zero drift.
- Independent linked section extraction remains retail-exact: `.init`
  164,048 bytes, SHA-256
  `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`;
  `.init_data` 17,376 bytes, SHA-256
  `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.
- Documentation links resolve; `git diff --check` passes.

README aggregates remain unchanged; no host-port build, Release change, or
gameplay acceptance is claimed. The known duplicate Makefile recipe warning
remains. The frame mapping and assessment are banked separately from pending
Game source/tests.

## Pick Up Here

1. Use this verified physical view to prototype an isolated frame-backed C
   scratch representation. Keep scalar/register state explicit and translate
   workspace addresses versus indices intentionally; do not overlay the
   current owning state object onto the frame.
2. Preserve initializer staging/output alias lifetimes and all nested return
   cells. Test the representation before trying an original-ABI entry adapter.
3. Qualify exception/FPR context and actual workspace/stack ownership. The
   ordinary three-argument entry alone does not settle those contracts.
4. Measure complete adapter plus connected C text and nested stack. Only a
   fitting, semantically/ABI-qualified replacement may change production
   ownership; byte-exact conversion still requires separate matching proof.
