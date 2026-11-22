# 2625 - Source-heading trail guarded byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_151945CC` is recovered as complete semantic C and matches its **114-word
retail slot through nine scheduling guards**. **Raw C still has nine word
differences**; this is not a raw byte-exact C claim. There are no inserted or
omitted instructions. Fresh production is **4,607 / 5,528 (83.34%) total** and
**3,934 / 4,855 (81.03%) Game**, zero address drift and 921 different converted
functions. Init remains 492/492 and Debugger 181/181. **92 more matches** reach 85%.

## Recovered source, frame and ABI

Source: `conker/src/game/generated_1C1150.c`; preserved original:
`conker/asm/1C1150.s:641`. VA `0x151945CC..0x15194794`, ROM
`0x1C1A7C..0x1C1C44`, 456 bytes, frame 176, S0 at SP+0x20 and RA at SP+0x24.
All 18 relocation sites and the existing O2/g3 profile are preserved. All
28 neighboring raw/padded functions and compact pools remain identical.
Raw instruction SHA256:
`5203b0707289dd41c6a8d0e191834522eb49f21c9838c0cf43841e5594c35cef`.

Actual arguments are source actor, selected actor and an unused byte-context
pointer. Both real registered callers supply that pointer from their stack.
The callback return is unused in the original continuations. Keeping one
32-bit classifier/category local recovers frame 0xB0 without invented padding;
separate locals produced the rejected 184-byte frame.

The source halfword at +0x7A is unsigned. Its high byte minus 64 is retained
in a signed halfword at SP+0xA2; the first angle subtracts another 64. The
selected actor's position is captured at SP+0xA4/A8/AC before both services.
Y performs a real double addition with `D_800A82A0` (270.0), then rounds to
single. Surface is 36 bytes at SP+0x30, angles eight bytes at SP+0x54, and the
localized trail 68 bytes at SP+0x5C. These are distinct objects, not a matrix.

The surface service runs first, followed by `func_15134070`. Type 99 rejects
before `D_800A3FE6[type*16]`; category 2 rejects submission. Accepted paths copy
the saved position, use angles heading-minus-64/128/-160/32, counts 15/12,
request selectors 3/1, durations 31/19, modes 155/100, selector iff category 1,
chance 0.5 and values 16/15/0. Time, time range, scale and radius parameters
come from `D_800A82A8/AC/B0/B4/B8`. **Scale range is zero; radius base comes
from D_800A82B4.** This corrects the prior private handoff's field-offset error.
The target submits through `func_15153F18`, then attaches the owner effect with
`func_151B4CD0(actor, 255, 1)`. No descriptor padding is newly initialized.

## Closed scheduling guards

The only raw differences form one rotation. The compiler emits `A1 = S0` at
word 15 and the final Z store in the first call's delay slot. Retail has that
move in delay word 24, with the same intervening memory/arithmetic sequence
one word earlier. The JAL at word 23 and its binding are fixed.

The entry captures A1 in S0 at word 4. Neither register changes before the
first call, so the rotated move is redundant at every point in this region.
The proof checks this register lifetime, exact rotation membership, unchanged
memory-instruction order and absence of relocations at the nine replaced words.
Nine expected-word guards normalize offsets 0x3C..0x58 and 0x60. The full old
CSV is a byte-identical prefix. No other guard or function is changed.

Raw C and normalized/original streams agree on complete final private state,
public effects and ordered memory accesses in the bounded guest model. Fault
PC/delay comparisons apply to the normalized streams, whose instructions
literally equal retail; raw fault PCs are not claimed to match.

## Fresh qualification

Run `python3 -m unittest tools.tests.test_game_source_heading_trail_151945cc_match -v`.
All five checks pass before and after installation in both primary tools and
the isolated sibling overlay. Python/non-Python inputs are fingerprinted;
shared `make tools-check` passes. The real dirty sibling is preserved.

