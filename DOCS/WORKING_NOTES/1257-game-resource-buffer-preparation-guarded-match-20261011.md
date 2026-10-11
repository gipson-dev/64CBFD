# Game Resource Buffer Preparation Guarded Match

Date: 2026-10-11. Continue
[Note 1256](1256-game-resource-buffer-retail-length-improvement-20261011.md)
under [the agent workflow](../AGENT_WORKFLOW.md). Single Codex writer,
zero Claude calls. Keep the full Game matching goal active. Authorized
checkpoints are committed tools-first, without pushing.

## Target And Baselines

- func_15084044: VA 0x15084044..0x1508434C, ROM 0xB14F4..0xB17FC.
- Full retail body: 194 words / 776 bytes, frame 0x60.
- Owner conker/src/game/generated_AEB40.c; retail conker/asm/AEB40.s.
- Consumer entry HEAD: 9e6e6bdabf7ad2a62b7608f5035a6b33f81a9ce8.
- Mounted tools entry HEAD: 2a4183d396f054401de85c2647d78c4805eaae78.
- Both active checkouts clean at entry. Older standalone tools remains at
  ddbdd16b53ce60b054fb6e11bf0649a41f48375a, 282 dirty entries.
- Previous complete C: 194 words/frame 0x60, 39 raw differences, no guards.
  ELF d543a0960902f688cb569ca95d96e563b105f2ff37ff1a8dc7a73f62d1987056.

The previous turn was verified progress, not a wait or no-progress turn.
Reread full assembly, current C and sole direct retail caller func_1503DA9C.
The selected body still implements every recovered sharing/allocation/copy/
failure path. It is not a zero-return skeleton or a ROM-word C wrapper.

## Source And Screening Evidence

Only three source lines change in the mode-two successful-allocation path.
After dispatch has selected mode two, the mode word is no longer needed as
an enum. Reuse this 32-bit word for the live destination load, test against
zero and cast it back to void * for bcopy. This recovers a shorter scratch
lifetime without changing width, memory access, helper ABI, frame or loop
bound. It is an O32 pointer-bit round trip, not portable 64-bit host code.

| Complete Candidate | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Committed body | 194 | 0x60 | 39 |
| Explicit parent selector in mode word | 194 | 0x60 | 39 |
| Reuse first-buffer local for loop copy | 194 | 0x60 | 33 |
| Reuse dispatched mode word, selected | 194 | 0x60 | 29 |
| Distinct block-local destination | 195 | 0x68 | 72 |
| Separate source plus channel/offset reuse | 195 | 0x60 | 194 |
| Inline loop destination expression | 194 | 0x60 | 36 |
| Inline both destination expressions | 194 | 0x60 | 29 |
| First-buffer integer type | 194 | 0x60 | 39 |
| Config integer type | 194 | 0x68 | 47 |

Twenty-four declaration permutations preserve the 36-difference expression
variant; unsigned mode and void * config do not improve it. Byte/halfword
mode types add a word and worsen differences. Address casts and reversed
pair expressions likewise do not recover the remaining allocation. Preserve
the complete experiment sources/results in ignored build output.

A numerical decrease was initially misread as recovery of the copy branch.
Full disassembly disproved that inference: the smaller raw candidates still
use beql. Corrected the user update before installation. Do not reuse the
earlier interpretation as evidence. A generated struct-member rename and
module initialization order were also corrected before qualification.

## Bounded Normalization

Raw C remains 29 words different. All 194 production linked words now match
retail after 29 explicit expected-word/relocation guards. This is a guarded
match, not a direct C match: 165 raw words already match without normalization.

- Twenty-six guards change only integer register fields. The generator
  verifies unchanged opcode, function, shift amount and every immediate/
  displacement bit. It closes actor/channel preservation, mode/config/source
  lifetimes and two commutative address operand orders. Retail preserves
  actor in A2 and channel in A1; the compiler preserves actor in A0/channel
  in A2. Retail mode is V1 rather than A1, cached source A0 rather than V0.
- Three guards at +0x290/+0x298/+0x29C recover the destination in V0,
  ordinary beq and move to A1 in its delay. The unnormalized compiler uses
  A1, beql and a shared-source load in the delay. The existing fallback load
  remains at +0x2B0, with the same ordered access on the zero path.
- Require the exact 29-offset set and exact four-word copy window (including
  unchanged +0x294). No inserts, omissions, new calls, stack/pool rewrite,
  immediate change outside the explicit branch schedule or relocation change.
- All guarded locations have empty relocation lists; both '-' fields are
  checked. Preserve every old guard byte and append only these 29 rows.

The coupled entry handoff and live-range mappings are checked against the
complete original routine, not justified merely by a register mask. Raw
behavior/access/fault tests pass before normalization. Independent rebases
then verify the actual padded body, with stale guards failing closed.

## Fresh Qualification

First, the selected raw body passes nine behavioral/owner/native/SDK/caller
gates in 26.550s without production edits. All fourteen pre-install tests
then pass in 42.207s. Add sixteen high-bit destination/failure cases before
the final run; all fourteen post-install tests pass in 51.900s.

- 7,424 core cases / 14,848 original-C runs, 172 original words reached;
  complete private/public memory and access-order equality.
- 912 parent/channel/size/mutation/high-bit cases / 1,824 runs. Destinations
  0x90024000 and 0xF0025000 exercise sign-bit round trips, successful copying,
  null failures and second-allocation cleanup at both stack phases.
- 3,632 all-access fault pairs, every gate fired, complete partial memory,
  access and call receipts equal. Guest faults are not portable C guarantees.
