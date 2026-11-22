# 2634 - View light script guarded byte match

Date:2026-11-22. The total85% matching goal remains active.

`func_150ECC70` replaces the last zero-return placeholder in
`conker/src/game/generated_1199D0.c` with the complete script-driven view
color/range update. All **341 body words** match the retail output after
**28 expected-word/relocation guards** preserve one signed-clamp branch layout.
The **56-byte frame** and **344-word slot** include **three trailing zero
words**. There are no inserted or omitted instructions. This is a guarded
match; the raw compiler stream matches313/341 words.

Production is **4,616 / 5,528 (83.50%) total**, **3,943 / 4,855 (81.22%) Game**,
zero address drift and912 different. Init492/492 and Debugger181/181 remain
exact. **83 more matches** reach85%. Conversion rows are unchanged.
Original:`conker/asm/1199D0.s:520`, VA150ECC70..150ED1C4 body, slot through
150ED1D0; ROM11A120..11A674 body, slot through11A680.

## Recovered behavior and ABI

The callback accepts the actual SDK `struct108 *` view (size0x9A0).
Script selector403B controls the enabled path. Three zero-payload setters
4031..4033 precede the view-flags update. Palette selectors4038,4039,403A
have ordered priority and choose RGB128/255/255,255/128/255,255/255/128,
or255/255/255. The disabled path restores white, submits three clear commands,
reloads callback-mutated flags, clears0x80021200 and sets0x8.

The enabled path obtains a selector through a zero-payload query2007/keyB7
and ORs2000. Query4010's zero result clears view+134 and the float at+190,
then returns before smoothing/publication. The OR makes the following zero
selector branch unreachable under the valid callback ABI; it is retained.
On the normal path, view+134 becomes1. Query9C supplies setter9000/key17.
Query9A supplies a signed value: range clamps to[900,1190], while radius
clamps **half of the original value** to[180,231]. Setter9000/key8 has
two payload words and therefore five total arguments. View+190 becomes220f.

Three smoothers use current RGB at80088AD0..AD8, target RGB at80088ADC..AE4,
velocity at80088AE8..AF0, strength4f, damping6f and a fresh view+7B4 timestep
at every call. Three setters30F3..30F5 publish the truncated unsigned color
low byte. Retail FCSR save, conversion fallbacks and restoration are retained.
Invalid/NaN/infinite/out-of-range casts are qualified in guest execution only.

## Guard boundary and complete signed-domain proof

Raw SHA256:`bcf8616cb989dba7034e1a3453608f2b6e82c34093fec84c49cb8f28e24959eb`.
All28 differences lie in words121..150. Every surrounding word, including
stack frame, local spill, saved-register lifetime, calls, conversions and
return path, already matches. The alternate clamp branches distribute output
setup differently. The normalization is **closed CFG equivalence**, not a
scheduling-only claim.

An independent exact interval interpreter executes the actual raw and retail
blocks over all2^32 signed input words. SLTI takes the exact preimage of each
threshold, including arithmetic right shift. Both partitions are:

| Signed input | Range | Radius |
| --- | --- | --- |
| INT_MIN..359 |900|180|
|360..463|900|value>>1|
|464..899|900|231|
|900..1190|value|231|
|1191..INT_MAX|1190|231|

The proof checks all five outgoing arguments, ordered outgoing-payload and
view-distance stores, common continuation state, preserved view/stack pointers
and untouched FCSR. Callback volatile registers are clobbered. Five effective
instruction controls reject incorrect bounds and shift count. Raw PCs,
internal call return addresses and caller-volatile temporaries are different;
instruction timing equivalence is not claimed.

Guard rows append to the exact old CSV bytes. Existing randomized-emitter
guards, its24-byte literal pool and D800A1578 Make binding remain unchanged.
All six other owner functions, constant pools and diagnostics match their
frozen baseline. Both padders agree; eight independent GNU links across four
rebases cover HI16 carry boundaries and the unchanged12-byte padding.

## Semantic and integration checks

- Guest664 cases per raw/original stream cover palette priority, enabled/
  disabled branches, early return, signed clamp boundaries, zero/one/two
  payload counts, fresh values after callback mutations, all four rounding
  modes, FCSR restore and unsigned-conversion fallbacks.338/341 words execute;
  three redundant MFC1 instructions are unreachable in these compiler CFGs.
-158 access-fault pairs in six discriminating cases compare complete memory,
  ordered access trace, calls/snapshots, saved registers and FCSR. Entry RA
  restoration is separately checked on completion; internal RA is excluded.
- SDK32 O0/O2/O3 each pass376 cases with the real view layout, complete view
  canaries, strict aliasing, UBSan and float-cast overflow sanitizer. Native
  colors are finite and in[0,2^32); invalid conversions remain guest-only.
  Nine effective source controls reject incorrect bounds, half of the
  clamped value, early-reset field, payload count, palette, flags, timestep
  field and publication width. Native patterned scalar fields are initialized
  as words to respect the guest/host endianness boundary.
- The original/current complete17-word scene dispatcher15130230 and its
  12-byte padding pass80 cases per stream. All36 callback-prefix entries
  match retail; entry17 at800896B4 selects this routine, preserves incoming
  A0 and ignores its result. The zero-scene gate and missing-view control pass.
- Connected960 cases per stream execute the exact current/original query
  and submit wrappers (92 words each) and smoother (54 words,52 exercised).
 36 standalone wrapper cases cover payload counts0..8 and count restoration.
  Five original/current table entries are verified: query type1→15099C14,
  type3→150A04D8; submit type2→1509E900,type3→150A03B0,type8→15096D78.
  Selected script-leaf semantics remain contracted; smoothing has an
  independent scalar IEEE model. This is not gameplay or hardware acceptance.

## Full image, adoption and tooling

The natural existing O2/g3 Make recipe emits the proposed owner through three
commands without a membership/profile override. The complete production ELF
equals the independent prediction: **1142 changed bytes, zero exclusions**.
Four explicitly fingerprinted adjacent GNU metadata permutations cover eight
symbol records and their strings; no loaded-code exceptions are allowed.
Protected189088 GameData bytes /720 owners and all conversion rows remain
unchanged. ELF SHA256:`647359b843a9c27a9bf110dad35f80b49f4a248962b70dfe622b41c112dd0cbe`.

Both tools configurations freshly pass all seven checks before and after
adoption with paired Python/data fingerprints. Shared tools-check passes.
The real sibling tools repository's pre-existing edits and dependency hashes
are preserved. Existing duplicate generated_12D630 Make warnings remain.
Baseline consumer:`a8e4855b41f78219679bdc9b24ff4f1ac6f14670`; tools:`23d455b17a69f729a41adc0010a1e91d7eaf4cd4`.
Tools commit:`bb0316930e9faa8d639d4ca83e7461c44ffb3de3` precedes the
consumer source/guard/docs commit. No push. Available host applicability is
recorded separately; no host build or Release changes. Zero Claude calls.
Finish graph retention and immutable banking before the next recovery.

Graph maintenance: the native update exited 1 with all
70,971 prior IDs retained. The subsequent serial scoped extraction
covers 9 C/Python files with no missing AST sources, producing
71,040 nodes / 169,082 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
