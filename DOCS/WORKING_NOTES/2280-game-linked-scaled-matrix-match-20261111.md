# Linked scaled-matrix transform byte match

Date: 2026-11-11. `func_151B76CC` replaces the zero-return placeholder in
`conker/src/game/generated_1E37D0.c`; the retail assembly is in
`conker/asm/1E37D0.s`. Its 74-word body spans VA
`0x151B76CC..0x151B77F4`, ROM `0x1E4B7C..0x1E4CA4`.

The typed C routine constructs a rotation matrix from a linked source, copies
the source translation, scales its first and third rows by the X scale and its
second row by the Y scale, and transforms the local offset `(0, 0, -250)` into
the supplied position. The owner layout includes its position at offset
`0x10`, matching the output alias used by both identified callers.

The compiler emits 74 raw words. **38 expected-word guards and no inserted
instructions** normalize register allocation and scheduling to the retail
body and its relocation bindings. This is a guarded, not an unguarded, C
match.

Retail and raw C guest executions agreed across 600 finite cases and visited
all 74 retail words. SDK32 native O0/O2/O3 each passed those cases and nine
negative controls with undefined-behavior sanitization. Both original caller
windows, in `func_151B7328` and `func_151B77F4`, passed 300 cases each through
`D_8008FB90[1]`, including the owner-position output alias. The two matrix
helpers were modeled; their implementations and the full parent functions
were not qualified. Tests use valid finite inputs and separate owner, source,
link and stack storage, with either a separate output or the documented owner
position alias. Other aliases, concurrent mutation and hardware faults are not
qualified.

Both padders match independently assembled retail code and bindings; 12
rebased GNU links, 200 bounded access-cut triples and 76 corrupted-guard
rejections pass. Actual Make and strict independent image comparison account
for **230 changed bytes** with zero exclusions. All 6,050 function
addresses, 16 neighboring functions and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `95ff3381f8d0abda487f09b73429c0960f39a64d0db5cec1b71ca22262ef9ad8`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,348 / 5,513 (78.87%)** overall and **3,675 /
4,840 (75.93%)** Game, zero drift and 1,165 different. The 80% target needs
63 more exact functions. Tools commit `ad739915df2b810fe49bf04121ed264b3d0ed1a6`
precedes the consumer change.
