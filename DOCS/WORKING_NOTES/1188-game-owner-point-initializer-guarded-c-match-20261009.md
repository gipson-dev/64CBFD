# Game Owner Point Initializer Guarded C Match

Date: 2026-10-09

## Installed Result

Replace func_151B3A7C's zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) with the complete
semantic ten-point initializer. VA 0x151B3A7C..0x151B3CF0, ROM
0x1E0F2C..0x1E11A0: all 157 linked words / 628 bytes match retail.

Retain the original 0x60 frame, SP+0x44 private position and SP+0x08 saved FP
pair. Actual actor prefix is 0x138 bytes; ten records are 24 bytes each.
The second vector is zeroed; the candidate field name velocity is not proof of
its runtime meaning. Keep three independent scales, repeated binary32 additions,
fresh final flags read, only bit 2 cleared and success return 1. Actual
D_8008FAF8[0] one-argument callback registration is unchanged.

## Closed Normalization

The complete Note 1187 raw C emits 158 words / 110 differences. A certified
two-pass control rewrite omits only the dead SLT result at raw offset 0x238
and replaces the branch at 0x254 with direct counter/end inequality. Counter
starts 2, advances 4, and is tested at 6 and 10; loop target 0x11C and delay
store are preserved. This fits 157 words / 98 differences without padding.

The complete matching recipe then applies a closed GPR role map, complete
43-word setup and 28-word loop permutations, ten actor-relative address folds
and isolated scratch lifetimes. It never synthesizes output by reading retail.
Retail is consulted only for the final measurement. The actual padder installs
99 relocation-aware expected-word rows: one omission, zero inserted words,
no frame/private-home patches. All six HI/LO relocation uses are retained.

Complete symbolic qualification uses byte-addressed memory and ordered FP-bit
expression trees for both loop passes: all raw 158 and normalized 157 words
are reached. All final bytes, read/write multisets, branch decisions/targets,
saved registers, FP expressions and return compare across 61 actor views,
including every aligned scale/output overlap. The private frame is disjoint
from public live objects. Memory access order, hardware, FCSR and FP exception
order are explicitly not claimed.

## Fresh Qualification

Command: python3 -m unittest
tools.tests.test_game_owner_points_initializer_match -v.

Pre-install: 14 tests pass in 17.504s. Installed final run: 14 tests pass in
19.579s, zero skips. Raw C is a separate third body, not a retail-equal substitute.

- 2,048 guest cases / 6,144 executions: all flag bytes, four geometry sets,
  two stack phases; all words in original/raw/normalized reached.
- Native32 actual raw source: 8,192 finite cases, complete actor/canary bytes.
- Independent scales/aliases: 44 cases / 132 executions; six effective compiled
  source negatives retained.
- Complete original 81-word registered update: 32 cases / 96 executions.
- Four symbol sets / 12 independent links: original and actual-padder normalized
  all 157 words equal; raw transforms identically; 32 cases / 96 executions.
- Actual copied owner: 16 neighbors, pools and relative relocations unchanged,
  zero diagnostics; all other padded owner bytes identical.
- Exact final private frame: 16 cases / 48 executions; original homes/footprint.
- Public reads: eight cases / 24 executions, retail's 13 reads, no output reload.
- Eight effective binary/proof negatives and two stale-word/relocation padder
  negatives reject unsafe mutations.
- Original/normalized missing-byte prefixes retain four faults / eight executions;
  prior raw-source fault evidence is reused explicitly, not claimed freshly rerun.

The initial suite exposed inherited test-name and target-only guard fixture
issues; correct scope without weakening gates. Installed audit exposed an old
target-hardcoded symbol helper and legitimate linker symbol/string ordering.
Correct the target assertion; compare decoded symbol/string tables, headers and
section layout structurally, then require every other ELF byte equal except
the target slot and target symbol size. All non-target symbol metadata remains
unchanged; do not claim raw whole-ELF byte equality.

Fresh make -C conker -j4 build/conker.us.elf progress.csv succeeds, preserving
existing warnings including duplicate generated_12D630 recipes. Whole linked
audit passes. All 189,088 protected Game-data bytes / 720 owners remain exact:
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
All previous guard bytes remain an exact prefix; conversion rows are byte-identical.
Fresh make tools-check passes.

Fresh matcher: total 3,417/5,489 (62.25%), Game 2,744/4,816 (56.98%),
Init 492/492 and Debugger 181/181 exact; zero drift / 2,072 different.
This is one additional byte-exact function, not a new C-conversion count:
the placeholder already had C representation. Root README aggregate rows only.

## Checkpoint And Next Boundary

Tools 94a6a0bf42bf3388ce2cb6c0233c657140c25b0c commits the three authored files
before the consumer source/guards/docs/pin. No push requested/performed.
Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 128
pre-existing dirty entries/both tracked dirty hashes are preserved. Mirror only
three absent files, yielding 131 entries; no older commit/reset/push.

Fresh scoped documentation audit: ten documents / 3,924 relative links,
zero broken links. All three affected authored tools parse in both copies and
are exact mounted/older mirrors; no broad unchanged-suite claim.

Final explicit graphify update . exits 1: refuses 39,093-to-17,312 node shrink,
retaining 19,398 nodes from 2,972 existing files outside the scan corpus.
Preserve version/zero-node warnings and existing graph; no force/purge/install.
Ignored receipts: conker/build/game-owner-points-initializer-match-test/
and conker/build/game-owner-points-initializer-matching/.

- [x] Install complete semantic C and certified control/allocation/scheduling recipe.
- [x] Qualify complete linked slot, rebases, owner, ELF, protected data and history.
- [x] Refresh aggregate status and bank tools before the consumer checkpoint.
- [x] Recover adjacent func_151B3CF0's complete bounded contract in
  [Note 1189](1189-game-owner-point-arc-recovery-and-helper-audit-20261009.md); frame/full-word fitting remains open:
  142 words / 568 bytes, frame 0x88,
  ROM 0x1E11A0..0x1E13D8. Audit threshold/early exit, midpoint and horizontal
  normalization, func_150484A0/sinf/cosf contracts, ten-record position loop,
  original saved GPR/FP lifetime and branch-delay angle advance before matching.
- [ ] Keep helper/FCSR/hardware/live rendering/gameplay acceptance separate.

Single Codex writer, zero Claude calls; no OGL/Release/save/editor changes.
The wider Game matching goal remains active.
