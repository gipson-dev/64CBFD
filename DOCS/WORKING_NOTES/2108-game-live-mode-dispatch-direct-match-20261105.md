# Live mode, input suppression and transition timer directly recovered

Date: 2026-11-05. Target `func_151E51EC`, owner `generated_20AE20`.
Source `conker/src/game/generated_20AE20.c`; original `conker/asm/20AE20.s`.

## Result and state protocol

All **72 words / 288 bytes** emit directly from semantic C, with **frame
0x20, 32 bindings and zero guards**. VA is `0x151E51EC..0x151E530C`;
ROM is `0x21269C..0x2127BC`. All **59 compact and padded owner neighbors**
remain unchanged. The original assembly, compiler options, guard bytes and
existing `jtbl_800AB9BC` rodata anchor remain fixed.

The recovered interface is `void func_151E51EC(void)`. Its sequence is:

1. Capture the unsigned entry mode `D_800E0B94` in the original SP+0x1F byte.
   Set `D_8003C8E0` to 0x08000000 and byte `D_800E0BDC` to 255, then call
   `func_15042D78(0x81)`.
2. Copy the live unsigned halfword `D_800BE930` into `D_800E0B9A`. When signed
   countdown byte `D_8008FE28` is nonzero, decrement it and clear that mask.
   A countdown of one still suppresses this invocation even though it becomes
   zero. Negative byte values also decrement, preserving the original low byte.
3. Reload the current mode. Call `func_151E6964` with 2 for mode 0, 4 for
   mode 8, or 1 otherwise. Reload the mode again and invoke its entry in
   `D_8008FDEC` through the live table pointer.
4. Reload the mode after the callback. Mode 7 skips both timer accounting and
   transition recording. Otherwise add the current `D_800BE9E4` to
   `D_800E0A90` with wrapping 32-bit arithmetic. If the final mode differs
   from the entry snapshot, store that snapshot in `D_800E0B95` and clear
   the timer. Intermediate mode changes are not substituted for the snapshot.
5. Clear `D_8003C8E0` on every normal return.

The C casts the timer addition to unsigned words so wraparound is explicit.
The final comparison's natural current-mode/previous-mode operand order
emits retail's BEQ operand order directly; reversing it was one semantically
equivalent instruction difference and is not hidden with a guard.

## Declarations, table and caller

The owner's countdown declaration changes from u8 to s8, recovering the
original LB. Its other existing uses store the constant 2; complete neighbor
comparison proves those routines remain identical. The caller's local
declaration changes from s32 to void, matching the unused result and the
retail routine's unconstrained V0 lifetime. All **sixteen functions** and
the complete `game_45B80` production object remain byte-identical.

The unrecovered `func_151E6964` placeholder retains its existing old-style
declaration in this owner; the new call sites pass the original single word.
The placeholder's signature/body is not rewritten to manufacture a prototype
match. The command helper has its recovered u8 interface. No shared header or
other owner requires editing.

An aligned full-ROM census finds exactly **one direct call**, at ROM 0x45D40 /
VA 0x15018890 in `func_1501878C`, with no tail jump or address literal.
The original ten-word caller window checks `D_800BE615` before the call and
again afterward. Both taken exits and fallthrough are checked; the complete
parent/frame coordinator is not claimed.

The actual callback table has **twelve entries / 48 bytes**, ROM
0x2348AC..0x2348DC, and agrees exactly with the linked ELF. Adjacent floats and
the countdown byte are not counted as additional entries. Original
`func_15042D78` executes all seven words and writes its command byte; mode 2
also executes the actual two-word empty `func_151DE8E8` callback. The other
callbacks and `func_151E6964` remain opaque effectful ABI providers. Their
implementations and gameplay are not qualified by this wrapper conversion.

## Fresh qualification

All **seven pre-install checks pass in 51.084 seconds**; all **seven installed
checks pass in 56.374 seconds**. Evidence includes:

* **1,250 guest cases per body** across original, natural compact C and padded
  C, with complete private-state equality. All 72 target words are visited.
  Independent call-boundary snapshots cover entry-mode capture, changes at
  each helper/callback phase, live table replacement, all 256 countdown-byte
  patterns, every real mode, timer wrapping and both stack phases. Opaque
  helpers clobber caller-save GPR/FPR state, HI/LO and all four outgoing homes.
* **Twelve mapped global aliases** qualify shared input/mask, timer/ticks,
  countdown/latch and flag/timer storage. **76 fired access-prefix cuts**
  compare complete registers, RAM, ordered traces, calls and PC/delay state.
  Seven invalid physical callback indices retain their faults; no range guard
  is inserted. These are guest instruction-model observations, not portable
  C invalid-access or hardware-MMU claims.
* **24 cases per body** execute the original caller's pre-call and post-call
  gates, including callback changes to the gate and both stack phases.
* **Nine independent GNU links** in three layouts qualify all **32 bindings**
  and HI/LO carry boundaries, with **870 cases per body**. Separate rebased
  fixtures provide 256 disjoint synthetic callback slots to check the complete
  unsigned mode-byte index range. The physical retail table remains twelve
  entries; its nearby countdown is preserved rather than overlaid by fixtures.
* Native32 O0/O2/O3 pass **1,875 executions**, 625 bounded disjoint fixtures per
  profile, through a volatile void callback pointer with UBSan enabled.
  Native call order, call-boundary state and all final scalar state are checked.
  Aliases, malformed physical indices and synthetic high-slot rebases remain
  separate guest evidence.
* **Twelve native and twelve separately compiled IDO controls** have fired
  witnesses: late entry snapshot, positive-only countdown, failure to suppress
  the last countdown frame, wrong mode-0/mode-8 helper parameters, stale
  callback index, entry-mode-7 gate, wrong previous-mode store, missing timer
  reset, wrong tick increment, and missing/wrong begin/end flag writes.
