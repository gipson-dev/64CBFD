# Complete Actor Animation Constructor Byte Match

Date: 2026-10-10

Continue [Note 1236](1236-game-actor-animation-request-direct-conversion-20261010.md).
Recover full func_15083568 instead of its false zero-return C placeholder.
The wider Game matching goal stays active; retail matching is not host or
live-gameplay acceptance. Single Codex writer, zero Claude calls.

## Scope And Baseline

- Consumer starts clean at 5673f44a, mounted tools clean at da7086a. Follow
  keep-committed authorization: tools first, consumer source/docs/tools pin
  second, no push. Original assembly and reference inputs stay preserved.
- Owner conker/src/game/generated_AEB40.c; VA 0x15083568..0x150836CC,
  ROM 0xB0A18..0xB0B7C, 89 words / 356 bytes, original 0x68 frame.
  Existing C emits 12 bytes and differs in 88 words over the complete slot.
  Graph query finds the old placeholder node; inspect the complete assembly,
  both outgoing packets and the actual request/record caller chain.
- Seven immutable before-* snapshots cover owner, ELF, guards, conversion
  CSV, protected rodata, tracked symbols and ignored undefined assignments.
  Before-source SHA-256
  a6cc09d04c11375374c05a7d71a695b6ff491630b5b8f226c4650173613d3242;
  ELF bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
  Recheck every snapshot, never overwrite the baseline after installation.
- Older tools remains ddbdd16, independently dirty: 237 native Windows Git
  entries before, 240 after three absent-path authored mirrors. Exact mirrored
  bytes and six Python parses pass. Preserve protected dirty fingerprints
  game_owner_pool.py
  159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E and
  test_game_node_effect_registration_match.py
  C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input edits.

## Recovered Behavior

Select the eight-byte D_80086CC4 descriptor with animation - 1. Read its
unsigned byte count and record pointer even when count is zero. Zero count
returns NULL without dereferencing actor or records. Otherwise scan 16-byte
records, retaining the initial pointer while rereading the live count after
each callback. Callback count shrink/growth applies immediately; changing the
descriptor pointer does not redirect the active cursor. No added index clamp,
record-null guard, count cap or early exit on a NULL callback result.

Type byte +3 chooses the outgoing packet. Type 0 calls func_15083AC8 with
actor, bytes 1/0, zero, bytes 2/4/5/6 and the original single scale: nine O32
arguments, final float bits at stack +0x20. Other types call func_15030AF4
with actor, bytes 0/1/7/4/5, full-word mode, animation ID, byte 2, record +8,
selector and bytes 14/15: thirteen arguments through stack +0x30. Selector
is unsigned byte 6 only for type 2, otherwise full-word -1. Return the last
callback result, including NULL; intermediate NULL does not stop iteration.

The initial linear-for body emits 88 words with the right frame but 67
positional differences. Splitting the loaded records pointer from the active
cursor recovers all 89 words. Seventeen checked words close the initial
A2/V0 pointer lifetime, byte-temporary register cycles, and the independent
animation-ID/payload-address schedule. No insertions, omissions, body fill,
alternate profile or pool. Original table HI16/LO16 at +0x3C/+0x40 and both
JALs at +0xA8/+0x110 remain unchanged. Every guard rejects stale compiler words
or relocations; all 89 individually perturbed words reject.

## Explicit Helper ABI Correction

The local func_15083AC8 placeholder now has a recovered typed nine-argument
signature with final f32 and pointer return. Leaving its old unspecified
prototype would promote the ninth float to double and break the retail packet.
Its C body still returns zero: this is not restoration of the actual helper.
IDO O2/g3 emits four incoming A0..A3 home stores before that return, changing
this one explicit stub from 12 to 28 bytes. Register keywords do not remove
those debug home stores; unnamed/old-style definitions reject the prototype.
Do not hide the observed neighbor change or claim all neighbors stayed exact.

Qualify all seven emitted stub words and their four caller-home writes through
an independent reference. The other 29 owner functions remain byte/extent/
relocation exact. The actual other helper still has its old zero placeholder.
The full ELF audit permits only the 356-byte constructor and 28-byte typed
stub slots plus their two symbol extents; all other linked bytes must match.

Tools: [complete candidates](../../tools/experiments/game_actor_animation_constructor_candidates.py),
[closed recipe and publisher](../../tools/experiments/game_actor_animation_constructor_matching.py),
[qualification and audit](../../tools/tests/test_game_actor_animation_constructor_match.py).

## Fresh Qualification

- 15,630 cases / 46,890 retail/raw-C/fitted-C guest runs pass an independent
  full private-order reference. All type/count bytes, unsigned record fields,
  full-word mode, count mutations, cached cursor and NULL-result behavior
  qualify. All 89 retail words execute across cases. Callback GP/FPR clobbers
  preserve the full saved-register set and paired F20/F21 lifetime. Scale
  bits, including zeros/infinities/NaNs/denormals, transfer without arithmetic;
  no hardware/FCSR or portable payload guarantee is inferred.
- 24 private-alias cases / 72 runs pass: outgoing descriptor/count, record
  and saved-RA byte aliases. Fire 1,144 strict access-fault triples / 3,432
  failed runs; compare memory/events/calls/FPR prefixes. All three positive-
  count NULL-record probes fail at read +3 with matching prefixes. Zero count
  permits NULL actor/records. Synthetic private aliases/faults are guest
  instruction probes, not portable C faults.
