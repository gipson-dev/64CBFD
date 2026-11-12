# Rotation matrix callback private screen

Date: 2026-11-12. `func_15187D6C` in
`conker/src/game/generated_1B1600.c` remains an unconverted placeholder.
This is a private screen; it does **not** change the production match count.
The routine's executable span is 83 words at VA `0x15187D6C..0x15187EB8`,
ROM `0x1B521C..0x1B5368`; the 85-word layout slot includes two padding words.
It uses a `0x48`-byte frame. Its original caller around `0x15187BD8` passes
a matrix pointer and three float bit patterns in A0..A3, choosing this routine
when the selected record's byte at offset `0x98` is nonzero. The following
call combines the resulting matrix with another matrix. This observation does
not establish every caller or the complete caller's behavior.

The original routine scales each angle by the float at `D_8008D578` (retail
bits `0x3C8EFA35`), calls `sinf` then `cosf` for each angle, initializes an
identity matrix through `func_151EFE00`, and writes the nine rotation cells.
This partial reconstruction was compiled in the complete owner with its actual
`-O2 -g3 -Wo,-loopunroll,0` profile. It retains all 31 other raw owner
functions. The initial O2-only screen was invalid for this owner because it
unrolled neighboring `func_15187978` beyond its slot; the actual Make override
must be retained in any further work. The 24 variable-order screens used O2,
and the selected order was separately recompiled with the actual profile.

The selected body has the original 83-word length and ten differing positions
when instruction words and relocations are compared against independently
assembled retail. Eight positions move the initial global-address setup and
saved-register schedule, including four relocation changes; the other two
move one temporary from stack offset `0x38` to `0x3C`. With ten proposed
checked guards, both padders produce the same retail words and relocations and
all 32 padded owner functions agree. Each guard was corrupted separately and
rejected by both padders; four symbol rebases agree with GNU linking.

A bounded finite-input model ran 686 angle/stack-phase cases for each raw,
retail, and guarded body and reached all 83 retail instructions. Six
trigonometric calls and identity initialization were modeled; the complete
real helpers and hardware FPU behavior were not run. An independent SDK32
native screen passed 343 cases at each of O0, O2 and O3 under trap UBSan and
five effective semantic negative controls. The original caller window
`0x15187BD8..0x15187BF8` passed 250 connected modeled cases, stopping at the
next matrix-combination helper; this is not a full parent execution.

A private Make-planned owner compile and shadow link used the same candidate
and guards. The predicted ELF has 298 changed bytes and two audited symbol
order groups, with zero exclusions. All 6,050 function addresses and all
189,088 protected Game-data bytes are unchanged; all 31 other padded owner
functions agree. Predicted ELF SHA-256
`487d69181acd1fb7108c4a1dd34b025e564f71ad37b500739fa0677ec2798225`.
Baseline production ELF SHA-256
`3a875cb61d873bbb37338026bae52818d73aa2c70f2bc1543aec4dcb71bae0e1`.
No production source, guard file, object, ELF, or counter was changed.
The temporary files and receipts are under ignored
`conker/build/game-rotation-15187d6c-screen/`; they may be cleaned.

The candidate source, requiring `extern f32 D_8008D578;` and
`void func_151EFE00(f32 [4][4]);`, is preserved here for a fresh screen:

```c
void func_15187D6C(f32 m[4][4], f32 x, f32 y, f32 z) {
    f32 sx, cx, sy, sz, cy, cz, t;
    x *= D_8008D578; y *= D_8008D578; z *= D_8008D578;
    sx = sinf(x); cx = cosf(x);
    sy = sinf(y); cy = cosf(y);
    sz = sinf(z); cz = cosf(z);
    func_151EFE00(m);
    t = sx * sy;
    m[1][2] = sx;
    m[0][0] = cy * cz - t * sz;
    m[0][1] = cy * sz + t * cz;
    m[0][2] = -sy * cx;
    m[1][0] = -cx * sz;
    m[1][1] = cx * cz;
    t = sx * cy;
    m[2][0] = sy * cz + t * sz;
    m[2][1] = sy * sz - t * cz;
    m[2][2] = cx * cy;
}
```

Next: create durable reproducible qualification in the tools repository;
check changed diagnostics, independent access/fault prefixes and symbol
bindings, and test in both mounted and standalone-sibling tools environments.
After private qualification, adopt the candidate and verify the actual Make
build and complete production image before crediting it; then recount, update
the aggregate README and refresh the scoped graph. The guarded result restores retail instruction order; the
raw candidate's earlier/later global load and different private stack slot do
not establish arbitrary alias or fault equivalence. Do not count a shadow
result as a production match.

Current production recount remains Game **3,710 / 4,840 (76.65%)**, total
**4,383 / 5,513 (79.50%)**, zero drift; 162 more Game matches to 80%.
