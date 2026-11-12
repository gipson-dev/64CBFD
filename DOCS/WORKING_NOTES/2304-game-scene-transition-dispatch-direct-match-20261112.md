# Scene transition dispatcher direct match

Date: 2026-11-12. `func_1501C730` in `conker/src/game/generated_49BE0.c`
replaces a zero-return placeholder. Its 74 retail words occupy VA
`0x1501C730..0x1501C858`, ROM `0x49BE0..0x49D08`; its padded slot ends at
`0x1501C860`. It emits the original instructions directly from semantic C,
without guards or insertions.

The routine first calls `func_1501C53C` and clears `D_800D2132`. Its switch
accepts five full-word arguments. Commands 4 and 6 save both trailing words,
the scene word and channel byte and set transition mode 2. Commands 1 and 2
set mode 3, save the scene and copy `D_800CC2D0[0].unkB2`; command 2 also
saves the channel. Command 3 sets mode 4 and invokes `func_15016680` only if
the gate byte is clear. Command 5 stores scene value 5 and sets mode 1. Zero
and out-of-range commands leave the transition halfword cleared. The explicit zero-case
store keeps IDO's original table range; IDO folds the repeated store into the
single retail instruction.

The object halfword is accessed as the actual `struct127` member, avoiding a
separate interior data declaration. Its HI/LO relocations use the parent
object symbol plus `0xB2`; the SDK32 test verifies the field offset. The
existing project declares `D_800BE9F4` as a pointer, so storing scene values
uses 32-bit integer-to-pointer conversions. Their representation is target
implementation-dependent; no portable-pointer or host-gameplay claim follows.

Both padders preserve all seven generated switch destinations and bind their
relocations to the retail table `jtbl_800969A0_game`; no table is copied into
protected data. Eight controls reject individual entry or relocation corruption.
Guest tests run 156 modeled-helper cases per retail and candidate body, visit
all 74 words, and run both against the original 16-, 13- and 4-word helper
bodies in 128 cases. All 33 helper words execute and match the current ELF.
The original five-word `func_151E327C` caller window passes 60 cases; the
complete parent is not qualified by this test. Native SDK32 O0/O2/O3 with
trapping UBSan each pass 78 cases and ten effective semantic controls. Twelve
GNU links cover four independent rebases, including the member-addend carry;
454 paired guest access cuts preserve instruction-order behavior. These cuts
do not establish portable C fault behavior or hardware/gameplay acceptance.

The actual three-command Make recipe and independent strict linked-image
prediction agree: 284 changed ELF bytes, zero exclusions,
all 6,050 function addresses fixed, and all 189,088 protected Game-data bytes
unchanged. Actual ELF SHA-256: `f8d80f4a79ae0ba0fde2c4dd19722199dcc4ad10ae1eba51d44bd026a628f870`. The existing whole-ROM
checksum mismatch remains.

Fresh ELF recount: **3,702 / 4,840 (76.49%)** Game and **4,375 / 5,513
(79.36%)** overall, zero address drift. The Game 80% target needs 170 more
matches. Tools commit `a0033438688cb235e65b7bb2f5208a83ea89d88d` precedes this consumer change.
