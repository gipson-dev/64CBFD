# Game Owner Ribbon Renderer Recovery Checkpoint

Date: 2026-10-09

## Result And Boundary

Recover the complete475-word func_151B32C8 renderer as semantic C in the
[candidate driver](../../tools/experiments/game_owner_ribbon_renderer_candidates.py).
This is a qualified, uninstalled recovery, not a byte match. The production
zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.

- VA151B32C8..151B3A34; ROM1E0778..1E0EE4;475 words/1,900 bytes.
- Original frame0x148 (328 bytes); S0..S4/RA saves70..84 and F20..F30 saves40..68.
- Selected complete O2/g3 C:477 words/frame304/432 word differences.
- Zero target diagnostics and zero pool bytes. Actual padder rejects the two-word
  slot overflow; no guards or installation authorized.
- Eleven tests pass20.010s, zero skips; all475 retail words reached.
- Production source/ELF/guards/progress are byte-identical to the baseline.
- No new matching or conversion credit. README aggregate rows remain unchanged.

Resume from [Note 1179](1179-game-owner-actor-update-direct-match-20261009.md).
Parent3b27c459b0aac565a09f4f8c7d341e4e3a2c5c46,
mounted tools baseline ae5a4de312cecb275c6de7780301371f5e81ecd3.
Both relevant checkouts were clean. One Codex writer, zero Claude calls.
No OGL/Release/save/editor changes.

## Full Renderer Contract

Actual callback ABI: Gfx *(Gfx *output, u8 *actor, s16 view).
Registered pointer8008BF0C /ROM2309CC is the type0x33 table's offset8 entry.
The complete original graphics walker is func_151674F8, not the unrelated
20-word effect dispatcher15149490.

1. Independently test actor+10 masks4,8,2 and return the original cursor for
   any set mask. No resource/material/geometry reads on these exits.
2. func_151D5D60(actor+140, signed16 view, 0x190, &vertices, NULL).
   A null vertex cursor returns the original Gfx cursor.
3. Capture origin = D_800DBFF0 +view*0x9A0 +0x2F8 before the material callback.
   Later changes to the global base do not replace this retained pointer.
4. Fresh unsigned-byte actor+2E indexes D_8008FB10; call its selected material
   callback with actor and13 output pointers. Zero return exits; nonzero
   permits the entire renderer. Setup/material mutation does not recheck flags.
5. Forward all11 word outputs and bank/combine byte outputs to the original
   graphics helper chain in the original order. Preserve sync byte lifetime.
6. Copy positions from actor+48 and actor+60. Points have24-byte stride; each
   copy retains exactly the first12 bytes of its record, not the whole24 bytes.
7. Emit the initial two vertices around the first point, using ray first-origin
   and tangent second-first. UVs are0/0 and0x3C0/0.
8. Read the signed word at actor+13C into a wrapping32-bit texture accumulator.
   Iterate offsets18..D8 inclusive, increment18; exactly nine iterations.
   Reload both point copies for each segment. Use ray second-origin and the
   same tangent second-first; emit two vertices around the second point.
9. Fresh-read actor+13C after each emitted pair, including the final pair,
   adding modulo2^32. Vertex texture T receives low16 bits.
10. Emit gSPVertex(last four vertices,4,0), then triangles(0,1,2) and(1,3,2).
    Preserve every pointer increment and returned Gfx cursor.

Total20 vertices/320 bytes and nine quads/27 commands. Shader hooks add six
bounded placeholder commands in the suite; these are not the actual full SDK
helper implementations.

For each pair compute:
tangent = second-first; ray = endpoint-origin;
normal = tangent cross ray; length2 = (nx*nx +ny*ny) +nz*nz.
Zero length sets three offsets to zero; otherwise multiply normal by
fresh actor+30 width /sqrt(length2), preserving binary32 operation grouping.
Negative width is retained. Truncate coordinates to low signed16 fields.

Every vertex writes xyz, S/T, and color255/100/100/255 in original order.
Flag bytes6/7 remain untouched:40 holes across20 vertices. There is no vertex
bzero and no replacement single quad.

Material outputs, in argument order:
mode1, mode2, envR, envG, envB, alpha, primR, primG, primB, primA, renderMode,
bank byte, combine byte. Primitive receives primR..primA; environment receives
0,0,envR,envG,envB,alpha. Render-mode helper uses
renderMode |0x80000 |fresh D_800D2C9C |0x2CA0, and fresh
D_800A4AC8[bank*2+1] |D_800A4AC8[bank*2].
Keep the original texture helper parameters0,0,0,0,54,0,NULL,&sync,3.

## Qualification Evidence

[Recovery suite](../../tools/tests/test_game_owner_ribbon_renderer_recovery.py)
uses the existing full-function compiler, strict guest interpreter, native32,
owner/pool/padder, linked data and relocation helpers.

- 512 primary guest cases/1,024 executions cover all three flag exits, allocation/
  material failure, four geometry patterns, both stack phases and vertex/texture-
  word aliases. All475 retail instructions reached. Independent public memory,
  returned cursor, complete ordered writes and helper arguments match.
- 385 mutation/width cases/770 executions cover signed16 view boundaries,
  unsigned selector255, retained camera origin and fresh selector/position/width/
  step/render-mode/table reads. Full-word material outputs and byte bank/combine
  widths are checked. Hostile volatile registers and outgoing argument homes
  are clobbered across hooks.
