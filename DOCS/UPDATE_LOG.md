# Update Log

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-09-27

### Game resource-entry reset byte-exact

- Restored `func_15023440` as a `struct163` reset helper with distinct release
  and active-resource refresh paths.
- All 25 words / 100 bytes match retail directly from structured C, including
  both branch-likely paths, saved-object lifetime across the calls, and the
  final leading-halfword reset. No guarded word patches are required.
- The complete linked span has SHA-256
  `a8d81a7d4b3a413a1f964ff45762715e657657e89cd4b13c1076393c346bf7a1`.
  Fresh totals are **2,833 / 5,469 (51.80%)** overall and
  **2,261 / 4,791 (47.19%)** in Game.

### Game four-handle cleanup byte-exact

- Restored `func_151D5E30` as a four-entry cleanup loop that calls
  `func_100043B4(handle, 3)` for each nonzero handle.
- All 24 words / 96 bytes match retail. Typed C reproduces the frame, saved
  registers, unsigned-byte loop counter, call, and epilogue; three guarded
  words preserve retail's retained-handle register and non-likely null-test
  schedule.
- The complete linked span has SHA-256
  `8a7230c21df7247d5bea3fff7fefbe01360547b2e816318b17bc6455f0914653`.
  Fresh totals are **2,832 / 5,469 (51.78%)** overall and
  **2,260 / 4,791 (47.17%)** in Game.

### Game mode-driven slot updater byte-exact

- Restored `func_151AE640` as a typed callback that clears a tracked slot in
  mode zero and swaps either member of a two-word pair in mode `0x2D`.
- All 28 words / 112 bytes match retail. Structured C reproduces the byte
  argument normalization, comparisons, branch-likely path, and slot writes;
  four guarded words preserve retail's zero-mode return scheduling and the
  two local branch targets shifted by its explicit delay-slot `nop`.
- The complete linked span has SHA-256
  `290f1de7726975b100bdf3b023d45174364d7fda0e0a2060cef19eeb052d4328`.
  Fresh totals are **2,831 / 5,469 (51.76%)** overall and
  **2,259 / 4,791 (47.15%)** in Game.

### Game fixed-scale transform copy byte-exact

- Restored `func_1519EF04` as a typed transform-copy helper that scales two
  source components by `10.0f` and copies two three-float vectors.
- All 27 words / 108 bytes match retail directly from C, including the
  constant load, floating-point hazard `nop`, and final return sequence. No
  guarded word patches are required.
- The complete linked span has SHA-256
  `538df983afbd767f37e9900031a7f0012a06eb70b77d7523a944083e8f40d98c`.
  Fresh totals are **2,830 / 5,469 (51.75%)** overall and
  **2,258 / 4,791 (47.13%)** in Game.

### Game scaled transform copy byte-exact

- Restored `func_1519ED24` as a typed transform-copy helper that applies the
  shared scale to two source components and copies two three-float vectors.
- All 24 words / 96 bytes match retail. The C reproduces the data flow; five
  guarded relocation-aware word entries preserve retail's independent setup
  scheduling at the function head.
- The complete linked span has SHA-256
  `c387b23efc90a3b66e61c6405b7a0f5c85193ede03ffef9e7a2aada0ba64fa01`.
  Fresh totals are **2,829 / 5,469 (51.73%)** overall and
  **2,257 / 4,791 (47.11%)** in Game.

### Game linked-position callback byte-exact

- Restored `func_1518E298` as a four-argument callback that validates its
  linked source and copies three truncated position floats into destination
  halfwords.
- All 28 words / 112 bytes match retail directly from C. The explicit unused
  parameters reproduce the frameless argument-home stores, while nested
  positive tests reproduce the shared default-return path. No guarded word
  patches are required.
- The complete span has SHA-256
  `394557df7bda8712ee5a6684d29ccf265f919731ac1f8b0acf9a200c004bc2da`.
  Fresh totals are **2,828 / 5,469 (51.71%)** overall and
  **2,256 / 4,791 (47.09%)** in Game.

### Game display-list state helper byte-exact

- Restored `func_1517EA4C` as a three-command `Gfx` helper using
  `gDPPipeSync`, `gDPSetCombine`, and `gDPSetOtherMode`.
- All 24 words / 96 bytes match retail directly from the standard macros,
  including macro-local temporary allocation and constant-load scheduling.
  No guarded word patches are required.
- The complete span has SHA-256
  `12a220ce6dd9bd2e40cbdc7e70533c694b619289159f5ca2f20418b1ddc74acf`.
  Fresh totals are **2,827 / 5,469 (51.69%)** overall and
  **2,255 / 4,791 (47.07%)** in Game.

### Game lifetime updater byte-exact

- Restored `func_15166204` as a signed halfword accumulator plus an unsigned
  byte lifetime countdown that destroys the object when the timer expires.
- All 25 words / 100 bytes match retail directly from C. Initializing the
  timer before the accumulator and spelling expiry as the primary branch
  reproduces retail's register lifetime, branch-likely form, and dead
  duplicate store without guarded word patches.
- The complete span has SHA-256
  `1a61744e11c39328ddee4adaaf1d193d7b88382e326b16990c76e93d61b2a689`.
  Fresh totals are **2,826 / 5,469 (51.67%)** overall and
  **2,254 / 4,791 (47.05%)** in Game.

### Game scaled fixed-point clamp byte-exact

- Restored `func_1515F040` as a two-stage signed float clamp followed by an
  in-place `65536.0f` scale, truncation, and indexed `D_800DCD10` store.
- All 27 words / 108 bytes match retail. Three guarded entries move the
  independent lower-bound `lui` into the first FP comparison slot and omit
  IDO's now-redundant hazard `nop`, matching the established sibling pattern.
- The complete span has SHA-256
  `df3794fced13b76134a228cb6d09226fb5de3e875ce14f3d7a43123269755d35`.
  Fresh totals are **2,825 / 5,469 (51.65%)** overall and
  **2,253 / 4,791 (47.03%)** in Game.

### Game category-29 identity filter byte-exact

- Restored `func_151640C0` around volatile ABI parameter slots and explicit
  record, object, owner, source-ID, and target-ID lifetimes.
- All 29 words / 116 bytes match retail. Structured C restores the category
  gate, three short-circuit identity checks, branch delay loads, and conditional
  `func_1516972C` call; nine guarded words preserve retail register allocation.
- The complete span has SHA-256
  `5c7f07b4183a17f6647dd6ac0b115f58ff60fa10d84f4c0c4e04f8ec6800c8b9`.
  Fresh totals are **2,824 / 5,469 (51.64%)** overall and
  **2,252 / 4,791 (47.00%)** in Game.

### Game integer range clamp byte-exact

- Restored `func_15143DA8` as a typed three-argument range clamp with its
  volatile pointer home slot, XOR-swap lifetime, cached comparison value, and
  distinct return codes for the lower and upper clamps.
- All 24 words / 96 bytes match retail. Structured C restores the complete
  branch and delay-slot layout; nine guarded words preserve IDO's retail local
  register allocation.
- The complete span has SHA-256
  `48fe80871bb5898a546f9cc24607c2e7623247fd8d33110039c6467297c2425a`.
  Fresh totals are **2,823 / 5,469 (51.62%)** overall and
  **2,251 / 4,791 (46.98%)** in Game.

### Game cached render-mode wrapper byte-exact

- Reshaped `func_15142FBC` around an explicit cache-difference update block and
  retained display-list command pointer.
- All 34 words / 136 bytes match retail. Structured C restores the cache-hit
  branch-likely return and command-pointer lifetime; three guarded words move
  the cursor increment and `D_800DD21C` HI16 setup across independent stores.
- The complete span has SHA-256
  `2f32966b66192dae3b5e58437d96dc69ea5606a1b676b41966996d9d980460ea`.
  Fresh totals are **2,822 / 5,469 (51.60%)** overall and
  **2,250 / 4,791 (46.96%)** in Game.

### Game typed eight-float forwarding wrapper byte-exact

- Replaced the zero placeholder at `func_15133760` with its destination plus
  eight-float forwarding call to `func_15142838`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The typed callee contract preserves single-precision arguments and naturally
  reproduces the mixed GPR/stack ABI, saved source pointer, and call schedule.
- The complete span has SHA-256
  `2f32a09575c94a5c410e4972036f77aa1e3f26d4f43cbe8b57f824663f5b4809`.
  Fresh totals are **2,821 / 5,469 (51.58%)** overall and
  **2,249 / 4,791 (46.94%)** in Game.

### Game nine-argument dual dispatcher byte-exact

- Replaced the zero placeholder at `func_1513164C` with its two-call
  dispatcher. It first sends arguments 5 through 9 to `func_15131514`, then
  sends arguments 1 through 4 plus argument 9 to `func_1513137C` and returns
  the second result.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The nine-argument signature naturally reproduces the 32-byte frame, incoming
  argument home slots, stack-argument reloads, call delay slots, and epilogue.
- The complete span has SHA-256
  `d1f2ddb2fc806b978707ae893df837c78ef338cc51db51e04be4c5441ab7e941`.
  Fresh totals are **2,820 / 5,469 (51.56%)** overall and
  **2,248 / 4,791 (46.92%)** in Game.

### Game relative hierarchy-index lookup byte-exact

- Replaced the zero placeholder at `func_1510FE30` with its relative-offset
  hierarchy traversal rooted at `D_800DBE48`. Offset `+0xC` descends without
  changing the index; offset `+0x4` advances to a sibling and increments it.
- All 28 tracked words / 112 bytes match retail directly from C with no guarded
  words. A shared sibling pointer update reproduces the original branch-delay
  arithmetic, increment, null termination, and three trailing layout words.
- The complete span has SHA-256
  `3c50f9175be4aac89031574212071c25c6da4d7a2c0fb0759961dc2ad1761d74`.
  Fresh totals are **2,819 / 5,469 (51.55%)** overall and
  **2,247 / 4,791 (46.90%)** in Game.

### Game secondary object-eligibility predicate byte-exact

- Replaced the zero placeholder at `func_151028AC` with the secondary form of
  the object-eligibility predicate, using caller pointer/flag offsets
  `+0x170/+0x174`.
- All 29 tracked words / 116 bytes match retail directly from typed C with no
  guarded words. Its 26 executable words reproduce the selector, nested-owner,
  branch-likely, and flag-test schedule; generated-slice padding preserves the
  three trailing layout words.
- The complete span has SHA-256
  `46ddfc72dd6c62c3641e2897081b79a165585a68b99e031779e04614fe1b8279`.
  Fresh totals are **2,818 / 5,469 (51.53%)** overall and
  **2,246 / 4,791 (46.88%)** in Game.

### Game object-eligibility predicate byte-exact

- Replaced the zero placeholder at `func_1510281C` with its object-eligibility
  predicate. A matching selector requires a nested object whose owner's byte
  `+0x197` is clear; surviving paths return the low flag bit from the caller's
  byte `+0xD4`.
- All 26 words / 104 bytes match retail directly from typed C with no guarded
  words. Advancing the base pointer by `0x110` before addressing its selector
  at relative offset `+0x22` reproduces retail's pointer lifetime and exact
  branch-likely schedule.
- The complete span has SHA-256
  `3d65ee6d48fdac7191cf7ff9857fd9e97d6e2fae1a47af955cf3aaa91cd57994`.
  Fresh totals are **2,817 / 5,469 (51.51%)** overall and
  **2,245 / 4,791 (46.86%)** in Game.

### Game actor parameter initializer byte-exact

- Replaced the zero placeholder at `func_150FB188` with its actor-field and
  five-float stack-parameter initialization before calling `func_15157DEC`.
  It writes `-95.0f`, `-80.0f`, and zero to actor offsets `+0x54..+0x5C`,
  then forwards three zeros and two copies of `D_800A1DC0`.
- All 24 words / 96 bytes match retail. The typed C has retail's exact extent,
  frame, call, and return sequence; seventeen guarded words normalize the
  compiler's independent scheduling, FP lifetimes, and moved global relocation
  pair.
- The complete span has SHA-256
  `01144cdde22851e6ac89ae165b93f105ed789a3d297fd0e77e9773a11973a827`.
  Fresh totals are **2,816 / 5,469 (51.49%)** overall and
  **2,244 / 4,791 (46.84%)** in Game.

### Game script-gated high-flag wrapper byte-exact

- Replaced the zero placeholder at `func_150F52B0` with its script-dispatch
  wrapper. It calls `func_1509BE40(1, 0x401C, 6, 0x9000)` and sets or clears
  bit 31 of actor word `+0x84` according to the result.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The direct branch reproduces the saved incoming pointer, call delay slot,
  branch-delay reload, high-bit materialization, and shared epilogue.
- The complete span has SHA-256
  `101a6dbcb8cea8393fd0b05a1b1b5018023f189c8b26d6ef52fcdd77a01a49e1`.
  Fresh totals are **2,815 / 5,469 (51.47%)** overall and
  **2,243 / 4,791 (46.82%)** in Game.

### Game actor-state byte selector byte-exact

- Replaced the zero placeholder at `func_150F1CB0` with its ordered actor-state
  selector. Halfword `+0x84` chooses byte `+0x68`; the low two bit-pairs of
  word `+0x2E4` choose and optionally override byte `+0x69`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The ordered stores naturally reproduce both branch delay slots and the
  alias-driven `+0x2E4` reload after writing byte `+0x69`.
- The complete span has SHA-256
  `56494e88f5d715bac816b14d0224f33c4a07cf1ea3a74785482ab275bc80ce51`.
  Fresh totals are **2,814 / 5,469 (51.45%)** overall and
  **2,242 / 4,791 (46.80%)** in Game.

### Game mapped record-active predicate byte-exact

- Replaced the zero placeholder at `func_150DF8C0` with its typed predicate.
  It maps indices `0..2` through rodata bytes `0x3B, 0x3C, 0x3D`, selects the
  corresponding `0x34`-byte record from runtime table pointer `D_800D3098`,
  and tests record byte `+0x14`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  Modeling both the three-byte rodata object and record layout reproduces the
  original unaligned stack copy, relocations, strength reduction, and registers.
- The complete span has SHA-256
  `f561e7c6bf079ec34a150cf8de10d548606801d1bed3893c687a8c0cde77242b`.
  Fresh totals are **2,813 / 5,469 (51.44%)** overall and
  **2,241 / 4,791 (46.78%)** in Game.

### Game typed effect-spawn wrapper byte-exact

- Replaced the zero placeholder at `func_150C1660` with its typed wrapper around
  `func_1514C2F0`. It forwards three incoming float coordinates, supplies
  `80.0f` as the fourth float, and passes the fixed effect configuration plus
  the incoming low-byte selector through the eight stack arguments.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The recovered `u8`/`s8`/`s16` stack contracts explain the callee's original
  big-endian byte and halfword loads while reproducing the caller schedule.
- The complete span has SHA-256
  `6f7f51e26c1e53fd7518734316f89e63941584f038798f4abac9b9875903ebad`.
  Fresh totals are **2,812 / 5,469 (51.42%)** overall and
  **2,240 / 4,791 (46.75%)** in Game.

### Game tagged table-value serializer byte-exact

- Replaced the zero placeholder at `func_150B58F0` with its typed four-byte
  serializer. Global mode 1 leaves the output cursor unchanged; other modes
  write tag `0x1A`, append a halfword selected from `D_800CC34A` using the
  incoming index and a `0x32C`-byte record stride, then advance the cursor.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  IDO emits the exact branch/return schedule and shift/add/sub strength
  reduction for the record stride.
- The complete span has SHA-256
  `f6d93c4607cecde125be160a07313bf365fe1f4ad166045b96596e0b31c52600`.
  Fresh totals are **2,811 / 5,469 (51.40%)** overall and
  **2,239 / 4,791 (46.73%)** in Game.

### Game counted object-dispatch loop byte-exact

- Replaced the zero placeholder at `func_1508434C` with its typed counted
  dispatch loop. It reads the unsigned count byte at object offset `0x2C9`,
  substitutes one when that byte is zero, and calls `func_150843AC` once for
  each index from zero through count minus one.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The source reproduces retail's retained object/count/index registers,
  zero-to-one normalization, empty-loop guard, and branch-likely post-test.
- The complete span has SHA-256
  `83fcda040d8f514bb3346c5db1daf2b45d2f74d998f6dd88fca5175461716227`.
  Fresh totals are **2,810 / 5,469 (51.38%)** overall and
  **2,238 / 4,791 (46.71%)** in Game.

### Game complementary history-marker wrapper byte-exact

- Replaced the zero placeholder at `func_1507EE58` with its typed byte-history
  wrapper. It inserts the incoming marker into the five-byte history through
  `func_1507EEB8`, then inserts `0x12` after marker `0x11` or `0x11` after
  marker `0x12`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The `u8` argument contract reproduces the incoming home-slot reload, while
  the source-level `if`/`else if` emits both retail branch-likely paths, three
  call relocations, their delay slots, and the shared epilogue.
- The complete span has SHA-256
  `1d32e38706b456f78bb80f1980911262f13dc972b5e4ed4fd73191b10743c01f`.
  Fresh totals are **2,809 / 5,469 (51.36%)** overall and
  **2,237 / 4,791 (46.69%)** in Game.

### Game packed event-mask updater byte-exact

- Recovered the explicit byte lifetimes in `func_1507488C`: the packed event
  value selects an actor-local word at offset `0x2E4`, supplies an eight-bit
  mask, conditionally inverts its low-bit gate, and adds the signed top byte to
  actor byte `0x138` when that gate remains active.
- All 26 words / 104 bytes match retail. Twenty-two guarded words preserve the
  retail register and branch schedule while explicitly retaining both global
  relocations. A full rebuild exposed stale overflow output in neighboring
  `func_1506EE60`; its retained packed value and low-half ABI are corrected,
  and a guarded 19-word overflow replacement restores its retail dispatcher.
- The spans have SHA-256
  `9d7e011a25b9d1c74c33c0fbfd7b61ec7a2250fbbfdeb7a657dda5a69d7a7176`
  (`func_1507488C`) and
  `3bafca9eac8e0ba631d319f1ce8a96fe5562a95bfe3c6fc6bceb8990346ba13c`
  (`func_1506EE60`). Fresh totals are **2,808 / 5,469 (51.34%)** overall and
  **2,236 / 4,791 (46.67%)** in Game.

### Game signed-coordinate event wrapper byte-exact

- Replaced the zero placeholder at `func_15044D40` with its typed event-call
  wrapper. It converts signed coordinates at record offsets `0x6`, `0x8`, and
  `0xA` to floats, forwards the signed halfword at `0x10`, and calls
  `func_1505D1C4` with trailing arguments `0xFF, 0, 0, 0` before returning zero.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The existing position/scale record layout plus the callee's eight-argument
  declaration reproduce the complete FP schedule, stack arguments, call delay
  slot, and explicit post-call zero result.
- The complete span has SHA-256
  `b848b28be2b8e6f198978fdef7b26edb1566def1a2068d1c50f1e59ab72c736a`.
  Fresh totals are **2,807 / 5,469 (51.33%)** overall and
  **2,235 / 4,791 (46.65%)** in Game.

### Game actor-position query wrapper byte-exact

- Replaced the zero placeholder at `func_1503F904` with its typed query
  wrapper. It truncates the actor coordinates at offsets `0x14` and `0x1C` to
  signed 16-bit values and calls `func_1503F800` on the embedded data at
  offset `0x320`, forwarding the selector and constant fifth argument `1`.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The unused third incoming argument retains retail's ABI spill, while the
  five-argument call reproduces the frame, floating-point conversion schedule,
  call delay slot, and untouched return value.
- The complete span has SHA-256
  `69d25b286871e4066bd8dd2c0d9860c569f2f74a0e75e5cdd729956128995a62`.
  Fresh totals are **2,806 / 5,469 (51.31%)** overall and
  **2,234 / 4,791 (46.63%)** in Game.

### Game bounded record-byte lookup byte-exact

- Replaced the zero placeholder at `func_1503DA3C` with its indexed record
  lookup. It resolves one of the 187 pointers at `D_800D19A0`, rejects null or
  out-of-range entries with `0xFF`, and otherwise returns the requested byte
  from the optional buffer stored in the preceding `0x38`-byte header.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  The typed header reproduces the two tail fields, and a ternary nullable-byte
  expression preserves retail's joined `v1` result and branch-delay layout.
- The complete span has SHA-256
  `cd897bcd1ed09dca607a2f374dde0d76ecbdeb299e2806264d6f6a901876d3d3`.
  Fresh totals are **2,805 / 5,469 (51.29%)** overall and
  **2,233 / 4,791 (46.61%)** in Game.

### Game indexed flag predicate byte-exact

