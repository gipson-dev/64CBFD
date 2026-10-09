# Game Owner Endpoint Quad Guarded C Match

Date: 2026-10-09

## Result

func_151B2974 now matches all340 retail words after recovering its actual
private declaration order and qualifying84 closed GPR allocation guards.
The full semantic C renderer replaces its false zero-return placeholder in
[generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
This is a guarded C match, not direct compiler output or an assembly restoration.

- VA151B2974..151B2EC4; ROM1DFE24..1E0374;340 words/1,360 bytes.
- Existing O2/g3; correct0xB8 frame and S0/S1/RA saves at34/38/3C.
- Raw selected C:340 words/frame184/84 differences, zero diagnostics/pool bytes.
- 256 words emit unchanged;84 expected-word guards rename only GPR fields.
- Ten installed tests pass17.255s, zero skips.
- Fresh Game2,741/4,816 exact (56.91%), total3,414/5,489 (62.20%).
- Zero address drift;2,075 remaining differences.
- Conversion rows/bytes are unchanged: the old false placeholder was already
  classified as C. Do not add conversion credit for replacing it.

Continue from [Note 1177](1177-game-owner-endpoint-quad-recovery-and-frame-fit-20261009.md).
Parent baseline1d003b176c33e15ab5b3caa3432df9ba91f0f66f,
tools71976ff9d4bc99643ef734b430d38c200f89f257; both relevant trees clean.
One Codex writer, zero Claude calls. No OGL/Release/save/editor changes.

## Complete Contract

Retain Note1177's recovered three-argument graphics ABI:
Gfx *(Gfx *output, u8 *actor, s16 view).

The renderer preserves endpoint validity/lazy resource exits, retained matrix
across both transforms, retained view-origin pointer across graphics helpers,
late render-state and width reads, finite binary32 camera-facing geometry,
four vertices and two triangles. Preserve negative width, zero-normal handling,
coordinate truncation and all24 untouched vertex flag/color bytes, including
helper mutation and actor/vertex alias cases. SDK macros emit the final commands.
The real20-word func_15149490 dispatcher and registered8008A670 pointer are
qualified for selector0/-1 and signed-view/returned-cursor forwarding.

Helper bodies, complete matrix/SDK behavior, FCSR/hardware, live rendering and
gameplay acceptance remain separate. The model's translated-transform hook is
bounded, not a replacement for the actual transform implementation.

## Frame And Source Fit

The former selected140-difference body had the right total frame but wrong
cursor, validity/sync, transformed-position, retained-origin/matrix and length
homes. Recover the following declaration order, without dummy padding locals:

pair; invalid; sync; cursor; origin; dx/dy/dz/rx/ry/rz; length;
first/second positions; nx/ny/nz; matrix; scale.

It emits the actual retail homes: invalidB3, syncB2, cursorAC, originA8,
first80, second74, matrix64 and length8C. Incoming actor/view homes remainBC/C0.
Separate zero assignments recover the retail F12/F14/F16 zero order.
Move the independent local sync initialization before origin capture and reverse
the commutative matrix-add/render-flag operand spellings. Public access order
and helper-visible behavior remain retail-congruent.

Ignored layout/schedule/register/typed screens retain33 complete probes in
conker/build/game-owner-endpoint-quad/. No exploratory body is installed merely
because its difference count improves.

Final complete-profile screen:

| Profile | Words | Frame bytes | Raw differences |
| --- | ---: | ---: | ---: |
| O2/g3 |340|184|84|
| O2 |339|184|338|
| O1/g3 |405|168|400|
| O1 |405|168|400|

Only O2/g3 passes normalization. Preserve compiler profiles and neighboring
source behavior; do not replace the remaining words with a literal retail table.

## Register Proof

[Matching driver](../../tools/experiments/game_owner_endpoint_quad_matching.py)
contains explicit field-only allocation maps in offset regions80..84,
1D8..1FC and324..53C. The early80 word forwards the correct validity temporary
along the resource-null likely-branch path; the latter region includes the
matching terminal validity load/use. These are path-connected lifetimes,
not a claim that every region is independently straight-line.

certify walks every acyclic branch path, including likely-delay annulment.
Raw/fitted architectural operands must have identical symbolic provenance
before each instruction result receives a shared token. Stores/loads keep the
same addresses, sizes and payloads; all non-GPR instruction bits are unchanged.
Calls observe matching A0..A3/SP after their delay slots, then independently
clobber volatile registers. Return V0/S0/S1/SP/RA provenance must agree.
All FP arithmetic words and FP operand fields remain unchanged; COP1 transfers
may rename their GPR destination fields.

Certificate:27 conservative paths,27 traversed helper boundaries,339 reached
instruction words. WordA0 /151B2A14 is the already-proven unreachable duplicate
load, not claimed dynamic coverage. The certificate rejects live-provenance
mutations. It reads no ROM/retail word table to construct fitted instructions.

All84 guard sites have no relocations;17 original relocation type/symbol uses
and sites stay intact. Guard generation reads the actual emitted object and
requires expected raw words. The real padder rejects a stale expected word.

## Qualification And Linked Audit

[Match suite](../../tools/tests/test_game_owner_endpoint_quad_match.py) reuses
the recovery suite's independent reference, strict guest memory model,
native32 helper contracts, real dispatcher, rebases and effective negatives.

- 384 guest cases/1,152 executions compare retail, raw selected and normalized
  bodies. Complete private/public memory, ordered write traces and actual
  helper argument lists agree. This is not a full read-trace/hardware claim.
- 11,520 native32 executions of the actual selected C retain all64 vertex bytes,
  including24 holes, aliases, helper mutation, signed views and degenerate
  geometry. Full signed-view boundaries remain guest-only.
- Six compiled effective negatives finish and fail public output/call
  expectations: triangle, hole clearing, UV, width, matrix reload and late origin.
- Copied actual owner preserves17 neighbor bodies, relative relocations and
  pools. Four preexisting owner warnings remain; zero new target warnings.
  Owner target output equals the isolated object. Actual asmprocessor/padder pass.
- Four symbol sets/eight raw original/candidate links,96 cases/192 executions;
  four additional symbol sets/eight original/normalized links match all340
  words each. All17 relocation sites/uses are preserved.
- 48 actual20-word dispatcher cases/96 executions preserve selector0/-1,
  signed-view forwarding, returned cursor and public footprints.
- 20 strict missing-byte cases/40 executions and four lazy-exit cases preserve
  public memory/write/call prefixes; no portable C/FCSR/hardware fault claim.

The initial pre-install ten-test run passed17.986s. The first installed run
caught a fixture assumption about a nonexistent .debugger_data section.
Correct the assertion against actual readelf sections and strengthen the
audit to a complete expected-ELF byte comparison. Final ten tests pass17.255s,
zero skips; do not count the failed run as acceptance.

Explicit make -C conker all NON_MATCHING=1 -j2 finishes successfully.
The unqualified default make invocation built only its first object target;
it was not used as linked acceptance. Existing duplicate generated_12D630
recipes and legacy diagnostics remain; this is not a warning-free build.

The complete expected ELF is the recorded baseline with only the1,360-byte
target slot and its symbol-size field replaced. It equals the installed ELF.
Every other symbol's metadata is unchanged. Header/boot, Init, Init data,
Debugger, Game overflow and protected Game data are byte-identical.
Protected Game data189,088 bytes/720 owners remains exact against checksum-
verified retail; registered pointer8008A670 is unchanged.

Append only84 guards after all11,604 existing rows, preserving their exact
bytes. All conversion/progress rows remain byte-identical. No profile, shared
helper/header, layout, ASM fragment or unrelated source changes.

Installed hashes:

- Source4f6ce9a6b9cc9dd86c09ad0c9a2f613b4afd77fcdae94d18d3193272a081bf3d.
- ELF30fe9875341c31f5fa09a419d009df1208f4cabe427c2cb23a7296c987218ea1.
- Guards6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b.
- Progress5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

## Checkpoint And Next

Tools7986e989678797f759a99c372349403b487099e1 commits the new matching driver
and suite first; parent source/docs pin it next. Mounted and older standalone
tools checks pass. Preserve all108 preexisting older status entries and its
HEADddbdd16 plus both tracked dirty-file hashes. Mirror only two absent new
files there, yielding110 entries. No older checkout commit/reset/push.
No push requested/performed.

Validation passes75 AST/exact-mirror file pairs and164 documents/4,467 relative
links, zero broken links. Fresh CSV calculation confirms5,489/6,042 converted
functions and1,940,312/2,256,728 converted bytes; Game4,816/5,321 and
1,768,876/2,072,880 bytes. No extra conversion credit.

Graph query remains a stale placeholder locator until refreshed. Manual
graphify update . exits1, refusing17,211 nodes over retained38,994; it keeps
19,398 excluded-but-existing nodes from2,972 files. Existing version and empty
devcontainer warnings persist. No force/reinstall/purge. Wait for the separate
post-commit graph hook; its receipt is operational, not byte/semantic proof.

Next adjacent-owner function is81-word/frame0x20 func_151B3184, currently a
false zero-return placeholder in generated_1E0560.c:
VA151B3184..151B32C8 /ROM1E0634..1E0778. Original assembly and retail data
register it at8008BF04 /ROM2309C4, immediately before renderer151B32C8.

1. Recover the real actor-update dispatcher ABI and registered caller path.
   Preserve optional signed16 countdown with narrowing/reload before the
   negative check, controlled by actor+10 bit0 and D_800BE9E4.
2. Recover signed byte selectors at2C/2D into D_8008FAF0, -1 skip behavior,
   first/second coordinate addresses14/20 and third arguments1/0. Preserve
   callback mutation and do not early-return after a failed first callback:
   the second selector is read and dispatched even when deletion is pending.
3. Preserve fresh actor+10 reads after callbacks, masks0x4/0x8 setting mask0x2,
   optional signed selector34 into D_8008FAF8 and eventual func_1516972C cleanup.
   Qualify full accesses/ABI/lifetimes/aliases before frame/register fitting.
4. Continue the neighboring full renderer151B32C8 after the update path is
   recovered and qualified. Do not substitute passing helper stubs for it.

The wider Game matching goal remains active. Ignored receipts live under
conker/build/game-owner-endpoint-quad-match-test/; recovery1177 receipts remain
historical. Root README gets only measured aggregate changes.
