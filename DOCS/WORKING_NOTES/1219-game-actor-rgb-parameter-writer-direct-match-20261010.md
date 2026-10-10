# Game Actor RGB Parameter Writer Direct Match

Date: 2026-10-10. Continue the complete dispatcher from
[Note 1218](1218-game-actor-render-dispatch-byte-match-20261010.md).
Codex is the single writer; zero Claude calls. Tools-first commits, no push,
host build, Release, saves, editor changes or older-tools commit/reset.

## Installed Routine

func_1502D54C, VA 0x1502D54C..0x1502D630, ROM 0x5A9FC..0x5AAE0:
all 57 words / 228 bytes match directly from complete semantic C.
[Production owner](../../conker/src/game/generated_58F80.c) now has the typed
void slot/output contract. The actual dispatcher ignores v0; it does not
require a fabricated return value. Original frame-free leaf, no new pools,
guards, insertions, omissions or missing-body padding.

Compute the actor address with the low 32-bit slot product and 0x32C stride.
When actor byte +0x66 masked by 0xC equals 4, average the unsigned byte pairs
+0x1DD/+0x1E0, +0x1DE/+0x1E1 and +0x1DF/+0x1E2 with signed integer division
by two, store intermediate RGB, then complement each channel with 255.
Otherwise write white in reverse output order: blue, green, red.
Alpha at output +0xC is untouched.

The source's commutative addition operand order recovers the retail physical
byte-read schedule. Do not collapse the intermediate stores, output reloads,
or chained white stores: output can alias the actor. Full raw emission is
exact, including the final blue store in the JR delay slot, six unreachable
negative-sum correction words and the ordinary unreachable constant at index
51. Reachable coverage is 50/57; unsigned byte sums cannot take the signed
negative correction paths. Preserve those emitted original words.

## Fresh Qualification

[Candidate helper](../../tools/experiments/game_actor_rgb_parameters_candidates.py)
reuses the existing isolated IDO compiler/parser.
[Focused suite](../../tools/tests/test_game_actor_rgb_parameters_match.py)
passes all nine tests before installation in 9.992s and after in 13.845s.
The initial test-fixture run exposed a C89-invalid negative-control declaration
and a miscounted green correction index; those test-only errors were fixed
before qualification and production installation.

- 1,683 guest cases / 5,049 executions compare independent ordered reference,
  original, complete raw C and current linked target. Cover all 256 flag bytes,
  signed/wide slot values, color boundaries and two stack phases. Check full
  memory/events, no leaf calls, and saved GPR/FPR/RA/SP preservation.
- 1,248 alias cases cover every aligned output offset from actor -0xC to
  +0x330, both stack phases and special/default flags. Include overlaps with
  actor flags and source colors, not only disjoint RGB buffers.
- 115 verified access-fault prefixes / 345 executions check original/raw/current
  full events and memory. Every requested gate fires, including actor/output
  and stack aliases. These qualify emitted guest instruction order, not
  portable C fault semantics.
- Nine independently assembled links under three entry/base symbol sets
  exercise signed LO16 carries. All original/raw/padded words agree exactly;
  54 linked semantic/alias cases agree. No replacement instructions generated
  from the ROM, and no normalization manifest needed.
- All 37 copied-owner neighboring bodies and relative relocations remain
  exact, including the dispatcher despite its corrected RGB declaration.
  Pools agree, copied target equals isolated target, target diagnostics are
  zero, and actual owner padding changes only the target 228-byte slot.
- 336 complete banked 176-word dispatcher connections execute the original,
  raw and current RGB bodies, never a leaf hook. Cover first/last slots, two
  views, seven modes, two stack phases, three flags and shading enabled/disabled.
  Verify renderer RGB and alpha plus whole memory/events/returned cursor.
  Other callbacks remain explicitly bounded opaque; no whole-game claim.
- 399,872 actual native32 complete-C cases check all 26 slots and 256 flags,
  every byte pair for every channel at first/last slots, and the alpha sentinel.
  Native inputs are valid and disjoint; guest probes carry alias/fault evidence.
- Seven fresh effective complete compiled negative controls distinguish wrong
  flag, average, inversion, blue byte, alpha write, white store order and red
  load order. Public results and physical traces are separately discriminating.

Fresh full build succeeds. It recompiles the owner without diagnostics and
retains the known generated_12D630 duplicate-recipe warning. Fresh tools-check
passes. The whole linked audit allows only target 228-byte instructions and
symbol extent, plus regenerated debug metadata. Every other protected linked
byte/address/extent is exact. Guard history, conversion CSV and retained
rodata are byte-identical. Protected .game_data: 189,088 bytes / 720 owners,
zero byte/owner differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh match-progress: Game 2,759/4,816 (57.29%), total 3,432/5,489 (62.53%),
zero address drift / 2,057 different. Converted functions/bytes unchanged.
Root README changes only the two aggregate matching rows.

## Bank And Resume

Consumer baseline 47872648; mounted-tools baseline 2136f14.
Immutable target baseline and receipts:
conker/build/game-actor-rgb-parameters-match-test/.
Before-source SHA-256:
86c3f740f17af6789f8b04a5761f14174126c490fa717fcd974a0cc6cbf25090.
Existing dispatcher baselines and historic suite receipts stay unchanged;
fresh neighbor/body and connected-caller evidence qualifies this change.

Tools b216274 commits the new candidate helper and nine-test suite first.
Mirror only those two previously absent authored files into older tools;
older HEAD ddbdd16 and its two tracked-dirty fingerprints remain unchanged.
Older dirty entries rise 197 to 199 solely for these new mirrors. Commit
source, concise indexes, aggregate README and tools pin together; no push.

Scoped validation passes: 41 documents / 4,234 relative links, zero broken
links and 71 exact authored tool mirrors parsed in both copies. Older HEAD
and tracked-dirty fingerprints remain exact.

Manual native graphify update exits 1 refusing a 39,387 to 17,606-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Preserve
the existing version and zero-node warnings; no force, purge or install.
Verify fresh detached consumer-hook workers and log growth after commit.

Next full target: func_1502D630, VA 0x1502D630..0x1502D824,
ROM 0x5AAE0..0x5ACD4, 125 words / 500 bytes, original 0x58 frame.
Recover ordered reciprocal/range blending and alpha output, floating-point
rounding/edge behavior, retained constants and physical private outputs.
Inspect its actual func_150A7A00 matrix-helper entry/return contract rather
than assuming a conventional function ABI. Then qualify its complete
connection to this dispatcher before installation. The 532-word renderer is
still separate. Preserve the uninstalled curve rejection gates from
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and hardware/live acceptance remain open.
