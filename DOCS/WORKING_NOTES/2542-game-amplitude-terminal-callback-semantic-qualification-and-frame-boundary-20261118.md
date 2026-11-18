# Amplitude terminal callback semantic qualification and frame boundary - 2026-11-18

`func_150B89E0` has a complete **uninstalled 345-word C recovery**, matching
the original 345-word / 1380-byte length. Its raw frame is **0x198 / 408 bytes**
against retail **0x190 / 400 bytes**. Fresh paired five-test suites qualify
the complete modeled semantics, native C and both caller interfaces. This
does **not** establish a byte match: private-state/ordered-FP proof, guarded
normalization, padders, actual Make and whole-image adoption gates remain open.
No source is installed and **no exact-match credit is added**.

Production is byte-identical to the accepted ELF
`9ea62e989d0b63ca64d3c5b92c9c278f85622a4a6907780f7646240767cb1893`.
Fresh recount remains **4,548 / 5,514 (82.48%)** total, **3,875 / 4,841
(80.05%)** Game, Init 492/492 and Debugger 181/181, zero drift and 966 still
different. **139 additional matches** reach 85%. Root README stays unchanged
because its aggregate rows already report these measurements.

Baseline consumer `44c7e456b4def6ec5416e61cde6def9c51969966`, tools
`89aa55df95590b181227768093587dc886f470ad`; all **1,730 frozen inputs** remain
unchanged. The `game_amplitude_terminal_150b89e0` tools stem retains the C body,
declarations, native template and five checks. Ignored
`conker/build/game-next-150b89e0-private/` retains the compiler spelling/lifetime
experiments, measured stack projection, original assembly, immutable snapshot,
paired reports, native fixture and this continuation packet.

## Recovered behavior and interfaces

The callback is `s32 func_150B89E0(u8 *actor, f32 x, f32 unusedY, f32 z,
f32 y, void *context)`. Its actual table entry is **D_80089934[1]**, address
0x80089938 / ROM 0x22E3F8. Both genuine dispatchers supply the old X/Y/Z values,
a queried height as argument4, and the actor's embedded context at +0x114.
The old Y argument is unused; it must remain in the six-argument interface.

The routine always stores actor+0x3C = actor+0x10 + argument4, then selects:

- Amplitude at actor+0x140 <=15, including unordered comparison: set bytes
  +0x72/+0x78, clear the low flags byte, build a float matrix, transform the
  actor position with the 200-unit argument, add its current motion and return1.
- Amplitude >15 through30: scale six motion components by actor+0x14, negate
  the second component before multiplication, play the selected fixed sound
  using truncated coordinates, and return1.
- Amplitude >30: build the 88-byte burst descriptor; capture the randomized
  extra float and actor+0x128; sequence the next three RNG values; submit the
  17-argument factory; conditionally copy **eight bytes** to result+0x128;
  build the 136-byte spray descriptor with late caller/actor/global loads;
  submit it; select/play the random sound; return0 even when allocation fails.

The eight-byte extra object intentionally has four untouched bytes. The C
uses an explicit retained byte array, without inventing a zero initializer.
Guest tests compare all eight bytes; native tests observe only the initialized
four. Factory and audio argument widths follow measured o32 word traffic;
the audio call-site declaration records that its callee narrows full words.
No shared headers, existing owner types or compiler profiles are changed.

## Source recovery and measured matching boundary

All seven owner neighbors and normalized compiler pools remain unchanged.
Raw compiler hash:
`d01ce723d9fbbe8f5d68c5bc8556cc5e92ff27d70897bed09c929ca1b2faed37`.
The selected body has100 bound-word differences. Its descriptors/matrix keep
their retail incoming-SP-relative addresses; the frame and saved-register
area remain different, and the first RNG spill moves by eight bytes.

