# Game Table-Driven Effect Constructor Restoration

Date: 2026-10-09

## Result

Continue [Note 1148](1148-game-random-effect-timer-restoration-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and zero
Claude calls. Replace the false-zero `func_151DA6F8` with its complete semantic
constructor in [game_2062D0.c](../../conker/src/game_2062D0.c):
VA 0x151DA6F8..0x151DA938, ROM 0x207BA8..0x207DE8,
**144 words / 576 bytes / frame 0xD0**. The linked target improves from
**143 to 61 differing words**. It is **still non-matching**, with no new
guards, normalizer, artificial tail, insertion, omission or filler.

Start from clean parent a1f0e279 and mounted tools 061d223. The old source's
normalized-text SHA-256 is
`d7653f8209f880cb8cfc2ed636b93535a01c4fe0f8e489c47c5849e5ec440396`;
the baseline ELF is the exact Note 1148 artifact. The fresh whole-ELF audit
allows only this target's 576-byte slot and its own symbol-size field
**12 -> 576** to change. All 6,058 slot addresses/extents, all other function
bodies and every other ELF byte stay unchanged. Protected data, progress CSV
bytes and all 11,475 guards remain unchanged. New ELF SHA-256:
`a0ed058388ea573771373ec23cb71ea656e2b4d5a889b96682a7921911f56093`.

The placeholder already counted as C and the semantic body is not yet exact:
**no converted-function, converted-byte or exact-match credit**. Fresh totals
remain 5,484 converted / 3,397 exact; Game 4,811 / 2,724; Init 492 / 492 and
Debugger 181 / 181 exact; zero drift and 2,087 different. Root README's
aggregate rows remain correct and are untouched. No function narrative goes
there. The wider Game goal stays active.

## Recovered Contract

Recover all **18 mixed O32 arguments**: position pointer, velocity pointer,
float scale, signed-halfword duration, byte mode, float time, full-word
request selector, byte opaque flag, two float payload values, byte fade flag,
unsigned-byte table selector, full-word extra bytes, two signed halfwords,
full-word request value, byte channel and full-word context. The original
request selector is loaded as a word before its low byte is stored, not as an
incoming byte argument. Preserve float transport bits; do not introduce float
arithmetic or invent null guards for the position/velocity inputs.

Build four local records with the consumed fields and explicit untouched
padding:

- Request: **28 bytes**, position XYZ, duration+16 narrowed to a halfword,
  kind 53, active word 1, signed sentinel -1, selector low byte, two untouched
  bytes and request value. The signed sentinel recovers retail's `li -1`.
- Descriptor: **32 bytes**, time, velocity XYZ, scale, live D_800AB498,
  flags, D_800AB3F4[selector], alpha 255, mode and both halfwords. Flags are
  0x48 plus 0x20 when D_800AB404[selector] is nonzero and 0x80 when
  D_800AB330[selector] is nonzero. Opaque adds 3 and sets call flags 7/4;
  otherwise those call flags are zero.
- Payload: **12 bytes**, two transported floats, selector and three untouched
  bytes. These bytes are copied as object representation, not zero-filled.
- Render prefix: **32 bytes**, words 0, 0x220005, 0x50600, 3, 70, 128, 32,
  bytes 0/12 and two untouched bytes. The callee consumes exactly 32 bytes;
  there is no evidence authorizing an extra 16-byte struct tail.

Call `func_15147DA0` with all **15 argument words**: request, descriptor,
16, 1, 0, 0, opaque flags 7/4 or 0/0, 0, fade flag 2 or 0, fade alpha
255 or 0, render prefix, extra bytes, channel, context. On nonnull return,
copy all 12 payload bytes to `*(created+0x98)+0x48`, then return the original
created pointer, ignoring memcpy's destination return. A null result performs
no payload lookup or copy. Preserve the pointer across call-clobbered registers
and outgoing argument-home writes.

Record and field labels are descriptive recovery names, not proof of original
declarations or gameplay meaning. "Trail" in the tool filenames is a working
label. The retail tables each contain 16 entries: tests use those valid
indices, not an invented 256-entry retail domain. Halfword narrowing follows
the prepared IDO/GCC target implementations, not a portable trap claim.

## Fitting And Remaining Differences

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_trail_effect_constructor_candidates.py)
provides **101 complete ordinary forms**: initial flag/layout choices,
narrowing and explicit-else alternatives, flag-use forms, local declaration
permutations and three cleaned complete forms. No truncated-call prefix or
fixed-return body is used for fitting. The original straightforward form
emits 137 words/frame0xD8/139 differences. Split contributions improve to
140 words/frame0xD0/99; explicit-else experiments reach 144/0xD0/80.
Signed sentinel plus conditional contributions and descriptor-flag use reach
144/0xD0/64. The selected cleaned form uses the flags variable meaningfully
and reaches **144/0xD0/61**, no isolated compiler diagnostics or pools.

Remaining measured differences include register allocation, independent
schedule, render-prefix base **SP+0x64 versus retail SP+0x54**, and the
returned-pointer/branch-delay arrangement. Both complete forms preserve the
request at SP+0xB0, descriptor +0x90, payload +0x84, pointer save +0xCC and
RA +0x44. Render padding consequently comes from different private addresses;
do not call its unspecified values equal or force them to zero. A 48-byte
render experiment moves its base, but its extra tail is only a fitting
hypothesis and is **not installed**. No broad retail-word replacement.

