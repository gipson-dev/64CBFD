# Game Extended-Character Metrics Direct Match

Date: 2026-10-12. Recover complete func_150415E0 in
conker/src/game/generated_6E770.c. VA 0x150415E0..0x150417AC,
ROM 0x6EA90..0x6EC5C: 115 words / 460 bytes. All 115 words emit directly
from semantic C under the unchanged O2/g3/no-unroll owner profile, frame zero,
no guards or helper calls. The sole Makefile addition binds this owner's
generated switch to existing jtbl_80098AB0_game. Preserve original assembly,
pool, undefined labels, guard manifest, progress CSV, SDK and caller bodies.
Matching +1 only; converted functions/bytes were already counted as C.

## Baseline And Contract

Consumer 8e127e8b4e2da614af8916af30fa68c4aa43e720 and mounted tools
69d7a80a2aafe5aa0bbae5b3ebc704b5ebbca8e1 were clean at entry.
[Note 1290](1290-game-glyph-rectangle-and-typed-caller-guarded-match-20261012.md)
left this 115-word / 112-difference zero-return placeholder. Read complete
retail metrics, actual caller setup windows, original pool and current owner
profile. Graphify is navigation only; literal retail/source bytes are evidence.
Codex sole writer, zero Claude calls. Reuse IDO, ELF/object/pool parsers,
MIPS/native32 oracles, GLOBAL_ASM processing and both actual padders.

Recover void func_150415E0(s32 code, s32 *width, s32 *height, f32 *scale,
s32 *mode, f32 *factor). Valid signed codes are 0xA8..0xFF. Initialize factor
to 1.0, then dispatch 0xA8..0xBA through the original 19-entry table;
0xBB..0xFF use the default. Output tuples follow retail:

| Codes | Width | Height | Scale | Mode | Factor |
| --- | ---: | ---: | --- | ---: | --- |
| A8..A9 | 32 | 18 | D_80098AFC | 1 | 1.0 |
| AA..AD | 32 | 27 | 2.0 | 1 | D_80098B00 |
| AE | 16 | 17 | D_80098B04 | 1 | 1.0 |
| AF..B0 | 46 | 16 | 2.0 | 1 | 1.0 |
| B1 | 38 | 24 | 2.0 | 1 | D_80098B0C |
| B6..B9 | 16 | 12 | 2.0 | 0 | 1.0 |
| BA | 55 | 12 | D_80098B08 | 0 | 1.0 |
| Other valid codes | 12 | 16 | 2.0 | 0 | 1.0 |

These are distinct-output tuples, not a license to reorder aliased stores.
Preserve branch-specific access order, especially BA: mode first, then live
scale, width and height. Invalid codes clear scale, width and height in that
order, leaving mode/factor untouched. The low invalid path skips the sixth
incoming argument home; the high invalid path reads it in the branch delay
before rejecting the code. On valid paths the factor pointer is cached before
its first store, while the fifth mode pointer is loaded late per branch.
Read float globals live after preceding stores; replacing them with literals
breaks aliases. The negative AE scale (-1.6) is intentional.

Original jtbl_80098AB0 and D_80098AFC..B0C are owned by
conker/asm/data/23D570.rodata.s. The compiler produces 80 bytes: all 19
meaningful entries / 76 bytes match the original table, plus four zero
alignment bytes. Both actual padders discard generated rodata and relocate
the text to the existing table. Do not append the four alignment bytes over
the following original D_80098AFC float or regenerate the pool.

## Source Screen And Qualification

The first selected body emits 115 words/frame zero/zero differences under
both owner no-unroll and O2/g3; O1/g3 and O1 give 117/104 differences.
Normalized-switch and corrected break-case forms also match under O2.
The inverted gate gives 115/109 differences. Keep the clear initial body and
existing profile. A preliminary break variant wrongly fell through to invalid
stores; fix that experiment with an explicit post-switch return before
measuring it. No broad conversion/profile batch or selected-body workaround.

Nine pre-install tests passed in 13.217 seconds. Final nine installed tests
pass in 14.312 seconds, after the complete linked audit described below.
The final two literal-integrity/corruption-control gates pass again after all
indexes in 5.277 seconds. All 4,432 relative links across seven edited docs
resolve; git diff --check passes.
Receipts: conker/build/game-extended-character-metrics-match-test/.

- 6,812 retail/raw/padded cases cover all byte codes and signed boundaries,
  thirteen output/global aliases and two stack phases. Reach all 115 words;
  complete memory/events/GPR/FPR and original table entries agree.
- 176 home/rebase cases retain cached factor and late mode homes, including
  guest-only home aliases. Two independent code/table/five-constant links
  cross HI16/LO16 carries and have identical original/raw/padded words/state.
- 462 fired fault triplets compare partial memory/events/GPR/FPR at every
  modeled access. Verify invalid untouched outputs and the unequal low/high
  invalid home-read behavior. No portable C or hardware fault claim.
- Six independent compiled semantic controls fail effectively: lower/upper
  gate, initial factor, literal instead of live float, BA order and mode value.
  Missing original-pool binding fails real linking. Mutated compiler pools
  live separately at 0x80100000 to avoid hiding a constant/global alias defect.
- Complete before/after owners are diagnostic-free under actual no-unroll;
  all seven neighbors' raw bodies/extents/relocations agree. GLOBAL_ASM and
  both actual padders preserve every other body and omit generated rodata.
- 352 actual callsite-window cases execute original six-argument setup and
  delay-slot stores at 0x15041F0C..15041F50 and 0x150429C0..150429E4, with
  actual metrics bodies, no metrics hook. A synthetic window exit bounds this
  evidence: it does not qualify the complete formatter or width measurer.
