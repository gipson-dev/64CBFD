# Game Actor Reference Coordinate Phase Match

Date: 2026-10-05. Starting HEAD: `09021a7a`, the banked
[actor-pass lifetime audit](1009-game-actor-pass-lifetime-audit-and-helper-handoff-20261005.md).

## Recovery And Match

Recover **`func_1502F3C8`**, the phase helper called by `func_1502BEE4` after
the captured actor updates. Its complete **50-word / 200-byte** slot at
**0x1502F3C8..0x1502F490**, ROM **0x5C878**, now matches retail. Frame:
**0x30**. Linked SHA-256:
`7670792f2767a44c1bd1f768d17ac4fda43fb43c49125f8cf7787e10d7fa7c0d`.

This is a **guard-normalized semantic C match**, not direct compiler output.
Default IDO emits 50 words with 16 differences. Sixteen expected-word and
relocation guards recover the fixed-address prelude and closed schedule.
No compiler override, insertion, omission, fake local padding or handwritten
instruction body is introduced. The `void(void)` signature replaces the false
zero-return placeholder; the caller's linked bytes remain unchanged.

The recovered 0x32C-byte layout view names only the fields this helper uses:
active word at +0, X/Y/Z floats at +0x14/+0x18/+0x1C, bound float at +0x180,
unsigned joint halfword at +0x19E and reference byte at +0x274. Existing
display/update views remain intact. The native fixture defines the end symbol
as the same array's +25 boundary, not an independently allocated object.

## Retail Contract

1. Freshly scan exactly the first 25 actor slots. A negative active word is
   active; a zero active word short-circuits the reference read. The reserved
   26th slot is not scanned, but can be referenced.
2. Skip zero references. For other bytes, use the one-based target
   `D_800CC2D0 + reference - 1`. No new range/null validation is added.
3. Copy the current +0x180 float into Y before calling `func_1502F490`.
4. Pass **five arguments**: referenced actor, X pointer, Y pointer, Z pointer
   and the zero-extended +0x19E joint. Argument five occupies SP+0x10.
5. After the call, reload both Y and +0x180. If Y is less than the bound,
   replace Y with the bound; otherwise copy Y into the bound. Do not cache
   the old bound across a callback or substitute a generic minimum/maximum.
6. Continue with a fresh activity/reference check for the next slot. A
   callback can activate or disable it. Restore saved registers and SP.

The actual 302-word transform helper's prologue confirms all five argument
homes and the full-word fifth-argument load at **0x1502F4D4**. Its owner is
still an unchanged zero-return placeholder. This caller recovery does not
qualify the transform's matrix/asset work or full gameplay.

## Guard Audit

| Offsets | Words | Change |
| --- | ---: | --- |
| +0x004..+0x02C | 11 | Save/constant-address prelude; retail's separate initial actor/base loads replace shared-base setup and an always-false fixed-bound entry comparison |
| +0x05C/+0x060/+0x064 | 3 | Independent Y store and Y/Z argument-address setup |
| +0x070/+0x0A4 | 2 | Close the S1/S2 base/end allocation swap at target construction and loop termination |

The entry comparison is not described as merely an instruction reorder:
the qualified domain has fixed addresses **0x800CC2D0** and **0x800D121C**,
separated by **25 * 0x32C**. Removing that impossible equality is valid for
this retail layout and the native same-array fixture. No dynamic/empty-array
API is claimed. Guards explicitly move HI16/LO16 relocation ownership,
including the two retail base initializations, rather than bake in linked
addresses. Altered expected instruction and relocation controls both fail
closed. All 34 unguarded words emit directly from C, including the complete
post-call float branch/stores and epilogue.

