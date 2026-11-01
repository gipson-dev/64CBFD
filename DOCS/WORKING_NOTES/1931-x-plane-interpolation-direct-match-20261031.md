# X-plane vertex interpolation restored directly from C

`func_15185B54` now has complete C in `conker/src/game/generated_1B1600.c`.
All **60 words emit directly**, with no frame, relocations, trailing alignment
words, guards, insertions or omissions. The private `ClipVertex` names its
20-byte layout: three floats at+0/+4/+8, signed halfword attributes
at+0xC/+0xE/+0x10, and two retained bytes at+0x12. Its interface returns the
next output vertex: `ClipVertex *func_15185B54(ClipVertex *a, ClipVertex *b,
ClipVertex *out)`.

Production Make and an independent recount against the Windows consumer ELF
establish **4,006/5,506 (72.76%)** exact C functions, Game **3,333/4,833
(68.96%)**, zero drift and 1,500 still different. Init remains 492/492 and
Debugger 181/181. **124 more matches** are needed to reach the active 75%
target of 4,130/5,506. Guard and conversion-inventory CSV bytes are unchanged.

## Recovered behavior and source

VA 0x15185B54..0x15185C44; ROM 0x1B3004..0x1B30F4. The routine computes
`ratio = a.x / (a.x - b.x)`, writes positive zero to output X, interpolates Y
and Z, interpolates each signed attribute and truncates it toward zero, leaves
the two retained bytes untouched, and returns `out+1` with a 20-byte stride.

The first complete typed candidate matched every word. Explicitly introducing
another captured-X local instead produced eleven register/scheduling
differences; that variant remains historical and is not installed. No shared
header or other vertex layout is changed.

Raw compiler/retail payload SHA-256:
`a89a5408775ca3707bdba0d50c9bb0a9da44dbf7e3fbd9db1cf085db37d5949f`.

## Function table and complete original caller

The aligned retail census finds no direct JAL and two literal pointers at
ROM 0x231F70/0x231F74, VA 0x8008D4B0/0x8008D4B4. These are slots 6 and 7
of `D_8008D498`. Corresponding classifier slots in `D_8008D4C0` select
`func_15185C44` (X<=0) and `func_15185D84` (X>0).

The complete original 84-word `func_15185DD4` takes a vertex array, signed
count, table index and output cursor. It closes the polygon with the last
vertex, classifies each current/previous pair, copies whole inside vertices,
and inserts a crossing when the pair's classifications differ.

It calls the interpolation pointer in S5 at 0x15185E90 and 0x15185EDC. A0/A1
are previous/current vertices; each JALR delay slot supplies S1 as A2. The
first path uses returned V0 as the destination for the current vertex's
20-byte copy and advances again. The second retains V0 as the next output
cursor. These observed uses establish the pointer-return ABI.

An independent polygon-clipping reference agrees with both instruction
streams in 42 caller cases / 82 executions. All 84 parent words, both original
10-word classifiers and both indirect call sites execute across the matrix.
Cases cover both table slots, inside/outside transitions, signed-zero
boundaries, whole-vertex copies including retained bytes, and positive, empty
and negative counts. There are no external service models in this caller
execution. The negative-count path performs no vertex accesses.

This executes original retail parent instructions. The parent itself is not
recovered or credited by this change; its existing production body is preserved.

## Numerical domain, aliases and native checks

The root matrix passes 894 cases / 1,788 executions across both supported
stack phases, with separate output, output aliasing A, and output aliasing B.
It reaches all 60 words and checks the exact store order at offsets
0/4/8/12/14/16, all remaining bytes, the returned cursor, SP and saved GPR/FPR
state. Signed attributes include full halfword limits and negative values;
float cases include varied exponents, endpoint crossings and cancellation.

The reference rounds each operation to binary32 and models signed-word
conversion only where its input is finite and representable. Portable native
tests use finite opposite-side or endpoint inputs, with a nonzero denominator
and representable signed-halfword conversion results. They do not qualify
NaN/infinite coordinates, invalid conversions, FCSR flags, denormal traps or
other hardware exception behavior. The target's full instruction identity is
verified separately from those bounded numerical-model claims.

Native32 asserts the 20-byte type and important offsets. O0/O2/O3 each pass
447 cases under UBSan plus the float-cast-overflow sanitizer. All three
vertices' bytes and surrounding canaries are checked, including legal output
aliases and untouched retained bytes. Eight compiled controls are effective:
reversing the ratio, writing the wrong zeroed axis, omitting Y interpolation,
using another attribute, narrowing an attribute to a byte, dropping the third
attribute, returning the old cursor and overwriting a retained byte. Controls
remain within the declared conversion domain.

Fifty-four fired access-prefix cases agree between retail and C payloads.
Two independent code relocations are consumed through rewritten test table
entries by the original parent in eight further executions. The target has no
relocations; those tests qualify indirect dispatch and returned-cursor use,
rather than claiming nonexistent HI16/LO16 bindings. Fault-prefix observations
do not establish portable C fault behavior.

## Owner, image and banking

Complete-owner compilation has no diagnostics and preserves all 31 other
functions and literal pools. The normal three-command generated-owner Make
recipe reproduces the independently padded object. All 240 byte-corruption
controls, an injected relocation and two owner/function scope changes fail
closed. A stale placeholder digest in the initial private canonical-test
setup was corrected; the candidate and prepared instruction evidence did not
change. Both seven-test suites and both shared tool checks then pass, as does
the installed production suite.

The private predictor and production ELF agree literally: **184 changed
bytes**, confined to the target and its symbol extent 12->240. No metadata
permutation, exclusion or mask is needed. All 6,055 other linked bodies and
every function address remain fixed. Protected Game data matches across
189,088 bytes and 720 owners. Full review of the 17,401-file predecessor seal
finds only expected target source, target object and ELF changes, with no
unplanned dependent-object changes.

Production ELF SHA-256:
`18be5f55c4862b1dede8af4bb5b4d32ff7cf84c57dfffdf0fa74d8877d76c8f2`.

Tools `db27de3` bank qualification before the consumer pin. The independently
dirty older mirror is preserved and is not committed. Nothing is pushed.
Scoped Graphify refresh retains all prior valid nodes and edge occurrences,
archiving the obsolete stub's return-type relationship with provenance. No
full-corpus extraction or global reclustering is claimed.

With prepared inputs and the retained stage:

```sh
python3 -m unittest tools.tests.test_game_x_plane_interpolation_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-x-plane-interpolation-15185B54-match`. Main receipts
are `preparation.json`, `runtime-qualification-v3.json`, `production-v17.json`,
`production-seal-changes-v17.json`, `installed-audit.json` and
`native-production-recount.txt`; current Native/cache seals and final banking
proof are retained alongside them.

Next screen: `func_15185C6C`, the corresponding 60-word Y-plane interpolation
routine in this owner. Reuse the qualified vertex layout and inspect table
slots 8/9 and their classifiers before extending original-parent tests.
Existing private screens remain uncredited.
