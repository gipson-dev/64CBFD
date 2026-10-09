# Game Owner Actor Update Direct Match

Date: 2026-10-09

## Result

Replace func_151B3184's false zero-return placeholder with its complete semantic
actor timer/callback updater in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c).
All 81 words emit directly from C under existing O2/g3; no guards or assembly
restoration. The actual ABI is void (u8 *actor), not s32 (void).

- VA151B3184..151B32C8; ROM1E0634..1E0778; 81 words/324 bytes.
- Frame0x20, saved RA at14, pending-delete byte at1B, incoming actor home20.
- Zero isolated diagnostics and zero pool bytes; O2 also matches all81 words.
- Nine installed tests pass11.396s, zero skips.
- Fresh Game2,742/4,816 exact (56.94%), total3,415/5,489 (62.22%).
- Zero address drift;2,074 remaining differences.
- All conversion rows/bytes unchanged: the old false placeholder already counted
  as C. This recovery adds matching credit, not additional conversion credit.

Continue from [Note 1178](1178-game-owner-endpoint-quad-guarded-c-match-20261009.md).
Parent baseline a1a90af6290222fec31ff1c84ae301f3e1eeeff1,
mounted tools baseline7986e989678797f759a99c372349403b487099e1.
One Codex writer, zero Claude calls. No host/OGL/Release/save/editor changes.

## Complete Contract And Source Fit

The actor-type0x33 registration is D_8008B4A8 +0x33*0x34 =8008BF04;
retail ROM2309C4 points to151B3184. Its renderer pointer8008BF0C /ROM2309CC
points to151B32C8. The original registered update walker is func_151670C0.

When actor+10 bit0 is set, subtract D_800BE9E4 from the signed16 timer at12,
store the low16 bits and reload signed16 before checking negativity. Timer
expiration skips all three callbacks/dirty-flag processing and requests cleanup.

Otherwise signed-byte selectors2C/2D dispatch D_8008FAF0, with -1 skipping:
first (actor, actor+14, 1), then (actor, actor+20, 0). Zero return marks deletion;
every nonzero word is success. A failed first callback does not skip the second.
Read the second selector after the first callback, preserving mutation.

Fresh flags at10 with either mask4 or8 set mask2 and skip the third callback.
Otherwise signed selector34 dispatches D_8008FAF8(actor), -1 skipping;
zero return marks deletion. Pending deletion survives every callback, including
hostile volatile-register clobbers and dirty-flag processing. Finally call
func_1516972C(actor) when deletion is pending.

The first array's actual entries are151B3F28/151B2FA0; the second array's six
entries are151B3A7C/151B3CF0/151B3FDC/151B42A4/151B48DC/151B4B78.
Recover the observed callback return/argument ABI locally without altering
unrelated placeholder/helper headers.

The first complete body had81 words/frame32 and six differences: only its
pending byte was1F instead of1B in three save/reload pairs. Declare a real s32
selector before the u8 pending byte, assigning the signed2C/2D selector before
each dispatch. This recovers the retail1B home with no dummy padding locals,
profile changes, literal instruction replacement or guards.

| Profile | Words | Frame bytes | Differences |
| --- | ---: | ---: | ---: |
| O2/g3 |81|32|0|
| O2 |81|32|0|
| O1/g3 |95|32|88|
| O1 |95|32|89|

The retained screen also measures unfitted/byte-selector/wide-pending locals,
volatile actor, combined-mask spelling and nested third-call variants.
[Candidate driver](../../tools/experiments/game_owner_actor_update_candidates.py)
persists all11 complete profile/control measurements in the ignored output.

## Qualification

[Focused suite](../../tools/tests/test_game_owner_actor_update_match.py) reuses
existing compiler, strict guest model, native32, owner/padder and ELF helpers.

- 6,048 guest cases/12,096 executions cover timer truncation/sign/wrap, -1 skips,
  both coordinate calls, all deletion-result positions, flags and both stack
  phases. All81 words reached. Compare against independent semantic memory,
  writes and call expectations; complete private/public memory and ordered
  read/write/call traces equal between retail and candidate.
- 144 callback-mutation cases/288 executions preserve fresh selectors/flags,
  coordinate writes and pending deletion under hostile volatile clobbers.
  A compiled wrong-cleanup condition is detected by actual call expectations.
- 102,400 native32 executions of actual selected C cover all256 flag bytes,
  signed timer edges, narrowing/wrap, callback result masks and first-callback
  selector/flag mutation. Compare all384 actor bytes with independent expected
  bytes, not merely selected output fields.