- 7,680 native32 executions of actual complete C check all1,024 actor bytes,
  all416 vertex-buffer bytes and all320 command-buffer bytes against independent
  expected data. Cover finite binary32 geometry, zero normal, negative width,
  early exits, five signed views, helper mutations, texture wrapping and alias.
- Six compiled semantic negatives are effective: wrong triangle, zeroed vertex
  flags, wrong S, eight rather than nine quads, late origin reload and cached
  texture step. The latter uses a deliberate future-vertex/step alias and
  zero-origin configuration; a nonchanging alias would not distinguish it.
- Four symbol sets/eight independently assembled original/candidate links;
 64 cases/128 executions agree semantically. All17 relocation type/symbol uses
  are preserved. No rebase byte-match claim.
-32 cases/64 executions connect the complete actual34-word func_151B498C
 material callback. Its production linked body is exact; all34 words reached.
 The second material callback151B4A14 remains separately open.
-32 cases/64 executions run the complete original348-word func_151674F8 walker.
 Its actual type0x33 record reads8008BF0C, forwards output/actor/signed view
 and consumes the returned cursor. Test both rows, empty/present actor lists,
 nesting2 and budget-mode0/1 below the budget limit. Check outer commands and
 nesting/continuation restoration. Range-selector15168F84 is a bounded hook;
 caller recovery and overflow/rollback behavior are not claimed complete.
-12 strict missing-byte cases/24 executions retain public call/write prefixes,
 plus three lazy exit fixtures with geometry/step/origin bytes deliberately
 missing. Guest prefix agreement is not portable C/FCSR/hardware fault semantics.
- Actual copied owner preserves16 neighbor bodies, relative relocations and
 pools, with zero preexisting/new warnings. Target owner output equals the
 isolated selected object. Actual padder rejects the oversized body.
- Source/ELF/guard/progress hashes remain unchanged. Protected Game data189,088
 bytes/720 owners matches retail; registered renderer pointer is unchanged.

Callbacks/setup and graphics helpers are bounded where not explicitly connected.
Model agreement is not full hardware, FCSR, live-rendering or gameplay acceptance.
Only the explicitly connected actual material callback is qualified as installed
here. Signed full-view edges are guest-only; native cases are finite/in-range.

Initial fixture failures were an ineffective cached-step negative and native
misleading-indentation warnings. Correct their fixtures, not production code.
The final eleven-test rerun passes23.776s, zero skips; failed runs are not
acceptance receipts.

## Compiler Screen And Installation Gate

| Candidate/profile | Words | Frame bytes | Differences |
| --- | ---: | ---: | ---: |
| Selected O2/g3 |477|304|432|
| Selected O2 |477|304|458|
| Selected O1/g3 |593|216|586|
| Selected O1 |593|216|585|
| Separate zero assignments |477|304|432|
| Separate point declarations |477|304|432|
| Volatile cursor |476|304|458|
| Signed texture accumulator |477|304|432|
| Less-than loop condition |477|304|432|
| Pointer loop |466|280|450|
| Separate normal/offset plus squared/length |477|320|432|

All11 full-profile/control rows are rejected for installation. The smaller
pointer loop is not accepted merely because it fits the slot; its frame/body
still differ. Do not synthesize literal retail words to close this renderer.

Unchanged hashes:
source33a6690f6229713ead48a1ba2fb2d826cb268a28c889671d378b4a1e94e1179b;
ELF952b3100768e9ef8f6ff029c29bcfe1bba3bda03d66d6b97769b02313b77eac8;
guards6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b;
progress5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Game2,742/4,816 exact,total3,415/5,489,zero drift/2,074 differences are the
unchanged Note1179 linked baseline, not a fresh matching increase.

## Checkpoint And Resume

Tools 5a82484 commits the recovery driver/suite
first; parent docs pin that checkpoint next. Mounted/older tools checks pass.
Preserve all112 preexisting older dirty entries, HEADddbdd16 and both tracked
dirty-file hashes. Mirror only the two absent authored files, yielding114;
no older checkout commit/reset/push. No push requested/performed.

Documentation validation passes:166 documents,4,487 relative links,zero broken.
All79 authored tooling files parse and have exact mounted/older mirror bytes.

Graph query locates the real production placeholder at line75; it is not evidence
of an installed renderer. Let the separate post-commit graph hook finish; no
graph force, dependency installation or purge is authorized.

Continue this same func_151B32C8, not another easier function:

1. Fit real declaration/temporary lifetimes to the328-byte retail workspace.
   Important homes: cursor140; first134; second128; retained origin120;
   syncEF; material word outputsE8..C0; bankBF; combineBE.
   The expanded320-byte probe is only a measured candidate, not acceptance.
2. Resolve the two-word code-length excess and original offset/pointer induction
   without changing the nine-segment public contract. Retain unsigned texture
   wrap, the initial pair and fresh per-segment step reads.
3. Qualify complete new source variants through the existing reference/native/
   connected callback/walker tests, then fit scheduling/register allocation.
4. Install only after all475 linked words, owner neighbors/pools/relocations,
   protected data and all guard/conversion history pass their gates. Do not
   claim matching/conversion credit until a fresh linked build proves it.

Ignored receipts: conker/build/game-owner-ribbon-renderer-test/ and
conker/build/game-owner-ribbon-renderer/. Wider Game matching remains active.
