# Registered update walker byte match

Date: 2026-11-12. `func_151670C0` replaces a zero-return placeholder in
`conker/src/game_1944C0.c`. Its 74-word body spans VA
`0x151670C0..0x151671E8` and ROM `0x194570..0x194698`; the original assembly
is in `conker/asm/nonmatchings/game_1944C0/func_151670C0.s`.

The routine visits two rows of 101 registered update lists. For each enabled
descriptor it increments the nesting depth, saves a node's next pointer in the
current iterator slot before the callback, and reloads that live slot after
the callback. It then restores the depth. Callback pointers are reloaded as
the walk continues. The original frame-loop call at `0x1501936C` ignores the
return value, so the recovered interface is `void`.

IDO emits 74 raw words. **35 expected-word guards and no inserted words**
normalize the body and relocation bindings to retail. This is a guarded C
match, not a direct compiler match.

Guest execution of both bodies agrees with an independent model across 96
cases, reaching all 74 retail words. Native SDK32 O0/O2/O3 each pass those
cases and five negative controls with undefined-behavior sanitization. The
original caller window passes 32 cases. The corpus includes empty and
multi-node lists, both rows, callback replacement, next-link mutation and
mutation of the saved iterator slot. Callbacks are modeled; full frame-loop,
arbitrary aliases, invalid nesting depths, native or hardware faults, and
gameplay are outside these checks. Iterator depths were bounded to the six
available slots.

An additional 80 connected cases execute the retail `func_151563B8` callback
inside both walker bodies; that callback's words also match the current ELF.
The cases include 136 callback entries and 26 removal requests. The removal
provider remains modeled, so this is not a full lifecycle or gameplay check.

Both padders reproduce the assembled retail body and relocation bindings.
Twelve rebased GNU links, 270 bounded access-cut triples and 70 corrupted-guard
rejections pass. Actual Make agrees with the strict independent image audit:
**224 changed bytes**, zero exclusions, all 6,050 function addresses and 41
neighboring functions unchanged, and 189,088 protected data bytes identical.
Actual ELF SHA-256: `c83885bb54941c88b5e5c911a44dd55052092308b3c8bd14dab94c111a1101af`. The existing complete-ROM checksum
mismatch remains.

Fresh actual ELF recount: **3,684 / 4,840 (76.12%)** Game and **4,357 /
5,513 (79.03%)** overall, zero drift. The Game-specific 80% target needs
188 more exact functions. Tools commit `10d5e85f4460bfc9d0fdbdc9b7bf30482b38b094` precedes the consumer change.

The adjacent secondary-callback walker `func_151671E8` is the next private
candidate. Its initial source emits 74 words with 35 positional differences,
and 96 guest cases agree with retail using modeled callbacks. It is not yet
qualified or credited. In particular, its callback lives at descriptor offset
4, currently described as padding in `struct115`; the tentative overlay needs
an effective-type and caller audit before native or production adoption.
