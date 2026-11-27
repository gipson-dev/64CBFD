# Owner and level action classifier direct match - 2026-11-27

`func_1514CA80` replaces the zero-return placeholder in
`conker/src/game/generated_179F30.c` with its complete **439-word / 1,756-byte**
semantic classifier. VA `0x1514CA80..0x1514D15C`; ROM `0x179F30..0x17A60C`.
Its **zero-byte frame** and **10 relocation positions** match retail.
No scheduling, register, spill, instruction insertion/omission or compiler
profile change. Eight checked table bindings qualify the target; one checked
pool displacement preserves the existing neighboring function.

Fresh production: **4,713 / 5,528 (85.26%) total**, **4,040 / 4,855 (83.21%)
Game**, Init 492/492, Debugger 181/181, zero drift and 815 different.
Exactly one new match: the classifier. Parent and neighboring function retain
their existing matches; conversion rows and denominators stay fixed.
The **90% goal remains active: 263 more** matches reaches 4,976 / 5,528.

The recovered interface is
`u8 func_1514CA80(u8 *owner, s32 *first, s32 *second, s32 *third)`.
The unsigned-byte return established in Note 2733 is retained, and its deferred
four formal parameters are now restored with the complete body. No incoming
argument-home stores or frame are emitted. The routine calls no services.

It starts with flags zero. A switch on owner byte +4 may write the third
output and set bit 2. A later switch on `D_800BE9F0` may write the second output
and set bit 1. Selected owner kinds or unique IDs at +0x3B may then write the
first output and set bit 0. Unselected outputs remain untouched. First/second/
third are observed output roles; more precise gameplay names remain open.

Keep the reads in order: an aliased third-output store can change the level;
an aliased second-output store can change the owner kind or unique ID before
the later test. No restrict qualifiers, eager output clearing or cached field
loads are introduced. Word-output aliases are supported by the tested typed
storage contract. Guest big-endian and native host-endian alias behavior are
qualified separately; no cross-endian byte identity claim is made.

The first complete source already emitted 439 words and no frame, with nine
positional differences confined to the level-14 unique-ID split. Expressing
its mutually exclusive IDs 8 and 1 as a switch, in original physical case
order, resolves every difference. The alternative if-1-before-8 form retains
seven differences and is rejected. No dummy local, padding, volatile or
instruction-scheduling guard is used.

The original four tables have 187 / 54 / 19 / 10 entries, totaling 270 entries
and 1,080 bytes at `jtbl_800A59AC..0x800A5DE4`. Every table byte matches the
frozen ELF and retail ROM; every generated entry resolves to the corresponding
classifier instruction. The existing 10-entry neighbor table starts at
`jtbl_800A5E20`. All intervening retail constants remain unchanged.

The compact pool grows from 48 to 1,120 bytes: the four new tables precede the
retained 40-byte table and consume its previous eight bytes of alignment.
Every relocation, ownership tuple and non-relocated zero byte is accounted
for. All 76 other raw neighbor bodies remain fixed. `func_1514EA1C` retains
its complete 84-word body and bindings except one LO16 addend, displaced by
exactly 1,080 bytes. A checked pool-offset guard restores its existing retail
binding. Its C body is unchanged and earns no additional matching credit.

Eight target guards map the compiler's local `.rodata` references onto the four
named retail tables. They check the expected word and relocation. The ninth
guard checks the neighboring LO16 displacement. Both complete padders reproduce
the frozen before object and the same selected object. All 77 padded neighbor
bodies, bindings and pools remain fixed. The complete prior guard history is
an unchanged prefix followed by exactly these nine rows.

Fresh qualification:

- **14,130 cases across five literal guest streams** compare full RAM, GPR/FPR,
  FCSR, HI/LO, trace, delay ownership and return state. All **439 words** execute.
  An independent ordered reference checks every memory effect and return.
  Include nine output-pointer alias patterns and ten unused-null-output checks.
  Forty fired access-prefix quintuples match. Three valid wrong-word controls
  reject by comparison. Guest fault probes do not claim portable C exceptions.
