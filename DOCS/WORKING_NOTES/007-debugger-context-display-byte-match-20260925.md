# Debugger Context Display Byte Match

Date: 2026-09-25

## Result

`func_16000590` now matches the complete retail range
`0x16000590..0x160006CC`: 79 words, 316 bytes, and zero differing words.

The source already represented both display loops correctly. Reusing
`temp_s2` for the right-shifted status bits, instead of introducing a separate
`var_s2`, grew IDO's compact body from 78 to the required 79 words and restored
the retail value lifetime. IDO still stack-homed the original context pointer,
while retail retains it in `s5` across the calls and both loops.

`conker/retail_word_patches.us.csv` therefore carries 53 guarded replacements.
They restore the `s5` lifetime and saved-register frame, volatile-register
coloring, call/delay-slot schedule, second-loop tail, epilogue, and six moved
relocations. Every row verifies the exact compiler-produced input word; the
build fails if the maintained C or compiler output drifts.

## Verification

These commands pass:

```sh
python3 -m unittest tools.tests.test_pad_c_object_word_patches
make -C conker replace NON_MATCHING=1 -j4
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

A direct byte comparison of 316 bytes between `assets/debugger.us.bin+0x590`
and the pristine ROM at `0x255E10` also passes. The linked matcher reports:

- total: `2524 / 5497 (45.92%)`, one address-drift blocker, 2,972 different;
- debugger: `178 / 181 (98.34%)`, no blockers, three different.

## Sibling Audit

`64CBFDOGL` contains generated recomp translations of `func_16000590`, not the
decomp C object-padding pipeline. The IDO register-allocation normalization is
not applicable to its host source. Its existing dirty worktree was left
untouched, and the frozen Release configuration was neither built nor launched.

## Resume Boundary

Continue with `func_16001044`, the decimal/hex/float drawing dispatcher. It has
151 real differences across 155 words. Establish the retail frame, mode switch,
and call graph first; then isolate compiler lifetime and scheduling differences.
The remaining debugger functions are `func_1600078C` (180 differences) and
`func_16000B14` (277 differences).
