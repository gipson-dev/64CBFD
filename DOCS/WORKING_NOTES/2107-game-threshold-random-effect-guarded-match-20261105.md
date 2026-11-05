# Signed-threshold randomized effect callback recovered

Date: 2026-11-05. Target `func_1516A538`, owner `generated_197120`.
Source `conker/src/game/generated_197120.c`; original `conker/asm/197120.s`.

## Result and record contract

The complete **68-word / 272-byte** routine matches as semantic C with
**nine closed frame corrections, frame 0x50 and three call bindings**.
Its VA is `0x1516A538..0x1516A648`; ROM is `0x1979E8..0x197AF8`.
All three compact/padded owner neighbors remain unchanged. No compiler-profile
change, assembly substitution, inserted instruction or omitted word is used.

The recovered callback is `void func_1516A538(u8 *record)`. It reads the
signed halfword at record+0x14 and returns without helpers when it is below
0x300. Otherwise it draws an unsigned remainder modulo 3, captures byte
record+0x25, draws an unsigned remainder modulo 360, and submits fourteen
arguments to `func_15171D4C`.

The second draw is an explicit statement. An argument-expression form emits
the same IDO words but permits other compilers to read trailing arguments
before that draw. Naming the unsigned angle preserves the original ordering
in native O0/O2/O3 too, with identical IDO bytes and frame corrections.
The threshold is tested once; subsequent helper changes do not recheck it.
Coordinates and trailing bytes are read after both draws, while the scale
byte retains the value captured between them.

| Argument / O32 location | Recovered value |
| --- | --- |
| 0 / F12 | Float conversion of signed record+0x18 halfword |
| 1 / F14 | Float conversion of signed record+0x1A halfword minus 10, before any narrowing |
| 2 / A2 | Float bits from signed record+0x1C halfword |
| 3 / A3 | Signed halfword 100 |
| 4 / SP+0x10 | Unsigned halfword zero |
| 5 / SP+0x14 | Unsigned byte, first unsigned remainder modulo 3 plus 32: 32..34 |
| 6 / SP+0x18 | Float conversion of second unsigned remainder modulo 360: 0..359 |
| 7 / SP+0x1C | Word zero |
| 8 / SP+0x20 | Word `25 + capturedByte * 25 / 255`: 25..50 |
| 9 / SP+0x24 | Word zero |
| 10 / SP+0x28 | Word 256 |
| 11 / SP+0x2C | Word zero |
| 12 / SP+0x30 | Unsigned record+0x0C byte |
| 13 / SP+0x34 | Word containing unsigned record+1 byte |

The final helper's interface is recovered from its actual incoming homes,
including signed/unsigned halfword, byte and word reads. No shared header
needs changing. Unknown record meanings keep offsets rather than invented
gameplay labels. The callback result is void; private V0 retention is checked
in the guest model without inventing a C return value.

## Closed frame correction

Normal O2/g3 emits all 68 words in the original order but reserves 72 rather
than 80 bytes. Its two spilled values occupy SP+0x40/0x44; retail uses
SP+0x44/0x48. RA remains at relative SP+0x3C in both layouts. The incoming
record home therefore changes from SP+0x48 to SP+0x50.

The nine guards alter only these immediate fields: the two SP adjustments,
three incoming-home accesses and four spill stores/loads. Opcodes, registers,
branches, arithmetic, call relocations and every other word are unchanged.
They restore the real frame's gap and alignment; they do not assert that the
unrecovered source declaration causing that reservation has been identified.
Named-angle, signed-variant and register-qualifier screens retain the same
raw frame; wider artificial declarations introduce extra instructions and
are rejected. No dummy padding declaration is installed.

The existing guard manifest is preserved as an exact byte prefix, followed
by exactly nine rows. Every row checks its own expected word and empty
relocation binding. Each expected-word corruption is rejected independently.
Raw public arguments agree on disjoint fixtures, but the raw frame fails
complete private-state parity. Original, normalized compact and production
padded code agree at the real private addresses, including alias/fault cases.

## Registration and original helper paths

