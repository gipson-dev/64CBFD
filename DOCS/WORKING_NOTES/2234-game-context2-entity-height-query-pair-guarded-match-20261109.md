# Game context-2 entity-height query pair guarded match - 2026-11-09

`func_15045880` (lowest) and `func_15045AE4` (highest) now match their complete
**153-word / 612-byte** retail slots. Each semantic C body emits all 153 words
with the natural **0x28 frame**, saved S0/S1/RA lifetimes, and selected-index
home at SP+0x20. Guards close 72 and 74 words respectively. No insertion,
omission, source padding, compiler-profile or shared declaration change.

Fresh production-ELF counts: **4,304 / 5,513 (78.07%)** overall, Game **3,631 /
4,840 (75.02%)**, Init 492/492, Debugger 181/181. Address drift is zero;
1,209 functions still differ. The active 80% goal requires **107** more
matches to reach 4,411/5,513. The README changes only aggregate rows.

## Scope and contract

Owner `conker/src/game/generated_71820.c`; object
`conker/build/src/game/generated_71820.c.o`; retail `conker/asm/71820.s`.

| Function | VA span | ROM span | Raw words | Guards |
| --- | --- | --- | --- | --- |
| func_15045880 | 15045880..15045AE4 | 72D30..72F94 | 153 | 72 |
| func_15045AE4 | 15045AE4..15045D48 | 72F94..731F8 | 153 | 74 |

This finishes the matching left open by [Note 771](771-game-entity-lowest-height-query-semantic-recovery-20261003.md)
and [Note 772](772-game-context2-entity-highest-height-query-recovery-20261003.md).
The context-3 pair from [Note 2233](2233-game-entity-height-query-pair-guarded-match-20261109.md)
remains exact. Original assembly and all existing restoration ownership stay intact.

Both interfaces are `(f32 *position, f32 threshold, s32 *input,
HeightResult71820 *result)`. The float threshold uses the second o32 argument
word. There is no early threshold gate. Defaults are D_80098D50 (47C34FF3,
99999.8984375f) and D_80098D54 (C61C4000,-10000.0f). Prepare input[0] with
150A44F0 and inline scratch D_800D37E0, then reload input and signed-truncated
X/Z for 150A43E0. These helper boundaries are bounded providers in the tests.

The signed count scans 16-byte D_800D3300 rows. Convert signed fixed heights
to f32 and multiply by 1/256. Lower keeps the first strict minimum >= live
queryY; upper keeps the first strict maximum <= live queryY. Equal heights
retain the first candidate. Helper mutations of queryY and result height remain
observable. Nonpositive counts select none.

Cache triangle and signed vertex BYTE OFFSET before three XYZ short copies.
Reload candidate.padC as entity index after copying, use pointer global
D_800DBEF4 with stride 0xA0, and publish that entity address in result.value
before loading entity.metadataTable. Table lookup uses signed
`(triangle-D_800DBE3C)/12` minus unsigned16 firstTriangle; null table uses
entity.metadata. Publish flags|6, then **reload both the candidate entity index
and global entity base** before testing entity flag 0x80 and optionally ORing
result flag1. State is **2** in both queries, stored after the late lookup.
Lower accepts height<=threshold, upper threshold<=height. Selected failure
retains publications; no selection clears only flag2.

## Natural source and closed normalization

Baseline C emitted 150 words plus three slot-padding nops, with 88 differences.
Bounded screens covered explicit flag widths, metadata/address representations,
local scopes, register hints and state branch shapes. Early state-store forms
were rejected: state can overlap the candidate index and affect its later reload.
The accepted source shares a byte state value across the two publication arms.
It naturally emits 153 words, frame0x28 and the original selected-index home.
Focused comments identify the context-2 query and late flag-owner reload.

Raw payload SHA256:

- Lower: 2c3b77a9e3ae18d3b904608b513418f1a358debe319642c91f91bf883d04a8ea.
- Upper: 1c114fc7b52ac182166c6a5e388ebded3c854623435967f63d4f18aa7c116e28.

The normalizer pins each complete raw body, function/owner and all 16 binding
sites. It derives selected/count/index/cached-pointer register changes and
the copy-loop schedule with identical effective short addresses and memory
event order. Metadata-edge decomposition exchanges a common flags load for
two exclusive edge loads: each path still executes exactly one after its
metadata store. The entity role copy is derived from the emitted move opcode.
The triangle-base LO16 binding moves from raw byte388 to normalized byte392;
the HI16 at360 and symbol remain fixed. Other bindings retain their identities.

