# Note 2615: Owner two-effect initializer direct byte match

Date: 2026-11-21. Consumer baseline `b3fbb112a8e01dd056bcde8abe0db46c3d8b8694`; tools baseline
`a5c018c375652dffa1e0300de2df8ecd4180ef80`. Qualified tools commit: `ac6d7d68dd291db9a6ece06254292aee6dfd5fe6`.

`func_1514F194` replaces its zero-return placeholder with the complete owner
initializer and two effect submissions. All **93 words / 372 bytes** emit
directly from semantic C, including the **0x50-byte frame**, S0/RA saves and
15 relocation sites. There are **zero guards, insertions or omissions**.
All **77 owner neighbors**, pools and existing compiler diagnostics are
unchanged. Shared headers and compiler profiles are unchanged.

Production recount: **4,598 / 5,528 (83.18%)** total, **3,925 / 4,855 (80.84%)**
Game, zero address drift and **930** still different. Init 492/492 and Debugger
181/181 remain exact. **101 more matches** reach 85% at this denominator.
The placeholder already counted as C, so conversion rows are unchanged.
Root README changes only its Total and Game byte-exact aggregate rows.

## Recovered behavior and interface

Owner `generated_179F30`; source `conker/src/game/generated_179F30.c`;
VA `0x1514F194..0x1514F308`, ROM `0x17C644..0x17C7B8`. The original routine
remains in `conker/asm/179F30.s:2862`. The correct interface is
`void func_1514F194(u8 *owner)`. Its earlier local declaration is updated too;
both existing wrapper bodies retain identical emitted bytes.

The routine calls `func_151D0F60` for channels 1 and 2 with 255/1, then
`func_151BB044`. A fresh `D_800BE616` byte read determines whether
`func_151BC074` runs. It then calls `func_151BD2F8` and `func_151B9F00` with
255/1, followed by two complete sixteen-argument `func_15160A58` submissions.

Both submissions use owner, channel 1, mode 2 and size 300. The first uses
the vector preset at `D_800A5958` and kind 12, with arguments 6..15 equal to
255,255,255,2,0,-1,0,0,255,1. The second uses `D_800A5964` and kind 15, with
255,0,0,255,1,-1,0,0,255,1. The first return is ignored. Only a nonnull second
return is attached through `func_1514EC1C(created, owner, 0x19)`.

The new preset declarations use the existing local `GameEffectVector` type.
The existing factory prototype retains its signed16-bit size, signed8-bit
negative selector and byte arguments. Native SDK32 checks use the real
`struct225` definition and objects for nonnull result addresses. No shared
structure or global data definition changes. The first semantic draft already
matches every word; no scheduling workaround or profile change is required.
Raw payload SHA256:
`ebef04b3290cdc362828d32c642981a8af1c466ae162cc0544f13781b03bfa20`.

## Qualification

- Literal original, raw C and production-padded payloads and bindings agree.
  All 78 owner function addresses/extents are preserved, apart from target
  symbol size 12 -> 372. The existing jump-table binding `jtbl_800A5E20` is
  retained. The natural unchanged O2/g3 Make recipe uses three commands and
  produces the independently prepared padded object exactly.
- The independent full-image prediction matches the linked production ELF
  exactly: **346 changed bytes**, **zero exclusions**, across 6,051 slots.
  The prediction explicitly includes two closed symbol/name reorderings of
  four and two existing names: six symbol records / 66 string bytes. Every
  named symbol attribute is unchanged except the declared target-size update;
  the tables are not omitted from comparison. Protected Game data remains
  **189,088 bytes / 720 owners exact**. ELF SHA256:
  `f6189d206bef66ef114feadb00f3de5857f6fb3bfdccf7f0713e0fe530810a3c`.
- Guest execution passes **3,088 cases in each of three streams**, covers
  **all 93 words**, and passes **87 target-access fault prefixes**. Complete
  memory, private stack, saved registers, calls, preset observations and
  ordered accesses agree. All sixteen incoming argument homes are overwritten
  by the factory contracts after capture, proving the second call rewrites
  all its arguments. Three instruction controls are effective.
- Native SDK32 execution passes **1,221 cases each at O0/O2/O3**, with strict
  aliasing and UBSan. Seven source controls detect wrong channel, stale gate,
  wrong second preset/kind, wrong attachment key, use of the first result and
  an unconditional null attachment. Owner/result storage and narrow argument
  types are defined C; null or overlapping-owner probes are guest-only.
- The fresh census finds two direct original calls and no aligned loaded
  pointer literals; computed references are not excluded. Both complete
  **eight-word wrappers**, `func_1514DB98` and `func_1514F110`, equal current
  linked bytes and pass **604 cases per stream each**. Skipped-call and valid
  wrong-owner delay controls are effective for both wrappers. Wider callers
  are outside this connected execution scope.
- Six independent GNU links at two code/data bases match the separate binding
  calculation, exercising R_MIPS_26/HI16/LO16 and signed-low carry. The padded
  owner's internal `func_1514EC1C` is also checked at its rebased address.
- Both caller wrappers and six of the seven helper routines equal original
  code; `func_151B9F00` remains unmatched.
  Execution uses explicit effectful contracts for all seven helper interfaces,
  rather than claiming their full implementation or gameplay acceptance.
- Five focused checks pass freshly in each primary/sibling configuration
  before and after installation, plus shared `make tools-check`. All imported
  source/data fingerprints agree. The actual dirty sibling checkout and all
  352 dependency hashes are preserved; the sibling tests use an isolated
  overlay without overwriting that checkout's changes.

The build retains the existing duplicate `generated_12D630` Make recipe
warnings and pointer/integer warnings in untouched neighbors. The owner
diagnostic comparison agrees with the baseline; this is not a warning-free
build claim.

The available host scene configuration consumes binary words and symbols,
not this recovered C. Its saved input has no identical target window or
prologue, and its configured symbols file is absent. Host mapping/runtime
acceptance is therefore unknown; no host source, build or Release changes.

`func_15188F84` remains private and uncredited: corrected registry declarations
and source/profile screens still miss the original 101-word/frame48 shape.
The read-only arrays at `D_80089240` / `D_80089250` point at live index/matrix
pointers; those declarations are recorded in its private handoff. Its best
ordinary source is 97 words / frame48, not an adopted match. The earlier
sequence query and noncanonical-return camera transition stay uncredited too.

Next inspect `func_15097798` in `generated_C3E20`: a 94-word gated camera
translation with six scaled coordinate updates. Freeze a fresh baseline before
new work. The wider 85% goal remains active. No push, model, ROM/save or host
changes are part of this checkpoint.

Graph maintenance: the native update exited 1 with all
69,904 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
69,945 nodes / 159,225 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