A full aligned ROM census finds zero direct calls/tail jumps and exactly one
function-address literal: ROM 0x2314EC, index 3 of the eleven-word
`D_8008CA20` table. The full 44-byte table agrees between retail and ELF.
Four original dispatch contexts are exercised:

* The opening twelve words of `func_15167B44`, selecting unsigned byte +0x24.
* The callback gate in `func_15167E0C` at 0x151680CC, selecting signed byte
  +0x48 and retaining its -1 skip before the separate release continuation.
* The complete fourteen-word `func_15168BAC`, selecting unsigned byte +0xE4.
* The opening twelve words of `func_15169988`, selecting signed byte +0x40.

The original eighteen-word handwritten RNG executes with its real 64-bit
seed update. All eighteen words are visited; its assembly receives no new
C credit. The new oracle explicitly tracks MFC1 as a GPR replacement, which
matters when the previous RNG temporary contains a nonzero high word. A
seed-2 case exposed that inherited instruction-model gap; production words
were not changed to compensate.

The original 110-word `func_15171D4C` consumer and 43-word
`func_15171CA0` constructor execute their selected allocation-null,
transform-success and release paths. The lower allocator/transform/release
remain opaque ABI providers. The actual constructor initializes the returned
record, including selector byte +0x58; bounded synthetic asset pointers for
selectors 32..34 supply the consumer's dimension lookup. Other constructor/
consumer modes, lower helper implementations, full other parents, hardware
and gameplay are not claimed by these connected paths.

## Fresh qualification

All **seven pre-install checks pass in 59.526 seconds**. Evidence includes:

* **1,590 guest cases per body** across original, raw C, normalized compact
  and padded code. Independent results cover all 360 angle residues and 256
  scale bytes, threshold endpoints, signed coordinate limits, unsigned RNG
  words, mutations at both draws, actual RNG seeds, consumer branches and
  both stack phases. Private complete-state equality is required for the
  three fitted-frame bodies; raw C is checked against the public contract.
* All **64 reachable target words** are visited. Four original instructions
  for the unsigned-to-float negative correction cannot execute after modulo
  360; their exact bytes are retained and corruption-checked statically.
* **Eight private stack aliases** expose the original frame placement.
  **146 fired access-prefix cuts** compare complete registers, RAM, calls,
  ordered access traces and PC/delay context across the three fitted bodies.
  Incoming-home redirects are deliberate guest-only probes. Sparse early exit
  needs only the threshold field and stack. Native C stack-alias or portable
  fault behavior is not claimed.
* **32 cases per body** cover the four original dispatch contexts, active/
  skipped selectors and both sides of the threshold at both stack phases.
* **Nine independent GNU links**, three helper/text layouts and 102 cases per
  body qualify all three R26 bindings.
* Native32 O0/O2/O3 pass **198,876 executions**: 756 typed disjoint fixtures
  plus all 65,536 signed-halfword gate inputs per profile. UBSan is enabled;
  all fourteen arguments are checked through a volatile typed callback.
  Guest-only redirects and private aliases are excluded from native claims.
* **Eleven native and eleven separately compiled IDO controls** have fired
  witnesses: exclusive threshold, unsigned gate, signed RNG remainders, wrong
  variant/angle divisors, early/late scale capture, missing coordinate offset,
  wrong scale divisor, flags and swapped trailing bytes.
* **272 raw-byte, three binding, nine individual guard expected-word and
  seven literal-image corruption controls** fail closed. The old placeholder
  is rejected because it makes none of the required three calls.

Nineteen shared matcher/padder/relocation/data checks pass in 9.049 seconds;
`make tools-check` passes. The sibling checkout's twelve supported standalone
matcher/padder checks and smoke test pass in 16.594 seconds. The target suite
is fresh in the mounted consumer layout only. Sibling dirty work is preserved.
Unchanged neighbor suites are reused through complete body/binding/pool
identity, not called fresh tests. Routine Claude calls: zero.

## Production and continuation

The immutable snapshot contains 105 files: all headers, source/object,
original caller/helper/data assembly, retail input, linker, manifests,
Makefile, ELF, binary, progress and graph. Artifacts remain under
`conker/build/game-threshold-random-effect-1516A538-match/`.
Consumer baseline is `2485cd6204daa2f05b7c482f028af65d46312a08`;
mounted tools baseline is `b9a7f35f0caf925a2bac12f3bb2103fc4b4dfba9`, both clean.
The sibling tools checkout and frozen host-port Release are untouched.

