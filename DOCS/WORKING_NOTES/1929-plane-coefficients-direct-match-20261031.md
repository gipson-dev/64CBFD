# Plane coefficients restored directly from C

`func_15049350` now emits its complete **57-word body and eight relocation
bindings directly from C**, without guards, insertions or omissions. The
complete 60-word retail slot also includes three post-body alignment NOPs.
The recovered declaration is `void func_15049350(PlanePoints points)`;
`PlanePoints` contains three arrays of three `f32` coordinates, passed by value.
The false zero-return stub and stale placeholder comments are removed from
`conker/src/game_76710.c`. No shared layout or header changes are needed.

Actual production Make and an independent recount against the Windows
consumer ELF establish **4,004/5,506 (72.72%)** exact C functions, Game
**3,331/4,833 (68.92%)**, zero address drift and 1,502 still different. Init
remains 492/492 and Debugger 181/181. **126 more** matches are needed to reach
the active 75% target of 4,130/5,506. The conversion inventory and guard CSV
remain byte-identical to the predecessor.

## Geometry and source recovery

The body occupies VA 0x15049350..0x15049434, ROM 0x76800..0x768E4; its slot ends
at VA 0x15049440 / ROM 0x768F0. It uses a 56-byte frame with no calls or saved
return address. With points A, B and C, it computes the unnormalized normal
`(A-B) x (A-C)`, then the normal's dot product with A. It publishes normal X,
Y, Z and the dot product to `D_800CC210`, `D_800CC214`, `D_800CC218` and
`D_800CC21C`, in that order. The plane convention is normal dot position = D;
the final coefficient is not negated.

The signed Y expression is `(-abx)*acz + abz*acx`, retaining the retail
negate/multiply/add sequence. The final floating-point association also matters.
The source `nx*Ax + ny*Ay + nz*Az` recovers all instruction scheduling and
register choices directly. An earlier Z-first expression had 37 word
differences despite matching the body length and frame. Array-temporary and
chained-assignment screens were insufficient. Only the selected exact source
is installed and credited.

Raw compiler payload SHA-256:
`a2f2f18f989174f552dfe71225f145b36290a28d9cc160c3478fd9be0a7727e0`.

## Aggregate ABI and caller evidence

The aligned retail census finds four direct JALs and no aligned literal
function pointers:

| JAL VA | JAL ROM | Original copy-window start | Aggregate at caller SP+ |
| --- | --- | --- | --- |
| 0x1500B558 | 0x38A08 | 0x1500B51C | 0x90 |
| 0x1505A02C | 0x874DC | 0x15059FF0 | 0x50 |
| 0x150E4F78 | 0x112428 | 0x150E4F3C | 0x124 |
| 0x150E5958 | 0x112E08 | 0x150E591C | 0x74 |

Each 17-word static window copies nine words into the outgoing argument area
using three iterations of a three-word copy loop. It loads the first three
words into A0..A2 and the fourth into A3 in the JAL delay slot. Five remaining
words arrive on the stack. This is one 36-byte aggregate, rather than nine
scalar floating-point arguments. The neighboring wrapper's nine-word by-value
argument is consistent with that interpretation.

All four original windows and the complete helper pass 64 cases / 128
executions with unrelated floating argument registers. The incoming aggregate
and source storage are preserved. The dynamic window ends when the helper
returns; it does not claim execution of each complete parent or natural
reachability through every preceding parent gate.

A separate continuation CFG audit follows both branch outcomes and delay
slots until each old V0/F0 value is overwritten, another call clobbers the
return registers, or the caller returns. It finds no read of either plane
return value. Eight injected return-read controls fail as required. This
supports the recovered void interface; it is static liveness evidence,
separate from the bounded caller execution.

## Floating-point and execution qualification

The rounded reference derives two difference vectors, their cross product and
the ordered dot product independently from the argument words. The guest
matrix passes 2,064 cases / 4,128 executions across both supported stack
phases, reaching all 57 body words. It includes signed zero, degenerate and
collinear triangles, varied orientation and deterministic finite inputs with
wide exponents. SP and all callee-saved GPR/FPR registers are preserved. All
four public stores occur in retail order. The three alignment words are not
counted as executed instructions.

Seven additional special-value model cases include subnormals, maximum finite
values, infinities and a quiet NaN. Both identical instruction streams agree.
The oracle's local `neg.s` operation flips the sign bit. This bounded binary32
model does not establish hardware FCSR flags, denormal traps, signaling NaN
behavior or hardware NaN payload propagation.

Three independently linked code/global profiles include distinct global high
halves and signed-low16 carry boundaries. All complete rebased payloads match;
48 executions agree with the reference. Eighty-four fired access-prefix cases
and two independently linked guest output-alias cases agree, including aliases
with incoming homes and a shared output address. These guest observations do
not claim portable C fault or overlapping-global semantics.

Native32 asserts the aggregate's 36-byte size and B/C offsets 12/24. O0/O2/O3
each pass 1,032 reference cases under UBSan, preserve the original aggregate
and canaries, and reject all seven compiled semantic controls: X/Y/Z sign
errors, a wrong source point, a wrong dot coordinate, an omitted publication,
and dot reassociation. Native tests use finite bounded inputs and disabled
floating-point contraction; hardware floating-point exceptions are not claimed.

The initial O2 harness crashed at an aligned SSE store. GDB showed an
unaligned ESP in the freestanding `_start` entry point. Applying
`force_align_arg_pointer` to that harness entry fixed all profiles; the
candidate and shared compiler flags did not change. Earlier fixture fixes
also selected the interpreter's supported stack phases and mapped the caller
stop boundary. None required a production-source workaround.

## Owner, production and banking

Complete-owner compilation emits no diagnostics and preserves both neighbors
and literal pools. The actual normal three-command Make recipe reproduces the
independently padded object. All 228 payload-byte corruption controls, eight
binding controls and two owner/function scope controls fail closed.

Private prediction and production ELF agree literally across the entire
image: **194 changed bytes**, limited to the target and its symbol extent
12->228. There are no metadata permutations, exclusions or masks. All 6,055
other linked bodies and all addresses remain fixed. Protected Game data is
exact across 189,088 bytes and 720 owners. The full 17,383-file predecessor
seal has only the expected source, target object and ELF changes, with no
unplanned dependent-object changes.

Production ELF SHA-256:
`ed315d5acc97e7491d314ae9e54d47e0b46bbfdcdc8fc97a72e0b4c9398681cf`.

Seven fresh target tests pass in both tools copies, both shared tool checks
pass, and the installed production suite passes again. Tools `33f0728` bank
the qualification before the consumer pin. The older mirror's inherited
changes are preserved; it is not committed. Nothing is pushed. Graph refresh
is limited to the changed source, tools and documents: all prior valid nodes
and edge occurrences are retained, and the obsolete s32 placeholder return
relationship is archived with provenance alongside the earlier archived edge.
No full-corpus extraction or global reclustering is claimed.

With the prepared inputs and retained stage:

```sh
python3 -m unittest tools.tests.test_game_plane_coefficients_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-plane-coefficients-15049350-match`. Key receipts are
`preparation.json`, `runtime-qualification-v12.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`. The Native/cache current seals and final
banking proof are retained with the stage.

Next screen: `func_1510A930`, a 60-word Game routine in `generated_137DE0`.
Start with its complete original calls and owner profile. Existing private
candidates remain uncredited and are not replaced by a broad conversion batch.
