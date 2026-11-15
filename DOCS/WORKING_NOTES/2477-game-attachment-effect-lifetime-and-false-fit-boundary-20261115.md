# Note 2477: Attachment-effect lifetime and false-fit boundary

Date: 2026-11-15. Consumer baseline `1644776eb567294b135cba3de4ba9cea644c19b1`,
tools baseline `66547a36b1fbdf2e7d90f9541fb6234b89053b1b`.
Continues [Note 2476](2476-game-vertex-transform-clip-custom-register-restoration-20261115.md)
and reuses [Note 2400](2400-game-attachment-effect-private-screen-20261113.md).

`func_150F97EC` remains a **production zero-return placeholder**. This phase
recovers the floating-result lifetime and qualifies the public behavior of
typed private candidates, while rejecting a misleading dimensional fit.
**Nothing is installed, no guards or profiles change, and C match credit is
zero.** All **866 frozen production inputs**, including all 698 objects, stay
byte-identical. Actual recount and the root README remain unchanged.

## Complete source boundary

Owner `conker/src/game/generated_124920.c`; VA `0x150F97EC..0x150F9950`, ROM
`0x126C9C..0x126E00`, **89 words / 356 bytes / frame 0x70**. The actor is
nonnull; its attachment pointer at +0x1D4 gates all calls. The routine passes
two pointer homes and the byte-selected matrix to `func_15145EA4`, then calls
float RNG, float RNG, integer RNG, integer RNG, float RNG, followed by the
14-argument `func_15102B38`. The selected slot byte must reload after helpers.

The private implementation uses a real **12-byte transformed vector** and
an **eight-byte spread pair**, with proper pointer-to-pointer transform
arguments. The alternate source's undersized `void *sp64` is not imported.
The factory's retained assembly independently confirms its pointer return,
halfword/byte argument reads and two-word spread copy. The corrected local
prototype preserves the full integer RNG results before unsigned modulo.
Names in these experimental records are descriptive, not recovered debug names.

The initial isolated O1 source emitted **92 words / frame 0x70**, with an extra
F20 lifetime: SDC1 at +0x14, MOV.S F20,F0 at +0xD0, LDC1 at +0x160.
Computing the final floating coefficient in a separate statement eliminates
those three instructions but adds a named coefficient spill. Current pinned
forms are:

| Private form | Words | Frame | Screen distance | Status |
| --- | ---: | ---: | ---: | --- |
| Conditional eight-byte pair | 90 | 0x68 | 63 | Faithful typed storage; wrong extent/frame |
| Conditional triple spread | 90 | 0x70 | 57 | Third unused field is only a layout hypothesis |
| Early pointer initialization + triple | 89 | 0x70 | 74 | Rejected by the null-path private-memory gate |

Screen distance means same-position mismatches plus excess/missing words; it
is not an exact-C counter. Every source body and all relocation bindings are
pinned in `game_attachment_effect_150f97ec_lifetime_manifest.json`.
All three O1 forms retain the actual literal multiply by 1.0f. The multiplier
check tracks constant operands: a matching MUL opcode with F4 holding 14.0f
does not establish this operation. Explicit one-versus-fourteen controls
correct the earlier exploratory opcode-only label in `strict-screen.json`.

The complete O2 owner replacement preserves all **16 non-target functions**,
normalized pools and diagnostics. This validates the owner boundary, not an
O1 production profile. O1 compilation is isolated; the generic GLOBAL_ASM
preprocessor must not size O1 holes using O2 assumptions.

## Why the 89-word form is rejected

The apparent fit stores its input and destination pointers before reading the
attachment. On the null path it changes **eight bytes** in the homes at
retail SP+0x50/SP+0x54. Retail leaves those bytes untouched. The conditional
90-word/frame0x70 hypothesis agrees with retail's null-path memory instead.

Both streams are stopped immediately before their actual attachment read at
actor+0x1D4. The fired cuts are **5 retail accesses** at PC `0x150F980C` and
**7 early-fit accesses** at PC `0x150F9818`. Both dispatched words are real
LW instructions with offset 0x1D4; their private memory still differs. This
is an observed rejection, not a synthetic fault or a word-count heuristic.

For the conditional 90-word/frame0x70 form, the extra SWC1 at +0x11C writes
the coefficient at SP+0x44; the two integer capture homes move to SP+0x48 and
SP+0x4C. Retail uses SP+0x44/SP+0x48 for those integers and has no coefficient
spill. Recover the expression lifetime and complete layout; do not remove
that store, add broad expected-word guards or declare the frame sufficient.

## Fresh behavior, caller and padder checks

The reused historical helper model is imported by its three definitions only,
with a pinned source hash. Its old top-level artifact reads, loops and receipts
do not execute. The extension models the transform advancing both cursor
variables as well as filling the point. Transform, RNG and factory helpers
remain bounded models; the actual helper bodies are not connected here.

- **960 finite cases per stream / four streams** compare retail and all three
  private forms. Every word is visited: 89 / 90 / 90 / 89. Cases include both
  attachment states, slots 0/5/255, byte truncation of full-width selectors,
  callback slot changes, multiple memory seeds, integer extrema and context
  values. Defined packets, ordered calls, public memory and preserved ABI
  state agree. Three effective instruction controls reject spread, modulus
  and coefficient changes.
