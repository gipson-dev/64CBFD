# 1741 - Live type-2 group actor reset match

Verified 2026-10-27, following [Note 1740](1740-owner-identity-event-match-20261027.md).

## Result

Replaced the zero-return placeholder for `func_150222E0` in
`conker/src/game/generated_49D30.c` with its semantic actor reset.
The complete **184-byte / 46-word** body matches directly from C at VA
`0x150222E0..0x15022398`, ROM `0x4F790..0x4F848`.
There are **zero guards**, inserted words or omitted instructions. The original
40-byte frame, saved RA lifetime, actor home at SP+0x24 and branch delays match.
The actual O2/g3/no-unroll Make profile is retained.

This restores an existing C inventory row. Converted function/byte totals and
progress CSV bytes are unchanged. The captured, adopted Native ELF recount is
**3,818 / 5,506 exact (69.34%)**, Game **3,145 / 4,833 (65.07%)**, Init 492/492
and Debugger 181/181. Address drift is zero; 1,688 C functions differ. The 75%
threshold remains 4,130, requiring **312 more** exact functions. The wider goal
is still open.

## Behavior and actual interfaces

The function takes `void(s32 index, s32 group)`. It reads the live halfword
through `D_800C35C8[group][index]` and returns immediately for zero. For a
live entry it selects the eight-byte record through `D_800C35F0[group]` and
returns unless its unsigned type halfword is 2. It passes record byte 2 to
`func_15083E90` and returns if the lookup yields NULL.

For a found actor, it clears bytes 0x6C, 0x6D, 0x6A and 0x6B in retail order,
then halfwords 0x282, 0x27A, 0x27C, 0x27E and 0x280. It calls
`func_1507E7E4(actor, 0, 3, 0xFFFF, 10)` and clears byte 0x71 after that
provider returns. Retaining the actor pointer and the final store after the
call matters because providers may overwrite caller registers, argument homes,
record contents and the pointer tables.

The actual defining C interfaces are:

- `u8 *func_15083E90(u8 selector)` in `generated_AEB40.c`.
- `void func_1507E7E4(u8 *actor, u8 channel, u8 priority, u16 duration,
  s32 amount)` in `generated_AB760.c`.

Local declarations use those interfaces. The older shared-header lookup
prototype remains stale; no shared header or other caller is changed by this
recovery. Treating an unsigned selector as signed before an unsigned-byte
parameter is an equivalent conversion, so the effective negative control
masks bit 7 instead. Earlier supplemental scratch checks with the stale signed
interface are retained as historical evidence and are not the canonical ABI
qualification.

The full original and retained 72-word lookup is connected in guest checks:
selector zero returns NULL, and the first live identity match among 26 actor
slots wins. All 68 reachable instructions are covered; four unreachable
unrolled fallthrough words at offsets 0x78, 0x9C, 0xC0 and 0xE4 remain literal.

The sole aligned direct JAL is at ROM `0x4FD54` in the complete 39-word
`func_15022848`. No literal target address occurs in the ROM census.
That caller passes index/group through both callbacks, reloads its byte count
after each pair, and brackets the loop with `D_800C3638` writes. Its original
and retained bodies are equal and are both connected to this recovered target.
The preceding `func_15022398` remains a placeholder and is a bounded test
contract. The inner reset provider is also a bounded contract. No new helper,
whole-gameplay or hardware acceptance is claimed.

## Complete owner, bindings and image preservation

The entire raw C payload and six bindings equal independently assembled retail
assembly before padding. HI16/LO16 pairs bind the live and record pointer
tables; R_MIPS_26 binds the lookup and reset providers. Six independent GNU
links over three address layouts preserve all bindings, including signed-low
carry cases. The real padder reproduces the complete qualified object without
any guard-manifest change.

All 56 other owner functions and normalized pools are unchanged. The actual
three-command Make route reproduces all 57 compact functions and the complete
padded object. Baseline-owner, proposed-owner and isolated-target diagnostics
are empty. Existing duplicate generated_12D630 Make recipe warnings remain
separate.

