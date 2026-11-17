# Ground-linked oscillator private recovery and sequencing qualification - 2026-11-17

`func_151AADF8` is recovered privately as a ground-linked effect constructor
and existing-effect notifier. Its complete retail span is **166 words / 664
bytes**, VA **151AADF8..151AB090**, ROM **1D82A8..1D8540**, frame **0xC0**.
The production placeholder is still present: **no C is installed, no guards
are added, and this work earns zero byte-match credit**.

The accepted production remains **4,529 / 5,514 (82.14%)**, Game **3,856 /
4,841 (79.65%)**, zero drift, 985 different, **158 more matches to 85%**.
Root README is unchanged. Continue this function from the sequenced v42
candidate; v48 is a rejected native ordering control, not an adoption candidate.

## Recovered interface and behavior

The original callback table `D_8008AFD0`, slot 14 at **8008B008 / ROM22FAC8**,
selects this routine. Retail `func_15158D2C` dispatches the table through
`jalr` at **15158F60**, passes the selection/owner in a0 from s1, and discards
the result. This supports the private `void (u8 *owner)` callback interface.
The complete dispatcher is not executed by this suite, and its production
placeholder is not mistaken for a literal restored caller.

If owner+0x70 already points to an effect, the callback freshly reads that
pointer, adds 0xB0, sets the payload's notification byte +4 to one, and returns.
The attached actor comes from owner+0x18. Otherwise it builds a ground query:
X/Z from actor+0x14/+0x1C; Y is actor+0x118+100 when the height is above
`D_800A8FE0`, or actor+0x18+150 otherwise. The real threshold is **-9500**.
`func_15045800(position,0,positionY-300,owner+0x34)` must report a hit before
the callback requests a selector or consumes any random values.

After `func_151D8E20`, Y is freshly read from owner+0x34. The float generator
`func_150ADA68` determines the scale with separately rounded multiply/add:
`sample*30.0f+50.0f`. Coefficients `D_800A8FE4` and `D_800A8FE8` are read
after that provider; their retail bits are **46CCCCCD** and **3E6C8B44**
(approximately 26214.40039 and 0.2310000062).

The recovered 32-byte oscillator payload retains its owner, enabled byte,
base, 32768 range, zero target, zero remaining count, two 10 halfwords and rate.
Its **27 defined bytes** are checked. Five unwritten bytes at **+5,+6,+7,
+0x1A,+0x1B** are copied by memcpy but get no semantic/padding credit.

The descriptor's initialized prefix is 28 bytes: flags **0x60300**, duration
300, kind 0x38, zero word, truncated angle `32768*.5+base`, opacity150,
alpha255, three selector-indexed color bytes, alpha255, zero byte, mode6,
and flags **0x440001**. Byte +7 is unwritten, so **27 descriptor bytes** are
observed. Its existing 40-byte source view has a further untouched 12-byte tail.
The actual `D_800AB414` table has 13 three-byte colors and one following pad.
Native creation cases use valid indices 0..12; wider backed indices are
guest-only rather than a portable array-domain claim.

Three integer PRNG calls must occur in sequence. The first supplies its low
byte; the second supplies the low pair bit; the third supplies the high pair
bit. The factory receives
`func_1513C73C(descriptor,7,1,owner+0x38,x,y,z,scale,scale,first&255,
((third&1)<<1)+(second&1),32,255,1)`.
The returned effect pointer overwrites owner+0x70 after the factory returns,
including a null allocation result. A nonnull result receives all 32 payload
bytes at effect+0xB0 through the real memcpy ABI.

## Measured fitting state

All **71 complete source forms v0..v70** are retained privately. They compile
with the existing O2/g3 owner profile, preserve all 40 other owner functions
and normalized pools, and make no compiler/profile changes.

| Candidate | Words / frame | Current evidence and remaining fit |
| --- | --- | --- |
| v33 | 166 / 0xC0 | Correct length/frame; 73 word differences across all 166 positions. Explicit random sequencing passes native. Query, packet and descriptor addresses remain displaced by 12 bytes. |
| v42 | 165 / 0xC0 | Correct position A8, descriptor80, payload60, scale5C and selector5B homes. Explicit random sequencing passes native. The early return emits one fewer word; named random spills use50/54 rather than4C/50. Scheduling/FP/register differences remain. |
| v48 | 165 / 0xC0 | Original exposed homes and random spills, but nested PRNG argument evaluation changes order under GCC. Guest-only fit, rejected for source adoption. |

The raw position-by-position v42/v48 comparison is **146 differences over
165 paired positions, plus a missing word**. That is a shifted comparison,
not 146 independently justified scheduling guards. The retail early arm stores
the notification before its branch and reloads ra in the branch delay slot.
The 165-word forms move the byte store to that delay slot and share the ra
reload. Retain the original early-exit shape before judging later word offsets.
Descriptor initialization order and FP/register scheduling also need fitting;
this is not presented as a one-word complete match.