A bounded ordinary-C spelling screen showed that `spray.field18 = 0` avoids
the initial draft's saved F20 zero spanning unrelated calls. Integer0 and
double0 produce the same emitted result; float0.0f retains the saved register.
Removing short-lived scalar carriers reduces the frame from424 to408 without
dummy padding, aliases or a profile override. All three branches remain in C.

`frame_diagnostic` is an explicitly **unproved projection**, not an installable
normalizer. After adjusting the measured frame/SP homes it leaves25 differences:

- Words143/144: independent literal-address setup versus incoming X load.
- Words169..190: five private descriptor stores move ahead of the remaining
  stores. The measured source order is [190,186,187,188,189,169..185].
- Word266: the fifth middle-path multiply swaps its two FP operands. Raw is
  0x460A0402; retail is0x46005402. Finite native agreement does not prove an
  arbitrary NaN payload/FCSR relation. Resolve or explicitly qualify this
  boundary before deriving any production guards.

The extra eight-byte raw frame gap and saved S0/RA homes need a complete
private-entry/address/call-boundary relation, including all untouched bytes.
The original unreachable duplicate load at word259 is retained and checked
as unvisited; it is the load following an unconditional terminal-branch exit.
No guard rows, inserted instructions or omission rows are produced at this stage.

## Fresh qualification and limits

Both final suites pass **five tests**, no failures/errors/skips: **56.949s
primary / 67.681s private sibling overlay**, with317 imported
tool fingerprints each. All dependencies were sealed before these final runs.

- Guest: **2,304 cases per raw/retail stream**, all three paths, both factory
  outcomes, unsigned RNG boundaries, all flag combinations, both stack phases,
  exact service transcripts and provider mutations. It compares all88/136
  descriptor bytes, all eight extra bytes, all64 matrix bytes, public memory,
  emitted return and saved ABI. It reaches344/345 words; word259 is unreachable.
  Initial threshold cases include qNaN/+infinity; converted coordinates remain
  finite and in signed32 range. This is not a hardware FCSR/fault-state claim.
- Native32: **288 cases at each O0/O2/O3**, exact independent retail transcripts,
  **1328 provider calls per positive run**,
  three public windows, strict aliasing and UBSan. All **12 semantic negatives**
  are effective: thresholds, duration, descriptor kind/flags, extra value/copy
  length, spray count/kind, sound height, flags reset and terminal return.
  It reads78/132 initialized descriptor bytes and four initialized extra bytes;
  untouched private bytes and incoming-home aliases remain separate guest tests.
- Complete original **func_15133894**, all80 words, connects to both child
  streams across **1,152 cases**. It checks flags/selector, crossing/geometry,
  attachment masks, all six callback arguments, both return values and saved
  ABI. Motion and terrain services remain modeled boundaries.
- The second genuine caller uses **0x15132FE0..0x15133028**, with its early
  return target0x151332C8, across **96 cases per stream**. This qualifies the
  literal dispatch window and return-dependent continuation. The full larger
  `func_15132DDC` body is not claimed qualified here.
- All1,730 production inputs, the live source, guard history and entire ELF
  remain byte-identical. Fresh actual-ELF recount and `make tools-check` pass.
  No production build or matching-credit increment is inferred from this screen.

## Continuation

Continue this function. First establish its complete frame/provider/FP relation
and investigate the remaining product operand order. Then derive checked
normalization from source fields/scheduling, exercise both padders and rebases,
connect actual child bodies where required, run actual Make and independent
strict full-image prediction, install, revalidate and recount before any credit.
Keep the original function/ROM and frozen baseline as authorities.

Graphify target links and scoped AST refresh are retained with old-node
preservation evidence; native refresh outcome is recorded separately. No
full-corpus re-extraction is claimed. Routine work uses zero Claude calls and
requires no REA setup changes. The separate dirty sibling tools tree is
preserved. No host-port source/build, Release artifact or save is changed.
Tools are committed before consumer notes; no push or automatic pause.
The 85% goal remains active.
