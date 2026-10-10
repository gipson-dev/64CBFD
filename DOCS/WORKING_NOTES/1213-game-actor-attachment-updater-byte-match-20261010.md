# Actor Attachment-Updater Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1212](1212-game-actor-segment-selector-byte-match-20261010.md).
Target func_1502F264: VA 0x1502F264..0x1502F3C8, ROM 0x5C714..0x5C878,
89 words / 356 bytes in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Recover its complete void/slot interface, original leaf body and ordered
attachment copies. Single Codex writer, zero Claude calls; no OGL, Release,
saves, editor or push work. Keep the wider Game matching goal active.

Consumer baseline 08cc655d2e45c84214bfc8c3d112c60ed38dd502; mounted tools
35a4757c04184464d7ae79df941c240169396899. Both start clean. New ignored
baseline conker/build/game-actor-attachment-update-match-test preserves
before-source, ELF, guards, conversion CSV and rodata assembly. Historical
selector, slot, phase, color and curve baselines remain untouched.

Source baseline SHA-256
787d31fd554192cd8e738a74c66e465ceb3f66a7a1f68d316f3db10967b5025c;
ELF 92ef2d2c1eea16e0fa4b1aaf61179228c80fd1284900cfc6af7b691320ab76c1;
guards 95d0a0c48e8d5f1fc6dd35b77d69d4888dbdb6216f5bd6aea882732b32cb477c.

## Recovered Semantics

Actor is D_800CC2D0 plus slot*0x32C. Byte +0x65 is a one-based attached-slot
index: zero returns without reading flags or any attached record. Nonzero
selects base plus index*0x32C minus 0x32C. Current actor byte +0x101 bit 2
also returns without reading the attached matrix pointer.

Read attached +0x1D4. NULL copies float words +0x14/+0x18/+0x1C directly,
in load/store pairs. Non-NULL reads the current actor's word +0x5C only on
that path, selecting a 0x40-byte matrix stride and translation words
+0x30/+0x34/+0x38. These are raw float-bit copies, not arithmetic; signed
zero, infinities, subnormals and quiet/signaling NaN payloads are retained.

Reload current flags before copying attached float +0x180 and setting
current float +0x20 to -4.0f. If flag bit 0x20 is clear, read attached
halfword +0x76, reload flags, store that halfword, copy floats +0x3C/+0x40,
repeat the +0x76 halfword copy, then copy +0x7A and +0x78 in that order.
Do not remove the repeated access from an emitted-order recovery.

If the retained flags' bit 0x40 is clear, copy bytes +7/+8/+9/+10/+15 in
load/store order. Read signed D_80082FA0 after those stores. Negative skips
the loop; otherwise copy byte +11 onward through the inclusive limit,
reloading the global word after every store. A store can change the limit
through an alias; a cached count or fixed copy length is not equivalent.

Slot arithmetic is qualified for all 26 valid native slots. Guest fixtures
also exercise all 256 attachment-index bytes with explicitly mapped records;
that does not establish valid native storage outside the 26-record array.
Fault prefixes qualify emitted instruction order, not portable C faults or
hardware/gameplay acceptance.

## Compiler And Closed Recipe

[Candidate driver](../../tools/experiments/game_actor_attachment_update_candidates.py)
measures 39 complete/profile forms. The unsigned-offset baseline emits
101 words; the signed slot/index form emits 89, but IDO eliminates a flag
reread and hoists the limit read across byte stores. Its 44 word differences
are not just allocation differences. O1 forms emit 157 words / 0x20 frame.
Block-pointer alternatives remain 101 words after correcting their fixture
substitutions; do not report earlier duplicate no-op variants as evidence.

Narrow volatile flag/limit reads and metadata/loop byte stores retain the
original access order. The selected ordered-u32-volatile-stores form emits
all 89 words directly, no frame, zero pools/diagnostics, with 29 isolated-link
word differences. The explicit first angle temporary preserves its load /
flag-reread / store shape. No unused record type is added to production.

[Matching helper](../../tools/experiments/game_actor_attachment_update_matching.py)
requires every one of the 89 raw words and all four actor/global HI16/LO16
relocations. It never reads ROM. The fitting changes only two commutative
address-add operand orders and a closed temporary-register cycle. Append
89 guards: 29 changed words and 60 unchanged dependencies; no insertions,
omissions, scheduling changes, frame changes, pool changes or tail padding.
Every control-flow edge and delay-slot operation remains compiler-emitted.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_attachment_update_match.py):
12 tests pass before installation in 20.644s and after the wider rebuild in
22.409s, following all fixture corrections.

- 14,106 guest cases / 42,318 original/fitted/raw executions cover every flag
  and attachment-index byte, all 26 bounded slots, NULL/non-NULL matrices,
  self-attachment, inclusive/negative limits and diverse raw float words.
  Complete memory/access traces and leaf ABI agree with an independent
  reference. Original coverage is 88/89 words; the compiler-emitted LW at
  word 28 is unreachable because the non-NULL likely delay already loads it.
