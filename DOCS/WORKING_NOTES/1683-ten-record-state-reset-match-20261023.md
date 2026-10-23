# Ten-Record State Reset Match

Date: 2026-10-23. Consumer baseline
`7c919d4eee0933c4f4cdb65ba436897a2321cb43`; tools baseline
`31e7a37f20ba7e6ce8380fa23cd05625b628f532`.

## Result

Recover `func_150A00F0`, VA `150A00F0..150A019C`, ROM
`CD5A0..CD64C`, in `conker/src/game/generated_CD5A0.c`.
The complete 43-word routine has frame zero and seventeen relocations.
It matches from a complete 46-word semantic C loop with twenty checked
normalization rows, including three omitted redundant high-address loads.
This is guarded semantic C, not compiler-only output; no word is inserted.
Retain the original assembly, existing local record type and all four owner
neighbors. Keep the adjacent `func_150A019C` placeholder unconverted.

## Interface And Fields

The actual interface is `void func_150A00F0(void)`. The routine consumes no
incoming argument, writes no argument home and does not define a C return.
Add that exact local prototype to `conker/src/game_44C40.c`; keep shared
headers and unrelated declarations unchanged.

`D_800D3010` names ten twelve-byte records, ending at `D_800D3088`.
For each record, preserve status bits 0..6 and the three padding bytes;
clear status bit 7 and the complete words at +4 and +8. Retain the existing
`GeneratedCD5A0Record` type and field names used by its other functions.
The source comment describes the active-bit and counter reset. An explicit
sixteen-bit mask preserves the original ANDI shape without a hoisted mask
register. Retail peels two records, then processes the remaining eight in
two four-record loop iterations, with the last word clear in a branch delay
slot. Preserve that complete emitted behavior rather than the old zero return.

## Compiler Normalization

Raw semantic C SHA-256:
`987d077d095b9342bb7e2bb3e8802539659266bdae9af7fa95b454a2b69972f4`.

Use this closed output-to-source word schedule for the opening nineteen
words, followed by unchanged source words 22..45:

```text
0, 1, 6, 7, 4, 5, 8, 9, 3, 10, 12, 18, 13, 14, 15, 16, 20, 19, 21
```

Omit source words 2, 11 and 17, offsets +0x08/+0x2C/+0x44. Each must be the
checked `LUI AT` with its expected record-array relocation. Every other raw
instruction occurs exactly once. Recover named field aliases at offsets
0/4/8/12/16/20/24/120; remove their corresponding C-array relocation addends
when introducing the aliases. All seventeen normalized relocations and
all words agree with an independently assembled original routine.

The first private crossing-boundary probe rejected an incomplete hypothesis
that kept every relocation under `D_800D3010`. GNU HI16/LO16 pairing then
associated different field addends incorrectly. Recovering the actual named
aliases closes that failure. Test original, guarded and actual-Make objects
at three independent code/data placements, including a low-half carry across
the record window. Preserve retail's high-half-sharing constraints for field
pairs 0/4, 8/12 and 16/20; reject incompatible layouts explicitly. These are
fixed-array aliases, not arbitrarily independent globals.

The guard file preserves its entire old byte prefix. All twenty rows are
scoped to this function/owner and check raw words and relocation lists.
Forty-six wrong raw-word controls and twenty wrong binding controls are
effective. The ordinary C loop's memory outcomes qualify separately; raw
literal complete-GPR, event-order and fault equivalence are not claimed.

## Actual Caller

The sole aligned retail direct JAL is at ROM `44CC8`, in the complete
28-word/frame-24 `func_150177F8`, VA `150177F8..15017868`.
Qualify its initial prepare call with argument one, twelve-byte bzero,
the no-argument reset, subsequent float/byte/word stores and saved RA lifetime.
All caller words are visited across 64 guest phases. Helper hooks deliberately
change the record bytes before reset, preventing a cached-state assumption.
The prepare and bzero providers remain explicitly bounded; this is not a
new proof of their entire implementations.

Compile the actual caller C body in the native fixture as well as the full
caller translation unit. The latter uses the existing ordinary C padder,
not the generated-slice padder. Applying that original build path preserves
the entire six-function caller object, SHA-256:
`69c050b3711483b9c81df1a45334f18ef33675a60bfde07105e4fd97baf89295`.
Its inherited unrelated pointer/integer diagnostic remains unchanged.
The initial raw-versus-padded setup gate failed before running tests;
preserve that zero-test receipt separately and use the corrected fresh suite.

## Fresh Qualification

