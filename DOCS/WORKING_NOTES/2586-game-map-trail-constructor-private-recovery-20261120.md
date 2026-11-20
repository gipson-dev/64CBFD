# Note 2586: Map-trail constructor private recovery

Date: 2026-11-20. Consumer baseline `47d255d464b4c93078360482fd63c0693331ee6c`;
mounted tools baseline `2606e4b690ed52be3c60bf4d5b6716cd235e63f1`.
Recovery tools commit: `33ab2994f7a601239c0db9dcd689a9cbcea6ee32`.

`func_15105CE0` has a complete, tested **private semantic C recovery**.
The selected O2/g3 candidate emits **233 words / 932 bytes**, versus retail's
**235 words / 940 bytes**, with the original **216-byte frame** and the
112-byte effect descriptor at **SP+0x58**. It remains **uninstalled and
uncredited**. Register allocation, arithmetic placement and independent
scheduling still differ; 215 positional word differences include displacement
from the unequal lengths. Being two words shorter does not mean only two words
need matching.

Production remains at **4,572 / 5,523 (82.78%)** total and **3,899 / 4,850
(80.39%)** Game, with zero drift and 951 different. Init 492/492 and Debugger
181/181 are unchanged. There are **123 more matches** to reach 85% at the
current denominator; additional ASM conversions can increase that denominator.
No production source, shared declaration, guard, compiler profile, progress CSV,
loaded image or root README aggregate was changed in this recovery checkpoint.

## Recovered interface and storage

Owner: `conker/src/game/generated_133190.c`. Retail window:
VA **0x15105CE0..0x1510608C**, ROM **0x133190..0x13353C**.
The original assembly remains in
`conker/asm/nonmatchings/generated_133190/func_15105CE0.s`.

The four-argument interface is an 80-byte map-particle packet pointer, s32 extra
allocation size, a priority narrowed through u8, and an s32 context. The result
is an allocation pointer or NULL. The packet agrees with the already recovered
`MapParticlePacket131F30` emitted by `func_15104C44`; the local view names four
points, count, width/spread, signed minimum/maximum and RGBA bytes. Local types
are kept in the experiment. Shared `variables.h` is not widened.

The constructor:

1. Caches the initial piece count and allocates `0x88 + count*52 +
   (count+2)*12 + extraBytes` via the existing six-argument allocator.
   Failure returns NULL before copying or creating children.
2. Copies all 80 input bytes at record+0x10; writes the end-of-storage pointer
   from the cached count, then reloads the input count for `1.0f/(count+1)`.
3. Calls the integer random provider before reading signed halfword bounds;
   its duration uses an **unsigned** 32-bit remainder and a halfword store.
4. Calls the curve and sample builders, clears two child pointers and sixteen
   scratch bytes, then reloads the output packet count for the segment size.
5. Initializes a 112-byte child descriptor with two 12-byte vector copies,
   RGBA, effect constants and two ordered single-precision size multiplies.
6. Creates exactly two child effects, using input points **0 then 3**. Two
   independent random results set flags 0x40 and 0x80. Descriptor changes made
   by the first child provider survive into the second call, except position
   and flags, which are explicitly refreshed.

The effect descriptor has three unwritten padding bytes at offsets **0x67,
0x6A and 0x6B**. Guest tests compare all 112 copied bytes against the original
stack pattern and preserve child-provider edits, including padding. Native
checks compare its defined fields and exclude those three padding bytes.
They do not claim portable C control of uninitialized padding.

The recovered literals are the original `D_800A2410` = 1,000,000 and
`D_800A2414` = 0x3D9D89D9. Both 12-byte copies at D_800A5480 use observed
word offsets 0/4/8; the local vector declaration does not alter the shared
scalar declaration or establish a complete global-object ownership model.

## Focused evidence

The immutable target baseline contains **2,074 hashes / 170 independent copies**
under `conker/build/game-map-trail-constructor-15105ce0-private/baseline/`.
The experiment compiles the complete original and proposed owners. All **36
neighbors**, normalized `.rodata` and `.data` pools remain unchanged. Two
pre-existing `func_1510761C` pointer/integer warnings are unchanged apart from
source paths and line numbers; the recovery introduces no compiler warning.

