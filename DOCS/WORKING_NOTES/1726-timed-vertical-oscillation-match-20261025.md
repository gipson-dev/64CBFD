# Timed Vertical Oscillation Direct C Match

Date: 2026-10-25

`func_151D3D50` replaces its zero-return placeholder with complete semantic C.
All **45 words / 180 bytes**, frame **32**, and **six bindings** emit directly
from C, without guards or an alignment tail. Only this routine receives new
matching credit. The actual adopted Native-ELF recount is **3,802 / 5,505
(69.06%)**, leaving **327 more matches** to the 75% threshold.

## Source And ABI

Owner `generated_200930`, source `conker/src/game/generated_200930.c`, original
assembly `conker/asm/200930.s`. VA `0x151D3D50..0x151D3E04`, VROM
`0x201200..0x2012B4`. The single input is an actor pointer; the result is always
the signed word one. Local partial views describe only the observed fields:

- Position vector at `0x20`, base vector at `0x50`.
- Signed halfword remaining time at `0x170`, preserved halfword at `0x172`.
- Float phase/rate/amplitude at `0x174`/`0x178`/`0x17C`.

For positive remaining time, add rate times `D_800BE9A4` to phase and store it
before calling the angle wrapper. Store the returned phase in the sine call's
delay slot. Compute position Y from sine times the late amplitude plus late
base Y. Reload both remaining time and word tick `D_800BE9E4`, subtract and
store the low halfword. For nonpositive time, copy all three base words to the
position vector without float arithmetic. Preserve all other bytes.

Both math helpers have `f32(f32)` prototypes, retaining the O32 F12/F0 ABI.
No shared-header, compiler-profile, guard-manifest or neighboring-body changes.
There is no inline assembly or physical-register binding in the recovered C.
Retail retains an unreachable duplicate load at **+136** after an unconditional
branch. It remains byte-exact; all **44 reachable words** execute in the tests.

## Qualification And Limits

Canonical primary/mirror modules pass **eight fresh checks each** before
installation: **73.255 / 56.780 seconds**, zero failures/errors/skips/reuses.
Shared project-tool checks pass in **0.309 / 0.261 seconds**. Both installed
copies then pass all eight fresh checks again in **78.854 / 76.354 seconds**;
none of those installed checks are counted as reused evidence.

- **716 cases / 1,432 guest phases**, including **320 global-alias phases**:
  signed timer edges, late helper mutations, untouched bytes, full modeled
  GPR/FPR/HI/LO/RAM/events, helper observations and both stack phases agree.
- Native32 with actual SDK types: **496 cases per O0/O2/O3 profile**, separate
  float32 operations, trap UBSan, exact field offsets/extent and byte fences.
  All **ten compiled semantic negatives** exit 23. Active Native math excludes
  nonfinite operands and oversized signed subtraction; guest cases retain the
  full-word tick edges and deliberate aliases. Inactive Native bit copies
  include infinity and NaN payloads. Guest aliases/faults are not portable C
  alias or fault guarantees. Only the Native harness uses stack realignment.
- Complete original sine **104 words** and wrap **24 words** are independently
  GNU assembled, locked to retail and connected in **144 phases**. All 24 wrap
  words execute. Huge/infinite wrap completion, FCSR and hardware parity are
  not established by these bounded models.
- **Nine independent GNU links / 48 rebased phases** cover all six bindings
  and signed-low HI/LO carries. **188 fired target-access fault prefixes** agree
  in complete modeled state and actual dispatched instruction context.
- All **45 raw-word** and **six binding** corruptions reject, together with
  **seven strict-image negatives** and **twelve live/frozen input mutations**.
  A valid installed input map passes; a stale predecessor object rejects.

The complete aligned prepared-ROM scan finds no direct target JAL and one
aligned target literal, VROM `0x22E3A0`: slot **12** of the real **25-entry**
`D_800898B0` table. Arbitrary computed references are not excluded by that scan.
The complete **119-word** original `func_151321D0` caller is independently
assembled and locked. **864 connected phases** test its real return gate,
timer behavior and target dispatch while fencing unrelated providers, alpha/
animation and geometry paths. The prior target stub demonstrably triggers an
incorrect release. The production caller remains its twelve-byte placeholder
and receives no credit. These paths do not cover all caller words or establish
full provider, heap, gameplay or hardware acceptance.

