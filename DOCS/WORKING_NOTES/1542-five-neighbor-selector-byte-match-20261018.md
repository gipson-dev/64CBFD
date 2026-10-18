# Five-Neighbor Selector Byte Match

Date: 2026-10-18. Consumer predecessor **abb41c01**, tools predecessor
**77d9c40**. Tools banked first as **155037c**. Restore **func_150888A8**,
owner `generated_B3020`, VA **0x150888A8..0x15088A08**, ROM
**0xB5D58..0xB5EB8**. This completes one function; the wider goal stays active.

## Semantic Recovery

Replace the zero-return placeholder with **s32(u8 excludedId,u8 recordIndex,
s8 alternate)**. The word return is always a zero-extended ID or0xFF; do not
sign-extend IDs128..255. Preserve the original address-based name and semantic
comments. Retail saves the three incoming argument words in their home slots,
reads the index's low byte, and sign-extends the mode byte before testing zero.
No table-null or bounds gate exists; qualification supplies a valid table.

D_800D2350 points to 0x10-byte records. Scan exactly five neighbor ID bytes
at source record+9..+0xD. Skip ID0xFF, the unsigned excluded ID, and candidates
whose byte+0xE is nonzero. Requested class is1 for nonzero alternate byte,
otherwise2. Eligible requested-class neighbors update a last-seen fallback.
Among non-requested classes, any later nonzero class replaces the selection;
class0 only fills an empty selection. Thus the independent closed-form result
is the last eligible nonzero non-requested neighbor, else the first eligible
class0 neighbor, else the last eligible requested-class neighbor, else0xFF.

Preserve the first-candidate peel, then two neighbors per iteration for the
remaining four. Word-sized candidate/state locals retain byte loads and
explicit low-byte assignments without redundant compiler truncation copies.
The original eight-byte frame saves S0. No floating operations, helper calls
or public stores occur. Both argument-home writes and exact read order matter.

## Typed Caller

The byte prototype initially made IDO expand the existing caller expression
`func_150888A8(rec[0x2C], value & 0xFF, 1)` into redundant truncation code.
Pass **value** directly: conversion to the unsigned-byte formal already
performs the same defined modulo256 conversion. This is not a cast between
incompatible function types or a suppressed ABI warning. No K&R definition
or changed compiler profile is installed.

The typed declaration, full body and this one equivalent expression change
preserve **all72 raw owner neighbors and relative bindings**, including the
complete **34-word/136-byte func_15087DCC** at0x15087DCC..0x15087E54. Its
retail mask instruction remains identical. No caller matching credit is
added for a caller that was already exact.

Seven aligned retail JALs target the selector at ROM0xB4674/B4688/B46D4/
B52C4/B52DC/B5F28/B5F84. No exact pointer or J word was found; this does not
exclude computed/encoded references. Other parents func_150870D0 and
func_15088A08 remain false C stubs, unlike the live C tag-update caller.

## Bounded Register Normalization

The selected source emits **88 words/frame8** under the unchanged B3020
O2/g3/MIPS2/o32 compiler-only no-unroll profile. **Sixty expected-word guards**
normalize bounded GPR lifetimes and six symmetric equality operand orders.
This is a guarded match, not direct/guard-free compilation.

Preserve the incoming mode A2 through word9; it cannot be renamed as the
later iteration counter. Early words8..14 only adjust result/fallback roles.
Later regions separately normalize table, record, first ID/counter, paired
candidate IDs, entry pointers, class values and short-lived address/flag
temporaries. At accepted updates53/56 and73/76, the old current-selection
value is dead: retail writes the return role first, then copies it into loop
state at58/78. Do not apply one global permutation across those lifetimes.
Equality words22/41/52/61/72/82 exchange only their source-register fields.

Opcode sequence, branch displacements, delay layout, literals, memory order
and both HI16/LO16 bindings remain unchanged. No scheduling permutation,
inserted/omitted word, assembly fallback, Makefile or compiler-profile change.
Raw dead GPR fault states are not claimed identical; normalized/retail
instruction bytes and complete bounded states agree.

## Qualification

New tools: `experiments/game_record_neighbor_selector.py` and
`tests/test_game_record_neighbor_selector.py`. Ignored build artifacts:
`conker/build/game-record-neighbor-selector/`. Thirteen explicit hashes pin
owner/ELF/guards/ROM/assembly, Makefile/symbol/header inputs and four prepared
IDO components. The caller is in the pinned owner. This is the declared
closure, not every unlisted dependency. Exact predecessor/successor views
remain serial/non-nesting; no older fixture or check is weakened.

All **seven pre-install tests pass in76.159s**, and all **seven installed
tests pass in81.004s**:

```sh
python3 -m unittest tools.tests.test_game_record_neighbor_selector -v
```

- **16,584 three-way raw/normalized/retail guest cases** cover all **7,776**
  combinations of sentinel/excluded/disabled/class0/class1/class2 at five
  positions in both modes, all256 values of each input byte and candidate
  ID, eight full-word upper-bit argument cases and both stack phases. Compare
  full public memory, complete return word, ordered reads, no public writes,
  saved GPRs and unchanged FPR bits.
- Execute all **85 reachable words**. A static branch/delay reachability
  walk proves words35/59/79 are unreachable retail tail duplicates. They
  are preserved in the complete88-word comparison, not replaced or
  claimed executed. All88 raw-word mutations remain gated.
