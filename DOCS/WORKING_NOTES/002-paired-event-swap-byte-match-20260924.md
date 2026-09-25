# Working Note 002: Paired Event-Swap Byte Match

Date: 2026-09-24

## Scope

Match the two 19-word event handlers selected in Working Note 001:

- `func_151906E0` in `conker/src/game/generated_1BA1D0.c`
- `func_151C1814` in `conker/src/game/generated_1ED0F0.c`

No broad conversion work was included.

## Measured mismatch

Each linked function differed from retail by one instruction. At
`0x15190718` and `0x151C184C`, the compiler emitted `bne a2,t8`; retail uses
`bne t8,a2`. All other words in both functions already matched.

Swapping equality operands, changing the early return to an `else if`, adding
casts, and storing the field value in a temporary all retained the wrong
operand order. Compiling with `-O2` without `-g3` also changed the prologue and
did not solve the comparison.

## Matching source shape

The second equality is expressed as unsigned subtraction to zero:

```c
if (temp_v1 == temp_a2) {
    field = arg1[1];
} else if ((u32) arg1[1] - (u32) temp_a2 == 0) {
    field = temp_v1;
}
```

For 32-bit unsigned values, the subtraction is zero exactly when the operands
are bitwise equal. This shape makes IDO 5.3 emit retail's `bne t8,a2` at both
sites without changing function behavior.

## Verification

The linked instructions now match at both former mismatch addresses. The
fresh linked scan reports:

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 2,519 / 5,497 (45.82%) | 1 | 2,977 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 1,959 / 4,808 (40.74%) | 0 | 2,849 |
| Debugger | 173 / 181 (95.58%) | 0 | 8 |

These commands passed:

```sh
make -C conker build/conker.us.elf NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
make -C conker replace NON_MATCHING=1 -j4
make NON_MATCHING=1 -j4
```

The build retains existing IDO pointer/integer warnings in
`generated_1BA1D0.c`; this change introduced no new warning class. No gameplay
run was needed because this pass changes compiler expression shape while
preserving behavior and verifies the complete linked instruction bodies.

## Sibling audit

`64CBFDOGL/recomp_out/.c` already contains generated N64Recomp translations of
both original 0x4C-byte routines. The matching-only C expression change does
not transfer to that architecture, so no sibling source change or build is
applicable. The frozen OGL Release artifact was not touched.

## Resume boundary

Resume byte matching with debugger `func_16001390`, whose two remaining words
are independent scheduling differences. `func_15135480` is a useful game
follow-up: it contains the same branch-operand mismatch solved here, but also
has one additional difference that must be isolated separately.
