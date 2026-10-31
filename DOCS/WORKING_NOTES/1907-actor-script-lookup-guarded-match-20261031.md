# Actor script lookup restored from guarded C

Date: 2026-10-31. Target `func_1507BB28`, owner `conker/src/game_A28B0.c`.
Original assembly: `conker/asm/nonmatchings/game_A28B0/func_1507BB28.s`.
VA `0x1507BB28..0x1507BC14`, ROM `0xA8FD8..0xA90C4`.

## Recovered interface and lookup

`s32 func_1507BB28(s32 unused, s32 id)` returns a 32-bit script address handle,
preserving the existing caller interface and all returned pointer bits. The
first argument is ignored but homed at incoming SP+0; the complete second
argument participates in comparisons. It must not be narrowed to a byte.
The routine is a leaf with a zero-byte frame and no saved-register writes.

The actor selector is the unsigned byte at `D_800D154C->id` (+4). Its entry in
`D_800D1588` points to a resource with a script-table pointer at resource-0x10.
Missing resource or missing table returns `D_8009A120`. Table entries are eight
bytes: a script pointer at +0, ID byte at +4, and three uninterpreted bytes.

The search tests the ID before the pointer. A matching entry returns its
pointer, including NULL. A nonmatching NULL primary entry switches to
`D_80086A88`; a nonmatching NULL global entry deliberately spins forever.
No replacement default, range clamp or missing-ID recovery was invented.

The original global table has three entries: IDs 1 and 250 both point to
`D_8009A120`; its NULL terminator has ID 0. A matching request for zero returns
NULL before checking the terminator pointer. Original bytes verify the first
five-byte script record: opcode 0x67 with arguments 0x14,0x0F,0x19,0.
Shared headers, other caller declarations and script record layouts are unchanged.

## Compiler layout and checked normalization

The full semantic C body emits 58 words under O2/g3, MIPS2/O32. Fourteen
expected-word rows restore the complete 59-word retail slot, with one insertion
and no omissions or alignment words. The rows cover a closed fallback-address
materialization, its T2/T3 allocation choice, independent cursor/index updates,
and branch offsets around the additional word. The added HI16/LO16 pair remains
bound by name to `D_80086A88`, and independent rebases are qualified.

This is a guarded C match. The raw C result is tested independently, and the
complete normalized result is compared with the original retail routine.
Twenty-eight actual-padder negative controls reject altered expected words or
relocation preimages. The inherited guard manifest remains a byte-identical
prefix; exactly 14 new rows apply to this function and owner only.

Raw compiler SHA-256:
`6e6708dc9aa34dde6b6553b7c229d306a9faed37073c4dc7a64f75f19b191485`.
Normalized unlinked body SHA-256:
`0977e9c81a7e04675f954fca850a53b6c44ab7ef68edaf36d126cf62816f8197`.
There are ten raw and twelve normalized named relocation bindings.

## Qualification

| Check | Measured evidence |
| --- | --- |
| Complete owner | All 210 neighbors and constant pools unchanged |
| Actual Make | Five commands reproduce the qualified object; all 14 inherited warnings unchanged after path/line normalization |
| Guest | 3,312 cases; 13,248 normalized executions plus 3,312 raw-C executions |
| Code/data rebases | Three independent layouts |
| Coverage | 55/59 retail words; four unreachable duplicate loads at +0x34,+0x4C,+0xA0,+0xC4 |
| Order/aliases | Six incoming-home aliases; 56 access-prefix cases, including 23 delay-slot cuts |
| Missing-ID behavior | 308 bounded spin cases; one original spin iteration is observed before stopping |
| Native32 | 382,976 cases each at O0/O2/O3; UBSan trapping; seven effective controls |
| Native domain | All 187 declared actor-resource slots, all 256 byte IDs and eight table outcomes; unused-argument bits and periodic table preservation checks |
| Original global data | Twelve cases, including IDs 1/250, NULL ID0 and bounded misses; four original five-byte script prefixes checked |
| Original callers | All 25 aligned JAL sites inventoried; four actual return-consumer windows, 256 cases / 1,024 normalized plus 256 raw-C executions |
| Canonical checks | Eight fresh methods in each tools copy; both shared tools checks pass |
| Installed checks | Two fresh methods per copy; six unchanged checks reused only under full input/module/artifact fingerprint equality |

The caller windows store the complete returned address at actor+0x218, clear
script timers, and prove the five-byte backup used by a script command caller.
They include a real nonzero ignored first argument. The aligned retail census
finds no literal function pointers. Full parent functions and gameplay are not
claimed. Guest byte-selector edges include 255 under explicitly mapped memory;
the native C array domain is its declared 187 slots. Guest spin/access-prefix
results are bounded machine behavior, not portable C fault or unbounded-run claims.

Native controls detect a wrong actor slot, wrong resource-prefix offset, wrong
default address, premature primary fallback, wrong primary/global indices and
an ignored first argument incorrectly affecting the ID. Each control exits
through a semantic mismatch rather than a timeout or memory trap.

## Image, adoption and banking

The independent complete-image prediction has zero exclusions and exactly
181 changed bytes: 180 target code bytes and one function-size byte. There are
no metadata changes. All other 6,055 function bodies and all function addresses
remain fixed. Protected Game data is exact: 189,088 bytes across 720 owners.

Production preserves the unchanged frozen sinf/debugger auxiliary objects by
full-input fingerprints while rebuilding the target owner and complete ELF.
Their source inputs and object bytes are verified, not excluded from the audit.
The adopted Native ELF is recounted through a captured-byte bridge; the existing
C inventory is unchanged. Existing Git CSV normalization is retained; parsed
committed rows agree with the qualified manifest while the working input keeps
its exact inherited prefix.

Adopted ELF SHA-256:
`f10c39b4ba7cb66faef1adf33b9434544aae4ceca059a4e580718b583fed85d9`.
Tools commit: `14718f0f32ea641d8bd29c8aacf72106891353da`, banked before the consumer source/CSV/pin/documents.
Primary tools and consumer are clean after banking. The old tools mirror's
2,159 inherited dirty paths are preserved, with three additional qualified
modules; that mirror is not committed. No push is authorized.

Accepted total **3,984 / 5,506 (72.36%)**; Game **3,311 / 4,833 (68.51%)**;
Init 492/492 and Debugger 181/181; zero drift and 1,522 still different.
The 75% threshold remains 4,130, requiring **146** further matches.
Next queued screen: `func_1500707C`; the full goal remains active.

Artifacts and handoff: `conker/build/game-script-entry-lookup-1507BB28-match/`.
Canonical modules: `tools/experiments/game_script_entry_lookup_match.py`,
`tools/tests/game_script_entry_lookup_oracle.py`, and
`tools/tests/test_game_script_entry_lookup_match.py`.
Historical reproduction requires the frozen target inputs and retained build
artifacts, rather than a later mutable global build.
