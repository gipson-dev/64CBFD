# Actor colored-effect dispatcher direct match

Date: 2026-11-12. `func_151026BC` in `conker/src/game/generated_12DAB0.c`
replaces a zero-return placeholder. Its 75 retail words occupy VA
`0x151026BC..0x151027E8`, ROM `0x12FB6C..0x12FC98`. All instructions emit
directly from semantic C with no word guards.

For a null actor the routine returns zero. Otherwise it selects one of the
color pairs (50,255) or (255,0) based on actor ID, falling back to the
attached object's byte at `0x78` for other IDs. It forwards the actor, two
indexed vectors, a byte-table entry, a signed halfword, the selected pair,
four floats and the remaining parameters to `func_15100600`. That helper
remains a zero-return placeholder: the target's exact instructions do not
imply that its complete effect is implemented in the current build.

The original 41-entry switch table remains at `jtbl_800A2298_game`. The
function-only `-Wo,-no_const_in_reg` compiler profile retains both retail
float-constant loads; the ordinary profile continues to supply all 22 owner
neighbors. A primary-build preprocessor branch preserves the existing helper
stub and its code, while the target compilation uses the observed typed o32
call. The matching caller declaration uses `int` for the four promoted narrow
parameters and `s32` for the last word: this distinction matters because the
SDK defines `s32` as `long`. All 40 functions in that caller's owner remain
unchanged.

Each original vector table contains seven rows. The existing callers pass
modes 3, 4, 5 or 6; the retail routine itself does not check the low byte of
its mode. Out-of-range modes are characterized in guest tests, but indexing
beyond those C arrays is not claimed to have defined portable behavior. The
two original caller windows are covered, not their complete parent functions.

Guest tests cover 4,100 cases per body and visit 74 of 75 original words;
the other load at `0x151026E0` is unreachable through the original null and
non-null branches. Native SDK32 O0/O2/O3 with trapping UBSan each cover 7,168
valid-row cases and 15 effective controls. The original caller windows pass
132 and 44 cases. Both padders, all 41 table entries, 42 table-corruption
controls, 12 GNU rebased links and 109 guest access-cut pairs pass. The helper
is modeled; guest fault cuts do not establish native fault semantics or
hardware/gameplay acceptance.

The actual seven-command Make paths and strict independent linked-image
prediction agree: 344 changed ELF bytes, zero exclusions,
all 6,050 function addresses fixed, and all 189,088 protected Game-data bytes
unchanged. Actual ELF SHA-256: `bf74c47dea47efbd05e0842c566b83e17922c5398a5bba32ba79d0f913ac185f`. The existing whole-ROM
checksum mismatch remains. Make also reports an intentional recipe-override
warning for this target in addition to the pre-existing `generated_12D630`
warning; the selected seven-command recipe is verified above. The target warning was subsequently removed in [Note 2306](2306-colored-dispatch-make-warning-fix-20261112.md).

Fresh ELF recount: **3,703 / 4,840 (76.51%)** Game and **4,376 / 5,513
(79.38%)** overall, zero address drift. The Game 80% target needs 169 more
matches. Tools commit `64f93ee5c79c4522a167ad842b0abece0cb853bd` precedes this consumer change.
