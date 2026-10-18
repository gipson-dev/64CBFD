# Object Command Enqueue Recovery

Date: 2026-10-18. Consumer predecessor **83a79f07**. Tools checkpoint
**6bebb52** is committed first. Target `func_1512D560`, owner
`generated_15AA10`, VA **1512D560..1512D604**, ROM **15AA10..15AAB4**:
**41 words /164 bytes /no frame**. Installed and byte-exact after the
qualification, first prediction and real linked-image gate below.

## Recovered C

Replace the zero-return placeholder with
`void func_1512D560(u8 *object, s32 command, void *payload)`. Retain the address
symbol and describe the behavior in its source comment. The third argument is
stored as a 32-bit payload value, never dereferenced. The projection parent
passes command5/null and command7/packet; other original calls also pass small
integer payload values. This is not a new globally renamed SDK interface.

The object byte at23D selects a B0-byte command queue through D_800DC2B0.
Each operation reloads the object bank and table pointer. Write the command,
reload and write the payload, reload and increment the unsigned cursor atAC,
then reload and clear only when the resulting cursor equals20. Do not cache
the row/cursor, clamp invalid cursors or replace equality with >=. A payload
write can alias the cursor; either queue write can change the bank/table.
Unsigned increment preserves the full 32-bit wrapping instruction behavior.

Normal O2/g3 emits the complete41-word body. Five source forms (ordinary,
signed-counter screen, explicit table source, index-first and integer-address)
emit identical raw instructions/bindings. The selected ordinary unsigned C
does not claim signed-overflow behavior or require a compiler/profile change.

## Closed Normalization

Raw SHA-256:
`ccab39cd1f02cba8c92321870c51d236e02df4408a89db98500eef8e7d4d85e0`.
Exactly two bindings: HI16 at0, LO16 at4, both D_800DC2B0.

Thirty expected-word guards normalize register lifetimes and four commutative
queue-address sums. No padding, insertion, omission, branch change, new data
or frame adjustment. The unchanged words and branch delay/return boundaries
are independently checked, not filled from a retail-byte blob.

An independent symbolic execution of raw and ROM instructions compares both
complete paths as ordered byte-memory reads/writes, branch conditions, return
target and preserved ABI state. Every read includes preceding store history;
partial aliases are not assumed disjoint. Four unsigned multiply-low values
and their consumers remain congruent. The void interface does not promise
caller-saved dead GPR or HI/LO equality at intermediate fault boundaries.
Eight independent function/data rebases cover signed LO16 and HI16 carry.

The full owner padder matches all41 retail words and preserves three raw
neighbor bodies/bindings plus all pools. A complete trial link is byte-equal
to the independently predicted predecessor image with only164 target bytes
replaced and its symbol size updated12->164. The prediction changes119 ELF
bytes; it does not whitelist or discard unrelated sections/metadata.

## Qualification

`python3 -m unittest tools.tests.test_game_object_command_enqueue -v`:
the final installed **ten tests pass in31.274 seconds**, with no skips.
Earlier pre-install runs explicitly skipped only the installed-image gate.

- 352 paired complete guest memories and ordered access traces. All41 words
  visited; eight effective bank changes and eight table changes. Cover all
  byte-bank sign boundaries, cursor19/20/21, unsigned extremes, payload/cursor
  overlap and stack aliases. Forged/sparse guest addresses are not native C
  object, MMU or hardware acceptance claims.
- 244 paired, actually fired memory-fault prefixes preserve complete memory
  and access traces. Dead caller-saved register contents are not compared.
- Seven compiled C negative controls are effective; the cached-row form also
  fails a complete public-memory alias case. Signed-bank and wrong-stride
  controls can reach explicitly unmapped addresses; those are recorded as
  changed-access witnesses, not successful returns.
- Native32 O0, O2 and O2+UBSan each pass5120 cases: all256 banks and20 valid
  cursor positions, full data-region comparison, high payload bits passed but
  not dereferenced. A compiled early-wrap control exits23. No native64 claim;
  forged aliases and out-of-range cursors stay guest-only.
- 575 connected projection cases execute the actual retail parent and selector
  with both raw and normalized enqueue bodies; public memory and actual helper
  arguments agree. The production parent remains a stub. This is not full
  caller reconstruction or gameplay acceptance.