- 115 alias cases / 345 executions cover matrix translations overlapping
  current actor fields and global-limit words overlapping fixed/loop byte
  stores. Only aligned float/word storage participates in accepted fixtures.
- 120 fault fixtures / 1,428 verified prefixes / 4,284 executions confirm
  each fired gate and the exact entire-memory/trace prefix, in both stack phases.
- Twelve independent links over four symbol sets qualify 240 cases, including
  HI16/signed-LO16 carries; actual padder rejects all 89 stale words and all
  four stale relocation sites. The full raw-word certificate also rejects
  every word mutation.
- 319,488 native32 complete-C cases cover all slots and flag values, four
  attachment modes, six signed limits, NULL/matrix paths and raw NaN payloads.
  A separate native test aliases the actual global symbol to actor byte +12:
  the copy decreases its limit, preserving the complete expected memory.
  This little-endian native alias does not claim big-endian native parity.
- Eight fresh complete compiled negative controls are effective. They include
  zero-based attachment lookup, wrong early bit, fixed/exclusive/cached limit,
  wrong matrix stride and the repeated-angle access. The latter distinguishes
  ordered accesses, not just disjoint final values.
- 320 connected cases use the complete actual banked 88-word dispatcher,
  74-word slot updater, 26-word classifier and 80-word final helper. Their
  linked bodies are checked against ROM. Substituting original versus fitted /
  installed attachment helper preserves full memory, traces and ABI. Other
  dispatcher callbacks are explicitly bounded opaque, not claimed recovered.
- All 37 copied-owner neighbors preserve bodies, relative relocations and
  decoded pools; both complete owner compiles have zero diagnostics. The typed
  caller prototype changes no neighbor words. Actual padded owner changes
  only the target 356-byte slot.

Fixture corrections precede acceptance: define NULL in the standalone native
fixture, force the connected classifier's below-ten gate to fire, restrict
matrix alias inputs to aligned words, and cache the verified current linked
helper once per suite instead of repeatedly rereading production files.
Earlier failed runs are not counted as qualification. The initial diff-patch
formatting attempts applied no production edits before the successful install.

## Linked Checkpoint

Fresh wider build, matcher and tools-check pass. The ignored build.log records
the wider rebuild. Existing shared pointer/type/assembly warnings and duplicate
generated_12D630 recipe warning remain; zero copied-owner diagnostics is not
a claim of a warning-free whole project.

Whole linked ELF changes only the target 356-byte slot and symbol extent,
normalizing symbol/string metadata for comparison. Old guards remain an exact
byte prefix; parsed rows equal old rows plus the 89 new rows. Conversion CSV
and rodata assembly remain exact. Protected .game_data remains 189,088 bytes /
720 owners, zero byte or owner differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Final source SHA-256
aad32d41cf0c19f101403444b11bd4393ab6c415e6a0acde2b9484f7dfba63d3;
ELF 25dfb7f6cd6f59da92da7631098beadb7fafd65f823830a2ef4a51bc5cc4facf;
guards 25077ad5131a5888739c0653a2f29464e949d5e94bf6b7c3980515d9b56ec2c8;
conversion CSV 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Fresh match-progress: Game 2,755/4,816 (57.21%), total 3,428/5,489 (62.45%),
Init 492/492 and Debugger 181/181 exact; zero drift / 2,061 different.
Converted function/byte totals stay unchanged because the old stub already
counted as C. Root README changes only the two aggregate matching rows.

## Bank And Resume

Bank mounted tools 9f1e85e027d2294c5b5423fbfae3f46c7892cd98 first, then
consumer source/guards/docs/pin, without push.
Only the three absent new files are mirrored to the older tools checkout;
preserve HEAD ddbdd16 and both tracked-dirty fingerprints. Older dirty entries
increase from 183 to 186 solely for these mirrors. No older commit/reset.
Verify the new consumer detached graph hook independently of historical logs.

Scoped validator passes: 35 documents / 4,172 relative links, zero broken
links; 58 authored tools have exact older mirrors and AST parsing in both
copies. Older HEAD and both tracked-dirty fingerprints remain unchanged.

Manual graphify update exits 1, refusing a 39,332 to 17,551-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
skill/package and zero-node devcontainer warnings remain. No force, purge,
package install or policy change.

1. Next is func_1502C608: VA 0x1502C608..0x1502C6E8, ROM 0x59AB8..0x59B98,
   56 words / 224 bytes, frame 0x28. The dispatcher state-2 path calls it;
   its current source is still a zero-return placeholder.
2. Recover the global byte disable gate, actor byte +7 gate, signed halfwords
   +0x60/+0x62 captured before the callback, and actual func_1502C3BC connection.
   Preserve original private halfword homes +0x22/+0x20 and actor home +0x18.
3. Read D_8008CA4C[result]->byte4 after the callback, shift it eight bits, wrap
   the sum to s16, and perform only one subtract/add with s16 wrap. Do not
   replace it with modulo or reload captured fields after callbacks.
4. Qualify complete callback mutation, signed/wrapping boundaries, physical
   shape, actual dispatcher and whole linked audit before installation.

Preserve the separate uninstalled curve rejection in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and hardware/live acceptance remain open.
