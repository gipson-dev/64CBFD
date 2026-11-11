# Radial callback dispatcher guarded byte match

Date: 2026-11-10. `func_1514C2F0` is restored as a radial callback dispatcher
in `conker/src/game/generated_176A00.c`; its original assembly remains in
`conker/asm/176A00.s`. The 96-word routine occupies VA
`0x1514C2F0..0x1514C470` and ROM `0x1797A0..0x179920`, with a 0xA0 frame.
The recovered semantic C compiles to 96 words; **17 expected-word guards**
normalize register allocation and independent scheduling to produce the retail
body. This is a guarded match rather than a direct compiler match.

For each positive-count iteration the routine samples the byte-angle helper
twice, forms radial X/Z coordinates, and reads a callback from `D_8008AA00`.
A non-null callback receives the position, center, angle, and additional
arguments; a zero return breaks iteration. The signed step is reloaded from
its argument home each iteration and the angle wraps to a byte. The existing
C caller declaration in `generated_EEB10.c` now returns `void`, consistent
with the three bounded original caller continuations, which ignore the return
register. The entire padded caller object and its 11 sections remain byte
identical; this observation does not qualify the full parents.

Qualification covers 900 guest cases / 2,700 executions and all 96 body
instructions, including callback-table and step-home mutations. Native SDK32
checks cover 750 defined cases per O0/O2/O3 with UBSan and eight effective
negative controls. The three original caller windows pass 144 connected
triples. The original 27-word angle helper and sine table are connected for
512 cases covering every byte angle and helper instruction. The callback is
still modeled; hardware FCSR, full callback and parent behavior, and portable
fault behavior are not claimed.

Both object padders agree, 392 corrupted byte/binding inputs and 17 individual
guard corruptions are rejected, and 16 rebased links plus 303 access-cut
quads pass. Actual Make rebuilt both owners; the independent complete-image
prediction explains **299 changed bytes** with zero exclusions. All 6,050
function addresses and 189,088 protected data bytes remain unchanged; 35
other target-owner functions and all three caller-owner functions are
unchanged. The actual ELF SHA-256 is `87be35cb4b134edbdb7d5d3ddf47746bb0ed251cf98c2a676497c79956a538ac`. The existing
full-build checksum mismatch remains, so this is not a complete ROM match.

Fresh actual ELF recount: **4,326 / 5,513 (78.47%)** overall and **3,653 /
4,840 (75.48%)** Game, zero drift and 1,187 different. The 80% target needs
85 more exact functions. The tools were committed first as
`eec90fcf97fb9d0c78317f27c355c7c7e48a28f2`; the consumer change is committed
separately. No push is implied.
