# Y=Z plane interpolation restored directly from C

`func_15185454` now emits all **64 words / 256 bytes directly from C**, with
no frame, relocations, guards, insertions, omissions or alignment tail. It
reuses the 20-byte `ClipVertex` interface and returns the next output vertex.
VA 0x15185454..0x15185554; ROM 0x1B2904..0x1B2A04.

Production Make and an independent Windows-checkout ELF recount establish
**4,011/5,506 (72.85%)** exact C functions, Game **3,338/4,833 (69.07%)**,
zero address drift and 1,495 still different. Init remains 492/492 and Debugger
181/181. The active 75% target is 4,130/5,506: **119 more matches** remain.
Guard and conversion-inventory CSV bytes are unchanged.

## Source shape and behavior

The ratio is `(a->z-a->y) / ((b->y-a->y)-(b->z-a->z))`. The routine
interpolates X, computes one Y value for both Y and Z, interpolates three signed
16-bit attributes with the original binary32 arithmetic and truncation, preserves
the two retained vertex bytes, and returns `out+1` (20-byte stride).

The original 65-word screen assigned Y then copied it into Z, introducing a
reload and 59 word differences. The recovered statement is
`out->y = out->z = a->y + (b->y-a->y)*ratio;`. It emits retail's X/Z/Y store
order and naturally matches all 64 words. An equivalent temporary with Z/Y
stores also matches; reversing the paired stores leaves two differences.
No instruction normalization is used.

There is no aligned direct JAL. The one aligned pointer is at ROM 0x231F58,
VA 0x8008D498, entry 0 of `D_8008D498`. The original ten-word classifier
`func_15185554` tests Y>Z. The restored complete 84-word polygon caller
`func_15185DD4` executes both JALR sites at 0x15185E90 and 0x15185EDC and
consumes the returned cursor.

## Qualification

The target's own Y-Z corpus has 149 endpoint pairs, two stack phases and
three output placements (separate, alias A, alias B): **894 cases / 1,788
executions**. All 64 words execute. Complete memory, register state, saved
GPR/FPR/SP, returned cursor and stores `[0,8,4,12,14,16]` agree between original
and compiled code. The polygon geometry reference is reused at index 0 under
its frozen source fingerprint. It rounds each arithmetic operation independently.

The corpus covers both crossing directions, zero endpoints, dyadic distances
from 2^-8 through 2^12, changing endpoint Z coordinates, X cancellation and
signed-halfword attribute limits. Tests establish a finite, nonzero-denominator
domain with representable attribute conversions; hardware FCSR, NaNs, invalid
conversions and denormal traps are not claimed.

Ten polygon patterns, two stack phases and one negative-count case yield
**21 cases / 42 executions** through the complete original caller and classifier.
Every parent word and both indirect sites execute. Complete vertices, retained
bytes, callback arguments and returned cursor agree, with no external service
models. The independent predicate is Y>Z.

**60 fired access-prefix cases**, two target-code placements and four rebased
table-caller executions pass. Guest access order does not establish portable C
fault behavior or arbitrary partial-overlap clipping.

Native32 O0/O2/O3 each pass **447 cases** with UBSan and float-cast-overflow
sanitization. All three vertices and surrounding canaries are checked. Eight
compiled controls are effective: reversed ratio, negated rather than equal Z,
omitted X interpolation, wrong attribute source, narrowed attribute, missing
third attribute, wrong cursor and changed retained byte. The reverse-ratio
control stays within the representable domain. Layout and field offsets are
compile-time checked.

## Owner, linked image and banking

The complete owner preserves all **31 neighbors and pools**, including the
restored X=Z, X=-Z, X/Y and polygon routines. Actual normal three-command Make
reproduces the independently padded object with no owner diagnostics. The
inherited duplicate generated_12D630 Make-recipe warning remains.

The final ELF matches the independent image prediction literally over **198
changed bytes**, with zero exclusions or metadata-order adjustments. Only target
instructions and symbol extent (12->256) change. All 6,055 other linked bodies
and every function address remain fixed. Protected Game data is exact over
189,088 bytes and 720 owners. The complete 17,446-file predecessor seal has only
the expected source/object/ELF changes before docs.

Seven canonical tests pass in both tools copies, both shared checks pass, and
the installed production suite passes. Tools `424726b` are committed before the
consumer pin. The older mirror's inherited work is preserved and not committed;
nothing is pushed. Scoped 12-file AST refresh retains prior valid nodes and
edge occurrences and archives obsolete stub-return relationships, without LLM
calls, full-corpus extraction or global reclustering.

Production ELF SHA-256:
`b203adbfdbeab8294ca9124d60483b8e8e59afeaa9853ac847290ea1afb7df40`.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_yz_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-yz-plane-interpolation-15185454-match`. Receipts include
`preparation.json`, `runtime-qualification-v3.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`. The focused snapshot contains 982 inputs;
Native/cache seals and final banking records are retained in the same stage.

Next screen: `func_151856A8`, the unfinished Y=-Z interpolator at table index 2.
Qualify its own sign operation, coordinate stores and original caller behavior.
Other private candidates remain uncredited.