Selected raw SHA256s are pinned in the maintained private manifest:

- v33 `14d3a4ab5fbb493ba0b28edc232bca9e769dbff47d4bae37bd5c24b8f2cf175f`
- v42 `4dec087dfca51cb62d484617f6868d4f7e5b9eea93edcd92bbf1ef15fd668dec`
- v48 `8668d075b3ca784cf5f1ab7a9ebf95125505aa2e9f73ee1b6fac3369d567c169`
- retail `3d88584dae34894b92b32e118466c9fdc699aaafe7a6ac05eef7f067af4bff39`

## Fresh qualification and its limits

All **three maintained tests pass in both tools copies** at identical task
fingerprints. Primary takes 45.503s including input checks; sibling 46.342s.
Actual module import origins are recorded, not inferred from PYTHONPATH.

1. Compile complete baseline and three candidate owners with production SDK
   headers. Both real padders preserve raw bodies/bindings, all 40 neighbor
   bodies/addresses and normalized pools. The short bodies retain a 660-byte
   function extent plus a separate four-byte zero slot gap; they are not
   falsely reported as 664-byte functions. No new guards or insertions.
2. Independent guest model: **1,094 cases per retail/v33/v42/v48 stream**,
   all 256 byte selectors, existing/miss/factory-null/factory-success routes,
   two stack phases, threshold equality/NaN/infinity and helper mutations.
   The model compares complete initialized public memory and ordered calls,
   all defined descriptor/payload bytes, three draws and callee saves.
   Four deliberately broken instruction variants reject. Two compiler-duplicated
   delay-slot loads are unreachable; visited totals are164/164/163/163.
3. SDK32 execution: **608 cases each for v33 and v42 at O0/O2/O3** with strict
   aliasing enabled, UB traps and original field widths. Both candidates pass.
   Five broken C variants and the unsequenced v48 form compile and exit3 as
   expected; **all 12 executions have their expected outcome**. The native
   ordering counterexample prevents an IDO-only fit being called portable C.

The first fixture attempt wrongly equated function extent with reserved slot
size; the corrected assertion checks both separately. A native fixture also
quieted an unread signaling-NaN owner-height pattern during float conversion;
byte-preserving initialization/serialization fixed the fixture. These were
test-fixture defects, not production defects. Original failed receipts remain
separate; the passing primary/sibling `*-v2` receipts are authoritative.

Helper implementations are bounded services here. Full dispatcher/helper
execution, arbitrary public aliases, complete private-memory/register/FCSR
proof, relocation rebases and trap/gameplay behavior are still unqualified.
Passing guest/native public behavior does not satisfy those remaining gates.

## Retained baseline, commands and continuation

Consumer baseline **4674aed4**, tools **279443f**. All **1,442 frozen inputs**
remain unchanged, including source, old guards, all production objects, ELF
and conversion/progress data. ELF SHA256 stays
`88c9ce8da565409f3219a394f71fb01bb8958449207e7a067901e96338a98f19`.
The snapshot uses 1,433 immutable-snapshot links and 9 copies, with zero links
to live worktree files. Shared `make tools-check` also passes.

Prepared checkouts can rerun the focused suite with a **fresh** ignored output
path supplied in `CBFD_GROUND_LINK_PRIVATE_WORK`:
`python3 -m unittest tools.tests.test_game_ground_link_151aadf8_private -v`.
The manifest is intentionally pinned to the retained production checkpoint;
it fails closed after those source/tool inputs change. Private study, all
candidate forms and sealed receipts are in
`conker/build/game-next-151aadf8-private/`.

The sibling's 2,434 changed paths and 339 scoped dependency files remain
unchanged; tests use an isolated five-file overlay. The host path still has
only `.codex` and `recomp_scene`, with no host source checkout available.
No host/Release/save changes, Claude calls, dependency updates or push.
The native Graphify update refuses a smaller 26,867-node replacement and
retains all 64,053 existing nodes. A scoped AST merge adds the qualified
tools without removing old IDs; a full-corpus re-extraction is not claimed.
Tools are committed before docs/consumer pin.

Continue in this order:

1. Use the explicitly sequenced **v42** to recover the retail early-return
   duplicate ra load and original random spill homes. Keep v48 as a negative
   ordering control. Fit the descriptor/FP schedule using the pinned candidates.
2. Qualify the complete private state, ordered FP/FCSR and alias epochs; then
   audit the real callback dispatcher/providers and independent relocation
   layouts. Decide any minimal expected-word guards only from that proof.
3. Run shadow Make and strict full-image prediction before installing. After
   installation run actual Make, complete image/protected-data/neighbor audit,
   installed focused checks and a real recount. Only then grant matching credit,
   update aggregate README rows, refresh the graph and commit tools first.

The full 85% goal remains active.
