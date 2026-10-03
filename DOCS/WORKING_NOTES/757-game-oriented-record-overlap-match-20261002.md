# Game Oriented Record Overlap Recovery

Date: 2026-10-02

## Recovery

`func_15044B78` replaces its zero-return placeholder with the player/record
oriented overlap test. Its original slot is 91 words / 364 bytes at
`0x15044B78..0x15044CE4`, ROM `0x72028..0x72194`.

The saved draft from
[Note 756](756-init-resume-verification-and-conversion-boundary-20261002.md)
was applied without dropping the stash. The production body uses the existing
`-O2 -g3` slice profile, local `fabsf` intrinsic declaration, and six strict
expected-word guards. No whole-body replacement or profile override is added.

## Recovered Contract

The player is the byte-view global `D_800CC2D0`; its positions are floats at
`0x14`, `0x18`, and `0x1C`. Its dimension pointer is at `0x31C`, with signed
halfwords at `0x114`, `0x116`, and `0x118`. The retail loads are signed even
though a shared dimension declaration elsewhere uses unsigned fields.
This recovery preserves the signed local views without a broad header rewrite.

Before calling either angle helper, the routine caches:

```text
halfHeight = signedHeight >> 1
extentZ = signedDimension[0x116]
extentX = signedDimension[0x118]
x = playerX - record.x
y = (playerY - record.y) + halfHeight
z = playerZ - record.z
```

The height shift is arithmetic: an odd negative height rounds downward, not
toward zero as C division by two would. Record coordinates are signed halfwords
at `0x06`, `0x08`, and `0x0A` in the existing 32-byte record layout.

It calls `func_15048A40(record.flags)` and then
`func_150489B0(record.flags)`, reloading the unsigned byte at `0x16` between
calls. Calling them first/second basis helpers avoids inferring their complete
table provenance from naming alone. Their float results produce:

```text
rotatedX = z * second + x * first
rotatedZ = x * second - z * first
```

The original X working value is reused for `rotatedZ`. Strict comparisons
are performed in Y, rotated-Z, rotated-X order:

```text
abs(y)        < record.scaleZ + halfHeight
abs(rotatedZ) < record.scaleY + extentZ
abs(rotatedX) < record.scaleX + extentX
```

The signed record extents at `0x14`, `0x12`, and `0x10` are loaded after the
helpers, not cached before them. All comparisons must pass to return one;
otherwise it returns zero. Equality, nonpositive bounds, and unordered NaN
comparisons do not count as overlap. The routine itself writes no player,
dimension, or record fields. It does not add null-pointer checks absent from
retail.

## Float-Return Correction

`func_15048A40` was declared `void` while this retail caller consumes `$f0`.
Its declaration and definition now return `f32` explicitly:

```c
return func_150489B0((arg0 - 0x40) & 0xFF);
```

The corrected wrapper still emits its complete original 12-word / 48-byte
slot directly from C. The underlying lookup body is unchanged. A host test
mocks that lookup and checks all 256 input bytes, modulo-256 forwarding,
exactly one call, and non-integer positive/negative float return values.

## Source Shape and Stack Proof

The resumed draft emitted 92 words for the 91-word slot. Introducing an
explicit post-call height bound fit the slot but retained substantially
different scheduling. Reusing the X working value, initializing the three
deltas in sequence, and reordering meaningful player/float locals recovered
the original 91-word instruction order, registers, floating-point operations,
branch displacements, delay slots, and `0x48` frame.

The final unguarded body differs only at six integer stack accesses. Each
variable has one defining store and one later load, with no intervening
access to its private slot by this routine. The called helpers cannot receive
these local addresses. The strict guards remap the complete three-variable
store/load set together:

