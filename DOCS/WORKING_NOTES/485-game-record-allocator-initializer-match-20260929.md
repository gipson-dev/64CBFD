# Game record allocator initializer byte match

Date: 2026-09-29

## Scope and behavior

`func_15155780` in `conker/src/game/generated_182C30.c` spans 31 words and
124 bytes at `0x15155780..0x151557FC`. Its recovered body:

- Calls `func_15167A68(0x50, 0, 0xA0, 1, selector, 1)`.
- Returns the allocator result unchanged when allocation fails.
- Clears byte `0x11` and word `0x14` on a successful record.
- Stores the incoming key in byte `0x10` and floating zero at offset `0x98`.
- Calls `func_1518C900(0xA6)` and returns the initialized record.

## Compiler shape

The null branch must use `return record`. Spelling it as `return NULL` makes
IDO emit a redundant `move v0, zero`, while restructuring the function as one
non-null block shortens the routine and changes the result-pointer lifetime.
The explicit null return reproduces retail's 31-word extent and shared
epilogue.

Semantic C emits 23 words directly. The remaining eight form one closed
success-path scheduling permutation: the incoming key load, floating-zero
setup, four initialization stores, retained result spill, and notification
argument are independent but ordered differently by IDO. Eight expected-word
guards restore retail's schedule without changing the instruction count or
control flow. Both call relocations, the allocator-call delay slot, the frame,
and the complete null path emit directly from C; the notification argument is
the guarded second-call delay slot.

## Verification

- The focused `generated_182C30` object builds with all 31 retail words.
- The complete ELF relink passes after regenerating every guarded object.
- Direct linked comparison reports zero differences across all 124 bytes.
- Both spans share SHA-256
  `4d92e5ed8d32b2f0a6b0c792b45f24b113301cb1eec8f2e968d9f65272daf21a`.
- The authoritative matcher omits `func_15155780` from its non-exact list and
  reports `2,989 / 5,465 (54.69%)` overall and `2,414 / 4,789 (50.41%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep `guMtxIdentF`
parked at its measured SDK compiler-profile boundary, and keep the documented
generated-slice ownership cases out of the ordinary C queue.