- 27 original/raw/padded links across three normal symbol sets plus aliases,
  43 cases. Global short circuits and signed-LO carry/rebases remain checked.
- Eight effective freshly compiled IDO semantic negative controls.
- Actual complete native32 C: 12,288 cases at each O2/O0, 24,576 total,
  plus effective wrong-count control; pointer/int widths both four bytes.
- All 30 owner neighbors preserve bytes, extents, relocations and pools;
  no owner diagnostics, both real padding routes preserve non-target bytes.
- Actual Init allocation wrapper/bcopy: 144 cases/288 runs, 207 connected
  words, 72 reached. Normalize only genuine saved continuation PCs; core/
  free callbacks remain bounded, not hardware-heap acceptance.
- Complete original caller: 576 cases/1,152 runs, all 104 words mapped but
  only 60 reached. Forwarding/failure propagation passes within the earlier
  loader-callback and extras-zero-count bounds; no full caller acceptance.
- All 29 guard words and relocation lists are corrupted separately through
  each padder: 116 fired rejections, not unexercised negative fixtures.
- Three immutable baselines retain original stub, 192-word recovery and
  preceding 194-word body. Never overwrite their saved bytes/JSON manifests.

Commands from 64CBFD:

```sh
wsl --exec python3 -m tools.experiments.game_resource_buffers_registers --guards
wsl --exec python3 -m unittest tools.tests.test_game_resource_buffers -v
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Guard-manifest dependencies trigger a wider object rebuild; it succeeds.
Preserve unrelated pointer/integer/long-double warnings and the duplicate
generated_12D630 recipe warning. The target copied owner remains diagnostic
free. Mounted and older standalone WSL checks pass; native py_compile of the
new older-mirror experiment passes. No fresh native full-check success claim.

## Complete Linked Evidence

Only 47 ELF bytes change from Note 1256, all inside the target slot. Every
other ELF byte is literally identical, including all other code/data/pools,
headers, sections, symbol/string tables and target extent (still 776 bytes).
All 194 target words equal retail. The preceding 192-word baseline differs
by 354 bytes (353 target, one extent byte); the original stub differs by
621 bytes (583 target, 38 extent/existing metadata-order bytes), with its
structured symbol/name equality checks retained.

- ELF SHA-256: 5b1d021e64d52f5aec54232e046d41b8024c7310729aa386ac2df5fe0dc49979.
- Owner SHA-256: 346dfa12ea5ec1b3eb0ac85543194f3f9e12f76595ac870f91c91fbb3ff69201.
- All 189,088 data bytes / 720 owners exact, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guard file SHA-256: 5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
  Every old byte retained; only the 29 target rows append. Mixed historical
  line endings are preserved, not reformatted to hide guard-history changes.
- Conversion CSV unchanged: 32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
  Rodata source/layout/tracked symbols/ignored auto assignments unchanged.

Fresh matcher: Game 2,787 / 4,822 (57.80%), total 3,460 / 5,495 (62.97%),
Init 492 / 492, Debugger 181 / 181. Zero drift, 2,035 different.
Only +1 matching credit; no new conversion. Root README changes only the
matching aggregate rows, not the function narrative or converted percentages.

## Ownership And Graph

Tools commit 8e07c9e4e9a6fe305f31e26258fd3253639a8a8a banks the new
experiment and focused test evolution before the consumer pin. Older HEAD
and all five protected existing file hashes stay unchanged. Copy only absent
experiments/game_resource_buffers_registers.py, SHA-256
98473D81B0B8DB105233DDA02D7DE8A6A43D43D17BB8E2854DC0BF986F4BAC71;
older dirty count 282 -> 283. Do not overwrite its independently dirty test,
previous modules or helpers; no older commit/reset or push.

Native graph query succeeds. Native update extracts two files but refuses
unsafe shrink 39,718 -> 17,936, preserving 19,398 nodes from 2,972 existing
excluded files. Keep version/zero-node warnings, no force/purge/install.
After consumer commit, require fresh rebuild-log bytes/UTC, a fresh Rebuilt
tail and zero actual Graphify/Python workers. No OGL/Release/save/editor/
private-input changes apply; Release remains frozen.

## Next Full Caller

Recover func_1503DA9C next: VA 0x1503DA9C..0x1503DC3C, ROM
0x6AF4C..0x6B0EC, 104 words/frame 0x48, generated_6A3D0.c.
Live C is still a zero-return stub. Preserve the complete original scope:

1. Word identity/channel/extras ABI and actor/config load order; absent main
   resource forwards all five loader arguments, including actor byte +0xAC.
2. Existing resource path's config +0x18 bit 0x4000 / actor +0xAC bit one
   auxiliary gate and D_800C5C08 cache check before func_150028BC.
3. Extras gate, unsigned count D_800C5628, and unsigned descriptor-word
   threshold 0x10000000 before func_1503DC3C.
4. Live D_800C4778 count and D_800C4488 list-base reload around every
   func_1510CE60 call, retaining five arguments (entry,0,0,0x3E,0).
5. Invoke the now-exact func_15084044 only when the loading result is zero;
   forward actor/channel and propagate helper failure/result unchanged.
6. Extend coverage beyond the earlier 60 reached words with full flags,
   extras, count/list mutations, loader failures, aliases and fault prefixes.
   Reuse the proven guest/native/owner/padder/ELF gates, not a broad stub batch.

Direct guard elimination remains a separate compiler-recovery improvement.
Actual deeper loaders, heap, hardware, renderer and gameplay are still open.
Do not mark the full Game goal complete for this one guarded match.
