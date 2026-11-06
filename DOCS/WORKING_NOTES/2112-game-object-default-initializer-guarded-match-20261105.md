# Object defaults initializer recovered with FPR allocation guards

Date: 2026-11-05. Target `func_1505F188`, owner `game_83300`.
Source `conker/src/game_83300.c`; original
`conker/asm/nonmatchings/game_83300/func_1505F188.s`.

## Result and initialization protocol

The complete **68 words / 272 bytes**, frame **0x18**, match at
VA `0x1505F188..0x1505F298`, ROM `0x8C638..0x8C748`.
The recovered interface is `void func_1505F188(struct127 *object)`.
It uses the existing canonical 0x32C-byte object and preserves the original
mixed-width accesses, including halfwords across currently opaque fields.
No shared header or global end-marker declaration changes are made.

1. Clear the complete **812-byte object**, in 203 ordered word stores.
   The end check is unsigned pointer order; there is no added null guard.
2. Load `D_8009962C`, set byte +0x2FD to two and halfword +0x38 to -10000.
   Set xz/y scale to 1.0f, and +0x118/+0x180 to the loaded value.
   Load `D_80099630` before the later ID/header/pointer stores.
3. Preserve the remaining byte/halfword defaults, including ID 0xFFFF at
   +0x84, the self pointer to object+4 at +0x2C4, ones at +0x2C8/+0x2C9,
   byte +0x2CB = 50, +0x48 = 1.0f and gravity from the second loaded constant.
4. Call the original `func_150ADA20()` and store its **unsigned 32-bit
   remainder modulo 50, plus 50**, at byte +0x6E. Negative signed returns
   must still be interpreted as their complete unsigned bit pattern.
5. Call `func_150615DC(object)`, then set bytes +0x1DD..+0x1DF to 255 and
   the nine halfwords +0x18C..+0x19C to 0,0,0,0,0,10,10,0,0 in order.
   Earlier helper effects outside those final stores remain visible.

The constants are unchanged at `0x8009962C..0x80099634`, original ROM
`0x23E0EC..0x23E0F4`: bits `C61C4000` (-10000.0f) and `40533333`
(the float32 representation of 3.3). Their meaning beyond the existing
canonical fields is not invented. These loads/stores perform no float
arithmetic; the qualification includes preserved NaN payloads.

## Natural source, FPR fit and unchanged owner

A chained float assignment caused an extra object reload in the first
69-word draft. Explicit snapshots recover the complete 68-word routine,
original store order, frame and incoming pointer home at SP+0x18. The
selected source uses the established O2/g3 profile, with no Makefile rule.

Nine guarded operand fields account for the complete floating allocation:
unit F12 -> F0, base F0 -> F2, gravity F2 -> F4. These cover one MTC1,
two LWC1s and six SWC1s. No opcode, immediate, GPR, relocation, instruction
order, frame or branch changes are made. All **59 other words** are unchanged.
The tool derives this mapping by decoding every target COP1/load/store
operand, pins the exact nine offsets and validates the complete result.

The nine appended guard rows preserve all predecessor bytes, with no insert
or omit rows. All six bindings remain at their original offsets and refer
to the same two data words and two callees. Raw and padded comparisons
preserve **all 88 other functions**. Every compact and padded allocatable
pool, including register information, remains identical. The eight inherited
IDO Warning 712 diagnostics remain identical after path/line normalization.

## Complete caller census and original helpers

The full aligned ROM census finds **six JALs**, no tail jump and no aligned
address literal. Each passes an object pointer and ignores the initializer's
return. The callers do not depend on a fabricated zero result.

| Parent | Call VA | Original context executed |
| --- | --- | --- |
| func_1505D1C4 | 0x1505D1EC | Complete 61-word slot-25 initializer |
| func_1505ED34 | 0x1505EE94 | Three-word call/save/reload window; reloads its own object into V0 |
| func_15060F28 | 0x150611CC | Two-word JAL / S1-to-A0 delay window |
| func_15072420 | 0x150724A8 | Three-word incoming-home argument / index-reload window |
| func_15082A44 | 0x15082AD4 | Seven-word pointer/save/call/branch window |
| func_15082A44 | 0x15082B2C | Seven-word indexed pointer/save/call/branch window |

