# Game Glyph Rectangle And Typed Caller Guarded Match

Date: 2026-10-12. Recover complete func_15041508 in
conker/src/game/generated_6E770.c and correct its caller/prototype ABI.
VA 0x15041508..0x150415E0, ROM 0x6E9B8..0x6EA90: 54 words / 216 bytes.
Semantic C emits 54 words, frame zero, no pool or relocations. Forty-three
words match directly; eleven expected-word guards normalize one closed
V1/T0/T1 register-allocation cycle. This is not a direct C match. Preserve
the existing O2/g3/no-unroll profile, original ASM, SDK and shared headers.
No instruction insertion/omission, helper stub, dummy state or broad batch.
The typed caller emits the identical raw object and retains its nine guards.
Matching +1 only; converted counts/bytes and progress CSV are unchanged.

## Baseline And Contract

Consumer b5f4dd37a2dafbb56dce87b7a565cb6e373fe530 and mounted tools
3fb9a26ad5f03f4673c5866275f2c121e558fefc were clean at entry.
[Note 1289](1289-game-intensity-texture-setup-direct-match-20261012.md)
left this 54-word / 52-difference placeholder and its incorrectly pointer-
shaped coordinate interface. Read workflow, current note, complete original
leaf/caller/lookup, SDK macros and actual no-unroll owner profile. Query
Graphify for navigation; retail/source and literal slots are authoritative.
Codex is the sole writer; zero Claude calls. Reuse existing IDO, structured
ELF/object/pool parsers, MIPS/native32 and both actual padders.

Recover Gfx *func_15041508(Gfx *displayList, s32 x, s32 y, s32 glyph).
Emit three commands / six ordered word stores and return output+24:
an 8-by-12 texture rectangle on render tile zero, RDPHALF_1 carrying its
texture S/T origin, and RDPHALF_2 with 0x400/0x400 increments. Screen corners
are quarter-pixel coordinates masked to twelve bits. Glyph column uses
truncating signed glyph % 8, including negative indices; row uses
(glyph - glyph % 8) / 8. Texture origin is column*8 and row*12 in five-
fractional-bit units, packed into two sixteen-bit fields.

Use the existing gSPTextureRectangle macro. Explicit unsigned casts precede
coordinate shifts/additions and texture multiplies/shifts, preserving defined
32-bit bit arithmetic rather than signed-shift/multiply overflow. Subtracting
the signed remainder before division stays in range. Do not replace signed
remainder/division with unsigned masks/arithmetic shifts, add range/NULL gates,
clip negative positions, or narrow the glyph to a byte just because the
ordinary caller currently provides indices 0..80.

The first rectangle stores word one before word zero; the two half commands
store word zero first. There are no leaf reads, helper calls, private stack
writes or saved-register changes. Eleven guards change only the closed scratch
register cycle; they are not eleven independent scheduling swaps. Guard words
validate the exact compiled words and absence of relocations, with no baseline
or expected-word regeneration to pass mutations.

Retype Gfx *func_150413FC(Gfx *displayList, s32 x, s32 y, u8 *text), its
result pointer, the local glyph prototype and scalar horizontal cursor.
The cursor advances eight units using unsigned 32-bit arithmetic. Caller
signature was incorrectly s32/u8 *row; that was integer screen X, not pointer
arithmetic through eight-byte records. Preserve the complete 33-word/frame
0x28 raw object, all two JAL relocations and its existing nine guards. The
unsigned cursor's conversion at the signed coordinate interface is qualified
for the actual 32-bit IDO/GCC ABIs, not claimed for all implementation models.

The original caller reads a zero-terminated byte stream, translates each byte
through the actual 34-word func_15041480 and the original 80-byte D_800848D0
table, then invokes the draw leaf. Lookup returns the first match or 80 when
absent; duplicate underscore entries remain first-match. Read the next byte
after drawing: output/text or output/table aliases can change later reads.
No direct original Game JALs to the string caller were found; the glyph leaf's
sole direct Game JAL is 0x15041444 inside this caller. The three-function
chain is actual retail code, not proof of a recovered upstream gameplay path.

