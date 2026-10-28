# 1754 - Phase-cycle spawn direct C match

Verified: 2026-10-27. Target `func_150D2110`, owner `generated_FF5C0`.
VA `150D2110..150D21CC`; retail ROM `FF5C0..FF67C`.

## Recovered routine and state

Replace the zero-return placeholder with complete semantic C. All 47 words /
188 bytes emit directly under normal O2/g3: frame 0x50, four bindings, zero
guards and no diagnostics. Preserve all six neighbors, pools and all seven
compact functions. The actual three-command Make recipe reproduces the object.

The recovered interface is
`void(s16 lifetime, f32 activeDuration, f32 inactiveDuration, u8 activeColor, u8 inactiveColor, u8 priority, s32 owner)`.
The original caller ignores the physical return. Its integer first argument
places both float bit patterns in A1/A2 under the O32 soft-float interface.
The full first word and fourth word retain their incoming stack homes; the
lifetime narrows to signed 16 bits and the three byte values narrow to eight.

Increment `D_800D9900` as a byte before attempting allocation, including on
failure. Construct a local 24-byte phase-cycle state. Extend the existing local
`PhaseCycle` prefix with its measured color bytes and name the previously
unused duration field `inactiveDuration`; the existing update routine retains
its exact instructions. No shared header changes are needed.

| Packet offset | Meaning / value |
| --- | --- |
| +0 | active byte, zero |
| +1..3 | original uninitialized bytes |
| +4 | phase, +0.0f |
| +8 | active-duration threshold |
| +12 | inactive duration |
| +16 | single-precision sum / period |
| +20 | active color byte |
| +21 | inactive color byte |
| +22..23 | original trailing padding |

The state lives at frame+0x38. Keep the counter increment first, followed by
the threshold, inactive duration, sum, active byte, phase and colors. This
recovers the original register and independent-store schedule. Sixteen bounded
source-order screens found the direct match; the first complete C had the
correct 47-word length but twelve scheduling/register differences. No forced
register binding or instruction patch is used.

Call `func_15149130` with the narrowed lifetime, -1, 0x2F, 2, 1, 0x26,
payload size 24, priority and owner. On success, copy all 24 bytes to object
+0x28; on null, make no copy. The local constructor declaration describes the
measured size argument as a word. The retained helper's older shared pointer
spelling and its implementation remain unchanged; the physical argument and
size+0x28 behavior are checked against original instructions.

Do not zero-initialize the state. Retail copies five seeded stack/padding
bytes as well as its defined fields. Guest checks qualify those exact bytes;
native checks qualify the defined fields and disjoint copies without making
an ISO C padding-value or overlapping-memcpy guarantee.

## Original caller and helper boundaries

The whole aligned-ROM census finds one JAL at ROM FF8A8, VA 150D23F8, in
`func_150D2374`, with no target pointer or tail J. Four cases execute the
actual 17-word window `150D23BC..150D2400`, including float-word loads,
byte/word homes, signed-halfword lifetime setup, and the call delay store.
The next caller instruction overwrites V0 through the RNG call. The containing
parent's C placeholder remains uncredited; no full parent/RNG claim is made.

The original and retained constructor match all 49 words; original and retained
`memcpy` match all 11. Four success/failure and counter-boundary integrations
execute those complete routines with bounded allocator and bzero providers.
They verify allocator arguments `(35, owner, 64, 1, priority, 1)`, actual
header stores, sixteen zeroed header bytes, and the complete packet copy.
This is scoped helper integration, not full allocator or gameplay acceptance.

## Qualification and controls

Both tools copies pass eight fresh canonical methods and shared tools checks.
After production, each runs two fresh installed owner/image methods and reuses
six semantic checks only after module/input/artifact identity.

- 7,744 guest cases cover all byte counter/argument values, signed lifetimes,
  high-word argument garbage, both allocation results, two stack phases,
  finite/subnormal/infinite/NaN float patterns and complete packet snapshots.
  Four destinations and three GNU-relocated counter layouts test self/forward
  guest copy behavior, counter aliases, provider mutations and late homes.
  All 47 instruction words are dynamically exercised. Full private GPR/FPR/
  RAM/events/visits and ordered access traces agree.
- Native32 O0/O2/O3 with trapping UBSan pass 65,536 positive cases per profile
  and eight effective controls. Valid typed providers check the constructor
  arguments, count timing, packet fields, exact copy size, null suppression
  and untouched bytes outside the destination. Padding values and guest-only
  aliases are excluded; floating checks do not claim MIPS FCSR/hardware parity.
- 154 fired access-prefix pairs verify complete private state, trace and PC/
  delay ownership. A null-allocation mapping needs no destination or copy.
- Three dedicated GNU layouts pass 18 rebase cases, including all four
  relocations and signed-low carries; alias links are additional. Three raw
  corruption controls and six whole-image corruptions fail closed.
- A compiled `PhaseCycle cycle = {0}` mutant is rejected because it changes
  the copied bytes. IDO places its constant initializer template in .data;
  the first fixture lacked this mapping and a second mapped only .rodata.
  The corrected test maps the actual emitted .data/.rodata template and
  reaches a result mismatch. Failed receipts are retained; production C
  remains unchanged throughout those fixture corrections.

Routine Claude calls: zero.

## Production, progress and banking

Actual production Make reproduces the independent whole-image prediction:
139 changed code bytes plus one function-size byte, 140 total, zero exclusions.
Only the target extent changes 12->188; all other named definitions, all 6,056
function addresses and 6,055 other bodies remain fixed. Protected Game data is
exact across 720 owners /189,088 bytes. No metadata cycle is introduced.
Inventory, guards, shared headers and retained helper objects remain unchanged.
The inherited duplicate generated_12D630 recipe remains the only build warning.

ELF SHA-256:
`d5fed435898d94afaa98740783d38a4c2bc04c93612e540cd2d9712488dada7a`.
Unchanged Native CRLF guard SHA-256:
`f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40`.
The audit seals 16,197 Native/cache inputs and 180 focused inputs. Recount the
captured adopted Native ELF against its unchanged C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,832 /5,506 (69.60%) | 1,674 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,159 /4,833 (65.36%) | 1,674 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only `func_150D2110` becomes exact. Converted totals stay fixed. The threshold
is 4,130, leaving 298 matches to 75%. Remaining source screens contain 1,545
placeholders, 120 semantic/other definitions and nine unlocated entries.

Predecessor consumer `6f13ada9728a77240517053aa62c4892625a9840` and tools
`98c3fb3d0dd30b71a4b3748a5c20ffc1e3ea4dfc`. Bank tools first at
`9c51017daf06d0cd156a4f1556dbd2dd2566d231`, then source, consumer pin and
measured documentation. Preserve the old mirror's 1,718 inherited dirty paths
plus two new tools files without committing its independent history. No push.
The root README changes only its two aggregate matching rows.

Refresh ten changed C/Markdown/tool sources with Graphify, retain every old node
and still-valid relationship/context, and retire only the obsolete placeholder
s32 return against both declarations. Verify the recovered parameter/helper
contexts against source and compiler relocations. Outside freshness and
communities remain historical; no full-corpus extraction or global clustering/
centrality claim. All receipts and the independent final audit remain under
`conker/build/game-phase-cycle-spawn-match/`.

Next inspect `func_15159370` in `generated_185560` with a new frozen predecessor
and caller/ABI review. Keep `func_1514E920` private and uncredited. The 75% goal
remains active.
