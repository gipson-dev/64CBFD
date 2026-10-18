# Record Progress/Lap Updater Byte Match

Date: 2026-10-18. Consumer predecessor **8c8313d8**, tools predecessor
**155037c**. Tools banked first as **64c3a9f**. Restore **func_15088A08**,
owner `generated_B3020`, VA **0x15088A08..0x15088D58**, ROM
**0xB5EB8..0xB6208**. This completes one function; the wider goal stays active.

## Semantic Recovery

Replace the false zero-return placeholder with **s32(u8 *record,f32 delta)**.
Keep the address-based name and a concise semantic comment. Mixed o32 passes
the pointer in A0 and float bits in A1. Return a complete signed word -1/0/+1.
The 24-byte frame saves RA; the record pointer is homed across helper calls.
No saved F20 pair belongs to this routine. No new caller declaration or
compiler-profile change is needed: both other caller parents remain stubs.

Add delta to binary32 fraction+8, store and reload it, then consume at most
one backward or forward boundary. Do not loop over arbitrary overshoot.
Backward steps shift neighbor bytes+0x2B..+0x2E toward the previous record;
forward steps shift them the opposite way. Snapshot the original bytes before
stores. Call the already-matched `func_150888A8` with the proper middle/next
IDs and signed mode+0x2F, then store the result's low byte. NaN does not
cross; infinities cross once and remain infinite. Hardware FCSR is not modeled.

Forward steps inspect global mode D_800D23A8 and the current route class+0xF
through D_800D2350. Mode0 maps class5/6 to event1/2; nonzero mode maps class7/
8/9 to event1/2/3 at D_800D2390. After an earlier event store, reread the
record's current-neighbor byte and class through the captured table. An
event byte may alias that record byte in the guest tests; caching it loses
the retail event chain. Do not refresh the captured global table pointer.

Only a nonzero step updates signed halfword+0x24. Capture signed goal
D_800E0BE7 before output stores, wrap the halfword, reload it signed, divide
by signed byte+0x26 and narrow the quotient to signed lap byte+0x27. Optional
D_800BE616 clamping stores goal+1. Update maximum+0x28 only for a strict
increase. The signed actor ID+0x31 is gated only by ID<count, not ID>=0;
record disable byte+0x30 and a strictly positive timer+0x1C gate score work.

For maximum<=goal, subtract stamp+0x18 with low32 arithmetic and interpret
the result signed, cap only above32000, conditionally replace nonpositive or
slower best halfword D_800E0C10[ID], and store elapsed+0x20. Reread maximum
after stores. At goal equality, reread timer, cap above360000 and store
D_800E0C18[ID]. Reread maximum again; stamp becomes unsigned0-minus-fresh-
timer at equality, fresh timer below goal, or remains untouched above goal.
Unsigned subtraction avoids C signed-overflow UB; signed narrowing follows
the verified two's-complement ABI. Negative elapsed values are not clamped.

## Bounded Register Normalization

Selected semantic C emits **212 words/frame0x18**, with **88 raw differences**
under the existing B3020 O2/g3/MIPS2/o32 compiler-only no-unroll profile.
Eighty-eight expected-word/relocation-aware guards normalize snapshot GPRs
over words17..29 and41..52, a closed temporary cycle over54..206, and five
commutative ADDU source orders at66/75/88/97/107. The old zero-step value is
dead within each crossing arm before its final -1/+1 assignment.

This is a guarded match, not direct/guard-free C. All floating operations,
opcodes, branch displacements, delay layout, memory order, length and all
26 bindings stay fixed, including both real selector calls. There is no
scheduling permutation, insertion/omission, assembly fallback or profile edit.
Raw dead-GPR interrupted states are not claimed identical; normalized/retail
complete bounded states agree. All 72 raw owner neighbors and pools/bindings
remain unchanged, including the previously qualified live selector caller.

## Qualification

New tools: `experiments/game_record_progress_lap.py` and
`tests/test_game_record_progress_lap.py`. Ignored artifacts live under
`conker/build/game-record-progress-lap/`. Thirteen explicit fingerprints pin
owner/ELF/guards/ROM/assembly, Makefile/symbol/header inputs and four prepared
IDO components. This is the declared closure, not every unlisted dependency.
Historical views are strict, serial and non-nesting; older checks are not
weakened. No alternative draft C body is imported.

All **seven pre-install tests pass in100.200s**, and all **seven installed
tests pass in122.806s**:

```sh
python3 -m unittest tools.tests.test_game_record_progress_lap -v
```

- **7,556 three-way raw/normalized/retail guest cases** compare complete
  public memory, full return word, interleaved read/write traces, saved GPRs
  and FPR bits. The real 88-word selector executes, not an opaque stub.
  Cover ordered/nonfinite fractions, one-step overshoot, signed count/mode/
  divisor bytes, all255 nonzero divisors, halfword boundaries, clamps, empty/
  negative best times, timer gates/caps and wrapping subtraction.
- Six deliberate guest byte-alias patterns test captured goal, event chains,
  best/total outputs changing maximum, elapsed/best overlap and total output
  changing the timer. Signed negative/outlying actor IDs have explicitly
  mapped guest address ranges; these are not valid native array claims.
- Execute **208 target words**. Words34/84 are bypassed retail duplicates;
  words130/136 are break7/break6. Preserve all212 in byte/mutation checks.
  Reject six crossing zero-divisor cases at DIV before inventing quotient or
  hardware trap state; compare the already-performed memory/trace prefix.
  Signed-overflow DIV cannot occur with a sign-extended16-bit dividend and
  an8-bit nonzero divisor. No native zero-divisor crossing is executed.