## Source Screen And Qualification

The full-width SDK body immediately recovers 54/frame zero/no pool, with
eleven register-only differences under both owner no-unroll and O2/g3.
Signed-shift/multiply, argument-name, register-argument, unsigned-coordinate
and integer-return variants retain eleven differences; unsafe signed forms
are not selected. A direct quotient produces 53 words/44 differences and
loses retail's expression shape. A local cursor produces 48/50 differences.
O1/g3 gives 67 words/frame 0x10/67 differences; O1 gives 67/0x10/64.
Keep the clear unsigned-arithmetic body and existing owner profile. This is
a bounded screen, not a claim that every possible direct-match form was tried.

Eight pre-install tests pass in 17.542 seconds; eight installed tests pass in
20.732 seconds. Final two literal-integrity/corruption-control gates pass
again after the installed suite in 4.987 seconds.
They pass again after all indexes in 4.820 seconds. All 4,427 relative links
across seven edited documentation files resolve; diff --check passes.
Receipts: conker/build/game-glyph-rectangle-match-test/.

- 2,816 retail/raw/guarded leaf cases cover eight X values, eight Y values,
  22 signed glyph values including both INT limits, and two stack phases.
  Three extra output buffers include high addresses and wrapping. Execute
  all 54 words. Raw public bytes/events/return agree with the independent
  reference; guarded complete memory/events/GPR/FPR agree with retail.
- 588 actual caller33/lookup34/draw54 chain cases cover all 256 initial
  bytes, empty and multi-byte streams, missing bytes, first duplicate matches,
  signed coordinate limits, both stack phases and output/text/table aliases.
  Original and typed/padded complete chains have identical linked words and
  complete state. No helper hooks or synthetic lookup/draw projections.
- Two independent chain links rebase code and table with HI16/LO16 carries
  in twelve cases. All 603 fired fault pairs compare complete partial memory,
  events, calls and GPR/FPR at leaf and chain access boundaries. Raw private
  fault order is not claimed; no portable C fault or hardware claim.
- Six independently compiled leaf controls fail: bit-masked remainder,
  shifted row, width, height, texture increment and returned pointer. Stale
  expected-word and missing-first-cycle-guard controls fail effectively.
- Complete before/after owners use the actual no-unroll profile, are
  diagnostic-free and pass GLOBAL_ASM processing and both actual padders.
  All seven neighbor bodies/extents/relocations/pools are identical, including
  the retyped caller's entire raw object and existing guard behavior.
- Native32 O2/O0 each pass 1,408 leaf and 1,024 chain cases with actual full
  SDK mbi/gbi headers, exact recovered lookup C and typed caller/draw C.
  Check four-byte pointers, eight-byte Gfx, complete output/table/text
  canaries and live aliases. Six leaf and three caller negative controls
  produce effective mismatch receipts. No 64-bit-host/RSP/RDP claim.
- Frozen literal source/entire-ELF/size/guard-prefix/ten-input gates reject
  four stale/duplicate/missing source forms, duplicate guards, source
  corruption, three ELF corruptions and guard corruption. No production
  mutation, metadata projection or frozen-baseline refresh.

Fixture issues were corrected before installation: conflicting prototypes
in alternative signature trials; a text buffer accidentally overlapping the
simulated stack; fixed --defsym values incorrectly overriding internally
defined functions during rebasing; misleading native indentation under
-Werror; and the wrong assumed old stub size. The actual old four-argument
stub is 28 bytes, including four unused-argument home stores, not 12 bytes.
No production workaround or weakened immutable audit was used.

~~~sh
python3 -m tools.experiments.game_glyph_rectangle_candidates --profiles
python3 -m tools.experiments.game_glyph_rectangle_candidates --filter=
python3 -m unittest tools.tests.test_game_glyph_rectangle_match -v
make -C conker -j4 -W src/game/generated_6E770.c build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit And Progress