- Native32 O2/O0 each pass 4,060 actual semantic-C cases with an independent
  bit-wise reference, all output/global canaries and fourteen public aliases.
  Check four-byte pointers/integers/floats. All six native semantic controls
  fail effectively. No native64, private-home, alignment or hardware claim.
- Frozen source/entire-ELF/extent/Makefile/nine-input gates reject source,
  code, neighbor, size, pool, symbol-value, symbol-string and binding damage,
  two stale source forms and duplicate binding. No production mutations or
  immutable-baseline refresh. Pointer redirection and misalignment fixtures
  are byte-addressed guest-model evidence only.

Fixture corrections: independent negative pools; correct s3 in the second
caller window; mapped redirected guest pointers; exact Makefile byte/newline
checking rather than normalized text; corrected break-case experiment; and
global canaries for the native INT-limit cases. No production workaround.

~~~sh
python3 -m tools.experiments.game_extended_character_metrics_candidates --filter= --profiles
python3 -m unittest tools.tests.test_game_extended_character_metrics_match -v
make -C conker -j4 -W src/game/generated_6E770.c build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit And Progress

Normal build exits zero. The Makefile dependency triggers broader generated
slice rebuilding. Existing unrelated CFE diagnostics and the duplicate
generated_12D630 recipe warning remain; the target owner is diagnostic-free,
not the complete build. Shared checks run under WSL: native Windows invocation
of the Linux object wrappers fails with WinError 193; no wrapper change was
needed. Native Windows py_compile passes for both new files in both copies.

The first installed entire-ELF gate rejected expected linker metadata movement.
Decode and audit every difference before admitting it: precisely eight closed
symbol/string reorderings, 22 retained symbols, 207 bytes. All symbol meanings
are unchanged except func_150415E0 size (12 -> 460). The test applies eight
explicit fixed cycles to frozen baseline records/contiguous name spans, then
compares the entire ELF literally. No broad metadata projection or arbitrary
symbol exception; symbol-value and string corruption controls both fail.

Exactly 521 ELF bytes change: 312 target instruction bytes, two size bytes,
207 symbol/string order bytes. Every other instruction/address/extent/header/
section/data/pool byte is identical. Nine other inputs are byte-identical:
guards, generated progress CSV, both pool/data assembly inputs, symbol
definitions, undefined functions/symbols, retail layout and original slice
assembly. The Makefile changes only the existing-pool binding line with its
prior byte prefix/newline style preserved; optimization remains unchanged.
Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 25ba94b9b2580a6657b42f1d834fe6f7799810e4a2da607635c2cebb44b4db56 |
| Source after | 8677e241aee0ae98694ab04154d4d1949de586b49d86e64e110edc37cfb33473 |
| ELF before | 48d60bd24c2c18e51c2d83704b8643dd6bfb8ff3c4db0ba932df4d0543f10f9a |
| ELF after | 1337dd11530d3ef13938f6cf3995e65acee4357cae88832059f50559aa7a7d07 |
| Guards unchanged | 9b08dabc9ccc24cfa82b40ec626d3f5f73a7521f89d5a118f8e62773ccfea168 |
| Makefile after | 89d7401cbfa4fa945ff5bc464382f70068b253f7a1b6d547e98651b565076c47 |

Fresh matching: Game 2,812/4,823 (58.30%), total 3,485/5,496 (63.41%),
Init 492/492, Debugger 181/181; zero drift / 2,011 still different.
Matching +1 only, converted counts/bytes unchanged. Root README aggregate
rows only; detailed recovery narrative stays here.

## Checkpoint And Next Body

Bank mounted tools 5d3c18bdb8e2fac83bbd8a5b3f7a2a8662edea3e first, then
consumer source/Makefile/docs/exact gitlink, no push. Consumer, mounted and
older WSL shared checks pass. Preserve older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 73 prior hashes; add only
two absent identical tool copies, dirty count 350 -> 352, final 75 hashes.
Do not commit/reset the independent older checkout. Prior unchanged neighbor
suite receipts are reused on exact fingerprints, not claimed as fresh suites.

Graphify query completes; native update exits one on protective shrink refusal:
18,257 candidate nodes versus 40,035 saved. Preserve 19,398 nodes from 2,972
excluded but existing files; no force/purge/install. Version/empty-source
warnings are separate from compiler diagnostics. Before final reporting,
require a fresh terminal post-consumer-commit Rebuilt receipt, advanced log
bytes/UTC and zero native workers; a launched hook is not completion.

Five of eight owner functions now match; three placeholders remain.
Next recover func_15042C40: 68-word / 272-byte slot, 62 differences,
VA 0x15042C40..0x15042D50, ROM 0x700F0..0x70200. There are 65 executing
words and three original zero tail words. It narrows input to u8, uppercases
a..z, maps space to 0x60, then finds the first match in the original 95-byte
D_80085930 table; absent bytes return the original narrowed character, not
the uppercase search character. Data owner: conker/asm/data/2275E0.data.s.
Actual callers at 0x15041BD8 and 0x15042968 narrow the return. Preserve the
table, first-three-entry checks, four-entry loop and incoming argument store.
This dependency prepares func_150428D4 (219 words) and func_150417AC
(1,098 words); they are not recovered by the current callsite-window tests.

Existing guard removal, hardware/FCSR/RSP/RDP/renderer/gameplay acceptance
and the full Game goal remain open. No OGL build/change, private input/save
or active editor/debugger mutation.