- **72,867 native32 cases per O2/O0 UBSan profile** link the actual semantic
  C selector and exercise all65,536 tick halfwords. Use valid separate typed
  record/route/global objects and actor indices0..3. Compare all132 record
  bytes, all4096 table bytes, global gates, best/total arrays and signed
  return. Compare NaN class, not payload, across native platforms.
- **Thirteen observable guest controls /ten native controls** reject wrong
  wrapping, selector order/mode, event class, divisor sign, inclusive maximum,
  clamp value, empty-best gate and caps; guest-only controls test event,
  goal and maximum caching. Native controls exit explicit wrong-result23,
  not a crash. The original mode matrix left record mode0 and its clamp case
  never clamped: add nonzero record modes and a genuinely clamping case.
- **Nine independent original/raw/padded main links plus three independently
  linked padded helper bodies** pass144 three-way cases at three placements,
  including HI16/LO16 carry boundaries. Separate accidental synthetic-global
  collisions that zeroed a divisor, while preserving deliberate aliases.
  Neither fixture correction changes C, guards or the first prediction.
- **1,355 access-fault prefixes across24 states** preserve full public/stack
  memory and trace prefixes; normalized/retail full states match. All212 raw
  words, 26 bindings, 88 guard expectations and26 live/frozen input mutations
  fail closed, as do nested historical views. These are bounded instruction
  access tests, not arbitrary native pointer or hardware-fault acceptance.

**36 paired original caller windows** execute all three retail JAL sites
at VA0x15087660/15087730/15088E28. Preserve pointer/float-bit delivery, actual
float doubling at the second site, the first window's F18 spill/reload and
low-byte step store. The third supplies real F20=1.0. Caller parents
`func_15087350` and `func_15088D58` remain production stubs. Window exits
are synthetic test boundaries; no whole-parent/gameplay claim is made.

## First Prediction And Build

Freeze the first complete **3,257,636-byte ELF**, owner and guard successors
before production edits by substituting only the qualified padded owner into
a copied link script. Install the semantic C and88 guard rows, then run:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals that first prediction, with **689 changed bytes =628
target code +25 symbol-table +36 string-table encoding bytes**. No metadata
exclusions. Canonical symbol definitions differ only in target extent12->848;
all6,057 bodies/addresses are audited and no other body changes. Actual owner
and relative bindings equal qualification. Old guard prefix stays byte-for-
byte intact; mechanically format only the88 appended rows' terminators to
predicted CRLF after checking exact row content/prefix/successor hash.
No broad newline normalization. Protected Game data stays **189,088 bytes /
720 owners /zero differences**. Makefile unchanged; no new compiler warning.
The pre-existing duplicate12D630 recipe warning remains.

| Artifact | SHA-256 |
| --- | --- |
| Raw target | 9bfc1a381ef174907ea455041b8cbc71083d2cb46c78169e3c738e70bedd0840 |
| Whole ELF | 285d0b3d53d8d3332d6ecca37d6468d06c99ba08c48d1778bb92c6061cdd40df |
| Owner source | b217d1beb819cb666f43d16d8e449604251cedaccb1670846542ebfc7ffcb506 |
| Guards | 2f534213effe5b5071b57336303029e8a7e7b8f12de2fc8366b51184f0b974ee |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Shared padder/PC16 tests pass **eleven per copy**, both tool smoke checks and
root tools-check pass. Four copies parse as ASCII/Python AST and both pairs
are byte-identical. Standalone mirror head ddbdd16 stays fixed, preserving
all **1,212 previous dirty hashes**, adding only two absent paths for1,214.
No mirror reset/commit, push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,981/4,828 (61.74%)**, **total3,654/5,501
(66.42%)**, Init492/492, Debugger181/181, **1,847 different /zero drift**.
Conversion counts/bytes stay fixed because the false C stub was already
counted converted. README changes only two aggregate matching rows.

## Next Work

Recover **func_15088D58**, **118 words/frame0xA8**, still a false C stub.
VA0x15088D58..0x15088F30, ROM0xB6208..0xB63E0. Complete retail body read;
one aligned JAL found at ROM0xAA98C. Audit that caller before fixing its C
signature. Preserve initial `func_1508855C` index gate, actor/0x84-byte record
lookup, saved S0..S6/F20 lifetimes and initial0.5 coordinate values. Its loop
scans exactly five neighbor bytes for type4, retaining the last eligible
class; a nonzero class advances by real delta1.0 until the scan stops.

Then preserve fraction reset, three vector outputs from `func_15088F30`,
projection helpers, actor position+0x14/+0x18/+0x1C, angular result+0x40 and
halfword rotations+0x76/+0x78/+0x7A. Define valid loop-termination and float-
conversion domains before native qualification. Keep helper and caller
completion distinct. Parent15087350, retained assembly, handwritten150A76F0,
fade gaps and wider Game queues remain open; the matching goal stays active.

Scoped Graphify refresh: **42,508 nodes /82,580 links /4,088 communities**.
Preserve **19,398 nodes from2,972 excluded-but-existing files**. Only three
line-disambiguated UPDATE_LOG heading IDs move; their labels and every other
old ID persist. The new note contributes seven nodes. Target/next definitions
resolve to **L658/L772**. Preserve the original graph in the ignored task
build folder; outputs remain ignored. No full-scan purge or graph-history
rewrite is performed.
