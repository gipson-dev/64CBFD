# Mode-Dependent Type Code Complete Match

Verified: 2026-10-18. **Installed complete C match: all 71 words / 284 bytes exact.**

Recover `func_1508E780`, generated_B3020, VA `1508E780..1508E89C`, ROM
`BBC30..BBD4C`, after [Note 1581](1581-route-limit-switch-complete-match-20261018.md).
Consumer predecessor `37e86361`; tools predecessor `943620e`. Bank tools
**8b851a0** first, then consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Replace the zero-return stub with `s32 func_1508E780(s32 type)`. Always load
the current global pointer and signed halfword at +0x16BC before evaluating
the full-word selector. Mode0xB8 selects the small switch: type1 ->0x105C,
type2 ->0x1059, type16 ->0x1019, type8 and all others ->-1. Every other halfword
bit pattern selects the ordinary 9..65 jump table, with its 17 non-default
selectors and default -1. Preserve independent return blocks and the original
source-derived case ordering, including the explicit special type8 block.

Three actual caller sites use the result as a code, testing -1 or stripping
its 0x1000 flag before subsequent calls. Preserve that flag, not just the low
code. Keep the original address name, a full-word parameter and one concise
purpose comment. No original enum/name authenticity is inferred. The earlier
route naming is a working subsystem label, not proof that this is a limit.

The complete ordinary C matches all 71 instructions in isolation, including
the mode load, early range calculation, delay slots and frame0. No volatile,
physical-register binding, inserted/omitted word or scheduling guard.

- Isolated raw SHA: `cf055a9004c6ed7bf1c00be92145c8630235266ad970e093bcec29a930794d37`.
- Full-owner raw SHA in both profiles: `4cad5feeb7d92dbee82d9194ab7bad8689b0830184c9d9c8ffd138d2487f74ce`.
- Four relocation bindings: global HI/LO at +0/+4, table HI/LO at +0x24/+0x2C.

## Table And Owner Layout

The ordinary table is jtbl_8009DB90, VA `8009DB90..8009DC74`, ROM
`242650..242734`, **57 active entries**. Its following three zero words are
alignment, not additional selectors. The isolated pool is 240 bytes including
that tail; all active targets and all alignment bytes match original assembly.

In the full owner, the new table begins at compact pool offset260 /0x104,
after the unchanged eight-byte constant and the preceding switch's 252-byte
table. The old pool is272 bytes including alignment; the new one is496 bytes:
eight constant bytes, 252 prior-table bytes, 228 new-table bytes and eight
alignment bytes. Normalize targets by function/relative offset and verify all
63 earlier targets plus all57 new targets in both compiler profiles.

The existing padder retains original global data. Append exactly two checked
table-ownership bindings: HI16 +0x24 selects jtbl_8009DB90_game; LO16 +0x2C
changes addend0x104 ->0 and selects that same symbol. Check expected instructions
and original .rodata relocation ownership before applying either. Preserve
the entire existing guard prefix byte-for-byte, including the first switch's
bindings. No shared padder, compiler flags, declarations or Makefile changes.

## Fresh Qualification

All **eight corrected pre-install tests pass in 26.791 seconds**; all **eight
final post-install tests pass in 26.619 seconds**, no skips. Final test setup
generates its own full-owner qualification and first-link artifacts rather
than relying on a previous command. Overlapping corpora are not independent
additional coverage.

- Run 1,805 full-word selectors across nine mode patterns and two stack phases:
  **32,490 paired guest executions**. Include special/ordinary/default paths,
  signed mode extremes and low-byte lookalikes such as0x1B8/0xFFB8. Compare the
  independent literal result map and complete modeled GP/FP/LO state, RAM and
  ordered reads. All71 words and57 table entries are visited. Every call first
  reads the global and halfword; only valid ordinary selectors read the table.
- Pass **1,044 fired access-fault pairs**, covering all three access positions,
  both modes, high-byte lookalike mode and both phases. A mapped guest table
  mutation redirects one result to another real return block. This does not
  claim portable mutation of a compiler-owned C read-only switch table.
- In each passing native32 O0, O2 and O2+UBSan build, sweep **all65,536 halfword
  patterns across six probes** (393,216 lookups), then all1,805 full-word
  selectors in both modes (3,610 more). Validate ABI widths, the global and
  current mode after each halfword step, and the bounded state's unchanged
  surrounding bytes at the end. These are numeric host-halfword views with
  the existing no-strict-alias optimization policy, not universal portable
  pointer/alias or arbitrary-state-memory guarantees.
