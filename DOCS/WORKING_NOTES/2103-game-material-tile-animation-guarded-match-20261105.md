# Animation-gated material tile callback recovered as guarded C

Date: 2026-11-05. Target `func_150D82BC`, owner `generated_105760`.
Source `conker/src/game/generated_105760.c`; original `conker/asm/105760.s`.

## Result and recovered contract

The complete **71-word / 284-byte** function matches retail with **no frame,
no alignment tail, four bindings and nine register-only guards**. Its VA is
`0x150D82BC..0x150D83D8`; ROM is `0x10576C..0x105888`. The eight other
functions in the compact and padded owner retain their bytes and bindings.
Existing O2/g3 compiler options remain unchanged.

The recovered signature is `s32 func_150D82BC(u8 *material, u8 *actor)`.
It reads the animation pointer at actor+0x2D0 and returns zero immediately
when absent. Otherwise it writes the low halfword of `D_80090298[6]`
(retail 0x0548) to material+0x18. Actor kind 13, read as an unsigned halfword
at +0x84, enables an inclusive 23..40 animation-time gate. An accepted time
selects table entry 7 (retail 0x0547), reloads the time, subtracts 23, and
multiplies by the existing `D_800A0B10` binary32 value 0x3D70F0F1.

The double indirection at material+0x24 supplies the display list. Its first
command byte 0xF2 identifies `G_SETTILESIZE`; the scan advances eight bytes.
The callback truncates `70 * fraction + 2` after the original binary32
operations. A negative offset adds the previous 12-bit coordinate; the
masked coordinate and fixed bits replace only the command's first word.
The second word and other commands remain unchanged. Every path returns zero.
As in the original, an active command stream must contain a terminating
0xF2 command. No arbitrary scan limit is invented.

Separate fraction assignments recover the original floating-register lifetime.
Updating the command cursor in place and retaining its signed word view give
the original arithmetic shift and instruction schedule. The source keeps
the live post-selection time reload, including guest aliases that change it.

## Nine closed register guards

The raw C body already has all 71 instruction positions. Nine expected-word
rows change only GPR fields at +0xCC, +0xD0, +0xD8, +0xE0, +0xE8,
+0xF0, +0xF4, +0xF8 and +0x10C. The command cursor moves V1 to A0;
the converted offset moves A0 to A3; the shifted/masked old coordinate moves
T5/T6 to T6/T7. Each definition and subsequent live use is covered before
the value dies. A2 remains the selected output coordinate. No opcode,
immediate, branch, memory-access position, floating operation or relocation
changes. All inherited manifest bytes are retained before the nine appended
rows. Natural emitted C and normalized matching are reported separately.

The compact `.reginfo` transition is explicitly checked:
`A300F9F6/00055DF0` to `A300FFFE/00075DF7` for its GPR/COP1 masks, with
every other byte fixed. All other allocatable compact sections and all
allocatable padded sections are identical. No compiler constant pool is added.

## Original caller and qualification

An aligned retail census finds no direct calls or tail jumps and exactly one
function-address literal: ROM 0x228C84, entry 1 of `D_800841C0`. The original
dispatcher in `func_15030468` reads material+7, indexes that table, passes
S1/S3 as material/actor, calls through T9 at 0x15030598, and copies the zero
result into S2 before 0x150305A4. The actual eleven-word dispatcher window
is connected to original, natural and padded target instructions for six
cases per body. This proves that boundary and result consumption, not the
complete parent renderer or gameplay.

All seven pre-install checks pass in **35.846 seconds**; all seven installed
checks pass in **40.558 seconds**. They include:

* **592 guest cases per body** covering null animation, unsigned kind,
  exact gate endpoints, adjacent floats, NaNs/infinities, command positions,
  both stack phases, coordinate masks and negative-scale overrides. Each
  arithmetic operation is rounded to binary32 in the independent reference.
* **Six aliases** and **43 fired memory-access cuts**. Original and padded
  instructions have identical complete fault state; natural C has identical
  ordered memory traces and RAM. A null animation completes with no mapped
  material, tables or display list. These are guest observations, not portable
  C fault/alias semantics or hardware-MMU acceptance.
* **Nine independent GNU links**, three text/data layouts and eighteen cases
  per body exercise all four HI16/LO16 bindings across carry boundaries.
* Native32 O0/O2/O3 pass **9,600 executions**, using a typed callback pointer,
  bounded aligned fixtures, UBSan, explicit first command bytes and disabled
  strict alias optimization for the recovered flat views. The native fixture
  honors native word byte order; it does not pretend that a little-endian
  command word has the N64's first-byte layout.
* **Ten native and ten separately compiled IDO negative controls** reject
  incorrect kind/endpoints/material entries, cursor, scale, negative branch,
  coordinate mask and return value. Every control has a fired witness.
* **284 raw-byte, four relocation and nine whole-image corruptions** fail
  closed. All 70 reachable words are visited. The duplicate table load at
  +0x1C follows the early return and stays statically exact but unreachable.