The tail closes duplicate state constants, a redundant branch and unreachable
duplicate state store into retail's branch edges. Actual state writes remain
after entity lookup. Retail reloads the flags byte just stored; source forwards
that same zero-extended value across read-only lookup. The proof permits that
specific store-forwarding equivalence, with no arbitrary payload substitution.
Guest checks compare the complete public read/write traces after removing only
flags-byte reads equal to this invocation's most recent stored byte. Every other
public access and its order must match. This is not a fault-prefix equivalence
claim for that redundant load. Upper also closes independent float-load order.

All 146 guards are replacements. Expected and replacement bindings are recorded
separately, including the moved LO16. Both independent target padders and original
assembly agree exactly. This includes control-flow and flags-forwarding closure,
not only register allocation. No unused slot or fabricated source word is added.

## Qualification

The 43-function owner contains 41 C definitions and two retained ASM functions,
15044660/15044ED0. All **41 non-target neighbors** remain identical in raw and
padded objects. Pools, reginfo and all 6,051 function addresses stay fixed.
CFE diagnostics remain zero. The actual five-command Make route agrees with
the independent padded owner. Strict whole-ELF prediction accounts for **472
changed bytes**, only the two 612-byte slots and st_size updates600->612, with
zero unexplained bytes or exclusions. Protected189,088 bytes across720 owners
remain exact (SHA2560bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670).
Conversion CSV and Makefile remain fixed. The inherited whole-ROM checksum
mismatch (`make all` exit2) and duplicate12D630 Make warnings remain.

- Guest: 904 cases per body across six bodies =5,424 executions, plus48 rebases.
  Full state/call observations, unsigned firstTriangle, byte offsets, private
  homes, saved registers and physical aliases pass. Raw dead words are109/130;
  every retail word, including dead word111, is verified. Public access-trace closure
  passes. Alias fixtures distinguish both late reloads and an early state store.
- Native SDK32: 1,728 defined cases at O0/O2/O3 with UBSan and24 effective
  per-function controls per profile. Full result/entity/candidate state,
  padding/canaries and readonly data pass; private homes/physical aliases are
  guest-only. No compiler/interpreter/sanitizer failure counts as a witness.
- IDO:30 effective controls, including separate cached-index, cached-base and
  early-state alias mutations per function. Both padders reject292 stale
  expected-word/binding cases each, including absent expected bindings. These
  corruptions use independent target objects; successful full-owner production
  padding is checked separately. All306 raw word corruptions and seven image
  corruptions are rejected. Eight independent GNU links and32 executions cover
  HI/LO carry boundaries.
- Caller census: one low JAL in150461D0 (word48, ROM73740), one high JAL
  in15046460 (word50, ROM739D8), no aligned entry pointers or direct tail jumps.
  Both complete164/166-word C callers run1,296 cases/864 target invocations
  against all three target forms. Every caller word is visited. Float ABI,
  real primary/secondary stack buffers, byte-narrowed results, packet selection,
  copies and early paths agree. Preparation and the second context-3 query
  remain bounded providers; full helper algorithms/gameplay are not claimed.

Six fresh focused tests run before and after installation in both tools
environments, with helper origins and dependency hashes recorded. The sibling
uses a read-only overlay for new modules; all2,439 preexisting dirty paths are
preserved. Shared smokes are fresh; three unchanged regression checks per copy
are explicitly fingerprinted reuses. There is no native/control receipt reuse.

Graphify refresh requests the owner and six tools modules. All41 owner C source
locations and both retained ASM routines are audited. Existing nodes outside
changed paths and excluded existing corpus are retained fail-closed; no full
semantic extraction is claimed. New tools-module node coverage is recorded
as observed. Tools are committed before consumer source/guards/docs/pin.
No push or host-port Release changes. Ignored evidence and the accepted handoff
are under `conker/build/game-context2-height-pair-match/` (717 frozen inputs).

Next: `func_1504BE2C`,147 retail words /144 screened differences, in
`conker/src/game_77AD0.c`. The hard private1510D404 remains uncredited.
Keep the full80% matching goal active.