Qualify the complete CSV successor, verify the old manifest hash, then promote
that generated artifact with its original byte prefix and mixed line endings.
Only eleven rows are appended. The guard dependency triggers a broad rebuild;
force this owner through its normal unchanged recipe to make the installed
guard application explicit. Build exits zero. Existing unrelated CFE warnings
and the duplicate generated_12D630 recipe warning remain separate from the
diagnostic-free target owner; do not call the full build warning-free.

Literal entire-ELF comparison changes only 165 bytes: 164 target bytes and one
size byte (28 -> 216). Every other instruction/address/extent/header/symbol/
string/section/pool/data byte is identical, including the complete typed
caller. Ten other inputs are unchanged: generated progress CSV, rodata,
symbol definitions, undefined functions, retail layout, Makefile, original
slice ASM, texture data assembly and both SDK headers. The old guard manifest
is an exact byte prefix; its old nine caller rows remain untouched.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | e13af74be9feec1ad02bd96e0cc20855754b7ee6b362a676b704d4888798e563 |
| Source after | 25ba94b9b2580a6657b42f1d834fe6f7799810e4a2da607635c2cebb44b4db56 |
| ELF before | 978ccf41d42999cf6a9ceb3b21792ea37451b23e8cd09f9c9cf9bae3acf22118 |
| ELF after | 48d60bd24c2c18e51c2d83704b8643dd6bfb8ff3c4db0ba932df4d0543f10f9a |
| Guards before | 0c28956baf37afeaa5129ad33cb532639375cfbee4fa8a8a6d479d8220adaf52 |
| Guards after | 9b08dabc9ccc24cfa82b40ec626d3f5f73a7521f89d5a118f8e62773ccfea168 |

Fresh matching: Game 2,811/4,823 (58.28%), total 3,484/5,496 (63.39%),
Init 492/492 and Debugger 181/181. Zero drift / 2,012 still different.
Matching +1 only; the old stub was already C-converted. Do not claim credit
for the already exact caller, changed C types, converted counts or bytes.
Root README gets aggregate rows only; detailed function narrative stays here.

## Checkpoint And Next Body

Consumer, mounted and older shared checks and native py_compile pass.
Bank mounted tools 69d7a80a2aafe5aa0bbae5b3ebc704b5ebbca8e1 first, then
consumer source/guards/docs/exact gitlink;
no push. Preserve older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
and all 71 prior hashes. Add only two new identical tools copies, dirty count
348 -> 350, final snapshot 73 hashes. Do not commit/reset independent older
history. Target tests run in the consumer, not the mirror. Prior unchanged
neighbor/SDK evidence from Notes 1289..1278 is reused on literal unchanged
fingerprints, not reported as fresh broad suites.

Native graphify update . exits one on protective shrink refusal: 18,248
candidate nodes versus 40,027 saved. Preserve 19,398 nodes from 2,972 excluded
but still existing files; no force/purge/install. Version/empty-source warnings
remain separate from compiler diagnostics.
Require a fresh terminal post-consumer-commit Graphify Rebuilt receipt,
advanced log bytes/UTC and zero native workers. Launching a hook is not
completion. Do not force shrink, purge, install or modify accounts.

The live owner now has four exact C functions and four remaining placeholders.
Next recover func_150415E0: 115 words / 112 differences,
VA 0x150415E0..0x150417AC, ROM 0x6EA90..0x6EC5C. This is an extended-
character metrics resolver, not a draw emitter. Recover its six-argument
code/width/height/scale/mode/factor interface, signed 0xA8..0xFF gate, ordered
output aliases and 19-entry switch. Original table and five float constants
are in conker/asm/data/23D570.rodata.s at jtbl_80098AB0 and D_80098AFC..B0C.
Preserve the original data/labels and inspect the downstream formatter's
actual caller contract before replacing the next placeholder.

Guard removal, independent SDK/hardware/FCSR/RSP/RDP/renderer/gameplay
acceptance and the full Game goal remain open. No OGL Release build/change,
private input/save or active editor/debugger mutation.
