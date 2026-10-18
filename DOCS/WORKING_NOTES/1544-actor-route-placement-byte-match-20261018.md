# Actor Route Placement Byte Match

Date: 2026-10-18. Consumer predecessor **2316661f**, tools predecessor
**64c3a9f**. Tools banked first as **0d4af42**. Restore **func_15088D58**,
owner `generated_B3020`, VA **0x15088D58..0x15088F30**, ROM
**0xB6208..0xB63E0**. This completes one function; the wider goal stays active.

## Semantic Recovery

Replace the zero-return placeholder with **void(u8 *actor)**. Keep its address
name and a concise semantic comment. The sole aligned retail JAL at ROM
0xAA98C/VA0x1507D4DC supplies S0 in the delay slot and ignores the result.
There is no invented C return value or non-void fallthrough. Retail's volatile
V0 still agrees after guarded normalization; no semantic word-return contract
is assigned from an unused register result.

Call already-matched `func_1508855C` for an index; negative results exit
without public writes. Otherwise capture the indexed0x84-byte record through
D_800872A0 and initialize floats+0/+4/+8 to0.5. Each iteration reloads the
route table D_800D2350, reads the current neighbor byte+0x2C and scans exactly
five candidate IDs at route+9..+0xD. Skip0xFF and non-type4 candidates. Every
eligible class byte+0xF overwrites the selection, including zero: this is the
**last eligible class**, not first eligible or last nonzero class.

A nonzero final class calls the real `func_15088A08(record,1.0f)` and repeats
the scan using the new neighbor state. Qualification supplies terminating
routes and nonzero progress divisors; it does not silently bound a production
loop. Preserve the saved S0..S6/F20 lifetimes, F20's1.0 value across calls,
frame0xA8 and original private vectors/slopes. No unused padding is installed.

Reset fraction+8 to0 before `func_15088F30(record,x,y,z)`. Pass each vector
to the appropriate cubic helper with integer index0 and freshly loaded float
fraction bits. Store actor positions+0x14/+0x18/+0x1C in order. Guest actor/
record overlap can change fraction between these stores; do not cache it.
Call atan with record floats+0x10/+0xC and zero third argument, add0x8000 to
the unsigned16-bit result, convert to float and multiply by exact180/32768.
Normalize with `func_15144BC8`; strict greater-than360 preserves exact360.
Store actor heading+0x40, then load D_8009DA04, multiply, truncate and subtract
0x4000. Store the low halfword at+0x7A/+0x78/+0x76 in that order.

## Three Guard Normalization

The selected C emits **118 words/frame0xA8**, with correct save/restore order,
private vectors at SP+0x88/+0x78/+0x68 and slope destinations+0x9C/+0x98.
All14 relative bindings and floating operations already agree. Source uses
direct indexed candidate fields and early rotation/heading declarations;
no Makefile or compiler-profile edit is installed. B3020 retains its existing
O2/g3/MIPS2/o32 compiler-only no-unroll profile.

Only **three expected-word guards** are appended. Word40 exchanges symmetric
BEQ source operands. Words101/103 give the float-to-integer result a short
T5 lifetime before the existing ADDIU writes final V0, instead of using V0
for both. No opcode, branch displacement, schedule, delay, memory operation,
frame, FPR, inserted/omitted word or helper binding changes. This is a guarded
match, not direct/guard-free compilation. Raw dead-T5 fault states are not
claimed equal; normalized/retail complete bounded states are exact.

## Qualification

New tools: `experiments/game_actor_route_snap.py` and
`tests/test_game_actor_route_snap.py`. Ignored artifacts:
`conker/build/game-actor-route-snap/`. Fifteen fingerprints cover the declared
owner/ELF/guard/ROM, assembly/caller, Makefile/symbol/header and prepared IDO
closure, not every unlisted dependency. Strict predecessor views remain
serial and non-nesting. No older fixture, guard or dependency is weakened.

All **seven pre-install tests pass in109.930s**, and all **seven installed
tests pass in125.850s**:

```sh
python3 -m unittest tools.tests.test_game_actor_route_snap -v
```

- **3,890 three-way raw/normalized/retail guest cases** compare all public
  bytes, ordered public traces, semantic call boundaries and saved ABI state.
  Execute **all118 target words** and **555 connected retail-helper words**:
  lookup36, progress212, selector88, vectors83, cubic49, derivative62, wrap25.
  The sole bounded provider returns a validu16 atan result and clobbers
  caller-saved registers, FPRs and argument-home words.
- Cover all **1,024** sentinel/type3/type4-zero/type4-nonzero categories at
  five positions in both modes, signed mode128, zero/one/multiple/31-step
  routes, four actor slots, null/missing/negative-count lookup gates, strict
  angle-wrap boundaries, finite positive/negative/zero scales and actor/
  record aliases. Native objects do not reuse those guest aliases.
- **69,414 native32 cases per O2/O0 UBSan profile**, including all65,536 atan
  return values, compare complete typed actors, records, route table, score
  arrays, gates and helper counts. Execute the frozen owner's real semantic
  C progress and selector; progress has a transparent counting wrapper.
  Lookup/vector/spline/atan/wrap providers are bounded typed models, not a
  claim that every production helper is converted. Distinct valid native
  actor/record/route objects avoid incompatible object/alias domains.
