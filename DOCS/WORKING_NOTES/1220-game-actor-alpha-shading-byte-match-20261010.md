# Game Actor Alpha Shading Byte Match

Date: 2026-10-10. Continue the RGB/dispatcher chain from
[Note 1219](1219-game-actor-rgb-parameter-writer-direct-match-20261010.md).
Codex is the single writer; zero Claude calls. Keep tools-first commits,
no push, host/Release build, saves, editor changes or older-tools commit/reset.

## Installed Complete Caller

func_1502D630, VA 0x1502D630..0x1502D824, ROM 0x5AAE0..0x5ACD4:
all 125 words / 500 bytes now match retail in the actual linked ELF.
[Production owner](../../conker/src/game/generated_58F80.c) replaces the
zero-return placeholder with the full typed void actor/RGB-array/view caller.
The dispatcher ignores v0. Only alpha at parameters +0xC is written;
RGB remains untouched by shading.

Keep separate initial reciprocal variables and final endpoints. Each global
zero/signed-zero denominator uses its retained 0.001f fallback. Compute the
ordered single-precision difference scaled by the retained 0.001f, then the
two endpoints using unsigned halfwords explicitly promoted through u32.
Matrix selection uses the full 32-bit view shifted by six, not a narrow view.

The transformed fourth coordinate is reciprocated with a third zero fallback.
Retail gates are directional: negative reciprocal means factor zero;
end <= reciprocal also means zero; reciprocal <= start means one; otherwise
factor = (reciprocal - end) / (start - end). Alpha truncates
(1.0f - factor) * 255.0f. The initial candidate reversed both inclusive
comparisons; independent instruction decoding corrected them before closure,
behavioral qualification or installation. Effective negative controls reject
those exact reversals.

Original 0x58 frame: RA +0x24; private matrix outputs x/y/z/w at
+0x40/+0x3C/+0x38/+0x34; captured start/end at +0x50/+0x54;
incoming actor/output/view at +0x58/+0x5C/+0x60. Retain reciprocal stores
to the escaped w local, its original reload order, and final truncation.

## Actual Matrix Contract

func_150A7A00 is a five-word handwritten wrapper, not an ordinary RA-preserving
leaf. It copies its incoming RA to t9, loads RA with func_150A7A14 and jumps
to the 40-word func_150A7960. That helper writes x/y/z; the 13-word continuation
writes w and returns through t9. This caller's saved RA and epilogue safely
cover the special return lifetime.

All 58 actual linked helper words equal their corresponding ROM words.
Focused tests execute the entire wrapper/helper/continuation chain, never a
matrix hook. Keep its pairwise matrix association (a*x + b*y) + (c*z + d),
with rounding after each operation, rather than reassociating four terms.

## Closed Matching And Fresh Proof

[Candidate helper](../../tools/experiments/game_actor_alpha_shading_candidates.py)
measures complete forms; separating reciprocal/endpoints and ordering their
declarations recovers the original frame and all private homes.
IDO O2/g3 emits 121 words, zero diagnostics and new pools.
[Matching helper](../../tools/experiments/game_actor_alpha_shading_matching.py)
closes all 121 raw words and 19 relative relocation entries.

121 guards: 16 changed replacements, 105 unchanged dependency rows,
four inserted setup words, zero omissions and zero missing-body padding.
Split zero and one into their retail FPU registers after the real matrix call;
place copies of existing constant producers in the two reciprocal arms,
retain the original separation NOP, and carry the fallback relocations to
their recovered positions. The recipe derives instructions from compiled
producers and does not read the ROM to generate replacements. The complete
first 74 raw words already match apart from normal unresolved relocations.

[Focused suite](../../tools/tests/test_game_actor_alpha_shading_match.py)
passes all nine tests before installation in 17.729s and after in 17.371s.
An earlier test-only unbound-super delegation failure in the connected oracle
was corrected before the passing pre-install run; no production change was
made to accommodate it.

- 703 guest cases / 2,109 executions compare independent alpha/matrix reference
  with original/raw/current instructions. Full memory/events agree, including
  private homes. Check zero/signed-zero denominators, unsigned cut boundaries,
  inclusive clamps, adjacent float bit patterns, signed/full-width view,
  actual matrix arguments, saved GPR/FPR/RA/SP and two stack phases.
- 1,728 nonfinite edge cases qualify bounded reference/original/raw/fitted
  behavior, including infinities and NaNs. The oracle explicitly models invalid
  truncation as integer-indefinite 0x80000000. Actual FCSR flags, traps,
  signaling NaN handling and hardware NaN payloads are not claimed.