- Replaced the zero placeholder at `func_1503B95C` with its indexed flag
  predicate. It reads the flag byte at `D_800CC5CB[index * 0x32C]`, clears
  byte `0x4E` of the supplied record and rejects when bit `0x02` is set,
  rejects without mutation when bit `0x01` is set, and otherwise accepts.
- All 24 words / 96 bytes match retail directly from C with no guarded words.
  Keeping the zero-extended flag in a word-sized temporary reproduces retail's
  `v0` lifetime and complete branch/delay-slot shape.
- The complete span has SHA-256
  `65a1b3ed7d8a1c961d3a7383c20d10959fbe356696bf0083283342ae4c56ca85`.
  Fresh totals are **2,804 / 5,469 (51.27%)** overall and
  **2,232 / 4,791 (46.59%)** in Game.

### Game three-slot resource cleanup byte-exact

- Replaced the zero placeholder at `func_150233E4` with the recovered cleanup
  loop over the three `struct163` records at `D_800C3CA0`. Active records pass
  their resource pointer at offset `0x34` to `func_1516D2E0`, then clear that
  pointer and their leading active halfword.
- All 23 words / 92 bytes match retail. The shared record now exposes its
  signed active halfword and resource pointer while retaining its `0x38`-byte
  size; two relocation-aware guarded rows retain retail's independent table-end
  and cursor address-completion schedule.
- The complete span has SHA-256
  `34cb02339eb3c43068a7172810cbfbe8f197106b1f7574581056dc6d71f7f896`.
  Fresh totals are **2,803 / 5,469 (51.25%)** overall and
  **2,231 / 4,791 (46.57%)** in Game.

### Init owner-reference repair byte-exact

- Recovered `func_1000B294`, which walks the three root table entries and
  repairs matching owner links on each root and its `unk60` child by replacing
  the old owner token with the record's own address.
- All 24 words / 96 bytes match retail. An Init-object no-unroll profile and
  two relocation-aware guarded scheduling swaps reproduce the short retail
  loop; one dead initial load preserves IDO's retail register allocation
  without changing behavior.
- Neighboring `func_1000B548` remains exact across all 60 words after its
  compiler unroll was represented explicitly as four record probes per outer
  iteration. Fresh totals are **2,802 / 5,469 (51.23%)** overall and
  **391 / 497 (78.67%)** in Init.

### Game phase/scale updater byte-exact

- Recovered `func_151DADA0` around a typed state record embedded at object
  offset `0x110`. Its byte phase advances by signed rate times `D_800BE9E4`,
  the biased phase is converted through `func_151423D8`, and two state floats
  drive the output fields at offsets `0x4C` and `0x50`.
- All 34 words / 136 bytes match retail. The typed state produces the retail
  shared-base and complete floating-point schedule directly from C; four
  guarded rows retain retail's equivalent `a0` phase lifetime and explicit
  masked-argument move.
- The complete span has SHA-256
  `6723b622c69527ac88243bffdc7dc384d71bfc069638272ee12fce606ab64d8f`.
  Fresh totals are **2,801 / 5,469 (51.22%)** overall and
  **2,230 / 4,791 (46.55%)** in Game.

### Game extended record validity predicate byte-exact

- Replaced the zero-return placeholder at `func_151C2E94` with the recovered
  four-condition record predicate. It rejects the comparison record itself, a
  null leading word, ID byte `0xFF`, or extended ID byte `0xFF` at offset
  `0x127`; every other record returns one.
- All 23 words / 92 bytes match retail directly from C. The source-level early
  returns reproduce retail's branch-likely chain and duplicated delay-slot
  loads without guarded scheduling words.
- The complete span has SHA-256
  `3d887e9020b87ba223d5866416343f7fee5008bd84f8b0cfd34f972166b65edb`.
  Fresh totals are **2,800 / 5,469 (51.20%)** overall and
  **2,229 / 4,791 (46.52%)** in Game.

### Game indexed callback dispatcher byte-exact

- Replaced the zero-return placeholder at `func_151A9060` with its recovered
  object callback dispatcher. It sets object flag bit `0x04`, validates the
  signed index at offset `0x18` against the eight-entry table, and calls a
  nonnull table entry with the object and validated index.
- All 24 words / 96 bytes match retail directly from C. Restoring the callback
  as a two-argument function keeps the index live in `a1` and selects `v0` for
  the callback pointer, reproducing retail without guarded scheduling words.
- The complete span has SHA-256
  `f1dcb7d5d51145eba852cfa5ddc264f455e842703946e1ae431d42affd7d0c64`.
  Fresh totals are **2,799 / 5,469 (51.18%)** overall and
  **2,228 / 4,791 (46.50%)** in Game.

### Game linked-record event callback byte-exact

- Replaced the zero-return placeholder at `func_151A0950` with its recovered
  three-argument callback. Event `0xA` follows the link at object offset
  `0x98`; a nonnull record is accepted when either its owner word or ID byte
  matches the supplied descriptor, then `func_1519F48C` is called.
- All 25 words / 100 bytes match retail directly from C. Explicit link and
  owner lifetimes produce the retail event-branch delay slot, null
  branch-likely epilogue, comparison registers, and call relocation without
  guarded scheduling words.
- The complete span has SHA-256
  `33dcd9647ac0531f73903a0cf150dfec1dea4c1f0047fadccf54342cc478efbb`.
  Fresh totals are **2,798 / 5,469 (51.16%)** overall and
  **2,227 / 4,791 (46.48%)** in Game.

### Game timer/phase updater byte-exact

- Replaced the zero-return placeholder at `func_1517F7B4` with the recovered
  global timer and phase update. A nonzero 16-bit timer subtracts the frame
  delta with saturation at zero, then the 8-bit phase accumulator advances by
  speed times frame delta.
- All 24 words / 96 bytes match retail. The behavioral C and instruction shape
  compile directly; five guarded words retain retail's `a1` timer-base lifetime
  instead of IDO's otherwise equivalent `a0` allocation, including both
  checked timer relocations.
- The complete span has SHA-256
  `e2b43acfdd268d2a26e9aaa278219ebc73751ae9197e6e408b87412c964eef4d`.
  Fresh totals are **2,797 / 5,469 (51.14%)** overall and
  **2,226 / 4,791 (46.46%)** in Game.

### Game state-toggle event callback byte-exact

- Replaced the zero-return placeholder at `func_1514F130` with its recovered
  three-argument event callback. Event `0xD` clears the nested state byte at
  offset 9, event `0xE` sets it, and other events return the result of
  `func_1514E89C`.
- All 25 words / 100 bytes match retail directly from typed C. IDO naturally
  emits the retail branch-likely load, store delay slots, default call, and
  duplicated return-address loads; no guarded scheduling words are used.
- The complete span has SHA-256
  `63ea08e9138c95d21ba223d62a809f68cadb1a9455a21ae59f7a0b6841fef142`.
  Fresh totals are **2,796 / 5,469 (51.12%)** overall and
  **2,225 / 4,791 (46.44%)** in Game.

### Game object-request wrapper byte-exact

- Replaced the zero-return placeholder at `func_1514EE70` with the recovered
  callback ABI and typed eight-byte stack request. The wrapper forwards its
  object pointer, unique ID, zero byte, and 300-byte size to `func_1515BE50`,
  then passes the returned object to `func_1514EC1C` with event ID `0x16`.
- All 23 words / 92 bytes match retail directly from C. The frame, saved return
  address, argument home, request stores, delay slots, and both call
  relocations are compiler-produced; no guarded scheduling words are used.
- The complete span has SHA-256
  `b46f3cea976c6aa50753d281c7c1ca16951ec531127b624c67ab126b30c7af4c`.
  Fresh totals are **2,795 / 5,469 (51.11%)** overall and
  **2,224 / 4,791 (46.42%)** in Game.

### Game water-distance classifier byte-exact

- Replaced the uncertain raw-pointer implementation of `func_15125490` with a
  typed classifier over `struct108::unk3D0` and `struct127` water/position
  fields. It returns null outside water or below 100 units, the object from
  100 through 300 units, and sentinel one above 300 units.
- All 25 words / 100 bytes match retail. IDO emits a behaviorally equivalent
  26-word body with reversed `v0`/`v1` lifetimes, so 25 guarded slot rows
  replace the overflow trampoline and zero fill after checking their expected
  words and relocation state.
- The complete span has SHA-256
  `a5ffeceac1d9fab6316daf2b99daed9276cdbc0c1a0ff0b8a16f7a0cf9b696a6`.
  Fresh totals are **2,794 / 5,469 (51.09%)** overall and
  **2,223 / 4,791 (46.40%)** in Game.

### Game linked-record validator byte-exact

- Replaced the zero-return placeholder at `func_151002BC` with the recovered
  record validation, invalid-state sentinel, and optional child-state update.
- All 29 tracked words / 116 bytes match retail, including 26 executable words
  and three trailing layout nops. Seven guarded scheduling rows preserve the
  shared `-1` sentinel, ordinary invalid branches, and retail branch-likely
  child load without changing the recovered behavior.
- The complete span has SHA-256
  `fad101c81118abf40b4ecbf34251163af098d3f86db815a56c573d4216c7c90f`.
  Fresh totals are **2,793 / 5,469 (51.07%)** overall and
  **2,222 / 4,791 (46.38%)** in Game.

### Game event state/teardown handler byte-exact

- Replaced the zero-return placeholder at `func_150F4CFC` with the recovered
  `0x4E` state update and `0x4F` object teardown paths.
- All 24 words / 96 bytes match directly from C. A minimal typed record at
  object offset `0x170` preserves retail's separate base formation and flag
  access at record offset `0x24`, along with the original branch schedule.
- The complete span has SHA-256
  `5bb7259de0c805b8e28072d2011a451b4ec747eae9f5a5a69e5aacd1dc61f8c7`.
  Fresh totals are **2,792 / 5,469 (51.05%)** overall and
  **2,221 / 4,791 (46.36%)** in Game.

### Game paired-table dispatcher byte-exact

- Replaced the zero-return placeholder at `func_150DEC28` with the recovered
  byte-indexed dispatches through `D_800A0D0B` and `D_800A0D2B`.
- All 26 tracked words / 104 bytes match directly from C, including the
  23-word function body and three trailing layout nops. Its K&R byte-parameter
  definition preserves the original argument homes and narrowing without
  changing the already exact old-style caller.
- The complete span has SHA-256
  `631364ff57f69fc8abf662ae782237dd7fcdc1413a777d7270bda3ae3624c8f0`.
  Fresh totals are **2,791 / 5,469 (51.03%)** overall and
  **2,220 / 4,791 (46.34%)** in Game.

### Game event-key forwarder byte-exact

- Replaced the zero-return placeholder at `func_150D32FC` with the recovered
  event gate, object-key comparison, and four-argument record forwarder.
- All 25 tracked words / 100 bytes match directly from C, including the
  23-word function body and two trailing layout nops. A derived record pointer
  initialized before the short-circuit condition preserves retail's load,
  comparison, branch-likely, and call-argument schedule.
- The complete span has SHA-256
  `33eb62e07e9e46c86be7d1d80a40c3465c16c01b981521dbeef75de32cf2af44`.
  Fresh totals are **2,790 / 5,469 (51.01%)** overall and
  **2,219 / 4,791 (46.32%)** in Game.

### Game six-entry cleanup loop byte-exact

- Replaced the zero-return placeholder at `func_150D2054` with the recovered
  six-entry cleanup loop. Each non-null pointer in the object range at offsets
  `0x4C..0x60` is forwarded to `func_1516972C`.
- All 23 words / 92 bytes match directly from C. The byte-width loop update
  preserves retail's narrowing and branch-delay assignment, while indexed
  array syntax preserves the original commutative address operand order.
- The complete span has SHA-256
  `eeac0c230700015d8097afd16b38ab2414d2e649eff75b81f111f9843feccfaa`.
  Fresh totals are **2,789 / 5,469 (51.00%)** overall and
  **2,218 / 4,791 (46.30%)** in Game.

### Game object-index flag updater byte-exact

- Replaced the zero-return placeholder at `func_150D1410` with the recovered
  effect lookup and object-index flag update. A found effect receives byte
  `0x6E = 1` only for object-table index zero, otherwise zero.
- All 23 words / 92 bytes match directly from C. Expressing the equality as an
  explicit `if`/`else` restores retail's divide, branch-likely delay store, and
  duplicated fallthrough store without guarded words.
- The complete span has SHA-256
  `180399b2fd93bf50c1f85964a6bf46017f0bff06622fe9a97a30f2905101cff1`.
  Fresh totals are **2,788 / 5,469 (50.98%)** overall and
  **2,217 / 4,791 (46.27%)** in Game.

### Game object-record writer byte-exact

- Replaced the zero-return placeholder at `func_150BE438` with the recovered
  eight-byte record writer. It indexes `D_800CC2D0` by the `0x32C` object
  stride and writes constants `0x68` and `0x0E` around the truncated object
  fields at offsets `0x2E8` and `0x2E4`.
- All 23 words / 92 bytes match directly from C. Preserving the logical field
  assignment order reproduces retail's shift/add multiplication, load/store
  schedule, register allocation, and return without guarded words.
- The complete span has SHA-256
  `d484a1ceeb46dfcbb7716528fc3e1a2264d29e766db12234881c54607e94459a`.
  Fresh totals are **2,787 / 5,469 (50.96%)** overall and
  **2,216 / 4,791 (46.25%)** in Game.

### Game bounded-query wrapper byte-exact and function boundary corrected

- Split the former 26-word `func_150A6500` inventory row at the independent
  frame and return boundary at `0x150A6538`. The inventory now contains 6,041
  functions; `func_150A6538` remains exact original assembly until its unusual
  incoming stack contract can be recovered from source-grounded evidence.
- Replaced the public wrapper placeholder with C that forwards four register
  arguments, repeats the first two as stack arguments, and appends bounds
  `-10000` and `20000` before calling `func_150A6568`.
- All 14 words / 56 bytes of `func_150A6500` match. Twelve guarded scheduling
  words include a checked move of the call relocation to retail offset `0x20`.
  The span has SHA-256
  `be675159dec10194e305421bb202e9b9518ee517624b117e0f618135235deff0`.
  Fresh totals are **2,786 / 5,469 (50.94%)** overall and
  **2,215 / 4,791 (46.23%)** in Game.

### Game indexed-record lookup byte-exact

- Confirmed that the existing C for `func_1508855C` recovers the complete
  table-index calculation and active-record search behavior.
- All 36 words / 144 bytes match. Twenty-two guarded words preserve retail's
  register lifetimes and equivalent branch scheduling; the two guarded table
  address words preserve their original `D_800872A0` relocation identities.
- The complete span has SHA-256
  `8e59eaab129aa398368550fe589cf0991cec44face9740101ec18eb00a61c74d`.
  Fresh totals are **2,785 / 5,469 (50.92%)** overall and
  **2,214 / 4,791 (46.21%)** in Game.

### Game position/scale initializer byte-exact

- Replaced the false zero-return placeholder at `func_15044CE4` with its
  position copy, signed scale conversion, and downstream callback.
- All 23 words / 92 bytes match. Direct C emits the exact instruction skeleton;
  seven guarded words preserve retail's independent pointer and quotient
  register lifetimes without changing behavior or relocations.
- The complete span has SHA-256
  `37ca0b9557fb759016a6023c73fee1e8eb5acaf0ff92967480af03dd4bfabaf1`.
  Fresh totals are **2,784 / 5,469 (50.91%)** overall and
  **2,213 / 4,791 (46.19%)** in Game.

### Game variadic formatting wrapper byte-exact

- Replaced the false zero-return placeholder at `func_151EFF94` with its
  two-fixed-argument variadic formatter wrapper and successful-output null
  termination.
- All 23 words / 92 bytes match directly from C. Expressing the argument
  cursor as `&arg1 + 1` restores retail's four register homes, formatter reload,
  call setup, and return lifetime; no guarded retail words are needed.
- The complete span has SHA-256
  `21bed0d95f6457b0e0ebf8ba8b78072ed1f6f7883ef19bf31c9a327fbe457102`.
  Fresh totals are **2,783 / 5,469 (50.89%)** overall and
  **2,212 / 4,791 (46.17%)** in Game.

### Game position/effect wrapper byte-exact

- Replaced the false zero-return placeholder at `func_151B4E4C` with the
  established three-float position-vector wrapper shape.
- All 22 words / 88 bytes match directly from C. The wrapper forwards three
  additional floats and actor bytes `0x58` and `0x0C` to `func_151B4EA4`;
  no guarded retail words are needed.
- The complete span has SHA-256
  `9636d4a1dfde42444c22687e8308ebb8e17535d14b38bb150bd9a1628d5d31f3`.
  Fresh totals are **2,782 / 5,469 (50.87%)** overall and
  **2,211 / 4,791 (46.15%)** in Game.

### Game conditional child teardown byte-exact

- Replaced the false zero-return placeholder at `func_151A09B4` with its
  original byte-flag gate, child pointer or selector-byte match, and two-call
  teardown path.
- All 23 words / 92 bytes match directly from C, including the incoming byte
  home and narrowing, branch-likely early return, callback relocations, and
  delay slots. No guarded retail words are needed.
- The complete span has SHA-256
  `93bbe71ba0637f3ea71c346fa823b4f50f42adc38d076a45ae4ffa286dd09e22`.
  Fresh totals are **2,781 / 5,469 (50.85%)** overall and
  **2,210 / 4,791 (46.13%)** in Game.

### Game paired state-clear callbacks byte-exact

- Replaced the false zero-return placeholders at `func_1519F108` and
  `func_1519F168` with their original null-gated state-clear logic and distinct
  final callbacks.
- Both 24-word / 96-byte spans match independently. The readable C clears
  record words at `+0x58` for state 6 and `+0x60` for state 7; symmetric
  guarded scheduling restores retail's shared field base and branch targets.
- The spans have SHA-256
  `c30604a30fce7acfc9c4508dc25d815ae938bc8fb15c221b8351c2fe3f46b2c1`
  and `15a54430576641fbb8f849e8250fb8f39c1527d06c5829a84d6c89597d227412`.
  Fresh totals are **2,780 / 5,469 (50.83%)** overall and
  **2,209 / 4,791 (46.11%)** in Game.

### Game scaled query wrapper byte-exact

- Corrected `func_15197A0C` to accept its original incoming argument.
- The restored argument home supplies the one missing instruction; all 23
  words / 92 bytes then match directly from C with no guarded words.
- The complete span has SHA-256
  `79e00b19930e3d83d5baf14d43868c3332e63a76de73d420b1f301259a31d872`.
  Fresh totals are **2,778 / 5,469 (50.80%)** overall and
  **2,207 / 4,791 (46.07%)** in Game.

### Game callback/resource cleanup byte-exact

- Replaced the false zero-return placeholder at `func_151904BC` with its
  original release, callback-unregister, and resource-teardown sequence.
- All 23 words / 92 bytes match. Volatile pointer accesses preserve the
  conditional release reload, and local declaration order places the derived
  resource pointer in retail stack slot `0x18`. Five guarded words preserve
  the original null-branch and independent unregister-call setup schedule.
- The complete span has SHA-256
  `723d6af129190b4ac047acf1739e7f4abfc79a6eea5f78b62c342f3e6c336ee4`.
  Fresh totals are **2,777 / 5,469 (50.78%)** overall and
  **2,206 / 4,791 (46.04%)** in Game.

### Game paired endpoint update byte-exact

- Replaced the false zero-return placeholder at `func_1518A360` with its
  original marker-`0x2D` paired endpoint update.
- All 24 words / 96 bytes match. The recovered C swaps either matching source
  endpoint into object word `0x188` and carries source byte 8 or 9 into object
  byte `0x18D`; one guarded word selects retail's equivalent operand order for
  the second equality branch.
- The complete span has SHA-256
  `c49fa92800abfcf75e48c6d36597feb3d3c75ae58cb91fb76bb2d503beebd0ed`.
  Fresh totals are **2,776 / 5,469 (50.76%)** overall and
  **2,205 / 4,791 (46.02%)** in Game.

### Game enabled player-state initializer byte-exact

- Replaced the false zero-return placeholder at `func_15181D70` with its
  original per-player enabled-state initialization.
- All 22 words / 88 bytes match directly from C. The routine installs float
  constant `D_800A72B0`, zeroes the paired scalar and vector fields, and sets
  the player enable byte to one. No guarded retail words are needed.
- The complete span has SHA-256
  `9bc443d34ee264cb7c11bf0e6e84c6c9ca2dbd088fbb4005afd2514acd0ab072`.
  Fresh totals are **2,775 / 5,469 (50.74%)** overall and
  **2,204 / 4,791 (46.00%)** in Game.

### Game player-timer decay byte-exact

