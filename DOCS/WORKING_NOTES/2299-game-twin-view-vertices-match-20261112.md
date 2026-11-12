# Two direct view-vertex callback matches

Date: 2026-11-12. `func_151AC810` in `generated_1D92F0.c` and
`func_151DAE28` in `game_2062D0.c` replace zero-return placeholders. Each
119-word retail body is identical and emits directly from semantic C with no
word guards or insertions.

Both request a four-vertex buffer for a signed view. A null result returns
null; a fresh buffer receives two copies of the actor template. The callbacks
compute width and height from the actor's scales and construct a view-facing
quad using the two per-view axis arrays, returning the original cursor. The
original `func_1513DB00` renderer dispatch window selects them through
`D_80089E1C` entries 11 and 14 respectively, and tests the returned pointer.
The complete renderer remains outside this qualification.

Each retail and candidate body passed 422 guest cases, with all 119 retail
words visited, covering null, fresh, repeated slot reads, helper mutation,
signed view and guest-only overlapping-memory cases. Connected checks run
the original copy and buffer helper bodies after verifying them against the
current ELF: all 11 copy words and 51 of 52 backend words were visited. The
remaining backend word is the fallback for a null fresh-byte pointer, while
these callbacks pass a non-null pointer. Native SDK32 O0/O2/O3 each pass 290
finite, valid disjoint cases and six effective negative controls per target
under UBSan. Each original dispatch window passes 422 cases with both null
and non-null branches. Guest exceptional casts and overlapping copies do not
establish portable C behavior; FCSR, full renderer and gameplay are not
qualified.

Both padders reproduce independently assembled retail bodies and relocations.
Per target, twelve GNU rebases and 471 bounded access-cut triples pass; these
are guest instruction-prefix checks, not native or hardware fault guarantees.
The combined actual Make and independent linked-image audit agree: 694 changed
bytes, no metadata groups or exclusions, all 6,050 function addresses fixed,
and all 189,088 protected Game-data bytes unchanged. Owner compilation
preserves 32 and 61 neighboring functions respectively. Actual ELF SHA-256:
`b86216171901db1cb156acdda4c1158be565e7f05f66f387c31554f3556c49d3`. The existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,696 / 4,840 (76.36%)** Game and **4,369 / 5,513
(79.25%)** overall, zero drift. The Game 80% target needs 176 more matches.
Tools commit `d980f21b4c6ec3f12a44d2e3475664b9288bbc1c` precedes this consumer change.
