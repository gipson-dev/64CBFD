# Six-record scene setup direct match

Date: 2026-11-12. `func_15010110` in `conker/src/game_3D5C0.c`
replaces a zero-return placeholder. Its 74-word retail body occupies VA
`0x15010110..0x15010238`, ROM `0x3D5C0..0x3D6E8`; two alignment words
follow. The function emits directly from C, with no guards or insertions.

The callback makes two setup calls using the current global values, then
copies each of six point-pair records from `D_800963A0`, assigns an index
from one through six, calculates the absolute vertical separation, and submits
the record. The original `func_1500E470` initialization window dispatches it
through `D_80082D90` entry 19 and ignores the callback return. The complete
parent initialization remains outside this qualification. The source uses a
local typed declaration for the six-record table; the shared variable header
still declares `D_800963A0` as a pointer and was not changed. The retail data
at that label contains the records themselves, not a stored pointer.

Guest execution of retail and candidate agreed with an independent model in
72 cases and visited all 74 retail words. The corpus includes helper changes
to the globals, later source records and the live record's flag. The original
dispatcher window passed those cases; helpers were modeled. Native SDK32
O0/O2/O3 with UBSan each passed 128 cases and eight effective negative
controls. Both padding paths reproduce independently assembled retail words
and relocation bindings. Twelve GNU rebased links and 369 bounded guest
access-cut triples passed. Those checks do not establish portable C fault
behavior, hardware behavior, the complete parent, or gameplay.

Actual Make and independent linked-image prediction agree: 233 changed bytes,
zero exclusions or symbol-metadata reorder groups, all 6,050 function
addresses fixed, and all 189,088 protected Game-data bytes unchanged. The
owner contains no other functions. Actual ELF SHA-256: `dd6ef3f4ce656fc0b58a8813ae1860901fdb757a1a5a33f4251b17d54ca25d2f`.
The existing complete-ROM checksum mismatch remains.

Fresh ELF recount: **3,699 / 4,840 (76.43%)** Game and **4,372 / 5,513
(79.30%)** overall, zero address drift. The Game 80% target needs 173 more
matches. Tools commit `0e3766636f9ea85e8618f4e4019d4832b74e8b96` precedes this consumer change.
