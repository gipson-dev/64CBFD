# Channel-preset initializer byte match

Date: 2026-11-11. `func_1500AD84` replaces the zero-return placeholder in
`conker/src/game_36680.c`; original assembly is in
`conker/asm/nonmatchings/game_36680/func_1500AD84.s`. Its 97-word body spans
VA `0x1500AD84..0x1500AF08`, ROM `0x38234..0x383B8`.

The C routine initializes one channel from a 10-byte preset and its option
bits, applies the preset's flags and two halfword values, updates three
channel bitmasks, and clears or seeds the remaining channel fields. Preset
`255` uses the original disabled-channel path. It retains the incoming
options while reusing the parameter for preset flags. The original caller
ignores the function's incidental register result.

The semantic C emits 97 raw words, with 62 expected-word guards normalizing
register allocation and scheduling. Five guard sites also change relocation
bindings. The complete guarded body and bindings match retail; this is not an
unguarded C match. Raw C and guarded code are checked separately.

A bounded oracle compared retail, raw C and guarded output in 3,240 cases
and visited all 97 retail words. Native SDK32 O0/O2/O3 each passed the same
3,240 cases and 12 negative controls with undefined-behavior sanitization.
The original `func_1500BEC0` caller window passed those cases, and its
15-channel loop passed 32 multi-channel scenarios. The complete parent is
not qualified. Cases use channels 0 through 14 and synthetic contiguous
256-record preset backing; the synthetic high preset indices are not evidence
that the retail preset table has that many records. Arbitrary aliasing,
concurrent mutation, out-of-range channels and hardware faults are not
qualified. An aligned ROM scan found one direct JAL at `0x393F8` and no
aligned address literal.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 27 bounded access-cut triples and 196 corruption
rejections pass. Actual Make and strict independent image comparison account
for **465 changed bytes** with zero exclusions. Six symbol-order
metadata changes are recorded in the manifest. All 6,050 function addresses
and 189,088 protected data bytes remain unchanged. Four pre-existing owner
diagnostic groups remain unchanged. Actual ELF SHA-256: `bf11c706346f8a6818d531739379ebd1cd3b95ab1eeab9914fb9afec8cc39204`.
The existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,341 / 5,513 (78.74%)** overall and **3,668 /
4,840 (75.79%)** Game, zero drift and 1,172 different. The 80% target needs
70 more exact functions. The tools commit `71218953bda08b7aa7fa143a5838d45731af4b24`
precedes the consumer change.
