# Position, random fields and RGB effect descriptor directly recovered

Date: 2026-11-05. Target `func_15149EC4`, owner `generated_176A00`.
Source `conker/src/game/generated_176A00.c`; original `conker/asm/176A00.s`.

## Result and descriptor layout

The complete **67-word / 268-byte** routine emits directly from C with
**frame 0x50, eight call bindings, no alignment tail and no guards**. Its
VA is `0x15149EC4..0x15149FD0`; ROM is `0x177374..0x177480`.
All 35 compact and padded owner neighbors remain unchanged. Existing O2/g3
compiler options, every inherited guard byte and unrelated source stay fixed.

The recovered signature is `s32 func_15149EC4(u8 *actor)`. A local descriptor
starts at SP+0x1C. Its meaningful extent is 0x32 bytes; the four-byte-aligned
structure occupies 0x34 bytes. Unknown meanings retain offset-based names
rather than invented particle parameters.

| Descriptor offset | Recovered content |
| --- | --- |
| 0x00..0x0B | Three position words copied from actor+0x34 before any helper call |
| 0x0C..0x15 | Ten untouched local bytes |
| 0x16, 0x18 | Zero halfwords |
| 0x1A, 0x1C | Equal halfwords, one unsigned RNG remainder modulo 6 plus 8 |
| 0x1E, 0x20 | Zero halfwords |
| 0x22 | Unsigned RNG remainder modulo 201 plus 100: 100..300 |
| 0x24 | Unsigned RNG remainder modulo 5 plus 3: 3..7 |
| 0x26 | Halfword 600 |
| 0x28..0x2A | RGB selector 3 output |
| 0x2B..0x2D | RGB selector 4 output |
| 0x2E | Alpha byte 255 |
| 0x2F | Unsigned RNG remainder modulo 65 plus 92: 92..156 |
| 0x30 | Signed-byte field, unsigned RNG remainder modulo 3 plus 1: 1..3 |
| 0x31 | Zero flags byte |
| 0x32..0x33 | Two untouched alignment bytes |

The descriptor is submitted to `func_1518CA80` with mode 1, then the callback
returns zero. Forty initialized bytes are distinguished from twelve untouched
bytes. No initializer, blanket clear or fabricated values are added.

Aggregate position assignment preserves all three raw words, including signed
zero and quiet-NaN payloads, without floating arithmetic. The chained 0x1A/
0x1C assignment preserves one RNG draw and the original temporary lifetime.
A named shared local initially produced an extra eight frame bytes; the
direct chained form recovers all original words and frame placement.

## Original callback and connected helpers

An aligned full-ROM census finds no direct call or tail jump and exactly one
function-address literal: ROM 0x22E8D4, entry 1 of `D_80089E10`. The original
sixteen-word dispatcher window in `func_1513CFE4` at
`0x1513D290..0x1513D2D0` qualifies both the active-control gate and actor+0x72
selector. It calls through T9 at 0x1513D2B8, restores the actor pointer and
reloads the saved signed control byte. A zero result skips the separate
control-clear instruction. **56 cases per body** include zero selectors,
zero flags, signed byte endpoints and noncanonical incoming flag words.
The complete parent callback scheduler is not claimed.

The five explicit RNG calls retain their exact order. Both original RGB
helpers additionally call RNG, so connected execution consumes seven draws.
The **18-word original handwritten RNG** is executed with its actual 64-bit
seed transitions; each callback division uses the low unsigned 32-bit result.
All 31 words of the original RGB selector are also visited. Its palette reads
and three ordered byte stores qualify selectors 3 and 4, including live
palette changes under the opaque RNG's adversarial-effect fixtures.

The **138-word original submitter** is connected for its mode-1 path, including
position conversion, color/alpha scaling and construction of the 54-byte
packet supplied to `func_15167D84`. The lower factory remains opaque. The
mode-0 submitter path, an implementation of that factory, source recovery of
these helpers and gameplay are not claimed by this callback conversion.
The handwritten RNG stays assembly and receives no C credit here.

## Fresh qualification and language boundaries

All seven pre-install checks pass in **103.602 seconds**. All seven fresh
installed checks pass in **96.783 seconds**. Their receipts include:

* **1,940 guest cases per body**, spanning opaque helpers, the original RGB
  helper, the actual 64-bit RNG and the connected original submitter. All 67
  target words and every RNG/RGB instruction are visited. All modulo-201
  residues, range endpoints, negative RNG words, seed boundaries, snapshot
  mutations and both stack phases are included.
* **Ten guest copy aliases** and **205 fired access-prefix cuts** compare
  complete registers, RAM, call observations and ordered traces across all
  three bodies. Partial overlap and private stack observations are guest-only;
  portable C overlap or hardware-MMU behavior is not claimed.
* After submission, all twelve untouched descriptor bytes are deliberately
  unmapped. The original mode-1 submitter still completes and produces the
  independently expected factory packet, proving that path does not read the
  uninitialized prefix or tail padding. Guest stack-byte retention remains
  separate from native C's unspecified uninitialized contents.
* **Nine independent GNU links** qualify all eight R26 calls in three text/
  helper layouts, with 132 cases per body.