- Five ordinary native source controls complete with expected exit21: byte-
  narrowed selector, low-byte-only mode, wrong ordinary result, missing special
  type1 and lost0x1000 flag. Passing variants exit0; crashes do not count.
- Execute **120 actual two-word caller windows** across three JAL sites and
  both phases. Two pass the selector in the delay slot; the third uses explicit
  live-in A0 and clears S5 in its actual delay slot. The stop trampoline is
  synthetic and the complete caller is not executed.
- Four binding-corruption controls fire the exact stale-word or stale-
  relocation error. Three image-byte mutations fire the actual strict image
  verifier, covering the target and unrelated beginning/end regions.
- Independently assemble the original routine and table. Three GNU maps emit
  identical source/original code and all57 targets plus the alignment tail.
  Execute **150 cases** with rebased code, table and global addresses, including
  HI/LO carries and both modes. No hardware exception behavior is inferred.
- Both owner profiles preserve all72 other routines and the earlier table.
  The actual padder and seven expanded shadow Make commands agree with the
  qualification; the normal-profile projection override remains unchanged.

The initial native negative crashed in harness startup, not in this lookup.
One bounded GDB run of the owned native fixture observes MOVAPS at0804908D
with ESP=FFFFD384, before any lookup call. Use the existing -mstackrealign and
-fno-strict-aliasing harness flags, then re-run all controls and positive
variants. No N64 production fix was needed. The failed20.104-second run is not
an acceptance receipt. No compiler capture was rerun, no REA setup or Claude call.

## Exact Image And Production

Retain the original first private ELF. Its initial target/extent prediction
exposes exactly40 additional metadata bytes. The linked image swaps one
adjacent pair, func_151D77C8 and D_80088874, with their original names, values,
sizes, bindings, sections, adjacency and string positions all checked before
reproducing that exact permutation. All20,313 symbol records remain accounted
for; no metadata section is excluded or broadly normalized.

The literal whole-image prediction changes exactly **257 bytes**: **215 target-
code bytes**, **two target size bytes** (12 ->284), and **40 bounded symbol/string
serialization bytes**. Actual Make reproduces the entire first predicted image.
All6,056 other function bodies, every address, all189,088 protected Game-data
bytes /720 owners and all other frozen inputs remain unchanged.

The shared guard manifest triggers a wider rebuild; it succeeds with existing
duplicate generated_12D630 recipes and warnings from untouched C sources.
Target compiler diagnostics remain empty. The complete build output is retained
in ignored `conker/build/game-route-mode-code/production-build.log`; do not
claim a warning-free build. Existing mixed CSV endings remain intact; the Git
CRLF-to-LF advisory is not an additional content change or build failure.

- ELF SHA: `f384fac3ed0d844cbe5f1c6165ff7ac36a3690bc62c157c7bcf9c63e14728f5e`.
- Owner SHA: `dea4dfd12a77af3cc6f98c79d89b8854f1d6e13b56e83fb0beb7771a3d09daed`.
- Guards SHA: `2bccb21a86652810e61c0522563b25ad229a791c1acc397a8989344810d6816e`.

Fresh matching: **Game2998/4832 (62.04%)**, **total3671/5505 (66.68%)**, Init
**492/492**, Debugger **181/181**, **1,834 different / zero drift**. This replaces
an already-C stub; conversion counts/bytes remain **5505/6044 (91.08%), 86.08%
bytes** overall and **4832/5323 (90.78%), 85.44% bytes** for Game. Exclude repeated
CSV headers. README receives aggregate matching rows only.

Both tools copies pass three setup tests and the smoke check; consumer
`make tools-check` passes. The three new files are identical ASCII/Python-valid.
Preserve all1,313 prior mirror hashes and its ddbdd16 HEAD; add only these three
files, leaving1,316 dirty paths without a mirror commit/reset. Post-commit graph
preservation is a final separate gate in ignored `graph-audit.json` under the
target build directory.

```sh
python3 -m unittest tools.tests.test_game_route_mode_code_match -v
python3 -m tools.experiments.game_route_mode_code_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

This lookup is finished. Next audit `func_1508E89C`, VA `1508E89C..1508EB90`,
ROM `BBD4C..BC040`, **189 words/frame0x50**, currently185 linked differences.
Recover byte/mask gates, full slot arguments with signed-halfword helper
views, ordered flag updates, repeated global-table reads, slot/actor state
transfer and optional script work. All observed return paths set V0=0; qualify
the actual caller interface rather than invent a success flag. Preserve helper
lifetimes, private homes, computed-address null checks and source/destination
ordering before byte-matching credit. Broader Game work stays active; no
sibling host, frozen Release or complete gameplay acceptance claim.