- Replaced the false zero-return placeholder at `func_1517F75C` with its
  original inclusive per-player timer decay loop.
- All 22 words / 88 bytes match directly from C. Each unsigned halfword timer
  through player index `D_80082FA0` loses the frame delta while larger than
  that delta and otherwise clamps to zero. No guarded retail words are needed.
- The complete span has SHA-256
  `4c14539ad1ebebefc3d10023afc401e7b495ec1001efaf6d0ef4ad5cbc26c7c3`.
  Fresh totals are **2,774 / 5,469 (50.72%)** overall and
  **2,203 / 4,791 (45.98%)** in Game.

### Game wrapped timer/counter byte-exact

- Replaced the false zero-return placeholder at `func_151749A0` with its
  original byte-width timer and counter update.
- All 22 words / 88 bytes match directly from C. The timer accumulates the
  frame delta with byte wrapping; crossing its threshold advances the wrapped
  counter, wraps that counter at the caller's limit, and clears the timer. No
  guarded retail words are needed.
- The complete span has SHA-256
  `1ef04391b9f03b0528bc0f1c4f9d39ed6df05e2f7125a49e456853d8507445cd`.
  Fresh totals are **2,773 / 5,469 (50.70%)** overall and
  **2,202 / 4,791 (45.96%)** in Game.

### Game object state transition byte-exact

- Replaced the false zero-return placeholder at `func_15172D28` with its
  original object state-transition behavior.
- All 22 words / 88 bytes match directly from C. The routine calls
  `func_15085430`, clears flag bit `0x10` at offset `0x2F8`, and, when the
  global mode byte is zero, writes state `3` through the object pointer at
  offset `0x31C`. No guarded retail words are needed.
- The complete span has SHA-256
  `f285d4661242ecf09be7ab29f754180e339c667a1036330afba8d6c07bd7473a`.
  Fresh totals are **2,772 / 5,469 (50.69%)** overall and
  **2,201 / 4,791 (45.94%)** in Game.

### Game two-table initializer byte-exact

- Replaced the false zero-return placeholder at `func_15172C50` with its
  original 16-entry table initialization behavior.
- All 22 words / 88 bytes match directly from C. The source assigns `-1` and
  zero to corresponding bytes in `D_800DD2B0` and `D_800DD2C0`, then stores
  the caller's value in the second table's first byte. IDO produces retail's
  four-way unrolled loop and branch-delay store. No guarded words are needed.
- The complete span has SHA-256
  `276590b6fd1af72abb45e1b76d352b988397165f8e9a5e69598a41a213e8465a`.
  Fresh totals are **2,771 / 5,469 (50.67%)** overall and
  **2,200 / 4,791 (45.92%)** in Game.

### Game effect callback adapter byte-exact

- Replaced the false zero-return placeholder at `func_15159BB0` with its
  original seven-slot callback adapter.
- All 22 words / 88 bytes match directly from C. The routine builds a position
  vector from its first three float arguments, supplies a zero velocity, and
  forwards bytes `0x0C` and `0x01` from the effect record to `func_15159890`.
  No guarded retail words are needed.
- The complete span has SHA-256
  `4ca84258ab41695df242af9177bdc89d911377839c1cc187058020c2c4d30d88`.
  Fresh totals are **2,770 / 5,469 (50.65%)** overall and
  **2,199 / 4,791 (45.90%)** in Game.

### Game signed-key list search byte-exact

- Replaced the false zero-return placeholder at `func_1514ECE0` with its
  original linked-list search by signed halfword key.
- All 23 words / 92 bytes match directly from C. The typed `s16` parameter
  reproduces retail's entry sign extension, and the existing `GameListNode`
  layout reproduces the branch-likely loop and optional result store. No
  guarded retail words are needed.
- The complete span has SHA-256
  `b86fa571f8372f319a0e24df91da420b10ef6e0d1478b06f8741b62923391112`.
  Fresh totals are **2,769 / 5,469 (50.63%)** overall and
  **2,198 / 4,791 (45.88%)** in Game.

### Game float damping threshold byte-exact

- Replaced the false zero-return placeholder at `func_15149BF4` with its
  original two-axis damping and minimum-threshold behavior.
- All 25 words / 100 bytes match directly from C. In-place updates force the
  stored first result to be reloaded, while one short-circuit OR reproduces
  retail's shared return-zero path. No guarded retail words are needed.
- The complete span has SHA-256
  `035239563829978bd71d6f260e062841506d078a1d0c22061d7c40fe8c5c24f4`.
  Fresh totals are **2,768 / 5,469 (50.61%)** overall and
  **2,197 / 4,791 (45.86%)** in Game.

### Game mode-dependent area scaler byte-exact

- Corrected `func_15144598` to read its mode from byte offset `0x15` and its
  dimensions as signed halfwords at offsets `0x06` and `0x0A`.
- All 37 words / 148 bytes match directly from C after placing case `2` before
  the shared `0/1` path and expressing the case-2 multiplication operands in
  IDO's reverse evaluation order. No guarded retail words are needed.
- The complete span has SHA-256
  `d24133a60d99d777e37a1986522ced2d3947226df1bf63479c3b2569cd62e7eb`.
  Fresh totals are **2,767 / 5,469 (50.59%)** overall and
  **2,196 / 4,791 (45.84%)** in Game.

### Game two-way type dispatcher byte-exact

- Preserved the existing behavior of `func_1513BA78`: type `1` dispatches to
  `func_15109064`, type `2` dispatches to `func_151BA468`, and other values
  return without calling either handler.
- Adding typed three-argument callee declarations makes all 23 words / 92
  bytes match directly from C. IDO now normalizes the byte argument in `a2`,
  reproducing retail's prologue and `nop` call delay slots without guards.
- The complete span has SHA-256
  `151da9e5c2e45abdfc2658142acaddc654729cd22fb97e3cfe3246a6457022fe`.
  Fresh totals are **2,766 / 5,469 (50.58%)** overall and
  **2,195 / 4,791 (45.82%)** in Game.

### Game indexed-record reset byte-exact

- Replaced the false zero-return placeholder at `func_1512D6F0` with its
  original one-argument reset of the actor-selected 104-byte table record.
- All 22 words / 88 bytes match directly from structured C, including the
  multiply-by-104 index calculation, state store, five zero-float stores, and
  final `-1.0f` store. No guarded retail words are needed.
- The complete span has SHA-256
  `de1fcbdbd7ec11e4aabe92c6ce6a332173b326d729cafdc4d5e2978c56a0c6cc`.
  Fresh totals are **2,765 / 5,469 (50.56%)** overall and
  **2,194 / 4,791 (45.79%)** in Game.

### Game paired-record updater twin byte-exact

- Replaced the false zero-return placeholder at `func_1510A8CC` with the same
  paired-record update behavior as adjacent `func_1510A870`.
- Its complete 25-word / 100-byte tracked layout matches from recovered C
  semantics plus one guarded commutative-branch operand word. The function has
  23 executable words followed by two retail layout-padding words.
- The complete span has SHA-256
  `f637c9f80def4be39e6e23fbc94349b62bb30814b7e22c6ffc593287695455ef`.
  Fresh totals are **2,764 / 5,469 (50.54%)** overall and
  **2,193 / 4,791 (45.77%)** in Game.

### Game paired-record updater byte-exact

- Replaced the false zero-return placeholder at `func_1510A870` with its
  original paired-record update behavior. For event `0x2D`, it replaces the
  destination's selected word and companion byte with the opposite source
  pair when either source word matches the destination.
- All 23 words / 92 bytes match from recovered C semantics plus one guarded
  word selecting retail's operand order for a commutative equality branch.
- The complete span has SHA-256
  `fd478fda75bdea9e1b7e81f5eff7d3c810f4609bb7f137f6a493be6fde6e5a48`.
  Fresh totals are **2,763 / 5,469 (50.52%)** overall and
  **2,192 / 4,791 (45.75%)** in Game.

### Game volatile callback-table dispatcher byte-exact

- Replaced the false zero-return placeholder at `func_151076A4` with its
  original three-argument indexed callback dispatch through `D_80088C38`.
- All 23 words / 92 bytes match directly from C. Volatile table and index
  accesses preserve retail's two record-index loads and two callback loads;
  no guarded retail words are needed.
- The complete span has SHA-256
  `c4ea7c4b5b4970d6a3c01f5e3a1695c86e46f09cf002f4750c56d9d6024a18db`.
  Fresh totals are **2,762 / 5,469 (50.50%)** overall and
  **2,191 / 4,791 (45.73%)** in Game.

### Game type-and-flag dispatcher byte-exact

- Replaced the false zero-return placeholder at `func_150FFD2C` with its
  original three-argument conditional dispatch. It accepts record types
  `0x9F` and `0xA0`, rejects records with flag `0x80` set at offset `0x94`,
  and otherwise calls `func_15081E0C(record, 4, 0)`.
- All 22 words / 88 bytes match directly from C, including unused-argument
  homes, both branch-likely epilogues, and the call delay slot. No guarded
  retail words are needed.
- The complete span has SHA-256
  `c113b829b96bfe97ffb7840abe7e9089b81c411b9dd423f97da89628aeb6300c`.
  Fresh totals are **2,761 / 5,469 (50.48%)** overall and
  **2,190 / 4,791 (45.71%)** in Game.

### Game signed-halfword mapper byte-exact

- Replaced the false zero-return placeholder at `func_150FB240` with its
  original five-argument leaf arithmetic. It stores the low byte of
  `(arg2 - arg1) * arg4` when `(arg2 - arg3) < arg1`, otherwise `0xFF`.
- All 23 words / 92 bytes match directly from C, including signed-halfword
  normalization, signed comparison, unsigned multiply, early return, and
  fallback store. No guarded retail words are needed.
- The complete span has SHA-256
  `ed9e5f96fd8e8f732dec356a12071b0c2f1ae9fbc689027f40b0592cb842106d`.
  Fresh totals are **2,760 / 5,469 (50.47%)** overall and
  **2,189 / 4,791 (45.69%)** in Game.

### Game two-stage forwarder byte-exact

- Replaced the false zero-return placeholder at `func_150FB1E8` with its
  original five-argument forwarding chain. It passes all five arguments to
  `func_151D710C`, then uses that result as the first argument to
  `func_15157F80` while replaying the remaining four.
- All 22 words / 88 bytes match directly from C, including argument homes and
  reloads, fifth-argument stack stores, both call relocations and delay slots,
  and the epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `fbb5d8ad1f5b61fff246fd8f6872d9f64fb94547d8705287f14c163b98474c00`.
  Fresh totals are **2,759 / 5,469 (50.45%)** overall and
  **2,188 / 4,791 (45.67%)** in Game.

### Game nested state classifier byte-exact

- Replaced the false zero-return placeholder at `func_150EB030` with its
  original classifier. Mode `1` and global state `4` call
  `func_151420F8(arg1)`, returning `6` or `3`; all other mode/state cases
  return `-1`.
- Nested switches preserve retail's two distinct default paths. All 24 words /
  96 bytes match directly from C, including both `-1` assignments, branch
  offsets, callback delay slot, result paths, and epilogue. No guards are used.
- The complete span has SHA-256
  `a34d5679b8a478511f46b1d6f21549808b5c1acf81b6a79448e9440a81bb660b`.
  Fresh totals are **2,758 / 5,469 (50.43%)** overall and
  **2,187 / 4,791 (45.65%)** in Game.

### Game parameter preset byte-exact

- Replaced the false zero-return placeholder at `func_150E411C` with its
  original eight-argument `func_151C3B0C` preset call, forwarding the incoming
  object, three exact float constants, global `D_800A1054`, and three `0xFF`
  values.
- All 22 words / 88 bytes match directly from C, including the global
  relocation pair, immediate float materialization, stack-argument stores,
  call delay slot, and epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `7719be748c7a2baa8892764bce224f70933275986384d391a4c0ed4dc0d77167`.
  Fresh totals are **2,757 / 5,469 (50.41%)** overall and
  **2,186 / 4,791 (45.63%)** in Game.

### Game event-bit updater twin byte-exact

- Replaced the false zero-return placeholder at `func_150D1BD0` with the
  second recovered event-bit template. Event `0x402C` sets bit `0x10` in the
  object word at `+0x84`; an inactive event clears it.
- All 24 tracked words / 96 bytes match directly from C, including call
  setup, branch and delay slot, both mask paths, epilogue, and two trailing
  padding words. No guarded retail words are needed.
- The complete span has SHA-256
  `2f7bbe6a8f54e13aca4d41dc1417f4f6b6f2af1c5181abfec7cfc76302499732`.
  Fresh totals are **2,756 / 5,469 (50.39%)** overall and
  **2,185 / 4,791 (45.61%)** in Game.

### Game event-bit updater byte-exact

- Replaced the false zero-return placeholder at `func_150BB700` with its
  original event query and object-flag behavior. Event `0x4047` sets bit
  `0x1000` in the object word at `+0x84`; an inactive event clears it.
- All 24 tracked words / 96 bytes match directly from C, including call
  argument setup, branch and delay slot, both mask paths, epilogue, and two
  trailing padding words. No guarded retail words are needed.
- The complete span has SHA-256
  `120ebe1a5434d337d45ad6cfdf8bc0db6e532efd860f38b9dee810c45f9b6204`.
  Fresh totals are **2,755 / 5,469 (50.37%)** overall and
  **2,184 / 4,791 (45.59%)** in Game.

### Game stack-record forwarder byte-exact

- Replaced the false zero-return placeholder at `func_150AF738` with the
  original behavior: build a seven-byte stack record containing
  `{1, -1, 2, arg0, 0}` and forward it with byte `arg1` and `arg2` to
  `func_1515FF74`.
- All 22 words / 88 bytes match from typed C plus fifteen guarded scheduling
  words. The guards only restore retail's rotation of independent argument,
  prologue, constant-load, and record-store instructions; the call, call
  relocation, delay slot, frame, and epilogue are emitted unguarded.
- The complete span has SHA-256
  `d2d5a6e1f37e723929f923d806d0242d7c073643f4b11c05f093a484cb5c6a7f`.
  Fresh totals are **2,754 / 5,469 (50.36%)** overall and
  **2,183 / 4,791 (45.56%)** in Game.

### Game fixed-point/float record value byte-exact

- Recovered `func_15088218` as a nullable indexed-record reader that combines
  the signed halfword at `+0x24`, shifted by four, with the truncated float at
  `+0x08` scaled by 16.
- All 22 words / 88 bytes match from the recovered C semantics plus nine
  guarded scheduling words. The guards preserve retail's index/stride
  lifetime, null-return schedule, relocations, and final commutative operand
  order; no behavior, branch condition, constant, memory access, or floating
  operation is supplied by a guard.
- The complete span has SHA-256
  `e5d5d321d70aa26986e0693c90892be508a283fd44a0fcebe53249e772f14a7f`.
  Fresh totals are **2,753 / 5,469 (50.34%)** overall and
  **2,182 / 4,791 (45.54%)** in Game.

### Game guarded mode-4 dispatcher byte-exact

- Recovered `func_15044DE8` as the guarded mode-4 variant of its neighboring
  dispatch helpers: it calls `func_1505D024` only when object-state bytes
  `0x104` and `0x125` are clear and global state is not one.
- All 22 words / 88 bytes match directly from C, including both branch-likely
  epilogues, global-state relocation, argument setup, call, and delay slot. No
  guarded retail words are needed.
- The complete span has SHA-256
  `2e614c823ff7b9d1a357dc862d044a336d070d58962e14ad022382c7e6c3a564`.
  Fresh totals are **2,752 / 5,469 (50.32%)** overall and
  **2,181 / 4,791 (45.52%)** in Game.

### Game six-ID type predicate byte-exact

- Recovered `func_1503378C` as a predicate that returns false only when object
  type byte `0x01` is `0x11` and the associated unsigned halfword is one of
  `0x3E`, `0x3D`, `0x41`, `0xD9`, `0x138`, or `0x139`.
- All 22 words / 88 bytes match directly from C, including the halfword
  preload, chained compare delay slots, final branch-likely, and both return
  paths. No guarded retail words are needed.
- The complete span has SHA-256
  `aaec9a5cbe36b7e1038be5629099576d751350b6e0d8617a4a68bf92f1300564`.
  Fresh totals are **2,751 / 5,469 (50.30%)** overall and
  **2,180 / 4,791 (45.50%)** in Game.

### Game swimming-attachment lifetime callback byte-exact

- Refined the recovered `func_15033328` C so its zero result remains live
  across the swimming-attachment lifetime checks, matching retail's register
  allocation and early-return structure without changing the behavior.
- All 32 words / 128 bytes now match directly from C, including both
  branch-likely reset stores, floating comparison, timing subtraction, and
  success return. No guarded retail words are needed.
- The complete span has SHA-256
  `41e163c146a74b2190cd422401cae4e101ac44a0b906369e1e75486b2d3215e8`.
  Fresh totals are **2,750 / 5,469 (50.28%)** overall and
  **2,179 / 4,791 (45.48%)** in Game.

### Game null-gated event-byte copy byte-exact

- Recovered `func_15023870` as the `(0xB, 2)` event handler that resolves an
  object from the fourth argument and, when non-null, copies its byte `0x3B`
  into byte `0x2A` of the indexed `D_800C35F0` record.
- All 24 words / 96 bytes match directly from C, including the event filters,
  resolver call, null gate, indexed pointer lookup, two branch-delay
  epilogues, and two trailing alignment words. No guards are needed.
- The complete span has SHA-256
  `31b6a4a8e8d8ca077e34240978a92a22b54ac3effa545273e03e30b0386abf36`.
  Fresh totals are **2,749 / 5,469 (50.27%)** overall and
  **2,178 / 4,791 (45.46%)** in Game.

### Game flagged coordinate setter byte-exact

- Recovered `func_15022190` as the flagged twin of `func_150221E8`: it stores
  three signed 16-bit coordinates and one float, then sets `D_800C3663` to one.
- All 22 words / 88 bytes match directly from C, including the incoming
  argument stores, sign-extension sequence, four global relocation pairs, and
  flag write. No guarded retail words are needed.
- The complete span has SHA-256
  `4313640b5a0c843e78e6ee6bbc03b7a274102f6275f51c7d3d02c499b485783a`.
  Fresh totals are **2,748 / 5,469 (50.25%)** overall and
  **2,177 / 4,791 (45.44%)** in Game.

### Game three-way state dispatcher byte-exact

- Recovered `func_151E7E9C` as a dispatcher from signed state byte
  `D_800E0BE9`: state two calls `func_10017870(1)`, state zero calls it with
  two, and every other state calls it with four.
- All 23 words / 92 bytes match directly from C, including both global
  relocations, three call relocations, branch delays, early epilogues, and the
  shared return. No guarded retail words are needed.
- The complete span has SHA-256
  `9e1f4c78ce7ec52e9380fa7c74c7e84150751076fb47ad086646a1af136cbe05`.
  Fresh totals are **2,747 / 5,469 (50.23%)** overall and
  **2,176 / 4,791 (45.42%)** in Game.

### Game two-mode preset wrapper byte-exact

- Recovered `func_151D4D58` as two calls to `func_151D469C` for modes zero and
  one, each using preset values `0x50`, `0xFF`, and one.
- All 21 words / 84 bytes match directly from C, including the frame, argument
  home slot, fifth stack arguments, both call relocations, delay slots, and
  epilogue. No guarded retail words are needed.
- The complete span has SHA-256
  `29e2cc5f82d51a75d33b58200a7c9fdd50236cb5e467c21010ba938403e94a61`.
  Fresh totals are **2,746 / 5,469 (50.21%)** overall and
  **2,175 / 4,791 (45.40%)** in Game.

### Game indexed record forwarder byte-exact

- Recovered `func_151D10E4` as a null-gated forwarder from object offset
  `0x1D4` into the 12-byte record table `D_800AAF9C`, indexed by the narrowed
  third argument.
- Twelve expected-word guards restore retail's byte normalization, target and
  stride register lifetimes, null-path scheduling, and relocation-aware table
  load. The call relocation and epilogue remain compiler emitted.
- The complete 21-word / 84-byte span has SHA-256
  `be6f6bade86c0c2f86c7f70e65b0555e2d868b0a1a06e05aba5523cde2bffff9`.
  Fresh totals are **2,745 / 5,469 (50.19%)** overall and
  **2,174 / 4,791 (45.38%)** in Game.

### Game conditional record forwarder byte-exact

- Recovered `func_151CF844` as a null-gated forwarding wrapper around
  `func_15169850`, using the record pointer at object offset `0x98` and its
  adjacent `+4` field.
- All 21 words / 84 bytes match directly from C, including the branch-likely
  return path, fifth stack argument, call relocation, and delay slot. No
  guarded retail words are needed.
