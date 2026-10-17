# Microcode Loader Recovery And Matching Boundary

Date: 2026-10-16. Consumer predecessor **9f9e1d9c**, tools predecessor
**44ac318**. Continue the target queued in
[Note 1459](1459-graphics-task-submission-direct-match-20261016.md).

## Status

**Research checkpoint, not an installed conversion.** The complete C candidate
for func_1501CC3C has **97 words / 388 bytes / frame 0x30**, but still differs
from retail at **44 words**. No source installation, guards, compiler-profile
changes, linked-image changes or matching credit. The production routine is
still its zero-return stub. Keep this same target active.

Owner: conker/src/game/generated_49D30.c. VA **0x1501CC3C..0x1501CDC0**,
ROM **0x4A0EC..0x4A270**. Preserve the existing **O2/g3/no-unroll** profile,
S0/RA homes, range pointer **SP+0x20**, paired offset **SP+0x28**, and variant
**SP+0x2C**. The candidate's interface is void with no interpreted arguments.
Changing its declaration leaves all **239 direct words of func_1501C880**
and all **56 other raw owner functions/bindings** unchanged.

## Recovered Contract

- Load the unsigned byte at D_800B0DF0 + 0x2B into a promoted **s32 local**.
  Start with paired offset four; values at least two subtract two and select
  offset zero. Add two only when the complete D_800BEB98 word equals **one**.
- Interpret D_80084078 as four 32-bit offsets per 16-byte record: text start,
  text end, data start and data end. The real table contains **eight records**,
  pinned against ELF/ROM bytes at ROM 0x228B38..0x228BB8.
- Compare the local variant/offset against **signed cache bytes** D_80084070
  and D_80084074. A hit performs no DMA or pointer/cache writes. A high
  unsigned variant cannot hit the same raw negative signed-cache byte.
- On a miss, load primary text into D_800C1060, primary data immediately
  after the reloaded text span, paired text into D_800BEBB0, then paired data
  after its reloaded text span. Device addresses add the **address** D_2D4B0,
  not its contents. Every func_10004514 packet has blocking argument one.
- Reload the primary row after the first DMA and paired row after the third
  DMA. Publish D_800BEB9C and D_800BEAD0 before their data transfers. Publish
  cache bytes after the second DMA, before the paired text transfer. Keep
  the original variant and paired offset across provider callbacks.

The alternate source's draft is a reference only, not byte-exact imported C.
The existing Init DMA provider is inspected and fingerprinted, not modified.
Direct retail callers are func_1501C880 and func_15007B3C; caller execution
and complete startup acceptance remain separate gates below.

## Source Fitting

The experiment retains **42 measured source forms** across ten screen groups.
These are source configurations, not 42 distinct emitted objects.

| Source shape | Words | Frame | Retail differences |
| --- | ---: | ---: | ---: |
| Initial u8 local and persistent offset | 102 | 0x38 | 100 |
| Promoted word local and persistent offset | 97 | 0x38 | 77 |
| Inline offset expressions | 96 | 0x30 | 84 |
| Explicit paired-offset else branch | 97 | 0x30 | 46 |
| Signed span grouping, selected checkpoint | 97 | 0x30 | 44 |

The selected raw SHA-256 is
**e4b491e01ea802d65e7e042abe7a8a42a84923d6b00f833fbf35a15ecd149e0f**;
pin all **34 relocation bindings** and reject private pools. Both the raw
and normal padded experimental objects retain the same 44 differences.
No guard manifest is generated or edited.

The first remaining difference is the table-address temporary at **+0x30**.
Differences also include spill ordering, primary data-pointer publication,
and paired-index arithmetic: the candidate distributes two shifts, whereas
retail adds the indices before shifting. Do not describe all 44 as independent
scheduling words or blindly replace them. Named pointer/start carriers,
declaration reordering, scoped/register locals and signed/pointer table forms
have not improved this checkpoint; some change frame size or saved lifetimes.
The detailed word pairs are in the ignored target qualification receipt.

