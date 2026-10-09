# Game Owner Endpoint Quad Recovery And Frame Fit

Continue from [Note 1176](1176-game-owner-companion-setup-guarded-c-match-20261009.md).
Start clean at parent5a3922f0/tools211a2f1. One Codex writer, zero Claude calls;
follow the scoped [agent workflow](../AGENT_WORKFLOW.md). Keep the same target
through full semantics, compiler fitting and qualification; tools commit first.
No push or OGL/Release/save/editor changes.

## Result And Installation Gate

Recover complete **func_151B2974**, VA151B2974..151B2EC4,
ROM1DFE24..1E0374,340 words/1,360 bytes, original frame0xB8.
The [complete driver](../../tools/experiments/game_owner_endpoint_quad_candidates.py)
and [nine-test suite](../../tools/tests/test_game_owner_endpoint_quad_recovery.py)
are banked. The selected body now has the correct340-word length and184-byte
frame, down from the initial340/frame200 candidate. **140 instruction
differences remain; this is not an installed C match.**

Keep [production source](../../conker/src/game/generated_1DF510.c) and the
[complete original owner assembly](../../conker/asm/1DF510.s) unchanged.
Production still contains its false no-argument zero-return C placeholder;
this note does not present that placeholder as recovery or original assembly.
No scoped2974 fragment exists. Full assembly remains the source of retail truth.
No guard/profile/header changes, conversion credit or new byte-exact credit.
Root README aggregate rows remain correct and are deliberately unchanged.

## Actual Caller And ABI

The local graph finds the stale func_151B2974() node at sourceL311; it is
navigation evidence, not ABI proof. An aligned big-endian retail pointer scan
finds the unique target pointer at ROM22F130, mapping through the YAML Game
data segment2275E0/80082B20 to **D_8008A670[0] at8008A670**.
Verify the same pointer in the installed protected Game data.

The real caller is func_15149490, VA15149490..151494E0,
ROM176940..176990,20 words. Its installed linked body equals retail.
Existing source and variables.h declare the three-argument graphics callback:
display-list cursorA0, actorA1, signed16-bit viewA2. The target returns the
retained or advanced display-list cursor, not a synthetic zero.
Caller reads the signed actor+12 selector, skips dispatch for-1 and uses
table entry0 for this renderer. Connected tests qualify0 and-1 only;
other selectors and their separate callbacks are not covered.

## Full Recovered Contract

All offsets below are hexadecimal unless decimal lengths/values are stated.

Start invalid=0, pair=actor+28. Read the endpoint pointer and its first word.
If that word is0, mark invalid without reading its code. Otherwise compare
pair+4 with endpoint+3B; mismatch marks invalid. Refresh pair=actor+28.
An invalid actor receives signed-1 at actor+E and returns its original cursor.
A valid endpoint with NULL resource at+1D4 also returns unchanged but does not
mark the actor invalid.

Request64 bytes through func_151D5D60(actor+14,view,64,&cursor,NULL).
A NULL cursor returns immediately without transforms or graphics globals.
Allocation may mutate the actor's endpoint pointer and joint byte; read their
post-allocation values before selecting the transform matrix:
endpoint+1D4 plus unsigned pair+5 times64.

Transform pair+8 into first position and pair+14 into second position with
func_15143134. Retain the **same matrix pointer** across both transforms,
even if the first helper mutates the endpoint resource or joint.
The second transform uses the then-current second input coordinates.
Transforms are bounded interface models, not a claim of matrix/SDK parity.

After both transforms, capture origin=D_800DBFF0+signedView*0x9A0+2F8.
Later graphics callbacks may change that global pointer; retain this captured
origin pointer, while reading its coordinate values after those callbacks.
Initialize sync=1 and make six exact graphics-state calls:

