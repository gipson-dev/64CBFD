# Game descriptor float-forwarding adapter byte match

Date: 2026-09-29

## Scope and behavior

`func_150B9D14` in `conker/src/game/generated_E5E90.c` spans 30 words and
120 bytes. It preserves its first argument and forwards three word fields plus
eight floating-point fields from its descriptor argument to `func_15142600`.
The floating-point values are taken from descriptor offsets `0x30`, `0x34`,
`0x38`, `0x3C`, `0x40`, `0x20`, `0x24`, and `0x28`, in that retail order.
After the call it returns one.

The recovered twelve-argument prototype exposes the outgoing ABI and naturally
reproduces retail's `s0` descriptor lifetime, 0x40-byte frame, and eight stack
stores. The complete routine emits directly from C with no guarded words.

## Verification

- The focused padded object reproduces all 30 retail instructions.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `235546b1e70cf0682de3289f8d12540ad11fc76ceef2f6e0f0288f20c68f186b`.
- The authoritative matcher reports `2,974 / 5,465 (54.42%)` overall and
  `2,400 / 4,789 (50.11%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep
`func_15022640` and `func_150B66DC` parked at their measured IDO register and
return-value scheduling boundaries.