* Native32 O0/O2/O3 pass **2,910 executions** through a volatile typed callback
  pointer. Fixtures check structure size/offsets and only the forty initialized
  bytes, RNG draw count/state, raw position bits and color results. UBSan stays
  enabled; strict alias optimization is disabled for the flat byte views.
  Uninitialized gaps and padding are never read by the native checker.
* **Twelve native and thirteen separately compiled IDO controls** reject
  signed remainder, a wrong/late position copy, repeated RNG consumption,
  wrong color selectors, fixed values, range divisors, alpha, flags and return.
  The extra retained-byte store is guest-only because native checks do not
  assign values to uninitialized bytes. Every counted control has a fired
  witness.
* **268 raw-byte, eight binding and seven whole-image corruptions** fail
  closed. No normalization row is introduced.

The nineteen shared padder, relocation, matcher and protected-data checks pass
in **11.341 seconds**, and `make tools-check` passes. Unchanged neighboring
suites are reused through complete code/binding/data identity, not called
fresh tests. Routine work uses zero Claude calls and the documented IDO/GNU
path under the existing REA MIPS-adapter limitation.

## Production, diagnostics and preserved inputs

The immutable snapshot contains **99 files**, including all headers, target
and original caller/helper/data assembly, source/object, retail ROM, manifest,
Makefile, linker, ELF, code binary, progress and graph. Artifacts remain in
`conker/build/game-random-colored-effect-descriptor-15149EC4-match/`.
Main baseline is `bfcdcde9cede48a9223fbc33a1ecd6d3c30f7855`; mounted tools
baseline is `e5ccf4a552b3340154786ddfd0b4523f46a286bd`. Both start clean.
The sibling tools checkout is untouched; no fresh sibling qualification or
host-port Release change is claimed.

The inherited IDO Warning 712 at `func_1514BF50(arg0)` is identical before
and after normalizing source path/line numbers; it is outside this target.
No new owner diagnostic is added. Compact `.reginfo` changes only its T0-use
bit, GPR mask `E3FFFEFE` to `E3FFFFFE`; all other register-info bytes are
explicitly checked. Every other allocatable compact section and every
allocatable padded section remain identical. No constant pool is added.

Actual Make's owner and complete ELF equal the independent prediction byte
for byte. All **6,052 function addresses** stay fixed; only this body changes.
All **189,088 protected bytes across 720 owners** remain exact. The literal
full-file prediction accounts for **197 changed ELF bytes**, confined to the
target slot and its 12-to-268 symbol-size update. There are **zero metadata
permutations and zero excluded bytes**; all other named definitions agree.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `f2969440d7eafdb519d6529b4c42ff67ed291d73f771dc91bcfd28ae193adfd0` |
| Original target | `16caf9b2249e3385078f6daa7f74f48c10495f1e233bc89590fecd57c79e7355` |
| Production owner | `346c1e7f0ae953307618281376be8145433dff9919355d8bdcd8ec9ff40a1d7d` |
| Complete ELF | `c896ff6aec86e3f2311c1b13f8a999dbbb9b175dece56efc0b2bc208f86d8200` |
| Code binary | `9c1b22ed26cff489d3ec2f9c5d9a1e065bd76e11811b1355965890a4c84103c5` |
| Unchanged guard manifest | `892dcc21c80c8cc41c6970ed89c7f218e072b5a5487946d406a0d133e7f6d6d6` |

`make -C conker all` produces the binary and returns 2 only at the expected
incomplete-project retail checksum mismatch. The inherited duplicate
generated_12D630 recipe warning remains unchanged. Source newline style,
unrelated work and private/frozen inputs are preserved.

## Progress and continuation

The fresh actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,176 / 5,512 | 75.76% | 0 | 1,336 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,503 / 4,839 | 72.39% | 0 | 1,336 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes aggregate rows
only. The 80% threshold is 4,410, leaving **234 more** exact functions.
Next ordinary candidate is **func_1514D3B0**. Retain the eight separate
boundaries from Note 2103: `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, `func_150A6760`,
`func_150A70C0`. Keep the wider 80% goal active.

Mounted tools are committed first as
`e629b7ac317d2982ff7154ae81e23699917f63ab`
(`test(game): qualify random colored effect descriptor`). The consumer
records that pointer with the direct C and supporting documentation.

The ordinary AST-only Graphify update refuses its smaller 24,969-node
replacement, preserving the existing 58,774-node graph. The seven-path
scoped refresh retains 58,771 old IDs, replaces three relocated update-log
IDs and adds ten IDs. Every removed ID has a unique same-label/same-source
replacement; **zero nodes outside changed paths are lost**. The graph is
**58,781 nodes / 112,542 links / 5,174 communities**, SHA-256
`c679f94b131451d260ac2445a50334048cfee99661b38fe5ee563d4e71ad135d`.
The 31,816 retained nodes from 3,754 files outside the current scan corpus
are preservation evidence, not fresh full-corpus extraction. No force
overwrite is used. Final receipt paragraphs add no headings; the final
scoped refresh verifies unchanged topology.

The follow-up graph query and `graph-call-audit.json` verify updated function
location L65 and its type references. The current AST graph omits this
callback's three cross-file helper-call relationships. That limitation is
recorded explicitly; original assembly, eight relocation bindings and connected
guest execution remain the authoritative call evidence. A graph query's
missing edges are not used as proof that these calls are absent.