## Qualification

The [eight-test suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_trail_effect_constructor_recovery.py)
reuses the existing Shaping/Triangle instruction oracles, native32 harness,
owner compiler, ELF/object/pool parsers and actual padder. No new emulator.
Independent packed-record expectations cover all defined bytes and complete
arguments rather than treating pairwise compiler agreement as semantics.

- **1,330 cases / 2,660 executions** compare complete selected/retail records,
  mixed argument widths, public access order, success/failure, original pointer
  return, 16 valid indices, both flag tables, float transport including NaN
  bit patterns and both SP phases. All 144 selected words execute. Saved
  GP/FP and float registers survive; private scalar scheduling is not claimed
  identical.
- **32 alias/home-clobber cases** cover common position/velocity pointers,
  created/payload input aliases and input mutation after construction. All
  15 outgoing homes can be overwritten without losing the result or records.
  **156 real missing-public-byte pairs** compare emitted fault prefixes;
  these are not portable invalid-C behavior or actual hardware traps.
- **65,536 actual native32 C cases** exhaust the duration halfword patterns,
  vary valid indices, table/opaque/fade flags, eight finite float patterns and
  allocation failure. Check all four type sizes, complete helper argument
  contract, output transport, preserved return and two 512-byte canary
  regions. Allocator/copy helpers are bounded native fixtures; physical FCSR
  exceptions and rounding modes remain unvalidated.
- **128 connected cases / 256 executions** connect the complete **original
  retail 70-word func_15147DA0** and the exact linked **11-word memcpy**.
  All 81 connected words execute. The callee calls func_15147A80 with eleven
  arguments, copies the descriptor, writes six flag bytes and copies eight
  render words inline; then the target copies its trailing payload. Qualify
  null/success and defined output bytes, excluding the two unspecified render
  padding bytes. The allocation core is bounded; the installed callee's
  existing C placeholder is not upgraded by this work. No complete caller,
  hardware or gameplay acceptance claim.
- Three complete ordinary controls pass; **four effective compiled negatives**
  alter duration bias, request selector, fade alpha or pointer return. Each
  compiled stream first executes to completion, then fails the independent
  behavior comparison; an oracle execution failure cannot qualify a negative.
- Preserve **61 copied-owner neighbors**, pools, relative relocations and
  six existing diagnostics. Actual pad_c_object emits the full 576-byte body
  without `.space` or target guards. **Four independent GNU links / 64 cases**
  cover HI/LO carry and J26 regions; their actual-owner baseline stream equals
  the isolated candidate. No separately rebased original-assembly claim.

Final pre-install eight-test run passes in **19.466s**; final post-install run
passes in **51.971s**, no skips. Fresh **25 shared padder/linker tests pass in
0.313s**, and both local tools checks pass. Preserve the duplicate
generated_12D630 recipe warning and six unchanged owner diagnostics; this is
not a warning-free production build. Prior unchanged neighbor suites remain
historical receipts, not fresh blanket reruns. Sixteen tool files parse and
match the older mirror exactly. Scoped link validation checks **135 documents /
4,159 relative links / zero broken** before the parent commit.

## Receipts And Banking

Ignored receipts: `conker/build/game-trail-effect-constructor-test/` contains
baseline.json, before.elf, before manifests/progress, slot.json, guest.json,
faults.json, forms.json, callee.json, native.json, owner.json, linked.json and
after.json. Candidate sources/objects/screens stay in the separate ignored
`game-trail-effect-constructor/` directory. Do not commit ROMs, artifacts,
progress CSV, private state or generated temporary sources.

Per "Keep commited", commit mounted tools
**77001d3fb4250e849deb42af7911e51b2496d205** first, then exact parent
source/docs/gitlink. Mirror only the two absent new files, verifying exact
bytes. Preserve older standalone HEAD ddbdd16, its independently modified
owner-pool/effect-test fingerprints, unrelated untracked files and history.
No push, pause, reset or duplicate standalone commits.

Manual Graphify refresh refuses 16,920 nodes over retained 38,709 and
preserves 19,398 nodes from 2,972 excluded files still on disk. Keep its graph;
do not force overwrite or change dependency/account settings. No OGL/Release,
runtime/save/editor or bridge work. Wider Game and graph/hardware gates remain
open.

## Next Work

Follow-up [Note 1150](1150-game-effect-record-constructor-match-20261009.md)
restores the complete 70-word `func_15147DA0` callee directly from C without
guards. Its active/fade parameters are full incoming words, narrowed only at
the six byte stores where applicable; the caller prototype is corrected
without changing any of its instructions. Seventy-three additional caller
forms remain uninstalled. This constructor still has 61 differences; the
allocation core and complete upstream callers remain separate work.

Continue **this constructor's matching**, starting from the complete selected
144-word/frame0xD0 body and **61 real differences**, not its removed zero
placeholder. First resolve the render-prefix local placement without inventing
a tail or padding bytes; then separate flag register allocation/independent
schedule from the return-pointer branch-delay schedule. Reuse the banked
records/native/connected/owner/ELF tests. Add no exact-match credit until the
actual linked target is exact. The allocation core and linked callee recovery,
complete direct callers and hardware/gameplay qualification remain separate.
