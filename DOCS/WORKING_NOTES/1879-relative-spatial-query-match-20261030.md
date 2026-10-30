# Note 1879: relative spatial query register allocation match

2026-10-30. `func_1510F720`, owner `generated_13BB20`, replaces its zero-return
placeholder with `s32 func_1510F720(s32 x, s32 z, s32 radius, u8 **output)`.
VA `0x1510F720..0x1510F800`, ROM `0x13CBD0..0x13CCB0`: all **56 words /224
bytes** match after21 expected-word guards normalize one closed register
allocation cycle. The raw C is56 words with21 register-field differences;
this is a normalized match, not direct raw-C identity. No instructions are
inserted or omitted, and no opcode, immediate, branch displacement, frame or
saved-register slot changes. Tools commit: `0f928ea54f6f2c07120c145e20ca57751b721af4`.

## Recovered query and live roles

Starting at `D_800DBE48`, the function reads signed16 x/z coordinates at+8/+0xA
and an unsigned16 extent at+6. It tests strict absolute coordinate differences
against the captured signed32 sum of radius and extent. Arithmetic uses explicit
32-bit wrapping subtraction, negation and addition, preserving INT_MIN behavior.
The z coordinate is read only after the x admission test succeeds.

An admitted record with a nonzero signed16 child offset at+0xC follows that
relative offset. An admitted record with zero child offset is emitted to the
output array and increments the count. Its ordinary signed16 next offset at+4
is read after the output store, preserving output aliases that alter the record.
Rejected records also use the ordinary offset. Zero ordinary offset terminates;
negative relative offsets can move backwards in the allocated record region.
The result is the number of emitted records; output capacity is caller-owned.

This leaf has a16-byte frame, saving S0/S1/S2 at SP+4/+8/+12 and no RA save.
Raw C keeps query x in S0 and radius in A2; retail keeps x in A0 and radius in
S0. Distance, limit, child and next temporaries rotate through A0/A1/A2 while
z remains S1 and the output cursor S2. Both implementations retain the exact
same spill slots and restore their incoming values on ordinary calls.

The guards check complete expected words and bindings in this function only.
They alter register fields, including one commutative add operand order. Seven
live-value checkpoints compare156,184 logical-role observations over the main
guest corpus. Raw C agrees on ABI results, complete memory and access order;
normalized code agrees with retail on complete modeled state. Raw caller-saved
register identity is not claimed. Diagnostic register masks are used only to
check instruction shapes, never to rewrite a binary. Forty-two independent
padder controls reject wrong preimage words and bindings.

## Source fitting and qualification

Ignored evidence: `conker/build/game-relative-spatial-query-1510F720-match/`.
Initial goto/in-place absolute forms emit47 words and two saved registers.
Separate absolute-value temporaries and structured child/ordinary branches
restore three saved registers, but need58/59 words. Combining the two admission
tests with short-circuit && and a comma expression for the late z read recovers
all56 words and the retail control flow. Signed/summed operand variants emit
the same object; the selected source keeps explicit unsigned wrapping arithmetic.
Reusing argument variables as carriers collapses the required shape to48 words.
Register hints and inlined absolute/limit expressions do not remove the cycle.
These rejected screens remain private and uncredited.

Raw word SHA-256:
`e272f3de532d3f4b538488a3e09c0d5f9fa00c96eb42dfb3177a1a04bccee98b`.
Original/normalized unresolved word SHA-256:
`58ac6b72d797cb8f452811d62d7134d9ec008db87e4be605491d4ea19a0e4de0`.
Recovered owner source SHA-256:
`ee2bc6d65b6b08840404371b2ace7fb4b60051c59d4fbd08e3dac0729598b765`.
Padded owner SHA-256:
`0ef902748ef43779aa505307284096f7211a4c6b0da0ea09b6d893a32a0c9bac`.

Both tools copies pass eight fresh canonical checks plus shared checks.
Production repeats two installed checks per copy and reuses six unchanged
semantic checks only under exact input/module/artifact fingerprints.

