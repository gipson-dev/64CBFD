# Note 2605: Camera control-bit filter direct byte match

Date: 2026-11-21. Consumer baseline `a46acd51ae29cc92df2df09791162a591f3bcb13`;
tools baseline `0b07aef51228f96f9a78158186e0731f41865965`.
Qualified tools commit: `42c50ce3bf3f7e12f6d479d6d8852fd0acfb0138`.

`func_15125DB4` now contains its complete camera control-bit filter. Its **225
words / 900 bytes**, **48-byte frame**, saved S0/RA and nine relocation sites
emit directly from C with **zero guards, insertions or omissions**. Its interface
is `void func_15125DB4(struct108 *camera)`; the obsolete placeholder declaration
and comment are removed. All **44 neighboring functions**, constant pools and
the five existing compiler warnings remain unchanged.

Production recount: **4,589 / 5,528 (83.01%)** total, **3,916 / 4,855 (80.66%)**
Game, zero address drift and **939** still different. Init 492/492 and Debugger
181/181 remain exact. **110 more** are needed for 85% at this denominator.
Converted rows do not change because the former stub already counted as C.
The root README receives only its two aggregate matching rows.

## Recovered behavior

Owner `game_14FF90`; VA `0x15125DB4..0x15126138`, ROM
`0x153264..0x1535E8`. The routine filters the local halfword at camera+0x36A
and the linked halfword selected by camera+0x36C. It preserves their distinct
mask orders, repeated pointer reads, and the asymmetry between clearing 0x1C
locally and 0x0C in the linked halfword for one actor-state condition.

The state byte selects grouped activation, table fallback, low-bit clearing,
and state-0x29 activation. State 0x0F submits the original six-word event packet
`(3, 0x9000, 0x18, 0x25, 0x13, 480)`. Subsequent gates inspect the current actor,
state-object bytes, global disable state, camera flags and selector. The final
0x40 path decrements the signed halfword at +0x84A by the current tick word,
clears bit 0x10 in both halfwords, reloads the narrowed timer, and clamps a
nonpositive result to zero. Helper mutations remain visible to later reloads.

The timer remains inside unresolved SDK padding. A private
`CameraControlTimer14FF90` view names only its measured +0x84A offset and uses
GCC's `may_alias` attribute for the native qualification build. IDO ignores
that conditional attribute. Shared SDK headers and structure layouts are
unchanged; native offset/extent assertions check the actual SDK declarations.

## Qualification and limits

Raw payload SHA256:
`720c143410e332b327dc8ac863234b0e855774560bf389c26d8d58b990cc5e25`.
Raw C, independent retail assembly and the padded body have identical payloads
and relocation bindings. The normal mixed GLOBAL_ASM Make route runs all five
commands and reproduces the complete proposed object under existing O2/g3.

The independent guest memory model passes **9,840 cases per stream**, visiting
all 225 words in retail, raw C and padded C. It checks complete public RAM,
all modeled registers, ordered accesses, private frame/incoming storage,
provider clobbers/mutations, signed table indices and six linked-halfword
arrangements. Timer cases include signed-halfword edges and large tick words.
Five altered instruction controls fail. An added actor-state/mode combination
closes the initially missing duplicated branch-delay load in coverage.

Native SDK32 runs pass **5,772 cases each at O0/O2/O3** with strict aliasing,
UBSan traps and six effective source controls. These use actual SDK objects,
the explicit alias view, two legal linked-halfword arrangements, in-range
table indices and no promoted signed arithmetic overflow. Signed-halfword
narrowing follows the SDK/compiler representation. The first proposed
`<= 0` to `< 0` clamp control was behaviorally equivalent on zero; it was
rejected and replaced by `< -1`, which leaves a negative timer observable.
Native tests make no private-frame claim. Guest wrap/alias evidence is
separate from these defined native-object cases.

A fresh census of the original ROM and sealed ELF finds one JAL at
`0x15122E8C` in `func_15122C5C`, with no aligned loaded pointer literals.
Its **11-word original window** passes **192 cases per stream**, including the
actual argument delay slot, target return, state-pointer reload, byte tests,
and conditional bounded reset-provider call. Lost argument and missing pointer
reload controls fail. The returned V0 is overwritten by that real reload.
The full outer caller and reset implementation are not reconstructed here;
computed references are not excluded by an aligned census.

Six GNU links compare original bases and code+`0x10010` / data+`0x18020`,
including HI16/LO16 carry. The raw target is isolated with exact payload and
binding equality before its link; unused raw-owner data is outside that scope.
The full padded owner is covered by the natural Make and complete-image gates.

The strict predictor covers all **6,051 slots** with **736 declared changed
bytes, zero exclusions or unexplained differences**. Only the target body and
its symbol size, 16 to 900 bytes, change. All **189,088 protected Game-data
bytes across 720 owners** remain exact. Production ELF SHA256:
`ce6a3f84cccdb0401fb4980b6958b069ff1b1d0068ecb2e2ff3b0b8cf3ef7842`.

Both primary and private sibling configurations pass five focused checks
before and after installation, and shared `make tools-check` passes. The
direct conversion preserves other linked bodies/data/guards, so earlier broad
suites are not rerun or claimed fresh. The current complete owner/image audit
covers the changed dependency without exclusions. Seven new tools files are
committed before adoption. The private hybrid contains 1159 files;
the real dirty sibling HEAD/status and 351 dependency
hashes are preserved. The production audit checks 2283 frozen
baseline inputs. No compiler-profile, Makefile, guard or shared-header changes.

Graph retention preserves old IDs and qualification metadata. The native
smaller-corpus refusal and serial scoped merge do not establish a full corpus
re-extraction. The available host scene snapshot lacks its configured symbols;
no host parity or runtime behavior is inferred. These tests establish no
MMIO, interrupt, hardware or unrestricted C alias semantics. No host, Release,
ROM or save changes, no push, and zero Claude calls. The 85% goal remains active.

```sh
python3 -m unittest tools.tests.test_game_camera_control_flags_15125db4_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
