# Timed effect callback guarded match

Date: 2026-11-12. `func_150E4CBC` replaces a zero-return placeholder in
`conker/src/game/generated_111670.c`; retail assembly is in
`conker/asm/111670.s`. The 82-word body spans VA `0x150E4CBC..0x150E4E04`
and ROM `0x11216C..0x1122B4`.

The callback uses the effect age and strength to update a scaled field,
adjusts its intensity or marks it finished, updates a second scaled field,
and advances age by the global tick. Unsigned low-word arithmetic preserves
the retail wraparound before signed division and conversion. Both original
dispatch windows select it through `D_8008C9C8[13]` and ignore its incidental
return register.

Signed conversions from wrapped words and right shifts of negative values
follow the target and tested host compilers' two's-complement behavior; those
operations are implementation-defined in standard C.

IDO emits 82 raw words. Fifty expected-word guards, with no inserted words,
restore retail register allocation, scheduling and branch layout. This is a
guarded C match, not a direct compiler match.

Retail and candidate guest execution agree with an independent model across
600 cases, including signed and wrapping boundaries, covering all 82 retail
words. SDK32 native O0/O2/O3 each pass those cases and ten effective negative
controls under undefined-behavior sanitization. The original windows in
`func_15167E0C` and `func_15168870` pass 1,200 cases combined. The inputs use
valid aligned records disjoint from tick storage; full dispatcher behavior,
arbitrary aliases, hardware faults and gameplay are not established.

Both padders reproduce separately assembled retail code and bindings. Twelve
rebased GNU links, 31 bounded access-cut triples and 100 corrupted-guard
rejections pass. Actual Make agrees with the strict independent image audit:
234 changed bytes and zero exclusions. All 6,050 function addresses, eight
owner neighbors and 189,088 protected data bytes remain unchanged. Actual ELF
SHA-256: `975fc7c38a7b37cd1af6d8574664c3c3c483489751efd879c042b5254ce456aa`. The pre-existing complete-ROM checksum mismatch
remains.

Fresh actual ELF recount: **3,687 / 4,840 (76.18%)** Game and **4,360 /
5,513 (79.09%)** overall, zero drift. The Game 80% target needs 185 more
exact functions. Tools commit `704d0336b21f8e772236ed3a8ccd033ca5a18fb4` precedes the consumer change.