- **Eleven guest /ten native observable controls** reject wrong type/scan
  length/class priority, one-step-only loops, initial fractions, vector order,
  angle bias/scale and rotation outputs. Guest-only cached fraction fails on
  an actual actor/record alias. Native controls exit wrong-result23, not a
  crash. Guest controls are independently linked at a private code placement
  with their read-only pools: larger controls previously overlapped an
  adjacent retail helper, and a changed float scale introduced a literal pool.
  Fix the harness, not the recovered C or frozen prediction.
- **Nine independent original/raw/padded main links plus21 independent helper
  links** pass **96 three-way rebased cases**, including independent globals,
  helper placements and HI16/LO16 carry boundaries. All14 main bindings and
  all seven helper bodies are covered.
- **1,608 access-fault prefixes across eight connected states** preserve
  public/stack memory and trace prefixes; normalized/retail complete states
  match. Five nonfinite/out-of-range conversions stop before TRUNC with equal
  performed-store prefixes. Do not invent FCSR, indefinite integers or native
  undefined-conversion behavior. Earlier progress qualification separately
  covers its zero-divisor boundary; new valid crossing cases use divisor3.
- All118 raw words, 14 bindings, three guard expectations, **30 live/frozen
  input mutations** and nested predecessor views fail closed. Earlier
  unchanged neighbor-suite receipts are reused only with matching raw owner/
  pool/binding fingerprints, not reported as freshly rerun broad suites.

**48 paired original retained-caller windows** run the actual JAL/delay and
caller epilogue at0x1507D4DC..0x1507D4F8. Verify actor-pointer delivery,
callee-saved state, both stack phases and gate/angle/step cases. The complete
**800-byte func_1507D1D8** parent slot also remains retail-exact. This is
bounded caller execution, not the complete parent's gameplay acceptance.

## Prediction And Build

Freeze the first complete **3,257,636-byte ELF**, source and guard successors
before production edits by substituting only the qualified padded owner into
a copied link script. Install the complete C body and three guard rows:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_B3020.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals that first prediction: **402 changed bytes =362 target
code +19 symbol-table +21 string-table encoding bytes**. Zero metadata
exclusions. Canonical definitions change only target extent12->472; all6,057
function addresses and every other body remain fixed. All72 raw owner
neighbors, pools and relative bindings remain fixed, and the actual padded
owner equals qualification. Preserve every byte of the old guard prefix;
mechanically format only the three appended rows' terminators to predicted
CRLF after exact row/prefix/successor-hash checks. No broad normalization.
Makefile unchanged; protected Game data stays **189,088 bytes /720 owners /
zero differences**. No new compiler diagnostic; the existing duplicate12D630
recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw target | e5095217500b82349000ff9e2aa2ab853d8e954f9d26471ec8f29c26a0f88fde |
| Whole ELF | a5c5541dc8f6863ebefac2896237ce0bc39a88e3893711c35cd0393fd851ecd7 |
| Owner source | ce0cf9b5504e5b41b267c09d69c3bdc9ed2f24533ed7de0dd68935bd678f467f |
| Guards | eb4dc7f42da17c278c908b8e5ab721c4b420edd2210b4a691c343b8aa0fcfd42 |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Shared padder/PC16 tests pass **eleven per copy**, both smoke checks and root
tools-check pass. Four task copies parse as ASCII/Python AST and both pairs
are byte-identical. Older mirror head ddbdd16 stays fixed: preserve all
**1,214 previous dirty hashes**, adding only two absent paths for1,216. No
mirror commit/reset, push, Claude call, host or frozen Release action.

Fresh official totals: **Game2,982/4,828 (61.76%)**, **total3,655/5,501
(66.44%)**, Init492/492, Debugger181/181, **1,846 different /zero drift**.
Conversion counts/bytes stay fixed because the old false C stub was already
counted converted. README changes only its two aggregate matching rows.

## Next Work

Recover **func_15088F30**, **83 words/frame0x10**, still a false C stub.
VA0x15088F30..0x1508907C, ROM0xB63E0..0xB652C. Complete retail body read.
Aligned JALs occur at ROM0xB4964/B4BF4/B4E04/B4E4C/B6308. No exact pointer/J
word found; computed or encoded references remain possible. Recover its four
pointer parameters, then update the parent's local unprototyped helper
declaration, requiring unchanged raw118-word parent and all its bindings.

Process record neighbor bytes+0x2B..+0x2E. For each non-FF ID, reload the global
route table, select the first type4 neighbor if present, otherwise the route
itself. Interpolate signed-halfword x/z coordinates with repeated record
float+0 reads and store signed y as float, preserving x/y/z order. FF slots
produce `(slot*64,0,0)`. Saved S0/S1 and frame0x10, byte/halfword sign, four
output increments and table/record/output alias boundaries need qualification.

Vector83 and cubic49/derivative62 helpers remain production stubs. The guest
suite overlays their real retail instructions for qualification; the current
production C call chain and full gameplay are not claimed complete. Their
test-only semantic models are useful references, not already installed or
independently byte-matched C. Parent15087350, retained assembly, handwritten
150A76F0, fade gaps and wider Game queues remain open; the goal stays active.

Scoped Graphify refresh: **42,517 nodes /82,591 links /3,977 communities**.
Preserve **19,398 nodes from2,972 excluded-but-existing files**. Only three
line-disambiguated UPDATE_LOG heading IDs move; their labels and every other
old ID persist. The new note contributes seven nodes. Target/next definitions
resolve to **L773/L832**. Preserve the original graph in the ignored task
build directory; outputs remain ignored. No full-scan purge or history rewrite.