- Reject41 raw-word corruptions, two missing bindings,32 live/snapshot input
  changes,30 altered expected guard words and both relocation expectations.

The first harness run exposed missing sparse-address mappings and a signed
load missing from the borrowed oracle, both corrected locally. Native O2's
initial SIGSEGV was observed in owned GDB at080490B3, `_start+35`, on a
`movaps` stack store with ESP ending364. Reuse the existing `-mstackrealign`
freestanding-harness flag; do not attribute that setup fault to game C.
The later installed-stage detection Path/string error was fixed before
installation. All qualification producers were observed terminal; none was
restarted merely on timeout.

## Parent Expression Rejections

Continue Note1553's `func_150891E8` investigation without replacing its retained
321/frame120/221-difference model. Four discriminating no-unroll-owner screens:

| Source Form | Words | Frame | Different Words |
| --- | ---: | ---: | ---: |
| Typed node fields and addresses, fixed scan | 320 | 120 | 289 |
| Typed node fields and loop | 250 | 128 | 321 |
| Pointer-to-array address expressions | 320 | 120 | 290 |
| Unsigned shift address expressions | 320 | 120 | 288 |

Each preserves72 raw owner neighbors/pools;192 sampled public cases pass.
All fail extent and remain rejected. The typed fixed scan still places record
inS4 and table inS3; it does not solve the observed choice-order mismatch.
No physical color forcing, object promotion or broad parent guard append.

Artifacts are ignored under `conker/build/game-object-command-enqueue-match/`
and `conker/build/game-route-projection-node-expression-fit/`. The earlier
ignored enqueue probe and parent allocator captures remain unchanged.

## Installed Gate

The real `make -C conker -j4 build/conker.us.elf progress.csv` build completes.
The installed audit reproduces the exact first prediction: **119 changed ELF
bytes**, only target code and its12->164 size. All6057 function addresses are
preserved;6056 other bodies are unchanged. Every other ELF byte is fixed,
including all189088 protected Game-data bytes across720 owners. The actual
owner definitions/bindings equal the qualified padded owner; prior guard bytes
are an exact prefix with only the declared30 rows appended. No Makefile change.

Successor SHA-256 values:

- ELF: `6157cecd5d2927c718121fffe1e6aae986b0cc3b65b9ed29bd2d1aa03a375265`.
- Owner: `31ed15c56622255fc358fdcedf654450f8358ceed976a793d8939eb39324f458`.
- Guards: `d6a8f7c3b993d0449c712b15e083077017266394458b483d22e091f0c942e5fa`.

Fresh `make -C conker match-progress NON_MATCHING=1`: **Game2986/4828
(61.85%)**, **total3659/5501 (66.52%)**, Init492/492, Debugger181/181,
**1842 different /zero address drift**. This adds one exact Game function.
Conversion remains5501/6044 (86.04% bytes); Game4828/5323 (85.41% bytes).
The old placeholder was already counted as C, so no conversion-count increase
is claimed. README changes only its two aggregate byte-exact rows.

Commands require the prepared consumer and retained ignored before/after
receipts; they do not silently regenerate or bless a changed predecessor.

## Resume Boundary

Return to the parent's joint321-word extent,
120-byte frame, saved-role order and live homes. Typed-loop normal-profile
emission is an untested possible discriminator, not an accepted body/profile
change. Vector15088F30, other parent150896EC and wider Game matching remain
open. No Claude call is made for this routine qualification; the previous
allocator advisory is not repeated or treated as approval.

Preserve the standalone mirror HEADddbdd16 and all1235 previous dirty-file
hashes; only three absent task files are added (1238 dirty paths). Shared
padder/PC16 checks pass eleven per tools copy, both smoke checks and consumer
tools-check pass. No mirror commit/reset, push, host-port or frozen Release
build, launch, save or configuration action.

Scoped Graphify refresh:42609 nodes,82676 links,4017 communities. Preserve
42596 old IDs; three duplicate UPDATE_LOG headings are uniquely relocated,
not lost. Retain19398 nodes from2972 excluded-but-existing files. Tools stay
outside the configured graph corpus; no new Python AST graph coverage is
claimed. Before graph and scoped-ID audit remain ignored receipts, with no
full-scan purge or tracked graph artifacts.