The target owner has zero compiler diagnostics before/after. Compact register
information changes only to the explicitly pinned emitted GPR/CP1 masks:
`80000004`/`00000000` to `A300FFD6`/`0007F750`; remaining bytes are fixed.
Other compact allocatable sections and all padded sections remain identical.
The broad normal rebuild retains existing SDK and duplicate-recipe warnings;
it is not described as warning-free.

Actual Make equals the independently linked owner and **entire ELF**. All
6,052 function addresses are fixed; only this body changes. The literal
prediction accounts for **208 changed ELF bytes**, confined to the target
slot and its 12-to-272 symbol-size update, with **zero excluded bytes and
zero metadata permutations**. All 189,088 protected data bytes across 720
owners remain exact. The complete consumer/dispatcher objects
generated_19F150, generated_196DB0 and game_1944C0 are unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `f91852acca330bbedea7d2cb186d94fd4eebb7d422e13361e7099d46f813049e` |
| Original target | `32a5796924aa96d4c9d38dd0c52e0c4918ca922793f1ed401ab6d050cffa7cf9` |
| Production owner | `d251c1a88b7c35dcd439c47054ac505e76a6a80b04e7f0af01eb2cd51f2a2f2c` |
| Complete ELF | `f393cfbd7602e51e735eb052dcb9d8ab3ddd59afda769203479384fa078b003b` |
| Code binary | `7a4534489aa4a80a040b32b8e24df26e30418895ccd941e0963ca0f805a38439` |
| Appended guard manifest | `dbf863c776f06735c271a02c91930c84fd5ce9cf064086653a32d6fb19d24f29` |

The production rebuild/recount takes 307.119 seconds. `make -C conker all`
produces the binary and returns 2 only at the expected incomplete-project
retail checksum mismatch. The progress CSV is byte-identical, preserving
conversion inventory and byte percentages. No private inputs or saves change.

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,178 / 5,512 | 75.80% | 0 | 1,334 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,505 / 4,839 | 72.43% | 0 | 1,334 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. The README changes aggregate rows
only. The 80% threshold is 4,410, leaving **232 more** exact functions.
Next ordinary candidate is **func_151E51EC**, 72 words/frame 0x20, owner
generated_20AE20, ROM 0x21269C. Its placeholder and original direct caller
in game_45B80 are identified; no matching credit is added for it here.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. The wider 80% goal stays active.

All seven fresh installed checks pass in **54.398 seconds**, including exact
guard-prefix preservation, the literal production ELF and the complete
private/fault/alias checks. Rerun the prepared target with
`python3 -m unittest tools.tests.test_game_threshold_random_effect_match -v`.

Mounted tools are committed first as
`581cf3760c33737cdcebf2bd423ad9e66380136f`
(`test(game): qualify threshold-triggered random effect`). The consumer
records this exact pointer with the source, guard append and documentation.
The commits are local; no push is performed.

The ordinary Graphify update refuses its smaller 24,991-node replacement.
The eight-path scoped refresh retains 58,785 old IDs, relocates three
update-log IDs through unique same-label/same-source replacements and adds
ten IDs. **Zero nodes outside changed paths are lost**. The resulting graph
has **58,795 nodes / 112,544 links / 5,120 communities**, SHA-256
`5805e734462655500b2fcba2d9874f5ac75fc4a9ea41aea6f97593f0b5904391`.
The target location is refreshed to L17. Its outgoing cross-file RNG/consumer
call edges are absent in this scoped graph, preserving the previously
documented limitation; the source, three relocations and connected guest
execution establish those calls. The graph is navigation evidence, not a
complete call census. The 31,816 retained nodes from 3,754 files outside the
current scan corpus are preservation evidence, not a fresh full extraction.

The final production audit rechecks the four production hashes, complete
guard-prefix append, byte-identical progress CSV, all 105 frozen inputs and
three unchanged context objects. The live nonexact list and Graphify locate
the next candidate, func_151E51EC; its source and original caller are verified
directly before handing it off.
