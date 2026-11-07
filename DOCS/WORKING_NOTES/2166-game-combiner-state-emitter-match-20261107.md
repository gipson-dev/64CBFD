# Dynamic combiner command recovered and directly byte matched

Date: 2026-11-07. Continues [Note 2165](2165-game-record-damping-update-match-20261107.md)
from consumer `ef13fe133257efe99c8896dc491a558603f7b5ff` and tools
`cde68505f09d9bdf117bbba747bebcb843538af7`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered interface and SDK body

`Gfx *func_1513F4E4(Gfx *cursor, u8 index, u8 *dirty)` replaces the false
s32 zero-return placeholder in `conker/src/game_169510.c`. All **103 words /
412 bytes** emit directly from semantic C under the existing O2/g3,
MIPS2/O32 profile, with **zero guards**, the original **24-byte frame**, saved
RA lifetime, incoming homes and seven literal relocations. VA is
0x1513F4E4..0x1513F680; ROM is 0x16C994..0x16CB30.

1. Call the selector `func_15143044(index, 0)` and compare its signed 16-bit
   result with D_800DD1BE. An unchanged cache returns the incoming Gfx cursor
   without touching dirty, table or output memory.
2. If changed and `*dirty == 1`, append gDPPipeSync, advance eight bytes and
   clear that byte. Other dirty values do not request the sync or clear.
3. Select the 16-byte record at D_800A4BA8[index]. Use the SDK's GCCc0w0,
   GCCc1w0, GCCc0w1 and GCCc1w1 macros with gDPSetCombine to emit the two
   packed command words. Preserve field masks and the first-word store
   before second-word field reads.
4. Store the signed 16-bit selection to D_800DD1BE and return the cursor advanced
   eight or sixteen bytes. Capture/reload behavior follows the original ABI.

The runtime table expressions require these lower-level SDK macros:
gDPSetCombineLERP token-pastes named constants and cannot directly take
runtime byte expressions. Normal SDK expression order emits retail exactly.
Reversing the two independent packed-expression orders still gives 103 words /
frame 24 but 62 word differences; that screen remains private and uncredited.

Raw target SHA-256: `8256c6666e4bfe47568ba48d277eab39022cb6c378deff45d3484b1716448a4e`.
Bindings remain at byte 28 (selector JAL), 36/40 (cache HI/LO), 56/76 (table
HI/LO), and 384/388 (second cache HI/LO). Two independent GNU links qualify
both repeated cache pairs and signed-LO carry at a second symbol layout.
No scheduling normalization, frame change or compiler-profile change is used.

## Actual helper, calls and original renderer connection

The complete aligned-ROM census finds **41 direct JAL sites in 36 distinct
callers**, with **zero entry or interior pointers**. Seven distinct callers
are already exact in production. This restoration does not restore or
credit the other callers.

The complete **10-word func_15143044**, VA 0x15143044..0x1514306C,
ROM 0x1704F4..0x17051C, is already exact in the frozen production ELF. Its
recovered interface is `s16 func_15143044(u8 index, s32 mode)`; this helper
returns `(s16)(0x7FFF - index)`. All 10 words are compared and execute in
the focused connection checks. Other bounded selector results additionally
qualify the emitter's complete signed 16-bit cache comparison.

The full **295-word func_1513DB00** invokes the combiner at 0x1513DEDC,
ROM 0x16B38C, with cursor A0, the selected byte A1 and its local dirty-byte
address A2. It consumes the returned Gfx pointer for following state commands.
**That renderer is still a production stub.** Its retained execution is
compared with a counterpart using an independent combiner provider; other
rendering/vertex services remain bounded. No renderer adoption or live
rendering/hardware acceptance is inferred.

The shared renderer fixture's color arena overlaps part of the combiner
table. The target-local fixture explicitly extends that known arena and
rejects unexpected overlaps; it does not silently overlay disjoint banks.

## Focused qualification

Seven checks pass before and after installation in both tools configurations:

* **4,388 guest cases per body** compare complete ordinary-RAM public effects,
  helper calls and pointer return with an independent masked-bitfield model.
  All 103 target words execute and full retail/compiled private state agrees.
  Cover all 256 indices, four dirty values, unchanged/changed signed caches,
  upper argument bits, helper mutations and six deliberate output/dirty/table/
  cache alias positions. Minimal unchanged-cache fixtures leave dirty, table
  and output unmapped. Second-word model fields reload after the first store.
* **42 cases per body** connect the original 10-word selector, compared
  against ROM and production. All 10 words execute, including its argument homes.