- Guest:8,400 cases /25,200 executions cover all53 reachable words. Three
  original compiler-dead words at indices37/42/47 are retained literally too.
  Empty heads, both relative-offset routes, strict boundaries, unsigned extent,
  signed coordinates/offsets, wrapped signed32 extremes and live roles are checked.
- Aliases:2,430 additional guest cases cover output overlapping coordinate/child
  fields, the ordinary offset, global head and saved-register slots. For the last
  group, expected restored values come from independently modeled output writes
  to the three exact spill cells; the ABI checker is not disabled. Such stack
  and record aliases are not claimed as portable native C behavior.
- Prefixes:144 cuts, including56 delay-slot cuts, compare normalized and original
  complete state, actual PC/delay context and traces. These qualify emitted
  instruction order, not portable C faults. Rebases:108 cases over three GNU
  entry/global layouts, including signed low-half carries, preserve both bindings.
- Native32:4,200 cases per O0/O2/O3 profile with trapping UBSan, real allocated
  backing, unchanged record bytes, output tails and canaries. Seventeen compiled
  semantic controls are effective. Wrong unsigned offsets land in allocated zero
  sentinel records, so a trap or invalid access is not accepted as rejection.
- Eighteen IDO-compiled controls are effective, including the guest-only early
  ordinary-offset load. They reject wrong head, width/sign, inclusive boundaries,
  omitted axis/absolute value, coordinate/offset fields, child path, count and
  output steps. Compiler and oracle failures are not negative-control successes.
- Caller:one aligned JAL at ROM `0x1B3A10`, zero literal pointers. The original
  seven-word window at `0x15186554..0x15186570` in `func_1518652C` passes1,296
  cases, including both original count-branch exits. Output is parent SP+0x330.
  The nonzero path next overwrites A0/A1 before its two-argument bzero call and
  later sets A2 before consuming it; the zero path returns without using them.
  The preceding context setup and remaining parent stay bounded, not executed
  as a complete parent or gameplay claim.
- Owner/Make:all13 neighbors and pools remain fixed; the actual five-command
  recipe reproduces the complete padded owner. Target/owner/command diagnostics
  are empty. Inherited duplicate-generated_12D630 Make warnings remain in the
  dry-run plan. No shared header or compiler-profile changes are made.

The first saved-slot alias run tripped the ordinary preserved-register checker;
its corrected fixture checks each intentionally overwritten spill value from
the reference instead. Role observations were moved to instruction fetch so
branch instructions participate too. An unused-variable warning in the omitted-z
negative control was fixed while retaining -Werror. Failed receipts are retained;
production C and guard scope were not weakened. Routine work used zero Claude/
REA calls and no dependency/account changes.

## Image and measured checkpoint

Production equals the independently predicted complete ELF:
**166 changed bytes =165 target-code bytes +one extent byte**, metadata0,
with zero exclusions. All6,055 other bodies, all6,056 addresses and189,088 Game
data bytes across720 owners remain fixed. Inventory CSV, linker script, map and
all inherited guard rows stay fixed;21 new function-scoped rows are appended.
All17,045 sealed inputs are verified under declared changes. The older tools
mirror preserves2,075 inherited changed paths plus the three new modules and
is not committed.

Adopted ELF SHA-256:
`06ce0c0fb8ab45b7a570c4f7eed18a1e5dd44ad3a46c44bfa46e829452c99fa2`.
Actual Native ELF recount: **3,956/5,506 (71.85%)**, Game
**3,283/4,833 (67.93%)**, Init492/492 and Debugger181/181, zero drift.
The75% threshold remains4,130/5,506, requiring **174** further exact functions.

Tools are committed before consumer source/guards/docs/pin. README changes only
two aggregate rows. Graphify refreshes eleven supported changed source/tools/docs
files, records the guard CSV hash and retains all old nodes and still-valid
relationships. The old s32 return relationships remain valid and are retained.
No full-corpus extraction, global clustering or centrality refresh is claimed.
Next private screen: `func_150DB630`. Private/parked candidates remain uncredited; the
wider goal stays active. No push or pause.