The corresponding ROM calls are 0x8A69C, 0x8C344, 0x8E67C, 0x9F958,
0xAFF84 and 0xAFFDC. The only C call now uses a scoped struct127 pointer
cast for `&D_800D121C`; the prototype agrees with the recovered definition.
That address is also an actor-array end marker elsewhere, so its existing
shared scalar declaration remains intact. All caller code stays unchanged.

The complete slot-25 parent preserves its mixed float/integer O32 arguments,
writes its position/settings after initialization, calls the opaque adapter
with current index 25, then restores its prior current-object index. The
other five windows do not qualify their full parent bodies or prior helpers.

All **18 original RNG words** execute with actual 64-bit seed transitions.
The handwritten RNG remains assembly, unchanged and separately accounted.
All **12 original component-initializer words** execute, covering the nine
header-byte stores at +7,+8,+9,+A,+F,+E,+D,+C,+B. That existing helper is
already byte-exact; its C body and emitted words stay unchanged.

## Focused qualification and production image

Seven checks pass before and after installation:

- **778 guest cases per original/raw/fitted/padded body** cover all 68 words,
  every clear store, signed/unsigned RNG boundaries, all fifty remainder
  classes, constant-bit patterns, snapshots and provider mutations.
- **22 alias/home cases** cover constant words within the cleared object,
  loads that observe earlier stores, both stack phases and incoming pointer
  home redirection at each helper. Two wrapping-address cases exercise the
  clear gate; these and invalid/home probes are guest-only evidence.
- **731 fired access-fault prefixes** preserve the complete original/fitted
  instruction, delay, private state and memory prefix. Two sparse cases
  check unmapped-null and unaligned stores, with no added guard.
- All six original caller contexts execute: **80 short-window cases** per
  body plus **16 complete-parent cases**, including the original slot-25
  stores, adapter observation and current-index restoration.
- **Twelve independent GNU links**, 51 cases per body and three entry/data/
  callee layouts qualify every HI/LO and both JAL bindings.
- Native32 O0/O2/O3 with UBSan pass **776 rows each / 2,328 executions**.
  Complete object-byte hashes, call snapshots and canaries are checked;
  the relocated self pointer is checked numerically. Native multibyte fields
  adapt to i386 byte order. Raw bit initialization avoids the native float
  return ABI altering signaling-NaN inputs. Seventeen IDO and seventeen
  native negative controls all fail effectively.
- All 272 raw-byte, six binding and eighteen guard corruptions are rejected.
  Nine literal-image corruptions cover the target, surrounding bytes, header,
  both symbol groups and both string blocks. The old stub is rejected.

Raw C has different private FPR allocation before the helpers; that private
state is not claimed identical. Public memory/call/access behavior is checked
independently. Fitted/padded instruction and private/fault state is exact.
Native invalid-address or incoming-home alias behavior is not claimed.

The immutable input snapshot contains **163 files**. It includes all headers,
target/caller sources and objects, original ASM inputs, RNG source/object/ASM,
the two external caller owners, ROM, manifests, linker, Makefile, ELF, binary,
progress and graph. Artifacts remain under
`conker/build/game-object-defaults-1505F188-match/`.
Consumer baseline: `0d9fe2cd2a30a7c45232b974632a2e6211b47925`.
Mounted tools baseline: `237f614ead7e57553bda6c3ae564c84059f288be`.

Actual Make equals the independent owner and **entire ELF** byte for byte.
The literal prediction accounts for **303 changed bytes**, including the
target slot, its symbol extent from 16 to 272, and **66 symbol/string bytes**.
Two fixed five-record rotations preserve every named definition except that
declared target size. There are no excluded bytes. All **6,052 function
addresses** stay fixed, and every other body stays unchanged. All **189,088
protected data bytes across 720 owners** remain exact.