Both tools copies pass eight fresh canonical methods, with zero errors,
failures or skips: 15.909 seconds in primary and 15.828 seconds in the older
mirror. Both shared tools checks pass. Coverage per copy includes:

- 2,560 target guest cases, all selector bytes, all 46 target instructions,
  complete private-state equality and a full observable 0x300-byte actor area.
  Record aliases and provider mutation of both pointer tables are included.
- 540 connected original/retained lookup cases, every possible hit position,
  inactive matching entries, live nonmatching entries and duplicate matches.
- 512 complete original/retained caller cases, every caller instruction,
  count shrink/growth and predecessor register/home clobbers.
- Native32 O0/O2/O3 with 49,152 valid cases per profile, typed function pointers,
  heap-backed typeless storage, trapping UBSan and 11 effective semantic controls.
- 57 fired guest fault prefixes, two sparse lazy-gate cases, an effective
  compiled MIPS early-read control and four guest-only stack-alias cases.
- Three raw/binding negative controls, six GNU links, 72 rebased guest cases,
  seven strict-image corruptions and three wrong-input controls.

The input seal contains **16,132 Native files** and **64 focused frozen
inputs**. The ordinary production Make completes in **0.501 seconds** and
reproduces the independent full-image prediction exactly: **150 changed bytes
= 149 target code + 1 symbol-size byte**, **zero exclusions**.
All 6,056 function addresses and all 6,055 other bodies remain fixed. Protected
Game data remains exact across 720 owners / 189,088 bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After installation each tools copy passes two fresh owner/image methods. The
six unchanged semantic checks are reused only with exact input-snapshot,
module and complete prepared-artifact fingerprints. The four adopted outputs
are the source, owner object, complete ELF and map; progress CSV, layout and
word-patch manifest bytes stay fixed. The actual adopted Native ELF is captured
and recounted independently of the proposed increment.

| Artifact | SHA256 or commit |
| --- | --- |
| Tools commit | 6a74f63d89c7779d363a04581a6b3b54a30e6f8f |
| Adopted ELF | 9827542129263cc9aadf4736a9c8459ef15f0d388ac22ab66beaff64ae4354b6 |
| Recovered owner source | a73fa2ca8befc207aace7880d1b4a8cb72c389f2395bb1092f7e770ee59c8173 |
| Padded target owner object | 7028265f9a67ec70e59d4a60908b8138e9464f03fa1f3ffd80f9999ecac87af8 |
| Raw selected C payload | d9ffb389bc262efcf505237026ecd45a324f46ec4dbf9751c33496c71fab9ba7 |
| Input snapshot | 6b9925b08ac69d5cb8371e48b10b3dd9a754b2822ca8c88c19cb91fd254b826e |

Receipts and frozen raw/Make/diagnostic evidence remain in
`conker/build/game-group-type2-actor-reset-match/`. Rejected oracle fixture
runs are archived separately: provider-symbol initialization, missing live-miss
coverage, explicit matching keys and inactive unrolled-lane coverage were
corrected before accepting either canonical run. The recovered C candidate did
not change during those fixture corrections. Prior WSL startup and stale-ABI
scratch evidence remain in Note 1740's ignored stage. No compiler install or
host-port/Release change was needed. Claude calls: 0 for this recovery.

## Next boundary

The next screened placeholder is `func_15063570` / `generated_90840`,
a 46-word actor state initializer. Its screen is not source/ABI qualification
or matching credit. Inspect its actor-pool indexing, retained incoming actor
pointer and two provider interfaces before recovering and qualifying the C.

Refresh these changed C/Markdown files and the two committed tools modules
with scoped AST extraction. Require old-node/valid-edge retention and no
query-graph dangling endpoints; preserve historical communities and centrality
without claiming a full-corpus extraction. Function narratives stay in these
working documents; root README changes are aggregate rows only.