The first candidate was 228 words/frame 224. Removing an unnecessary point-index
local and ordering the descriptor before the byte loop counter restored frame
216 and descriptor SP+0x58. Expressing the 52-byte segment stride as thirteen
words followed by a two-bit shift prevents the compiler from retaining the
wrong scaled count across the copy; this yields **233 words/frame 216**.
The selected raw payload SHA-256 is
`2ab1135c15544731abe149634de72d77c2180be53985a6fc054c7f7c1a064218`.
No binary normalization, inserted instruction or expected-word guard was added.

The four focused tests cover owner shape/pools, guest execution, native source
execution and the literal ROM caller census. The guest corpus contains **512
cases per stream**, covering allocation success/failure, piece counts 0/1/7/31,
two stack phases, nontrivial upper argument bits, signed bound extremes,
nonzero/zero random flags and three modeled mutation boundaries. It reaches
**232/233 candidate words and 234/235 retail words**; the excluded instruction
is the zero-divisor BREAK, outside the ordinary nonzero-divisor C contract.
It checks all public fixture bytes, complete call arguments, return pointers,
both full child descriptors and callee-saved registers.

Native SDK32 runs **512 cases each at -O0/-O2/-O3**, with strict aliasing and
UBSan. All pass. Eight effective source controls reject a wrong point, allocation
size, signed random remainder, unsigned bound read, lifetime, second flag,
descriptor reinitialization, or cached output count. The first -O2 harness
attempt faulted in `_start` on an unaligned `movaps`; GDB located that harness
entry fault. The harness now explicitly aligns its entry stack, and the
recovered function is unchanged by that correction.

The original ROM contains four aligned direct JALs to the constructor:

| Caller | Call VA | Call ROM | Extra bytes |
| --- | --- | --- | --- |
| `func_15104C44` | 0x15104F90 | 0x132440 | 0 |
| `func_151072BC` | 0x151075C0 | 0x134A70 | 4 |
| `func_15107700` | 0x151078A8 | 0x134D58 | 12 |
| `func_15107C1C` | 0x15107E0C | 0x1352BC | 24 |

Their inspected argument setup agrees with the recovered four-argument ABI.
The census cannot exclude computed calls. Complete original-parent and
provider execution are **not qualified by this checkpoint**: allocation,
copy, zeroing, random generation and child construction are bounded contracts
in the new guest model. Provider mutation checks are deliberate stress cases,
not claims that retail helpers perform those mutations during gameplay.

Fresh paired suites run through the mounted tools and an isolated sibling
overlay, with **307 equal imported Python hashes** and four passing tests per
configuration. The **1,011-file** overlay contains **341 sibling files, 664
primary fallbacks, five task files and one bootstrap**; **345 real sibling file
hashes**, its HEAD and its complete dirty status remain unchanged. It retains the real
dirty `64CBFD Tools` checkout: matching files come from it and unavailable or
different dependencies fall back to the mounted tools. Its exact composition,
real-file fingerprints and suite receipts are retained in the ignored target
folder. `make tools-check` passes. No host, save, frozen Release, account or
compiler-installation changes were made; no Claude calls or pushes were used.

## Continue the same function

Reproduce with `python3 -m unittest
tools.tests.test_game_map_trail_constructor_15105ce0_recovery -v` from a prepared
consumer checkout. The source experiment contains the complete candidate and
can use the fingerprinted original live owner when a private snapshot is absent.

1. Recover the opening `(count+2)*12` arithmetic and count/point-size lifetimes.
   The compiler currently reassociates this as `count*12+24`, keeps count in S0
   and point bytes in S1; retail uses the opposite saved roles and the original
   multiply/argument-delay layout. Preserve the recovered defined data flow.
2. Fit independent descriptor-initialization scheduling and the two hoisted
   descriptor/position addresses; keep all 112 descriptor bytes and the two
   provider-visible lifetimes intact. Do not replace this with a retail-word
   array or claim a match from shape agreement alone.
3. Qualify actual caller/provider paths, full control-flow and necessary
   instruction/access-order relations. Then run actual Make, both real padders,
   independent whole-image/protected-data audit and production recount before
   installation or matching credit. Keep this candidate private until those
   gates pass.

Graphify has no earlier function node for this target. The refresh must retain
all prior nodes and identify this as an **uninstalled recovery candidate** with
an active ASM reference. A scoped AST merge is not full-corpus semantic extraction.
The native update refused a smaller 27,392-node result and preserved the existing
68,343 nodes. The subsequent four-file scoped AST merge retains **all 68,343
old node IDs**, ending at **68,381 nodes / 145,439 links**, with the candidate
explicitly marked uninstalled and zero credit. No forced graph overwrite was used.