- The complete span has SHA-256
  `63e2de29d6ff3c9de2f9df2244a8c564c82f5d4a7a354bfda47b93ce08cf6b4e`.
  Fresh totals are **2,744 / 5,469 (50.17%)** overall and
  **2,173 / 4,791 (45.36%)** in Game.

### Game dual event-record dispatch twin byte-exact

- Recovered `func_151AA210`, the instruction-identical structural twin of
  `func_151AA17C`, from the same local target/code record dispatch semantics.
- Ten separately scoped expected-word guards restore this function's retail
  scheduling and local slots; no call relocation or delay slot is patched.
- Its independent 21-word / 84-byte span matches retail with SHA-256
  `504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.
  Fresh totals are **2,743 / 5,469 (50.16%)** overall and
  **2,172 / 4,791 (45.34%)** in Game.

### Game dual event-record dispatch byte-exact

- Recovered `func_151AA17C` as construction and two-stage dispatch of a local
  target/code record, followed by the original object callback.
- The C body provides 11 of 21 words directly. Ten guarded, non-relocating
  scheduling and local-slot words restore retail's saved-register lifetime,
  record placement, and temporary choices without altering any call target or
  delay slot.
- All 21 words / 84 bytes match retail, with SHA-256
  `504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.
  Fresh totals are **2,742 / 5,469 (50.14%)** overall and
  **2,171 / 4,791 (45.31%)** in Game.

### Game coordinate-transform wrapper byte-exact

- Recovered `func_151A8F1C` as a five-argument wrapper around
  `func_151432BC`, forwarding the embedded object pointer and four float-vector
  destinations before copying the source component into the result vector.
- All 20 words / 80 bytes match retail directly from C, with SHA-256
  `d30780df86a38014cb46919b17c975e7767d1829f0b156339d10252c415e2dfd`.
  Fresh totals are **2,741 / 5,469 (50.12%)** overall and
  **2,170 / 4,791 (45.29%)** in Game.

### Game bounded callback dispatcher byte-exact

- Recovered `func_151A8A20` as a typed three-entry callback-table dispatcher.
  Selector bytes `3+` fall back to slot zero, and a non-null callback receives
  the original object, event pointer, and normalized byte argument.
- All 22 words / 88 bytes match retail directly from C, with SHA-256
  `8b82ac8d37d486ce4aa72a79997287dc4fadcd880adc9881cdd64f877cf34a8d`.
  Fresh totals are **2,740 / 5,469 (50.10%)** overall and
  **2,169 / 4,791 (45.27%)** in Game.

### Game list-tail insertion and hidden no-op byte-exact

- Recovered `func_151957B0` as a doubly linked-list tail insertion with the
  nonempty arm first and an intentional repeated old-tail load. This restores
  all 29 executable words directly from C without guarded scheduling.
- Split the complete trailing `jr ra; nop` pair from the old function extent
  into independently tracked `func_15195824`; its empty `void` body emits both
  retail words exactly.
- The combined 31-word span shares SHA-256
  `22c5d40b78c2f3bccdc1e6f6d0d4265b35303c4ef299109fd6b688c92acee6fd`.
  Fresh totals are **2,739 / 5,469 (50.08%)** overall and
  **2,168 / 4,791 (45.25%)** in Game.

### Game state-to-animation selector byte-exact

- Corrected `func_15194AB4` from an `s32` result model to its retail `void`
  contract and recovered the two state mappings through a compact `switch`.
- Assigning the default selector after the object-flag store reproduces the
  retail store, branch, and delay-slot order directly; all 26 words match
  without guarded scheduling.
- The complete span shares SHA-256
  `40de0694c6e29793a6fbb3f72e0080b97e0d8e4d940106fa98005d1c23e5aefd`.
  Fresh totals are **2,737 / 5,468 (50.05%)** overall and
  **2,166 / 4,790 (45.22%)** in Game.

### Game active-object flag scan byte-exact

- Replaced the zero-return `func_15179AB8` placeholder with its backward scan
  from `D_800DD436 - 1` through the object-pointer array in `D_800DD440`.
- Null entries and objects already carrying bit `0x2` at offset `0x90` are
  skipped. The first eligible object receives the bit and returns immediately.
  Explicit index, object, and flag lifetimes reproduce all 23 retail words
  directly without guarded scheduling.
- The complete span shares SHA-256
  `940ef12c88416ed016ef139dad5491ff725c85f7c5c9208d18932f0ede6c643b`.
  Fresh totals are **2,736 / 5,468 (50.04%)** overall and
  **2,165 / 4,790 (45.20%)** in Game.

### Game indexed-list unlink byte-exact

- Recovered `func_15168A9C` as removal from the row/index-selected
  `D_800DCE50` list, including head replacement and both neighboring-link
  repairs.
- Typed `ListNode` access plus explicit `u8 row` and `u8 index` lifetimes
  reproduce all 29 retail words directly, including the `v0`/`v1` index
  registers, `a1` slot pointer, branch-likely loads, and link temporaries.
- The complete 29-word span shares SHA-256
  `3d0eff7bee4097954ec64a6c5026e8fd390df1a7edcd8a26f92c594b4126b538`.
  Fresh totals are **2,735 / 5,468 (50.02%)** overall and
  **2,164 / 4,790 (45.18%)** in Game.

### Game callback-table loop byte-exact

- Recovered `func_1516706C` as a post-tested walk over the three callback
  entries from `D_8008CB64` through the distinct `D_8008CB70` endpoint.
- The `do/while` spelling removes the false zero-trip check and restores
  retail's direct `bnel` loop tail. Two guarded relocation-aware words preserve
  retail's independent low-half endpoint/cursor construction order.
- The complete 21-word span shares SHA-256
  `2e77ca36f960f7f9e2116dfb8a2453897fe582f432ea2d5726a978f3f2c01fa6`.
  Fresh totals are **2,734 / 5,468 (50.00%)** overall and
  **2,163 / 4,790 (45.16%)** in Game.

### Game signed fixed-point clamp byte-exact

- Replaced the empty `func_1515F0AC` placeholder with its signed float clamp:
  cap at `D_800A6524`, floor at `-32768.0f`, truncate, and store in the indexed
  `D_800DCD10` slot.
- IDO emits the correct logic as 25 words but hoists the lower-clamp `lui`
  before the first FP comparison and inserts a hazard `nop`. Three guarded
  scheduling entries swap the independent words and omit that verified `nop`;
  the padding tool now supports guarded omission with unit coverage.
- The complete 24-word span shares SHA-256
  `eb00f652ed78de4e60ec74635e029f60fed83a99c0277df0d27706c69fc97107`.
  Fresh totals are **2,733 / 5,468 (49.98%)** overall and
  **2,162 / 4,790 (45.14%)** in Game.

### Game flag-gated callback dispatcher byte-exact

- Replaced the zero-return `func_15131C2C` placeholder with its `0x4000`
  object-flag gate and indexed `D_80089878` callback dispatch.
- The typed callback contract preserves all three incoming arguments, including
  retail's stack spill and unsigned-byte narrowing of the third argument.
  Both null exits compile as retail's branch-likely shared epilogue.
- The complete 22-word span shares SHA-256
  `0f9c9edd02a198a0416dc76b94408c401a85dd821f1989840c3d9a54023f4dec`.
  Fresh totals are **2,732 / 5,468 (49.96%)** overall and
  **2,161 / 4,790 (45.11%)** in Game.

### Game handwritten vector cross product restored

- Reclassified the `func_150AD8B0` generated-slice placeholder to its original
  19-word vector cross-product assembly body while retaining equivalent C as
  documentation.
- IDO `-O2` and `-O3` both emit a 21-word body with an FP hazard `nop` and an
  empty return delay slot. Retail uses a tightly interleaved schedule with the
  final component store in the return delay slot.
- The complete 240-byte tracked slice shares SHA-256
  `7ae7de32b7fe1c2acc411a544cf6b1f5a38233ceb2c6ae35ce0f892d59f65948`.
  Fresh C-only totals are **2,731 / 5,468 (49.95%)** overall and
  **2,160 / 4,790 (45.09%)** in Game.

### Game backing-buffer reset byte-exact

- Recovered `func_1505DFDC` as a conditional reset of the object backing
  buffer, including the `0x3A0`-byte clear and two selector-byte writes.
- A full-width index and two direct `D_800C4ED0` reads recover retail's stack
  slots and repeated load. Declaration and source store order reproduce all
  remaining IDO scheduling directly, without guarded retail words.
- The complete 33-word span shares SHA-256
  `715ebfa81ced3911f6b4616b912c1f45f7373229d091f13f28d99674fcc05eff`.
  Fresh totals are **2,731 / 5,469 (49.94%)** overall and
  **2,160 / 4,791 (45.08%)** in Game.

### Game four-timer handwritten assembly restored

- Reclassified `func_15125628` from a behaviorally equivalent C model to its
  maintained original 26-word assembly body.
- Retail independently expands each timer-byte load and store through separate
  symbol-address macros. IDO C always combines those accesses unless given
  false single-use symbols, so keeping it in the C queue was misleading.
- The complete 104-byte linked and retail spans share SHA-256
  `ea2a21dfd73b25f4db3c08366068559df6e0985d32ba0a86af22edd3e74542ac`.
  Fresh C-only totals are **2,730 / 5,469 (49.92%)** overall and
  **2,159 / 4,791 (45.06%)** in Game.

### Game marker-record swap byte-exact

- Replaced the zero-return `func_150E2FC0` placeholder with its marker-gated
  comparison and swap between the first two words of the source record.
- Matching either source word updates the destination word at `0xDC` and its
  paired selector byte at `0xDA`. Typed C emits 23 of 24 tracked words; one
  guarded word preserves retail's equivalent alternate-first branch operands.
- The complete 24-word span shares SHA-256
  `815e571938eeb39d9ffeae2889c41574f46c2fa15e9b608e8ccc12d0e8dff23f`.
  Fresh totals are **2,730 / 5,470 (49.91%)** overall and
  **2,159 / 4,792 (45.05%)** in Game.

### Game mode-flag toggle byte-exact

- Replaced the zero-return `func_150C5310` placeholder with its call to
  `func_150C5280`, conditional `0x20000` bit update at offset `0x60`, and
  constant true return.
- Typed C reproduces the complete routine directly, including its frame,
  delay slot, branches, shared return, and three tracked padding words. No
  guarded retail-word replacement is used.
- The complete 24-word span shares SHA-256
  `0179e738632a005405b2a6cbec57c8da5a8f6b66f9707772bf19f68c884fcdf7`.
  Fresh totals are **2,729 / 5,470 (49.89%)** overall and
  **2,158 / 4,792 (45.03%)** in Game.

### Game packed actor-mask clear byte-exact

- Recovered `func_1507A47C` as a packed four-byte mask that clears the
  corresponding bits in the current actor's `unk94` field.
- A named mask local preserves the retail extent. Eighteen guarded,
  relocation-aware words restore IDO's independent byte-load, actor-access,
  shift, OR-tree, complement, and field-update schedule.
- The complete 22-word span shares SHA-256
  `45861dbacdfafde2e9941b698382ca182e210932c1f210c4d95ce0388da56e3c`.
  Fresh totals are **2,728 / 5,470 (49.87%)** overall and
  **2,157 / 4,792 (45.01%)** in Game.

### Game state-transition wrapper byte-exact

- Replaced the zero-return `func_15155F3C` placeholder with its lookup and
  state transitions: `2 -> 0`, `3 -> 2`, and all other states unchanged.
- One retained state-byte local reproduces the complete retail control flow.
  Three guarded words preserve only IDO's `a0` versus retail `v1` register
  choice for the load and two comparisons.
- The complete 21-word span shares SHA-256
  `0119e77d17efbde4d25797a1ebcd4419b5641efec94faf73ec7d9be6bf5fe34d`.
  Fresh totals are **2,727 / 5,470 (49.85%)** overall and
  **2,156 / 4,792 (44.99%)** in Game.

### Game stack-vector sum wrapper byte-exact

- Replaced the zero-return `func_150EB430` placeholder with its three-component
  vector sum and forwarding call to `func_150EB484`.
- Reversing each commutative source addition reproduces retail's load order and
  floating-register choices. Four guarded words preserve only the compiler's
  `a2` versus retail `a3` lifetime for the retained second vector.
- The complete 21-word span shares SHA-256
  `bb57799e7e106d77a3a3c05e720507b9841d7179ad06170cde91cf5dccc1a7ee`.
  Fresh totals are **2,726 / 5,470 (49.84%)** overall and
  **2,155 / 4,792 (44.97%)** in Game.

## 2026-09-26

### Game flag-gated record update byte-exact

- Replaced the zero-return `func_150C7968` placeholder with its initial
  `func_15116110` call and flag-gated optional-record byte update.
- Compact C emits 20 words. Five guarded entries swap the independent global
  and record loads, move the signed source read before the null test, preserve
  both global relocations, adjust the outer branch, and insert retail's dead
  `D_800DBEF4 + 0x1E0` pointer advance.
- The complete 21-word span shares SHA-256
  `44bd9f87969d7f78f53c6889bbcefec767a3c726977b9b281e3f9cc353457889`.
  Fresh totals are **2,725 / 5,470 (49.82%)** overall and
  **2,154 / 4,792 (44.95%)** in Game.

### Game existing-record wrapper twin byte-exact

- Replaced the zero-return `func_150C6870` placeholder with the `+0x70`
  structural twin of the preceding existing-record activation and allocator
  wrapper.
- The same typed owner and wrapper lifetimes reproduce all 21 retail words,
  including the two-argument `func_150C68C4` call, without a retail-word patch.
- The complete span shares SHA-256
  `20817a804dc0355c5d9ffea271db0521cd85aac833f0dfa7653ea887b002e5fb`.
  Fresh totals are **2,724 / 5,470 (49.80%)** overall and
  **2,153 / 4,792 (44.93%)** in Game.

### Game existing-record wrapper byte-exact

- Replaced the zero-return `func_150C5F40` placeholder with its existing-record
  activation and allocator path.
- Typed owner and wrapper lifetimes reproduce the preloaded `+0x18` owner,
  embedded `+0x58` activation byte, two-argument allocator call, call-delay
  spill, and returned `+0x5C` record directly, without a retail-word patch.
- The complete 21-word span shares SHA-256
  `5809aac14fd7051e9acbf5960f6c29c0e8557a442bacb5c54804f44d028b1d93`.
  Fresh totals are **2,723 / 5,470 (49.78%)** overall and
  **2,152 / 4,792 (44.91%)** in Game.

### Game four-slot release loop byte-exact

- Replaced the zero-return `func_150C522C` placeholder with its four-entry
  optional release loop over `D_800D98D0`.
- Typed cursor/end pointers reproduce 19 of 21 retail words directly. Two
  guarded relocation-aware words preserve retail's equivalent ordering of
  the independent `D_800D98E0` and `D_800D98D0` low-half completions.
- The complete 21-word span shares SHA-256
  `fe3eecef23e97693912477fffab1907f920f93615fa711342dcd7c82ebb484df`.
  Fresh totals are **2,722 / 5,470 (49.76%)** overall and
  **2,151 / 4,792 (44.89%)** in Game.

### Game conditional callback and hidden no-op byte-exact

- Recovered `func_15178750` as a typed conditional forwarding wrapper whose
  fallback result is the incoming object pointer.
- Identified `0x151787A4` as a separate two-word no-op callback referenced by
  `D_8008CB64`, added tracked symbol metadata, and split the retail inventory
  so fresh extraction regenerates both the code label and table relocation.
- Both functions, 23 words and 92 bytes combined, share SHA-256
  `f307fce3f160a10be38bf97d7a75d49ddee5383998957b956b7498a21c236cd9`.
  Fresh totals are **2,721 / 5,470 (49.74%)** overall and
  **2,150 / 4,792 (44.87%)** in Game.

### Game reverse-slot update byte-exact

- Replaced `func_1515D030`'s early returns with retail's shared result lifetime
  and made the slot-byte decrement explicitly signed.
- IDO now reproduces the initial true result, branch-likely false assignment,
  signed wrap test, wrapped slot selection, and shared return path without a
  retail-word patch.
- The complete 22-word span shares SHA-256
  `52ace76263f53fd9e73fcad2e3e753d4bdd6d1060db7b2381385b6662dce7021`.
  Fresh totals are **2,719 / 5,469 (49.72%)** overall and
  **2,148 / 4,791 (44.83%)** in Game.

### Game object-index wrapper byte-exact

- Corrected the local `func_15083E90` declaration to return an object pointer
  and accept the byte identifier used by `func_15083FB0`.
- That byte-parameter contract makes IDO emit retail's pre-call normalization,
  empty call delay slot, object-table base register, index division, and
  compact return epilogue directly, without a retail-word patch.
- The complete `func_15083FB0` span shares SHA-256
  `903332ebe2d5ba12e58c9139e884b7c32ffd83b60f3c6211225b7df5bea4368c`.
  Fresh totals are **2,718 / 5,469 (49.70%)** overall and
  **2,147 / 4,791 (44.81%)** in Game.

### Game two-event release callback byte-exact

- Replaced the zero-return `func_151D8D5C` placeholder with its release
  handling for event bytes `0x58` and `0x47`.
- The typed object/float/byte callback signature and explicit event branches
  reproduce the unused float home, normalized event byte, two distinct call
  sites, and branch-likely exit without a retail-word patch.
- The complete span shares SHA-256
  `dbb07e5309308e508f7a463a934b4a9c6499b6129bff1d6e74dbc0b015987aac`.
  Fresh totals are **2,717 / 5,469 (49.68%)** overall and
  **2,146 / 4,791 (44.79%)** in Game.

### Game optional record release byte-exact

- Replaced the zero-return `func_151B8318` placeholder with its optional
  matching-record release gate.
- Typed pointer traversal and an explicit supplied-record word reproduce the
  byte-flag normalization, pointer-or-tag match, branch-likely mismatch exit,
  and release call without a retail-word patch.
- The complete span shares SHA-256
  `9943dcd929ed73f90c0a377ed615475e599d1ae6b60e9243438c146009649cb7`.
  Fresh totals are **2,716 / 5,469 (49.66%)** overall and
  **2,145 / 4,791 (44.77%)** in Game.

### Game validated-position reader byte-exact

- Replaced the zero-return `func_151B7678` placeholder with its pointer-chain
  validation and three-float position copy.
- A short-circuit empty-record or tag-mismatch failure reproduces retail's
  shared zero-return block, branch-likely success path, duplicated scheduled
  float load, and all 21 words without a retail-word patch.
- The complete span shares SHA-256
  `b6be4112a6bbc89160af04c63a144617a2f1d834e34c138fc78fc2089f63d57b`.
  Fresh totals are **2,715 / 5,469 (49.64%)** overall and
  **2,144 / 4,791 (44.75%)** in Game.

### Game second float ABI adapter byte-exact

- Replaced the zero-return `func_151B50A4` placeholder with its complete
  seven-argument adapter into `func_151B50F4`.
- The typed wrapper shared with `func_151AF338` reproduces the mixed o32
  hard-float argument homes, local three-float vector, byte extraction, and
  forwarding sequence without a retail-word patch.
- The complete span shares SHA-256
  `480b14e5919e75a4efab526e78c6895aa7d95e3090cd7d1a868dd32d37a20dfe`.
  Fresh totals are **2,714 / 5,469 (49.63%)** overall and
  **2,143 / 4,791 (44.73%)** in Game.

### Game embedded cleanup dispatch byte-exact

- Replaced the zero-return `func_151B4C1C` placeholder with its embedded
  cleanup and optional callback dispatch.
- Typed pointer and callback lifetimes reproduce retail's `+0x140` cleanup,
  callback lookup from `D_8008FB70` by byte `+0x44`, branch-likely null return,
  and indirect call without a retail-word patch.
- The complete span shares SHA-256
  `a08bf8588f3eb11ac0c886027a1db252f1fe639ea88ad592cff9cebea2a533ab`.
  Fresh totals are **2,713 / 5,469 (49.61%)** overall and
  **2,142 / 4,791 (44.71%)** in Game.

### Game float ABI adapter byte-exact

- Replaced the zero-return `func_151AF338` placeholder with its complete
  seven-argument adapter into `func_151AF388`.
- Typed float parameters reproduce the o32 hard-float homes, local three-float
  vector, three forwarded scalar floats, and byte loaded from offset `0xC` of
  the final pointer argument without a retail-word patch.
- The complete span shares SHA-256
  `6d681cd9d26d447146cef46aef99e2567bb2edbf0a3833b27aa03352edde2b87`.
  Fresh totals are **2,712 / 5,469 (49.59%)** overall and
  **2,141 / 4,791 (44.69%)** in Game.