| Variable | Compiler slot | Retail slot | Store offset | Load offset |
| --- | ---: | ---: | ---: | ---: |
| `extentZ` | `0x20` | `0x1C` | `0x028` | `0x0C8` |
| `extentX` | `0x1C` | `0x18` | `0x034` | `0x110` |
| `halfHeight` | `0x24` | `0x20` | `0x08C` | `0x0BC` |

The three destination slots are distinct, above the outgoing argument area,
and do not overlap `$ra` at `0x14`, the float spills at `0x30..0x40`, or the
saved record pointer at `0x48`. All 85 other words emit unchanged. No frame,
call, branch, arithmetic, or floating-point instruction is normalized.
Each guard requires its precise expected compiler word; none permits mismatch.

## Tests

`tools/tests/test_game_oriented_record_overlap.py` extracts the actual record
type, overlap function, and corrected wrapper definitions. Its freestanding
32-bit fixture preserves pointer size and guest offsets. Byte-buffer overlays
use aligned storage and `-fno-strict-aliasing`; SSE single-precision arithmetic
and disabled contraction avoid x87 extended-precision boundary differences.
The process entry explicitly realigns the stack for the i386 C ABI.

Sixteen focused tests cover guest layout; no field writes; strict boundaries
on both sides of each axis; nonzero origins; quadrature and mixed-basis
rotation signs; odd signed heights; signed dimension/extents extremes;
nonpositive bounds; all 256 flag bytes and inter-call reload; pre-call position
and dimension caching; post-call extent reload; NaN/infinite coordinates;
adjacent representable floats at a bound; and the wrapper's float return.

The fixture initially exposed a host entrypoint alignment crash in the large
byte-preservation test. Correcting only its process-entry ABI made that test
pass; the recovered production routine was unchanged by that correction.

## Validation

The full `make -C conker NON_MATCHING=1 all match-progress -j4` rebuild passes.
All 147 tool tests, `make tools-check`, and `git diff --check` pass. The final
linked matcher reports Total 3,255 / 5,461 exact (59.60%) and Game
2,582 / 4,788 exact (53.93%), with zero drift and 2,206 differing C rows.
C representation totals do not change because the placeholder already counted
as C. README changes only the two affected aggregate matching rows.

Independent linked-span comparisons against retail confirm:

| Span | Bytes | Result |
| --- | ---: | --- |
| `func_150448D0` constructor | 148 | Exact |
| `func_15044964` allocator | 196 | Exact |
| `func_15044A28` list processor | 336 | Exact |
| `func_15044B78` overlap | 364 | Exact |
| `func_15048A40` float-return wrapper | 48 | Exact |

The following routine stays at `0x15044CE4`. Overlap SHA-256:
`f92d0c6b843b317fa86e8d6257518e06a7fb3f371ce529d965e8b18a7f6c5a8d`.
Float-return wrapper SHA-256:
`d5318150e1e7561a7e808e82934cac1cc5c70b7282300419f6964c1cbdcf967f`.

Independent ELF extraction also confirms the complete `.init` section
(164,048 bytes) and `.init_data` section (17,376 bytes) still match retail.
Their unchanged hashes are respectively
`34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`
and `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.
No gameplay qualification, compressed-ROM build, or guest execution is implied
by source fixtures or guest byte matching.

## Next Dependency

The linked callback table at `D_80085E80`, independently checked against
retail ROM offset `0x22A940`, contains `func_15044B78`,
`func_15044CE4`, and `func_15044D40`, followed by the secondary callback table
at `D_80085E8C`. The list processor consumes a signed callback result.

`func_15044CE4` already has a position-copy / signed-scale-divide C body, but
its source return type is `void`. Retail leaves the overlap return in `$v0`
through its epilogue. The next scoped task is to recover that explicit C
return contract, prove its complete 23-word span, and test the wrapper and
overlap together, including signed scale division and pointer aliasing.

The saved pre-recovery stash remains available as historical WIP, not as a
patch to apply over this completed source. No sibling host-port or frozen
Release artifact is changed by this guest decomp recovery.