- **16,832 native32 cases per O2/O0 UBSan profile** use the real byte prototype
  and a valid4096-byte table. Independent zero/last-other/last-requested
  accumulators produce expected results. Compare every table byte and the
  global pointer before/after. Native calls narrow through the actual C
  prototype; raw guest register-word upper bits are a separate ABI test.
- Nine requested-class/exclusion/disabled/zero-overwrite/first-nonzero/
  stride/signed-return/no-fallback/first-fallback controls change actual
  guest return words and exit with explicit native wrong-result status23.
  The original excluded-neighbor fixture was also disabled, masking that
  control. Add an enabled excluded first neighbor; no recovered code or
  first prediction changes. Crashes are not accepted as result evidence.
- **Nine independent original/raw/padded links** at three placements pass
  **144 three-way rebased cases**, including both sides of HI16/LO16 carry.
  **472 access-fault prefixes across32 states** preserve public and stack
  memory/read prefixes for all bodies; normalized/retail complete state
  agrees. No hardware fault or arbitrary invalid native pointer claim.
- All88 raw words, two bindings, sixty guard expectations, **26 live/frozen
  input mutations** and nested historical views fail closed.

**144 paired whole-C-caller executions** run all34 actual func_15087DCC
words, both raw/normalized selector queries, low-byte stores to own record
+0x2D/+0x2E and final tag+0x2F. Cover null own-table, unchanged tag, zero tag,
signed nonzero tag, index0/3, both stack phases and neighbor profiles. The
second query uses the real first result masked to its argument byte. No
opaque helper or synthetic early exit is used. This is complete bounded
caller/selector execution, not whole-game gameplay validation.

## First Prediction And Build

Before production edits, freeze the first complete **3,257,636-byte ELF**,
source and guard successors using only a substituted padded owner in a
copied link script. Install the full C/prototype/call expression and sixty
guard rows, then run the existing scoped build:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals the first prediction: **256 changed bytes =254 target
code +two target symbol-size bytes** at offsets3010890/3010891, extent12->352.
Zero metadata exclusions. Audit all **6,057 bodies/addresses** and canonical
symbols: only this body and extent change, with every address fixed. All72
raw neighbors, pools/bindings and the actual padded owner match qualification.
Preserve every byte of the old guard prefix and append exactly60 rows. The
mechanical formatter changes only those rows' LF terminators to predicted
CRLF after checking the prefix and exact successor hash. No broad newline
normalization. Makefile unchanged; protected Game data remains **189,088 bytes
/720 owners /zero differences**. No new compiler diagnostic; the existing
duplicate12D630 recipe warning remains unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw target | 72a73228b5d5ec20212eca6c4682406ce6ffdb11f6266f4aa2e1ccc483241de4 |
| Whole ELF | 52311814c017d8714aa125c789243a20fc0eade9c09cb66680f15e5116d45f77 |
| Owner source | dde8438e4b98764c530ded940cf659620f4210dbf954161d85d1476d990860f3 |
| Guards | 73e3a4be767287fcef63d082bacd379919e1477372e6e74d20b25c4505a7ada1 |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Shared padder/PC16 tests pass **eleven per copy**, both tool smoke checks and
root tools-check pass. Four copies parse as ASCII/Python AST and both pairs
are byte-identical. Standalone mirror head ddbdd16 stays fixed: all **1,210**
previous dirty hashes are preserved, adding only two absent paths for1,212.
No mirror commit/reset, push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,980/4,828 (61.72%)**, **total3,653/5,501
(66.41%)**, Init492/492, Debugger181/181, **1,848 different /zero drift**.
Conversion counts/bytes stay fixed because the false C stub was already
counted converted. README changes only its two aggregate matching rows.

## Next Work

Recover **func_15088A08**, **212 words/frame0x18**, current false stub.
VA0x15088A08..0x15088D58, ROM0xB5EB8..0xB6208. Full retail body read and
three aligned JALs found at ROM0xB4B10/B4BE0/B62D8 (VA0x15087660/15087730/
15088E28). No exact pointer/J word; computed references remain possible.
Caller parents func_15087350 and func_15088D58 are still production stubs.
Audit the record pointer plus float bits passed in A1 and signed -1/0/+1
step result before assigning the C signature.

Preserve a single fractional backward/forward step at record+8, not a loop
that consumes arbitrary overshoot. Shift bytes+0x2B..+0x2E in the proper
direction and call the now-matched selector with signed mode+0x2F. Forward
steps inspect class/mode event flags D_800D23A8/D_800D2390. Later signed
halfword+0x24 wrapping, signed divisor byte+0x26, quotient byte+0x27, maximum
lap byte+0x28, global lap limits, signed actor ID+0x31, optional clamps and
32000/360000 timer caps need exact order and reloads. Keep divide-by-zero/
native UB versus guest trap boundaries explicit; do not invent hardware
results. Audit helper/caller float preservation and valid array domains.
Other retained assembly, handwritten150A76F0, fade gaps and wider queues stay
open. The active matching goal remains active.

Scoped Graphify refresh: **42,499 nodes /82,569 links /4,126 communities**.
Preserve **19,398 nodes from2,972 excluded-but-existing files**. Only three
line-disambiguated UPDATE_LOG heading IDs move; their labels and every other
old ID persist. The new note contributes eight nodes. Target/next definitions
resolve to **L575/L657**. Preserve the original graph in the ignored task
build folder; graph outputs stay ignored. No full-scan purge or graph-history
rewrite is performed.