Both tools copies pass all eight pre-install tests, with zero failures,
errors or skips: primary 15.862 seconds, older mirror 14.428 seconds.
Both shared project-tools checks pass. Both fresh installed checks also pass
per copy, explicitly reusing six unchanged behavioral checks under strict
source, raw/padded object, guard, caller and complete-image identity.

- 3,584 target phases cover every status byte, counters, padding, fences and
  repeated resets; all 43 original words are visited.
- Native32 O0/O2/O3 with trap UBSan covers 4,096 direct reset calls and 256
  actual C-caller cases per optimization, plus ten effective defined wrong-C
  controls. Native storage is correctly typed and disjoint.
- Nine independent GNU links cover three constrained rebases and thirty
  behavioral phases. All 320 selected root access prefixes fire and agree
  in guarded complete state and fault PC/delay-slot state.
- Thirty-two guest stack-overlap phases remain guest-only evidence, not a
  portable C alias or invalid-address claim.
- Nineteen strict-image controls reject code, metadata and length changes.

Actual Make executes three normal O2/g3 commands for the generated owner
and three for the typed caller. Both whole padded objects agree with their
qualified outputs; the caller object remains byte-identical to baseline.

## Full Image

Independent linking and production Make agree on exactly 303 changed ELF
bytes: 161 target-code bytes and 142 metadata bytes, zero exclusions.
Metadata accounting covers the target's symbol size and six closed existing
symbol/string serialization cycles, not changes to symbol values or addresses.
The initial body/size-only image prediction failed before tests; retain that
zero-test receipt and qualify the explicit complete metadata prediction.

ELF SHA-256:
`bbb2ee554aaa62b3b0b93ed0e26eb67f8a631681d62d7644d8630b08015a7663`.
Padded owner SHA-256:
`4fcae83271c6936a194bd0b48cacd5d00e011244eb7d839b805396ec9c7e098c`.

Preserve all other 6,054 function bodies, all 6,055 addresses and all 720
protected Game-data owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal 15,902 inputs, including all 1,454 linker objects and 27 focused pins.
Advance the preceding checkpoint's eight adopted entries before qualification.
New mutable entries are only the two C sources, guard CSV, target object and
ELF. The caller object, linker script and progress CSV retain identical bytes.

Primary tools are committed first at
`7ea237d1bd50edf8796fff0efca4fb3bff6e7ede`. Preserve all 1,578 preexisting
older-mirror dirty paths and its HEAD, adding only the two identical owned
task files. Do not commit that mirror or push either repository.

## Runtime Environment

WSL restarted and the prior disposable `/tmp` cache was absent. Revalidate
the complete native seal rather than trusting the missing cache. Retire only
the owned scratch compile/copy jobs after measuring stalled Plan9 reads:
the direct copy had transferred only 41 files. A native-verified archive
streamed over stdin restores and rechecks all 15,898 predecessor files in
14.719 seconds, without Linux reading the Windows source paths. Restore
cache-only executable modes for ELF/shebang tools; contents remain unchanged.
An initial shared-check launch lacked a helper's executable bit; both final
shared checks are fresh successful runs after that correction.

Use the same native-streamed boundary for installed source bytes, artifacts
and live-ELF recount input. Keep the host port, frozen Release, saves, user
configuration, VS Code and Docker processes untouched.

## Live Recount And Handoff

Native promotion rechecks every sealed file before and after adopting only
the target object, ELF, unchanged linker script and unchanged progress CSV.
The five mutable entries agree with their qualified outputs. Capture the
actual adopted native ELF bytes and stream them to the standard matcher;
require identity with the production and independent-link ELF before counting.
That fresh matcher exits zero in 5.501 seconds:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,755 / 5,505 (68.21%) | 0 | 1,750 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,082 / 4,832 (63.78%) | 0 | 1,750 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The converted-C denominator is unchanged. The 75% objective is not complete:
4,129 exact functions are required, 374 more than this checkpoint. Remove
only `func_150A00F0` from the ELF-pinned queue. It now contains 1,619
placeholders, 122 semantic/other definitions and nine unlocated entries.
Next `func_150F00EC` is a 43-word placeholder with 42 differences, queued
only and uncredited. Keep the 862-word `func_1508CAD8` owner stub separate.

Bank only the eleven scoped consumer paths after the installed-input,
documentation-link and older-mirror audits. README receives only the Total
and Game aggregate-row updates. Do not push. After the normal Graphify hook,
audit every one of the 43,824 preceding nodes for retention or unique
relocation and verify all changed C/Markdown hashes, mtimes and membership.
If the graph omits `built_at_commit`, retain that explicit metadata limitation;
do not forge a stamp or claim complete stamp provenance. Excluded-old nodes
remaining in the graph do not establish full-corpus re-extraction.
