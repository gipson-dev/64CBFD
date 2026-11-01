# Y=-Z plane interpolation restored directly from C

`func_151856A8` now emits all **66 words / 264 bytes directly from C**, with
no frame, relocations, guards, insertions, omissions or alignment tail. The
interface is `ClipVertex *func_151856A8(ClipVertex *a, ClipVertex *b,
ClipVertex *out)`, using the existing 20-byte vertex type.
VA 0x151856A8..0x151857B0; ROM 0x1B2B58..0x1B2C60.

Production Make and an independent Windows-checkout ELF recount establish
**4,012/5,506 (72.87%)** exact C functions, Game **3,339/4,833 (69.09%)**,
zero address drift and 1,494 still different. Init remains 492/492 and Debugger
181/181. The active 75% target is 4,130/5,506: **118 more matches** remain.
Conversion inventory and guard CSV bytes are unchanged.

## Arithmetic and original interface

The ratio is `(a->z+a->y) / ((a->y-b->y)+(a->z-b->z))`. The function
interpolates X and Y, stores Z as the negation of the stored Y, interpolates
three signed 16-bit attributes using binary32 arithmetic and truncation,
preserves the last two vertex bytes, and returns `out+1` (20-byte stride).
Retail reloads the stored Y before neg.s; the selected ordinary C reproduces
this access order without volatile declarations or assembly.

Source assignments X/Y/Z naturally match all 66 words. Moving the Z assignment
before Y produces twelve differences. Guest coordinate stores are X/Y/Z,
followed by three halfword stores: offsets `[0,4,8,12,14,16]`.

There is no aligned direct JAL and one aligned function pointer at ROM
0x231F60, VA 0x8008D4A0, entry 2 of `D_8008D498`. Its original 11-word
classifier `func_151857B0` tests Y<-Z. The complete restored 84-word polygon
caller invokes the interpolator at both original JALR sites, 0x15185E90 and
0x15185EDC, and consumes its returned cursor.

## Behavioral qualification

The target's Y+Z-distance corpus has 149 endpoint pairs, two stack phases and
three output placements (separate, alias A, alias B): **894 cases / 1,788
executions**. All 66 words execute. Complete memory, registers, saved GPR/FPR/SP,
returned cursor and store order agree between original and compiled code. The
frozen polygon geometry reference rounds each operation independently at table
index 2; the guest neg.s model flips the float sign bit.

The corpus covers both crossing directions, zero endpoints, dyadic distances
from 2^-8 through 2^12, changing Z coordinates, cancellation-prone X values and
signed attribute limits. This is a finite, nonzero-denominator domain with
representable attribute conversions. Hardware FCSR, NaNs, invalid conversions
and denormal-trap behavior are not established.

Ten polygon patterns, two stack phases and a negative-count case give **21
cases / 42 executions** through the entire original caller and classifier.
Every parent word and both indirect sites execute. Complete vertices, retained
bytes, callback arguments and returned cursor agree, without external service
models. The independent predicate is Y<-Z.

**63 fired access-prefix cases**, two target-code placements and four rebased
table-caller executions pass. Guest access ordering does not establish portable
C fault behavior or arbitrary partial-overlap clipping.

Native32 O0/O2/O3 each pass **447 cases** with UBSan and float-cast-overflow
sanitization. Every byte in all three vertices and surrounding canaries is
checked, including both legal output aliases. Eight compiled controls are
effective: reversed ratio, positive rather than negated Z, omitted Y, wrong
attribute source, narrowed attribute, missing third attribute, wrong cursor
and changed retained byte. The reverse-ratio control remains within the
representable domain. The vertex layout and attribute offsets are compile-time
checked.

## Owner, complete image and banking

Complete-owner compilation preserves all **31 neighbors and pools**, including
the restored Y=Z, X=Z, X=-Z, X/Y and polygon routines. The actual normal
three-command Make recipe reproduces the independently padded object without
owner diagnostics. The inherited duplicate generated_12D630 recipe warning
remains. A copied preparation-driver field name was corrected from ELF_SHA264
to ELF_SHA256 before evidence fingerprinting; the original receipt is retained,
and the unchanged 64-hex-digit hash was checked against the complete ELF.

The production ELF literally matches the independent prediction across **204
changed bytes**, with zero exclusions or metadata-order adjustments. Only target
instructions and symbol extent (12->264) change. All 6,055 other linked bodies
and every function address stay fixed. Protected Game data is exact across
189,088 bytes and 720 owners. The complete 17,455-file predecessor seal has
only the expected source/object/ELF changes before docs.

Seven canonical checks pass in both tools copies, both shared checks pass,
and the installed production suite passes. Tools `a410754` are committed before
the consumer pin. The older mirror's inherited changes are preserved and not
committed; nothing is pushed. Scoped 12-file AST refresh retains prior valid
nodes and edge occurrences and archives obsolete stub-return relationships;
no LLM calls, full-corpus extraction or global reclustering are claimed.

Production ELF SHA-256:
`2a7d208da964f6608bf94a5c438e85e9d5e6c8a65f0218ee4c85550975efbcaf`.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_negative_yz_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-negative-yz-plane-interpolation-151856A8-match`.
Receipts include `preparation.json`, `runtime-qualification-v3.json`,
`production-v17.json`, `production-seal-changes-v17.json`, `installed-audit.json`
and `native-production-recount.txt`. There are 982 focused inputs; Native/cache
seals and final banking records are retained in the same stage.

Next screen: `func_151858FC`, the unfinished depth-plane interpolator at table
index 4. Qualify its live depth constant, relocation bindings, arithmetic and
original caller behavior. Other private candidates remain uncredited.
