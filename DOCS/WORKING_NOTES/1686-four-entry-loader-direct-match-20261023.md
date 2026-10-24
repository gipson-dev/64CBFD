# Four-Entry Pointer And Count Loader Direct C Match

Date: 2026-10-23. Consumer predecessor `069348e3`; tools predecessor
`7027bcb7`. Qualification tools committed before the consumer pin as
`19a576c18df2871783d2600256b7bbc3e3c70584`. No push requested/performed.

## Recovered Routine

`func_1512D238`, owner `conker/src/game/generated_159940.c`:

- VA `0x1512D238..0x1512D2E4`, ROM `0x15A6E8..0x15A794`.
- All 43 words directly from semantic C, frame 64, five bindings, no guards
  or profile changes. Existing symbol size advances from 12 to 172 bytes.
- Raw C SHA-256:
  `4077557b28d7193ec8a40d7c7228c77ca117f0d299287f0cc874d74226e4cf36`.
- Retail/resolved SHA-256:
  `26f575f42cb2e07e47e51a216fc6c520bae742bd67e718a3cf14c5f91eafc30f`.

Recover `void func_1512D238(void)`. For each of four indices, call
`func_1502B5C8(&size,2,27,index)`, store its pointer in `D_800DC280[index]`,
and store `(u32)size / 24` in `D_800DC290[index]`. Both stores are
unconditional, even if the helper returns NULL. Keep the signed size local
declared before index, matching its real SP+0x3C home. Reversing those local
declarations leaves two scheduling differences.

Word and pointer return types can emit the same isolated instructions.
Resolve that ambiguity from the actual existing helper source:
`void *func_1502B5C8(s32 *size,u32 depth,...)`. Use a pointer table and the
canonical signed output-size local, with an explicit unsigned conversion
before division. Preserve the owner's existing signed count-table declaration.
No shared header changes, speculative shared record type or source-only
integer-return helper approximation is introduced.

Retail retains a divisor-zero break at `0x1512D2B0`, although saved S4 is
always 24 on the qualified paths. Preserve all 43 words; public paths visit
42 of them. Preserve all six saved-register lifetimes and the branch-likely
delay update that prepares the next helper's output-size pointer.

## Original Caller And Helper

The sole aligned direct JAL is at ROM `0x328F8`, VA `0x15005448`, in
`func_15005290`. No aligned literal function pointers are present. Execute
the complete six-word window `0x15005440..0x15005458`: prior initializer,
target call, then the original unconditional `D_800894B0` clear. Qualify
32 phases in the authentic 0x70-byte parent frame, with nonzero incoming
registers and bounded initializer side effects. The parent's C body remains
a placeholder; its complete object/source are unchanged. Full parent behavior
and other initialization paths are not claimed.

The existing linked 61-word `func_1502B5C8`, frame 80, is byte-exact against
retail. Execute every helper word with the target's nonnull size pointer and
depth two, including missing first/second descriptors, NULL results and
nonzero output sizes. Lower lookup/fetch providers are explicitly bounded.
The actual helper C body is also compiled in native32 fixtures using the
repository's GCC-compatible variadic macros. Its unrelated zero-depth path
with an unwritten descriptor is excluded, not repaired or declared safe.

## Focused Qualification

Both tools copies pass six fresh checks before and after installation, zero
failures/errors/skips and no reused checks. Pre-install times: primary 20.022
seconds, mirror 19.309 seconds. Installed times: primary 20.474 seconds,
mirror 20.114 seconds. Both shared `check_project_tools.py` runs exit zero.

- 4,096 ordinary guest phases cover 32 size patterns, every four-slot NULL
  mask, helper mutations and two stack phases. Retain complete literal
  GPR/FPR/HI/LO/RAM/events, four calls and saved-register restoration.
- 2,304 connected-helper phases execute all 61 original words. Preserve
  variadic component reads, descriptor masking and size updates when lookups
  or fetches fail. Do not add a pointer-success gate around the count store.
- Native32 O0/O2/O3 with trap UBSan: 98,304 calls per optimization using the
  actual C variadic helper and bounded lower providers. Cover all remainders,
  signed-boundary/full-word sizes, NULL/non-NULL combinations, table mutations,
  full fences and eleven effective defined wrong-C controls. Native storage
  remains disjoint and typed.
- 33 independent GNU links compare original, qualified padded and actual
  Make objects. 176 cases cover independent symbol rebases, overlapping
  output tables and tables backed by the guest private size/argument homes.
  Retail captures size before the first output store; preserve that literal
  order for aliases without claiming portable C stack/global overlap.
- All 832 root-access prefixes fire, with the same state, PC and branch-delay
  origin. Nine complete-image corruption/truncation controls are rejected.
  Neither portable C fault semantics nor hardware/FCSR parity is claimed.

A missing staged private runner was corrected before the final fresh suites;
no compiler/provider installation, production helper edit or historical-input
change was used to bypass it.

## Production And Preservation

The complete owner emits the same raw payload and all five bindings as the
isolated function and independent GNU assembly. Five raw/padded neighbors and
all owner pools are unchanged. The actual three-command Make recipe uses
normal O2/g3 and emits the qualified object byte-for-byte. Owner compiler
diagnostics are empty; inherited duplicate-recipe warnings remain unchanged.
Production Make exits zero in 0.573 seconds.

Independent and production full links reproduce the exact body/size-only
prediction: 135 changed ELF bytes, comprising 134 code bytes and one size
byte, zero exclusions. All other 6,054 function bodies and all 6,055 addresses
are fixed. The complete guard manifest is byte-identical. Protected Game data
remains exact across 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Result ELF SHA-256:
`85b152c71a51b836b6334efcd8069d1a346d3cdadedad904fd2d510e8b773add`.
Target object SHA-256:
`c70f1718dcf5f5086671990fba1b353be62b603ed48e634edba9285f0e0381c8`.

Seal 15,914 files, 29 focused inputs and all 1,454 linker objects. Verify
the disposable Linux cache against a fresh native capture, then stream inputs
and artifacts over native stdin/checked tar without Linux reading Windows
project paths through DrvFS. Native adoption checks every sealed file before
and after promoting only the target object, ELF and unchanged linker-script/
progress outputs. Only source/object/ELF are mutable. Preserve all 1,584
older-mirror dirty paths/statuses/hashes and its HEAD; add only two task files.
Host Release, saves/configuration and unrelated processes remain untouched.

## Live Recount And Handoff

Capture actual adopted Windows ELF bytes and require identity with production
and independent-link images before the standard matcher runs. The fresh
matcher exits zero in 1.365 seconds:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,758 / 5,505 (68.27%) | 0 | 1,747 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,085 / 4,832 (63.85%) | 0 | 1,747 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted-C denominator unchanged. The 75% goal still requires 4,129 exact
functions, 371 more. Remove only `func_1512D238` from the ELF-pinned queue:
1,616 placeholders, 122 semantic/other definitions and nine unlocated entries
remain. Next `func_15171CA0` is queued only, uninstalled and uncredited.
Keep the 862-word `func_1508CAD8` owner stub separately queued.

Bank only the nine scoped consumer paths. Root README gets only two aggregate
row updates. After the normal Graphify hook, audit all 43,855 old nodes for
retention or unique relocation and all eight changed C/Markdown hashes,
mtimes and memberships. Never forge a missing commit stamp or equate
excluded-old retention with complete corpus re-extraction.