```sh
python3 -m tools.experiments.game_microcode_loader --qualify
python3 -m tools.experiments.game_microcode_loader --screen grouped
python3 -m tools.experiments.game_microcode_loader --screen tables
python3 -m unittest tools.tests.test_game_microcode_loader -v
```

Other screen names: initial, forms, inline, lifetimes, locals, registers,
scopes and ordering. Run producers sequentially in the target build directory.

## Fresh Qualification

All **seven final research tests pass in 15.679s**:

- GNU-assemble the complete original 97-word routine and compare all bytes
  with retail. Preserve all 56 raw neighbors, including the matched caller.
- Run **770 original-and-candidate selector/cache cases**, each against an
  independent ordered reference. Cover two stack phases, unsigned high input
  bytes, signed cache hits/misses and full-word flag distinctions. All 97
  instruction positions execute in both versions.
- Run **80 callback cases**, with every requested DMA mutation gate positively
  fired. Check live table reloads, cached local lifetimes, data-pointer and
  cache publication timing, and provider changes that must persist.
- Run **24 cases with the real eight-record table and actual transfer lengths**.
  The larger 260-row high-byte fixture is explicitly synthetic. All payload
  bytes are deterministic test data, not the original microcode contents.
- Reject **two compiled/executed functional controls**: unsigned cache
  comparison and a nonzero rather than exactly-one flag. Do not count compiler
  failures, signals or unmapped memory as successful negative controls.
- Reject all 97 word corruptions, 34 binding corruptions plus an extra binding,
  private pools and stale source anchors. All **135 live input hashes** remain
  equal to the recorded production baseline.
- Qualify the local oracle's added signed-byte load with **eight vectors**,
  including negative address offsets, sign extension and register-zero writes.
  Shared machine helpers are unchanged.

Compare complete final public memory, ordered DMA packets and cache/data-pointer
snapshots at each call. **Literal GPR/private-stack/instruction-trace equality
and fault-prefix equivalence are not claimed** for this non-matching candidate.
The DMA byte-copy/ABI hook is bounded; PI hardware, cache coherency, OS queues,
native execution and natural gameplay are not emulated or accepted here.

Windows parses all three task files in both copies. WSL passes all eleven
shared padder tests in each copy: active **0.033s + 0.020s**, mirror
**0.029s + 0.019s**, no skips. Windows alone skips assembler-dependent tests;
those skipped runs are not qualification. Consumer tools-check passes.

Tools **932b4de** banks the three research files before the consumer pin.
Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **928**
initial dirty-file hashes and **931** final dirty paths; all three added file
pairs match. No mirror commit/reset, push, host-port or frozen Release action.

## Next Gates

- [x] Recover and test the full semantic candidate without installing it.
- [x] Bank the research tools and concise consumer handoff, preserving production and the older mirror.
- [ ] Resolve the same function's 44-word boundary, retaining its frame, homes, no-unroll profile and raw neighbors. Do not patch a different frame or call-save lifetime into a match.
- [ ] Complete native32, independent rebases, real caller/provider-chain qualification and applicable ordered/fault checks after the source fit settles.
- [ ] Reproduce the predecessor and independently predict the entire new ELF before installation; install only after the focused gates pass.
- [ ] Complete normal build, installed audit, fresh progress measurement and tools-first banking. Root README gets aggregate rows only.

Production ELF remains
**5ae0082dd77652314c8e63569a43439a330d133b749907fa5db2d5b76fe41d9e**.
Because all source/image/guard/progress inputs are literally unchanged, retain
Note 1459's measured Game **2,936/4,828 (60.81%)**, total **3,609/5,501
(65.61%)**, different **1,892**, zero drift and conversion **5,501/6,044**.
These are preserved measurements, not a newly rebuilt progress report. Root
README is unchanged. Timing's 141 differences and wider Game remain open.
