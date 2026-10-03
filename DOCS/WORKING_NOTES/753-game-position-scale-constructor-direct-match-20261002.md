# Game Position/Scale Constructor: Direct Match

Date: 2026-10-02

## Result

`func_150448D0` replaces its zero-return placeholder with a complete
position/scale record constructor. Its entire 37-word / 148-byte slot matches
retail directly under the generated slice's existing `-O2 -g3` profile.
No expected-word guards, compiler override, or overflow body is required.

The checkout began clean at `e5e3c8c`. Source owner:
`conker/src/game/generated_71820.c`; reference: `conker/asm/71820.s`.
Retail address span: `0x150448D0..0x15044964`.
ROM byte span: `0x71D80..0x71E14`.

## Recovered Contract

The function takes nine arguments: three full-word values forwarded to the
common allocator, three full-word scale inputs narrowed by halfword stores,
one full-word value narrowed by a byte store, and two halfword-array pointers.
It requests the record through:

```c
record = func_15044964(0x20, 1, arg0, arg1, arg2, 0, 0, 0);
```

If allocation returns null, the constructor returns null without writing any
fields. Otherwise it sets:

| Offset | Width | Value |
| --- | --- | --- |
| `0x10` | Halfword | `arg3`, low sixteen bits |
| `0x12` | Halfword | `arg4`, low sixteen bits |
| `0x14` | Halfword | `arg5`, low sixteen bits |
| `0x16` | Byte | `arg6`, low eight bits |
| `0x18` | Guest pointer word | `arg7`, position array |
| `0x1C` | Guest pointer word | `arg8`, scale array |

It returns the allocated record identity. Earlier record fields and the
padding byte at `0x17` are untouched by this constructor. Pointer pointees
are neither read nor written here.

The slice already has `PositionScaleRecord71820`, used by `func_15044CE4`
to read the position/scale arrays and write the three scale fields. Its old
two-byte padding at `0x16` is now represented as `flags` and `pad17`, without
changing any guest offsets or the 32-byte size. No meaning for individual
bits in the stored byte is established by this recovery.

The common allocator declaration and placeholder signature were corrected to
return the record pointer and accept the eight observed arguments. **Its body
is still a null-return placeholder.** This constructor match does not establish
an operational allocation path or gameplay acceptance. Recovering that shared
body is the next dependency, not completed work.

## Compiler Evidence

The first semantic source trial emits all 37 retail words directly. The
compiler reproduces the `0x28` frame, incoming argument home stores,
allocator argument forwarding, zero outgoing stack arguments, null-return
branch, field-store widths/order, returned pointer, and final return delay nop.
There is no normalization table change or isolated compiler-profile tuning.

## Behavior Tests

`tools/tests/test_game_position_scale_constructor.py` extracts both the actual
record declaration and production constructor body. Seven freestanding 32-bit
tests preserve the guest pointer width and cover:

- Record size and every field offset written by the constructor.
- Allocation failure, argument forwarding, and absence of field writes.
- Full signed-word forwarding and exact successful write bounds.
- Halfword truncation, including negative and out-of-range inputs.
- Every low-byte value, wider flag inputs, negative input, and null pointers.
- Preservation of bytes initialized by the allocator mock.
- Repeated construction and replacement of both pointer identities.

The allocator is mocked to qualify the constructor independently. Tests compare
all 32 record bytes, not only named fields. They do not exercise the unfinished
common allocator, guest gameplay, or the downstream array-update routine.

## Verification

- Focused generated-slice build passes.
- `make -C conker NON_MATCHING=1 all match-progress -j4` passes.
- All seven new tests and all 106 tests under `tools/tests` pass.
- `make tools-check` passes.
- Independent linked-function extraction matches all 148 retail bytes.
- The following function remains at `0x15044964`.
- Both entire Init code/data sections remain exact: 164,048 and 17,376 bytes,
  with the unchanged hashes recorded in Note 749.

The shared SHA-256 of the linked and retail constructor spans is:

```text
f407f9766dc29a3982b06bc7362c415fea2a70900e617baa5c80d4a54d45b186
```

Fresh exact counts are Total 3,252 / 5,461 (59.55%), Game 2,579 / 4,788
(53.86%), Init 492 / 492, and Debugger 181 / 181. Address drift is zero;
2,209 Game C rows remain different. Converted-function and byte totals do
not change because the prior placeholder already counted as C.
README changes are limited to the aggregate exact/different table.

No compressed-ROM replacement build or gameplay test was performed. The
sibling host port and frozen Release artifacts remain untouched.

## Resume

Recover dependency `func_15044964` next: 49 retail words, currently 48
retail-slot differences. Retail requests memory, initializes the common
record header, and appends it to the list at `D_800CBE00`. Verify its allocator
failure, list-head/tail behavior, argument narrowing, and returned identity
before claiming the complete constructor allocation path is restored.

The other ordinary queued placeholders remain `func_1508B20C` and
`func_1509F6E8`. Keep the semantic-but-nonmatching dispatcher `func_15040CC8`
in its overflow queue, as documented in Note 752.