1. Both guard-aware padders reproduce the complete original target payload
   and all relocations. The natural mixed GLOBAL_ASM Make recipe executes five
   commands and produces the independent qualified owner exactly. Sixteen GNU
   links check four emitted forms at alternate constant/callee addresses,
   including HI16 carry boundaries. The isolated link's optional eight zero
   alignment bytes are explicitly checked. Stale words, stale source/expected
   relocations, duplicate guard offsets and wrong replacements are detected.
2. The guest runs **3,090 cases per stream**, covering all 114 words, all 256
   heading high bytes, low-byte boundaries, source/actor aliases, rejection and
   selector branches, pointer-home mutations, service changes to positions,
   headings, categories and constants, and single/double precision boundaries.
   Raw/normalized/original final states agree. **99 sampled normalized fault
   triples** compare full private memory, registers, trace, PC and delay state.
   Sparse wider classifier indices and incoming-home writes remain guest-only.
3. The original **63-word classifier**, with both original jump tables
   totaling **608 bytes**, executes **2,048 cases per stream** across all 256
   actor identity bytes. All 63 classifier words execute. Other providers use
   explicit mutating contracts; their complete 89/168/95-word extents are
   statically retail-exact. No full provider/hardware execution is inferred.
4. The target is D_80086694 entry 10 at 0x800866BC / ROM 0x22B17C. There are no
   direct ROM calls or other aligned loaded pointer literals; computed references
   are not excluded. Both real JALR windows at 0x1505BD78 and 0x1505C6DC execute
   **128 cases per stream**, totaling 17 original caller words. They verify all
   three pointer arguments and the saved-T1/context-pointer delay slots with
   effective omission controls. Current windows equal original; full parents
   are outside this focused execution test.
5. Defined SDK32 native fixtures run **6,408 cases at each of O0/O2/O3** with
   strict aliasing and UBSan. Pointer width, all descriptor extents and actor
   offsets are asserted. Ten incorrect-source controls detect signed heading,
   bias, both gates, selector, stride, the prior field swap, reduced height
   precision and late position/heading capture. Native tests use valid objects;
   they do not perform sparse guest-address or incoming-home mutations.

## Production, storage and continuation

The production rebuild and fresh recount pass. The independent whole-ELF
prediction accounts for **565 changed bytes with zero exclusions**: target
slot and symbol size 12->456, plus seven closed GNU symbol/name permutations.
All **20 moved records and 233 name bytes** preserve their named definitions
and attributes. Those bytes are reconstructed explicitly from the frozen
baseline; no metadata region is ignored. All 189,088 GameData bytes / 720 owners,
conversion rows and all other function addresses/bodies/extents are preserved.

ELF SHA256: `0675d67cf3ca1f9b9c8da281fa81fc78943edbb04ce27c18909b3580d3514b5b`.
Prior consumer `78a8d88d76b685e42609b6a3f2f9636892a46613`; prior tools `32ef4dd12140078cb56cc4cfd8104d876fae29c3`.
Tools are committed first. The existing duplicate generated_12D630 recipe
warning remains recorded. The root README receives aggregate row changes only.

[Note 2624](2624-completed-build-compression-and-preservation-20261121.md)
records the verified storage recovery that preceded this function. No host
build or Release change was made. The available scene-recompile configuration
consumes binary words and symbols; this C recovery supplies no direct import.
Full gameplay/hardware acceptance is outside these matching checks. Zero
advisory calls; the prior authentication failure was not retried.

Continue with adjacent `func_15194810` (116 words / frame 0xA8). Its five-entry
table, kind-0x53 branch-likely path and seven-byte sound packet require a fresh
pool/ABI audit; the packet producer already has compatible C in this owner.
The private read-only next-function audit records its exact field offsets.
Existing private camera, position, matrix and history handoffs remain uncredited.

Graph maintenance: the native update exited 1 with all
70,374 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,426 nodes / 163,984 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
