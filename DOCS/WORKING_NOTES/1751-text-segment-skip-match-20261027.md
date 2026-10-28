# 1751 - Text segment cursor direct C match

Verified: 2026-10-27. Target `func_1516C878`, owner `generated_197C20`.
VA `1516C878..1516C934`; retail ROM `199D28..199DE4`.

## Result and recovered interface

Replace the zero-return placeholder with the complete 47-word /188-byte routine.
Every word emits directly under normal O2/g3: frame 8, four HI16/LO16 bindings,
zero guards. Preserve all 11 neighbors, pools and all 12 compact owner functions.
The existing three-command IDO/padder/assembler Make recipe reproduces the object.

The recovered interface is `u8 *(TextSegmentSource *, s32 segment, s16 bank)`.
`TextSegmentSource` describes only the measured eight-byte record prefix:
flags at +0 and a word at +4 that is either an unsigned table index or text
pointer. `TextBankEntry` describes an eight-byte table entry with its text
pointer at +0 and an untouched reserved word at +4. Shared headers/types do
not change.

Bank 0 selects `D_800DD254[index].text`; bank 1 selects `D_800DD258[index].text`;
bank 2 takes the direct pointer in the record. The selector is narrowed to
signed 16 bits while its full incoming word is saved at incoming SP+8. After
selection, a nonpositive segment returns the pointer without reading text.
Each positive iteration scans the current nonzero run, skips the complete
zero run and returns at the next nonzero byte. Leading zero bytes are skipped
as one transition; consecutive separator bytes do not create extra transitions.
Use unsigned byte loads and signed full-word segment comparisons.

Declare the counter before the cursor to retain the original cursor home at
frame+0. The initial reversed local order matched all other words but loaded
an unsupported-selector cursor from frame+4. No forced register binding or
instruction patch is needed. One redundant direct-pointer load at offset 104
is unreachable; all 47 words are checked literally and all 46 reachable words
are covered dynamically.

Retail leaves the cursor unset for other selectors, loading its prior stack
word. Preserve that original shape. Unsupported selectors and aliases that
produce invalid pointers are qualified only as emitted guest behavior. Native
checks use banks 0/1/2 and valid terminated buffers; no portable C guarantee for
an indeterminate cursor or malformed text is claimed.

## Actual callers and return consumers

The aligned whole-ROM census finds three direct JALs at ROM 197DBC, 197EA8 and
1985CC (VA 1516A90C, 1516A9F8 and 1516B11C), with no pointer literal or tail J.
They belong to `func_1516A7B0` and `func_1516AA70`, whose C bodies remain
placeholders. Each supplies a byte selector from state+0xD. One result becomes
the next helper's A0; the others are stored at state+0x24.

Seventy-two cases execute the authentic 5-, 3- and 15-word call windows, including
argument setup where present, real delay-slot writes, return forwarding and
pointer stores. Preserve the containing parents as uncredited; these windows
are not complete parent or text-rendering acceptance.

## Fresh qualification and bounded reuse

Both tools copies pass eight fresh canonical methods plus shared tools checks.
After production installation, each copy runs the owner/image checks fresh and
reuses six semantic receipts only after module/input/artifact identity.

- 7,344 guest cases cover all low selector bytes plus high-word noise, signed
  selector boundaries, nonpositive and positive segments, full-word wrapped
  table indices, two stack phases, leading/consecutive zeros and five aliases.
  Twenty invalid direct-pointer/home alias cases compare natural fault state.
  Compare complete private state and access traces between original and rebuilt.
- Native32 O0/O2/O3 with trapping UBSan pass 1,344 positive cases per profile
  and eight effective C controls. Use the unchanged body as always-inline
  functions called with constant valid selectors, keeping unsupported cursor
  behavior outside the native contract. No default initialization, warning
  suppression or sanitizer removal is introduced.
- Seventy-six fired fault-prefix pairs verify PC/delay ownership and state.
  Sparse mappings prove that nonpositive segments need no text bytes, while
  unsupported selectors need no source-record or bank-global mapping. These
  are guest instruction observations, not portable C fault or MMU claims.
- Six GNU links over three layouts, including signed-low address carries,
  preserve both HI16/LO16 pairs and pass 18 guest cases. Three raw controls
  reject truncation, changed bindings and a changed unreachable word.
- An actual compiled s32-selector mutant fails the low16-bank 2 return case.
  Ten full-image corruptions and three wrong-input controls fail closed.

The first native reference used a postdecrement on INT_MIN and trapped before
the target ran; it now tests positivity before decrementing. Invalid aliased
direct pointers are now tested as faults instead of pretending they have
backing text. Failed v1 receipts are archived. Production C/artifacts did not
change. Routine Claude calls: zero.

## Closed metadata cycle and production image

The first slot/size-only ELF prediction was rejected: 59 other bytes changed.
Inspection identifies exactly one closed symbol and string ordering cycle:

| Prior order | Resulting order |
| --- | --- |
| D_800DD258 | func_1503F404 |
| func_1503F404 | func_151BBEE4 |
| func_151BBEE4 | D_800DD258 |

Predict the new order from the frozen named records and their literal names.
Require contiguous predecessor records/strings, the exact original addresses,
sizes, binding/type/section fields and equal total string length. All named
definitions remain fixed except the target's size 12->188. No symbol or string
section is excluded, and no candidate bytes are copied into the predictor.

Normal production Make reproduces the independent full image: 136 changed code
bytes plus 60 metadata bytes (59 cycle bytes and one target-size byte), 196 total,
zero exclusions. All 6,056 function addresses and 6,055 other bodies remain fixed.
Protected Game data is exact: 720 owners /189,088 bytes. The inherited duplicate
12D630 recipe warning remains the only build warning. Inventory and the whole
guard CSV are unchanged.

Native guard CSV SHA-256:
`bc18bdc4633b2387568bc04ee6f816ede14290f391446f745a97b44027eecc59`.
ELF SHA-256:
`b0e7761ede773cb12b033885cf6e7f1df84e7481a13403bb589d4f5ec3c47475`.
Native/cache audit: 16,182 sealed inputs and 146 focused inputs, with only
qualified source/object/ELF/map overrides. Recount the captured adopted Native
ELF with its unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,829 /5,506 (69.54%) | 1,677 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,156 /4,833 (65.30%) | 1,677 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_1516C878` becomes exact. Conversion totals remain fixed. The 75%
threshold is 4,130, requiring 301 more matches. Remaining source screens are
1,548 placeholders, 120 semantic/other definitions and nine unlocated entries;
these shapes are not qualification.

## Banking and next target

Predecessor consumer `bc9cad661ed01ba719803970f95d8395969e4a63` and tools
`995b06ec87046aeb17f571d3f0cf622288348f8e`. Bank qualified tools first at
`d6359407c83911a42f902ddfab81e43ee2e01bec`, then source, consumer pin and
measured docs. Preserve 1,712 inherited dirty paths plus two new tools files
in the older mirror; do not commit its independent history. No push.
README changes only its two aggregate matching rows.

Refresh ten changed graph sources, accounting for the pointer return and
preserving all still-valid prior relationships. Keep outside manifest rows
and historical communities historical; no full-corpus extraction, global
clustering or centrality claim. Final graph and independent audit receipts
are in `conker/build/game-text-segment-skip-match/`, alongside the rejected
first prediction, qualified artifacts, tests, production and recount evidence.

Next inspect `func_151D324C` in `game_1FFF60` (47 words), starting with its
actual owner profile/assembly route, callers and a fresh frozen predecessor.
Keep `func_1514E920` parked and uncredited. The 75% goal remains active.