## Owner, Build And Exact Image

All **27 raw and padded neighbors**, their bindings, extents, pools and
addresses remain fixed, including the existing GLOBAL_ASM routines. The actual
five-command recipe runs preprocessing, normal O2/g3 IDO, GLOBAL_ASM
postprocessing, the ordinary padder and GNU assembly. It reproduces the
qualified owner. Compiler diagnostics are unchanged and the isolated compile
has none; the inherited duplicate-generated_12D630 Make warning remains.

The independent complete-image prediction changes exactly **143 bytes**:
**142 code bytes** and **one target symbol-size byte** (12 to 180). There are
**zero metadata exclusions or symbol/string permutations**. Actual production
Make exits zero in **4.413 seconds** and reproduces that entire image.
All **6,055 function addresses** and the other **6,054 bodies** remain fixed.
All **720 protected Game-data owners / 189,088 bytes** stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Tools commit `ca1a655b24080c1d16386c4f0b2bb9b3be6dc2dc` precedes the consumer
source/docs/pin. Baseline consumer is
`14dbe7a56f08b20fed2be4ddbfa3c7f8fffc2662`; baseline tools are
`8ad2cea49aaa283e232f3f3ddf5aa975da370405`. Capture verifies all **16,066**
adopted Native inputs, normalizes the prior three overrides, and then seals
exactly four new primary/mirror module files, **16,070** total. The older
mirror's **1,662 pre-existing dirty paths** and HEAD are preserved, plus the
two owned additions; no mirror commit, reset or stash.

Native adoption verifies every sealed file before and after copying. Exactly
the target source, owner object and linked ELF differ from the sealed baseline.
Guard CSV SHA-256 remains
`876afb871a1a6c41916b69b192d8b9fc786b688ad91a2381bfdcd9a698814d3b`.
The recount streams the actual adopted Windows ELF to the verified Linux
cache, without reading the project through DrvFS.

| Section | Exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,802 / 5,505 (69.06%) | 0 | 1,703 |
| Game | 3,129 / 4,832 (64.76%) | 0 | 1,703 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Only `func_151D3D50` leaves the prior queue. The unresolved pointer/NULL factory
retains its explicit placeholder classification. Queue source shapes are now
1,574 placeholders, 120 semantic/other definitions and nine unlocated entries.
Threshold `ceil(0.75 * 5,505)` remains **4,129**, requiring **327 more**.
Adopted ELF SHA-256:
`7686274a83dae9636fc1230508a775d372ee739c17b3024e436c1f3d9593f442`.

## Handoff

Private screening originally exposed two fixture defects: the Native SDK
include needed `_LANGUAGE_C`, and the original caller's skip-geometry flag is
bit 19. Their corrections do not change the C body; failed producer logs and
receipts stay separate. The canonical modules then receive the complete fresh
checks above. Private-only results are not reused as canonical suite results.

A read-only Native Git probe verifies that the installed direct executable
and its wrapper have identical version, HEAD and effective configuration.
The direct entry point reduces read overhead; subsequent read checks use its
verified executable fingerprint. Commit/staging still use the established
wrapper. No system/repository configuration or dependency changes.

Next ordinary placeholder is **`func_15013000`**, owner `game_40490`, 45 words.
Its private indexed form remains **23 words different**. The old header calls
`D_800D3098` a 73-record `struct178` array, whereas retail loads its first word
as the scan base. Resolve that storage/ABI boundary before installing a typed
body or changing shared declarations. Later `func_150228E4` also remains a
nonmatching private screen. Neither receives new credit.

Receipts live in ignored `conker/build/game-vertical-bob-match/`; earlier
private qualification remains in `game-vertical-bob-private/`. After the
consumer commit, refresh exactly the eight changed C/Markdown files through
the supported incremental merge API and verify retention of all **44,231**
prior nodes, current file fingerprints and the actual commit marker. Index
the new tools separately; no full-corpus freshness claim. Claude calls zero.
No host/editor/Release, global configuration or dependency changes. Nothing
is pushed. The wider 75% goal remains active.
