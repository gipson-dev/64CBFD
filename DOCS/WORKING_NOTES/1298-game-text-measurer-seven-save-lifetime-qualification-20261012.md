# Game Text Measurer Seven-Save Lifetime Qualification

Date: 2026-10-12. Resume the active Game matching goal after
[Note 1297](1297-game-text-measurer-ugen-diagnostic-checkpoint-20261012.md).
Continue func_150428D4 in conker/src/game/generated_6E770.c, original
VA 0x150428D4..0x15042C40 / ROM 0x6FD84..0x700F0, 219 words / 876 bytes,
frame 0x80. No production installation or matching credit at this checkpoint.

## Baseline And Source Fitting

Consumer 2ce41e84fb57fb334df67c0e6563123f9826e9ac and mounted tools
5e14815817d9d772195c6b337ae2ef8e08a147ad were clean at entry. Codex sole
writer, zero Claude calls. Previous checkpoint was verified progress, not an
external blocker. Keep the wider Game objective active and the same target.
No OGL/Release change/build, ROM/save/config/editor/debugger mutation,
compiler/package installation, push or independent older-history commit.

Read the complete original routine and query the existing graph. The verified
UGEN trace of capture218 shows S3 text/flag, S4 glyph and an extra S7 save.
Source hints and promotion changes do not recover the original save set.
Consult the primary [IDO O2 guide](https://github.com/n64decomp/oot/blob/master/docs/guides/-O2%20decompilation%20%28for%20IDO%205.3%29.md)
for bounded lifetime/control-flow experiments, not proof of coloring causes.
Do not retry the failed UOPT modes, change the compiler profile or add dummy
state. All screens keep -O2 -g3 -Wo,-loopunroll,0 and produce no pools.

| Form | Words | Frame | Differences | Finding |
| --- | --- | --- | --- | --- |
| capture-constant-spill / register hints / call promotion | 218 | 0x80 | 174 | No improvement |
| capture-automatic-spill | 216 | 0x80 | 202 | S3 text/glyph, but flag still saved in S4 |
| capture-widened-glyph | 218 | 0x80 | 178 | No accepted fit |
| capture-flat-dispatch / automatic | 218 / 216 | 0x80 | 173 / 201 | No accepted fit |
| capture-local-dispatch | 222 | 0x80 | 148 | Seven saves, wrong roles/store order |
| capture-local-reuse-typed / address | 220 | 0x80 | 194 | Still wrong roles/length |
| deferred local-reuse outputs / index | 220 | 0x80 | 194 / 195 | No accepted fit |
| capture-shared-flag-exit | 222 | 0x80 | 184 | Wrong initial saved-store order |
| capture-flat-late-flag | 222 | 0x80 | 178 | Original first 13 words and save roles |
| existing flag-branches-captured | 222 | 0x80 | 146 | Original first 13 words; now qualified below |

The existing nested branch form was previously screened for size/word score,
not qualified as a fitting seed. This checkpoint verifies its original
S0..S6/RA homes, argument moves and S3 text/glyph reuse. Its 173,067-byte
code-identical UGEN trace shows a caller-saved V1 flag, not the original T0.
The new flat late-flag trace is 171,234 bytes. Neither is a full match.

## Complete Bounded Qualification

Add tests 17/18 and one shared qualification helper. Three complete bodies:
local dispatch222/148, nested late flags222/146 and flat late flags222/178.
Link each isolated candidate at 0x152428D4 using the existing compiler/linker;
leave actual normalizer/metrics helpers at their original addresses. Assert
code ranges do not overlap. A 222-word candidate cannot be executed at the
retail entry without overlapping the next normalizer; do not hide that by
overwriting code maps or manually patching calls. No helper hooks are used.

For each body, compare 755 public memory/helper-call cases against the full
219-word original and independent reference. Include all bytes/two phases,
empty/null, newline/control skip, output/font/factor/scale/text aliases,
pointer reload and nested truncation. Six named SP+0x68 flag-home aliases
also agree per body. Native32 executes 733 portable cases per O2/O0 profile
with the complete recovered helpers and buffer canaries: 4,398 new-body runs.
Synthetic guest stack/low-pointer aliases are not native portability claims.

Both late-flag bodies emit the exact first 13 original words. For each,
28 fired access-fault pairs (indices 0..13, phases 0/8) have equal complete
partial memory/events/GPR/FPR state. Confirm the fault fires and access count
before comparison. This covers only the early prefix, not every access or
full saved-register/flag lifetime through the function.

The local-dispatch form has the same seven-register set but still fails at
the first completed store: original saves S6 at SP+0x38, candidate S5 at
SP+0x34. Four fired pairs retain this effective count-versus-order rejection.
Do not weaken the earlier captured218 frame rejection or private witnesses.

## Actual Slot Rejection And Trampoline Discriminator

Extract the complete frozen 219-word slot. The strict generated-object padder
rejects all three 888-byte bodies against its 876-byte retail span. This is
an executed exception gate, not merely an asserted measurement.

Create a one-function layout using the structured CSV parser/writer and the
original frozen layout row. Run the real legacy padder and GNU assembler.
It succeeds by emitting an in-slot jump relocation to __retail_overflow_*
and a separate .game_overflow section. Assert the slot's function size remains
876 but its actual bytes differ from the original. That is an overflow
trampoline, not a byte-exact routine. Do not install it as a matching substitute.
This is an isolated overflow discriminator, not a new full-owner/rebase audit.

## Verification And Bank

All 18 focused tests pass in 75.344 seconds, no skips. New-body receipts are
conker/build/game-text-measurer-recovery-test/*-seven-saves.json. Prior gates
also run freshly: immutable-production controls, actual-helper/public/native
tests, old copied-owner neighbors/pools/padders, independent links/rebases,
private rejection controls and code-identical trace/rejection tests.
The old copied-owner/link qualification still describes captured218, not
the oversized new fitting seeds; do not transfer those receipts to them.

Consumer/mounted/older ROM-free tool checks, Windows py_compile and task-only
diff checks pass. All nine frozen production inputs and 189,088 protected
data bytes/720 owners remain exact. Source/ELF/guard/Makefile fingerprints and
Game 2,813/4,823 / total 3,486/5,496 matching counts stay unchanged. These
are preserved prior aggregates, not new matching credit. Root README unchanged.

Bank mounted tools fb5162b566040ba0038ed69ae120858aa2567f5f before consumer
docs/exact gitlink. Verify older HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
dirty357 and all 80 saved fingerprints before two conflict-checked copies;
preserve the other 78 hashes and old history. No push or older history commit.

Standalone Graphify update exits one on protective shrink refusal: 18,316
candidate versus 40,094 saved nodes. Retain 19,398 excluded-but-existing nodes
from 2,972 files, no force/purge/install. Final reporting requires clean
active repos, resolved documentation links and a fresh terminal post-consumer
Rebuilt receipt, advanced log bytes/UTC and zero native workers.

## Continue This Same Target

Use qualified flag-branches-captured222/0x80/146 as the next source-fitting
seed, retaining captured218 as the prior qualified reference. Recover the
original shared T0 flag initialization/call-only SP+0x68 lifetime, original
control-flow/load/scheduling and all 219 words. Being three words too long
does not mean only three words differ; 146 differences remain.

Do not substitute a padded/overflow form, select the privately rejected168
shape or copy broad retail word guards. After the real fit, requalify all
private/fired-fault/native/full-owner/padder/independent-link/rebase gates,
then install and perform the literal whole-ELF/data/old-guard-prefix audit.
Only then measure fresh README totals. Next afterward is func_150417AC,
1,098 words. Full Game matching and independent hardware/FCSR/renderer/
gameplay acceptance remain open; the matching goal stays active.