The patch CSV has **10622 unique rows**, SHA-256
`b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.
All previous **10606 rows** are structurally unchanged; only these 16 target
rows are appended. There are still no `func_1502BEE4` guards.

## Qualification Boundaries

The source driver screens 16 forms. The raw selected 50-word form, the raw
49-word do-loop control and retail are compared in complete guest traces.
Completed case groups are:

- **2048** reference-byte/joint/stack-phase cases: all 256 reference bytes,
  joint 0/1/0x8000/0xFFFF, both O32 stack phases. Out-of-table reference bytes
  qualify address/argument construction with an opaque callback, not target
  dereferences or a native out-of-array pointer domain.
- **1458** initial/result/fresh-bound/phase cases for finite values, both
  zero signs, infinities and IEEE NaN comparison-model values. Observed
  pre-call Y, final raw float bits and fresh bound reads are checked.
- One reserved-slot exclusion case and two live next-slot mutation cases.
- **32** connections to the actual retail transform's zero-table path. They
  execute its argument-home/fifth-word load and return through the real
  saved-register epilogue; nonzero transform-table paths remain unqualified.
- **300** three-way actor-pass/selector/dispatcher/coordinate-phase cases,
  retaining the caller's separate live scans and captured update queue.

That is **3841 completed three-way cases**, with full external memory/events
and restored saved GPR/SP checks. The phase also seeds and verifies saved
FPRs; the cached-bound negative control needs local FR=0 paired save/restore
support. The odd/high-word pairing was checked against the
[Ares FPU register implementation](https://raw.githubusercontent.com/ares-emulator/ares/master/ares/n64/cpu/interpreter-fpu.cpp).
The comparison fixtures **do not model FCSR flags, traps, subnormal handling
or legacy VR4300 NaN classification**. Native IEEE quiet-NaN behavior is not
claimed as complete N64 hardware exception parity.

The native 32-bit C fixture compares **82944** whole-record cases with an
independent indexed reference, including all padding, reserved actor storage,
callback ABI logs and live mutations. Native references stay within the
26-element array. The cached-bound and omitted-joint controls fail their
respective semantic/actual-callee ABI checks. The unreachable duplicate store
at **0x1502F464** is byte-exact but not an executed coverage claim; all other
49 retail words are covered across the matrices.

## Linked Audit And Progress

The before/after audit covers **6060 slots**: only `func_1502F3C8` changes,
with no added/deleted slots, address moves or length changes. `func_1502BEE4`
retains its hash and **109 differing words**; display scan, dispatcher and
selector remain intact. Build/progress/match-progress and tools checks pass.
Complete Init code **164048 bytes**, Init data/rodata **17376 bytes**,
Debugger **19800 bytes** and Game data **189088 bytes / 720 owners** remain
retail-exact.
Final focused helper/pass/dispatcher run: **30 tests in 99.051 seconds,
no skips**, against the rebuilt ELF. The complete actor, viewport, SDK,
resource, matching and tool regression corpus passes **332 tests in 374.293
seconds, no skips**. Tools and whitespace checks pass; all **2941** checked
relative links resolve across the eight current/working-note/README documents.

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3303 / 5463 (60.46%) | 0 | 2160 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2630 / 4790 (54.91%) | 0 | 2160 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

README changes only these aggregate exact/different counts. Conversion counts,
47 retained Init ASM routines and sibling sources/builds/saves/frozen Release
are unchanged. No host transplant or push is made.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_attachment_phase_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Follow-up: **`func_1502F948`**, the actor post-pass buffer-copy helper,
is now directly matched in [Note 1011](1011-game-actor-buffer-copy-direct-match-20261005.md).
The following allocator contract was the handoff used for that recovery.
The helper has 45 words / frame 0x28. The restored
[`allocate_memory`](../../conker/src/init_3C40.c) wrapper takes four `s32`
arguments and returns an `s32` address word. Retail passes
`D_800C4ED0[cachedId] << 6, 1, 1, 2`, then stores even a null result to
actor+0x1D8 before testing it. Preserve the +4 ID byte cached across allocation
while reloading the source at +0x1D4, destination at +0x1D8 and halfword
size table before `bcopy`. Allocation callbacks can change those live values;
do not cache them together with the ID. The caller's
maximum-depth spill/address lifetime/scheduling remains open; `func_1502F490`
and full transform/gameplay acceptance also remain separate work. The Game
goal remains active with 2160 differing C functions.