- func_15142B7C(output,0x200005,0x60600).
- func_15142E24(output,D_80090DE8,0,0,0,0,54,0,NULL,&sync,3).
- func_15142C10(output,255,255,255,255,&sync).
- func_15142CF0(output,0,0,255,255,255,255,&sync).
- func_1513F4E4(output,0x2B,&sync).
- func_15142FBC(output,D_800D2C9C|0x80000|0x2CA0,
  D_800A4AC8[11]|D_800A4AC8[10],&sync).

Return values thread the cursor through every helper. Render-state globals are
read late, after preceding callbacks, not cached before them.
The bounded state hooks consume the actual sync pointer and clobber scratch
GPR/FP registers and outgoing homes to qualify retained lifetimes.

Let delta=second-first and ray=delta*0.5+first-origin, with each operation
rounded to binary32. Compute normal=delta cross ray and its squared length.
A zero squared length produces three positive-zero offsets without reading
width. Otherwise use sqrtf and scale=pair+20 width divided by length.
Reuse normal locals for the three scaled offsets in the selected frame-fit form.
Negative width is retained, not clamped.

Write four16-byte Vtx records: second+offset, second-offset, first-offset,
first+offset. Signed truncation then16-bit stores produce each coordinate.
Texture coordinates are(0,0),(960,0),(960,960),(0,960).
**Do not write Vtx flag bytes6/7 or color bytes12..15.**
Those six holes per vertex retain allocator/aliased/helper-mutated memory.

Append the SDK four-vertex load and triangles(0,1,2),(0,2,3).
Their words are01004008/pointer,05000204/0,05000406/0.
Use the original four-record base, not the advanced cursor, for the vertex load.
Return the final graphics cursor. Vertex allocation, transforms and six graphics
helpers remain bounded; no live renderer/gameplay/hardware acceptance claim.

## Compiler Evidence And Next Fit

Final catalog: nine complete bodies/12 profile rows, all nonmatching.
Selected (words/frame/differences):
O2/g3 340/184/140, O2 339/184/338,
O1/g3 406/168/397, O1 406/168/396.
Every isolated row has zero diagnostics and no literal pools.
The initial complete body is340/200/155; separate-zero is340/184/138,
but it has not received the selected body's full qualification.
No bulk prefix substitution or unexplained guard installation is authorized.

Twenty-four ignored real-local/temporary reuse probes identify the current
frame fit. Drop the separate squared local and reuse normal components for
offsets. This preserves the complete body, public behavior and original frame.
Selected private locations still differ:
invalidB2/syncB3/cursorB4/firstA4/second98/matrix90/origin8C versus
retail invalidB3/syncB2/cursorAC/first80/second74/matrix64/originA8.
SavedS0/S1/RA already occupy34/38/3C. Many remaining words reflect private
layout and closed register allocation, but they are not yet certified guards.

Resume **the same func_151B2974 fitting**. Recover its declaration/workspace
shape and these private addresses, then resolve the measured register schedules.
Do not move to an easier target or install a word table. Qualify any improved
complete form, rebuild and audit the linked ELF, then refresh totals.

## Qualification

Final **nine tests pass29.375s, zero skips**:

- Twelve complete profile rows compile and fail the byte-exact installation gate.
  Assert selected340/frame184/140 and unchanged production placeholder.
- 384 guest cases/768 executions: lazy invalid/resource/allocation exits,
  endpoint distinct/actor aliases, four finite and degenerate geometries, signed
  view boundaries, joint0/255, helper mutations, two stack phases and vertex
  writes over actor endpoint inputs. Independently check complete public memory,
  ordered public writes, logical calls, returns and saved GPR/FP lifetimes.
- Reach339 retail instruction words. The sole missing word151B2A14 is a duplicate
  load after the unconditional failure jump; success likely-branches over it.
  Verify both predecessor instructions explicitly. Do not call this340-word
  dynamic coverage. No full raw private-stack/access-trace claim.
- Six compiled effective negatives finish and fail independent public outputs/
  calls: wrong triangle, clearing vertex holes, wrong UV, wrong width, reloaded
  matrix and late origin recapture. They fail behavior, not arbitrary assertions.
