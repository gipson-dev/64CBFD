# Linked ring emitter recovery and ordered setup screen - 2026-11-16

`func_151A37C0` has a complete private semantic C draft and a maintained,
bounded symbolic setup screen. **It is not adopted or byte-exact.** The selected
draft emits **266 words / frame 0x120** for the original **265-word / frame
0x120** slot. The production function remains its zero-return placeholder.

Accepted progress stays **4,522 / 5,514 (82.01%)**, Game **3,849 / 4,841
(79.51%)**, zero drift, 992 different; **165** further matches to 85%.
Init492/492 and Debugger181/181 remain exact. Root README aggregate rows do
not change. This checkpoint gives **zero C-match credit**.

## Retail interface and complete draft

VA `151A37C0..151A3BE4`, ROM `1D0C70..1D1094`, owner
`conker/src/game/generated_1D0840.c`, original `conker/asm/1D0840.s`.
The aligned callback is `D_8008A23C[6]`, VA `8008A254`, ROM `22ED14`.
The original 100-word `func_15147740` invokes this second callback table at
`15147820`; zero requests release and one keeps the owner. This pointer/caller
inventory is not a completed connected-caller test.

The draft validates the linked owner's live word and identity, initializes
the position through `func_151A4E34`, samples later positions, and retains
fractional movement progress. On a failed later query it calls
`func_151A4E9C`, snapshots all 48 descriptor bytes, and submits
`func_151491F4(300, -1, 10, 0, 5, 48, owner[0xC], 0)`. A successful factory
result receives that snapshot at +0x28. The remaining path emits 24-byte ring
records, updates phase with unsigned RNG modulo (range-byte +1), maintains
signed byte head/tail/count and stores the final position/time remainder.
This complete body is retained for continued qualification; these descriptions
do not claim all of its paths have passed acceptance.

`D_800A8D58` contains `0x38D1B717` (0.0001f) in the protected retail data.
`D_800BE9A4` is an absolute runtime timestep symbol with no static ELF-backed
value. The selected draft retains the extern threshold access. Literal,
typed-owner, expression, scope and compiler-profile experiments remain private.
The existing no-unroll profile emits the same selected raw text and leaves
all 22 raw neighbors unchanged; it does not resolve the extra word. Production
Makefile, headers, guards, source, objects and ELF remain untouched.

## Verified setup transfer and rejected shorter form

The maintained manifest retains two complete C bodies. Selected raw SHA256:
`ecd27daa05e56adeb187bd5a42f34aa2d076a8f2fa7eb7e2ee762310f8fbfd87`.
It has 151 positional differences before any alignment or scheduling recovery;
the one-word size excess makes that positional count unsuitable as a count
of independent remaining edits. The deliberately rejected form has the retail
265-word length and 0x120 frame, with 58 positional differences, raw SHA256:
`05f9ab98ceb748f8c3ab4cf823633438aa04affbfe328ec274a2d3954cf21cb4`.
It fails the ordered floating-point transfer. Matching size/frame or ordinary
finite outputs is therefore insufficient.

The instruction-driven screen starts at offset 0x154 after the query paths
and ends at the first emission or return cut. All **eight symbolic setup
paths** agree on the ordered FP opcode/operand/FCSR sequence, public writes,
the joint FP/write sequence, each live emission-loop FP value, copied position,
cached output pointer, stride/mark/entry roles and unchanged saved odd FP
registers. An explicit private-write inventory protects all other frame state.
Initial FCSR is arbitrary; the screen does not assume disabled FP traps.

The domain has ordinary mapped/aligned public memory, a private disjoint stack
and an immutable epsilon word. Ordinary reads commute only within intervals
without a public write. This is a bounded setup transfer, not a whole-function
or fault-prefix proof. Entry, fallback providers, the loop, tail, epilogue,
general caller integration and portable native C still need qualification.

Four semantic controls are rejected: wrong coordinate subtraction, a lost
horizontal-step liveout, a lost copied-position liveout and a saved-frame
write. An independent temporary GPR renaming passes. The missing-position
control first exposed a fixture diagnostic defect: a missing dictionary key
escaped as KeyError. The screen now asserts the complete live-home inventory
before reading it. The first 1,293-input freeze and failed smoke receipt remain
retained; fresh qualification uses the separate immutable v2 freeze. No old
snapshot or failed receipt is rewritten into passing evidence.

Both full owner compiles retain all 22 other raw functions and their pools.
Four maintained unit tests pass freshly in the primary tools and the isolated
sibling overlay at identical four-file hashes. The sibling's 2,434 existing
dirty paths and scoped dependency bytes remain unchanged. Actual import
origins, including any primary fallbacks, are recorded. All **1293 current
production/tool inputs remain unchanged** through the screen, and project
tools checks pass. The prepared `qualified.o` filename names the selected
screen stream; it is not evidence of full matching or production adoption.

## Continue here

1. Resolve the selected draft's four-byte slot excess and remaining allocation,
   stack-home and scheduling differences. The 265-word near match is an
   effective rejection control; do not adopt it or repair it by hiding FP order.
2. Extend independent transfer checks through entry and retirement, the actual
   position query and cleanup, both memcpy calls and the factory's exact ABI.
   Preserve every copied byte and the distinct raw/retail snapshot homes.
3. Prove one emission and the ring tail/backedge inductively. Carry all live
   FP/private values across arbitrary o32 RNG clobbers and public mutations;
   prove the byte-derived divisor stays in [1,256].
4. Run independent guest/native and original-parent tests, including boundaries,
   provider mutations, aliases, wrapping bytes and ordered FP behavior.
5. Qualify both actual padders, relocation negatives and independent GNU rebases.
   Only then perform the frozen actual-Make and strict whole-image production
   gates, recount and document an adopted match. Do not exclude the next slot
   or unrelated data to fit the current oversized draft.

Reproduce the prepared screen with
`python3 -m unittest tools.tests.test_game_ring_emitter_151a37c0_screen -v`.
Receipts: `conker/build/game-next-151a37c0-private/setup-screen/`;
immutable authority: `input-baseline-v2/fingerprints.json`. The original
private preflight, all losing candidates and earlier accepted checkpoints
remain intact. Graphify uses retained-ID scoped updates and an explicit
screen-to-function reference, not a full-corpus extraction claim. No Claude,
host build, Release/save change or push. Commit tools before consumer docs/pin;
continue this function and keep the full 85% goal active.