* **290 full-renderer cases per body**, with **64 actual target calls per body**,
  compare with the independent combiner-provider counterpart. Visibility,
  enabled/attached state, buffer presence, selected flags, view, animation
  and cache paths are represented. All 295 caller words compare; 293 execute.
  Words 115/146 are duplicate defaults skipped by both explicit preceding
  branches, whose opcodes and offsets are checked. Two hidden-buffer cases
  cover words 24..34, which the first fixture set omitted.
* **272 fired access cuts**, including **9 delay cuts**, compare complete memory,
  GPR/FPR/HI/LO, PC, delay context and access prefixes. Cover saved RA,
  incoming homes, explicit aliases, provider redirects and original-helper
  execution. Incoming-home mutation evidence is guest-specific.
* SDK native32 O0/O2/O3 each pass **4,147 cases** using eight-byte Gfx,
  pointer32, the typed u8/dirty-pointer/Gfx-return interface, all 256 selectors,
  signed 16-bit cache/results, and checked helper arguments/call counts, with
  trapping UBSan. Nine compiled negatives reject with exit 1: stub, reversed
  cache comparison, wrong dirty test, skipped clear, wrong helper mode,
  table record, mux field, cache store and return. Native cases use disjoint
  valid objects; guest aliases/private homes are separate evidence.
* All 103 raw-word corruptions, seven binding corruptions, historical-guard/
  pool/option corruptions and seven complete-image corruptions reject.
  Two independent GNU links preserve all seven original bindings.

No Claude call was needed for this direct recovery. The shared source,
parsers and previous oracles are unchanged; new behavior stays in five
target-local modules.

## Complete linked image and production

All **181 frozen inputs**, **58 raw/padded neighboring functions**, pools,
register metadata/options and **43 inherited warnings** are preserved.
Actual Make recompiles only game_169510.c and equals the independent
complete-image predictor: **354 changed bytes, zero exclusions**.

The target's Game slot changes by 320 bytes. 18 symbol bytes include the
target's extent change from 12 to 412 and two adjacent definition-order swaps;
16 string bytes reflect the corresponding contiguous name swaps.

The literal symbol/name groups are:

| First symbol-entry file offset | Original adjacent names | New order |
| --- | --- | --- |
| 2790108 | D_800DD1BE, D_800AB1CC | second, first |
| 2853436 | D_800A4BA8, D_8009BBC0 | second, first |

The predictor verifies original names, entry positions, contiguous string
blocks and every carried definition field before constructing both swaps.
A separate section/symbol census verifies the five changed symbol slots,
320 Game bytes, 18 symbol bytes and 16 string bytes. Every named value,
section binding and extent remains fixed except the intended target size.
No metadata or executable byte range is excluded.

All **6,052 function addresses** and **189,088 protected Game bytes across
720 owners** remain exact. Guard history is byte-identical and no rows
append. Makefile and progress CSV remain unchanged. Compilation/linking pass;
the whole-ROM checksum retains expected exit 2 and the inherited duplicate
generated_12D630 recipe warning. No whole-ROM checksum match is claimed.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regressions per copy are explicitly reused after exact fingerprints. The
new-module overlay and identified read-only missing-helper fallback preserve
all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,236 / 5,512 | 76.85% | 0 | 1276 |
| Game | 3,563 / 4,839 | 73.63% | 0 | 1276 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**174 more exact functions** remain to 4,410 / 80%. README gets aggregate rows
only. Four concise index leads retain all historical text. Refresh Graphify
with scoped, fail-closed legacy-node retention, without a fresh full-corpus
claim; commit tools before consumer source/docs/pin, then check the fresh
hook terminal, clean trees and stable production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `2145f715d8963cf0d41edea196f898a4386510294c2cd03cdf0157971b9ec376` |
| Production binary | `d3b6ff2545f5feef8d1613f7485f54ca417ac92fae9051a3c742301fd19fca10` |
| Padded owner | `1e010e6693af1ac1129caa7edb93bf0187b28fa8bd74e3a5e708802bb824cf00` |
| Unchanged guard manifest | `7d1ab46c6a902544af9086d2e3a0b1cabe5e0e467ba1c3f06be39b6f50d4fb9a` |

Ignored receipts: `conker/build/game-combiner-state-1513F4E4-match/`;
initial SDK source screens/census: adjacent private directory.

Next: **func_1513EAD8**, the related 183-word routine at
VA 0x1513EAD8..0x1513EDB4, ROM 0x16BF88..0x16C264. Its source remains a
placeholder and its 24-byte production extent remains unmatched. Inspect
the complete retail interface and state-table/graphics behavior, then
qualify independently. Keep the 80% goal active and preserve all frozen,
private-input, save, sibling-work and host Release boundaries.
