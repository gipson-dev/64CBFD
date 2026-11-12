# Oscillating effect direct C match

Date: 2026-11-12. `func_151DB97C` replaces a placeholder in
`conker/src/game_2062D0.c`. Its 75 words span VA `0x151DB97C..0x151DBAA8`
and ROM `0x208E2C..0x208F58`.

The callback advances three effect phases using the global tick, optionally
calls the damping helper, and multiplies three sine results by amplitudes to
write an output vector. It returns one. A nested parameter structure and local
variable ordering reproduce all instructions and relocations directly from C;
no word guards or insertions are needed.

Retail and candidate guest execution agree across 384 modeled cases and cover
all 75 retail words. Native SDK32 tests pass the same case count at O0, O2 and
O3 under UBSan with ten negative controls per profile. The original callback
table dispatch window passes 384 cases, including two return-branch negative
controls. Another 96 valid finite cases execute the actual retail damping and
sine helpers and their lookup table; all 16 and 27 helper words are visited.
These tests use valid disjoint records and do not establish full gameplay,
arbitrary aliases or hardware fault behavior.

Both padders reproduce independently assembled retail instructions and
relocations. Twelve rebased GNU links, 79 bounded access-cut triples and 81
fingerprint corruption controls pass. Actual Make agrees with the strict
independent image audit: 237 changed bytes and zero exclusions. All 6,050
function addresses, 61 owner neighbors and 189,088 protected data bytes remain
unchanged. Actual ELF SHA-256: `04f18ba2671cc76fec079473ae3944fbdeb71a216a04bb53f2f42fa1db47c8fd`. The existing complete-ROM
checksum mismatch remains.

Fresh actual ELF recount: **3,688 / 4,840 (76.20%)** Game and **4,361 /
5,513 (79.10%)** overall, zero drift. The Game 80% target needs 184 more
exact functions. Tools commit `d2c37f966bdbb56bd9d47a847311e9c79a99331b` precedes the consumer change.
