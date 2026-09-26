# Update Log

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-09-26

### Null-first table populator byte-exact

- Completed all 30 words of `func_15085B70` directly from source. Reversing
  the condition to test `temp_v0 == 0` places retail's compact zeroing path
  before the populated path and restores all thirteen differing words.
- The complete frame, both calls, delay slots, six global relocation pairs,
  branch targets, and epilogue are source-emitted and exact. No guarded rows
  were added.
- The patch table remains at 808 unique rows. Linked `0xB2FF0` and retail
  `0xB3020` share SHA-256
  `420680f426f2b1f2b80d4d03a344b7ca8de125e0cc9067820c2464ec5e5d5a19`.
  Fresh scan: **2615 / 5484 (47.68%)** overall and
  **2047 / 4795 (42.69%)** game, with debugger unchanged at **181 / 181**.

### Retained local-record pointer byte-exact

- Completed all 17 words of `func_1507FF94`. A volatile local pointer retained
  across the first call restores retail's 40-byte frame, pointer spill/reload,
  and complete function extent.
- The first call uses `&rec` directly while the second uses the retained local,
  avoiding the extra volatile load that overflowed the slot. Five guarded,
  non-relocating words finish the independent prologue setup order.
- The patch table now has 808 unique rows. Linked `0xAD414` and retail
  `0xAD444` share SHA-256
  `e4200d3dee6cba3505c9510b8b1bf1aec92d126dead87a84c041535655634e4f`.
  Fresh scan: **2614 / 5484 (47.67%)** overall and
  **2046 / 4795 (42.67%)** game, with debugger unchanged at **181 / 181**.

### Packed four-byte reader byte-exact

- Completed all 16 words of `func_1507A3E8`. The plain packed-byte expression
  remains the clearest source after prior local, term-order, accumulator, and
  volatile experiments all produced inferior schedules.
- Thirteen guarded words restore retail's adjacent address/load pairs and
  `t7` through `t9` merge lifetimes. All four global HI16/LO16 relocation
  pairs are explicitly validated and moved with their loads.
- The patch table now has 803 unique rows. Linked `0xA7868` and retail
  `0xA7898` share SHA-256
  `c542b461c15efeba5d814856ab3ff92fc74b2482448be8462a1718c97a228e9d`.
  Fresh scan: **2613 / 5484 (47.65%)** overall and
  **2045 / 4795 (42.65%)** game, with debugger unchanged at **181 / 181**.

### Chunked-boundary loop byte-exact

- Completed all 18 words of `func_15043B70` directly from source. Expressing
  the selected chunk as a scalar ternary restores retail's explicit two-arm
  merge and the unconditional branch missing from the prior object.
- That one recovered word realigns the initial exit, loop-back branch, and
  every subsequent instruction. No guarded patch rows or relocations apply.
- The patch table remains at 790 unique rows. Linked `0x70FF0` and retail
  `0x71020` share SHA-256
  `ba904403da942b5a2963e724bdcbec9cf4b4ec668ad4072fece06f24f09fefc2`.
  Fresh scan: **2612 / 5484 (47.63%)** overall and
  **2044 / 4795 (42.63%)** game, with debugger unchanged at **181 / 181**.

### Slot-cursor allocation byte-exact

- Completed all 19 words of `func_150356C8`. Reusing and incrementing the
  loaded slot byte directly restores retail's cursor base register and final
  store while preserving the full original control flow and extent.
- Nine guarded words restore the `t6`/`t7`/`t8`/`t9` arithmetic schedule and
  `t0` table base. The `D_800C3F08` high relocation remains at relative
  `0x10`; its paired low relocation moves from `0x18` to retail's `0x38`.
- The patch table now has 790 unique rows. Linked `0x62B48` and retail
  `0x62B78` share SHA-256
  `ce94daa79799e73dfcc4b67025fc8e51fcb016d97ee6964f07a39a20f6c3b44c`.
  Fresh scan: **2611 / 5484 (47.61%)** overall and
  **2043 / 4795 (42.61%)** game, with debugger unchanged at **181 / 181**.

### Relative-offset tree walk byte-exact

- Completed all 39 words of `func_15002560`. An explicit infinite loop with a
  top null exit restores retail's unconditional loop-back edge. Materializing
  the optional sibling offset in one scalar before its halfword store restores
  eleven additional control-flow and `t7`/`t8`/`t9` schedule words.
- Two guarded, non-relocating words select retail's base-first operand order
  for the child and sibling pointer additions. The recursive call relocation
  remains source-emitted and exact.
- The patch table now has 781 unique rows. Linked `0x2F9E0` and retail
  `0x2FA10` share SHA-256
  `38e72a9437314876eb11b824d041a92158c88f2856a50f2a371ab8c5ec554f8f`.
  Fresh scan: **2610 / 5484 (47.59%)** overall and
  **2042 / 4795 (42.59%)** game, with debugger unchanged at **181 / 181**.

### Signed-byte fallback selector byte-exact

- Completed all 18 words of `func_151E5FAC`. Duplicating the explicit fallback
  return restores separate flag-false and threshold-failure paths; spelling the
  threshold as `>= 5` restores retail's positive branch to the candidate.
- Twelve guarded words restore retail's fallback-address preload/rematerialize
  schedule and move the `D_8008FD8C` and `D_8008FD90` relocation pairs. The
  flag load, final fallback load, and return are unguarded and exact.
- The patch table now has 779 unique rows. Linked `0x21342C` and retail
  `0x21345C` share SHA-256
  `6b4a87b0141da6aebe6c6d4e3a60eefa444d170d0fdf07689f40e48da5d1f7ff`.
  Fresh scan: **2609 / 5484 (47.57%)** overall and
  **2041 / 4795 (42.57%)** game, with debugger unchanged at **181 / 181**.

### Allocation/copy wrapper byte-exact

- Completed all 28 words of `func_15168800` directly from source by expressing
  allocation failure as an explicit early null return before `bcopy`.
- That control-flow shape restores retail's positive branch into the copy
  path, explicit zero-return delay slot, retained allocation in `v1`, stack
  spill across `bcopy`, and both call relocations. No guarded rows were added.
- The patch table remains at 767 unique rows. Linked `0x195C80` and retail
  `0x195CB0` share SHA-256
  `163d065da4eac9216fff364ccc3d94c87935a63389ba18289abde3a2eef4f5f7`.
  Fresh scan: **2608 / 5484 (47.56%)** overall and
  **2040 / 4795 (42.54%)** game, with debugger unchanged at **181 / 181**.

### Duplicate masked-field store byte-exact

- Completed all 40 words of `func_151355B8`. Volatile-qualified accesses to
  the masked field retain retail's duplicate store and directly restore every
  shifted exit-branch target.
- Chained assignment still collapsed to one store. A split loaded-value local
  selected worse registers, while a volatile pointer local emitted the same
  object as direct volatile accesses. Five guarded, non-relocating words select
  retail's `t5` loaded value and `t6` masked result.
- The patch table now has 767 unique rows. Linked `0x162A38` and retail
  `0x162A68` share SHA-256
  `905987a8e0bd8c6da95744f53d6707165b266566a5e67456208c2d84e35d4f97`.
  Fresh scan: **2607 / 5484 (47.54%)** overall and
  **2039 / 4795 (42.52%)** game, with debugger unchanged at **181 / 181**.

### Three-word aggregate forwarder byte-exact

- Completed all 20 words of `func_15131D4C` directly from source by replacing
  three scalar assignments with a typed three-word aggregate copy and declaring
  the callee's first argument as a pointer.
- The aggregate copy alone restored retail's interleaved `lw`/`sw` sequence
  but formed the stack destination in `v0`, making the function one word too
  large. The corrected pointer contract lets IDO form it directly in `a0` and
  restores the complete retail schedule with no guarded rows.
- The patch table remains at 762 unique rows. Linked `0x15F1CC` and retail
  `0x15F1FC` share SHA-256
  `0c3949fd9d561f5442219ef46c00c7ce47d53bf0a05c7263f3e0ff7e392891f0`.
  Fresh scan: **2606 / 5484 (47.52%)** overall and
  **2038 / 4795 (42.50%)** game, with debugger unchanged at **181 / 181**.

### Optional-pointer call wrapper byte-exact

- Completed all 18 words of `func_150E33CC`. Direct dereference, shared-result
  local, and preassigned-selector source probes did not reproduce retail's
  schedule and were reverted.
- Twelve guarded words restore retail's `v0` pointed-value lifetime, early
  selector materialization, zero path, call-delay `a1` move, and epilogue.
  The `func_1000E7A0` relocation moves explicitly from relative offset `0x28`
  to `0x2C`. The frame and final padding word were already exact.
- The patch table now has 762 unique rows. Linked `0x11084C` and retail
  `0x11087C` share SHA-256
  `4e11e68c67960b22b570a25feb7aaff4c509e19a21d120d7eb328c4e489d276a`.
  Fresh scan: **2605 / 5484 (47.50%)** overall and
  **2037 / 4795 (42.48%)** game, with debugger unchanged at **181 / 181**.

### Bounds-checked halfword getter byte-exact

- Completed all 16 words of `func_1508B194` by expressing the bounds check as
  retail's early-zero path. This directly restored the positive branch,
  branch delay slot, explicit zero return, halfword-load position, and final
  return sequence.
- Five guarded words select retail's `t7` record-table base and `t8` 12-byte
  stride while explicitly moving the `D_8008FDD4` HI16 relocation. The
  `D_8008FD90` relocation pair was already exact. The patch table now has 750
  unique rows. Linked `0xB8614` and retail `0xB8644` share SHA-256
  `3b86be0e704bd4067e9efad6096d883a46966c5626da1fb6476ed2dafbb9b1ee`.
  Fresh scan: **2604 / 5484 (47.48%)** overall and
  **2036 / 4795 (42.46%)** game, with debugger unchanged at **181 / 181**.

### Indexed signed-byte getter byte-exact

- Completed all 13 words of `func_150882B0` by declaring the global pointer
  before the retained index, reusing `arg0` for the final record pointer, and
  guarding the remaining ten schedule positions. Retail now preserves the
  index in `a1`, keeps `D_800872A0` in `v1`, and loads through final `a0`.
- The moved `D_800872A0` HI16/LO16 pair is explicitly guarded. The patch table
  now has 745 unique rows. Linked `0xB5730` and retail `0xB5760` share SHA-256
  `7c3ea120c159b30ba557ad53b2e8ab7720ec13bb50a7daebf4f56f9d93ed63c4`.
  Fresh scan: **2603 / 5484 (47.47%)** overall and
  **2035 / 4795 (42.44%)** game, with debugger unchanged at **181 / 181**.

### Three-byte record update byte-exact

- Completed all 46 words of `func_1504BA38` with twelve guarded words that
  restore retail's `v1` record pointer, `a1` byte-two value, and `v0` byte-one
  value. The arithmetic, branches, stores, floating-point conversions, and
  both existing global relocation pairs were already correctly positioned.
- The patch table now has 735 unique rows. Linked `0x78EB8` and retail
  `0x78EE8` share SHA-256
  `f6b31137a29e73ab755499f92e5ae0090afb835db155431476753cb081e410b4`.
  Fresh scan: **2602 / 5484 (47.45%)** overall and
  **2034 / 4795 (42.42%)** game, with debugger unchanged at **181 / 181**.

### Timed toggle/table update byte-exact

- Completed all 21 words of `func_150337E4` by replacing its accumulated-value
  and table-index locals with direct field expressions. IDO now emits retail's
  `t8` accumulated counter, `t0`/`t1` toggle pipeline, and `t2`/`t4` table
  pipeline directly from C.
- No guarded rows were added; the patch table remains at 723 unique rows.
  Linked `0x60C64` and retail `0x60C94` share SHA-256
  `54b59cd622a7bc63daf39021633dca3bfe362e4cf2812761b2aa81f4273bac76`.
  Fresh scan: **2601 / 5484 (47.43%)** overall and
  **2033 / 4795 (42.40%)** game, with debugger unchanged at **181 / 181**.

### Mirrored counter/table update byte-exact

- Completed all 20 words of `func_15031E2C` with twelve guarded register-choice
  words after declaration, assignment, and K&R/ANSI source probes produced the
  same stable object. The guards recover retail's `v1` counter, `v0` mirrored
  index, `t9` increment, and `t8` table-value pipeline.
- The two table-address guards preserve the `D_800902BC` HI16/LO16 relocation
  pair. The patch table now has 723 unique rows. Linked `0x5F2AC` and retail
  `0x5F2DC` share SHA-256
  `d1fcfc04e9e799d2864afd8d204547594fe1f79d94eba637d63fe84656099ddf`.
  Fresh scan after this two-function pass: **2600 / 5484 (47.41%)** overall and
  **2032 / 4795 (42.38%)** game, with debugger unchanged at **181 / 181**.

### Table sum loop byte-exact

- Completed all 19 words of `func_1501CFF8` by ordering the sum/index locals
  before directly testing `D_800C363A[arg0]` at entry and on the loop back edge.
  IDO reuses one byte load while preserving retail's `a1` count, `v0` index,
  `v1` sum, and `slt`/`bnez` loop test.
- No guarded rows were added for this function. Linked `0x4A478` and retail
  `0x4A4A8` share SHA-256
  `5e8669328165c7bbc1972b40dfe5c9162102aff28a9088f06f5276ee387ee090`.

### Conditional minimum update byte-exact

- Completed all 16 words of `func_151ACA20` by declaring the output candidate
  before the signed-halfword source and expressing four-bit scaling as one
  signed assignment. IDO now emits retail's `v1` source and `v0` candidate
  lifetimes, both branch-likely delay slots, store, and return schedule.
- No guarded rows were added; the patch table remains at 711 unique rows. The
  linked span at `0x1D9EA0` and retail span at `0x1D9ED0` share SHA-256
  `2650fd7f0a4ea8c62ed6c2de28b52fbf4bac60fc9924be173f872ad030eb954a`.
  Fresh scan: **2598 / 5484 (47.37%)** overall and
  **2030 / 4795 (42.34%)** game, with debugger unchanged at **181 / 181**.

### Byte lookup forwarding wrapper byte-exact

- Completed all 15 words of `func_15178E14` by replacing its K&R definition
  with an ANSI byte parameter and giving both local callees their actual
  argument contracts. IDO now emits retail's narrowing, first-call nop delay
  slot, forwarded-result delay slot, and complete epilogue directly from C.