### Game bounded embedded-owner release byte-exact

- Replaced the zero-return `func_151A73EC` placeholder with its bounded release
  and clear of the pointer stored at object offset `0x174`.
- Nested typed conditions reproduce retail's signed `< 0x20` gate, both
  branch-likely return paths, interior-pointer spill across `func_1516972C`,
  and all 20 words without a retail-word patch.
- The complete span shares SHA-256
  `019efff64d8d7ce0f17f9f3d54d94649404be7cb4852b79daa15023147b58f6d`.
  Fresh totals are **2,711 / 5,469 (49.57%)** overall and
  **2,140 / 4,791 (44.67%)** in Game.

### Game embedded-address setup wrapper byte-exact

- Replaced the zero-return `func_15192308` placeholder with its complete call
  to `func_15131C84`, forwarding one object field and five embedded addresses.
- The typed six-argument call reproduces retail's `0x28`-byte frame, retained
  `s0` lifetime, unused second-argument home, stack-argument order, call delay
  slot, and all 20 words without a retail-word patch.
- The complete span shares SHA-256
  `8376d022e1edf5b1dd28744f7ee1198c93438ac0a7acea02d3b09240cf2f60a1`.
  Fresh totals are **2,710 / 5,469 (49.55%)** overall and
  **2,139 / 4,791 (44.65%)** in Game.

### Game shifted motion-decay update byte-exact

- Replaced the zero-return `func_1518F108` placeholder with its two float
  decay updates and conditional scaled-byte calculation.
- The body is the shifted-field twin of `func_1514A498`; its factor, limit,
  and scale live at offsets `0x154`, `0x158`, and `0x15A`.
- Direct C reproduces 20 of 21 retail words. One guarded non-relocating patch
  preserves retail's equivalent `multu v0,t7` operand order.
- The complete span shares SHA-256
  `3ffe7494afd5ff6f15b2c609f15b61cf689c756363214ebc03ea988c4bb71059`.
  Fresh totals are **2,709 / 5,469 (49.53%)** overall and
  **2,138 / 4,791 (44.63%)** in Game.

### Game per-slot state reset byte-exact

- Replaced the zero-return `func_15181DC8` placeholder with its complete reset
  of two indexed scalar floats, one indexed float pair, and one state byte.
- Direct C emits the complete behavior in 19 words. Two guarded entries insert
  retail's redundant `mtc1 zero,$f4` and use `$f4` for only the first store;
  the remaining stores retain the compiler's `$f0` zero.
- The complete span shares SHA-256
  `46a4fcb449b8f5cab466a5e009ace1fafb9aec11abd05a64d76dc5db6496b189`.
  Fresh totals are **2,708 / 5,469 (49.52%)** overall and
  **2,137 / 4,791 (44.60%)** in Game.

### Game motion-decay update byte-exact

- Replaced the zero-return `func_1514A498` placeholder with its two float
  decay updates and conditional indexed byte calculation.
- Direct C reproduces 20 of 21 retail words. One guarded non-relocating patch
  preserves retail's equivalent `multu v0,t7` operand order instead of IDO's
  canonical `multu t7,v0`.
- The complete span shares SHA-256
  `4325a1e4fbe15bca49875d5f4799d57884826a356ff97ae78ad0b22b03e21939`.
  Fresh totals are **2,707 / 5,469 (49.50%)** overall and
  **2,136 / 4,791 (44.58%)** in Game.

### Game conditional stack-record wrapper byte-exact

- Replaced the zero-return `func_150F2390` placeholder with its complete
  conditional `struct17` construction and submission path.
- The typed local and low-byte cast reproduce retail's stack layout,
  branch-likely restore, byte reload, and both call delay slots across all 20
  words.
- The complete span shares SHA-256
  `7990c285682c470388437b0da8386a307ca4e58dce971a9b1b16819b8e0c3abb`.
  Fresh totals are **2,706 / 5,469 (49.48%)** overall and
  **2,135 / 4,791 (44.56%)** in Game.

### Game constant preset wrapper byte-exact

- Replaced the zero-return `func_150EC45C` placeholder with its typed call to
  `func_151C3B0C`, forwarding the object with three `1.0f` scales, `0.0f`,
  and three `0xFF` channel values.
- The direct call reproduces retail's float-register setup, reverse stack
  argument stores, and all 21 tracked words without a retail-word patch.
- The complete span shares SHA-256
  `286cfe5e6e7390c73018d14668a98f0ca33576873782a1ea1b5ce26dac6ab473`.
  Fresh totals are **2,705 / 5,469 (49.46%)** overall and
  **2,134 / 4,791 (44.54%)** in Game.

### Game event-flag handler byte-exact

- Replaced the zero-return `func_151087FC` placeholder with its event-byte
  dispatch for setting or clearing bit zero in the offset-`0x30` flag byte.
- Modeling the offset-`0x28` state as one initialized interior-object pointer
  lets IDO sink the address calculation independently into both branches,
  reproducing all 21 tracked words.
- The complete span shares SHA-256
  `79a176792d390d8b8fb0b0b77f55b7e2d332e2be6bbce79269abc52aafe01ea1`.
  Fresh totals are **2,704 / 5,469 (49.44%)** overall and
  **2,133 / 4,791 (44.52%)** in Game.

### Game two-pass list lookup byte-exact

- Corrected `func_150319CC` so both searches retain each node's next pointer
  before testing the current node, matching retail's `v1` current-node and
  `v0` next-node lifetimes.
- The complete 33-word span shares SHA-256
  `f8a247eb9795d103d7ccdfbf5fcf438e8d563b2164901157b401e44b4d611c4c`.
  Fresh totals are **2,703 / 5,469 (49.42%)** overall and
  **2,132 / 4,791 (44.50%)** in Game.

### Game conditional submission wrapper byte-exact

- Replaced the zero-return `func_1502E474` placeholder with its complete
  conditional indexed-pointer submission and completion-flag update.
- Correcting `D_800C3E7A` to `u16` and using it directly in the condition and
  call reproduce retail's `a1` address/value lifetime and all 20 words.
- The complete span shares SHA-256
  `57242216c7ecf9676d6561c4c19d0d06ea0b3e217660676bcd1140454ccaf708`.
  Fresh totals are **2,702 / 5,469 (49.41%)** overall and
  **2,131 / 4,791 (44.48%)** in Game.

### Game volatile callback dispatch byte-exact

- Corrected `func_151D73A8` so the callback-table index and entry are both
  read twice, matching retail rather than being common-subexpression reduced.
- A local table-base pointer with volatile index and entry reads reproduces all
  23 retail words while retaining the typed three-argument callback call.
- The complete span shares SHA-256
  `57531c17795eef924bf98ddf2b9a699f1dac86900db25b0a68b855dada588fee`.
  Fresh totals are **2,701 / 5,469 (49.39%)** overall and
  **2,130 / 4,791 (44.46%)** in Game.

### Game slot-state predicate byte-exact

- Replaced the zero-return `func_151B22F4` placeholder with its complete
  one-based slot-index and owner-state predicate.
- Signed pointer-distance division by the `0x32C` record stride plus typed
  field loads reproduce all 21 retail words directly from C.
- The complete span shares SHA-256
  `0831d55fc5252d7dd1179e8eb002d59cc94a5f0e0a074103537cee91c689d0d9`.
  Fresh totals are **2,700 / 5,469 (49.37%)** overall and
  **2,129 / 4,791 (44.44%)** in Game.

### Game embedded-owner release handler byte-exact

- Replaced the zero-return `func_151A4F7C` placeholder with its complete
  event-zero comparison against the embedded record at object offset `0x28`.
- The direct short-circuit condition reproduces the delayed pointer setup and
  all 21 retail words without guarded words or compiler-steering expressions.
- The complete span shares SHA-256
  `0bd405af9a6aebab3730df73a5236f99bdc9e8078ae9b36038f9554135498794`.
  Fresh totals are **2,699 / 5,469 (49.35%)** overall and
  **2,128 / 4,791 (44.42%)** in Game.

### Game unregister-and-broadcast wrapper byte-exact

- Replaced the zero-return `func_15191B8C` placeholder with its complete
  global-word snapshot, target unregister, and event broadcast sequence.
- The typed byte argument reproduces retail's big-endian stack-byte reloads;
  the local one-word record reproduces all 21 retail words directly.
- The complete span shares SHA-256
  `bf392e47a547c97973ce4acb9c2d4e4fb27927996a73ec68d090289742bfc0cc`.
  Fresh totals are **2,698 / 5,469 (49.33%)** overall and
  **2,127 / 4,791 (44.40%)** in Game.

### Game event-owner release handler byte-exact

- Replaced the zero-return `func_15190400` placeholder with its complete
  event-zero owner/discriminator matching and object-release call.
- Explicit field temporaries and the nested early-return comparison reproduce
  all 21 retail words directly from typed C. The final source operand swap
  preserves retail's `bnel a3,a2` register order without guarded words.
- The complete span shares SHA-256
  `b8231fb73fe2d92e312651d44bba9e27a8a684800ea1891f132a18d280083a39`.
  Fresh totals are **2,697 / 5,469 (49.31%)** overall and
  **2,126 / 4,791 (44.37%)** in Game.

### Game indexed color extractor byte-exact

- Replaced the zero-return `func_15187FC0` placeholder with its complete
  bounds-checked extraction of three record bytes into three 32-bit outputs.
- Nested bounds checks and `arg0 * 36` indexing reproduce all 20 retail words
  directly from typed C, without guarded words or compiler-steering code.
- The complete span shares SHA-256
  `24ab31b6bdb61df664e09424955ba7447d6ef120f39a5300999b79db4b371b1a`.
  Fresh totals are **2,696 / 5,469 (49.30%)** overall and
  **2,125 / 4,791 (44.35%)** in Game.

### Game node initializer byte-exact

- Replaced the zero-return `func_15178BE4` placeholder with its complete
  selector lookup and node-field initialization.
- Correct `u8`, pointer, and `s16` formal types reproduce all 20 retail words
  directly, including the big-endian signed-halfword stack reload.
- The complete span shares SHA-256
  `9c710896056e8c17946409cb801951aba3733dc00c0ed26a65bfb8a36b277773`.
  Fresh totals are **2,695 / 5,469 (49.28%)** overall and
  **2,124 / 4,791 (44.33%)** in Game.

### Game linked-list key lookup byte-exact

- Replaced the zero-return `func_1514ED3C` placeholder with its complete
  20-word linked-list search, including optional matched-node output.
- A typed node header plus separate current/next pointer lifetimes reproduces
  every retail branch-likely delay slot directly, without guarded words.
- The complete span shares SHA-256
  `10caa2bb84bec91148134f5ebee3b7856aad744979f985e503f3860cc03b5d65`.
  Fresh totals are **2,694 / 5,469 (49.26%)** overall and
  **2,123 / 4,791 (44.31%)** in Game.

### Game active-player-mask predicate byte-exact

- Completed all 20 words of `func_151464B8`, which builds a signed 16-bit mask
  for active player indices and reports whether the caller's halfword has no
  active-player bits set.
- Recovered the `u8` return, explicit `i`-then-`mask` initialization order, and
  masked-value lifetime. Optimized-away `^ 0` and all-ones masking retain
  retail's final IDO register allocation without guarded instruction words.
- Linked `0x151464B8..0x15146508` and pristine retail share SHA-256
  `39b706408f76f7e1676a9c8d19fce2a64ed7d81da41e115e35b876a8ccf2e25e`.
  The fresh scan is **2,693 / 5,469 (49.24%)** overall and
  **2,122 / 4,791 (44.29%)** in Game.

### Game integer range wrapper byte-exact

- Completed all 19 words of `func_151444DC`, which repeatedly wraps an integer
  into the inclusive range bounded by `arg2` and `arg1`.
- Expressing both adjustment paths as `do/while` loops makes IDO materialize
  the complete step before its first use and reproduces both retail
  branch-likely delay-slot updates directly, with no guarded words.
- Linked `0x151444DC..0x15144528` and pristine retail share SHA-256
  `682c1fbc5ae2acf2b0199b940b022a45b7610905e88ae616c2dd5ae974104416`.
  The fresh scan is **2,692 / 5,469 (49.22%)** overall and
  **2,121 / 4,791 (44.27%)** in Game.

### Handwritten Game bitstream helpers restored

- Restored `func_151F892C` and `func_151F8960` from false zero-return C
  placeholders to their original 13-word assembly bodies. Both use paired
  `lwl`/`lwr` loads; the first also consumes non-ABI live `t0` and `s1` state.
- Their complete linked 52-byte spans independently match retail with SHA-256
  `e1bcfb7ac1912e9ca1986dacb6e16db8ea7c1b0b9c9a192ce35b789a44739cd6`
  and `a5c0dbc044b26fe073f7e493a8977b0ed69b6ef729eab087d2b973d3b7ee6af7`.
- Fresh accounting is **2,691 / 5,469 (49.20%)** exact C functions overall
  and **2,120 / 4,791 (44.25%)** in Game. The exact handwritten rows are
  intentionally excluded from the C matcher denominator.

### Init TLB unmap routine restored

- Replaced the empty `osUnmapTLB` C placeholder with its original 16-word
  libultra assembly body. The routine saves CP0 EntryHi, writes Index and both
  EntryLo registers, executes `tlbwi`, observes the hazard nops, and restores
  EntryHi.
- The complete linked 64-byte span matches retail with SHA-256
  `2fea954023376ffbe406e320314f3a2b6cf1acddb591e2fc0754e2259c01bf3b`.
- Fresh accounting is **2,691 / 5,471 (49.19%)** exact C functions overall
  and **390 / 497 (78.47%)** in Init. The exact SDK assembly row is excluded
  from the C matcher denominator by design.

### Init full data-cache writeback restored

- Replaced the empty `osWritebackDCacheAll` C placeholder with its original
  12-word libultra assembly body. The routine issues handwritten cache writeback
  operations across the complete `0x2000`-byte data-cache range.
- The complete linked 48-byte span matches retail with SHA-256
  `9e2e910cf2dcf19b0d2826eea41187a62acc4584b8fb7316cc74acbd40f4b04f`.
- Fresh accounting is **2,691 / 5,472 (49.18%)** exact C functions overall
  and **390 / 498 (78.31%)** in Init. The exact SDK assembly row is excluded
  from the C matcher denominator by design.

### Handwritten Init MMIO setup restored

- Restored `func_100038E0` from an equivalent C conversion to its original
  11-word assembly body. Retail retains the MMIO address in return register
  `v0` and materializes the two `0x4040` stores independently in `t6` and `t7`.
- The complete linked 44-byte span matches retail with SHA-256
  `2afa60e885db40dd282ff0cf18ffe43a5716521c18c5c235975bcf8cb84d97f4`.
- Fresh accounting is **2,691 / 5,473 (49.17%)** exact C functions overall
  and **390 / 499 (78.16%)** in Init. The exact original assembly row is
  intentionally excluded from the C matcher denominator.

### Handwritten Init memory-clear loop restored

- Restored `func_10001420` from a false C conversion to its original nine-word
  assembly loop. The C body requires ten words and therefore linked through an
  overflow trampoline instead of reproducing the retail extent.
- Retail uses `a1` as the moving pointer, `a0` as the end pointer, and performs
  each zero store in the loop branch delay slot. The complete linked 36-byte
  span matches retail with SHA-256
  `a4726841f3477fedc98f9ff44c74f6cb613b2950e7d1c9434a0f61dbda17bdbf`.
- Fresh accounting is **2,691 / 5,474 (49.16%)** exact C functions overall
  and **390 / 500 (78.00%)** in Init. The original assembly row is exact but
  intentionally excluded from the C matcher denominator.

### Init release-loop bound refresh byte-exact

- Completed all 47 words of `func_1000FD38`, which finds matching resource
  records, releases an optional owned object, and marks each record inactive.
- Six guarded words restore retail's control-flow schedule: no-call iterations
  retain the cached loop bound, while the release-call path refreshes it before
  loading and updating the record flags. The `D_80042760` HI/LO relocations
  move with that reload.
- Linked `0x1000FD38..0x1000FDF4` and pristine retail share SHA-256
  `d6c4a2d813bb07d09cda2a9aee5f4cb54f9e0ac388a66f9f0265775945c171e6`.
  The fresh scan is **2,691 / 5,475 (49.15%)** overall and
  **390 / 501 (77.84%)** in Init.

### Init header-tag update byte-exact

- Completed all 22 words of `func_100043B4`, which replaces the high tag byte
  in the word immediately preceding the caller's pointer while preserving the
  low 24 bits under an interrupt-mask save/restore pair.
- Six guarded words restore retail's pre-call store, move the second
  `osSetIntMask` relocation, retain a dead `arg0 - 3` adjustment in its delay
  slot, and shift the unchanged epilogue. A direct source assignment was
  tested and rejected because IDO eliminates it.
- Linked `0x100043B4..0x1000440C` and pristine retail share SHA-256
  `96bbbe8d7fc2767413fc9f85d64896d95b633d867cc2b61023c410a9646d2616`.
  The fresh scan is **2,690 / 5,475 (49.13%)** overall and
  **389 / 501 (77.64%)** in Init.

### Handwritten Init interrupt wrappers restored

- Restored `__osDisableInt` and `__osRestoreInt` from false zero-return/no-op
  C placeholders to their original handwritten CP0 assembly ownership.
- The disable wrapper reads Status, clears `SR_IE`, writes Status, and returns
  the former interrupt-enable bit. The restore wrapper reads Status, merges the
  saved bit, writes Status, and preserves the required hazard/alignment nops.
- Their complete linked 32-byte spans match retail with SHA-256
  `b5ec893cd5c1e37c723f982142b67fc24befcf35b6e48b596abbcca4c4d44560`
  and `760fabe684a57096a1f98fb972d27fc9ae0f5b227768fa227ed73c15b4ad1e09`.
  The exact numerator remains **2,689**, while corrected C inventory is
  **5,475 / 6,038 (90.68%)** overall and **501 / 538 (93.12%)** in Init.
  The matcher is **2,689 / 5,475 (49.11%)** overall and
  **388 / 501 (77.45%)** in Init.

### Init current-pointer helper byte-exact

- Completed all 26 words of `func_1000FE88` while retaining its recovered C
  behavior: validate the index, optionally release the record resource, set
  bit `0x80` in the record word, and return success or failure.
- Two guarded, non-relocating words move the live current-pointer spill and
  reload from compiler-selected frame slot `0x18` to retail slot `0x1C`.
  Frame size, control flow, register lifetimes, call relocation, and the other
  24 words already matched.
- Linked `0x1000FE88..0x1000FEF0` and pristine retail share SHA-256
  `2468ea4fa2e9ade3f4f573e236236195922ecb3b8673d3543c19095073a2243d`.
  The fresh scan is **2,689 / 5,477 (49.10%)** overall and
  **388 / 503 (77.14%)** in Init.

### Adjacent Init control-register wrappers restored

- Restored handwritten `__osSetSR` and low-level SDK `__osSetFpcCsr` from
  false no-op/zero-return C placeholders to original assembly ownership.
- `__osSetSR` now preserves retail's `mtc0`, hazard `nop`, return, and delay
  slot. `__osSetFpcCsr` preserves the `cfc1` old-value read followed by the
  `ctc1` update. No guarded word patches were added.
- Their complete linked 16-byte spans match retail with SHA-256
  `8c9798aafb630c54a679991a2a686c3379687a94f8b3c8c14e5eafe1cd8cb961`
  and `1b1c2a5e117a433a988d960120310c5634987537358a5b13b49fddcee5d2dac4`.
- The fresh scan is **2,688 / 5,477 (49.08%)** overall and
  **387 / 503 (76.94%)** in Init. The next ordinary Init C candidate is
  26-word `func_1000FE88`, with two real differences.

### Handwritten Init CP0 wrappers restored

- Restored `__osGetSR`, `osGetCount`, and `__osSetCompare` from false C
  zero/no-op placeholders to their preserved handwritten assembly ownership.
  IDO C cannot express the required `mfc0`/`mtc0` operations.
- The generated-slice `GLOBAL_ASM` path now inserts minimal extracted bodies,
  while each preserved libultra source remains the authority for its complete
  four-word retail slot. No guarded word patches were added.
- Independent 16-byte linked-versus-retail comparisons pass with SHA-256
  `98eb78e5220bcc1e31ff049202bde4471c76ac15ebbc22d818771f741671fe0a`,
  `49439260d2ea325fd9d1049a302274c512c90775bbc3751b54513b65152f01ae`,
  and `424b05c5a5a48f29b4669731a97ea63a5ee362e2b47fa58afc9317487695229c`.
- The exact numerator remains **2,688**, while the corrected C denominator is
  **5,479** overall and **505** in Init. The fresh scan is
  **2,688 / 5,479 (49.06%)** overall and **387 / 505 (76.63%)** in Init.

