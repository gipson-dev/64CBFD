# Y-plane vertex interpolation restored directly from C

`func_15185C6C` now emits all **60 retail words directly from C**, with no
frame, relocations, guards, insertions, omissions or trailing alignment words.
It reuses the private `ClipVertex` layout already qualified by
[Note 1931](1931-x-plane-interpolation-direct-match-20261031.md); the owner
contains one typedef, and the X-plane routine is unchanged.

Production Make and an independent recount against the Windows consumer ELF
establish **4,007/5,506 (72.78%)** exact C functions, Game **3,334/4,833
(68.98%)**, zero address drift and 1,499 still different. Init remains 492/492
and Debugger 181/181. Guard and conversion-inventory CSV bytes remain fixed.
The active 75% target is 4,130/5,506: **123 more matches** remain.

## Source and original callers

VA 0x15185C6C..0x15185D5C; ROM 0x1B311C..0x1B320C. The recovered signature is
`ClipVertex *func_15185C6C(ClipVertex *a, ClipVertex *b, ClipVertex *out)`.
The routine computes `ratio = a.y / (a.y - b.y)`, publishes positive zero to
output Y, interpolates X/Z and the three signed halfword attributes, retains
the final two bytes, and returns `out+1` with a 20-byte stride. The exact
store order is +4/+0/+8/+0xC/+0xE/+0x10.

The aligned input census has no direct JAL and two function pointers at
ROM 0x231F78/0x231F7C, VA 0x8008D4B8/0x8008D4BC. These are interpolation
table `D_8008D498` slots 8/9. Their classifier slots in `D_8008D4C0` select
`func_15185DAC` (Y>0) and `func_15185D5C` (Y<=0). That predicate order differs
from the X-plane pair and is explicitly reflected in this target's fixtures.

The complete original 84-word `func_15185DD4` executes through both JALR sites
at 0x15185E90 and 0x15185EDC, with output S1 supplied as A2 in the delay slot.
The original parent consumes returned V0 as a vertex cursor and copies whole
20-byte vertices, including retained bytes. Forty-two caller cases / 82
executions cover all 84 parent words, both original ten-word classifiers,
both table indices, all transition paths, and positive, empty and negative
counts. There are no external service models in these executions.

These are original parent instructions used for qualification. The parent's
existing production C stub is preserved and is not credited by this adoption.

## Fresh Y-axis qualification

The source screen matched immediately. Complete-owner compilation reproduces
the isolated payload, emits no diagnostics, and preserves all 31 neighboring
functions and pools, including the banked X-plane body.

The independent rounded reference uses Y for the crossing denominator, writes
output Y first, and interpolates X/Z. Serialized X/Y coordinate fields are
swapped when adapting the root input corpus; vertex layout, signed attributes
and retained bytes are unchanged. The polygon fixture varies Y, and the
original classifiers and table entries provide the independently observed
dispatch behavior.

Fresh guest tests pass 894 cases / 1,788 executions over both supported stack
phases and output separate from, aliasing A, or aliasing B. All 60 words are
reached. Store order, complete memory, untouched retained bytes, returned
cursor, SP and callee-saved GPR/FPR state agree. Fifty-four fired access-prefix
cases also agree. Two independent code placements are called through test
table entries by the original parent in eight further executions. The target
has no relocation bindings; these checks exercise indirect dispatch rather
than asserting nonexistent HI16/LO16 relocations.

Native32 O0/O2/O3 each pass 447 cases with UBSan and the float-cast-overflow
sanitizer. The 20-byte type, attribute and retained-byte offsets are asserted;
all three vertices' bytes and surrounding canaries are compared. Eight
effective compiled controls cover reversed ratio, wrong zeroed axis, omitted
X interpolation, wrong/narrowed attribute, omitted third attribute, old cursor
return and retained-byte corruption. Each source replacement is checked to
produce a distinct changed body.

The numerical domain is finite opposite-side or endpoint coordinates, a
nonzero denominator and representable signed-halfword conversion results.
NaN/infinite coordinates, invalid conversions, FCSR flags and denormal traps
are outside the modeled hardware claims. Fault-prefix evidence does not
establish portable C fault behavior. A copied private stage path was fixed
before runtime qualification; candidate source and instruction identity did
not change.

## Production image and banking

The normal three-command generated-owner Make recipe matches the independently
padded object. All 240 payload-byte corruptions, one injected relocation and
two owner/function scope changes are rejected by the qualification guards.
Seven fresh target tests pass in both tools copies, both shared tool checks
pass, and the installed production suite passes.

The literal whole-image prediction agrees with production: **182 changed
bytes**, confined to the target and its symbol extent 12->240, with no
metadata adjustment, exclusions or masks. All 6,055 other linked bodies and
all addresses remain fixed. Protected Game data is exact across 189,088 bytes
and 720 owners. The entire 17,410-file predecessor seal has only expected
target source, target object and ELF differences, with no unplanned dependent
object changes.

Production ELF SHA-256:
`16fbd460baf2f940cd902c41ab76754220d15a5148ad63c4b0717d8562f8b00d`.

Tools `3ad93ca` bank qualification before the consumer pin. The older tools
mirror's inherited work remains preserved and uncommitted. Nothing is pushed.
Scoped Graphify refresh retains prior valid nodes and edge occurrences and
archives the obsolete placeholder return relationship with provenance; no
full-corpus extraction or global reclustering is claimed.

Reproduction with prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_y_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-y-plane-interpolation-15185C6C-match`. Receipts include
`preparation.json`, `runtime-qualification-v4.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`. Complete current Native/cache seals and final
banking proofs are retained with the stage.

Next screen: `func_15185DD4`, the 84-word polygon caller in this owner. Reuse
the vertex and callback ABI evidence from both interpolation recoveries,
while qualifying the full table's contracts and count/address arithmetic
before installing its C body. Other private candidates remain uncredited.