- 16 complete original74-word walker cases/32 executions exercise both rows,
  empty/one/two/three-actor lists, nesting0/2 and both stack phases. The real
  JALR delay slot saves actor.next before cleanup clears that pointer. Callback
  visitation and nesting/continuation restoration agree.
- Four symbol sets/eight independent original/candidate links match81 words
  each; all nine relocation type/symbol uses are retained.
- Actual copied owner preserves16 neighbor bodies, pools and relative
  relocations. Zero owner warnings before/after. Actual asmprocessor/padder pass.
- Six strict lazy-read/fault-prefix cases/12 executions: disabled timer has no
  clock read, expiry has no selector reads, dirty flags skip selector34;
  missing timer/first/second-selector bytes fail with equal access prefixes.

Signed out-of-array selector probes use explicitly mapped guest callback cells
to qualify retail indexing and lack of an added range check. They are not
native C bounds-safety claims. Callback and cleanup hooks are bounded, not
acceptance of all actual helper bodies. The original full walker remains a
false C placeholder in production; its connected retail test does not claim
that caller is installed/recovered. Hardware, FCSR, live rendering and gameplay
acceptance remain separate.

Initial fixture failures exposed missing signed-byte load support, an unused
native fixture variable and overlapping synthetic callback cells. Correct
these locally, preserve actual array entries and derive callback arity from
the callsite rather than target identity. Nine pre-install tests pass11.157s;
nine final installed tests pass11.396s. Failed runs are not acceptance receipts.

## Linked Audit And Checkpoint

Explicit make -C conker -j2 build/conker.us.elf progress.csv NON_MATCHING=1
passes; retain preexisting duplicate generated_12D630 recipe warnings.
Fresh match-progress measures the aggregates above.

The entire installed ELF equals the recorded baseline with only this324-byte
function slot and its target symbol-size field replaced. All other function
bytes/addresses/sizes, symbol metadata, header/boot, Init/data, Debugger,
Game overflow and Game data remain byte-identical.
Protected Game data189,088 bytes/720 owners is exact against retail;
the registered8008BF04 callback pointer remains unchanged.

All existing11,688 guard rows and their complete bytes are unchanged.
Conversion/progress rows remain byte-identical; converted total5,489/6,042
(90.85%),1,940,312/2,256,728 bytes (85.98%); Game4,816/5,321 (90.51%),
1,768,876/2,072,880 bytes (85.33%).

Installed hashes:

- Source33a6690f6229713ead48a1ba2fb2d826cb268a28c889671d378b4a1e94e1179b.
- ELF952b3100768e9ef8f6ff029c29bcfe1bba3bda03d66d6b97769b02313b77eac8.
- Guards6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b.
- Progress5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Tools ae5a4de312cecb275c6de7780301371f5e81ecd3 commits the driver and suite first;
parent source/docs pin it next. Mounted/older tools checks pass. Preserve all110
preexisting older dirty entries and HEADddbdd16. Mirror only two absent authored
files, yielding112 entries; no older checkout commit/reset/push.
No push requested/performed. Root README receives measured aggregate rows only.

Validation passes77 AST/exact-mirror file pairs and165 documents/4,477 relative
links, zero broken links. Both preexisting tracked dirty-file hashes and every
older status entry remain unchanged. The separate post-commit graph hook is
operational indexing, not matching/semantic acceptance; wait for its completion
before ending the checkpoint. No graph force/reinstall/purge is authorized.

## Next Target

Continue complete neighboring renderer func_151B32C8:
VA151B32C8..151B3A34 /ROM1E0778..1E0EE4,475 words/frame0x148.
Registered8008BF0C, original three-argument graphics callback:
Gfx *(Gfx *output, u8 *actor, s16 view), with returned cursor in V0.
Its production body is still a false zero-return placeholder.

1. Recover complete original gates for actor flags4/8/2, retained actor/output/
   signed view and func_151D5D60 resource setup with packet actor+140.
2. Recover full helper ABI, retained resource/matrix/geometry lifetimes, vertex
   writes and SDK commands before any compiler fitting or installation.
3. Qualify independent complete output/memory expectations, mutation/alias/
   boundary cases, actual registered caller and protected-owner/linked audits.
4. Keep full helper/hardware/gameplay gates separate; do not count a partial
   renderer or passing bounded hooks as full implementation acceptance.

Ignored receipts: conker/build/game-owner-actor-update-test/ and
conker/build/game-owner-actor-update/. The wider Game matching goal remains active.