- No guarded rows were added; the patch table remains at 711 unique rows. The
  linked span at `0x1A6294` and retail span at `0x1A62C4` share SHA-256
  `a019d616adcd1685df8d90af91eb0c6da92463538aeeb540adf85fd4e9ccbbfd`.
  Fresh scan: **2597 / 5484 (47.36%)** overall and
  **2029 / 4795 (42.31%)** game, with debugger unchanged at **181 / 181**.

### Position and phase update byte-exact

- Completed all 28 words of `func_15141564` by expressing its position update
  in multiplication-first order and guarding the two residual base-pointer
  spill/reload slot words. The source change restores retail's frame and both
  FP-register pipelines; no relocation or instruction position changes.
- The patch table now has 711 unique rows. The linked span at `0x16E9E4` and
  retail span at `0x16EA14` share SHA-256
  `364192b03df56b95681c27fb0a27b22cdeacb071d6a9a462c1b4a07bcb72364b`.
  Fresh scan: **2596 / 5484 (47.34%)** overall and
  **2028 / 4795 (42.29%)** game, with debugger unchanged at **181 / 181**.

### Two-word aggregate call byte-exact

- Completed all 17 words of `func_151090DC` by replacing two scalar stack
  assignments with a typed two-word aggregate initializer and passing the
  aggregate through the callee's pointer ABI. IDO now emits retail's complete
  aggregate-copy and argument schedule directly from C.
- No guarded rows were added; the patch table remains at 709 unique rows. The
  linked span at `0x13655C` and retail span at `0x13658C` share SHA-256
  `55ddb338289c96218fdbd1278286280acc0413a16f923996dfc3be3651ad8e9a`.
  Fresh scan: **2595 / 5484 (47.32%)** overall and
  **2027 / 4795 (42.27%)** game, with debugger unchanged at **181 / 181**.

### Record activation loop byte-exact

- Completed all 17 words of `func_150B6D34` by simplifying its cursor loop and
  guarding nine residual cursor/record-pointer register choices. The three
  address-setup guards explicitly preserve or move the corresponding
  `D_800D9898` and `D_800D98A4` relocations.
- The patch table now has 709 unique rows. The complete linked span at
  `0xE41B4` and retail span at `0xE41E4` share SHA-256
  `03ce6560ee0992ce0939368415ac8387c68e5cac8aa8022d68bc01deea2f1124`.
  Fresh scan: **2594 / 5484 (47.30%)** overall and
  **2026 / 4795 (42.25%)** game, with debugger unchanged at **181 / 181**.

### Five-byte queue shift byte-exact

- Completed all 15 words of `func_1507EEB8` by replacing five scalar byte
  assignments with the original fixed reverse loop. IDO now emits retail's
  `arg1 + 4` induction pointer, unrolled load/store order, and final new-byte
  store directly from C.
- No guarded rows were added. The patch table remains at 700 unique rows. The
  complete linked span at `0xAC338` and retail span at `0xAC368` share SHA-256
  `bec0e721180c79c0dfb9915789558fbb481fe906c5fee1e835496f9727260b1f`.
  Fresh scan: **2593 / 5484 (47.28%)** overall and
  **2025 / 4795 (42.23%)** game, with debugger unchanged at **181 / 181**.

### Interpolation register match byte-exact

- Completed all 58 words of `func_15074A94` by expressing the interpolation as
  one factor-times-distance calculation and guarding eleven residual
  floating-point register choices. The three patched constant loads retain
  their original relocations, and no words or relocations move.
- Added `retail_word_patches.us.csv` as an explicit prerequisite of both
  hand-maintained padded-object rules. The subsequent complete invalidation and
  rebuild passed, proving all current expected-word guards against fresh
  compiler output instead of potentially stale objects.
- The patch table now has 700 unique rows. The complete linked span at
  `0xA1F14` and retail span at `0xA1F44` share SHA-256
  `4b85cc9681ac9d582b3f068553382b892a04d8c7201c789e79347a5ba4cbfc86`.
  Fresh scan: **2592 / 5484 (47.26%)** overall and
  **2024 / 4795 (42.21%)** game, with debugger unchanged at **181 / 181**.

### Local-record pointer schedule byte-exact

- Completed all 20 words of `func_150717E0` through eleven guarded schedule
  words. Retail preserves the local-record pointer at `sp+0x18` across the
  first call; the current compiler rematerializes `sp+0x20`. The guards restore
  that pointer lifetime, both call positions and relocations, delay slots, and
  epilogue order without inserting words.
- The patch table now has 689 unique rows. The complete linked span at
  `0x9EC60` and retail span at `0x9EC90` share SHA-256
  `6cb1079ed02c68652e32fb90cad0f0e18cc65a1ed4deec89e7af75b236fe2d7a`.
  Fresh scan: **2591 / 5484 (47.25%)** overall and
  **2023 / 4795 (42.19%)** game, with debugger unchanged at **181 / 181**.

## 2026-09-25

### Record-construction order byte-exact

- Completed all 34 words of `func_151D74B0` by moving the record pointer
  assignment ahead of its three byte fields. This restores retail's pointer
  store before the remaining byte and stack-argument loads and closes the
  ten-difference game tier without guarded rows.
- The patch table remains at 678 unique rows. The complete linked span at
  `0x204930` and retail span at `0x204960` share SHA-256
  `002a8c708dffc31c8235fae006313e893a65b893b7ffcc3e730a65a2ec243d01`.
  Fresh scan: **2590 / 5484 (47.23%)** overall and
  **2022 / 4795 (42.17%)** game, with debugger unchanged at **181 / 181**.

### Seven-argument wrapper byte-exact

- Completed all 19 words of `func_151581D8` through ten guarded prologue and
  argument-preparation schedule words. Every value, stack slot, call
  relocation, delay-slot store, and epilogue instruction was already present;
  the guards move no relocations and insert no words.
- The patch table now has 678 rows with no duplicate keys; this function has
  ten rows and no insertion-bearing rows. The complete linked span at
  `0x185658` and retail span at `0x185688` share SHA-256
  `0792b2f5cacd300b78d1eda3584b4422de9d312ba57cc4a943b7be7af3efd4be`.
  Fresh scan: **2589 / 5484 (47.21%)** overall and
  **2021 / 4795 (42.15%)** game, with debugger unchanged at **181 / 181**.

### Two-word record forwarder byte-exact

- Completed all 18 words of `func_15133E3C` by replacing two scalar array
  assignments with a `TwoWord15F680` aggregate initializer and correcting
  `func_15169260`'s first parameter to `void *`. This restores retail's
  direct `a0` local address, `at`/`t9` copy, and call-delay store from C.
- No guarded rows were added. The patch table remains at 668 unique rows.
  The complete linked span at `0x1612BC` and retail span at `0x1612EC` share
  SHA-256
  `edc82dab6f11e3d95b78955ef9d2bb24d4330125fc2decc6f04d9861724ebd28`.
  Fresh scan: **2588 / 5484 (47.19%)** overall and
  **2020 / 4795 (42.13%)** game, with debugger unchanged at **181 / 181**.

### Float-state reset byte-exact

- Completed all 17 words of `func_15133A50` by naming the pending sum,
  restoring retail's field-store order, and guarding the remaining nine
  `f0`/`f2`/`f8` register words. The guards move no relocations, insert no
  words, and change no addresses or control flow.
- The patch table now has 668 rows with no duplicate keys; this function has
  nine rows and no insertion-bearing rows. The complete linked span at
  `0x160ED0` and retail span at `0x160F00` share SHA-256
  `d46c11f94cffe15df0b700b643efd7c5844f60926746c7f45c7fb8c409ef7705`.
  Fresh scan: **2587 / 5484 (47.17%)** overall and
  **2019 / 4795 (42.11%)** game, with debugger unchanged at **181 / 181**.

### Repeated float-scale loop byte-exact

- Replaced the zero-return `func_151318E8` placeholder with retail's
  `D_800BE9E4`-counted multiplication loop. Its typed mixed pointer/float ABI
  emits the retail `mtc1 a1,f12` entry, while caller `func_151316AC` remains
  independently byte-exact.
- No guarded rows were added. The target linked/retail spans share SHA-256
  `dd1732f04e8fad0d5daed64f7a9833097445188e8d285d53da86220914bb350b`,
  and the caller spans share
  `22cb90341b57ea50023850f7cab38aaca0afbf2da61e0637c62336feffc0198e`.
  The patch table remains at 659 unique rows. Fresh scan:
  **2586 / 5484 (47.16%)** overall and **2018 / 4795 (42.09%)** game, with
  debugger unchanged at **181 / 181**.

### Short-circuit threshold update byte-exact

- Completed all 19 tracked words of `func_150DE2C4` by combining two
  equivalent field clears under one logical-OR condition. This restores
  retail's branch-likely delay-slot clear, shared second clear, and trailing
  padding directly from C, with no guarded rows.
- The patch table remains at 659 rows with no duplicate keys and no row for
  this function. The complete linked span at `0x10B744` and retail span at
  `0x10B774` share SHA-256
  `fc341f80de7976c7bcfee30c55345917dd6461764c3c1015adf431f8ad893c4b`.
  Fresh scan: **2585 / 5484 (47.14%)** overall and
  **2017 / 4795 (42.06%)** game, with debugger unchanged at **181 / 181**.

### Global-coordinate update byte-exact

- Completed all 28 words of `func_150CF578` by naming the loaded
  `D_800BE9E4` value before deriving the 28-times temporary. This restores
  retail's `v0` source lifetime, `v1` product lifetime, and instruction
  schedule directly from C, with no guarded rows.
