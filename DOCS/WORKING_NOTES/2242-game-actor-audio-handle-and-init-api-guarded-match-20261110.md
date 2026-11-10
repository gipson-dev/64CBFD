# Actor audio handle and Init API guarded match

Date: 2026-11-10. `func_15060778` now matches all **174 words / 696 bytes**
in production, with its natural **0x58 frame** and eight checked private
spill-home guards. The consistent narrow-handle Init API repair also
preserves the complete previously accepted Init object. This closes the
investigation in [Note 2241](2241-game-actor-audio-handle-abi-and-spill-audit-20261110.md).

Fresh actual-ELF recount: **4,311 / 5,513 (78.20%)** total; Game **3,638 /
4,840 (75.17%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,202** different. **100 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion rows and converted-function totals are unchanged.

Baseline consumer: `59587f5f8571452423b65ea580ff7c4dd3a854a5`.
Baseline tools: `ccdb67b4be30b866be45f75d312a750c0590a666`.
The ten new matching/qualification files are already banked in tools commit
`9be9fe159e437fe7866fa475a5005d3b46eacb0c`; the consumer records that pin.
Local commits only. The independently dirty sibling checkout is preserved.

## Source and interface

Owner: `conker/src/game_83300.c`; object: `build/src/game_83300.c.o`.
Retail slot: VA **0x15060778..0x15060A30**, ROM **0x8DC28..0x8DEE0**.
Original assembly remains in `asm/nonmatchings/game_83300/func_15060778.s`.

```c
void func_15060778(s32 sound_id, struct127 *actor, u16 volume,
                  s32 pitch, s32 arg4, s32 arg5, s32 flags);
```

The routine chooses the actor's handle at 0x8C or 0x8E from flags 0..1,
derives an effect from field 0x184 unless bit 8 disables it, and chooses
spatial audio with bit 4. Mode 3 queries the cached handle; a matching sound
is updated, otherwise bit 0x8000 requests a restart. A newly returned handle
is stored only when a slot was selected. Helper-visible mutations must not
change the cached handle/effect, while subsequent actor reads remain live.

The recovered repeated switch and word-sized handle carrier restore the
174-word shape; the former body was 171 words/frame 0x50. Preserve the
original `(func_1001147C(handle) == arg0) & 0x7FFF`: the mask is on the
boolean comparison. Remove the eager unsigned-halfword volume local.
Nonspatial command 8 takes the full word sum: 65535 + 48 * 50 is **67935**.
Spatial/creation helper parameters still narrow according to their actual
u16/s16 declarations. Source comments explain this distinction and the Init
generation-tagged slot allocator; original function names remain stable.

## Shared Init dependency repair

Both `conker/include/functions.h` and `conker/src/init_EB00.c` now declare
the first argument of `func_10010BE8` as **u16**. Remove its synthetic
`volatile s32 normalizedHandle` local and assignments. There is no
incompatible function-pointer cast or conflicting caller-only declaration.
The allocator still performs the original low-16-bit handle selection,
sixteen-slot reuse/scan, generation wrap and typed audio submission.

This changes exactly two raw Init routines. The affected caller
`func_10010FFC` keeps its C text but changes its emitted call coercion.
Its raw byte differences are audited explicitly; equal length/difference
counts are not used as equality evidence.

| Routine | Raw words | Raw frame | Old guards | Qualified guards |
| --- | --- | --- | --- | --- |
| `func_15060778` | 174 | 0x58 | 0 | 8 |
| `func_10010BE8` | 164 | 0x58 | 85 | 73 |
| `func_10010FFC` | 115 | 0x40 | 104 | 104 |

The Game guards change only eight load/store displacements at word indices
38, 39, 43, 44, 93, 95, 96 and 98: cached handle **SP+0x40 -> SP+0x44**,
cached effect **SP+0x48 -> SP+0x54**. Registers, opcodes and all six bindings
already agree. There are no inserted/omitted instructions or frame/profile
changes in the Game routine.

Init retail retains its existing 0x50 allocator frame. The replacement
normalizations compose the qualified source refinement with the frozen,
previously accepted Init object, preserving that entire object's bytes.
The generator does not read ROM instructions to construct the Init rows.
Expected raw words, relocations, complete row records and normalized hashes
are sealed in the manifest; stale source/bindings are rejected. Raw old,
raw proposed and original programs are independently exercised below.
These remain guarded Init bodies, not direct compiler matches.

There are **185 selected rows**, versus 189 before: net **four fewer**.
Every unrelated CSV line is retained byte for byte. All **88 non-target
Game functions** and **52 other raw Init functions**, their bindings, pools
and register information remain fixed. The complete padded **54-function
Init object is byte-identical** to baseline.

## Guest, native and original-caller qualification

- Game: **1,447 cases per body / 2,894 executions**, raw and original;
  every one of the 174 words is reached. Exercise every flag byte, slot
  selection, query mismatch, restart, full-word volume overflow, cached
  values, helper clobbers and late actor mutations.
- Init allocator: **2,160 cases per body / 6,480 executions**, current raw,
  proposed raw and original. Cover all sixteen slots, exhaustion, reservation,
  generation wrap, input upper bits, mix/global-mix bytes and callback
  mutations. Reach **162/164** words; static CFG proves words 33 and 83 are
  unreachable duplicate instructions.
- Affected Init caller: **776 cases per body / 2,328 executions**. Reach
  **109/115** words. Original words 18, 47, 48, 49, 68 and 78 are unreachable;
  this includes unsigned-LHU conversion fixup instructions. Raw counterparts
  are checked at their actual positions.
- Native SDK32: **4,379 cases per O0/O2/O3 profile**, UBSan enabled,
  **13,137 executions**. Compare canonical calls and **12,668,068 complete
  public output bytes per profile**. The four caller cases for sound IDs
  187/254 use deliberately extended guest memory; the SDK table has 187
  entries, so native runs retain only the 772 defined caller cases.
- **29 effective compiled semantic controls**: ten Game, ten allocator,
  nine affected-caller mutations. Every witness completes normally; execution
  errors are never counted as semantic disagreements. All **488** raw-word
  and relocation corruptions, **370** stale-guard attempts across both padders,
  and **eight** strict-image corruptions are rejected. Image corruption tests
  establish structural checking, separately from functional evidence.
- **132 executions across four independent symbol sets** bind raw,
  normalized and original programs at low halves 0, 0x7FFC, 0x8000 and 0xFFFC.
  Preserve the E0/E4/E8 slot-table aliases and adjacent mix/bus globals.

The aligned ROM JAL census identifies all five original Game call sites.
Four complete parents, `func_15060A30`, `func_15060A9C`, `func_15060B04` and
`func_15076250`, cover all their **104 words**. The larger `func_150538CC`
uses its actual **15-word** call window at VA 0x15054420..0x1505445C.
**888 full-parent runs + 36 window runs** make **864 connected target calls**;
other branches use opaque fallback helpers. All five sites have no V0 read
before a subsequent call or a previously established void-parent return.
The void interface does not invent a semantic return from incidental V0 bits.

The fixture originally placed voice memory over guest SP 0x40000; native
public-byte comparison exposed that fixture error. Voices now occupy 0x90000,
0xA1000 and 0xA2000. Additional low-nibble-zero handles and FFF0/FFFF generation
cases close the missed wrap branch; older 2,137/2,153-case receipts are
superseded by the final 2,160-case suite. One float mutation needed its actual
rodata pool mapped at 0xE0000. Neither fixture problem was a production bug.

## Actual Make, dependent objects and strict image

Freeze **2,189** source/header/compiler/layout/object/image inputs before
adoption. The independent nine-command owner plan uses the actual Make
recipes and unchanged per-function profiles, including the existing
`func_1000FEF0` no-unroll selection. Both target padders agree.

The shared-header inventory contains **199 linked C consumers**, no inactive
consumer in that inventory and no header-to-header inclusion of functions.h.
Force all 199 through their original Make recipes. The subsequent linked
build treats the audited header/Makefile/guard inputs as already accounted
for; this avoids broad timestamp-driven dependency changes after explicitly
rebuilding every affected linked consumer.

Five additional objects differ **only in their .mdebug payload**:
`debugger_258ED0.c`, `game/done/game_75810.c`, `game/done/game_75950.c`,
`libultra/audio/init_128D0.c` and `libultra/gu/sinf.c`. Every other named
section payload/address stays fixed. These metadata differences are audited,
not excluded. The linked image discards those debug sections.

The complete expected ELF differs at exactly **590 bytes**: the original
696-byte Game slot and the target symbol's size **684 -> 696**. No section,
range or dependent object is excluded. All **6,050** function addresses stay
fixed, and only the intended canonical Game body changes. No metadata
permutation is needed. All **189,088 protected bytes / 720 data owners**
stay exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production build elapsed **178.13 seconds**. Existing duplicate
`generated_12D630` recipe warnings and the expected full-ROM checksum exit 2
remain; actual owner/image/recount gates pass. No compiler/Makefile change.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `33ac445952e90e97179d1778f2a1874b529713a5e6bbaea4773202c2fcdb1bfc` |
| Built binary | `0c2573c322dc8034624c826591d2c91fb74df4ed3a5759ab958f755055b1402e` |
| Padded Game object | `55758b0b3bdd3141f65ccb74e1c0c2662e72b9c5b0f5bd43b7d9ffb73f69b325` |
| Unchanged padded Init object | `d8eff52ea164c3a6078e5aec0e3544d74cd963876962acf87ad079ab17e47f32` |
| Guard manifest | `1178b1e350bf4465bfabee931074f98b966bcd2c817ad3aae6b7e4058323a411` |
| Raw Game body | `3be80c40626a62646943723826602d2e96f1895995a1aaca760414a40801c526` |
| Raw proposed allocator | `4a8595bc493fe784ed3c931263c1d7b5da43077e22235cd1b45ab6bfe0c79175` |
| Raw affected caller | `e4a91191655041ad07700c77f1d2cf1987e7c42de0923636acd16eed1c7ca575` |

## Tool copies, graph and review

All **ten checks pass freshly before installation in each tools environment**
(mounted 204.70 s; sibling 134.54 s). After installation, **two fresh checks
per environment** requalify full owners/actual Make/image and Game guest
execution (mounted 50.28 s; sibling 48.76 s). The other **eight** are explicit
preinstall reuses verified against every tool/dependency fingerprint. Fresh
shared smoke checks pass; three unchanged shared regression receipts per
environment cover match-progress and padder parsing, not the changed API.

The sibling uses a private overlay for the ten new files. Missing
`diagnostic_rows`, `bound_blob` and `audit_proposal` use explicit fingerprinted
read-only mounted fallbacks. Consumer Make invokes the mounted CLI; independent
in-process padder checks use sibling helpers. No file is copied into the
sibling checkout, whose **2,434** pre-existing dirty paths remain unchanged.
Native Windows Git is authoritative: WSL Git reported false nested-submodule
dirtiness during preflight, which stopped before production writes. The
corrected adopter uses native Git without changing configuration or cleanup.

The scoped pre-documentation Graphify refresh contains **59,654 nodes /
113,056 links**, versus 59,653/113,077. All **59,653 old nodes remain**;
definitions outside changed paths stay equal apart from community metadata.
Verify source positions for **71 Game and 54 Init C definitions**, retaining
18 Game assembly pragmas. The header has one file node, without individual
prototype extraction. The ten new tool files still have **zero indexed nodes**
under current submodule filters. Historical excluded files remain retained;
this is a scoped refresh with explicit coverage limits, not full extraction.
Post-commit documentation graph receipts remain in the private task directory.

Codex is the only writer. No further Claude call is made: the one advisory
and its independently rejected fit/width suggestions are recorded in Note
2241. It does not replace the qualification evidence above. No host-port
source, saves or frozen Release artifact is touched.

## Reproduce and continue

From the prepared consumer root under WSL PSBBN:

```sh
python3 -m unittest tools.tests.test_game_actor_audio_handle_15060778_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The matching suite requires the retained exact pre-adoption baseline in
`conker/build/game-actor-audio-15060778-match/adoption/frozen/`; a clean clone
without those private inputs is not claimed to reproduce the qualified image.
No retail ROM or ELF fixture is committed. Public helper algorithms remain
typed opaque providers; finite defined float-to-integer/pitch ranges qualify
native behavior. NaN/Inf invalid conversions, FCSR, arbitrary physical stack
aliases, the complete large parent and actual audio/gameplay remain outside
this evidence.

Next: investigate **`func_1506045C`**, the recursive actor-state dispatcher
in the same owner. Its unchanged zero-return placeholder is still uncredited;
retail has **199 words / 796 bytes**, frame **0x50**, VA
**0x1506045C..0x15060778**, ROM **0x8D90C..0x8DC28**. Review its five-argument
recursive call, live actor+0x31C reloads, state-table remapping and calls to
`func_15080738`, `func_15065A5C` and `func_150642AC` before attempting C.
There is no matching candidate or qualification claim for that next target.