- 24 private aliases include actor reads overlapping incoming/private/saved
  homes and the final alpha destination overlapping matrix outputs/endpoints.
  Test cancellation-sensitive matrix association with the actual helper bodies.
- 358 verified full access-fault prefixes / 1,074 executions preserve complete
  original/raw/current memory and trace prefixes. Include private aliases and
  both stack phases; every requested fault gate fires. These qualify emitted
  guest order, not portable C fault semantics.
- Nine independent assembled links / 54 cases under three symbol sets exercise
  signed LO16 carries and exact original/fitted instructions. Reject all 121
  damaged words both in the closed recipe and actual padder. Reject all 19
  stale expected relocation entries in the actual padder.
- All 37 copied-owner neighbor bodies/relative relocations and decoded pools
  remain exact, including the corrected-prototype dispatcher and RGB writer.
  Copied target guards equal isolated guards. Actual owner padding changes
  only the target 500-byte slot, with no new compiler diagnostics.
- 203,972 actual native32 complete-C cases use a bounded four-output matrix
  model and valid/disjoint finite inputs. Exercise both unsigned cuts across
  all 65,536 values, reciprocal/clamp combinations, four views and untouched
  RGB sentinels. Native invalid-conversion or FCSR behavior is not inferred.
- Seven fresh effective complete compiled negatives distinguish both reversed
  gates, signed-halfword error, wrong output slot, blend sign, fallback and
  actor-coordinate read.
- 168 complete banked dispatcher connections execute all 176 caller words,
  the real 57-word RGB writer, the complete shading body and all 58 matrix-chain
  words. Cover first/last slots, two views, all seven modes, two stack phases
  and three transformed-w paths. Verify the renderer's full RGBA arguments,
  whole memory/events and returned cursor. Other callbacks remain explicitly
  bounded opaque; this is not whole-game or renderer acceptance.

Fresh full build succeeds. The global guard dependency causes broad normal
recompilation; preserve the known duplicate generated_12D630 recipe warning
and existing outside-target pointer/type/long-double warnings. Target isolated
and copied-owner compilation is clean; no warning-free full-build claim.
Fresh tools-check passes.

Whole linked audit permits only target 500-byte instructions and symbol extent
to change, plus regenerated debug metadata. Every other protected linked
byte/address/extent is exact. Prior guard bytes remain an exact prefix;
conversion CSV and retained rodata are byte-identical. Protected .game_data
remains 189,088 bytes / 720 owners with zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh matching: Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%),
zero address drift / 2,056 different. Converted counts/bytes unchanged;
root README changes only the two aggregate matching rows.

## Bank And Resume

Consumer baseline 2be68afa; mounted-tools baseline b216274.
Before-source SHA-256:
921b3fff5e41a7abdc112fb4ba249dcdc9fc17765730132f6590df357ba13f86.
Immutable baseline, candidates and fresh receipts remain in
conker/build/game-actor-alpha-shading-match-test/ and
conker/build/game-actor-alpha-shading/.
Do not replace previous dispatcher/RGB baselines to accommodate a later
neighbor's installation. Fresh copied-owner and connected proofs cover this
change; earlier unchanged receipts remain historical.

Tools 89e8ece commits the three new authored files first. Mirror only their
previously absent paths into older tools. Older HEAD ddbdd16 and its two
tracked-dirty hashes remain exact; dirty entries rise 199 to 202 solely for
these new mirrors. Bank source, generated rows, concise indexes, aggregate
README and consumer pin next. No push.

Manual native graphify update exits 1 refusing a 39,394 to 17,613-node shrink.
Retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Preserve
version/zero-node warnings; no force, purge or install. Verify fresh detached
consumer-hook workers and log growth after commit.

Next full target: func_1502CCFC, VA 0x1502CCFC..0x1502D54C,
ROM 0x5A1AC..0x5A9FC, 532 words / 2,128 bytes, original 0x150 frame.
Recover the complete eight-argument actor renderer, including its model/tier
selection, graphics commands, callbacks, alpha/RGB/matrix inputs and all return
paths. Use existing SDK graphics macros and real banked helpers; do not
replace only the early gate or substitute a reduced renderer. Qualify the
complete dispatcher/RGB/shading/renderer chain before installation.
Preserve the separate uninstalled curve gates from
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and hardware/live acceptance remain open.