### Record/owner match callback byte-exact

- Converted `func_15133DE8` from a zero-return placeholder to its real
  three-argument callback. When its event byte is zero, matching either the
  record's 32-bit identifier or following byte against owner fields
  `+0x7C/+0x80` dispatches `func_1516972C`.
- An explicit record-identifier lifetime restores retail's persistent `v0`
  allocation and the exact `t7/t8/t9` comparison temporaries. All 21 words,
  including branch-likely epilogues and the call relocation, compile directly
  from C without guarded rows.
- Linked `0x15133DE8..0x15133E38` and pristine retail
  `conker.us.bin+0x161298` share SHA-256
  `90076a0b24263542cb4bd2d6d371c257b8c5cd3c03c1160ff420bf9ea7cdf8bf`.
  The fresh scan is **2688 / 5482 (49.03%)** overall and
  **2120 / 4793 (44.23%)** game.

### Event-bit callback byte-exact

- Converted `func_150FADC8` from a zero-return placeholder to its real
  three-argument callback ABI. Event `0x53` sets bit `0x2` in the owner word
  at offset `0x58`; event `0x54` clears it.
- The natural typed `if`/`else if` implementation reproduces all 20 retail
  words directly, including both argument homes, byte normalization, the
  early-return store delay slot, and the signed `~2` mask. No guarded rows are
  required.
- Linked `0x150FADC8..0x150FAE14` and pristine retail
  `conker.us.bin+0x128278` share SHA-256
  `d5ecec1757d0c3cb4b0029f249451874134a13c2e94381cf7c0408d6bd066a96`.
  The fresh scan is **2687 / 5482 (49.01%)** overall and
  **2119 / 4793 (44.21%)** game.

### Float threshold mapper byte-exact

- Converted `func_150F34A0` from a zero-return placeholder to its real
  two-argument floating-point implementation. Values below `-5.0f` are
  transformed by `arg1 * D_800A1980 + D_800A1984`; other values return
  `0.75f`.
- The natural local-result C form reproduces all 21 retail words directly,
  including the argument home store, branch-likely delay slot, both global
  relocations, arithmetic schedule, and shared floating-point return path.
- Linked `0x150F34A0..0x150F34F0` and pristine retail
  `conker.us.bin+0x120950` share SHA-256
  `6d6c36748842f9c5cbab4fb19be66043bbefb79055a5b5e4cfe1625bcda8dd9d`.
  The fresh scan is **2686 / 5482 (49.00%)** overall and
  **2118 / 4793 (44.19%)** game.

### Buffer-advance helper byte-exact

- Recovered `func_150CFE98`'s retail expression lifetimes by removing the
  one-use `ptr38`, `field10`, and `len` locals and assigning the advanced
  buffer pointer inside the `func_150CFD84` call.
- The source now emits every semantic instruction, register, branch, call,
  and delay-slot schedule directly. Seven guarded words preserve only the
  retail 32-byte frame and its owner/buffer-state spill slots.
- Linked `0x150CFE98..0x150CFF0C` and pristine retail
  `conker.us.bin+0xFD348` share SHA-256
  `2324732635eb02dc1675a8a8928f4d551e8d425e0751a1a08beb25ef70d755cd`.
  The fresh scan is **2685 / 5482 (48.98%)** overall and
  **2117 / 4793 (44.17%)** game.

### Original handwritten PRNG step restored

- Restored `func_150ADA20` from its maintained behavioral C equivalent to the
  original 18-word MIPS III assembly body. The C form compiled to 19 words and
  therefore occupied an out-of-line overflow section behind a slot trampoline.
- Preserved the verified C equivalent under `#if 0`. Retail's strict
  source-order shifts, assembler-style self-base seed load, independent seed
  store, compact `a0`/`a1`/`a2` register reuse, and useful return-delay
  `dsra32` are now represented directly by the extracted original body.
- Linked `0x150ADA20..0x150ADA64` and pristine retail
  `conker.us.bin+0xDAED0` share SHA-256
  `040875e60d965f65ffa115c2fbc6a46afadd210d3daa55d6fd1ba1c1b5accfd2`.
  This classification correction leaves the exact numerator at **2,684**;
  the fresh scan is **2684 / 5482 (48.96%)** overall and
  **2116 / 4793 (44.15%)** game.

### Translation matrix initializer byte-exact

- Corrected `func_150A7DA0` from raw integer identity constants to four
  floating `1.0f` diagonal stores while preserving the caller's three raw
  translation words at offsets `0x30`, `0x34`, and `0x38`.
- Retained IDO's interleaved store schedule with the recovered empty branch
  and label source shape, then added six guarded rows for the independent
  `f0`/`f4` register choices and final return-delay schedule. The patch table
  now contains 1,125 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA7DA0` and pristine retail `conker.us.bin+0xD5250`
  share SHA-256
  `a0acd238bcbd6bedcd98c66c0eeb58fe64efddb28dd7aa1b179fecdc5dcc4e96`.
  Fresh scan: **2684 / 5483 (48.95%)** overall and
  **2116 / 4794 (44.14%)** game, with debugger unchanged at **181 / 181**.

### Matrix identity element byte-exact

- Corrected `func_150A7CB0`'s final identity element from an integer
  `0x3F800000` store to the recovered floating `1.0f` store. This restores
  retail's opening `lui`/`mtc1` pair and final `swc1` while preserving the
  raw-word matrix components and zero fill.
- Added three guarded rows for IDO's remaining final-store schedule: float
  store, return, then final zero store in the return delay slot. The patch
  table now contains 1,119 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA7CB0` and retail ROM `0xD5160` share SHA-256
  `d6a1e950c51300de8a005337398173f3f308e6b4b263fcbaebab1267f8ce93b2`.
  Fresh scan: **2683 / 5483 (48.93%)** overall and
  **2115 / 4794 (44.12%)** game, with debugger unchanged at **181 / 181**.

### Record gate wrapper converted and byte-exact

- Replaced `func_150A34B0`'s zero-return placeholder with its complete record
  gate: return zero when byte `0x14` equals `1`, call `func_150A3504(arg0)`
  when byte `0x15` has both low bits clear, and otherwise return zero.
- The call-positive source order reproduces retail's branch-likely duplicated
  byte load, preloaded zero result, low-bit test, call, and shared epilogue
  directly from C. No guarded rows were added; the patch table remains at
  1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0xA34B0` and retail ROM `0xD0960` share SHA-256
  `fb9edd181a18b5c89565ce4898cf3549dc72d810b57d7f04578cb572abaddeef`.
  Fresh scan: **2682 / 5483 (48.91%)** overall and
  **2114 / 4794 (44.10%)** game, with debugger unchanged at **181 / 181**.

### Selector init wrapper converted and byte-exact

- Replaced `func_1509E8A0`'s zero-return placeholder with its complete
  three-argument callback contract. Selector `7` forwards the first argument
  to `func_1000E0F8`, selector `8` forwards it to `func_1000E8F0`, and all
  other selectors return zero.
- The two-case `switch` reproduces retail's incoming `a2` spill, comparison
  chain, calls, return values, shared epilogue, and two padded words directly
  from C. No guarded rows were added; the patch table remains at 1,116 unique
  rows with zero duplicate keys.
- Linked ELF `.game+0x9E8A0` and retail ROM `0xCBD50` share SHA-256
  `6cb20288b9c0d04cb6020064f8ce112235044f1ac1eff97063a03cdad6d33617`.
  Fresh scan: **2681 / 5483 (48.90%)** overall and
  **2113 / 4794 (44.08%)** game, with debugger unchanged at **181 / 181**.

### Indexed record deactivation byte-exact

- Simplified `func_15088780` by removing its one-use record-pointer local and
  expressing the target address in retail's table-base-plus-scaled-index
  order. The behavior remains unchanged: clear record byte `0x31`, then clear
  the corresponding bit in `D_800D2394`.
- The source shape restores retail's complete post-call register allocation,
  so all 30 words now match directly from C. No guarded rows were added; the
  patch table remains at 1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0x88780` and retail ROM `0xB5C30` share SHA-256
  `c70d2601cd04ee0b936cb95e64238adc7d0e652f7e66e903f39f4cfe2ba79e33`.
  Fresh scan: **2680 / 5483 (48.88%)** overall and
  **2112 / 4794 (44.06%)** game, with debugger unchanged at **181 / 181**.

### Scaled table reader byte-exact

- Confirmed `func_150881CC`'s existing C behavior: return zero for a null
  table, otherwise read the float at `table + index * 0x84`, scale it by
  `256.0f`, and truncate it to `s32`.
- Added five guarded rows that retain retail's copied index and computed
  pointer registers without obscuring the recovered behavior. The patch table
  now contains 1,116 unique rows with zero duplicate keys.
- Linked ELF `.game+0x881CC` and retail ROM `0xB567C` share SHA-256
  `227423c851572c4f05742c91087d60334e216d39e9efa44f811ad6dc6b3a92eb`.
  Fresh scan: **2679 / 5483 (48.86%)** overall and
  **2111 / 4794 (44.03%)** game, with debugger unchanged at **181 / 181**.

### Object-selector record wrapper converted and byte-exact

- Replaced `func_1506AC0C`'s zero-return placeholder with its complete local
  record construction: object pointer in word zero and object byte `0x3B` in
  byte four, followed by `func_151B7328(&record, 0, 8, 0xFF, 1)`.
- The typed record reproduces retail's frame, incoming spills, payload stores,
  five call arguments, delay slot, and epilogue directly from C. No guarded
  rows were added; the patch table remains at 1,111 unique rows.
