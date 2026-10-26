# 1732 - Two-Key Actor State Classifier Match - 2026-10-26

The adopted Native ELF measures **3,809/5,506 exact C functions (69.18%)**,
Game **3,136/4,833 (64.89%)**, zero address drift and 1,697 different.
Only `func_151592B8` gains credit. Inventory and converted-byte totals are
unchanged; 321 more matches reach the present 4,130-function 75% threshold.

## Complete C and recovered interface

`func_151592B8`, owner `generated_185560`, occupies VA
`0x151592B8..0x15159370`, ROM `0x186768..0x186820`: 46 words and a
24-byte frame. The source replaces its full zero-return placeholder with
`s32 func_151592B8(u8 *actor, u8 mode)`. No shared declaration conflicts or
shared-header changes are required. Names and comments describe the recovered
roles while preserving the retail function symbol.

When the low mode byte is zero, capture the packed halfword `D_8008B040`
into a two-byte local object and scan its bytes backwards. Compare the actor
kind at `+0x84` as a zero-extended halfword held in a 32-bit local. A match
has priority and returns 3. Otherwise the late flag byte at `+0xAD` returns 2
when nonzero. With no flag, zero motion at `+0x28` returns 4; other float
values return 1. Both signed zeros take the zero path; NaNs take the nonzero path.

The original read-only table is in `asm/data/22FA90.rodata.s`, ROM `0x22FB00`,
VA `0x8008B040`: `3B3C` followed by fourteen zero padding bytes. It stays
unchanged. The C routine reads the real symbol; it does not hardcode the two
keys. Its integer address cursor avoids forming a C pointer before the local
object when the last byte is consumed.

## Nine derived storage/register guards

All 46 words, the 24-byte frame and both HI/LO bindings emit from complete C
under the ordinary O2/g3/mips2/o32 profile. Nine expected-word guards derive
exactly two temporary roles and one complete local-object translation:
cursor A1 to A2, kind V1 to A1, and the two-byte object from SP+0x14/0x15
into retail SP+0x0C/0x0D. The cursor, halfword store and lower bound all move
by the same -8 displacement. Branches, data-field offsets, arithmetic, frame,
instruction count and the two constant relocations are unchanged.
This is guarded C matching. No instruction is inserted or omitted.

Raw compiler code agrees on logical results and non-stack state for ordinary
inputs. Complete original/fitted states agree for the private stack aliases
and access-fault prefixes. Raw private stack placement is explicitly different;
guest stack aliases and faults are not claimed as portable C behavior. The
unreachable duplicate loads at words 29 and 34 remain in the emitted body.

Preserve all 36 raw/padded neighbors and their bindings, including all six
GLOBAL_ASM routines. Actual Make runs its five normal generated-object steps;
the complete padded object equals the independently qualified object and all
37 compact functions agree. No compiler profile, layout manifest, symbol
annotation, fallback manifest or caller source is changed.

## Caller and behavioral qualification

Graphify query finds the C stub and owner at
`conker/src/game/generated_185560.c:L221`; the retail census supplies the
complete real interface. There is one JAL at VA `0x15158E20`, ROM `0x1862D0`,
in `func_15158D2C`, and no literal registration. The original window loads
actor pointer `owner+0x18`, mode byte `owner+0x1D`, copies three coordinates
into `owner+0x20/+0x24/+0x28` with the last store in the JAL delay slot,
and stores the classifier result into byte `owner+0x30`. Its preceding
component-query result is saved into `owner+0x2F`. That earlier provider return
is bounded to 0/1/2 in the fixture; the parent C stub remains uncredited.

Both tools copies pass eight fresh private checks and both shared tools checks.
After production each runs two fresh installation checks and reuses six
unchanged semantic checks only through exact module, 54-input snapshot and
eight-artifact fingerprints. Original private execution receipts are preserved.

- 8,732 guest cases cover all mode bytes and low kind bytes, high kind controls,
  priority, table perturbations, signed zeros, NaN, infinities and subnormals.