- The patch table remains at 659 rows with no duplicate keys and no row for
  this function. The complete linked span at `0xFC9F8` and retail span at
  `0xFCA28` share SHA-256
  `9380ec55443833e5ed9950f30c40317a0bd33d130dbcba4a2a34e2aa36427898`.
  Fresh scan: **2584 / 5484 (47.12%)** overall and
  **2016 / 4795 (42.04%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor and state-byte clear byte-exact

- Completed all 15 words of `func_15096934` with an independent nine-row
  application of the generated-slice cursor expansion. It preserves the
  original cursor in `v1`, emits the `D_80087408` command pair, advances the
  cursor, clears byte `D_800D2DAB`, and restores the retail return sequence.
- All four moved relocations are explicitly guarded. The patch table now has
  659 rows with no duplicate keys; this function has nine rows and two
  insertion-bearing rows.
- The complete linked span at ELF `0xD6934` and retail `0xC3DE4` shares
  SHA-256
  `0ce9e94a848eba73ef07a221cf21947ea38ba900526bc53580d4a1f9417ea7ed`.
  Fresh scan: **2583 / 5484 (47.10%)** overall and
  **2015 / 4795 (42.02%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor and state clear byte-exact

- Completed all 12 words of `func_15094F40` through the established
  generated-slice cursor expansion. Nine guarded rows preserve the original
  cursor in `v1`, restore retail's command-store and global-clear schedule,
  and insert the advanced-cursor copy plus final return delay slot.
- All four moved relocations are explicitly guarded. The patch table now has
  650 rows with no duplicate keys; this function has nine rows and two
  insertion-bearing rows.
- The complete linked span at ELF `0xD4F40` and retail `0xC23F0` shares
  SHA-256
  `989b94637e932e7057eebd6fad9b2ef29c52742fc6ad60b41c25aa1e85b783b1`.
  Fresh scan: **2582 / 5484 (47.08%)** overall and
  **2014 / 4795 (42.00%)** game, with debugger unchanged at **181 / 181**.

### Linked-list search byte-exact

- Completed all 16 words of `func_15033E84` by loading `node->next` before
  the type comparison and assigning `node = next` in the loop condition.
  This recovers retail's preloaded `v0` next pointer, ordinary comparison and
  loop branches, and `move v1, v0` branch-delay update directly from C.
- No guarded rows were added; the patch table remains at 641 rows with no
  duplicate keys. The complete linked span at ELF `0x73E84` and retail
  `0x61334` shares SHA-256
  `944012697ea2666086f345f59f6c1cd8f750eb86b20835a40aa096bbae61d6c8`.
- Fresh scan: **2581 / 5484 (47.06%)** overall and
  **2013 / 4795 (41.98%)** game, with debugger unchanged at **181 / 181**.

### Packed-byte writer byte-exact

- Completed all 17 words of `func_1502EA0C` with ten guarded scheduling and
  register words. The C already expresses the four byte fields and packed
  32-bit value correctly; the guards recover retail's shift/store interleave
  and temporary lifetimes without changing control flow or relocations.
- Explicit partial-value locals did not change IDO allocation. Volatile stores
  improved byte-store order but increased the total differing words, so that
  experiment was rejected. The patch table now has 641 rows with no duplicate
  keys.
- The complete linked span at ELF `0x6EA0C` and retail `0x5BEBC` shares SHA-256
  `99bafbd40986e990628a4a760a04fedeb2eabda80b5ecd0355427dd6a209a1aa`.
  Fresh scan: **2580 / 5484 (47.05%)** overall and
  **2012 / 4795 (41.96%)** game, with debugger unchanged at **181 / 181**.

### Four-word state clear byte-exact

- Replaced the `func_151E81EC` placeholder with a real four-word state clear
  and byte reset. A local struct and chained assignment preserve all five
  stores, retail order, the 10-word extent, and the correct `void` return.
- Six guarded relocation words recover retail's two shared `$at` high halves.
  The patch table now has 631 rows with no duplicate keys. The complete linked
  span at ELF `0x2281EC` and retail `0x21569C` shares SHA-256
  `8ffd94c76c5a73aa7b0eaa0be788a471eb78a68224cc3b6365c6ce6666ddd16d`.
- Fresh scan: **2579 / 5484 (47.03%)** overall and
  **2011 / 4795 (41.94%)** game, with debugger unchanged at **181 / 181**.

### Indexed signed-byte selector byte-exact

- Completed all 18 words of `func_151E5F64` by expressing the enabled lookup
  as the positive branch and leaving the disabled `return arg0` path last.
  IDO now reproduces retail's two return sites, non-likely signed clamp, and
  exact branch layout directly from C.
- No patch rows were added. The patch table remains at 625 rows with no
  duplicate keys. The complete linked span at ELF `0x225F64` and retail
  `0x213414` shares SHA-256
  `0beb65faa2a495c68f3866e3915fa51747ea7149656f30e71e53a1a6828cdace`.
- Fresh scan: **2578 / 5484 (47.01%)** overall and
  **2010 / 4795 (41.92%)** game, with debugger unchanged at **181 / 181**.

### Callback selector twin byte-exact

- Completed all 33 words of `func_151963B4` with its own nine guarded
  pointer/selector register words. The structure matches `func_15196330`, while
  the independently preserved final relocation targets `func_15147928`.
- The patch table now has 625 rows with no duplicate keys. The complete linked
  span at ELF `0x1D63B4` and retail `0x1C3864` shares SHA-256
  `cf3ff8a08a41e22809847c2dccc1abd13cd671b7db20372f07d2575926cd3adf`.
- Fresh scan: **2577 / 5484 (46.99%)** overall and
  **2009 / 4795 (41.90%)** game, with debugger unchanged at **181 / 181**.

### Callback selector registers byte-exact

- Completed all 33 words of `func_15196330` with nine guarded words rotating
  the retained record pointer into `v0` and both signed callback selectors into
  `v1`. Its frame, branches, table dispatches, final call, and relocations were
  already exact.
- Separate declarations and a widened selector did not change allocation;
  reversed declarations moved the spill slot and were rejected. The patch
  table now has 616 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `8661611d0a0313dbe6f9307ad9d011fdeda11efe9b9a69fd63b2fefd45d67efb`.
  Fresh scan: **2576 / 5484 (46.97%)** overall and
  **2008 / 4795 (41.88%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor twin byte-exact

- Completed all 14 words of `func_15166FD8` with eight guarded transformations
  preserving the original cursor in `v1`, resolving `D_80089470` before the
  command constant, storing through `v1`, and returning the advanced cursor.
- Its typed `Gfx` source was already correct. The established generated-slice
  insertion path restores the two IDO-elided lifetime words while guarding the
  moved `R_MIPS_LO16` relocation. The patch table now has 607 rows and no
  duplicate keys.
- The independent complete-span SHA-256 is
  `4905a240f582ba884f83a2b6ab96c6f6109fbf5a5d54ce9e50a382b3f95c8ef3`.
  Fresh scan: **2575 / 5484 (46.95%)** overall and
  **2007 / 4795 (41.86%)** game, with debugger unchanged at **181 / 181**.

### Record-stride register lifetimes byte-exact

- Completed all 16 words of `func_1512D6B0` with nine guarded words selecting
  retail's `t7` index, `t6` global base, and `t8` 176-byte record offset.
  Control flow, field loads, equality reduction, and padding were already
  exact.
- An explicit-local source experiment spread the same values into argument
  registers and was reverted. The patch table now has 599 rows with no
  duplicate keys.
- The independent complete-span SHA-256 is
  `3266b541de99bd06941b770d4b38988db458dab3e62d8deb16339a6f96df436a`.
  Fresh scan: **2574 / 5484 (46.94%)** overall and
  **2006 / 4795 (41.84%)** game, with debugger unchanged at **181 / 181**.

### Display-list cursor expansion byte-exact

- Completed all 15 words of `func_1510E634` using the established typed `Gfx`
  writer idiom and eight guarded rows. Two rows insert the missing preserved
  cursor and return-delay words; the remaining rows restore retail's address,
  command, store, cursor-advance, and return schedule.
- Extended `pad_generated_object.py` to support bounded `insert_after` words,
  including retail-span accounting and shifted jump-label emission. All five
  padding-tool tests pass, including the new generated insertion fixture.
- The independent complete-span SHA-256 is
  `28d8bacba51037d5bdf8db9e479119ce8122427682c41a509a427bc6079ec25e`.
  The patch table has 590 unique rows. Fresh scan: **2573 / 5484 (46.92%)**
  overall and **2005 / 4795 (41.81%)** game, with debugger unchanged at
  **181 / 181**.

### Chained global clear byte-exact

- Completed all ten words of `func_15080200` by expressing its three zero
  stores as one chained assignment. IDO now retains `v0` and `v1` addresses
  for the first two globals and emits the retail store order naturally.
- Explicit local pointer variables were optimized back into three direct
  stores and were rejected. No guarded patch rows were needed; the table
  remains at 582 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `5fe7f7f6c8dc160faba47b5b2a363a0d7a7ca5dadc9982da1e3fe41d9141e7b6`.
  Fresh scan: **2572 / 5484 (46.90%)** overall and
  **2004 / 4795 (41.79%)** game, with debugger unchanged at **181 / 181**.

### Argument-load schedule byte-exact

- Completed all 41 words of `func_150771F0`. Inlining the selector expression
  into the five-argument call improved IDO's argument preparation; nine
  expected-word guards finish retail's `a2`/`a3` loads, two-arm `a1`
  selection, and delayed actor-pointer load.
- Eight of the guarded rows explicitly validate and move symbol relocations.
  The patch table now has 582 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `735443235523748393545106b44ca5886db042803279aa7dc842704ff00d72f8`.
  Fresh scan: **2571 / 5484 (46.88%)** overall and
  **2003 / 4795 (41.77%)** game, with debugger unchanged at **181 / 181**.

### Global PRNG step restored to assembly

- Restored `func_151EF610` to its original 12-word assembly ownership. Its C
  model computes the same recurrence, but IDO retains one global address and
  stores before return; retail uses independent load/store relocations and a
  store in the `jr ra` delay slot.
- Explicit-return and volatile-declaration source variants retained the same
  address lifetime. Omitting the return grew the body and returned the wrong
  value, so that experiment was rejected.
- The independent complete-span SHA-256 is
  `7fa144078d7821335feae3ad8e5f7953424f200288ed27731c1764cd45f04606`.
  The patch table remains at 573 unique rows with no row for this function.
  Fresh scan: **2570 / 5484 (46.86%)** overall and
  **2002 / 4795 (41.75%)** game, with debugger unchanged at **181 / 181**.

### Third dead child-pointer family member restored to assembly

- Restored `func_151AB180` to its original 17-word assembly ownership. Like
  `func_150C5EFC` and `func_150C682C`, IDO removes retail's otherwise dead
  `addiu v0,v0,0x58` and shifts the following call relocation.
- The preserved body retains its distinct `+0x70` child-field clear, the
  original `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay
  store. The patch table remains at 573 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `4f98b42bf797016c7e59eee9047f9777c22dbeb51ca0946889bd3b450758683f`.
  This is an ownership correction, so the exact numerator remains **2570**;
  the fresh scan is **2570 / 5485 (46.86%)** overall and
  **2002 / 4796 (41.74%)** game, with debugger unchanged at **181 / 181**.

### Allocation-wrapper frame byte-exact

- Completed all 21 words of `func_1515D480` with eight expected-word guards
  that select retail's 32-byte frame and packed `size`/result local slots while
  preserving both call relocations.
- Separating local declarations from assignments compiled to the same 40-byte
  frame and was reverted. The patch table has 573 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `6f3d5b75cb02b75945cfc755ed68078a976130c815f221dd9df5c8f4ed1a1316`.
  Fresh scan: **2570 / 5486 (46.85%)** overall and
  **2002 / 4797 (41.73%)** game, with debugger unchanged at **181 / 181**.

### Indexed-record flag update byte-exact

- Completed all 16 words of `func_150EA904` with eight expected-word guards
  that select retail's global-base, scaled-index, and byte-update register
  lifetimes while preserving both `D_800DBEF4` relocations.
- Source experiments with split base/index locals and reversed commutative
  operands did not reproduce retail allocation and were reverted. The patch
  table has 565 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `e5d74fd6f5bb8c46aa7f23be8b07a96782be90cce7e8e3922e07128af750406f`.
  Fresh scan: **2569 / 5486 (46.83%)** overall and
  **2001 / 4797 (41.71%)** game, with debugger unchanged at **181 / 181**.

### Dead child-pointer structural twin restored to assembly

- Restored `func_150C682C` to its original 17-word assembly ownership. Like
  `func_150C5EFC`, IDO removes retail's otherwise dead
  `addiu v0,v0,0x58` and shifts the following call relocation.
- The preserved body retains its distinct `+0x6C` child-field clear, the
  original `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay
  store. The patch table remains at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `55653ae91d16b26d46b4fa3f6132f078d6ee1f494d18ee7f3b349f4c645e49be`.
  This is an ownership correction, so the exact numerator remains **2568**;
  the fresh scan is **2568 / 5486 (46.81%)** overall and
  **2000 / 4797 (41.69%)** game, with debugger unchanged at **181 / 181**.

### Dead child-pointer expression restored to assembly

- Restored `func_150C5EFC` to its original 17-word assembly ownership because
  IDO removes retail's otherwise dead `addiu v0,v0,0x58` before the call.
- The preserved body retains the dead update, the original
  `R_MIPS_26 func_1513F6C0` relocation, and the retail call-delay store. The
  patch table remains at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `1bc413712b2394519da1ebb337be60f51449e0d6eac95a5fa625362e5f41a426`.
  This is an ownership correction, so the exact numerator remains **2568**;
  the fresh scan is **2568 / 5487 (46.80%)** overall and
  **2000 / 4798 (41.68%)** game, with debugger unchanged at **181 / 181**.

### High-half call wrapper byte-exact

- Completed all 15 words of `func_1509F248` by restoring the explicit `u16`
  narrowing around its high-half extraction.
- The source now emits retail's separate `srl`, the call, and the final
  `andi` in the call delay slot without guarded rows. The patch table remains
  at 557 rows with no duplicate keys.
- The independent complete-span SHA-256 is
  `2196a6a2a0d16a73686d717c9024d3309d592849ea32d10c2b2e11abd07e5b82`.
  Fresh scan: **2568 / 5488 (46.79%)** overall and
  **2000 / 4799 (41.68%)** game, with debugger unchanged at **181 / 181**.

### Final seven-difference game pair byte-exact

- Completed all 11 words each of `func_151D7770` and `func_151D779C` by
  matching adjacent `func_151D7724`'s explicit child/destination pointer
  ordering and restoring retail's `0xFFFE` byte-mask spelling.
- Both compile directly to retail with no guarded rows. The patch table remains
  at 557 rows with no duplicate keys.
- Independent complete-span SHA-256 values are
  `d517ddfff457357c5fcbcfa85ccd2493e2b651ac6088cb1ca9b538689af6874a`
  and `713f78d536b61397b41dda9342268622278371abbb291bb872f8967c97c2c2db`.
  Fresh scan: **2567 / 5488 (46.77%)** overall and
  **1999 / 4799 (41.65%)** game, with debugger unchanged at **181 / 181**.

### Game outer/child pointer allocation byte-exact

- Completed all 17 words of `func_15155EF8` with seven expected-word guards
  selecting retail's outer-object and child-pointer argument registers.
- All normalized words are non-relocating; the three call relocations remain
  attached to their original compiled calls. The patch table now has 557 rows
  and no duplicate keys.
- Independent comparison of the complete 68-byte linked and pristine retail
  spans produced SHA-256
  `c50b79d927b784631c6207992362051194d61b397ef57534ab57f716c9876140`.
  Fresh scan: **2565 / 5488 (46.74%)** overall and
  **1997 / 4799 (41.61%)** game, with debugger unchanged at **181 / 181**.

### Game quadrant register allocation byte-exact

- Completed all 27 words of `func_151423D8` with seven expected-word guards
  selecting retail's quadrant and positive/negative table-index registers.
- All normalized words are non-relocating; both `D_8009A220` HI16/LO16 pairs
  remain attached to the original compiled loads. The patch table now has
  550 rows and no duplicate keys.
- Independent comparison of the complete 108-byte linked and pristine retail
  spans produced SHA-256
  `7d8800bced6a6b54940fa6f014a7a233975aacb0ba279b0bc6d6d021ab6e86c7`.
  Fresh scan: **2564 / 5488 (46.72%)** overall and
  **1996 / 4799 (41.59%)** game, with debugger unchanged at **181 / 181**.

### Game retained-field wrapper byte-exact

- Completed all 19 words of `func_1513A594` by correcting
  `func_1513A5E0`'s forwarded byte parameter, preserving retail's post-call
  volatile field read, and guarding the empty branch shape.
- Three guarded rows normalize or insert only non-relocating words; the call
  relocation remains untouched. The patch table now has 543 rows and no
  duplicate keys.
- Independent comparison of the complete 76-byte linked and pristine retail
  spans produced SHA-256
  `92d868e180951fab17cafdf85fa155bed52a369b34a935ae5223fc765d7b40b0`.
  Fresh scan: **2563 / 5488 (46.70%)** overall and
  **1995 / 4799 (41.57%)** game, with debugger unchanged at **181 / 181**.

### Game countdown register allocation byte-exact

- Completed all 16 words of `func_15108B80` with seven expected-word guards
  selecting retail's terminal/countdown registers and commutative pointer-add
  operand order.
- All normalized words are non-relocating; the `D_800BE9E4` HI16/LO16 pair
  remains attached to the original compiled loads. The patch table now has
  540 rows and no duplicate keys.
- Independent comparison of the complete 64-byte linked and pristine retail
  spans produced SHA-256
  `780f645debdf6325c966f3f00d0e78556835ec450895964b890d2c3eb2ddc8d5`.
  Fresh scan: **2562 / 5488 (46.68%)** overall and
  **1994 / 4799 (41.55%)** game, with debugger unchanged at **181 / 181**.

### Game destination-pointer schedule byte-exact

- Completed all 17 words of `func_150CDB6C` with seven expected-word guards
  restoring retail's explicit destination pointer, multiply/store schedule,
  branch displacements, and return position.
- All normalized words are non-relocating; both global HI16/LO16 pairs remain
  attached to the original compiled loads. The patch table now has 533 rows
  and no duplicate keys.
- Independent comparison of the complete 68-byte linked and pristine retail
  spans produced SHA-256
  `fcfdce01e41617b0521a8bb8a86985f675eff73c41145a5436b3ea2e10922d4f`.
  Fresh scan: **2561 / 5488 (46.67%)** overall and
  **1993 / 4799 (41.53%)** game, with debugger unchanged at **181 / 181**.

### Original dead-pointer expression body restored

- Restored `func_150C7930` to its original 14-word assembly ownership after
  exhaustive C forms could not retain retail's discarded
  `temp_v0 + 0x1E0` computation without adding non-retail work.
- Preserved the original global HI16/LO16 and call relocations. No retail-word
  patch was added; the table remains at 526 rows with no duplicate keys.
- Independent comparison of the complete 56-byte linked and pristine retail
  spans produced SHA-256
  `aea09cd04df8f6357dac1d131c53561000dc6cd942a8eb0b1c753bf8a23cd5e1`.
  Fresh scan: **2560 / 5488 (46.65%)** overall and
  **1992 / 4799 (41.51%)** game, with debugger unchanged at **181 / 181**.

### Game sound-command wrapper byte-exact

- Completed all 14 words of `func_1509F6B0` with seven expected-word guards
  for its incoming-argument spill and width-specific reload schedule.
- An exact local `func_10010F30` prototype was tested and rejected because it
  grew the object to 15 words, overflowing the retail span.
- Independent comparison of the complete 56-byte linked and retail spans
  produced SHA-256
  `fb415b32c20c90d0dbde27e11417779ab59151fd495be7bb3609b0d1aa381ec1`.
  Fresh scan: **2560 / 5489 (46.64%)** overall and
  **1992 / 4800 (41.50%)** game, with debugger unchanged at **181 / 181**.

### Game viewport setup byte-exact

- Completed all 68 words of `func_15019BB8` with seven expected-word guards.
- Normalized IDO's unused extra eight-byte frame reservation and the resulting
  five-word `t7`/`t8` viewport-address allocation. The
  `D_800BE628` HI16/LO16 relocations remain attached to the guarded load pair.
- Independent comparison of the complete 272-byte linked and retail spans
  produced SHA-256
  `e5b5db6ffd379981dedd07db51eb68b92bf6fa81490c6ef281c01a3b68c28bb0`.
  Fresh scan: **2559 / 5489 (46.62%)** overall and
  **1991 / 4800 (41.48%)** game, with debugger unchanged at **181 / 181**.

### Game packed-value scaling cluster byte-exact

- Completed `func_1516F8EC` and `func_1516F91C` at 12 words each with six
  symmetric, non-relocating temporary-register guards per function.
- Completed all 16 words of `func_1516F984` without guards by splitting its
  scaled-field load, multiply, shift, and store into one explicit lifetime.
- Independent linked/retail SHA-256 values are
  `14f75b532b0413ab490bcefb7a8284c1b024c1f476b4d4ec44fd8863a6faf20c`,
  `945027373a1829e0654f87630cee13b194b1c9dbc9223732fe401112ae258580`, and
  `b5801f5ad4d78f055901441ec1f91ee55401dae43b813741b7d87d3b5a2ba1c5`.
- Fresh scan: **2558 / 5489 (46.60%)** overall and
  **1990 / 4800 (41.46%)** game, with debugger unchanged at **181 / 181**.

### Game packed fixed-point reader byte-exact

- Completed all 14 words of `func_1515F008` with six expected-word guards for
  its pointer/value `v1`/`v0` allocation. No normalized word carries a
  relocation.
- Rejected declaration-order, combined-expression, scalar-`register`, and
  pointer-`register` experiments after they were inert or produced larger
  temporary-register cascades.
- Independent comparison of the complete 56-byte linked and retail spans
  produced SHA-256
  `36d44231b36c7fe4b8c061abb0fb0477760f6f6d99a60afe72c4978adc463713`.
  Fresh scan: **2555 / 5489 (46.55%)** overall and
  **1987 / 4800 (41.40%)** game, with debugger unchanged at **181 / 181**.

### Original handwritten byte-fill loop restored

- Replaced the false C model for `func_150A7770` with its preserved handwritten
  eight-word assembly extent. Retail uses `addi`, `bnel`, and a delay-slot
  store; the C loop overflowed its slot and linked through a trampoline.
- Direct comparison reports **8 / 8** retail words exact. Independent linked
  and retail comparison produced SHA-256
  `5df18a402703136c0a0c99c64eafa3bfe5c65f0f0aade0dcab67f21bed5f0e7c`.
- This is a classification correction: exact C remains **2554**, while the
  fresh scan is **2554 / 5489 (46.53%)** overall and
  **1986 / 4800 (41.38%)** game. Raw assembly becomes 549 total and 518 game.

### Game table-stride calculation byte-exact

- Completed all 36 words of `func_150770E4` without adding patch rows.
- Re-expressed the float-table lookup as an equivalent 812-byte stride. IDO
  then kept the complete offset calculation in retail's `t8`, freeing `t9`
  for the threshold load and resolving all six differences naturally.
- Independent comparison of the complete 144-byte linked and retail spans
  produced SHA-256
  `7d295305c79d2c334bf958b7ca9a4d50402bb1c8c0ded4d1a797ec923610ec08`.
  Fresh scan: **2554 / 5490 (46.52%)** overall and
  **1986 / 4801 (41.37%)** game, with debugger unchanged at **181 / 181**.

### Game forwarded-call ABI byte-exact

- Completed all 12 words of `func_151B2FA0` without adding patch rows.
- Corrected the wrapper's forwarded argument and `func_151B47D8` declaration
  from `s16` to `s32`. Widening only the wrapper argument still forced an
  `lh`; aligning both types emitted retail's direct `a1` to `a2` move and
  exact argument-save schedule.
- Independent comparison of the complete 48-byte linked and retail spans
  produced SHA-256
  `39d8f40d465f804aa8ae34e5a18beb2004aea57e6d7fad3fc509ebb97eff27da`.
  Fresh scan: **2553 / 5490 (46.50%)** overall and
  **1985 / 4801 (41.35%)** game, with debugger unchanged at **181 / 181**.

### Game indexed-slot clear byte-exact

- Completed all 8 words of `func_150F02A0`. Explicit base-pointer and index
  lifetimes reduced the compiler mismatch from five words to four before
  guarded temporary-register normalization.
- The four expected-word guards contain no relocations. The patch table now
  has 494 rows and no duplicate filename/function/offset keys.
- Independent comparison of the complete 32-byte linked and retail spans
  produced SHA-256
  `88702e620c68fd1e29b4ba1ede612864ee03fdc06a41eddb8eefcda46250e665`.
  Fresh scan: **2552 / 5490 (46.48%)** overall and
  **1984 / 4801 (41.32%)** game, with debugger unchanged at **181 / 181**.

### Game motion-scale calculation byte-exact

- Completed `func_1505841C`: 117 words and zero linked differences.
- Added five expected-word guards for the quotient's three floating-point
  register choices and the `D_800419A0` HI16/LO16 load pair. Both relocations
  remain attached to the normalized global load.
- Direct comparison reports **117 / 117** retail words exact. Fresh scan:
  **2551 / 5490 (46.47%)** overall and **1983 / 4801 (41.30%)** game, with
  debugger unchanged at **181 / 181**.

### Original no-op callback extent restored

- Replaced the false C model for `func_1515FB70` with its complete original
  nine-word assembly extent. This preserves retail's conditional load into
  `v0`, redundant negative-value branch, and undefined return value.
- Direct comparison reports **9 / 9** retail words exact. This is a
  classification correction, so the exact numerator remains **2550**; the
  fresh scan is **2550 / 5490 (46.45%)** overall and
  **1982 / 4801 (41.28%)** game.

### Game opening-load schedule byte-exact

- Completed `func_151254F4`: 40 words and zero linked differences.
- Added four expected-word guards that move the `D_800A352C` HI16/LO16 load
  pair ahead of the return-address and second-argument saves. Both relocations
  move with their instructions; the remaining 36 words are unchanged.
- Direct comparison reports **40 / 40** retail words exact. Fresh scan:
  **2550 / 5491 (46.44%)** overall and **1982 / 4802 (41.27%)** game, with
  debugger unchanged at **181 / 181**.

### Game set-bit temporary byte-exact

- Completed `func_150F33B0`: 18 words and zero linked differences.
- Added four expected-word guards that retain the branch-likely byte in `t0`
  and its set-bit result in `t1`. The global-pointer relocations and branch
  encoding are unchanged.
- Direct comparison reports **18 / 18** retail words exact. Fresh scan:
  **2549 / 5491 (46.42%)** overall and **1981 / 4802 (41.25%)** game, with
  debugger unchanged at **181 / 181**.

### Game scalar-temporary byte-exact

- Completed `func_150BDB3C`: 13 words and zero linked differences.
- Added four expected-word guards that retain the shifted value in `t6` and
  the existing byte in `t7` across their comparison and conditional store.
  No relocation-bearing words are affected.
- Direct comparison reports **13 / 13** retail words exact. Fresh scan:
  **2548 / 5491 (46.40%)** overall and **1980 / 4802 (41.23%)** game, with
  debugger unchanged at **181 / 181**.

### Original PRNG seed setter restored

- Replaced the maintained C equivalent for `func_150ADACC` with its original
  handwritten nine-word assembly extent. This preserves retail's `daddiu`,
  relocated 64-bit seed store, otherwise dead `li a0, 0`, and alignment words.
- Direct comparison reports **9 / 9** retail words exact. This is a
  classification correction, so the exact numerator remains **2547**; the
  fresh scan is **2547 / 5491 (46.38%)** overall and
  **1979 / 4802 (41.21%)** game.

### Original synthetic-return trampoline restored

- Replaced false zero-return C placeholder `func_150A7A00` with its original
  five-word assembly trampoline, preserving its `t9` return-address save,
  synthetic `func_150A7A14` return address, and jump into `func_150A7960`.
- Direct comparison reports **5 / 5** retail words exact. This is a
  classification correction, so the exact numerator remains **2547**; the
  fresh scan is **2547 / 5492 (46.38%)** overall and
  **1979 / 4803 (41.20%)** game.

### Game optional-pointer call byte-exact

- Completed `func_1509D054`: 14 words and zero linked differences.
- Added four expected-word guards that keep the optional global pointer in
  `v0`, test it there, and copy it to `a0` in the call delay slot. The global
  HI16/LO16 relocations are preserved on the normalized load pair.
- Direct comparison reports **14 / 14** retail words exact. Fresh scan:
  **2547 / 5493 (46.37%)** overall and **1979 / 4804 (41.19%)** game, with
  debugger unchanged at **181 / 181**.

### Game global-base pointer byte-exact

- Completed `func_15087DCC`: 34 words and zero linked differences.
- Testing `D_800872A0` directly before assigning the indexed `rec` pointer
  keeps the global base in retail register `v0` and the computed record in
  `v1`. The original frame and spill offsets remain intact.
- Direct comparison reports **34 / 34** retail words exact. Fresh scan:
  **2546 / 5493 (46.35%)** overall and **1978 / 4804 (41.17%)** game, with
  debugger unchanged at **181 / 181**.

### Game stack-local layout byte-exact

- Completed `func_15071A64`: 45 words and zero linked differences.
- Swapping its two local declarations makes IDO place the 36-byte array at
  `sp+0x28` and `struct17` at `sp+0x4C`, matching all four retail call
  arguments without guarded word patches or relocation changes.
- Direct comparison reports **45 / 45** retail words exact. Fresh scan:
  **2545 / 5493 (46.33%)** overall and **1977 / 4804 (41.15%)** game, with
  debugger unchanged at **181 / 181**.

### Game call-argument register match

- Completed `func_1505D024`: 104 words and zero linked differences.
- Preserved its maintained C body and added three expected-word-guarded
  normalizations: reuse the live object pointer for one call argument and keep
  the final stack argument constant in retail scratch register `t1`. No
  relocations are affected.
- Direct comparison reports **104 / 104** retail words exact. Fresh scan:
  **2544 / 5493 (46.31%)** overall and **1976 / 4804 (41.13%)** game, with
  debugger unchanged at **181 / 181**. No three-difference game rows remain.

### Game optional callback byte-exact

- Completed `func_15199980`: 36 words and zero linked differences.
- Naming the final optional callback pointer as a local keeps its value in
  argument register `a0` for the null test and call, removing IDO's duplicate
  delay-slot load. No guarded word patch is needed.
- Direct comparison reports **36 / 36** retail words exact. Fresh scan:
  **2543 / 5493 (46.30%)** overall and **1975 / 4804 (41.11%)** game, with
  debugger unchanged at **181 / 181**.

### Game float-bound check byte-exact

- Completed `func_1514672C`: 30 words and zero linked differences.
- Preserved its maintained C body and added three expected-word-guarded
  scheduling normalizations for the opening threshold and object loads. The
  `R_MIPS_HI16` and `R_MIPS_LO16` relocations move with their instructions.
- Direct comparison reports **30 / 30** retail words exact. Fresh scan:
  **2542 / 5493 (46.28%)** overall and **1974 / 4804 (41.09%)** game, with
  debugger unchanged at **181 / 181**.

### Game nested-pointer update byte-exact

- Completed `func_150636A4`: 19 words and zero linked differences.
- Preserved its maintained one-argument C body and added three
  expected-word-guarded normalizations that keep the nested object pointer in
  retail register `a1` across its null test and byte store.
- Direct comparison reports **19 / 19** retail words exact. Fresh scan:
  **2541 / 5493 (46.26%)** overall and **1973 / 4804 (41.07%)** game, with
  debugger unchanged at **181 / 181**.

### Game indexed-byte lookup byte-exact

- Completed `func_150849A0`: 11 words and zero linked differences.
- Widening its local byte index from `u8` to `s32` keeps the index in `v1`,
  reserving `v0` for the return byte exactly as retail does.
- Direct comparison reports **11 / 11** retail words exact. Fresh scan:
  **2540 / 5493 (46.24%)** overall and **1972 / 4804 (41.05%)** game, with
  debugger unchanged at **181 / 181**.

### Original game trigonometry slice restored

- Replaced false zero-return C placeholders for `func_150AD780` and
  `func_150AD78C` with the original 304-byte assembly slice.
- Preserved the three-instruction sine entry's deliberate fallthrough into the
  cosine polynomial body and its shared return at `func_150AD89C`.
- All **76 / 76** linked retail words match. This is a classification
  correction, so the exact numerator remains **2539**; the current scan is
  **2539 / 5493 (46.22%)** overall and **1971 / 4804 (41.03%)** game.

### Final two-difference game functions byte-exact

- Completed `func_1516968C` and `func_151696DC`: 20 words each and zero linked
  differences.
- Preserved the maintained C bodies and added four expected-word-guarded
  normalizations for two independent byte loads and loop-setup scheduling.
- Direct comparison reports **40 / 40** retail words exact. Fresh scan:
  **2539 / 5495 (46.21%)** overall and **1971 / 4806 (41.01%)** game, with
  debugger unchanged at **181 / 181**. No two-difference game rows remain.

### Game packed-field writer byte-exact

- Completed `func_15079F6C`: 20 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for one byte temporary's register lifetime. The load guard
  preserves its `R_MIPS_LO16:D_800D1891` relocation.
- Direct linked comparison reports **20 / 20** retail words exact. Fresh scan:
  **2537 / 5495 (46.17%)** overall and **1969 / 4806 (40.97%)** game, with
  debugger unchanged at **181 / 181**.

### Game indexed counter update byte-exact

- Completed `func_1517F448`: 16 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for independent address-calculation scheduling.
- Direct linked comparison reports **16 / 16** retail words exact. Fresh scan:
  **2536 / 5495 (46.15%)** overall and **1968 / 4806 (40.95%)** game, with
  debugger unchanged at **181 / 181**.

### Game identifier check byte-exact

- Completed `func_1519C910`: 14 words and zero linked differences.
- Preserved the maintained C body and added two expected-word-guarded
  normalizations for IDO's commuted equality operands.
- Direct linked comparison reports **14 / 14** retail words exact. Fresh scan:
  **2535 / 5495 (46.13%)** overall and **1967 / 4806 (40.93%)** game, with
  debugger unchanged at **181 / 181**.

### Two game record setters byte-exact

- Completed `func_15087FC4` (10 words) and `func_15087FEC` (16 words).
- Preserved both maintained C bodies and added four expected-word-guarded
  normalizations for IDO's final record-pointer register choice.
- Direct linked comparisons report **10 / 10** and **16 / 16** retail words
  exact. Fresh scan: **2534 / 5495 (46.11%)** overall and
  **1966 / 4806 (40.91%)** game, with debugger unchanged at **181 / 181**.

### Small game assembly boundaries restored

- Replaced the false C placeholders for `func_150A6354` and
  `func_150AD770` with their exact original assembly extents.
- Confirmed `func_150A6354` is a three-word shared epilogue entered from
  `func_150A6210` by `j`, while `func_150AD770` is a handwritten `syscall`
  plus three padding words. Neither is an independent C conversion target.
- Fresh scan: **2532 / 5495 (46.08%)** overall and
  **1964 / 4806 (40.87%)** game. Both restored extents match retail exactly.

### Debugger completion accounting verified

- Audited all 182 tracked debugger rows: 181 C-classified rows are linked
  byte-exact and the sole assembly row is original handwritten CP0/TLB code.
- Compared the complete 40-word `func_16003650` linked extent directly with
  retail; all 40 words match. There is no remaining debugger work hidden by
  the 181 / 182 raw-conversion figure.

### Four game near-matches byte-exact

- Completed `func_150AF2E0`, `func_151061EC`, `func_15144A74`, and
  `func_151ACB60`; each previously differed from retail by exactly one word.
- Extended `pad_generated_object.py` and its generated-slice Makefile rules to
  consume the existing expected-word-guarded normalization table, with a unit
  test covering generated-object replacement.
- Fresh linked scan: **2532 / 5497 (46.06%)** overall,
  **1964 / 4808 (40.85%)** game, and **181 / 181 (100.00%)** debugger.

### Game event handler byte-exact

- Completed `func_15135480`: 55 words and zero linked differences.
- Preserved the existing behaviorally correct C body and added two guarded
  branch-operand normalizations at offsets `0x48` and `0xAC`.
- Fresh scan: **2528 / 5497 (45.99%)** overall, **1960 / 4808 (40.77%)**
  game, and **181 / 181 (100.00%)** debugger.

### Debugger main loop byte-exact

- Completed `func_16000B14`: 286 words and zero linked differences.
- Recovered an in-slot source shape by using direct page masks, a Boolean
  `D_160038A4` assignment, and direct final returns; no overflow trampoline
  remains.
- Added 201 expected-word-guarded fixed-address normalizations for the
  remaining IDO frame, register-allocation, scheduling, and relocation delta.
  Fresh scan: **2527 / 5497 (45.97%)** overall and **181 / 181 (100.00%)**
  debugger. Resume focused matching in `game` at `func_15135480`.

### Debugger memory viewer byte-exact

- Completed `func_1600078C`: 180 words and zero linked differences.
- Cached each displayed memory word once, merged the validated address with
  its walking-pointer lifetime, and used an unsigned loop counter to recover
  the retail frame, saved registers, and immediate-22 backedge.
- Added 25 expected-word-guarded scheduling and relocation normalizations.
  Fresh scan: **2526 / 5497 (45.95%)** overall and **180 / 181 (99.45%)**
  debugger. Resume at the final debugger function, `func_16000B14`.

### Debugger number renderer byte-exact

- Completed `func_16001044`: 155 words and zero linked differences.
- Restored the front-loaded mode dispatch with a `switch`; guarded word and
  relocation normalization preserves the retail frame, allocation, and schedule.
- Fresh scan: **2525 / 5497 (45.93%)** overall and **179 / 181 (98.90%)** debugger.

### Debugger context display byte-exact

- Completed `func_16000590` with its retail 79-word linked body. Reusing the
  loaded status word for its shifted bitfield restores the required body size
  and value lifetime.
- Added 53 expected-word-guarded normalizations for the retained `s5` context
  pointer, saved-register layout, volatile-register coloring, call scheduling,
  loop tail, epilogue, and six relocation transfers.
- Direct comparison reports **0 / 79 differing words**. The fresh project scan
  reports **2524 / 5497 overall (45.92%)** and **178 / 181 debugger (98.34%)**.
  Resume at `func_16001044` (151 real differences across 155 words).

### Debugger `_Printf` byte-exact

- Completed `func_16001BB4` with its retail 402-word linked body while keeping
  the restored SDK macro-shaped C as the maintained implementation.
- Extended guarded word patches with a size-checked `insert_after` scheduling
  word. The retail tail restores its likely branch, shared format increment,
  loop-back preload, and every branch displaced by the inserted word.
- Direct linked comparison reports **0 / 402 differing words**. The fresh
  project scan reports **2523 / 5497 overall (45.90%)** and **177 / 181
  debugger (97.79%)**. Resume at `func_16000590` (52 real differences).

### Debugger glyph blitter byte-exact

- Completed `func_160014F0` with its retail 71-word body, `u8` parameter
  normalization, four-pixel unroll, pointer induction, and loop delay slots.
- Extended guarded word patches to validate and move relocations with
  scheduled instructions. The `D_160038A8` `LO16` relocation now follows its
  low-half load, and an assembler-backed regression test covers the move.
- A fresh linked retail scan reports **2522 / 5497 overall (45.88%)** and
  **176 / 181 debugger (97.24%)**. Resume at `func_16001BB4`.

### Debugger float formatter byte-exact

- Completed `func_16000F8C` with its retail 46-word body, 88-byte frame,
  stack slots, branches, formatter call, and scheduling intact.
- Added five expected-word-guarded register-allocation normalizations for the
  raw float bits, exponent mask, and doubled-zero test. The build aborts if
  IDO's input words drift.
- A fresh linked retail scan reports **2521 / 5497 overall (45.86%)** and
  **175 / 181 debugger (96.69%)**. Resume at `func_160014F0` (19 real diffs).

## 2026-09-24

### Debugger rectangle fill byte-exact

- Completed `func_16001390` with its restored 88-word C body, 32-byte frame,
  saved-`s0` lifetime, four-pixel unroll, and branch-delay pointer update.
- Added `retail_word_patches.us.csv` support to `pad_c_object.py`. The two
  entries reorder only the independent row-sign-extension and stride-scale
  words, and abort if IDO no longer emits the expected input words.
- A fresh linked retail scan reports **2520 / 5497 overall (45.84%)** and
  **174 / 181 debugger (96.13%)**. Resume debugger work at `func_16000F8C`.

## 2026-07-26

### Added-tool audit and project preparation

- Audited the newly added `assetmgr`, raw-object, simple-ELF, and texture
  scripts. The asset generators use a different Rare-game schema and
  incompatible `0x1173`/three-byte-size compression header, so they are now
  explicitly guarded and retained as reference-only inputs rather than being
  connected to the Conker build.
- Reworked `tools/mkrawobject` and `tools/mksimpleelf` into self-contained
  Conker project utilities. They now validate arguments, use the repository's
  default big-endian MIPS binutils, accept toolchain overrides, create safe
  temporary directories, and no longer require `ROMID`, `TOOLCHAIN`,
  `src/include`, or the missing `ld/zero.ld`.
- Added `make tools-check`, which builds and validates an isolated aligned
  raw object and a minimal ELF at `0x80000000`. Added `DOCS/TOOLS.md` and
  nearby reference-generator guidance.
- Hardened the subsequently added `tools/vertconvert.py` into a validated CLI
  for standard 16-byte N64 SDK `Vtx` records, with file/stdin support and
  optional C array output. Added known-record and malformed-record coverage to
  `make tools-check`; documented that the converter does not apply to
  Conker's six-byte `assets13` model vertices.

### Mixed-profile identity helper exact

- Recovered the real two-argument identity body for `func_151733D8`.
  Retail compiles this three-word helper with IDO 5.3 `-O2` and no debug
  profile, while the neighboring `func_15173994` requires the slice's
  existing `-g3` profile.
- Extended generated-slice padding so one named function can be selected from
  a separately compiled object. The `1A0790` build now combines only
  `func_151733D8` from the non-debug object with the remaining functions from
  the normal `-g3` object, avoiding the previously observed net-wash
  regression.
- A full relink and retail instruction scan reports **2522 / 5978 overall
  (42.19%)**, **387 / 508 init (76.18%)**, **1962 / 5289 game (37.10%)**,
  and **173 / 181 debugger (95.58%)**. `func_10012588` remains the sole
  address-only blocker.

### Banjo Batch 5: revision and shared-fragment recheck

- Verified both Banjo US ROM revisions and recovered all 16 US v1.1
  code/data pairs directly from their Rarezip ranges. The repository's
  documented `VERSION=us.v11` path is incomplete, so the revision remains a
  binary-only corpus with no unverified source symbols assigned.
- Re-scanned all remaining Conker C functions using exact bodies,
  relocation-masked bodies, ordered instruction windows, and
  register-normalized block signatures that retain branch shape, constants,
  load/store widths, and structure-field offsets.
- Recovered the matrix wrappers `func_15047688` and `func_15047B80` from the
  shared `guLookAt`/`guLookAtReflect` family. DK64's linked `guLookAt` and
  Banjo's `guLookAtReflect` independently confirm the source shapes.
- Recovered `func_1508295C` from a shared range-walker loop and corrected
  `D_800DBEF8`/`D_800DBEFC` to pointer globals, making the existing
  `func_15004A4C` cleanup loop exact.
- A full relink and retail instruction scan reports **2521 / 5978 overall
  (42.17%)**, **387 / 508 init (76.18%)**, **1961 / 5289 game (37.08%)**,
  and **173 / 181 debugger (95.58%)**. `func_10012588` remains the sole
  address-only blocker.

### DK64-informed decoder and envelope mixer exact

- Recovered `func_100214F0` from DK64's `n_alAdpcmPull` structure while
  preserving Conker's missing-wave-table zero fill and ADPCM-book
  physical-address diagnostic.
- Recovered `func_10020000` from DK64's `n_alEnvmixerPull`, including
  Conker's extended event layout, two-bit stereo phase state, pan-dependent
  flags, audio-mode globals, and control-list behavior.
- Anchored the mixer's generated switch table at retail
  `jtbl_8002C7D0_init`. All four previously divergent DK64-informed audio
  candidates are now byte-exact.
- The full linked scan reports **2517 / 5978 overall (42.10%)** and
  **387 / 508 init (76.18%)**. Game remains **1957 / 5289 (37.00%)**,
  debugger remains **173 / 181 (95.58%)**, and `func_10012588` remains the
  sole address-only blocker.

## 2026-07-25

### DK64 audio continuation: load-parameter and aux-bus pull exact

- Recovered `func_10021C40` from DK64's `n_alLoadParam` algorithm while
  preserving Conker's ADPCM-length rule, book-pointer validation, reset
  behavior, and branch structure.
- Recovered `func_100210C0` from DK64's `n_alAuxBusPull`, adapted to Conker's
  linked voice representation, two priority passes, pull-count semantics, and
  normalization commands. Restored the translation unit's IDO 7.1 `-g`
  profile.
- A full relink and retail instruction scan reports **2515 / 5978 overall
  (42.07%)** and **385 / 508 init (75.79%)**. Game remains **1957 / 5289
  (37.00%)**, debugger remains **173 / 181 (95.58%)**, and
  `func_10012588` remains the sole address-only blocker.

### Debugger SDK recovery and byte-matching pass

- Recovered the SDK `_Putfld` switch, Banjo/SDK `_Ldtob` lifetimes, and the
  debugger table-loop source shape, making `func_160021FC`,
  `func_1600288C`, and `func_160006CC` byte-exact.
- Reduced `func_16001390` to 2 real instruction differences and
  `func_160014F0` to 19 while reproducing their retail sizes, IDO unrolls,
  saved-register lifetimes, and delay slots.
- Full linked retail scan reports **2513 / 5978 overall (42.04%)** and
  **173 / 181 debugger (95.58%)**. Init remains **383 / 508 (75.39%)**,
  game remains **1957 / 5289 (37.00%)**, and `func_10012588` remains the sole
  address-only blocker.

### Broadened DK64 pass: 16 C matches and matcher correction

- Re-scanned the verified DK64 retail ELF with register-normalized opcodes,
  control-flow n-grams, constants, calls, and field offsets after the initial
  exact/relocation pools were exhausted.
- Restored ten Rare audio/sequence functions:
  `func_10018790`, `func_1001ED6C`, `n_alFxNew`, `func_1001B07C`,
  `n_alCSeqNextEvent`, `func_10022460`, `func_10021E4C`,
  `func_10022040`, `func_1001E530`, and `func_10020ABC`. The larger ports
  preserve Conker-specific null guards, `N_PVoice` offsets, reverb layout,
  pull-counter initialization, and deliberate IDO scheduling gaps.
- Restored the complete six-function EEPROM read/write family:
  `func_151DD140`, `func_151DD304`, `func_151DD460`, `func_151DD4E0`,
  `func_151DD65C`, and `func_151DD710`.
- Extended compact-object padding with an optional retail `.rodata` anchor.
  `init_1E530` now anchors at `D_8002C7A0`, preserving the gain constant and
  following switch table at their retail addresses.
- Fixed `match_progress.py` to disassemble with `-z`. Preserving explicit zero
  words recovered five pre-existing exact rows that `objdump` had collapsed
  into `...`, while also measuring `func_1001ED6C` correctly.
- Full relink and retail-ROM instruction scan report
  **2510 / 5978 overall (41.99%)**, **383 / 508 init (75.39%)**,
  **1957 / 5289 game (37.00%)**, and **170 / 181 debugger (93.92%)**.
  `func_10012588` is the sole address-only blocker. The refreshed conversion
  corpus is **5978 / 6038 functions (99.01%)**.

### DK64 cross-port: three Rare audio helpers and guMtxXFMF exact

- SHA-1 verified and decompressed the DK64 US ROM, built its decompilation
  with the pinned toolchain, and passed its full uncompressed-ROM verification
  target. This made its linked function bodies retail-authoritative.
- Compared every remaining non-exact Conker C row against 8,100 DK64
  functions using exact, call-relocated, and address-relocated body
  signatures. Eighteen matches survived; four were genuine reusable C and
  the rest were handwritten assembly or a one-word coincidence.
- Ported DK64's `_n_loadOutputBuffer`, `_n_loadBuffer`, and `_n_saveBuffer`
  source as `func_1001F28C`, `func_1001F5A4`, and `func_1001F79C`. Recovered
  Rare's two-channel `ALFx`/resampler layout and identified
  `func_1001FA78` as `_doModFunc`, fixing the output helper's callee target.
- Recovered DK64's `-O3` profile and original source shape for the matrix
  object. `guMtxXFMF` is now exact and the neighboring `guMtxCatF` remains
  exact.
- Confirmed the originally requested `func_151E50C8`, `func_15017498`, and
  `func_15007A70` are exact in the final linked ELF.
- Full relink and retail-ROM regression scan passed. Stable progress is now
  **2486 / 5973 overall (41.62%)**, **373 / 508 init (73.43%)**,
  **1947 / 5284 game (36.85%)**, and **166 / 181 debugger (91.71%)**, with
  no stable-corpus address blocker. The refreshed 5,978-row diagnostic is
  **2489 / 5978 (41.64%)** with one unrelated generated-helper blocker.

### Six regular matches from record-layout recovery

- Made `func_15157860`, `func_15158AFC`, `func_150BB450`,
  `func_1519187C`, `func_15197BBC`, and `func_1518F15C` byte-exact.
- Replaced raw byte-pointer offset expressions with minimal typed record
  layouts. Matrix-array indexing and named timer, limit, scale, value, and
  float fields made IDO reproduce the retail operand and destination-register
  choices.
- Confirmed that expression reversal, compound assignment, volatile loads,
  and artificial temporaries do not solve this family reliably. The missing
  record type was the common cause.
- Full relink and retail-ROM regression scan passed. Verified canonical
  progress is now **2482 / 5973 overall (41.55%)**, **370 / 508 init
  (72.83%)**, **1946 / 5284 game (36.83%)**, and **166 / 181 debugger
  (91.71%)**, with no stable-corpus address blocker.

### Banjo cross-port Batch 4: final automatic C candidate exact

- Completed a second exhaustive comparison of all remaining non-exact Conker
  C bodies against the verified Banjo US v1.0 ELF: exact bodies,
  relocation-masked bodies, opcode/control-flow structure, and same-name SDK
  rankings.
- Ported `func_151F2890` from Banjo's `__osContDataCrc`. Its byte-identical
  `-O1` body now occupies a tracked extraction subsegment beside
  `func_151F27E0`, while the following audio unit retains its original `-g`
  profile.
- A fresh extraction and full dependency-driven rebuild verified the CRC and
  neighboring functions. Restoring the complete CRC span also repaired a
  downstream call target, producing a canonical gain of two exact functions
  and removing the last address-drift blocker from the stable corpus.
- Verified canonical progress is now **2476 / 5973 overall (41.45%)**,
  **370 / 508 init (72.83%)**, **1940 / 5284 game (36.71%)**, and
  **166 / 181 debugger (91.71%)**.
- No further safe C port remains in the automatic comparison pool. The
  remaining exact shared routines are handwritten SDK assembly and remain
  useful only as reference evidence; looser candidates are different
  implementations or SDK variants.

### Banjo cross-port Batch 3: 15 duplicated PFS/CRC functions exact

- Completed all 15 Batch 3 targets: `__osSumcalc2`, `__osIdCheckSum2`,
  `__osRepairPackId2`, `__osCheckPackId2`, `__osGetId2`, `__osCheckId2`,
  `__osPfsRWInode2`, `__osPfsSelectBank2`, `osPfsChecker2`,
  `corrupted_init2`, `corrupted2`, `osPfsIsPlug2`,
  `__osPfsRequestData2`, `__osPfsGetInitData2`, and `func_151F27E0`.
- Reused Conker's exact primary PFS source for the 14 duplicated routines,
  with Banjo confirming the SDK implementation and `-O1` object profile.
  `func_151F27E0` uses Banjo's byte-identical `__osContAddressCrc` source.
- Split the CRC routine into its own tracked extraction subsegment and `-O1`
  object ahead of the remaining `-g` audio unit. A fresh extraction and full
  dependency-driven rebuild reproduced the layout and all 15 matches without
  regressing the checked neighboring exact functions.
- Verified linked retail-ROM progress is now **2474 / 5973 overall
  (41.42%)**, **370 / 508 init (72.83%)**, **1938 / 5284 game (36.68%)**,
  and **166 / 181 debugger (91.71%)**, with the same one address-drift
  blocker.

### Banjo cross-port Batch 2: 14 duplicated SDK functions exact

- Completed all 12 controller, SI, timer, and matrix targets in Batch 2:
  `func_151EF090`, `func_151EF288`, `func_151EF358`, `func_151EF504`,
  `func_151EF640`, `func_151EF800`, `func_151EF954`, `func_151EF9C0`,
  `osContStartReadData2`, `osContGetReadData2`, `__osSiRawStartDma2`, and
  `getTime2`.
- Recovered the adjacent `osPfsInit2` and `__osPackReadData2` copies during
  the same sweep, for a net gain of 14 byte-exact functions.
- Reused Conker's already-exact primary SDK source where available and used
  Banjo to verify the SDK implementation and compiler profile. Banjo supplied
  the missing VI-special-features and orthographic-matrix bodies directly.
  SDK I/O/OS objects matched with `-O1`, while the GU object matched with
  `-O3`.
- Verified a clean dependency-driven full rebuild followed by the linked
  retail-ROM scan: **2459 / 5973 overall (41.17%)**, **370 / 508 init
  (72.83%)**, **1923 / 5284 game (36.39%)**, and **166 / 181 debugger
  (91.71%)**, with the same one address-drift blocker.

### Banjo cross-port sweep started: first eight functions exact

- Added a temporary, evidence-ranked TODO for using every applicable source,
  compile-profile, signature, and SDK finding from the completed
  Banjo-Kazooie decompilation. The remaining work is grouped into controller,
  SI, timer, matrix, and PFS batches; handwritten assembly matches are
  reference-only.
- Completed the first eight ports: `func_15012F90`, `guMtxCatF`,
  `__osSiGetAccess2`, `guMtxL2F`, `__ull_divremi`, `__ll_mod`, `guNormalize`,
  and `__osTimerServicesInit`.
- Recovered the necessary object profiles from Banjo (`-O1`, plain `-O2`, or
  `-O3` depending on the object), avoided the graphics-header `sqrtf`
  intrinsic for `guNormalize`, and reproduced timer initialization's
  same-translation-unit 64-bit global coalescing.
- Verified the normal full build and retail-ROM scan with no neighboring
  regressions: **2445 / 5973 overall (40.93%)**, **370 / 508 init (72.83%)**,
  **1909 / 5284 game (36.13%)**, and **166 / 181 debugger (91.71%)**. This is
  a net gain of eight byte-exact functions with the same one address-drift
  blocker.

### Three-function byte-matching target completed

- Completed the requested
  `[########################] 3 / 3 (100.00%)` target:
  `func_151E50C8`, `func_15017498`, and `func_15007A70` are all independently
  byte-exact.
- Reconstructed `func_151E50C8`'s complete behavior and matched its retail
  `0x124`-byte body. The adjacent `func_151DD970` 23-byte copy helper also
  became exact at `0x74` bytes.
- Used the verified Banjo-Kazooie decompilation to confirm that IDO code
  generation depends on same-translation-unit BSS ownership. In Conker's
  generated-slice build, a correctly-sized destination definition guides IDO
  address coalescing while `pad_generated_object.py` discards the compact
  object's `.bss` and retains only text/relocations.
- Resolved the last scheduling difference with the decomp permuter: the
  matching form keeps the copy loop on one physical source line and uses an
  optimized-away `^ 0` to retain the retail register allocation.
- Verified a full production relink and drift-aware match scan. Byte-exact
  progress is now **1904 / 5284 game functions (36.03%)** and
  **2437 / 5973 overall (40.80%)**, with the same one address-drift blocker
  and no regressions.

## 2026-07-24 (continued, fourth pass - scoping a push toward 42%)

### Two more matched; the easy-win pool is now mostly exhausted

- `func_1503DF0C` and `func_150A0374` reached byte-exact: a struct-field
  read-modify-write against the already-typed `struct106 D_800C6660[]`
  array (needed the byte-index-14 field widened past `struct106`'s
  anonymous `pad[3]`), and another instance of the then/else physical-layout
  swap pattern (now fixed four times this session).
- **Scale check, since the ask was a specific percentage target:** a bulk
  scan of every non-exact C function (`ours` compiled length vs `truth`
  retail length) found roughly **3,080 functions that are still literal
  `return 0;` placeholders** with a real retail body waiting to be
  reconstructed - the actual remaining backlog is almost entirely this, not
  small scheduling diffs. Reaching 42% needs 73 more exact functions from
  a session baseline of 2,433; each one still requires the same
  manual cycle (read retail words, infer the C shape, guess field/array
  types from the few already-typed structs, build, diff, iterate) with no
  found way to batch it - a promising-looking family of ~62 near-identical
  "dispatch through a function-pointer table, then two fixed calls"
  handlers (`func_151A8584`/`func_151A85D4` and siblings in
  `generated_1D4E00.c`) turned out to hit the same argument-homing-timing
  wall as `func_151ACB60` (retail homes the incoming pointer lazily, in a
  `jalr` delay slot; our compile homes it eagerly at entry) once actually
  tried, so it isn't the multiplier it looked like.
- Reconstructed real (but not yet byte-exact) bodies for four more former
  stubs while investigating - `func_15096934`/`func_1510E634` (write a
  2-word "magic tag + pointer" node header, matching the game's node/list
  init idiom), `func_1507EEB8` (5-byte ring-buffer push/shift), and
  `func_1502C380` (read an indexed lookup table entry, fan it out to two
  fields plus a cleared counter) - all confirmed logically correct against
  retail's instructions but still differ by register choice or instruction
  order, the same resistant classes from earlier in this session. Left
  as-is rather than reverted to `return 0;`, since a real, instruction-level
  verified implementation is strictly more useful to the next session than
  a placeholder, even short of byte-exact.
- Re-tried the previously-parked `func_151E81EC` global-clear family
  (`DOCS/WORKING_NOTES.md`'s "lui-$at paired stores... cannot be reproduced
  with extern declarations") with both a scalar-externs shape and an
  array-element shape; both confirmed the same finding again - IDO emits a
  fresh `lui` per external symbol access and never reuses one `%hi` load
  across consecutive stores to different symbols the way retail's build
  did, regardless of declaration style. Still unsolved; not a source-shape
  problem.
- Verified **1902 / 5284 game functions (36.00%)** and **2435 / 5973 overall
  (40.77%)** byte-exact, same one address-drift blocker, no regressions.
  Raw C conversion remains **5973 / 6033 (99.01%)**. At the pace of this
  session (roughly 2-5 confirmed exact functions per focused pass, after
  screening out many more that hit resistant compiler-behavior classes),
  reaching 42% is a real but multi-session undertaking, not a single push -
  see the bulk-stub-scan finding above for where the remaining work
  actually lives.

## 2026-07-24 (continued, third pass)

### Five more functions matched: two libultra stubs implemented, two struct-size bugs found

- `__osSiRelAccess2` and `__osSiCreateAccessQueue2` (`game/generated_siacs2.c`)
  were still raw `return 0;` placeholders. Their non-"2" siblings
  (`__osSiRelAccess`/`__osSiCreateAccessQueue` in `libultra/io/siacs.c`) were
  already matched real implementations using the same
  `osSendMesg`/`osCreateMesgQueue`/`D_8002BE20`/`D_80042AA8` idiom; copied the
  pattern onto the "2" queue's own globals (`D_800E0D20` message buffer,
  confirmed via the linked ELF's `osCreateMesgQueue`/`osSendMesg` call targets
  at their name-implied addresses) and both went byte-exact immediately.
  `func_15149104` was the same class - an unconverted stub whose retail body
  is a single forwarding call (`func_151478F4(arg0)`, confirmed against that
  function's real signature from its other call sites) with no visible
  argument setup, meaning it just passes its own incoming `a0` straight
  through.
- `func_15194DC8`: retail's stack frame is 80 bytes, but the placeholder's
  local buffer (`f32 sp2C[3]`, passed to two undecompiled callees) only
  produced 56. Growing the buffer to `f32 sp2C[9]` (matching the 24-byte /
  6-word gap exactly) reached byte-exact in one try - the callee apparently
  writes a larger record than the `struct17` (3-float vec3) guess used at
  other call sites of the first callee, `func_1504715C`; worth revisiting
  those other sites' type later.
- `func_15195738` pattern repeats: `func_1000FE88` and `func_15019BB8` are
  the same stack-slot/frame-size class as previously-fixed
  `func_1515FBC4`/`func_15194DC8` but resisted the same tricks (adding a
  local grew the frame past retail's size instead of reusing slack); left
  for a future session.
- `func_151D7724`: retail computes `arg0 + 0x28` before evaluating the
  four-way OR condition and reuses it in the delay slot of the first
  `bnezl`, but the placeholder computed it only inside the `if` body once
  the condition was already known true. Hoisting the local's declaration to
  match retail's unconditional-early-computation order fixed the placement;
  a second, unrelated diff remained (`andi ...,0xfe` vs `andi ...,0xfffe`)
  that turned out to be a harmless mask-width difference - both produce the
  same result once the value's already come from an 8-bit `lbu`, so widening
  our literal to `0xFFFE` matched retail's source exactly with no behavior
  change. The two sibling functions in the same file (`func_151D7770`,
  `func_151D779C`) show the same `0xfe`-vs-`0xfffe` mask pattern in their own
  diffs - worth checking first next time, they may be one-line fixes.
- Tried and reverted several more candidates, all confirming already-known
  resistant classes rather than new ones: `func_1514672C` and
  `func_151254F4`/`__osSiGetAccess2` (independent-instruction/prologue
  reorder - explicit temps don't change IDO's chosen order), `func_1509D054`
  and `func_151B2FA0` (retail routes a call argument through an extra
  register/stack round-trip our compile elides), `func_1000FE88` (stack-slot
  class with only one real local, no reorder candidate), `func_1515FB70` and
  `func_100043B4` (retail computes a value it then provably discards - the
  same "dead code IDO won't reproduce" puzzle as `func_150C7930`), and
  `func_150A7770`/`func_10001420` (both are `__retail_overflow_*` trampolines
  - our correct-looking C loop body doesn't fit the tiny 8-9 word retail
  span even with `-Wo,-loopunroll,0`; retail's tight `bnezl`-based loop is
  almost certainly genuinely hand-written SDK code, same class as the COP0
  accessors and the `sin`/`cos` fallthrough trampoline from the last
  session).
- Verified **1900 / 5284 game functions (35.96%)** and **2433 / 5973 overall
  (40.73%)** byte-exact, same one address-drift blocker, no regressions in
  init or debugger. Raw C conversion remains **5973 / 6033 (99.01%)**.

## 2026-07-24 (continued)

### Three more game functions matched; two more real bugs found

- `func_1515F10C` (linked-list node removal) and `func_151F2D6C` (audio pitch
  clamp) both had the same shape: an `if`/`else` whose source order matched
  the *logic* but not retail's *physical instruction layout* - IDO put the
  other branch at the fallthrough position and this one at the jump target.
  Swapping the branch condition and its body order (same trick that fixed
  `func_151BD2BC` earlier today) made both byte-exact.
- `func_15195738`: two independent bugs in one stack-local record init.
  (1) `func_150ADA20() % 0xB` used signed division; retail's `divu` proves the
  modulus needs an unsigned operand (`% 0xBU`), matching the `% 3U` idiom
  already used elsewhere in the codebase for the same PRNG call. (2) the two
  final field writes (`sp18[5] = 1; sp18[6] = -1;`) had the right values but
  the wrong evaluation order - retail assigns index 6 before index 5. Fixing
  both (division operand type, then statement order) reached byte-exact.
- Tried and reverted three more candidates, each confirming a resistant class
  already on record: `func_1514672C` (independent-load reorder feeding a
  float compare - explicit temp did not change it, worse when tried harder),
  `func_1509D054` and `func_151B2FA0` (retail routes a call argument through
  an extra register/stack round-trip that our compile elides - adding a
  prototype for the untyped callee did not change it). `func_1000FE88` (init)
  is the same stack-slot-offset class already fixed twice elsewhere, but here
  the function has only one real local and no reordering candidate; adding a
  matching second local shifted the slot but grew the frame past retail's 32
  bytes, so reverted. `func_150AD780` turned out to be a shared fallthrough
  trampoline (`sin(x) = cos(x + pi/2)`, no `jr ra` of its own - it falls
  straight into `func_150AD78C`'s body), the same "not really its own
  function" class as `func_150A6354` from the last session.
- Verified **1895 / 5284 game functions (35.86%)** and **2428 / 5973 overall
  (40.65%)** byte-exact, same one address-drift blocker, no regressions in
  init or debugger. Raw C conversion remains **5973 / 6033 (99.01%)**.

## 2026-07-24

### Two more game functions matched; one real logic bug fixed

- `func_151BD2BC`: found and fixed an inverted-comparison bug, not just a
  matching artifact. The existing placeholder returned 1 when two byte fields
  were *unequal* and 0 when equal; retail's preset/override pattern
  (`li v0,1` before the compare, `move v0,zero` in the fallthrough) proves the
  real predicate returns 1 on equality. Swapping the comparison and return
  values makes the function byte-exact.
- `func_1515FBC4`: reordering the `index`/`temp_v1` local declarations shifted
  `temp_v1`'s stack slot from `sp+28` to retail's `sp+24`, the only remaining
  difference. Now byte-exact.
- Surveyed the smallest remaining diffs (1-3 real instruction words) for more
  candidates. Most of the rest are one of two resistant, already-documented
  classes and were reverted after confirming no source-level rewrite changes
  the output: (1) commutative-operand / independent-instruction canonicalization
  (`addu`/`multu`/`bne`/`beq` operand order, or the order of two independent
  address computations) that IDO reorders the same way regardless of source
  expression or declaration order; (2) register-choice artifacts where IDO
  picks a different scratch register for a dead value than retail
  (`func_15087FC4`/`func_15087FEC`, `func_15079F6C`, `func_15199980`). A
  fix for `func_151733D8` (adding its real 2-argument signature plus a
  per-file `-O2` no-`-g3` override to get the retail-filled branch-delay
  slot) only works by changing the whole file's compile profile, which flips
  the file's one already-exact function (`func_15173994`) to non-exact - a
  net wash, reverted per the "no regressions" rule. This limitation was
  superseded on 2026-07-26 by selecting just that function from a separately
  compiled non-debug object.
- New findings for future sessions: `func_150AC9B0`'s retail body is a bare
  `j func_150AC2D8` (no `jal`, no frame) - a real tail call, but a plain
  `return func_150AC2D8();` compiles to a full `jal`+move+`jr` sequence (2x
  the retail size); this is the only function in the entire retail corpus
  with that exact bare-tail-jump shape, so it's likely not reachable through
  normal C. `func_150A6354` is not an independent callable function at all -
  retail's own `func_150A6210` reaches it via raw `j func_150A6354` (twice,
  as a shared exit path) rather than `jal`, so it's a shared epilogue
  fragment of `func_150A6210`, not a real leaf routine with its own C
  signature.
- Verified **1892 / 5284 game functions (35.81%)** and **2425 / 5973 overall
  (40.60%)** byte-exact, with the same one address-drift blocker and no
  regressions in init or debugger. Raw C conversion remains
  **5973 / 6033 (99.01%)**.

## 2026-07-19

### Byte-exact matching crossed 40% overall

- Matched roughly 230 more game functions by reconstructing small
  generated-slice placeholders directly against retail instructions, focusing
  on repeated families: typed argument-forwarding wrappers, predicates,
  stack-local event records, jump-table dispatchers, linked-list walkers,
  clamped-store helpers, and float accumulate/scale routines.
- Root-caused a large class of mismatches to missing local prototypes in
  generated slices (implicit declarations reload narrow arguments from home
  slots instead of masking in place) and fixed whole families by adding
  per-file prototypes.
- Identified per-slice retail compile profiles: two slices build with plain
  `-O2` (filled jr-delay slots) and four need `-Wo,-loopunroll,0`; recorded the
  overrides in `conker/Makefile`.
- Corrected two wrong callee identities (`func_100111C8` vs a stale
  `func_140111C8` symbol, and `memcpy`/`bzero`/`allocate_memory`/Pi-access
  libultra callees referenced by name-implied placeholder ids).
- Verified **1860 / 5284 game functions (35.20%)** and **2393 / 5973 overall
  (40.06%)** byte-exact, with one address-drift blocker and no regressions in
  init or debugger sections.

## 2026-07-18

### Documentation topics consolidated

- Rebuilt the root README as a concise project entry point with a clearer
  status explanation, supported build overview, contribution path, and
  purpose-based documentation links.
- Reorganized `DOCS/README.md` into a subject index and made `PROJECT.md` the
  detailed source for build, environment, CI, ROM-layout, and progress
  explanations.
- Added `DOCS/CONTRIBUTING.md` as the durable home for function selection,
  byte-matching workflow, IDO-sensitive source patterns, retail-span rules,
  and required validation.
- Labeled `WORKING_NOTES.md` as an archive/scratchpad, added a topic index, and
  separated the current recovery entry from historical focus snapshots.
- Corrected and expanded the asset specification: documented the real packed
  entry bitfield and 30-entry master table, libaudio `B1`/`S1` structures,
  confirmed game-code archive/XOR layout, vertex-count ambiguity, scoped
  texture evidence, and the complete known/unknown section inventory.
- Updated `tools/asset_dump.py` to derive all `assets00-assets1C` boundaries
  from the retail master table instead of maintaining a partial hardcoded list.

### Repeated wrapper sweep reached 36.28% overall

- Matched 13 more game functions across four repeated two-function families
  and one five-function cleanup family.
- Recovered exact retail argument forwarding, indexed byte lookup, stack-local
  record dispatch, and deliberate repeated volatile field reads in call delay
  slots.
- Verified **1634 / 5284 game functions (30.92%)** and **2167 / 5973 overall
  (36.28%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast byte-matching sweep passed 35% overall

- Matched 246 additional game functions across generated slices, emphasizing
  repeated two-call wrappers, field setters, callback dispatchers, compact
  predicates, argument-forwarding helpers, and fixed-point/float leaves.
- Restored retail IDO schedules with exact argument widths, explicit temporary
  loads, direct boolean expressions, name-implied retail globals, and repeated
  wrapper templates; rejected experiments that exceeded their retail spans.
- Added the missing external routine symbol at `0x140111C8`, allowing two
  retail handle-release wrappers to link and be measured normally.
- Verified **1621 / 5284 game functions (30.68%)** and **2154 / 5973 overall
  (36.06%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast generated game sweep reached 26.02%

- Matched 45 additional compact game functions across generated slices,
  concentrating on direct wrappers, state setters, accessors, flag updates,
  indexed writes, and global resets that reproduce retail IDO code cleanly.
- Recovered exact short-function shapes through argument preservation, call
  delay-slot constants, right-to-left expression ordering, volatile pointer
  reloads where retail reads twice, and explicit field-width/sign choices.
- Kept useful partial reductions for `func_150F02A0`, `func_150CBF5C`, and
  `func_151D0128`; reverted the `func_151EFF70` experiment after its compiled
  body exceeded the retail span.
- Verified **1375 / 5284 game functions (26.02%)** and **1908 / 5973 overall
  (31.94%)**, with zero address-drift blockers and no lost exact matches.

### Difficult game near-matches recovered

- Matched `func_150779D4` and `func_15079570`, two 51- and 59-instruction
  routines that were already behaviorally correct but still differed in
  floating-point temporary allocation and a final address-register choice.
- Restored the retail expression shapes with explicit distance and threshold
  temporaries plus the native `struct127.y_position` field access.
- Matched the 54-instruction `func_1507879C` by separating its `struct197`
  pointer load from the float access, restoring retail's `v0` reuse across
  the indexed object lookup.
- Reduced the 55-instruction `func_15135480` from seven real instruction
  differences to two by restoring its reused object value and early-exit
  comparison shape; the two remaining differences are commuted branch
  operands.
- Rejected and reverted experiments that worsened `guMtxCatF`,
  `func_1505D024`, `func_1505841C`, `func_151254F4`, and `func_1514672C`.
- Verified **1330 / 5284 game functions (25.17%)** and **1863 / 5973 overall
  (31.19%)**, with zero address-drift blockers and no lost matches.

### PC-port runtime reference

- Evaluated N64 Modern Runtime as a useful Phase 1/2 candidate instead of a
  generic reference: `ultramodern` covers much of the libultra OS surface and
  `librecomp` bridges N64Recomp output plus ROM/save operations.
- Added a compatibility-inventory step and kept the runtime reference-only
  until Conker's Rare-specific code and microcode are proven compatible; no
  dependency, submodule, or ROM-build change was made.
- Added RT64 as the first renderer to evaluate before committing to a custom
  RSP/RDP display-list interpreter.

### Game byte-exact progress reached 25.11%

- Matched ten additional game functions: `func_15014220`, `func_15015644`,
  `func_15075884`, `func_15075AAC`, `func_1512D368`, `func_1514373C`,
  `func_151927C0`, `func_151D2BA4`, `func_151EEFF0`, and `func_151EF080`.
- Recovered four larger 35-45-word routines alongside compact math, state,
  copy, and generated-slice helpers by restoring retail argument constants,
  statement order, temporary-expression shapes, and the required IDO object
  profile.
- Rejected an optimization-setting tradeoff that would have lost an existing
  exact function; the clean rebuild retains every prior match.
- Published game byte-exact progress at **1327 / 5284 functions (25.11%)**
  and total byte-exact progress at **1860 / 5973 (31.14%)**. Address-drift
  blockers remain zero and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 56.89%

- Matched 26 additional init functions across PI/SI/SP raw I/O, VI state,
  message queues, thread management, timers, audio, libc, and game code.
- Restored the retail IDO `-O1` object profiles and the original
  `register`-qualified status, interrupt-mask, queue-index, and thread-walk
  locals that control allocation and scheduling.
- Reconstructed exact source shapes for `func_1000F1A8`, `func_1001AFEC`,
  `__n_nextSampleTime`, `strchr`, and `osAiSetNextBuffer`; reduced
  `func_1000FE88` from three real instruction differences to two.
- Published init byte-exact progress at **289 / 508 functions (56.89%)** and
  total byte-exact progress at **1735 / 5973 (29.05%)**. Address-drift
  blockers remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 51.77%

- Matched eight additional init functions: `ldiv`, `lldiv`,
  `__osSpRawStartDma`, `osSpTaskYielded`, `osViSwapBuffer`,
  `__osDequeueThread`, `__osTimerInterrupt`, and `__osSetTimerIntr`.
- Recorded the retail IDO optimization profiles per object and restored the
  original `register`-qualified thread-queue source shape.
- Corrected `func_1001091C` to pass the retail pointer value instead of an
  unrelated pointed-to field; the function remains one instruction from an
  exact match.
- Published init byte-exact progress at **263 / 508 functions (51.77%)** and
  total byte-exact progress at **1709 / 5973 (28.61%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress crossed 50%

- Matched 22 additional init functions, including native 64-bit compiler
  helpers, PI/SI access and raw-I/O routines, SP status helpers, VI framebuffer
  accessors, message-queue helpers, `memcpy`, `strlen`, and one audio event
  walker.
- Restored retail IDO `-O1`/`-O2` profiles, native MIPS III code generation,
  and original `register`-qualified source shapes where they determine exact
  instruction scheduling.
- Published init byte-exact progress at **255 / 508 functions (50.20%)** and
  total byte-exact progress at **1701 / 5973 (28.48%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 28%

- Reconstructed 63 compact generated-slice functions as matching C,
  including callbacks, constant handlers, scalar helpers, field initializers,
  table accessors, flag setters, and thin call wrappers.
- Preserved retail incoming registers and call-delay-slot constants through
  explicit legacy declarations, calling-convention-width parameters, and
  targeted `register` annotations.
- Reverted four exploratory near-matches so the published code batch contains
  only confirmed exact improvements.
- Published byte-exact progress at **1679 / 5973 functions (28.11%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 27%

- Reconstructed 35 small generated-slice functions as matching C, including
  typed callbacks, constant-return handlers, nested accessors, arithmetic
  helpers, and state setters.
- Preserved IDO's retail argument-home behavior and register scheduling with
  explicit calling-convention-width parameters and targeted `register`
  annotations.
- Published byte-exact progress at **1616 / 5973 functions (27.06%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Total raw C conversion crossed 99%

- Replaced 416 validated `GLOBAL_ASM` groups across 105 mixed sources and
  moved 80 tracked libultra functions through 40 typed standalone C slices.
- Extended signature discovery for nested function pointers, local `static`
  declarations, directly included source headers, macro-shadowed names, and
  legacy functions called with inconsistent argument counts.
- Generalized generated-slice Makefile and linker support to nested libultra
  assembly paths, while retaining exact retail symbol placement.
- Published raw conversion at **5973 / 6033 functions (99.01%)** and **98.34%
  by bytes**; game conversion reached **5284 / 5313 (99.45%)**.
- Recorded the complete 60-function raw remainder and the honest byte-exact
  result: **1581 / 5973 (26.47%)**, with 27 address-drift blockers.

### Total raw C conversion crossed 90%

- Added 167 validated standalone game slices and replaced 246 `GLOBAL_ASM`
  groups across the eight largest remaining mixed C sources.
- Added a reproducible mixed-source converter that reuses declared signatures,
  infers consistent legacy-call arity, and validates each referenced asm file.
- Published raw conversion at **5477 / 6033 functions (90.78%)** and **84.09%
  by bytes**; game conversion reached **4968 / 5313 (93.51%)**.
- Kept address blockers at 24. Required legacy-call signatures perturb one
  previously exact caller, leaving **1584 / 5477 (28.92%)** byte-exact.

### Total raw C conversion crossed 80%

- Replaced 82 additional safe text-only game assembly slices with generated
  non-matching C sources, moving 588 tracked functions into C.
- Taught the placeholder generator to recognize indented global entry points
  and reject retail slots smaller than the compiler's eight-byte minimum.
- Excluded one mixed code/data slice and two slices with four-byte entry spans
  instead of weakening the layout validator or dropping symbols.
- Published raw conversion at **4846 / 6033 functions (80.32%)** and **68.37%
  by bytes**; game conversion reached **4338 / 5313 (81.65%)**.
- Retained all **1585** byte-exact functions and kept address blockers at 24.

### Total and game raw C conversion crossed 70%

- Replaced 44 additional text-only game assembly slices with generated
  non-matching C sources, moving 612 tracked functions into C.
- Checked every selected slice for embedded data sections or word tables before
  replacement, then regenerated the retail-layout manifest.
- Published raw conversion at **4258 / 6033 functions (70.58%)** and **55.77%
  by bytes**; the game section independently reached **3750 / 5313 (70.58%)**.
- Preserved all prior exact matches and recovered one additional match, taking
  byte-exact progress to **1585 / 4258 (37.22%)** with 24 address blockers.

### Total raw C conversion crossed 60%

- Replaced 25 additional text-only game assembly slices with generated
  non-matching C sources, moving 613 tracked functions into C.
- Made generated-slice Makefile filtering and linker placement automatic so
  future additions no longer require duplicated hardcoded slice lists.
- Added a reproducible placeholder generator, including compact empty-body
  stubs for functions whose retail slots are only eight bytes.
- Published raw conversion at **3646 / 6033 functions (60.43%)** and **43.81%
  by bytes**. Byte-exact progress is **1584 / 3646 (43.44%)**, with all prior
  exact matches retained and one additional exact function recovered.

## 2026-07-17

### Byte-exact progress crossed 50%

- Added retail-layout manifests and build-time object re-spacing that preserve
  C-compiled instruction words and relocations while restoring function and
  object addresses.
- Kept oversized non-matching functions executable in section-local overflow
  regions through short retail-slot trampolines, preventing them from shifting
  later exact code.
- Restored generated-slice jump labels inside their padded C-derived objects
  and reduced address-drift blockers from 836 to 24.
- Published the new result: **1583 / 3033 C functions byte-exact (52.19%)**,
  with raw C conversion unchanged at **3033 / 6033 (50.27%)**.

### Tool reference triage

- Recorded `n64img` as the preferred N64 image-format reference through the
  existing n64splat dependency path (`tools/n64splat/requirements.txt` already
  requires it), avoiding a redundant standalone submodule.
- Added `N64-IPL` as a reference-only upstream for boot/IPL/header/checksum
  context.
- Left `mips-gcc-2.7.2` out of the active toolchain for now; it is useful if a
  KMC/GCC-compiled island is identified, but current matching work is still
  IDO 5.3 based.
- Updated active helper submodules after checking upstream HEADs:
  `tools/asm-differ` to `fdf9c6c`, `tools/asm-processor` to `b29ff12`, and
  the parent repo's `tools/mips_to_c` pointer to the already-checked-out
  `m2c` upstream `554de36`.

## 2026-07-14

### ROM library, EU pipeline, and censorship analysis

- All four target versions (`us`, `eu`, `debug`, `ects`) now have
  hash-verified baseroms available locally for the first time. The EU ROM
  arrived as a byte-swapped `.n64`; converted to big-endian and verified
  against `conker.eu.sha1`. (The local ROM store was reorganized mid-way and
  temporarily lost the us/ects copies; the recovery, including hash
  identification of every file in the store, is logged in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).)
- Modernized `conker.eu.yaml`/`game.eu.rzip.yaml` (and `conker/conker.eu.yaml`)
  to current splat format with version-separated output paths
  (`asm_eu`/`assets_eu`/`src_eu`), so `make extract VERSION=eu` runs clean and
  the decompressed EU code image verifies against `conker/conker.eu.sha1`.
  EU disassembly (5,759 functions) now extractable as a third matched-code
  reference alongside the `debug_proto`/`ects_proto` trees.
  `conker.debug.yaml`/`conker.ects.yaml` still need the same two-line fix.
- Analyzed the "Uncensored" US romhack as a differential probe for asset
  formats: it replaces exactly 15 of 50 `assets06` files and 23 of 453
  `assets16` files strictly in place (offset tables byte-identical). This
  confirms `assets16` as the dialogue-audio MP3 bank and pins down which
  `assets06` files carry per-dialogue-line data. A Spanish translation hack
  independently corroborates this (it rewrites `assets06` far beyond the
  censored lines - subtitle text lives there). Findings folded into
  [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md).

### Windows/WSL build environment for this checkout

- Set up and documented building directly from this Windows checkout through
  WSL (Debian distro, project venv, `binutils-mips-linux-gnu`; the bundled
  IDO recomp binaries run fine from `/mnt/c`). Exact steps and the
  incremental rebuild/verify loop are in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- The CRLF/symlink checkout corruption documented below recurred (suspected
  OneDrive interaction) and was re-fixed; diagnosis shortcut now documented:
  splat failing with `could not load segment type 'rzip'` means
  `tools/splat_ext/rareunzip.py` (a git symlink) got checked out as a text
  stub again.

### Byte-matching progress tooling

- Added `tools/match_progress.py` and a `make -C conker match-progress`
  target (add `LIST=1` for a per-function listing): for every C-converted
  function in `progress.csv`, it compares the linked ELF's disassembly
  (keyed by function symbol, so immune to the known init-section layout
  drift) against ground-truth bytes from the pristine `conker.us.bin`, and
  classifies each as byte-exact, blocked-on-callees (only `j`/`jal` targets
  differ), or still differing. This productizes the session's scratchpad
  verification method. First run: **379 / 1553 C functions byte-exact
  (24.40%)** - init 201/232, game 167/1151, debugger 11/170 - now published
  as a second snapshot table in the root `README.md`,
  [`DOCS/README.md`](README.md), and [`DOCS/PROJECT.md`](PROJECT.md).

### Function matching (continued)

- Resolved 6 more of the remaining ECTS-ported non-matching functions:
  5 now byte-exact (`func_16001B00`, `func_15060BA4`, `func_1506196C`,
  `func_150AED9C`, `func_15142A5C`), 1 logically complete pending callees
  (`func_1504CA60`). 26 remain. Two stubborn functions are documented
  non-matching with in-source comments (`func_1514143C`, `func_1507A3E8`).
- Wrote up six reusable IDO/cfe codegen idioms (register-class rules for
  named locals vs temps, `u8` field-update codegen, branch-vs-`slt` return
  forms, operand evaluation order, mips_to_c artifact locals, pointer
  folding) in [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) - read these
  before brute-forcing rewrites on the rest.

### Build environment and decomp progress

- Fixed a broken local build environment (pre-existing, not caused by this
  session): incorrect `core.symlinks`/`core.autocrlf` git config had left
  ~450 tracked files checked out with CRLF line endings and broken symlinks,
  which silently broke the IDO compiler. Fixed locally; see
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) for the exact recovery steps
  if this recurs in a fresh clone or devcontainer.
- Fixed two `tools/n64splat` submodule version-compatibility bugs in this
  project's own extension code/config (`tools/splat_ext/rzip.py`,
  `conker/conker.us.yaml`, new `conker/include/asm_processor_prelude.inc`)
  that were blocking `make extract` and the C compile entirely.
- Ported 56 functions (46 `game`, 10 `debugger`) from the untracked
  `ects_proto/` reference checkout (targets the ECTS prototype ROM) into
  this repo's `conker/src/`, replacing raw-assembly stubs with real matched
  C, and added the struct fields/globals/prototypes those functions needed.
  12 of the 56 byte-match the US retail ROM exactly out of the box; the
  other 44 compile cleanly and are marked `// NON-MATCHING: ported from
  ects_proto (ECTS ROM build), not yet byte-verified for us` pending a real
  matching pass. Also fixed one small pre-existing bug found along the way
  (a call site in `game_1944C0.c` missing an argument).
- Fixed a long-standing link-time blocker: 26 jump-table `rodata` segments
  in `conker/conker.us.yaml` were declared as standalone segments, causing
  1153 `undefined reference` errors at link time once code near them got
  matched. Changed them to `bin` (opaque byte blobs - jump table contents
  don't need symbolic disassembly). Full root-cause writeup in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- `make -C conker --jobs` → `make -C conker replace NON_MATCHING=1` →
  `make` (repo root) now runs end to end for the first time, producing a
  real (correctly non-matching, ~20% complete) `build/conker.us.z64`.
  Regenerated the progress table in [`DOCS/PROJECT.md`](PROJECT.md) from
  this working build - it's the first `.map`-file-derived count this
  checkout has actually produced, so it supersedes the previously
  documented (never locally re-verified) numbers.

### Planning docs

- Added [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md): a live, editable log of
  in-progress work, so a crashed editor/terminal/assistant session can be
  resumed from a known state instead of re-derived from scratch.
- Added [`DOCS/PC_PORT_ROADMAP.md`](PC_PORT_ROADMAP.md): a phased,
  date-free plan covering what's needed to get the game running natively on
  PC with keyboard, mouse, and controller input in a playable state, plus a
  longer-term modern-graphics phase (resolution scaling, widescreen, texture
  filtering/HD packs, enhanced lighting). No PC-port work has started; this
  is planning only.
- Linked both from the `DOCS/README.md` reading order.

## 2026-07-13

### Asset formats

- Added [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md) documenting the asset
  compression (`rzip`), the offset-table container format (confirmed against
  `func_1502B9B4` in `game_57FA0.c`), and per-type payloads.
- Confirmed findings against the retail US ROM and the debug prototype:
  RGBA5551 textures (assets00–05), MP3 streams (assets16), the `"B1"` audio bank
  header (assets17, 22050 Hz + 170-entry sample table), and container payloads.
- Corrected the earlier "assets06 = models" assumption: assets06 is composite
  object/script data (positions, float params, dialogue strings). assets08 is
  chapter-select metadata.
- Decoded the `assets13` model geometry: four-level-nested containers whose leaf
  records are `s16` XYZ vertex arrays (6 bytes/vertex, zero-padded to 16 bytes),
  validated across all 69 records; near-identical arrays within a block are
  vertex-animation frames.
- Established that `assets13` holds **only** vertex positions - 0 display-list
  markers across all 69 records - so face/UV/normal/material data is stored
  separately or built at runtime; locating it needs the model-drawing code.
- Linked the new doc from the `DOCS/README.md` reading order.

### GitHub Actions

- Updated checkout steps from `actions/checkout@v4` to `actions/checkout@v7` so workflows use the Node 24-compatible action.
- Changed the ROM build workflow to skip baserom-dependent steps when `PRIVATE_REPO_ACCESS` or `CONKER_BASEROM_US` is missing.
- Added clear workflow notices explaining which secrets are needed to enable the full ROM build.

### Documentation

- Moved repository-owned README content into the `DOCS/` folder.
- Added the `DOCS/README.md` documentation index.
- Rewrote the project overview, code sub-project notes, compressed config notes, and IDO toolchain notes for clearer reading.
- Added this update log.
- Added `DOCS/ASSET_FORMATS.md` documenting the rzip codec, the offset-table archive container (including the previously undocumented nested-compression layer inside model files), and the model/texture/audio/table payload formats.
