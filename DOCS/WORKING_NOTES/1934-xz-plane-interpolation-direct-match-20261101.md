# X=Z plane interpolation restored directly from C

`func_151857DC` now emits all **62 words / 248 bytes directly from C**, with
no frame, relocations, guards, insertions, omissions or alignment tail.
Its interface is `ClipVertex *func_151857DC(ClipVertex *a, ClipVertex *b,
ClipVertex *out)`. The existing 20-byte vertex type moves above this earlier
routine; it is shared with the restored X/Y helpers and polygon caller.

Production Make and an independent recount of the Windows checkout ELF establish
**4,009/5,506 (72.81%)** exact C functions, Game **3,336/4,833 (69.03%)**,
zero address drift and 1,497 still different. Init remains 492/492 and Debugger
181/181. The active 75% target is 4,130/5,506: **121 more matches** remain.
Conversion inventory and guard CSV bytes are unchanged.

## Arithmetic and callback contract

VA 0x151857DC..0x151858D4; ROM 0x1B2C8C..0x1B2D84. The interpolation ratio is
`(a->z-a->x) / ((b->x-a->x)-(b->z-a->z))`. It interpolates X and Y, copies the
resulting X bit pattern into Z, interpolates three signed 16-bit attributes
with the original binary32 arithmetic and truncation, preserves the last two
vertex bytes, and returns `out+1`. Z is deliberately copied rather than
independently interpolated, preserving the plane constraint exactly.

The selected source assigns X/Y/Z in that order; retail IDO schedules the
actual coordinate stores X/Z/Y. Changing source order to X/Z/Y produced eight
word differences. The complete XYZ source naturally matches all 62 words.
There is no inline assembly or word normalization in this recovery.

The aligned ROM census has no direct JAL and one function pointer at ROM
0x231F64, VA 0x8008D4A4: entry 3 of `D_8008D498`. Its original classifier
`func_151858D4` implements X>Z in ten words. The complete 84-word polygon caller
`func_15185DD4` invokes it through both original JALR sites at 0x15185E90 and
0x15185EDC and consumes its returned cursor.

## Guest, native and caller qualification

The guest suite uses 149 endpoint pairs, two stack phases and three output
placements (separate, alias A, alias B): **894 cases / 1,788 executions**.
All 62 words are reached. Complete memory, register state, saved GPR/FPR/SP,
return cursor, and actual store order `[0,8,4,12,14,16]` agree between original
and newly compiled code. The rounded geometry reference is reused from the
qualified polygon oracle under its frozen input fingerprint.

Distinct X-Z distances include zero endpoints, both crossing directions,
powers from 2^-8 through 2^12, changing endpoint Z values, cancellation-prone Y
coordinates and signed attributes including full halfword limits. The domain
is finite with nonzero denominators and representable attribute conversions;
hardware FCSR, NaNs, invalid conversions and denormal traps are not claimed.

Ten polygon patterns, two stack phases and a negative-count case give
**21 cases / 42 executions** through the complete original caller and classifier.
All 84 parent words and both JALR sites are reached. Whole retained vertices,
including their tail bytes, and the returned output cursor agree. No external
service model replaces either original routine. Classification is independently
computed as X>Z, without depending on unrelated far/near depth globals.

There are **57 fired access-prefix cases**, plus two independent target-code
placements with four rebased table-caller executions. These qualify guest
instruction access order and do not assert portable C fault semantics or
arbitrary partial-overlap behavior.

Native32 runs **447 cases per profile at O0/O2/O3**, with UBSan and the
float-cast-overflow sanitizer. All three vertices and surrounding canaries are
checked, including both legal output aliases. Eight compiled controls are
effective: reversed ratio, negated copied Z, omitted Y, wrong attribute source,
narrowed attribute, missing third attribute, wrong returned cursor and a changed
retained byte. The reversed-ratio control remains within the interpolation
domain to avoid relying on undefined out-of-range conversion behavior.

## Owner, image and banking

Complete-owner compilation preserves all **31 neighbors and pools**, including
the previously restored X/Y helpers and polygon caller after moving the type.
The actual normal three-command Make recipe reproduces the independently padded
object with no owner diagnostics. The inherited duplicate generated_12D630
Make-recipe warning remains; a warning-free complete build is not claimed.

The production ELF exactly matches the independent full-image prediction over
**190 changed bytes**, with zero exclusions or symbol-order adjustments. Only
the target code and target symbol extent (12->248) change. All 6,055 other
linked bodies and every function address remain fixed. Protected Game data is
exact across 189,088 bytes and 720 owners. The entire 17,428-file predecessor
seal has only the expected source/object/ELF changes before documentation.

Seven fresh canonical checks pass in both tools copies; both shared tool checks
and the installed production suite pass. Tools `3912ea7` are committed before
the consumer pin. The older mirror's inherited edits are preserved and not
committed. Nothing is pushed. Scoped 12-file AST refresh retains every prior
valid node and edge occurrence and archives the obsolete stub-return edges;
it makes no full-corpus extraction or global reclustering claim.

Production ELF SHA-256:
`89118642417bffc0ce0de6378af49cebb62b407f7156a6913d30c65c40c5dde5`.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_xz_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-xz-plane-interpolation-151857DC-match`. Receipts include
`preparation.json`, `runtime-qualification-v3.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`. Native/cache seals and final banking records
are retained there. The focused snapshot contains 982 input files.

Next screen: `func_1518557C`, the 64-word X=-Z interpolator in table entry 1.
The neighboring X>Z classifier already has a semantic C body; the new target
still has a zero-return placeholder and needs its own arithmetic and caller gates. Existing private candidates remain uncredited.
