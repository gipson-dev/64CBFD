# Resource table loader byte match

Date: 2026-11-11. `func_150163D0` replaces the zero-return placeholder in
`conker/src/game/generated_43880.c`; original assembly is in
`conker/asm/43880.s`. The 75-instruction body begins at VA `0x150163D0`, ROM
`0x43880`; the 76-word retail slot includes one trailing alignment NOP.

The routine requests resource path `(3, 12, resource, 9)` through
`func_1502B7F0`. On a positive signed result it counts zero-terminated
eight-byte records and relocates each first word against the loaded table
base; otherwise it clears `D_800D18B0`. The one identified direct retail
caller, `func_15007B3C`, ignores the incidental return register. A scan for
the literal function address found no retail-ROM pointer, but does not rule
out every possible indirect call.

The compiler emits 75 body words. **52 explicit expected-word guards**
replace differing control-flow, register-allocation and scheduling words;
the guards preserve the three original relocation sites. The guarded body
and bindings match retail. This is not an unguarded C match.

The raw C and retail guest executions agreed in 195 cases covering zero to
12 entries, five loader results and three resource IDs; 74 of the 75 retail
body words were executed. SDK32 native runs at O0, O2 and O3 each passed 65
cases and nine negative controls with undefined-behavior sanitization. The
original caller window at `0x15007F60..0x15007F6C` passed 195 cases; the full
parent was not qualified. The loader helper is modeled, with its arguments
checked. These tests use valid, aligned, disjoint table and global storage;
arbitrary aliasing, concurrent mutation, hardware faults and the incidental
return register are not qualified.

Both padders agree with independently assembled retail code and bindings.
Twelve GNU rebased links, 100 bounded access-cut triples and 104 deliberately
corrupted guard checks pass. Actual Make and strict independent image
comparison account for **221 changed bytes** with zero exclusions.
All 6,050 function addresses and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `eb696b14112ccafa1f482a3244b4046fe7dc818194d304c3579e3557a55e7041`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,343 / 5,513 (78.78%)** overall and **3,670 /
4,840 (75.83%)** Game, zero drift and 1,170 different. The 80% target needs
68 more exact functions. Tools commit `42a4d8be7a3fee88439fb3b61e9c4ec07543b91a`
precedes the consumer change.
