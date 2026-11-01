# X=-Z plane interpolation restored directly from C

`func_1518557C` now emits all **64 words / 256 bytes directly from C**, with
no frame, relocations, guards, insertions, omissions or alignment tail. Its
interface is `ClipVertex *func_1518557C(ClipVertex *a, ClipVertex *b,
ClipVertex *out)`. It reuses the existing 20-byte vertex type without moving it.

Production Make and an independent recount of the Windows checkout ELF establish
**4,010/5,506 (72.83%)** exact C functions, Game **3,337/4,833 (69.05%)**,
zero address drift and 1,496 still different. Init remains 492/492 and Debugger
181/181. The active 75% target is 4,130/5,506: **120 more matches** remain.
Conversion inventory and guard CSV bytes are unchanged.

## Arithmetic and table contract

VA 0x1518557C..0x1518567C; ROM 0x1B2A2C..0x1B2B2C. The ratio is
`(a->z+a->x) / ((a->x-b->x)+(a->z-b->z))`. The function interpolates X and Y,
sets Z to the negation of the interpolated X, interpolates three signed 16-bit
attributes using the original binary32 arithmetic and truncation, preserves
the last two vertex bytes, and returns `out+1`. The negated coordinate retains
the exact plane constraint, including the guest sign-bit operation.

The selected source assigns X/Y/Z in that order. Retail IDO schedules its
coordinate stores X/Z/Y and emits the original neg.s. Moving the source Z
assignment before Y instead produces nine word differences. The selected
complete semantic C naturally matches all 64 words without normalization.

There is no aligned direct JAL and one aligned function pointer at ROM 0x231F5C,
VA 0x8008D49C: entry 1 of `D_8008D498`. Its original 11-word classifier,
`func_1518567C`, tests X<-Z. The restored 84-word polygon caller invokes it
through both original JALR sites, 0x15185E90 and 0x15185EDC, and uses the
interpolator's returned cursor.

## Guest, native and caller evidence

A newly adapted X+Z-distance corpus covers 149 endpoint pairs, two stack phases
and three output placements (separate, alias A, alias B): **894 cases / 1,788
executions**. All 64 target words execute. Original and compiled programs agree
on complete memory, registers, saved GPR/FPR/SP, returned cursor and stores
`[0,8,4,12,14,16]`. The frozen polygon geometry oracle independently rounds the
ratio/interpolation operations for table index 1. The local guest model handles
neg.s by flipping the float sign bit and bounds trunc.w.s to finite int32.

Endpoint equality, both crossing directions, power-of-two distances from 2^-8
through 2^12, changing Z coordinates, Y cancellation and full signed-halfword
attribute limits are covered. This is a finite, nonzero-denominator domain
with representable attribute conversions. It does not establish hardware FCSR,
NaN, invalid-conversion or denormal-trap behavior.

Ten polygon patterns, two stack phases and a negative-count case give **21
cases / 42 executions** through the complete original caller and classifier.
All 84 parent words and both indirect sites execute. Complete copied vertices,
retained bytes and returned output cursor agree; no service model replaces the
original routines. The reference predicate is independently X<-Z.

There are **57 fired access-prefix cases** and two independently linked target
placements with four rebased table-caller executions. These establish guest
access-order agreement and do not claim portable C fault behavior or arbitrary
partial-overlap clipping.

Native32 O0/O2/O3 each pass **447 cases** with UBSan and float-cast-overflow
sanitization. All three vertices and surrounding canaries are compared for each
output placement. Eight compiled controls are effective: reversed ratio,
positive rather than negated copied Z, omitted Y, wrong attribute source,
narrowed attribute, missing third attribute, wrong cursor and changed retained
byte. The reversed-ratio control stays within the representable interpolation
domain. The whole 20-byte vertex layout and attribute offsets are compile-time
checked in the native harness.

## Owner, literal image and banking

Complete-owner compilation preserves all **31 neighbors and pools**, including
the restored X=Z, X/Y and polygon routines. The actual normal three-command Make
recipe reproduces the independently padded object without owner diagnostics.
The pre-existing duplicate generated_12D630 Make-recipe warning is retained.

The full production ELF matches the independent prediction literally over
**198 changed bytes**, with zero exclusions and no metadata-order adjustments.
Only the target instructions and target symbol extent (12->256) change. Every
function address and all 6,055 other linked bodies stay fixed. Protected Game
data is exact across 189,088 bytes and 720 owners. The entire 17,437-file
predecessor seal has only the expected source/object/ELF changes before docs.

Seven fresh canonical checks pass in both tools copies. Both shared checks and
the installed production suite pass. Tools `baae2d0` are committed before the
consumer pin. The older mirror's inherited work is preserved and not committed;
nothing is pushed. A scoped 12-file AST refresh retains prior valid nodes and
edge occurrences and archives obsolete stub-return relationships, without
full-corpus extraction, LLM calls or global reclustering.

Production ELF SHA-256:
`dcd7e07b2a16d22330f4cadefff7eb2f8e873c7254189addcfb54e2fee9cf1a7`.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_negative_xz_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-negative-xz-plane-interpolation-1518557C-match`.
Receipts include `preparation.json`, `runtime-qualification-v3.json`,
`production-v17.json`, `production-seal-changes-v17.json`, `installed-audit.json`
and `native-production-recount.txt`. The focused snapshot contains 982 inputs;
Native/cache seals and final banking records are retained in the same stage.

Next screen: `func_15185454`, the unfinished Y=Z interpolator at table index 0.
Qualify its own arithmetic, coordinate-copy order and original caller behavior.
Other private candidates remain uncredited.
