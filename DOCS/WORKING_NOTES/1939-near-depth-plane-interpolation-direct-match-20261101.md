# Near depth-plane interpolation restored directly from C

`func_15185A28` emits all **64 words / 256 bytes and both depth-address
relocation bindings directly from C**, with no frame, guards, insertions,
omissions or alignment tail. VA 0x15185A28..0x15185B28; ROM 0x1B2ED8..0x1B2FD8.
It uses the existing 20-byte `ClipVertex` interface and returns `out+1`.

Production Make and an independent Windows-checkout ELF recount establish
**4,014/5,506 (72.90%)** exact C functions, Game **3,341/4,833 (69.13%)**,
zero drift and 1,492 still different. Init remains 492/492 and Debugger 181/181.
The active 75% target is 4,130/5,506: **116 more matches** remain.
Guard and conversion-inventory CSV bytes are unchanged.

## Arithmetic, loads and bindings

The ratio is `(D_800D368C-a->z)/(b->z-a->z)`. The function interpolates X/Y,
loads `D_800D368C` again for output Z, interpolates three signed-halfword
attributes with binary32 arithmetic and truncation, preserves two retained bytes,
and returns the next 20-byte vertex. It emits X/Y/Z stores, followed by the
three halfword stores: offsets `[0,4,8,12,14,16]`.

Both ordinary global accesses and an explicit pointer candidate match the
complete original routine. The ordinary source is selected. Unresolved raw
object words and binding identities match the original assembly object. The
bindings are offset 0 `R_MIPS_HI16:D_800D368C` and offset 4
`R_MIPS_LO16:D_800D368C`; the linked image separately matches retail addresses.
Raw-object and retail-linked hashes are kept distinct in the verifier.

There is no aligned direct JAL. The aligned pointer at ROM 0x231F6C,
VA 0x8008D4AC, is table index 5 in `D_8008D498`. Its original 11-word classifier,
`func_15185B28`, tests `Z < D_800D368C`. The complete 84-word polygon caller
executes both original JALR sites, 0x15185E90/0x15185EDC, and consumes the
returned interpolation cursor.

## Guest, native and relocation qualification

The target has 212 endpoint/plane combinations, two stack phases and three
output placements (separate, alias A, alias B): **1,272 cases / 2,544 executions**.
All 64 words execute. Complete memory, registers, saved GPR/FPR/SP, output order
and cursor agree with original code and the frozen rounded geometry reference.
Depth values include negative, positive and both signed zeros; crossings cover
both directions, zero endpoints, dyadic distances and signed attribute limits.

Six additional cases model an external change to the depth value after the
first output store and before its second global load. Ratio arithmetic uses
the old value; output Z uses the new negative-zero bit pattern. All output
placements and both stack phases pass, with both global reads observed.
This is an explicitly injected guest event, not evidence of real concurrent
gameplay or a C threading contract.

Ten polygon patterns across four plane values and two stack phases, plus one
negative-count case, give **81 cases / 162 executions** through the original
classifier and complete polygon caller. Every parent word and both sites are
reached; complete retained vertices, calls and cursors agree, with no service
models. The predicate reference independently compares Z with the plane value.

There are **60 fired access-prefix cases**, two independent code placements
with four table-caller executions, and two separate code/global placements with
12 root executions. Global rebases at 0x31008000 and0x3200FFFC exercise signed
low-16 carries and both relocation bindings. The complete-caller tests keep the
original classifier's depth address at retail; independent global rebases are
qualified at the target root. Arbitrary overlap and portable C faults are not
claimed.

Native32 O0/O2/O3 each pass **636 cases**, supplying the actual depth global per
case, with UBSan and float-cast-overflow sanitization. All three vertices and
canaries are checked. Eight compiled controls are effective: reversed ratio,
negated output depth, omitted Y, wrong attribute source, narrowed attribute,
missing third attribute, wrong cursor and changed retained byte. The domain is
finite with nonzero denominators and representable attribute conversions;
hardware FCSR, NaNs, invalid conversions and denormal traps remain outside it.

## Complete owner, image and banking

All 31 neighboring functions and pools stay fixed. Actual normal three-command
Make reproduces the independently padded owner object without owner diagnostics.
The inherited duplicate generated_12D630 recipe warning remains.

The production ELF matches the independent full-image prediction literally
across **195 changed bytes**, with zero exclusions or metadata-order changes.
Only target instructions and symbol extent 12->256 change. All 6,055 other bodies
and every address stay fixed. Protected Game data is exact over 189,088 bytes
and 720 owners. The 17,473-file predecessor seal has only expected source/object/
ELF differences before documentation.

Seven fresh canonical checks pass in both tools copies; both shared checks and
the installed production suite pass. Tools `8b6940f` are committed before the
consumer pin. The independently dirty mirror is preserved; nothing is pushed.
A scoped 12-file AST refresh retains prior valid nodes and edge occurrences,
archives obsolete stub-return edges and uses no LLM or global reclustering.

Production ELF SHA-256:
`d3455d627d30e8555a2d7aca6c4132104a9090ba0f9753941aa2a8454de5ea1f`.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_near_depth_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-near-depth-plane-interpolation-15185A28-match`.
Receipts include `preparation.json`, `runtime-qualification-v3.json`,
`production-v17.json`, `production-seal-changes-v17.json`, `installed-audit.json`
and `native-production-recount.txt`. There are 982 focused inputs; final banking
and Native/cache seals are retained in the same stage.

## Plane callback family closure

A fresh production audit checks all 18 distinct callbacks: eight interpolators
and ten classifiers, totaling 608 original instruction words. All 18 have semantic
C bodies in the conversion inventory, and every linked instruction matches the
original assembly words. The audit uses a local return-type spelling adaptation
for the existing span parser, which accepts void pointers but not ClipVertex
pointers; production source is unchanged. See `all-plane-callbacks-v10.json`.
The larger outer routine `func_15185F24` remains unfinished.

Next screen: `func_150495B0`, the unfinished scalar position/velocity smoothing
and overshoot-clamp routine in generated_76A60. Qualify its six-argument o32 ABI,
sign branches, update order, aliases and actual caller behavior before adoption.
Other private candidates remain uncredited.