- **51 cases per stream** execute the original five-word caller window
  `0x1502890C..0x15028920`, including its branch to 0x15029BA4 and V0=1
  delay slot. Three return-poison controls are overwritten there. The known
  caller ignores this function's return. The earlier one-JAL/no-literal-pointer
  census is reused on the unchanged complete ROM; computed/external calls
  remain outside that census and full parent execution is uncredited.
- The typed pair C body passes **960 native32 cases each at O0/O2/O3** with
  UBSan, plus **five effective source controls per profile**. Native helpers
  model the same cursor, slot, random-order and factory contract. Native
  selector inputs are canonically narrowed to a byte; guest tests additionally
  exercise full incoming register bits. Native checks do not cover the other
  two layout hypotheses or exceptional FP/FCSR behavior.
- The strict generated padder rejects both 90-word overrides: 0x168 bytes
  exceed the 0x164-byte retail span. `pad_c_object` intentionally accepts them
  using a relocated trampoline and a **360-byte .game_overflow** body. Tests
  verify that output explicitly; it is not a match. Both padders accept the
  dimensional 89-word form and preserve 16 production neighbors, yet its
  body differs from retail and the private-memory test rejects it. Raw owners
  have no data section; padded objects have the same empty `.data` section
  as production. No data contents are excluded to make that comparison pass.

The focused suite is:

```sh
python3 -m unittest tools.tests.test_game_attachment_effect_150f97ec_lifetime -v
```

Fresh complete receipts: **161.195 s mounted**, **198.9 s sibling**.
`make tools-check` passes. An initial test incorrectly expected the C padder to
reject overflow and compared an absent raw `.data` section with a present
empty padded section. The fixture now checks each API's actual behavior and
compares objects at the same stage. Its first failure is archived separately.
No shared padder implementation or acceptance gate was weakened.

## Profile controls and advisory disposition

Controlled expression, declaration and debug-profile probes are retained in
the ignored build directory. Reversing floating expression trees keeps the
F20 lifetime; a register coefficient also retains it. Scoped pointer or
coefficient initializers do not recover the complete fit. Local driver string
inspection exposed `-strictIEEE`, but actual O2 bodies are unchanged by that
flag. Olimit 0/1 instead emit **97 words / frame 0x78**, with explicit optimizer
threshold warnings. None is a selected production configuration. `-show`
triggers an existing unsupported timing fprintf format in the prepared wrapper;
the compiler was not patched or replaced, and that diagnostic is not a valid
compiler timing/provenance trace.

One focused Claude review was attempted under the workflow's difficult-
lifetime allowance through freshly verified claude.ai/firstParty Pro auth.
Safe mode, empty tools, strict empty MCP and no persistence were requested.
The process returned output, but the Windows capture failed on a Unicode arrow
before init/result verification. No recoverable response was retained and
**no advisory was used**. The capture script is corrected to explicit UTF-8;
it was not rerun. **One invocation is consumed, zero verified reviews**, so
do not repeat it on resume. Packet SHA-256:
`823533e6c17f166d92f038eaafded39fdf739c1bf49bf8475cdf2cf31ed6337a`.
The private plan, empty stream and failure record retain that distinction.

## Preservation and resume point

All **866 production inputs** and all **698 objects** remain identical to
the recorded baseline. ELF SHA-256 remains
`f9648bd31a9604b17b2753451395c9b9f7e54e01392ade3683ad55a4ca512349`.
The preceding strict/protected-data audit remains applicable by complete image
identity; no new production Make or image adoption is claimed. Fresh recount:
**4,507 / 5,514 total exact C (81.74%)**, Game **3,834 / 4,841 (79.20%)**,
Init **492 / 492**, Debugger **181 / 181**, zero drift and **1,007 different**.
The root README is verified and unchanged. **180 further C matches** reach
85% at this denominator; that goal remains active.

Tools commit `5c1750ac08d9ce07c1e0f81b632997e0410c6fbc` precedes the consumer notes/tools-pin commit.
The six-file ignored overlay preserves sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434 dirty paths**, and status
SHA-256 `a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped extraction covers five Python files and retains all **62,039 old IDs**;
snapshot **62,072 nodes / 116,276 links**, no lost nodes, not full-corpus
extraction. Post-commit heading aliases retain old document IDs. Five DOCS
indexes receive one concise entry; no function narrative enters the root README.
The host-port path contains only scratch directories, with no Git/CMake
checkout; no host build/adoption applies and Release remains untouched.
Nothing is pushed.

Resume from this note and Note 2400 together, not from a fresh generic profile
screen. Evidence is in `conker/build/game-actor-joint-effect-150f97ec-private/`.
The next discriminating source/compiler work is the **named coefficient spill
and conditional pointer-home schedule**. Keep the pair's real eight-byte
storage and transformed vector's twelve bytes; the third spread field is an
unproven hypothesis. Require emitted-word/binding, complete ABI/caller,
guest/native, private/fault/FP, both-padder, actual-Make, strict full-image and
production/recount gates before installing or crediting any replacement.
