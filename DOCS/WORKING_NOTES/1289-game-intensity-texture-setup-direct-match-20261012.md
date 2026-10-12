# Game Intensity Texture Setup Direct Match

Date: 2026-10-12. Recover complete func_150412C0 in
conker/src/game/generated_6E770.c, replacing its zero-return placeholder.
VA 0x150412C0..0x150413FC, ROM 0x6E770..0x6E8AC: 79 words / 316 bytes.
All 79 words emit directly from SDK-macro semantic C. No frame, constant
pool, guards, instruction drops/insertions, shared headers, callers or recipe
changes. Keep the existing O2/g3/no-unroll owner profile, required by the
already exact byte-table lookup neighbor. Add one local texture declaration.
Matching +1 only: converted counts and bytes remain unchanged.

## Baseline And Contract

Consumer fb8af768eacd79578eff5eadef7afde95486ea12 and mounted tools
6bee2750e1d77b102ad376f69b81acab8b5fcb8c were clean at entry.
[Note 1288](1288-game-matrix-decomposer-guarded-c-conversion-20261011.md)
left this genuine placeholder, 79 slot words / 78 differences. Read the
workflow/current handoff, query Graphify, inspect the complete original body,
SDK macros, actual owner profile and relevant prior neighbor Notes
[570](570-game-byte-table-index-lookup-match-20260930.md) and
[674](674-game-command-row-loop-match-20261002.md). Codex is the sole writer;
zero Claude calls. Reuse existing IDO, structured ELF/object/pool parsers,
MIPS/native32 harnesses, GLOBAL_ASM processing and both production padders.

Recover Gfx *func_150412C0(Gfx *displayList). Emit exactly twelve commands /
96 output bytes and return the advanced pointer. There are no input-memory
reads, helper calls, NULL/range gates or stack accesses. The two texture-image
commands both carry the address of D_80084930, not its contents. Preserve the
first width-64 image command even though the load-block macro then emits a
width-one image command. Do not remove it as redundant.

| Command | First Word | Second Word |
| --- | --- | --- |
| Texture enable, full S/T scale | D7000002 | FFFFFFFF |
| Pipeline sync | E7000000 | 00000000 |
| Decal RGBA combine, both cycles | FCFFFFFF | FFFCF279 |
| Other mode | EF002C0F | 0055204C |
| I-format 16-bit image, width 64 | FD90003F | D_80084930 |
| I-format load image, width one | FD900000 | D_80084930 |
| Load tile | F5900000 | 07000000 |
| Load sync | E6000000 | 00000000 |
| Load block | F3000000 | 077FF200 |
| Pipeline sync | E7000000 | 00000000 |
| Render tile, intensity 4-bit | F5800800 | 00000000 |
| Tile size, 64 by 128 | F2000000 | 000FC1FC |

Use gSPTexture, gDPPipeSync, gDPSetCombineMode, gDPSetOtherMode,
gDPSetTextureImage and gDPLoadTextureBlock_4b from the existing SDK. The
expert other-mode word retains retail's exact low bits; no guessed flag
replacement. Word-one stores precede word-zero stores for the first texture
enable and load-tile commands; the other ten commands store word zero first.
The texture is not dereferenced, even when output aliases its address.

The graph resolved the placeholder but supplied no caller contract. An aligned
original Game-code scan found no direct JALs to this entry; an aligned entire
original-ROM scan found no literal function-address references. Current linked
code/data scans also found none. These bounded scans do not prove absence of
all computed/indirect callers. No original caller-chain test is claimed.

## Fresh Qualification

The first SDK-macro body matches all 79 words directly. Both existing
no-unroll O2/g3 and unrolled O2/g3 emit the same body/frame zero/no pool.
Raw other-mode spelling and argument-name variants also match. O1/g3 and O1
each emit 107 words, frame 0x30, 105 differences; do not adopt those profiles.

Eight pre-install tests pass in 15.278 seconds; eight installed tests pass
in 14.221 seconds. Final two literal-integrity/corruption-control gates pass
again after documentation and the EOF correction in 2.636 seconds.
All 4,424 relative links across seven edited documentation files resolve;
diff --check passes.
Receipts: conker/build/game-intensity-texture-setup-match-test/.

- Sixty-four retail/raw/padded cases cover eight output addresses, four
  canary patterns and both stack phases. Execute all 79 words and compare
  every output byte, all 24 ordered write events, all GPR/FPR state and
  returned pointer. No reads/calls/private stack writes. Texture/output
  aliases, mapped-zero and 32-bit wrap fixtures are guest evidence only,
  not portable C NULL/wrap or hardware-address claims.
- Two independent links rebase code and texture with HI16/LO16 carries in
  36 cases, including texture-address aliases. All raw/unlinked relocation
  records and complete independently linked words agree with original ASM.
- All 144 fired fault triplets cover every one of the 24 write boundaries
  across three buffers and two stack phases. Compare complete partial
  memory/events/GPR/FPR. A missing final output byte rejects all three
  forms after 23 completed stores. No portable C fault/hardware claim.
- Six independently compiled semantic negatives fail: wrong texture height,
  initial image width, combine mode, texture enable, omitted first image
  command and wrong returned pointer. O1 is an effective profile control.