- Copied owner with actual asmprocessor/padder preserves17 neighbors, pools,
  relative relocations and four old Warning712 messages. Zero new target
  diagnostics. Scratch padding accepts the nonmatching body; it does not authorize
  production installation.
- Source, entire ELF, guard manifest and progress CSV hashes remain unchanged.
  Protected Game data189,088 bytes/720 owners stays exact; retail/installed
  graphics callback pointer remains8008A670.
- 11,520 native32 executions of the actual selected C body: five signed views,
  two joint values, aliases, mutations, exits and geometry patterns. Independent
  binary32 arithmetic expectations and typed helper contracts check all64
  vertex bytes including holes and all three final commands.
  Full signed-view boundaries are guest-only. No FCSR/hardware claim.
- Four independent symbol sets/eight links,96 cases/192 executions.
  Assemble original directly from the unique full-owner target block; its
  default link equals all340 ROM words. Preserve the same17 relocation type/
  symbol uses, while allowing measured nonmatching relative offsets.
  Independently check public outputs/calls/writes under segment/low-half changes.
- 48 actual20-word dispatcher cases/96 executions connect original and candidate
  renderers through the real registered table pointer; verify installed caller
  exactness, signed view forwarding, skip path and returned cursor propagation.
- 20 missing-byte cases/40 executions and four lazy-exit cases compare public
  memory/write/call prefixes. Strict missing-write checks are enforced.
  Missing helper input records helper entry before fault. No portable C fault,
  private access order, FCSR, asynchronous alias or hardware guarantee.

Earlier runs catch the unreachable-word coverage assumption and native fixture
issues: misleading-indentation diagnostics, identity byte seeded before aliased
coordinates, and hole expectations missing helper mutations. Correct those
fixtures without removing alias cases or relaxing exact write/byte comparisons.
Fault-reference corrections record helper entry before its input fault and
reject writes to absent bytes. Production remains untouched throughout.

## Banked Checkpoint

Tools71976ff9d4bc99643ef734b430d38c200f89f257 commits exactly the new driver
and suite first; parent docs pin it next. Preserve all106 preexisting older
standalone tools status entries, HEADddbdd16 and both tracked dirty hashes.
Mirror only these two absent authored files there, yielding108 entries.
No older checkout commit/reset/push. Mounted make tools-check and older
standalone check_project_tools.py both pass.

Fresh production build/progress targets are up to date.
Fresh match-progress NON_MATCHING=1 confirms unchanged Game2,740/4,816 exact,
total3,413/5,489,zero drift/2,076 differences. No new credit.
Converted5,489/6,042 (90.85%),85.98% bytes; Game4,816/5,321 (90.51%),85.33%.

Validation passes73 AST/exact-mirror file pairs and163 documents/4,457 relative
links, zero broken links. Manual Graphify update exits1, refusing17,199 nodes
over retained38,984 and preserving19,398 excluded-but-existing nodes from2,972
files. Existing version/devcontainer warnings persist. Preserve that history,
no force/reinstall/purge. Wait for the separate post-commit hook before close-out;
its operational graph receipt is not semantic or byte-matching proof.

Ignored conker/build/game-owner-endpoint-quad-test holds shape/guest/native/
negative/owner/unchanged/rebase/dispatcher/fault receipts.
Driver rows live in conker/build/game-owner-endpoint-quad/measurements.json.
Its fitting/fitting2 directories retain24 complete exploratory objects/sources.

Unchanged source SHA256: 1ea7fbb5840d0dd0cdbd1137be018f3b9f4aecd3ec95b8e2a6c2202ac4ea6ac6.
Unchanged ELF SHA256: 873bf0f5b6f335c423f8d577cf0e330bf522bfaf04017bffd57ec5d2b6388dde.
Unchanged guards SHA256: e3e98d06c96d3bd4130f26b54a9d03b7fbce4d61d9cbc7a3410817fbf5bab0af.
Unchanged progress SHA256: 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.
The Game goal stays active. Full helpers/SDK/renderer/gameplay remain open.
