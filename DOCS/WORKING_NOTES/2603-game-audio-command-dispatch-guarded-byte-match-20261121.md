# Note 2603: Audio script command dispatcher guarded byte match

Date: 2026-11-21. Consumer baseline `0bf115b79f929c33f8d000a6118587099c31cca6`;
tools baseline `64aa7580e13b3d78f8495f5a6554075066bcbae3`.
Qualified tools commit: `57b6b6a8c044c1fd00ddcc195141e4a0da990d00`.

`func_1509E730` now contains its complete semantic C body. Its **92 words /
368 bytes**, **32-byte frame**, saved S0/S1/RA and **17 relocation sites** match
retail through **80 checked normalization rows**. All four functions in
`conker/src/game/generated_CBAF0.c` are now restored; the three existing
neighbors retain their instructions and bindings. The owner comment describes
the recovered callbacks instead of calling them placeholders.

Production recount: **4,587 / 5,528 (82.98%)** total, **3,914 / 4,855 (80.62%)**
Game, zero address drift and **941** still different. Init 492/492 and Debugger
181/181 remain exact. **112 more** are needed for 85% at this denominator.
Converted rows are unchanged because the former zero-return stub counted as C.

## Behavior and interface

Owner `generated_CBAF0`, VA `0x1509E730..0x1509E8A0`, ROM
`0xCBBE0..0xCBD50`. The recovered interface is
`s32 func_1509E730(s32 handle, s32 command, s32 *packet)`.

The dispatcher masks handles to 12 bits and sends commands 0 through 6 to
the recovered Init audio-control helpers. It preserves the two script-layout
tests of `D_800D3840`: mode 5 supplies the extended fade/secondary-handle
arguments, while mode 3 supplies the explicit enable argument. Commands 3
and 4 propagate the helper result; the other recognized commands return one.
Unknown commands return zero without reading the packet.

The physical block order is **0, 2, 5, 1, 3, 4, 6**. The initial sequential-label
draft emitted the same instructions but had the wrong command table. It was
rejected before installation. All seven corrected compiler destinations are
independently checked against the retained table at `0x8009F3D0`. Its 28 bytes
and all other Game data remain unchanged. The compiler's four padding bytes
are not published. A scoped Makefile binding selects the retained table.

## Normalization and evidence

The default O2/g3 C body already has the correct length, frame, saved homes,
operations and helper arguments. IDO hoists `V0 = 0` into the switch-range
branch's delay slot. The closed transformation moves that compiled word into
the default block, rotates the intervening instructions, and adjusts local
branches and relocation positions. Every input instruction is retained once;
there are **zero insertions or omissions**. The emitter reads compiled C and
its bindings, and stores no output instruction words or retail payload.

Raw payload SHA256:
`7781565d57520a7af31c3d64a613b1452740b73d692ed77233786e078fa9f3b4`.
Normalized unbound SHA256:
`4dc69513a8cac5f89a4e97df5fc22f600e26e6e24e333a827291b5d170b3cf32`.

The structural comparison covers all **11 control-flow paths**. The complete
command partition is unsigned values below seven versus the default; the
only version predicates are equality to three or five. On valid paths the
early V0 assignment is dead before the provider contract defines its result.
On the default path the added shift writes only dead caller-saved T6. Ordered
effectful instructions and private-stack operations agree. Four proof defects
and three raw-payload defects reject.

Guest execution passes **7,446 cases per stream** for retail, raw compiled C
and normalized C, reaching all 92 words. It checks ordered public reads, full
public RAM, all 32 frame bytes and 12 incoming bytes, helper packets and the
saved ABI. The read-only compiler code table is compared under its proved PC
mapping. Five instruction/table defects reject. A fixture marker initially
overlapped the stack; the disjoint-range assertion and complete rerun pass.

Native SDK32 checks compile the complete owner at O0/O2/O3 with strict aliasing
and UBSan traps: **13,440 cases each**, with six effective source defects.
One backing array makes global/packet overlap defined in native C. The guest
checks private frames. The existing freestanding native recipe is used;
default GCC's unavailable multilib headers require no installation change.

The sole aligned pointer reference is `D_800884D4[9]` at ROM `0x22CFB8` /
VA `0x800884F8`; there are no direct calls. Both original registry-consumer
windows execute **432 cases per stream**: the 18-word varargs window at
`0x1509C0D8` and the 26-word interpreter window at `0x150AE12C`. Their actual
JALR, delay-slot argument/save operations and original return tails agree.
Four missing-transfer defects reject. These are bounded connected windows;
the whole outer callers remain unrecovered.

Independent GNU links at original bases and code+`0x10010` / data+`0x18020`
match all **704 owner text bytes** between original assembly and padded C.
Raw C agrees with independent binding and all seven compiler table entries;
the second link exercises HI16/LO16 carry.

## Production and history

Both padders agree on complete text, functions and relocations. The layout-only
padder lacks the seven original global case labels; adding only those proved
names and PCs makes its complete object identical to the natural assembly
padder. The production route retains that original namespace. Three actual
O2/g3 Make commands reproduce the qualified object.

The full-image predictor covers all **6,051 slots**: **321 declared changed
bytes, zero exclusions or unexplained bytes**. Besides the target and its
symbol size 12 to 368, GNU serialization swaps the adjacent `D_80099A24` and
`func_151F8960` records and their 25 name-string bytes. The complete definitions
are preserved by an explicit closed permutation. All **189,088 protected
Game-data bytes across 720 owners** remain exact. Production ELF SHA256:
`95909e0eee87ace336ec22f7c524c44213f82a61ed9d76fbe887dc803517a7ea`.

Primary and private sibling-tools configurations each pass **60 focused tests**
and **three historical full-image gates** before and after installation. That
includes nine new target checks, 36 previous projection/effect checks and 15
input/dependency checks. Historical manifests append exact contexts and object
overrides; all original snapshots and frozen fixtures remain intact. Reversible
AST audits preserve old source generation and the original historical linker.
Only a qualified source/guard pair plus exact source/Makefile context admits
the supplemental inputs. Historical images use private linker copies.

The final guest-tool edit removes only an extra blank line at EOF. The
pre-install receipt reuse is tied to both exact hashes and an identical AST;
both installed configurations rerun all checks against the final file bytes.

All 37 tools files are committed before consumer adoption. The private hybrid
contains 1142 files with {'task': 37, 'sibling': 347, 'bootstrap': 1, 'primary-fallback': 757}; the actual dirty
sibling HEAD/status and 351 dependency hashes are
preserved. The production audit checks 2247 original baseline
inputs plus supplemental caller/configuration snapshots. README changes are
limited to aggregate totals. Graph refresh retains existing IDs and metadata;
the scoped merge is not a full-corpus extraction.

The contracts assume mapped ordinary RAM disjoint from private stack, a
read-only code table and o32 providers observing defined arguments/public RAM.
They do not establish return-PC introspection, MMIO, faults, interrupts,
hardware or gameplay behavior. No host-port, Release, ROM or save changes.
The available sibling scene-recompile configuration consumes a code binary;
its configured symbol file is absent, and its saved input does not contain
this original function window. That snapshot establishes no host parity or
runtime applicability claim for the recovered C.
Zero Claude calls and no push. The 85% goal remains active.

```sh
python3 -m unittest tools.tests.test_game_audio_command_dispatch_1509e730_match -v
python3 -m unittest tools.tests.test_game_qualified_historical_inputs -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
