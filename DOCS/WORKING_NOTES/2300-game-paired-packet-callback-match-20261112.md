# Paired packet callback matches

Date: 2026-11-12. `func_1514E00C` and `func_1514E194`, both in
`generated_179F30.c`, replace zero-return placeholders. Their retail code
occupies 98 words each at ROM `0x17B4BC` and `0x17B644`. They differ in
only three retail words: a 20.0 versus 16.0 size and two global float loads.

Both callbacks prepare a descriptor, source and runtime record on the stack,
create an effect with `func_15189FF0`, pass the result and owner to
`func_1514EC1C` with key 6, and call `func_151D74B0` with mode 5. The
runtime snapshot includes the owner's byte at offset `0x3B`. The original
callback dispatcher window in `func_1514D15C` selects these through
`D_8008AA70` entries 1 and 2, supplies the owner, and does not consume the
callback return. This window is qualified; the whole parent is not.

The independently compiled C matches the retail stack layout, helper calls,
and body length. Each has eleven expected-word guards that reorder independent
stores into the original sequence; no guard modifies relocation records or
inserts instructions. Both padders reproduce independently assembled retail
objects and relocations. Deliberately corrupting each expected word was
rejected by both padders, for 44 rejected mutations.

Guest comparison exercised all 98 retail words and 80 cases per callback,
including allocation success and failure, owner-byte values and helper
mutation; helpers were modeled. The original dispatcher window passed the
same cases. SDK32 native builds at O0, O2 and O3 with UBSan each passed 1,024
cases per callback and detected nine deliberately incorrect variants. Twenty-four
GNU rebased links and 330 bounded guest access-cut triples passed. Guest access
cuts do not establish portable C, native or hardware fault behavior; complete
parent behavior and gameplay are outside these checks.

Actual Make agrees with the independent image prediction: 717 changed bytes,
three symbol-metadata reorder groups, zero exclusions, all 6,050 function
addresses fixed, all 76 neighboring owner functions preserved, and all 189,088
protected Game-data bytes unchanged. Actual ELF SHA-256: `b5e1ea465dee74abbd3f0fee856e7550d9970631a9f50457268a3304d6e5cd56`.
The existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,698 / 4,840 (76.40%)** Game and **4,371 / 5,513
(79.29%)** overall, zero address drift. The Game 80% target needs 174 more
matches. Tools commit `14f43c5e326dcf5c8a248bf4c74bc6ba1e953fd3` precedes this consumer change.