- Copied complete before/after owners use the actual no-unroll profile and
  are diagnostic-free. GLOBAL_ASM processing and both actual padders preserve
  all seven neighbors, their extents/relocations and normalized pools. The
  target matches the isolated object. An unrolled owner control overflows
  the unchanged lookup neighbor (216 bytes versus its 136-byte slot), and
  the real padder rejects it; no production profile change is made.
- Native32 O2/O0 each pass 384 cases using the actual full SDK mbi/gbi
  headers, not replacement graphics macros. Check real four-byte pointers,
  eight-byte Gfx, the returned pointer and complete 384-byte output/4096-byte
  texture canaries over 16 patterns, two buffers and twelve starting slots.
  Six native controls produce effective mismatch receipts. Native tests do
  not qualify 64-bit hosts, guest wrapping/NULL or the hardware RSP/RDP.
- Frozen-baseline literal source/entire-ELF/size/eleven-input gates reject
  stale or duplicate source, source corruption, three ELF corruptions and
  guard corruption without production mutation or baseline refresh.

Fixture issues were corrected without production workarounds: generic frame
reporting had interpreted the leading LUI as an allocation (0x1900), so this
candidate derives frame only from a real downward SP adjustment; the generic
whole-owner fixture initially used the wrong unrolled profile, so it now
uses the unchanged production no-unroll recipe flags. One extra EOF blank
line in the new test was removed in both new tools copies before commit.

~~~sh
python3 -m tools.experiments.game_intensity_texture_setup_candidates --profiles
python3 -m unittest tools.tests.test_game_intensity_texture_setup_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit And Progress

Source-only rebuild compiles this one owner and relinks successfully. The
known duplicate generated_12D630 recipe warning remains; target owner is
diagnostic-free. Literal whole-ELF comparison changes exactly 241 bytes:
239 target bytes plus two size bytes (12 -> 316). Every other body/address/
extent/header/symbol/string/section/data/pool byte remains unchanged. Eleven
other inputs are identical: guards, generated progress CSV, rodata assembly,
symbol definitions, undefined functions, retail layout, Makefile, original
slice ASM, texture data assembly and both SDK headers.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | e61b9a95d46df6d94fbf844eba778533559a662425c63b6d6ddfc8d413ee9241 |
| Source after | e13af74be9feec1ad02bd96e0cc20855754b7ee6b362a676b704d4888798e563 |
| ELF before | 4b4bece866646b9f453b958c1dccdd2f37e31f65dc2abaaa810b71f72a5d4071 |
| ELF after | 978ccf41d42999cf6a9ceb3b21792ea37451b23e8cd09f9c9cf9bae3acf22118 |
| Guards unchanged | 0c28956baf37afeaa5129ad33cb532639375cfbee4fa8a8a6d479d8220adaf52 |

Fresh matching: Game 2,810/4,823 (58.26%), total 3,483/5,496 (63.37%),
Init 492/492 and Debugger 181/181. Zero drift / 2,013 still different.
Matching +1 only. Converted counts/bytes and the generated progress CSV
are unchanged; this former C stub was already counted as converted. Root
README gets aggregate rows/date only, not a function narrative.

## Checkpoint And Next Body

Consumer, mounted and older shared checks and native py_compile pass. Bank
mounted tools 3fb9a26ad5f03f4673c5866275f2c121e558fefc first, consumer
source/docs/exact gitlink second; no push.
Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all
69 prior hashes remain unchanged. Add only two new identical tools copies,
dirty count 346 -> 348, final snapshot 71 hashes. Do not commit/reset that
independent older history. Target tests run mounted in the consumer.
Prior unchanged neighbor evidence from Notes 570/674 and owner Notes
1288..1278 is reused on literal unchanged fingerprints, not called fresh.

Native graphify update . completes with protective shrink refusal: final
18,246 candidate nodes versus 40,019 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. The first update
before the EOF-only correction likewise refused 18,240 versus 40,019.
Version/empty-source warnings remain separate from compiler diagnostics.
Require fresh post-consumer-commit terminal Graphify Rebuilt receipt, advanced
log bytes/UTC and zero native workers; launching a hook is not completion.
Do not force protective shrink, purge, install or modify accounts.

Live complete-slot scan finds three exact C functions in generated_6E770
(this setup, func_150413FC and func_15041480), with five placeholders still
different. Next recover func_15041508: 54 words / 52 differences,
VA 0x15041508..0x150415E0, ROM 0x6E9B8..0x6EA90. Retail emits a three-
command 8-by-12 glyph texture rectangle and returns output+24. Its A1/A2
are scalar screen coordinates, not the current u8 *row interpretation;
its signed glyph index uses truncating remainder/division by eight. Recover
the typed Gfx/coordinate ABI in both this leaf and the already exact
33-word caller func_150413FC, preserving that caller's existing guards,
eight-unit horizontal advance and the exact 34-word byte-table lookup.
Qualify the actual caller/lookup/draw chain before installation.

Existing guard removal and wider Game matching remain open. Hardware/FCSR/
RSP/RDP/renderer/gameplay acceptance is independent. No OGL Release build/
change, private input/save or editor/debugger mutation. Keep the full Game
goal active.