The nineteen shared padder, relocation, matcher and data-layout checks pass
in **14.462 seconds**; `make tools-check` passes. Unchanged neighbor suites
are reused through full byte/binding/data identity, not called fresh tests.
Routine work uses zero Claude calls and the documented IDO/GNU path under
the existing REA MIPS-adapter limitation.

## Production and immutable evidence

The immutable snapshot contains **98 inputs**, including all headers,
original target/caller/data assembly, retail ROM, source/object, manifest,
Makefile, linker, ELF, code binary, progress and graph. Artifacts remain in
`conker/build/game-material-tile-animation-150D82BC-match/`.
Main baseline is `22972da8acf7babc899ff6ec6b8fb43ad606a52a`; mounted tools
baseline is `271aa0867e4ab141c5be886a9add28f25fed2242`. Both start clean.
The sibling tools checkout is untouched; no fresh sibling qualification or
host-port Release change is claimed.

Actual Make's owner and complete ELF equal the independent prediction byte
for byte. All **6,052 function addresses** stay fixed; only this body changes.
All **189,088 protected bytes across 720 owners** remain exact. The literal
full-file prediction accounts for **234 changed ELF bytes**: 204 in the
target/12-to-284 symbol extent and 30 in two closed named symbol/string
permutations. At file 0x29F1DC the original four names
`D_800A0B10,D_800A02E0,D_8009FEE0,D_800A0F60` rotate left; at 0x2BE30C,
`D_80090298,D_800A6F98` exchange places. Every named definition is otherwise
identical. There are **zero excluded bytes**.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `cd537882e4bdcc4f58af8c59bb00d49e486d0a22dbde9cc57277d9806f038012` |
| Original target | `e9065d4c611170e40c9548a5efd4a6a6c7165c835187114e63b937b11ac95d73` |
| Production owner | `648810cd6fa2eaeac745a0c06e0759b6bf858dc551bfd89386815f84db0e46a6` |
| Complete ELF | `94f8cc66a05885e429df07ebdf25554d0143f3d4fd7803c5fbf62890aa9b6fdc` |
| Code binary | `c57f7c956a3a58e606e16cac5d0a1e960aa40d57fb1ee8438a7fe65a98c120e0` |
| Updated guard manifest | `892dcc21c80c8cc41c6970ed89c7f218e072b5a5487946d406a0d133e7f6d6d6` |

Actual Make performs the normal broader rebuild caused by the guard-file
dependency. `make -C conker all` produces the binary and returns 2 only at
the expected incomplete-project retail checksum mismatch. The inherited
duplicate generated_12D630 recipe warning is unchanged.

## Handwritten boundary and continuation

The preceding ranked candidate `func_150A70C0` is explicitly marked
handwritten in `asm/D4450.s`. Its complete 66-word span at
0x150A70C0..0x150A71C8 contains the global continuation `func_150A717C`
at +0xBC. The ordinary padder treats that label as a separate function,
dividing this outer span into 47 and 19 words. The routine uses odd FPR F19,
increments incoming T2, preserves its original pre-frame save and live-FCSR
`cvt.w.s` conversion. Its fifth argument is supplied by the delay-slot store
at the original `func_15177A94` call at 0x15177C20. The original span's
SHA-256 is `5161d4fce825896f34c41091cbf0012dcf66122ef35667aedb4f30d4d8d0a534`.
The read-only `handwritten-boundary.json` records this audit. Its placeholder
is unchanged and receives no C credit or denominator reclassification.

The fresh actual-ELF recount is:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,174 / 5,512 | 75.73% | 0 | 1,338 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,501 / 4,839 | 72.35% | 0 | 1,338 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory remains 5,512/6,046. Root README changes aggregate rows
only. The 80% threshold is 4,410, leaving **236 more** exact functions.
Next ordinary candidate is **func_1510FD20**. Retain eight separate boundaries:
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, `func_150A6760`, `func_150A70C0`.
Keep the wider 80% goal active.

Mounted tools are committed first as
`cc982da9f6a26c589f6ba3266f754e6a257e838a`
(`test(game): qualify material tile animation callback`). The consumer
records that pointer with the semantic C, nine register guards and notes.

The ordinary AST-only Graphify update refuses its smaller 24,962-node
replacement, preserving the existing 58,758-node graph. The seven-path
scoped refresh retains 58,755 old IDs, removes three relocated update-log
IDs and adds ten IDs. Every removed ID has a unique same-label/same-source
replacement; **zero nodes outside changed paths are lost**. The graph is
**58,765 nodes / 112,529 links / 5,276 communities**, SHA-256
`cfbeced95fd60c9495a9f254562e1df8bf62f8ced101527c8cfb3280e79a82ff`.
The 31,816 retained nodes from 3,754 files outside the current scan corpus
are preservation evidence, not fresh full-corpus extraction. No force
overwrite is used. Final receipt paragraphs add no headings; the final
scoped refresh verifies unchanged topology.