- Nine independent retail/raw/fitted links at three entry/table/callback
  rebases pass 324 cases / 972 runs, including signed LO carries and both JAL
  targets. Extreme wrapping indices are synthetic guest-only probes.
- Complete copied-owner compile/post-process/actual padding has zero
  diagnostics and exact pools. Constructor guard rows match the standalone
  profile. All 29 unaffected neighbors remain exact; the explicit typed stub
  is the only second change. Connect the actual new seven-word stub and
  unchanged three-word other stub in 432 cases / 1,296 runs, including all
  scale bit patterns and exact incoming-home writes. Both remain placeholders.
- Nine effective newly compiled IDO negatives reject wrong stride/type gate,
  narrowed mode, zero scale, first-result return, cached count, reloaded
  records pointer, signed record byte and signed count. Three native stride/
  type/mode negatives also fail.
- Native32 complete C at O2/O0 passes 262,400 cases per profile / 524,800 runs.
  Cover every type/parameter-byte pair, all count bytes, valid synthetic
  descriptor indices, typed nine/thirteen-argument packets, live count/cursor,
  full-word mode, last result and exact float bits. Actor, complete record/
  alternate arrays and selected descriptor changes compare.
- Actual 60-word record caller, 30-word request, 24-word definition lookup,
  19-word list and 11-word classifier connect to each complete constructor
  form in 324 cases / 972 runs. Fire 276 connected fault triples / 828 failed
  runs with full FPR prefixes. Deeper callbacks are bounded models in this
  matrix, not their retail bodies or natural gameplay.
- Eight actual descriptors (IDs 5,6,7,10,11,0x17,0x23,0x44) and every referenced
  record byte compare to checksum-verified retail ROM data. Pass 384 cases /
  1,152 runs using those real bytes. This qualifies these input samples only;
  all deeper callbacks and hardware/gameplay remain separate gates.

The first native O0 fixture failed ninth-argument bits 0x7F812345 -> 0x7FC12345:
its float-returning input helper used x87 and quieted a signaling NaN before
the constructor received it. Confirm with a three-word failure receipt, then
form the input directly in a local union and rerun both profiles without
dropping nonfinite tests. Initial object comparisons also incorrectly used
absolute ROM relocation values in an unlinked object; compare the checked
unlinked recipe and separately verify all relocations.

## Linked Audit And Banking

All nine final post-install tests pass in 72.629 seconds. Both tools checks,
exact mirrors and all six Python parses pass. Manifest dependency changes
trigger a wider successful guest rebuild, retaining the duplicate
generated_12D630 recipe warning and legacy pointer/type warnings in unchanged sources.
Copied-owner production compile has zero diagnostics. No build/profile changes.

Complete linked audit permits exactly the two explicit slots/extents, 384
scoped instruction bytes and 288 changed ELF bytes; everything else is byte-
identical. ELF 3,261,160 bytes, SHA-256
5cbb958e352c5f4166a314ad84aa52dc04ffdfadcef7b9fcefb6d5fdfa78beb8.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Protected rodata, tracked symbols and ignored undefined assignments are exact.
CSV remains 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Installed source 6,536 bytes, SHA-256
4d49232acdb3783174e197b3f9764f2b3ac35b60887706648ff08864c86a50e2.

The guard manifest has 298 historical CRLF lines; the generated publisher
retains its entire old byte prefix and appends only 17 validated rows. Reject
stale/duplicate publication; a targeted publisher test passes. Do not normalize
unrelated historical metadata. Current working-file SHA-256
4c8e876d3c4a21872de7e93af11545c4eb603ff7c11c0fb281bf154213fc6e71.
Git's existing LF checkout warning remains; no line-ending policy change.

Fresh matching: Game 2,772/4,821 (57.50%), total 3,445/5,494 (62.70%), zero
drift / 2,049 different. Delta +1 matching credit / -1 different. Converted
counts and bytes are unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). Both restored source and typed stub were
already C placeholders, so do not invent extra conversion credit.

```sh
python3 -m unittest tools.tests.test_game_actor_animation_constructor_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Bank tools 975e23b before consumer source/guards/docs/tools pin, no push.
Root README gets aggregate rows only. Earlier neighbor-suite receipts are
historical, not fresh tests; the full audit proves all their other linked
bodies remain unchanged. Native Graphify update after final code edits refuses
unsafe shrink 39,544 -> 17,770 nodes, retaining 19,398 nodes from 2,972
excluded-but-existing files. Preserve exit 1, skill 0.9.20/package 0.9.26 and
devcontainer.json zero-node warnings, no force/purge/install. The separate
consumer commit hook requires fresh log growth/completion and zero workers
before reporting clean. Nine added relative links pass, zero broken.

## Next And Boundaries

Next: full func_15030AF4 in conker/src/game/generated_5D2C0.c, still a false
zero-return C placeholder. VA 0x15030AF4..0x15030D54, ROM 0x5DFA4..0x5E204,
152 words / 608 bytes, original 0x30 frame. All eight sampled real descriptors
use its nonzero-type path, so restore the complete thirteen-argument helper
and then qualify the actual constructor connection. Recover actor-state/
flag branches, saved argument homes, table-backed allocation and NULL/return
paths without selecting only the easy branch. The full 182-word type-0
func_15083AC8 remains open too (original 0x38 frame); a typed empty stub does
not restore it. No goal-completion, hardware/gameplay or billing claim.