- **207,314 native32 cases per O0/O2/O3**, three translation units, actual
  extracted C and an independent table-driven reference. Typed signed-word
  storage permits legal output/owner/level aliases. Complete arenas, canaries,
  level, return and MXCSR agree. Strict aliasing, trapping UBSan, LTO type checks
  and noipa boundaries are enabled. Eight wrong-source controls exit 42 by
  comparison, including eager level and stale owner/unique-ID reads. No compile
  error, signal or trap is counted as a valid rejection.
- **878 word-mutation checks**: 862 remain visible; 16 reject against expected
  guard words. Twenty binding mutations yield four visible differences and
  16 expected-relocation rejections. The ninth guard rejects word and binding
  drift in both padders, four additional rejections.
- **20 GNU links / 120 guest rebases**, five independent construction routes
  across four entry regions. All four table symbols and the level symbol move
  independently through signed HI16/LO16 carry boundaries. Table destinations
  move with the code. Both scoped padders reject oversized input; the generic
  route rejects a stale overflow guard, the generated route rejects the span.
- The accepted **complete 109-word dispatcher** is pinned to original ASM/ROM
  and executed with the complete classifier: 761 cases across two parent and
  two child streams, **3,044 runs**. All 109 parent words and 73 child words
  execute in this connected matrix; standalone tests cover all 439 child words.
  Full private states and independent dispatcher/classifier references agree.
  Two valid call/argument controls reject by comparison. Other dispatcher
  services remain opaque. The unfinished 538-word grandparent is unexecuted
  and uncredited.
- Actual three-command owner Make replay reproduces the complete qualified
  object. Four existing pointer/integer Warning712 diagnostics remain unchanged
  after source-label/line normalization; zero new warnings or profile changes.
- An independent frozen-before-C plus original-ASM whole-image prediction
  equals the private and production ELF: **1,310 changed bytes**, **zero
  exclusions**, 6 accounted symbol-record permutations.
  All protected **189,088 data bytes / 720 owners** and other function bodies,
  addresses, extents and conversion rows remain fixed.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 216.891 s | 5 fresh / 0 reused |
| preinstall-sibling | 217.569 s | 5 fresh / 0 reused |
| installed-primary | 174.44 s | 5 fresh / 0 reused |
| installed-sibling | 190.168 s | 5 fresh / 0 reused |

All 20 target test methods are fresh. Shared tools-check passes. Primary and
isolated sibling import, task, data and artifact fingerprints agree; each uses
its own tools paths. The prior dispatcher's copied module description is
corrected with its executable AST unchanged. Dirty real tools sibling remains
untouched. Freeze: 4188 inputs / 3140 copies.

Tools commit: `3a2176b716ac2c2fb174ee1ade3724316eeed840`.
Baseline consumer: `ecdc8f9fc18c0fa32b70c3eab5a9e6a476b1a307`.
Source SHA256: `f658184ee0ac81673b7f80c165897e72d32ff1a94c420ada11048b26d8400c11`.
Padded owner SHA256: `d3d99c91fb43447354e7c631f8ac263f48ac40383a365ebdcc6f7f353515e02c`.
Production ELF SHA256: `dedad1e9de8ce185666ae150952a3c1a6fd56554c7159edb4c012664c3ba4a1e`.
Receipts: `conker/build/game-owner-action-classifier-1514ca80-private`.

Routine Claude calls: zero; no subagents. The host generated classifier remains
an empty stub with active applicability unqualified; no host transfer, build,
launch or Release change. Scoped Graphify refresh retains all old IDs and
qualification records, updates the complete four-argument classifier and the
neighbor's binding metadata, and observes actual commit-hook producers terminal
before publication. No full-corpus re-extraction claim. Root README receives
only aggregate rows. Continue the active 90% goal from sealed N79.