- Linked `0x9808C` and retail `0x980BC` share SHA-256
  `d6b76d7ce1622ade285c6a6b5b364fd243ea0794725e02515fa4990891d223ae`.
  Fresh scan: **2678 / 5483 (48.84%)** overall and
  **2110 / 4794 (44.01%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback forwarding byte-exact

- Corrected `func_151B82CC`'s callback-table contract so a selected callback
  receives the original object pointer, integer argument, and byte argument.
  A separate child-pointer local restores the selector-load lifetime.
- IDO now reproduces retail's byte spill and zero extension, `v0` child
  pointer, `v1` callback, table lookup, null branch, indirect call, and
  epilogue directly from C. No guarded rows were added; the patch table
  remains at 1,111 unique rows.
- Linked `0x1E574C` and retail `0x1E577C` share SHA-256
  `e8095c4ad32badb28ba75115586cce130c72a73b44a9c39a00c22ec7f7389baf`.
  Fresh scan: **2677 / 5483 (48.82%)** overall and
  **2109 / 4794 (43.99%)** game, with debugger unchanged at **181 / 181**.

### Gated byte-result chain converted and byte-exact

- Replaced `func_1519257C`'s zero-return placeholder with its complete call
  chain. A zero `func_15192308` result returns zero; a nonzero result gates a
  `func_15192358` call, and the selected call's low byte is returned.
- Separate full-width and byte result locals recover retail's full-width zero
  test, both masks, and shared return path. No guarded rows were added; the
  patch table remains at 1,111 unique rows.
- Linked `0x1BF9FC` and retail `0x1BFA2C` share SHA-256
  `6fa2ab2ca7daf2cf8c3d1ced76a4176bcf5b66029fc45fa455b7964fd90a52a8`.
  Fresh scan: **2676 / 5483 (48.81%)** overall and
  **2108 / 4794 (43.97%)** game, with debugger unchanged at **181 / 181**.

### Selector linked-list lookup converted and byte-exact

- Replaced `func_15178B98`'s zero-return placeholder with its complete lookup:
  walk from `D_800DCF38`, compare selector byte `0x34`, follow next pointer
  `0x08`, and return the matching node or zero.
- The direct loop reproduces both retail branch-likely instructions, the null
  paths, early return, and duplicated next-pointer load. No guarded rows were
  added; the patch table remains at 1,111 unique rows.
- Linked `0x1A6018` and retail `0x1A6048` share SHA-256
  `c90feae04990328b11469fe19f238fd17925d37dd5be53fc0c9df139b6c63333`.
  Fresh scan: **2675 / 5483 (48.79%)** overall and
  **2107 / 4794 (43.95%)** game, with debugger unchanged at **181 / 181**.

### Two-word template dispatcher converted and byte-exact

- Replaced `func_1515572C`'s zero-return placeholder with its complete typed
  wrapper: copy the two-word `D_800A6038` template to a local record and call
  `func_15169260` with kind `2`, the data pointer, and byte selector.
- The template copy, selector spill and zero extension, relocation pair, call,
  frame, epilogue, and three trailing padded nops match directly from C. No
  guarded rows were added; the patch table remains at 1,111 unique rows.
- Linked `0x182BAC` and retail `0x182BDC` share SHA-256
  `944cf9c1d5c4ad797dfd79c5dc99f879a68303faccdd6a7f279fb7077bbc0413`.
  Fresh scan: **2674 / 5483 (48.77%)** overall and
  **2106 / 4794 (43.93%)** game, with debugger unchanged at **181 / 181**.

### Six-argument forwarding wrapper converted and byte-exact

- Replaced `func_15130374`'s zero-return placeholder with its direct
  six-argument call to `func_15130280`, preserving the callee's return value.
  The fourth input is now typed as `u8`, which recovers retail's incoming
  `a3` spill and low-byte reload from the big-endian argument-home slot.
- The complete frame, argument register shuffle, two stack arguments, call,
  and epilogue match directly from C without guarded rows. The patch table
  remains at 1,111 unique rows with zero duplicate keys.
- Linked `0x15D7F4` and retail `0x15D824` share SHA-256
  `184a83f8a6398738fccde102155bf4ddd03b35140388f4548245a78aaf418eb0`.
  Fresh scan: **2673 / 5483 (48.75%)** overall and
  **2105 / 4794 (43.91%)** game, with debugger unchanged at **181 / 181**.

### Nullable coordinate-copy wrapper converted and byte-exact

- Replaced `func_1511F92C`'s zero-return placeholder with its complete
  lookup-and-copy behavior. A nonnull `func_151149AC` result supplies the
  three signed halfwords at offsets `0x10`, `0x12`, and `0x14`.
- An explicit retained destination pointer recovers retail's `a1` spill and
  reload around the call. The function and three authored trailing nops match
  directly from C without guarded rows; the patch table remains at 1,111
  unique rows.
- Linked `0x14CDAC` and retail `0x14CDDC` share SHA-256
  `8640e14c5975fc467cd18311e1eb4d66accd1db351c5dad86efe81635ba5440b`.
  Fresh scan: **2672 / 5483 (48.73%)** overall and
  **2104 / 4794 (43.89%)** game, with debugger unchanged at **181 / 181**.

### State-gated owner check converted and byte-exact

- Replaced `func_15116930`'s zero-return placeholder with its complete
  21-word behavior. It requires object flag `0x04`, rejects existing state
  bits at offset `0x73`, validates the owner's byte at offset `0x57`, and
  transitions the object state to bit `0x02`.
- Retaining `arg1 + 0x31C` as an owner-slot address gives IDO the exact retail
  state-byte and owner-pointer lifetimes. All instructions match directly
  from C, with no guarded rows; the patch table remains at 1,111 unique rows.
- Linked `0x143DB0` and retail `0x143DE0` share SHA-256
  `c5c323dece9963de7032c222fae4dbd364fe18d5a94e0da60766d8cf3e62566a`.
  Fresh scan: **2671 / 5483 (48.71%)** overall and
  **2103 / 4794 (43.87%)** game, with debugger unchanged at **181 / 181**.

### Wrapping signed-byte counter byte-exact

- Completed all 20 words of `func_1508CA88`. It increments the signed object
  byte at offset `0x1703`, returns values below `D_8008FD90`, and wraps the
  byte to zero at the limit.
- Signed accesses and a shared return recover nineteen retail words directly.
  Two guarded rows retain retail's independently hoisted final
  `D_800D23B0` reload. Both padding tools now support and test symbolic
  relocations on inserted words. The patch table is 1,111 unique rows with no
  duplicate keys.
- Linked `0xB9F08` and retail `0xB9F38` share SHA-256
  `5329f59db01e662472dbd6eb6a3f48747d1c3dfdd94fa66d5fbeada21b9403cf`.
  Fresh scan: **2670 / 5483 (48.70%)** overall and
  **2102 / 4794 (43.85%)** game, with debugger unchanged at **181 / 181**.

### Selector-table byte conversion byte-exact

- Replaced `func_150849CC`'s zero-return placeholder with its complete
  19-word behavior. It derives a zero-based selector from byte `0x1C9`, falls
  back to byte `0x2C8`, optionally returns the selector through `arg1`, and
  returns the selected byte from the table pointer at offset `0x2C4`.
- The recovered C emits every operation, register, delay slot, and memory
  access directly in an equivalent 18-word CFG. Three guarded rows extend two
  branch distances and retain retail's redundant fallback branch. The patch
  table is now 1,109 unique rows with no duplicate keys.
- Linked `0xB1E4C` and retail `0xB1E7C` share SHA-256
  `69dd64e52454a5db16aa031021fd5e6ee7c1a1a0140673367baad3924113ab24`.
  Fresh scan: **2669 / 5483 (48.68%)** overall and
  **2101 / 4794 (43.83%)** game, with debugger unchanged at **181 / 181**.

### Selected actor-state cleanup byte-exact

- Completed all 23 words of `func_150747E4`. When the active object's slot
  byte is nonzero, it selects `D_800CC2D0[slot - 1]`, clears that actor's
  pointer at offset `0x218`, and stores the low byte of `D_800D1580` at
  offset `0x232`.
- Explicit selected-slot, decremented-index, full-width update-value, and
  actor-pointer lifetimes recover the retail stride calculation, load timing,
  final `a0` pointer, stores, branch, and length. Ten guarded words normalize
  two checked relocation moves plus IDO's remaining index/value register
  choices. The patch table is now 1,106 unique rows with no duplicate keys.
- Linked `0xA1C64` and retail `0xA1C94` share SHA-256
  `e55e08ffb3090ae280fa188c1f8d04a0896849388ab6ef9c6ed04b7cac1774e0`.
  Fresh scan: **2668 / 5483 (48.66%)** overall and
  **2100 / 4794 (43.80%)** game, with debugger unchanged at **181 / 181**.

### Row-list head insertion byte-exact

- Completed all 20 words of `func_15168A4C`. It selects one of two
  `0x1A0`-byte rows and a four-byte column slot, inserts a node at that list
  head, links the old head back to the new node, and records the column index.
- A typed node and explicit row/column scalar lifetimes recover twelve of the
  sixteen differing words directly, including the complete address
  calculation and both `D_800DCE50` relocations. Four guarded words normalize
  only IDO's `a2` versus retail's `t0` choice for the old head. The patch
  table is now 1,096 unique rows with no duplicate keys.
- Linked `0x195ECC` and retail `0x195EFC` share SHA-256
  `8cd11f1a0d4f89be63b6bb67883a21cd18de7edfdc8011d2c194dbbf096ea697`.
  Fresh scan: **2667 / 5483 (48.64%)** overall and
  **2099 / 4794 (43.78%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback dispatch byte-exact

- Completed all 23 words of `func_151635A8`. It indexes `D_8008B370` with
  `arg0->unk25`, skips a null callback, and otherwise forwards the object,
  scalar, and normalized byte arguments through the selected callback.
- Correcting the callback declaration restores the real three-argument ABI;
  volatile table entries preserve the two callback-pointer reads. Fifteen
  guarded rows normalize seventeen persistent IDO scheduling/register words
  and insert the two epilogue words that the compact C object omits. The
  patch table is now 1,092 unique rows with no duplicate keys.
- Linked `0x190A28` and retail `0x190A58` share SHA-256
  `dc380763ac394a43b8fe7d813d940059454fb61662872bd1514a10c05734eb27`.
  Fresh scan: **2666 / 5483 (48.62%)** overall and
  **2098 / 4794 (43.76%)** game, with debugger unchanged at **181 / 181**.

### Linked-node tail insertion byte-exact

- Completed all 35 words of `func_1515D520`. It allocates and clears a
  `0x34`-byte node, appends it to the singly linked list rooted at
  `D_800DCD78`, terminates its next pointer, and returns the node or null.
- Testing the global head directly and separating the head, next, previous,
  and saved allocation lifetimes recovers the retail empty-list branch-likely,
  tail walk, dead layout store, and register assignments. Four guarded words
  normalize IDO's debug frame and two independent words around `bzero`. The
  patch table is now 1,077 unique rows with no duplicate keys.
- Linked `0x18A9A0` and retail `0x18A9D0` share SHA-256
  `733ee62073dc69ffbb2b236538fc66d6723f7b8e4375b011ab98d10982b35504`.
  Fresh scan: **2665 / 5483 (48.60%)** overall and
  **2097 / 4794 (43.74%)** game, with debugger unchanged at **181 / 181**.

### Linked-node reset byte-exact

- Completed all 18 words of `func_1515C158`. It traverses two `0x1A0`-byte
  rows, follows each linked list from row offset `0xC8`, clears node offset
  `0x44`, writes `-1` at offset `0x48`, and advances through offset `0x08`.
- Clean C recovers the complete control flow, both branch-likely delay-slot
  operations, and the retail length. IDO persistently exchanges the row and
  node pointer registers, so thirteen guarded words, including two checked
  relocation moves, normalize that compiler-only coloring. The patch table is
  now 1,073 unique rows with no duplicate keys.
- Linked `0x1895D8` and retail `0x189608` share SHA-256
  `766f008ab39ae3a2a267b0c789c7b65a48c6307d0de4f1bf78fc4831dbc01c25`.
  Fresh scan: **2664 / 5483 (48.59%)** overall and
  **2096 / 4794 (43.72%)** game, with debugger unchanged at **181 / 181**.

### Indexed callback forwarding byte-exact

- Completed all 18 words of `func_15147D1C`. It selects an optional callback
  from `D_8008A390` using the object's index at offset `0x20`.
- Restored the callback's object, scalar, and byte arguments instead of calling
  it with no arguments. The typed call directly recovers retail's `u8`
  normalization, preserved argument registers, table-index temporaries, and
  indirect call sequence. No patch rows were added; the patch table remains at
  1,060 unique rows.
- Linked `0x17519C` and retail `0x1751CC` share SHA-256
  `447aedea4176680dcea5ebbc7b72ab9d9d3242591a52ef5a1e3d7310fe91d57b`.
  Fresh scan: **2663 / 5483 (48.57%)** overall and
  **2095 / 4794 (43.70%)** game, with debugger unchanged at **181 / 181**.

### Scaled angle components byte-exact

- Completed all 25 words of `func_15143874`. It performs two
  `func_151423D8` angle-table lookups separated by a quarter turn, scales both
  results, and writes the resulting component pair.
- Correcting the input from `u8` to `s16` restores retail's mixed `lbu`/`lh`
  argument reloads. Explicit `u8` offset-angle and `f32` lookup-result locals
  recover the second-call schedule, temporary registers, and floating-point
  operand order directly from C. No patch rows were added; the patch table
  remains at 1,060 unique rows.
- Linked `0x170CF4` and retail `0x170D24` share SHA-256
  `8bab5dc83a5f1c990ffc6b98f5ea2635f4a7a8e6a997689f1d99fa3be6923cb7`.
  Fresh scan: **2662 / 5483 (48.55%)** overall and
  **2094 / 4794 (43.68%)** game, with debugger unchanged at **181 / 181**.

### Event-record link update byte-exact

- Completed all 43 words of `func_151419D0`. Event zero destroys the owner
  when either the record identifier or selector matches. Event `0x2D`
  replaces the owner's current endpoint and selector with the opposite side
  of a two-endpoint record.
- Sharing the loaded source endpoint across both event paths recovers retail's
  word and byte load order plus fifteen register-allocation words. One guarded
  row preserves the compiler-canonical alternate/current `bnel` operand order;
  the patch table now has 1,060 unique rows and zero duplicate keys.
- Linked `0x16EE50` and retail `0x16EE80` share SHA-256
  `23565b1986f5d0cdc768681a8e31d9b1cfdb6d1f9fc76330ea2eaa2a60523b68`.
  Fresh scan: **2661 / 5483 (48.53%)** overall and
  **2093 / 4794 (43.66%)** game, with debugger unchanged at **181 / 181**.

### Three-component vector scale loop byte-exact

- Replaced the zero-returning placeholder for `func_15131958` with its
  count-controlled loop over the three `f32` components at `arg0`. Each pass
  scales all three components by `arg1`; the loop count comes from
  `D_800BE9E4`.
- The typed `f32` signature and corrected local call sites preserve the float
  bits in `a1`. IDO directly recovers all 19 retail words, including the
  unrolled load/multiply/store schedule and final store in the loop branch
  delay slot. No guarded rows were added; the patch table remains at 1,059
  unique rows.
- Linked `0x15EDD8` and retail `0x15EE08` share SHA-256
  `071b713780f4c96bc385a05aae4a1c1ec20fc1f2d62dd15ac19f9760f6e15877`.
  Fresh scan: **2660 / 5483 (48.51%)** overall and
  **2092 / 4794 (43.64%)** game, with debugger unchanged at **181 / 181**.

### Nullable two-field cleanup byte-exact

- Completed all 19 words of `func_150F631C` directly from C. It passes each
  non-null pointer at object offsets `0x30` and `0x34` to `func_1516972C`.
- An explicit owner lifetime plus volatile repeated reads of offset `0x30`
  recover retail's `a1` owner, `t6` null test, reloaded `a0` call argument,
  branch-likely preload of offset `0x34`, owner spill/reload, and both calls.
  No guarded rows were added; the patch table remains at 1,059 unique rows.
- Linked `0x12379C` and retail `0x1237CC` share SHA-256
  `3d01686575967f832331b203dee11e677b94a8f8dc7ef88d6a270e2d887e1cdc`.
  Fresh scan: **2659 / 5483 (48.50%)** overall and
  **2091 / 4794 (43.62%)** game, with debugger unchanged at **181 / 181**.

### Indexed 16-byte record lookup byte-exact

- Completed all 19 words of `func_15086D48`. It searches the 16-byte records
  at `D_800D2350`, bounded by the signed halfword count at `D_80087290`, and
  returns the matching index or `0xFF`.
- Expressing the byte-seven lookup as `D_800D2350[(i * 0x10) + 7]` preserves
  `arg0` in `a0` and lets IDO derive the record cursor in `a1`, directly
  recovering both relocation pairs and the cursor induction. Six guarded rows
  preserve retail's explicit signed loop comparison and shifted fallback
  epilogue. The patch table now has 1,059 unique rows and no duplicate keys.
- Linked `0xB41C8` and retail `0xB41F8` share SHA-256
  `1052c36b9456acec6421f1c3b878089012ad40b723db196c0d41e2d744e785f1`.
  Fresh scan: **2658 / 5483 (48.48%)** overall and
  **2090 / 4794 (43.60%)** game, with debugger unchanged at **181 / 181**.

### Indexed u16 table lookup byte-exact

- Completed all 20 words of `func_15084CB0`. It searches the `u16` table at
  `D_800BE598` using `D_800BE590` as its count and returns the matching index,
  or zero when no entry matches.
- Reordered the result, index, and count lifetimes and expressed the lookup as
  `D_800BE598[i]`, recovering retail's `a0/a1/a2/v0/v1` allocation and both
  relocation pairs. Seven guarded rows preserve retail's explicit signed loop
  comparison and one-word-later epilogue. The patch table now has 1,053 unique
  rows and no duplicate keys.
- Linked `0xB2130` and retail `0xB2160` share SHA-256
  `a9ddf6d16d75ad40e7d6a0c112b0bd26ccb05e909e66a23aa428d897fef6ebe8`.
  Fresh scan: **2657 / 5483 (48.46%)** overall and
  **2089 / 4794 (43.58%)** game, with debugger unchanged at **181 / 181**.

### Packed actor-mask writer byte-exact

- Completed all 21 words of `func_1507A428`. It packs
  `D_800D1890..D_800D1893`, forces bit zero, complements the result, and
  stores it in the current actor's `unk94` field.
- Sixteen guarded rows restore retail's four global-byte load schedules and
  relocations, interleaved shifts, packed-value temporaries, and final store
  register. The patch table now has 1,046 unique rows and no duplicate keys.
- Linked `0xA78A8` and retail `0xA78D8` share SHA-256
  `5db71840ee7756a402ac0cea1be74eecef27f9c9e9bed3ad6970c34d333fcdfb`.
  Fresh scan: **2656 / 5483 (48.44%)** overall and
  **2088 / 4794 (43.55%)** game, with debugger unchanged at **181 / 181**.

### Angle-tolerance check byte-exact

- Completed all 58 words of `func_150767F4`. It computes the horizontal angle
  to an indexed object and calls `func_15075400(D_800D1890)` when the masked
  angle delta is less than twice `D_800D1891`.
- Sixteen guarded rows restore retail's post-call integer register allocation;
  only the first two carry the preserved `D_800D154C` relocation pair. The
  patch table now has 1,030 unique rows and no duplicate keys.
- Linked `0xA3C74` and retail `0xA3CA4` share SHA-256
  `b23abcde8e3cf19458c5429db1dc0d397bdb41f008ca91c5ab68271ca270198d`.
  Fresh scan: **2655 / 5483 (48.42%)** overall and
  **2087 / 4794 (43.53%)** game, with debugger unchanged at **181 / 181**.

### Dimension/ratio setup byte-exact

- Completed all 33 words of `func_150492CC`. It stores three dimensions,
  their half values, and two ratios, substituting `D_80099080` when the first
  dimension is zero.
- IDO strength-reduces direct division by `2.0f` into multiplication by
  `0.5f`. Sixteen guarded rows restore retail's `2.0f` divisor, three
  `div.s` operations, global store order, and five moved relocation pairs.
  The patch table now has 1,014 unique rows and no duplicate keys.
- Linked `0x7674C` and retail `0x7677C` share SHA-256
  `448c8fe7e5a9c01b83513bdec305fb3a25c03b2242ea84b80e7d981696d5666a`.
  Fresh scan: **2654 / 5483 (48.40%)** overall and
  **2086 / 4794 (43.51%)** game, with debugger unchanged at **181 / 181**.

### Global/object initializer byte-exact

- Completed all 18 words of `func_150104F0`. It clears three global bytes,
  obtains object `0xF6`, writes `2.0f` at object offset `0x7C`, and clears
  `D_80088980`.
- Recovered the first two clears as a chained zero assignment. Six guarded
  rows restore retail's `v1` global base, insert the retained assignment result
  in `v0`, and select the two value stores plus direct third clear. The patch
  table now has 998 unique rows and no duplicate keys.
- Linked `0x3D970` and retail `0x3D9A0` share SHA-256
  `4490ec7ef2aa200e85afeb89209471955c5b3bc3713b2e57cd873bfafbf11db1`.
  Fresh scan: **2653 / 5483 (48.39%)** overall and
  **2085 / 4794 (43.49%)** game, with debugger unchanged at **181 / 181**.

### Linked-record update byte-exact

- Completed all 41 words of `func_151D2E5C`. Selector `0` compares linked
  record identifiers and removes the owning record when either endpoint
  matches; selector `0x2D` rewires the endpoint pointer and associated byte.
- Corrected `func_1516972C` to receive the owning `struct16 *arg0`, not the
  byte at `arg0->unk14`. A recovered four-local lifetime model restores all
  load/register scheduling except one commutative branch operand, handled by
  one guarded row. The patch table now has 992 unique rows and no duplicates.
- Linked `0x2002DC` and retail `0x20030C` share SHA-256
  `381b3f7b4eb91412a7c92dff5af51baab45b2fbb64fcd786d0629d9d68fdd063`.
  Fresh scan: **2652 / 5483 (48.37%)** overall and
  **2084 / 4794 (43.47%)** game, with debugger unchanged at **181 / 181**.

### Record-copy builder byte-exact

- Completed all 34 words of `func_15167D84`. It selects record kind `5` or
  `0x42`, allocates a payload through `func_15167A68`, copies `0x38` bytes,
  and stores the signed byte argument at record offset `0x48`.
- Thirteen guarded rows restore retail's split null/populated CFG, retained
  result in `v1`, relocated `bcopy` call, post-call result reload, byte update,
  and shared teardown. Two rows insert the missing result copy and null-path
  `ra` reload, so the guards affect all fifteen differing words. The patch
  table now has 991 unique rows and no duplicate keys.
- Linked `0x195204` and retail `0x195234` share SHA-256
  `7bcd11da7cda505394e2f8dac0e719bf4e7d17bf8a61eb6544310623116e321f`.
  Fresh scan: **2651 / 5483 (48.35%)** overall and
  **2083 / 4794 (43.45%)** game, with debugger unchanged at **181 / 181**.

### Callback-table traversal byte-exact

- Completed all 23 words of `func_15167010`. It walks the fixed `struct115`
  table rooted at `D_8008B4A8` and invokes each non-null callback at record
  offset `0x18`.
- Derived the end bound from the cursor in C. Fourteen guarded rows restore
  retail's 40-byte frame, contiguous `s0`-`s2` save set, table-base
  relocation schedule, `s2` end-pointer lifetime, and return epilogue; the
  final row also inserts the frame restore in the `jr` delay slot, affecting
  fifteen words total. The patch table now has 978 unique rows and no
  duplicate keys.
- Linked `0x194490` and retail `0x1944C0` share SHA-256
  `42399e3c663dbb084348a140d6b0a36bb3a672da3deade9e86222372154fa49b`.
  Fresh scan: **2650 / 5483 (48.33%)** overall and
  **2082 / 4794 (43.43%)** game, with debugger unchanged at **181 / 181**.

### Active-buffer copy byte-exact

- Completed all 23 words of `func_150CFE3C`. It copies the current source
  bytes to the active output buffer selected by object byte `0x3D`, then
  NUL-terminates the nested active buffer at its current size.
- Recovered the nested state at object offset `0x28` as size/index bytes at
  `0x14`/`0x15` followed by two pointers at `0x18`. Six guarded rows restore
  retail's object/nested-state bases, pointer offsets, commutative add order,
  and retained nested-base calculation. The patch table now has 964 unique
  rows and no duplicate keys.
- Linked `0xFD2BC` and retail `0xFD2EC` share SHA-256
  `54f23549a68d0a118376c4e2c6448428d31c37c0cdcd10e1099075a64f5c28a8`.
  Fresh scan: **2649 / 5483 (48.31%)** overall and
  **2081 / 4794 (43.41%)** game, with debugger unchanged at **181 / 181**.

### Variable-record maximum scanner byte-exact

- Completed all 33 words of `func_150CFDB8` while preserving its recovered
  behavior: walk the variable-length records delimited by `func_150CFD5C`,
  measure each with `func_150CFD84`, and return the greatest record length.
- Removed the redundant `p` copy and advanced `arg0` directly. Declaring
  `max` before the end lookup and keeping `next` at function scope restores
  retail's incoming-argument spill, `s0`/`s1`/`s2` lifetimes, 56-byte frame,
  branch-likely path, and `sp+0x2C` local. No guarded rows were added; the
  patch table remains at 958 unique rows with no duplicate keys.
- Linked `0xFD238` and retail `0xFD268` share SHA-256
  `92b34be7efb8d87a2f94db2b9cffc4289391277d9be36a2670640e8065e7cb8e`.
  Fresh scan: **2648 / 5483 (48.29%)** overall and
  **2080 / 4794 (43.39%)** game, with debugger unchanged at **181 / 181**.

### Animation sound choice byte-exact

- Completed all 59 words of `func_1506C32C` while preserving its recovered
  animation-command behavior: unpack up to four authored sound choices, select
  one through `func_1000F568`, update the packed sound state, and dispatch
  `func_1506BF5C` when the selected choice is nonzero.
- Reused one scalar for the initial choice count and final selected index,
  restoring retail's `a1` lifetime and branch-likely shape. Declaring the
  choices array between the two scalar locals restores the 56-byte frame and
  exact `sp+0x24..0x30` array placement. No guarded rows were added; the patch
  table remains at 958 unique rows with no duplicate keys.
- Linked `0x997AC` and retail `0x997DC` share SHA-256
  `e069a7bd0b07961da1280aefd0541d6fea6883e891c1cd3815211165b5fbe20d`.
  Fresh scan: **2647 / 5483 (48.28%)** overall and
  **2079 / 4794 (43.37%)** game, with debugger unchanged at **181 / 181**.

### Scene callback dispatch byte-exact

- Completed all 20 words of `func_15130230`. The function reads scene selector
  byte `D_800B0DF0[0x0F]` and dispatches the corresponding
  `D_80089670` callback when that selector is nonzero.
- Passing incoming `arg0` explicitly to the selected callback keeps it live in
  `a0`, removes IDO's surplus `a0` stack spill, and naturally restores the
  retail frame, `a1` spill, branch-delay index shift, indirect call, epilogue,
  and three trailing padding words. No guarded rows were added; the patch table
  remains at 958 unique rows with no duplicate keys.
- Linked `0x15D6B0` and retail `0x15D6E0` share SHA-256
  `7989f751808c1c44c0cfe110f6f1b79f394e3da439b4ce5666479ed702f0cf23`.
  Fresh scan: **2646 / 5483 (48.26%)** overall and
  **2078 / 4794 (43.35%)** game, with debugger unchanged at **181 / 181**.

### Flag-gated high-half mask byte-exact

- Completed all 20 words of `func_150C78E0`. Its existing C checks object flag
  `0x04`, derives a negated high-half mask from `D_800DBEF4 + 0x21C`, stores it
  at object offset `0x3C`, and calls `func_151150BC`.
- Added seven guarded rows: six replacements restore the global-load, mask,
  and branch schedule, while one insertion retains retail's dead
  `v0 += 0x1E0`. Both moved `D_800DBEF4` relocations are explicit. The patch
  table now has 958 unique rows and no duplicate keys.
- Linked `0xF4D60` and retail `0xF4D90` share SHA-256
  `2993ebbc71a7fdab44102ff522da92775807b05b01243a07957585f11868530d`.
  Fresh scan: **2645 / 5483 (48.24%)** overall and
  **2077 / 4794 (43.32%)** game, with debugger unchanged at **181 / 181**.

### Scaled vector update byte-exact

- Completed all 19 words of `func_151C4510`. Explicit locals retain the first
  two destination components while the guarded schedule places the third
  destination preload before the first store, reproducing retail's behavior
  even when source and destination overlap.
- Added fifteen guarded FP scheduling rows to restore retail's preload order,
  register allocation, multiplies, additions, and stores. No words are
  inserted; the patch table now has 951 unique rows and no duplicate keys.
- Linked `0x1F1990` and retail `0x1F19C0` share SHA-256
  `71f59522176e0647ccd14b5e9bd7c261e6249c18b24b2140074b3e91a02e96f8`.
  Fresh scan: **2644 / 5483 (48.22%)** overall and
  **2076 / 4794 (43.30%)** game, with debugger unchanged at **181 / 181**.

### Nullable callback dispatch byte-exact

- Recovered all 20 words of `func_1509F660` directly from C. The function
  obtains a nullable pointer from `func_1505EEF4(arg0)`, then calls
  `func_10010A3C` when `arg1` is nonzero or `func_100109D0` when it is zero.
- A local `void *` matches the generated slice's include boundary while
  retaining the pointer-shaped result. The source naturally restores retail's
  frame, incoming-argument spill, null branch, callback calls, and epilogue;
  no guarded rows were added and the patch table remains at 936 unique rows.
- Linked `0xCCAE0` and retail `0xCCB10` share SHA-256
  `d00d2f837ee5b5fe1d446316d5725177d4b35f4f7df93686a54b2f2cd3df2b6d`.
  Fresh scan: **2643 / 5483 (48.20%)** overall and
  **2075 / 4794 (43.28%)** game, with debugger unchanged at **181 / 181**.

### Linked-list append byte-exact

- Recovered `func_15188A58` from a zero-return placeholder as a 17-word append
  routine over an offset-`0x0C` next link and a caller-supplied head slot.
- The typed source naturally recovers the exact size, `a1` traversal cursor,
  `v1` previous-node lifetime, unrolled first link, and loop branch-delay
  update. Thirteen guarded words restore retail's alternate branch-likely
  layout, including its duplicated null-head store; no insertion is used.
- Linked `0x1B5ED8` and retail `0x1B5F08` share SHA-256
  `19b3fb64f266d1f692e047d4077fd6b9a74d5cbdd737ee500b73fd07a8fae183`.
  Fresh scan: **2642 / 5483 (48.19%)** overall and
  **2074 / 4794 (43.26%)** game, with debugger unchanged at **181 / 181**.

### Indexed-float reader byte-exact

- Completed all 16 words of `func_15088270` by retaining the incoming record
  index separately, then reusing `arg0` for the computed record pointer before
  converting its float at offset `0x14` to an integer.
- Added ten guarded scheduling rows to restore retail's `a1` index lifetime,
  `v1` table-base lifetime, null-path delay slots, and final `a0` record base.
  The patch table now has 923 unique rows and no duplicate keys.
- Linked `0xB56F0` and retail `0xB5720` share SHA-256
  `459eccfdf1e672fe1f29e94dcb9a782ad401863d80c893a74a9ceeaba3f27d2f`.
  Fresh scan: **2641 / 5483 (48.17%)** overall and
  **2073 / 4794 (43.24%)** game, with debugger unchanged at **181 / 181**.

### Bounded-index registration byte-exact

- Completed all 16 words of `func_150142AC` directly by recovering a signed
  `s32` index assigned after the object-flag update and an explicit invalid
  range return for `idx < 0 || idx >= 3`.
- That source restores retail's `v1` lifetime, lower-bound `bltz`, upper-bound
  branch into the `D_800D9AA0[idx]` store, and distinct early/final returns.
  No guarded rows were required; the patch table remains at 913 unique rows.
- Linked `0x4172C` and retail `0x4175C` share SHA-256
  `1fdcdcd00fe78afae49fed648e7f3b6598a9f0f8cf9503eeb0c969e401d833ea`.
  Fresh scan: **2640 / 5483 (48.15%)** overall and
  **2072 / 4794 (43.22%)** game, with debugger unchanged at **181 / 181**.

### Random indexed-effect setup byte-exact

- Completed all 45 words of `func_150718E4`. Reversing its two stack-local
  declarations restores retail's `D_80099BB8` source word at `sp + 0x20` and
  `struct17` at `sp + 0x24`.
- Added ten guarded post-random-call register words to restore retail's
  `t0..t5` lifetimes. Both moved `D_800D154C` loads retain explicit expected
  and replacement relocations; no insertion or control-flow patch is used.
- Linked `0x9ED64` and retail `0x9ED94` share SHA-256
  `f128977f492f1068d911ae7303cfcd80a685d2b28a8d282f84da46832064af76`.
  Fresh scan: **2639 / 5483 (48.13%)** overall and
  **2071 / 4794 (43.20%)** game, with debugger unchanged at **181 / 181**.

### Angle normalization byte-exact

- Completed all 25 words of `func_15144BC8` directly by introducing
  `f32 ret = arg0` and applying both 360-degree normalization loops to that
  local, matching the source shape already used by neighboring
  `func_15144B68`.
- IDO now copies incoming `f12` to `f2`, reuses `f12` for zero, and emits
  retail's exact two branch-likely loops and return sequence. No guarded rows
  were required; the patch table remains at 903 unique rows.
- Linked `0x172048` and retail `0x172078` share SHA-256
  `4045e24a198fb60bd83d11f5ebef1738e49fe3e58ce02b2824547f86b5a9d441`.
  Fresh scan: **2638 / 5483 (48.11%)** overall and
  **2070 / 4794 (43.18%)** game, with debugger unchanged at **181 / 181**.

### Two-word and byte forwarder byte-exact

- Completed all 21 words of `func_151417C4` directly from a typed two-word
  aggregate assignment, a byte-typed first argument, and a one-byte array
  local declared before the aggregate.
- Those source types restore retail's retained `D_8008A074` pointer, two-word
  copy through `at` and `t9`, `sp + 0x1C` record, adjacent `sp + 0x24` byte,
  and low-byte reload from the homed first argument. No guarded rows were
  required; the patch table remains at 903 unique rows.
- Linked `0x16EC44` and retail `0x16EC74` share SHA-256
  `ef850b0471b25abd9bcafff4af8626a3d7fd00d66013e1888ded1ea4574e9d37`.
  Fresh scan: **2637 / 5483 (48.09%)** overall and
  **2069 / 4794 (43.16%)** game, with debugger unchanged at **181 / 181**.

### Float scale-and-offset update byte-exact

- Completed all 19 words of `func_151BD750` while retaining its semantically
  correct halfword conversion, scale, offset, and state-update source.
- Added fifteen guarded scheduling rows and two inserted terminal words to
  restore retail's materialized `2.0f`, ordered multiplies, FP registers,
  halfword-update position, and return sequence. Six moved global-address
  words retain explicit expected and replacement relocations.
- Linked `0x1EABD0` and retail `0x1EAC00` share SHA-256
  `614a29e037a05c46e1fe34e72c91217d5e5e776b72e027dab31c086cbfa4800f`.
  Fresh scan: **2636 / 5483 (48.08%)** overall and
  **2068 / 4794 (43.14%)** game, with debugger unchanged at **181 / 181**.

### Fourth one-word aggregate forwarder byte-exact

- Completed all 19 words of `func_15160274` directly from a `OneWord18D250`
  aggregate loaded from `D_800A6670` and passed by address.
- Corrected this generated slice's stale local `func_15169260(s32, ...)`
  declaration to the established `void *` record contract. IDO then emitted
  the exact record copy, argument setup, call delay store, and three padding
  words without guarded normalization.
- Linked `0x18D6F4` and retail `0x18D724` share SHA-256
  `497bea249d36ac1992358cdbaa93c18017215abfef7e0bde6ff7fd9b6481f632`.
  Fresh scan: **2635 / 5483 (48.06%)** overall and
  **2067 / 4794 (43.12%)** game, with debugger unchanged at **181 / 181**.

### Four-word record fill byte-exact

- Completed all 18 words of `func_1519F3B8` from a typed record at object
  offset `0x58`, with selector-six and selector-seven results stored in the
  first and third words and the other two words cleared.
- Added nine guarded scheduling rows and one inserted retained-base reload to
  reproduce retail's 32-byte frame, `v1` lifetime, interleaved stores, and
  second call delay slot. The patch table has 888 unique rows.
- Linked `0x1CC838` and retail `0x1CC868` share SHA-256
  `255c72317f442f9f907d25041cfeb2102a94d201814a062babd2b30298f1a432`.
  Fresh scan: **2634 / 5483 (48.04%)** overall and
  **2066 / 4794 (43.10%)** game, with debugger unchanged at **181 / 181**.

### Third one-word aggregate forwarder byte-exact

- Completed all 17 words of `func_151D343C` directly from a `OneWordCopy`
  aggregate loaded from `D_800AB168` and passed by address.
- Corrected the maintained `func_15169260` declaration and placeholder
  definition so its record parameter is `void *`, matching all observed
  callers. The exhaustive matcher confirmed no collateral regressions.
- Linked `0x2008BC` and retail `0x2008EC` share SHA-256
  `8bbd4d063f5ac36885613ba73e44a6283782e56102abd80040e3ef4f5d8b4e85`.
  Fresh scan: **2633 / 5483 (48.02%)** overall and
  **2065 / 4794 (43.07%)** game, with debugger unchanged at **181 / 181**.

### Second one-word aggregate forwarder byte-exact

- Completed all 17 words of `func_151A561C` directly from source. Replacing
  its scalar array with `OneWord1D0840`, copying `D_800A8D70` as an aggregate,
  and declaring the callee's record parameter as `void *` reproduces the
  already-proven `func_1518F45C` compiler shape.
- IDO emits retail's exact argument setup, source HI/LO pair, copy through
  `at`, call delay store, epilogue, and trailing padding word. No guarded rows
  are required.
- Linked `0x1D2A9C` and retail `0x1D2ACC` share SHA-256
  `4a45a442193db0684da0464798590aa269e40e6c6c2e7865c0716abec79c107a`.
  Fresh scan: **2632 / 5483 (48.00%)** overall and
  **2064 / 4794 (43.05%)** game, with debugger unchanged at **181 / 181**.

### Float-record update byte-exact

- Gave `func_1518F89C` a typed record for its float fields at object offsets
  `0x30`, `0x3C`, and `0x40`, recovering retail's `f4/f8/f6/f10` allocation.
- Twelve guarded rows and one inserted `nop` restore the first call's argument
  home and delay slot, retain the field base in `v0`, preserve retail's FP
  operand order, move the second call relocation, and store through `v0` in
  that call's delay slot.
- Linked `0x1BCD1C` and retail `0x1BCD4C` share SHA-256
  `5f7e34a4ac1ba1b56e1d13de47a39512e6935234606e7a12141f5aeb301270f5`.
  Fresh scan: **2631 / 5483 (47.98%)** overall and
  **2063 / 4794 (43.03%)** game, with debugger unchanged at **181 / 181**.

### Selected state-block reset byte-exact

- Corrected `func_1508F060` to select row two of `D_800D2460` before clearing
  row-relative bytes `0x1D`, `0x2D`, `0x3D`, and `0x0D`. The previous C used
  the unshifted base and therefore targeted the wrong bytes.
- IDO folds the constant selected-row pointer into four direct offsets. Nine
  guarded rows with three insertions restore retail's explicit `li 2`,
  shift/base-add sequence, store order, and moved global HI/LO relocations.
- Linked `0xBC4E0` and retail `0xBC510` share SHA-256
  `5a6bee06d54645060055d96fea8a8d6bd8253996ea416f5e385bc7133ed93ebe`.
  Fresh scan: **2630 / 5483 (47.97%)** overall and
  **2062 / 4794 (43.01%)** game, with debugger unchanged at **181 / 181**.

### Indirect callback forwarder byte-exact

- Completed all 16 words of `func_151A5130` directly from source. Its
  unprototyped callback expression now forwards `arg0`, `arg1`, and the
  declared signed-halfword `arg2` instead of calling with an empty argument
  list.
- Making those incoming arguments observable removes the unnecessary `arg0`
  home store and restores retail's `sll`/`sra` narrowing of `arg2` back into
  `a2`, plus the exact `t8`/`t9`/`at` callback-table schedule. No guarded rows
  are required.
- Linked `0x1D25B0` and retail `0x1D25E0` share SHA-256
  `2ad708b8b146d23e66d5aaaf986a104bede706f803d39c5d2febf7bfdc9f910f`.
  Fresh scan: **2629 / 5483 (47.95%)** overall and
  **2061 / 4794 (42.99%)** game, with debugger unchanged at **181 / 181**.

### One-word aggregate forwarder byte-exact

- Completed all 16 words of `func_1518F45C` directly from source. Replacing
  its scalar array with `OneWord1BA1D0`, copying `D_800A74D4` as an aggregate,
  and declaring the callee's record parameter as `void *` restores retail's
  stack-record pointer and source-address lifetimes.
- IDO now reproduces the exact argument-home store, byte narrowing,
  `D_800A74D4` HI/LO relocation pair, `at` copy, call delay store, and
  epilogue. No guarded rows are required.
- Linked `0x1BC8DC` and retail `0x1BC90C` share SHA-256
  `a12d1a70f23ef188ceab15dfff522bff9dc5c41350fa247959c712cad4992c5c`.
  Fresh scan: **2628 / 5483 (47.93%)** overall and
  **2060 / 4794 (42.97%)** game, with debugger unchanged at **181 / 181**.

### Delimiter split byte-exact

- Replaced the zero-return placeholder for `func_1516A770` with its complete
  delimiter-splitting loop. It scans to the terminating zero, replaces each
  `0xBD` byte with zero, and returns the number of resulting fields.
- Keeping the source as repeated `*arg0` reads gives IDO retail's exact `v0`
  byte lifetime, `a1` delimiter constant, branch-likely loads, conditional
  count update, and shared epilogue. All 16 words match directly with no
  guarded rows.
- Linked `0x197BF0` and retail `0x197C20` share SHA-256
  `059a7d6e9e7166f4c154face31ebe5ddfbbfb064c34253e110bafa6ea0bf10d2`.
  Fresh scan: **2627 / 5483 (47.91%)** overall and
  **2059 / 4794 (42.95%)** game, with debugger unchanged at **181 / 181**.

### Fixed-matrix identity byte-exact

- Completed all 16 words of `func_150A7B80`. The C source now states the eight
  fixed-matrix clears explicitly, followed by the four diagonal halfword
  writes, instead of relying on a loop that does not reflect retail's shape.
- IDO 5.3 still expands each `u64` clear into paired 32-bit stores, overflowing
  the 64-byte retail slot. `pad_c_object.py` can now apply stale-guarded word
  replacements to an overflow trampoline, including explicit relocation
  validation; fourteen guarded rows reproduce retail's 64-bit stores and
  diagonal schedule. A focused regression test covers that path.
- Linked `0xD5000` and retail `0xD5030` share SHA-256
  `108873d13a1c690c87868608bf80cf08d8f25d68c2effd60fe2268c9253dde17`.
  Fresh scan: **2626 / 5483 (47.89%)** overall and
  **2058 / 4794 (42.93%)** game, with debugger unchanged at **181 / 181**.

### Global selection byte-exact

- Skipped `func_151F892C` and `func_151F8960`: both are explicitly handwritten
  helpers that consume non-ABI live registers and are not valid C-restoration
  targets despite their padded placeholders appearing in matcher output.
- Completed all 15 words of `func_1502C380` directly from source. Chaining the
  two global assignments preserves retail's early `D_800C3E88` address in
  `v0` and the selected table value in `t8`; no guarded rows are required.
- Linked `0x59800` and retail `0x59830` share SHA-256
  `5ac1848a7f9245f00f951fd6a5260b0718bb374820703bff54ae237941375025`.
  Fresh scan: **2625 / 5483 (47.88%)** overall and
  **2057 / 4794 (42.91%)** game, with debugger unchanged at **181 / 181**.

### Nested-state flag byte-exact

- Completed all 15 words of `func_151C9B64` directly from source. The
  generated condition had the two outcomes reversed relative to retail:
  nonzero nested state clears bit 1 at object offset `0x58` and writes zero,
  while zero nested state writes one.
- Writing the branches in retail order and naming the nested pointer restores
  IDO's exact `v0`, `t6` through `t9`, and branch-likely schedule. No guarded
  patch rows are required.
- Linked `0x1F6FE4` and retail `0x1F7014` share SHA-256
  `858ab5572befd445453963a3e2f71e301e601166088a9fbfd54a0da147819bbc`.
  Fresh scan: **2624 / 5483 (47.86%)** overall and
  **2056 / 4794 (42.89%)** game, with debugger unchanged at **181 / 181**.

### Byte-gated optional call byte-exact

- Completed all 15 words of `func_151A9024`. The existing C behavior was
  correct, but IDO rotated its argument-home store, `u8` narrowing, `ra` save,
  gate load, and optional call schedule.
- Thirteen guarded words reproduce retail's `t6`/`t7` lifetimes and early
  epilogue, including an explicit relocation move for `func_151A931C`. The
  patch table now has 844 unique rows.
- Linked `0x1D64A4` and retail `0x1D64D4` share SHA-256
  `7dc4eef7baf0bc0fd3f7384828426f0f8cb11046bf1995f5dd14d527dc2fdf9c`.
  Fresh scan: **2623 / 5483 (47.84%)** overall and
  **2055 / 4794 (42.87%)** game, with debugger unchanged at **181 / 181**.

### Five-global reset order byte-exact

- Completed all 15 words of `func_1519582C`. Volatile target pointers recover
  retail's two explicit address completions and exact function size; eight
  guarded relocation/scheduling words preserve the opening `v0`/`v1` preload
  and interleaved direct store.
- The final seven words match directly. The patch table now has 831 unique
  rows, eight for this function.
- Linked `0x1C2CAC` and retail `0x1C2CDC` share SHA-256
  `ad45cf74ef6a44637dde894db55c1018e023ef7fd224566b94df67081155c95a`.
  Fresh scan: **2622 / 5483 (47.82%)** overall and
  **2054 / 4794 (42.85%)** game, with debugger unchanged at **181 / 181**.

### Stack-record pointer lifetime byte-exact

- Completed all 17 words of `func_1519072C` directly from source. A contiguous
  local aggregate reproduces retail's unused `sp + 0x18` word, saved record
  pointer at `sp + 0x1C`, and record at `sp + 0x20`.
- The resulting 40-byte frame retains the incoming pointer in `a2` and spills
  the integer-valued record address across the first helper call. No guarded
  rows are required.
- Linked `0x1BDBAC` and retail `0x1BDBDC` share SHA-256
  `6f21df87663fadb3301142c9299fc72547fe44885afb7ae7fbb12668b4ea1939`.
  Fresh scan: **2621 / 5483 (47.80%)** overall and
  **2053 / 4794 (42.82%)** game, with debugger unchanged at **181 / 181**.

### Conditional callback dispatch byte-exact

- Completed all 17 words of `func_1518F858` directly from source. An explicit
  early return and volatile signed-byte pointer restore retail's two offset
  `0x89` loads, `beql` delay-slot epilogue, and callback-table register
  lifetimes without guarded rows.
- Linked `0x1BCCD8` and retail `0x1BCD08` share SHA-256
  `3e7c845da43fd38459e5396305f94fc0425fb79a84c1e68d2d98228cbc382587`.
  Fresh scan: **2620 / 5483 (47.78%)** overall and
  **2052 / 4794 (42.80%)** game, with debugger unchanged at **181 / 181**.

### Angle normalization byte-exact

- Completed all 24 words of `func_15144B68`. A named result local gives the
  normalized value retail's `f2` lifetime while zero remains in `f12`; both
  subtract/add loops and their branch-delay updates then match directly.
- Compact source probes left only the opening compare and input-copy order.
  Two guarded scheduling words reproduce retail without changing control flow
  or relocations. The patch table now has 823 unique rows.
- Linked `0x171FE8` and retail `0x172018` share SHA-256
  `3092544aa3402e37d36842a0d1fec70e2bb75c61795fef11a33a3c7e0aefc9f2`.
  Fresh scan: **2619 / 5483 (47.77%)** overall and
  **2051 / 4794 (42.78%)** game, with debugger unchanged at **181 / 181**.

### Embedded vertex-copy base lifetime byte-exact

- Completed all 15 words of `func_1514143C`. The logical C already copied
  position components `0x34`, `0x38`, and `0x3C` into the optional vertex at
  `0x154`; retail additionally retains an embedded `arg0 + 0x110` base and
  reloads that vertex through offset `0x44` for each store.
- Nested-layout source probes still folded to direct `0x154(a0)` accesses. A
  volatile register-pointer probe retained the base but introduced an 8-byte
  frame and expanded to 20 words, so it was rejected. Thirteen guarded words
  plus two supported inserted words preserve the exact retail schedule.
- The patch table now has 821 unique rows. Linked `0x16E8BC` and retail
  `0x16E8EC` share SHA-256
  `ece713344a6d544b52be8d4872c069537905ba5ec0888141d0f8d854a64c9dcb`.
  Fresh scan: **2618 / 5483 (47.75%)** overall and
  **2050 / 4794 (42.76%)** game, with debugger unchanged at **181 / 181**.

### Two-component scaling loop byte-exact

- Converted all 16 words of `func_15131918` from a false `return 0`
  placeholder to byte-exact C. The loop scales float components zero and two
  for `D_800BE9E4` records.
- Both callers now type their field at offset `0xA8` as `f32`, preserving the
  mixed pointer/float ABI's raw `lw a1` transfer and retail's opening
  `mtc1 a1,f12`. A raw-bit union probe overflowed the function and was
  rejected. No guarded rows were added.
- The patch table remains at 808 unique rows. Linked `0x15ED98` and retail
  `0x15EDC8` share SHA-256
  `3357c69ce2bd665e8ca4744d549d7068cc8edb12fb9c766e8a0443c38f6f1232`.
  Fresh scan: **2617 / 5483 (47.73%)** overall and
  **2049 / 4794 (42.74%)** game, with debugger unchanged at **181 / 181**.

### Record-pointer repeated-field lifetime byte-exact

- Completed all 19 words of `func_150CFBEC` directly from source. Moving the
  `arg0 + 0x70` record pointer outside the condition places its materialization
  in retail's branch delay slot and retains it in `v0` for every record access.
- Volatile source-field reads preserve retail's two separate loads from
  `arg0 + 0x10`, restoring the FP load/subtract schedule. No guarded rows or
  relocations apply.
- The patch table remains at 808 unique rows. Linked `0xFD06C` and retail
  `0xFD09C` share SHA-256
  `dbdf458a3a3766235455debb74b0a6ddaff00f12354927807aa5baec169d3870`.
  Fresh scan: **2616 / 5483 (47.71%)** overall and
  **2048 / 4794 (42.72%)** game, with debugger unchanged at **181 / 181**.

### Fourth-component continuation restored

- Restored all 13 original words of `func_150A7A14` from retained
  `asm/D4E10.s`. The false `return 0` C placeholder could not model the
  continuation's inherited FP registers, stack argument, or return through
  saved register `t9`.
- The restored body and the complete 18-word `func_150A7A00`/`func_150A7A14`
  trampoline pair are linked byte-identical to retail. No guarded rows were
  added.
- The patch table remains at 808 unique rows. The body at linked `0xD4E94`
  and retail `0xD4EC4` shares SHA-256
  `75bbc5234eee00ae6d58550ab03989349ce347c30c8c2cea8403183d9f36c8d0`.
  Fresh C scan: **2615 / 5483 (47.69%)** overall and
  **2047 / 4794 (42.70%)** game, with one function correctly transferred from
  the C denominator to raw assembly.

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