The complete RNG and both external caller objects remain byte-identical.
The Makefile, original assembly, headers and progress CSV remain unchanged.
The installed suite, nineteen shared checks and tools smoke pass. The dirty
sibling tools checkout passes its twelve supported shared checks and smoke,
without edits. Prior neighbor suites are reused through unchanged complete
function/binding/pool evidence. Routine Claude calls: zero.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `fca1d82f9f69139b5f3a2b741a5b1e3f070f502dc730995ec69cff72a52a863a` |
| Original target | `f40509518bd60c31bd037ae4b24a8f20b4869676ea8541108c6b5f0d10134c65` |
| Production owner | `71853fc3dbc1e39aadc324d4c832f422a35b7107085f70c54e9748f82da3c0bf` |
| Complete ELF | `57c96c17776df60f2ce0a4a4fc21e5399f79eff0db45b34007f5813e4bf1aeac` |
| Code binary | `ee65cbda7ccf5fe370693532b4a4061f4b041a125aa7b01ebc13781248680513` |
| Extended guard manifest | `693728894a396b7cb48827cc87d5a33f30a2000e981e65f531ba78c3b9fe76d8` |

The production rebuild/recount takes **309.835 seconds**.
`make -C conker all` returns 2 only at the expected incomplete-project retail
checksum mismatch. Existing compiler/recipe warnings remain. Source newline
styles are preserved. Root README receives aggregate rows only; prior history
bytes stay intact. Unrelated sibling work, private inputs, real saves and the
frozen host-port Release remain untouched. This is not gameplay acceptance.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,183 / 5,512 | 75.89% | 0 | 1,329 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,510 / 4,839 | 72.54% | 0 | 1,329 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. The 80% threshold is 4,410,
leaving **227 more** exact functions. Continue with **func_15062D10**,
69 original words, frame zero, in the same owner and original
`conker/asm/nonmatchings/game_83300/func_15062D10.s`,
ROM `0x901C0..0x902D4`. It gates on the slot table and updates two packed
12-bit coordinates while retaining the high command byte and strict single-wrap
tests. Its first private C draft emits 67 words and preserves all other
88 owner functions. Caller/ABI, parameter homes, wrapping arithmetic,
ordered reads/stores, shape, padding and production gates remain open;
the private draft is uninstalled and uncredited.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the 80% goal active.

Mounted tools are committed first as
`165d1f230c6fdedca76a1e310e5bb8f43486973a`
(`test(game): qualify object defaults initialization`). The consumer records
that exact pointer with the recovered C/interface, nine guards and documentation.
These are local commits; no push is made.

The ordinary Graphify update refuses its smaller 25,021-node replacement.
The subsequent refresh is scoped to the eight changed consumer paths. It
retains 31,816 nodes from 3,754 files outside the current scan corpus;
this is not a fresh full extraction or a graph-package/policy change.

The scoped refresh retains 58,822 old IDs and relocates three update-log IDs
through unique same-label/same-source replacements. No nodes outside changed
paths are lost. It adds ten IDs, seven for this note and the three relocated
headings. The result is **58,832 nodes / 112,595 links / 5,160 communities**,
SHA-256
`9f5fec24d63c0c05a6912162853423b55ee5e52e4e010e21cc872668a6adadba`.
The target node is refreshed to L1105 with struct127 and the local component
call edge. The cross-file handwritten RNG edge is absent; emitted code and
the complete caller/ABI audit remain authoritative. No edge is hand-added.
A following refresh reports no topology changes and leaves the hash stable.

The final production audit verifies the full ELF/binary/owner/guard hashes,
all 163 frozen inputs, unchanged progress/Makefile and three complete external
objects. Historical documentation bytes are preserved; the root README changes
only two aggregate rows. The separate sibling dirty state and frozen host
Release remain untouched, and the wider 80% goal remains active.
