# Init handwritten interrupt-wrapper restoration - 2026-09-26

## Result

`__osDisableInt` and `__osRestoreInt` are restored from false C placeholders
to original handwritten assembly ownership. Both complete eight-word,
32-byte spans match retail. The fresh C-only matcher reports 2,689 / 5,475
exact functions overall and 388 / 501 in Init.

## Ownership evidence

The preserved `asm/libultra/os/interrupt.s` explicitly marks both routines as
handwritten. `__osDisableInt` reads CP0 Status with `mfc0`, clears bit zero,
writes the result with `mtc0`, and returns the old interrupt-enable bit.
`__osRestoreInt` reads Status, merges the caller's saved bit, writes Status,
and retains the required hazard and alignment nops.

The generated C file instead returned zero from `__osDisableInt` and did
nothing in `__osRestoreInt`. C cannot express the required `mfc0`/`mtc0`
operations, so guarded replacement of compiled placeholder words would be the
wrong ownership model.

## Build integration

`src/game/generated_interrupt.c` now uses one tracked `GLOBAL_ASM` body for
each symbol. The preserved full assembly remains the retail-layout authority
for `pad_generated_object.py`. The restore snippet includes the trailing
alignment `nop` in its declared eight-word extent. No guarded word-patch rows
were added.

## Exact-byte evidence

| Function | Address | Bytes | SHA-256 |
| --- | ---: | --- | --- |
| `__osDisableInt` | `0x10022DC0` | `400860002401fffe0101482440896000310200010000000003e0000800000000` | `b5ec893cd5c1e37c723f982142b67fc24befcf35b6e48b596abbcca4c4d44560` |
| `__osRestoreInt` | `0x10022DE0` | `400860000104402540886000000000000000000003e000080000000000000000` | `760fabe684a57096a1f98fb972d27fc9ae0f5b227768fa227ed73c15b4ad1e09` |

The linked Init spans and pristine `conker.us.bin` spans compare equal. The
corrected conversion inventory is 5,475 / 6,038 functions and
1,932,264 / 2,256,728 bytes overall. Init is 501 / 538 functions and
148,792 / 164,048 bytes. Exact C numerators remain unchanged because two
non-exact C rows correctly left the denominator.

## Sibling audit

`64CBFDOGL` keeps both symbols in its recomp inventory and generated dispatch,
with no native source override found. This guest ownership correction does not
justify editing generated host output independently. The sibling's 1,659
existing dirty entries were preserved, and frozen Release was not built,
modified, or launched. `build/Release/conker_pc.exe` remains 13,712,896 bytes
with timestamp `2026-09-23 05:04:28`.

## Validation

- The focused `generated_interrupt.c.o` build passes.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and summary/list `match-progress` runs pass.
- Both independent 32-byte linked-versus-retail comparisons pass.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Init C matching with 22-word `func_100043B4`, the first
non-blocked row in the fresh difference list. It has six real differences and
is smaller than the tied 47-word `func_1000FD38`. Keep address-blocked
`func_10012588` parked.