- 240 alias cases span six layouts, two stack phases and full incoming mode
  homes. Disabled scanning requires no table/kind mapping, and a nonzero flag
  can bypass an unmapped float field.
- 432 original caller-window cases enter 864 target calls across coordinate
  aliases, both local gate outcomes and both stack phases. Full states agree.
- SDK/native32 O0/O2/O3 each run 1,456,128 positive cases with trap UBSan, all
  unsigned-halfword kinds, all mode bytes, typed actor fields, layout assertions,
  and actor/table canaries. Nine compiled semantic negatives are effective.
- Fifty fired guest fault-prefix pairs preserve complete states and access order.
- All 46 raw-word perturbations, bindings/extent/history controls, an actual
  padder negative, six GNU links across three layouts with HI/LO carry, and
  seven full-image corruptions are checked.

The first private suite correctly rejected a caller fixture that omitted the
preceding result-byte store, and a native assertion using the old SDK offsetof
macro as a GCC integer constant. The corrected fixture includes that real store
and uses the compiler offsetof builtin. Both complete suites then pass freshly;
the recovered C and frozen raw objects are unchanged. An exploratory metadata
report also hit its bounded timeout due to repeated symbol-table scans. A linear
36,242-row audit closes the same immutable image; the process audit found no
lingering worker. Failed reports and compiler probes remain separate.

## Production, image and adopted inputs

Actual production Make exits zero in 3.013s and reproduces ELF
`40663e322b4c401cb94a4a81a703498310b00346da0bd4444beec9c155d04e9d`. The exact delta is 137 bytes: 122 target code bytes and 15 metadata
bytes, zero exclusions. Metadata comprises the target size 12 to 184 and a
closed serialization swap of `D_800991D0` / `D_8009E6E0`; their named values
and types remain unchanged. All 6,056 function addresses and 6,055 other
function bodies remain fixed. All 720 protected Game data owners / 189,088
bytes remain exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The inherited duplicate generated_12D630 Make warning is unchanged.

Source SHA: `574614d51b7f805e4bbb1e6d1e18f98aa153363b482f0fa923e14507946fe114`.
Guard CSV SHA: `a72b7892470dbf90e90aeb998c4675994fc707941ee76938bdc2ebdfa937cf83`.
Padded object SHA: `81cf36bc2b41d66bb32c75c07f95283503e656ff82eaec76df34c8c63c03a11a`.
Raw body SHA: `0e2a8cae1b1fc8315d2027fb08bb5da06e7a04577d44c72d5e28ebbdf7602016`.

Baseline consumer `5ca3bfbb`, tools `7f416643`, ELF `ae2868d7`.
Tools `4980b4b1fa2b13c5babaa91e79a787bab9ef0299` are committed first. Preserve all 1,674 pre-existing dirty
paths and the history of the older tools mirror; only this pair is added there.
The final seal covers 16,095 Native files, 54 focused inputs and exactly five
qualified adoption outputs. The map is byte-identical; four outputs change
bytes. Progress CSV bytes and all inventory/converted-byte totals stay fixed.
Recount classifies the actual adopted Native ELF, not an inferred one-match gain.

The scoped graph closeout refreshes eight changed C/MD files through the
package native no-cluster update. It must retain or uniquely relocate all
44,280 previous nodes before adoption, preserve historical manifest freshness
outside that scope, and preserve prior community labels as historical metadata.
Global clustering/centrality are not recomputed or claimed fresh. Tools AST
extraction remains separate because the parent ignores tools/.

## Continuation

The ELF-pinned queue contains 1,568 placeholders, 120 semantic/other definitions
and nine unlocated screens. Next screened placeholder is `func_15007778`
(`game_33990`), uncredited until its own complete gates pass. Preserve the
unresolved pointer/NULL factory classification. Keep the 75% goal active.
Routine Claude calls: zero. No push or host-port work.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_two_key_state_classifier_match -v
```

Keep frozen raw objects intact. A new compilation requires new fingerprints.