* **288 raw-byte, 32 binding and eleven literal-image corruption controls**
  fail closed. The old zero-return placeholder is rejected by its missing
  three-call protocol. No normalization rows are added.

Nineteen shared matcher/padder/relocation/protected-data checks pass in 11.725
seconds; `make tools-check` passes. The sibling tools checkout's twelve
supported standalone matcher/padder checks and smoke test pass in 10.844
seconds. The new target suite is fresh in the mounted consumer layout only.
Unchanged neighbor suites are reused through complete body/binding/data
identity, not described as fresh checks. Routine Claude calls: zero.

## Literal production image and preserved inputs

The immutable snapshot contains **98 files**, including all headers, owner/
caller source and objects, original assembly/data, command-helper source/
object, retail ROM, manifests, Makefile, linker, ELF, binary, progress and
graph. Artifacts remain under
`conker/build/game-live-mode-dispatch-151E51EC-match/`.
Consumer baseline is `b19054988fca1334c1dfad9db3faed7ac673fbd1`;
mounted tools baseline is `581cf3760c33737cdcebf2bd423ad9e66380136f`, both clean.
Sibling dirty work, private inputs, saves and frozen host-port Release remain
untouched.

The target owner has zero compiler diagnostics before/after. All compact
allocatable sections, including register information, are identical; all
padded sections remain identical too. The caller's three inherited Warning
712 diagnostics agree after source/line normalization. The existing duplicate
generated_12D630 recipe warning remains; the full build is not warning-free.

Actual Make equals the independent owner and **entire ELF** byte for byte.
All **6,052 function addresses** stay fixed; only this function's body changes.
All **189,088 protected data bytes across 720 owners** remain exact.

The full-file prediction accounts for **299 changed bytes**: 228 in the target
slot/symbol-size update from 12 to 288, plus exactly **71 metadata bytes** in
three closed symbol/string pair swaps:

| Symbol-record start | Original adjacent names, swapped together with their strings |
| --- | --- |
| 0x2BE69C | D_800E0BDC, D_800A36AC |
| 0x2C9DFC | D_800BE930, D_8009CDE8 |
| 0x2DDD1C | func_15187978, D_8009E570 |

Every original record/string boundary is checked. The serializer preserves
each named definition's value, size, binding and section, apart from the
target's declared size update. There are **zero excluded bytes**, no blanket
metadata comparison exclusion and no unnamed unexplained difference.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `f3a8c25768375ee91817dd8ed3251295bb22ca379e3a3f9beb8e13331b122d5e` |
| Original target | `34c234ce0c4fa85689d95088b4eae5315bbb7dcfa4dfc33252d376ab474d256c` |
| Production owner | `e241f5fe3b27f075148678d9bacd66e95617c1bfab77a4701212ab8fd0cce389` |
| Complete ELF | `acf4fa64d83e59624bf21d9f9da35e85d2f32c78b391e8cf873f5ef697223e17` |
| Code binary | `efb6b8b54633a757acbf15a3b27a18c186e9458efb483e38f2d1d6a9337b3f30` |
| Unchanged guard manifest | `dbf863c776f06735c271a02c91930c84fd5ce9cf064086653a32d6fb19d24f29` |

The production rebuild/recount takes 63.630 seconds. `make -C conker all`
produces the binary and returns 2 only at the expected incomplete-project
retail checksum mismatch. The entire progress CSV is byte-identical,
preserving conversion rows and byte percentages. Source newline styles are
preserved.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,179 / 5,512 | 75.82% | 0 | 1,333 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,506 / 4,839 | 72.45% | 0 | 1,333 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes aggregate rows
only. The 80% threshold is 4,410, leaving **231 more** exact functions.
The live nonexact list selects **func_15007168** next: 69 words/frame 0,
owner game_33990, ROM 0x34618. Its existing placeholder and original
`asm/nonmatchings/game_33990/func_15007168.s` are identified; no matching
credit is added for it here.

Retain the eight separate boundaries from Note 2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Keep the wider 80% goal active.

Mounted tools are committed first as
`6ea23cff3be96f909de0fc369fd7c27c40840728`
(`test(game): qualify live mode dispatch and transition timing`). The consumer
records that exact pointer with the C, declaration repairs and documentation.
These are local commits; no push is performed. Rerun the prepared target with
`python3 -m unittest tools.tests.test_game_live_mode_dispatch_match -v`.

The ordinary Graphify update refuses its smaller 24,998-node replacement.
The eight-path scoped refresh retains 58,792 old IDs, relocates three
update-log IDs through unique same-label/same-source replacements and adds
ten IDs. **Zero nodes outside changed paths are lost**. The result is
**58,802 nodes / 112,580 links / 5,096 communities**, SHA-256
`59998310103dc5c221123715b0ab87be23a8fd471b514c025ebe2bed24b5a48a`.
The target node is refreshed to L492 and its same-file helper call is present.
The cross-file command-helper edge is absent, and a stale s32 return-type
reference at L421 remains despite the recovered void definition. Those are
scoped-graph limitations, not source/ABI evidence. Source, relocations and
connected execution are authoritative. The 31,816 nodes retained from 3,754
files outside the scan corpus are preservation evidence, not a fresh full
extraction. No graph package/policy change or hand-added call edge is made.

The final production audit rechecks all production hashes, the unchanged
guard manifest and progress CSV, all 98 frozen inputs and the complete caller
object. The next candidate is confirmed through the live nonexact list,
Graphify navigation and its complete original assembly before handoff.
