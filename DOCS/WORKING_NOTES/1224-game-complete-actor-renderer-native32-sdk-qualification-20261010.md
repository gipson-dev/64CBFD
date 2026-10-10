# Complete Game Actor Renderer Native32 SDK Qualification

Date: 2026-10-10. Continue the same complete renderer after
[Note 1223](1223-game-complete-actor-renderer-certified-schedule-and-padding-20261010.md).
Consumer baseline 1b048443; mounted-tools baseline e59626e.
Codex is the single writer, zero Claude calls. Tools-first authorized commits,
no push. No host/Release builds, saves or editor changes.

## Scope And Fresh Results

func_1502CCFC: VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC,
532 words / 2,128 bytes; eight arguments and original 0x150 guest frame.
The complete portable C and certified matching recipe are unchanged.
Production still contains its zero-return placeholder. This checkpoint
qualifies native behavior only; it does not install the renderer or add credit.

[Native fixture generator](../../tools/experiments/game_actor_renderer_native32.py)
uses SDK graphics macros extracted from the repository's gbi.h/mbi.h,
not simplified replacement command macros. Its independent reference uses
an explicit little-endian memory adapter for native byte/word overlap.
Original big-endian guest proofs and their immutable baselines stay intact.

[Native suite](../../tools/tests/test_game_actor_renderer_native32.py)
adds five tests. The final combined run with the eight-test
[schedule suite](../../tools/tests/test_game_actor_renderer_schedule.py)
passes all 13 tests in 59.417s:

```sh
python3 -m unittest tools.tests.test_game_actor_renderer_native32 tools.tests.test_game_actor_renderer_schedule -v
make tools-check
```

- 330 complete native cases each at -O2 and -O0: 660 executions.
  Include all 273 prior primary vectors, 45 expanded mask/count/mode cases,
  nine signed-alpha/color cases and three unsigned-maximum-count cases.
- Check every graphics word and returned cursor, full callback order/arity/
  value arguments, distinct aligned color outputs, parameter snapshots,
  complete actor/configuration byte images, live table/count/global mutations
  and the final identity matrix.
- Exercise counts 0, 1, 4, 31, 32, 33, 63, 64 and 65,535. Privately map the
  full-width view fixture in the freestanding native test process; no real
  game state is accessed. Preserve the matrix header within its allocation.
- Reexecute three all-skipped count-65,535 cases separately. Their independent
  oracle is zero-count command/call equivalence; restore the original counts
  in the expected final state. This proves wrapped skipping, not guest fault
  prefixes or memory-access ordering.
- Four freshly compiled complete negatives are effective: wrong fog bit and
  primitive control fail command checks (12), missing tail state fails actor
  bytes (15), wrong lighting pointer fails callback arguments (10).
- A focused pointer-provenance regression preserves scalar 0x20000 even
  though it equals the guest fixture output address. Only typed pointer
  arguments and pointer-bearing command fields are rebound to native storage.
- Production source, linked ELF, guards, progress and rodata hashes remain
  byte-for-byte equal to the original recovery and schedule baselines.
  Fresh schedule tests retain exact whole-owner padding and stale-dependency
  rejection. Project tool checks pass.

Initial native fixture failures exposed a missing SDK DPRGBColor dependency,
matrix-header rebinding and a scalar/address collision. Fix only those fixture
bindings; explicit pointer provenance also avoids rewriting scalar callback
values. Rerun positive profiles and all negative controls after the fixes.
No renderer body, matching recipe or historical baseline is changed.

Callbacks still use explicit bounded ABI/effect models. Native compiler
execution is not proof of N64 private stack homes, FCSR/traps, hardware,
live gameplay, or execution of actual recovered callback helpers.
Matching remains Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%),
zero drift / 2,056 different. Root README aggregate rows are unchanged.

## Bank And Resume

Tools e5f59e3 commits the two new authored files first. Mirror only their
previously absent paths to older tools. Preserve older HEAD ddbdd16 and both
tracked-dirty fingerprints; only the two new mirrors raise native Git dirty
entries from 208 to 210. Do not commit or reset that independent checkout.
Consumer commit banks this note, five concise indexes and the tools pin.
No push. Freshly validate exact mirrors, Python parsing, relative links and
the older checkout fingerprints before banking. Fresh validation passes seven
documents / 4,086 relative links with zero broken links, both exact new mirrors
parsed in both copies, older dirty count 210 and unchanged tracked fingerprints.

Native graphify update refuses the unsafe 39,424 to 17,643-node shrink,
exit 1; retention preserves 19,398 nodes from 2,972 existing excluded files.
Keep version and devcontainer zero-node warnings, no force/purge/install.
Verify fresh detached hook completion and log growth after consumer commit.

Continue this same complete renderer:

1. Connect the complete actual dispatcher/RGB/shading/renderer chain.
   Execute the full original 50-word func_1502CC34 color helper and its actual
   conditional func_1502EC34 contract, plus the actual matrix helper bodies.
   Bounded hooks cannot support a claimed actual-helper execution.
2. Only after connected qualification, install the complete C/guards,
   rebuild and audit the linked ELF, all neighbors/data and guard history
   against the immutable baseline. Measure credit from the fresh build.
3. Keep FCSR/trap, hardware/live acceptance and the separate curve rejection
   gates from [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
   open. The wider Game matching goal remains active.
