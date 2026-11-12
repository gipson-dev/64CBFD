# Game position interpolation candidate screen ? 2026-11-12

`func_150BE2E8` remains an **uninstalled, uncredited candidate**. Consumer baseline `6a40a4b0`; tools submodule `7b9cdb9`. The last production recount is Game 3,703 / 4,840 (76.51%), with 169 more exact functions needed for 80%.

## Retail evidence

- The 84-word slot is VA `0x150BE2E8..0x150BE438`, ROM `0xEB798..0xEB8E8`, in `asm/EB340.s`; `generated_EB340.c` still contains a zero-return placeholder.
- The routine reads signed halfwords at offsets `0x7C..0x86`, `0x3C`, and `0x3E`, and writes signed-halfword results at `0x10..0x14`, `0x3C`, and `0x3E`. It converts the latter two inputs with `1/16384`, applies `D_800A0068` and `D_800BE9E4`, calculates three interpolated values, clamps progress above 1 only after calculating those values, and scales the final progress and step by 16384.
- `asm/data/22D710.rodata.s` contains a function-pointer entry for this target; its complete dynamic dispatch and caller contract have not yet been qualified. The live Makefile still uses the owner's ordinary profile; target-only profile routing has not been installed or validated.

## Private compiler screen

The candidate below is an experiment, not a proven semantic recovery. Using the existing IDO 5.3 owner compiler, `-O2 -g3 -Wo,-no_const_in_reg` yields 84 words and the retail `0x18` frame. After binding the four HI16/LO16 relocations for the two globals to the current linked symbols, 74 of 84 word positions agree. The ten differences are:

| Offset | Candidate | Retail |
| --- | --- | --- |
| 0xAC | `46145102` | `460AA102` |
| 0xB0 | `46162580` | `4604B580` |
| 0x114 | `44814000` | `44810000` |
| 0x118 | `44813000` | `00000000` |
| 0x11C | `4608A282` | `4600A202` |
| 0x124 | `4606B202` | `4600B102` |
| 0x128 | `4600510D` | `4600428D` |
| 0x12C | `4600428D` | `4600218D` |
| 0x130 | `440A2000` | `440A5000` |
| 0x134 | `440C5000` | `440C3000` |

The first pair changes multiply operand/register order; the final eight alter constant and floating-register allocation. Treat them as hypotheses requiring dataflow and exceptional-value proof, not as approved guards. Ordinary O2 produced 83 words and 47 same-position words after binding; O1 produced 111. Reversing the source order of the global multiplication or addition did not change these scores in this screen. No target-specific build rule, patch, or source was installed.

```c
extern f32 D_800A0068;
extern s32 D_800BE9E4;
void func_150BE2E8(s16 *p) {
    f32 x0 = p[0x7c/2], y0 = p[0x7e/2], z0 = p[0x80/2];
    f32 x1 = p[0x82/2], y1 = p[0x84/2], z1 = p[0x86/2];
    f32 step = p[0x3c/2] * (1.0f / 16384.0f);
    f32 t = p[0x3e/2] * (1.0f / 16384.0f);
    step = step - step * D_800A0068;
    t = t + step * D_800BE9E4;
    p[0x10/2] = (s32)((x1-x0)*t+x0);
    p[0x12/2] = (s32)((y1-y0)*t+y0);
    p[0x14/2] = (s32)((z1-z0)*t+z0);
    if (1.0f < t) t = 1.0f;
    p[0x3c/2] = (s32)(step * 16384.0f);
    p[0x3e/2] = (s32)(t * 16384.0f);
}
```

The compiled object and screen scripts are retained under the ignored `conker/build/game-motion-interpolation-screen/` directory, which is disposable and not part of the commit. Freeze the current source, inputs and tool hashes again before reusing them.

## Qualification still required

1. Verify global types, the registration table and actual callers; preserve source access and write order, including alias and fault behavior. Determine the behavior of signed truncation and narrowing for out-of-range, NaN and infinity rather than assuming portable C equivalence.
2. Check each mismatch by instruction-level def/use and guest execution, including NaN payloads, signed zero, infinities, denormals, overflow, negative values and clamp boundaries. Use effective negative controls. Any guards must have expected words and correctly preserve relocation and all dependent uses.
3. Prove owner neighbors, both padding paths, ABI/caller windows, native defined-domain behavior, full linked image and protected data. Run actual production Make, recount the actual ELF, update aggregate status only after all gates pass, then commit the tools and consumer in order if both change.

A second screened candidate, `func_1504A140`, appears to construct a 4x4 quaternion-derived matrix while leaving output slots 12?14 untouched. The initial source emitted 86 words with a `0x68` frame against the retail 92-word slot and `0x48` frame; 24 local-declaration permutations did not change that result. Its operation ordering, exceptional floats, buffer overlap and caller remain unqualified. The private screen is in ignored `conker/build/game-quaternion-matrix-screen/`.
