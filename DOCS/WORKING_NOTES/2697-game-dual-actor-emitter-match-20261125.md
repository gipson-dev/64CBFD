# Dual actor emitter match - 2026-11-25

`func_150B37C8` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_DFBF0.c`. VA150B37C8..150B3AA8 /
ROME0C78..E0F58: 184 body words, 736 bytes, frame248. The unchanged slot ends
at150B3AB0/E0F60 and contains two unreachable alignment NOPs.
**99 word values and bindings emit directly; 85 expected-word guards recover
retail register allocation, independent scheduling and one unpassed four-byte
integer RNG spill at SP+54 instead of SP+5C. Raw C is not byte-exact.**
The frame, saves/lifetimes, incoming/outgoing homes, FP operands and relocation
bindings agree. There are no inserted/omitted words, dummy locals, size tricks,
compiler profile, Makefile or shared-header changes.

Actual production: **4,676 / 5,528 (84.59%)** total and **4,003 / 4,855
(82.45%)** Game. Init492/492 and Debugger181/181, zero address drift,
852different. **23 more verified matches to85%**. This function earns one
match; helpers/callers earn none. Conversion rows and denominators stay fixed.

The aligned pristine-ROM census finds no direct J/JAL and exactly one literal
entry pointer: ROM22EF04 / VA8008A444, `D_8008A430[5]`. Its actual parent is
`func_15148BA4`, whose source declares the table's six-word callback interface:
actor, previousX/Y/Z, actor+60 height, actor+64 context. The three previous
coordinates are unused by this callback. Actor+94 positions and actor+98 record
are captured before providers. Three signed16 choices at `D_80088700` (15/16/17)
are copied before the first float RNG; all six bytes match pristine ROM and the
frozen ELF (SHA256 8f6210d6c395c30b732af85d2b2051dfda2aa27a10d300c952b70f4248e42430).

The callback writes record+20=4 and computes range=FRNG*50+50. Unsigned RNG%3
selects the captured choice. The real first descriptor is40 bytes: flags17,
duration150, selected kind, zero fields08/0C, record1B/1A bytes10/11, zero
bytes12/13/14, FF at15 and resource30002. There are25 initialized and15
unspecified bytes; the backend's complete40-byte copy must not be shortened.
The next three integer draws supply the low byte and the sum of two low bits.
The14-argument `func_1513C73C` call forwards descriptor,1,0,context,
captured-position x,height,z,range,range,lowByte,parity,0,actor0C,actor01.

The second request is28 bytes: captured-position x/z with two signed index
reloads at actor2D, reloaded height, duration60, field0E1, active1 and actor25
count. Its32-byte payload has record0*.75, record4 x velocity, FRNG*15+15 y,
record0C z reloaded after that RNG, record10, field18=8 and record19/1A/1B
kind/alpha/control bytes. The32-byte render block contains words0,1,160600,3,
16,128,32 and bytes0/9. These three objects have75 initialized bytes and17
unspecified bytes. The15-argument `func_15147DA0` call forwards request,payload,
0,1,7,0,0,0,0,0,0,render,0,actor0C,actor01. Both factory results are ignored;
return is always one. Struct names retain the address and opaque fields where
semantics are not established; SDK `vertex` fields describe actual positions
and velocities. Real random locals are named `byteDraw` and `parity`.

Initial reconstruction had184words/frame256/98 differences. Declaration order,
consumed-parity reuse, real field assignment order and SDK vertices recover the
248-byte frame and85 differences. Several bounded alternatives were rejected
(including an earlier-request variant of183words and a scoped RNG block of185).
None was installed. The final named body emits identical words/bindings to the
selected vertex candidate. Source screens remain private historical evidence.

The scoped symbolic observation proof executes all184 words and compares
8 provider boundaries, 5 ordered FP operations, 4 ordered public/ABI writes,
every provider argument and every byte of each passed private object. It treats
all signed-byte indices, unsigned RNG returns, initial template bytes and
provider public epochs/results symbolically. Four independent rebases include
HI/LO carry and different jump regions. Nine supported, completely executed
controls alter flags, duration, resource, mask, provider tag, FP operation,
public byte, spill alias or template binding; every change is rejected.
The contract is mapped ordinary nonvolatile, single-thread memory with the
callee's private frame disjoint from public objects. A provider cannot inspect
unpassed private bytes. This is an observation proof, not general SMT, arbitrary
machine-context equivalence or raw private store/fault-order equality. The
85 guards are therefore explicitly broader than GPR-only coloring.

Both complete owner padders agree, preserving all five raw/padded neighbors and
all owner pools. The three-command actual-Make route and independent reference
link splice only the original736-byte target into frozen old C and retain the
8 alignment bytes through the owner's end. **Complete production equals the
predicted ELF: 573 changed bytes, zero exclusions.**
All189,088 protected Game data bytes/720 owners, layouts, conversion rows,
old guard bytes and unrelated frozen inputs remain fixed. Only85 checked rows
append; their expected words and relocation bindings fail closed.

Guest execution passes **680cases per four
retail-equivalent streams plus raw**, all184 words and
**436fault quads** for the four normalized/original
streams. Cases include all256 signed-byte indices, modulo and32-bit RNG limits,
low-byte/parity combinations, four rounding modes, finite inexact values,
captured pointers/template and actual home/public reload mutations. Complete
40/28/32/32 byte packets include seeded holes. Raw public/passed-object,
register/FP and return observations agree; raw whole-private-stack and fault
prefix equality are not claimed. GNU checks make20 links and40 guest runs,
32 full normalized/original and8 raw observable comparisons. Both oversized
probes reject. All170 guarded corruptions reject,198 unguarded corruptions
remain visible and10 relocation pins reject changed bindings.

Native SDK32 execution passes **672legal cases each
at O0/O2/O3**, strict aliasing, explicit rounding and UBSan. It observes all
10,630 public fixture bytes through paired digests and25/75 initialized packet
bytes; it excludes15/17 unspecified bytes and does not inspect unpassed private
storage. All17 wrong-source controls terminate with comparison exit42; signals
and UBSan traps do not count as effective controls. An initial O0 fixture failure
was traced to reset arithmetic inheriting the previous row's downward rounding
and creating negative zero. Reset now runs under round-to-nearest before setting
the requested mode. Production C was unchanged by that fixture correction.

The full143-word original parent is executed in384 cases per stream, with
48 connected children per stream;120 parent words are visited. All six actual
callback words and four effective child-return-zero controls pass. The primary
registry context is qualified; the alternate callback table branch and the
geometry helper's internals remain contracted. Static byte identity is recorded
separately from executed coverage.

Both original RNG routines execute all43 words in192 cases per each of five
streams. An independent64-bit recurrence checks six transitions (two float and
four integer draws), both float results and FCSR under all four rounding modes.
The original70-word secondary factory and11-word memcpy execute in16 cases,
including allocation failure. Full32-byte payload and32-byte render copies
preserve all64 bytes, including10 unspecified guest bytes. The original50-word
first wrapper executes64 cases spanning backend failure, initializer failure
with free, and success; all forwarded arguments, SP/saves and returns agree.
An independent16-case original memcpy check copies the entire first40-byte
descriptor including15 unspecified bytes. Backend1513C350 and initializer1513E2AC
match their103/271-word pristine windows but their internals remain contracted.
Allocator/backend internals and full gameplay are not qualified by these tests.

One packet-only Claude Pro advisory was used, with zero tools/MCP/agent calls.
Its RNG delay-slot interpretation was accepted. A blanket equivalence claim and
the asserted retail computed-index hoist were rejected; retail only hoists the
constant20 and reloads the index twice. The suggested earlier reads were tested
and worsened the fit. Provider/private contracts and public read commutation were
independently checked. No Claude answer supplies matching credit.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 90.952s | 1 fresh / 4 unchanged |
| preinstall-sibling | 98.339s | 1 fresh / 4 unchanged |
| installed-primary | 326.728s | 5 fresh / 0 unchanged |
| installed-sibling | 344.285s | 5 fresh / 0 unchanged |

Baseline consumer `b05fedc4669814e273b8861a2efeabfa01ea4ea5`.
Tools commit `c43d9d5a6bea49efe21d8bdc8388bfb2d52715e2`.
Production ELF SHA256 `d897364166407170c535ae00cc6174ae7673e000d0cd8f4c80758da9209e14c3`.
Padded owner SHA256 `9fb46a20d5fbc6caf97451d132e505d31ead52324fdfdcfc860ebac9ff7c61d5`.
The pre-adoption freeze contains3695 inputs/2300 immutable snapshot copies.
Private receipts: `conker/build/game-dual-actor-emitter-150b37c8-private`.

Both initial pre-install suites passed five fresh tests (370.338/338.782s).
Git then caught one final blank line in the caller test. Both copies received
the same AST-identical EOF correction. The affected parent/helper gate was
rerun in each copy; the other four gates retain their complete unchanged-input,
import, data and artifact fingerprints. Those receipts are explicitly reused,
not called fresh. Both installed suites have five fresh tests, zero reuses.
Both task copies use exact source/import/data/manifest fingerprints. The real independently dirty sibling
checkout is preserved. Shared `make tools-check` passes. Tools are committed
before consumer adoption; production rebuild, recount and installed suites are
fresh. The root README only receives aggregate status rows/date. Graphify's
native update and scoped AST retention audit follow, retaining all old IDs and
qualification metadata; this is not a full-corpus re-extraction claim. No host
build, launch, Release change, helper credit or push is performed. The expected
host checkout currently has no source/Git tree suitable for applying this change.

Next: keep the85% objective active and qualify another unmatched Game function.
The C9BDC/matrix and previously rejected candidates remain private/uncredited.
