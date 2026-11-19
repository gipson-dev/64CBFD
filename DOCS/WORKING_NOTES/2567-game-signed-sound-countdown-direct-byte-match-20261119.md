# Note 2567: Signed sound-countdown callback direct byte match

Date: 2026-11-19. Consumer baseline `72ff18174600403e58551dae2abad607c3175a54`,
tools baseline `18fc5e52530ac25f97a52d3dde577c0d4489927d`.

`func_15103910` is installed as **directly byte-exact C across all 100 words /
400 bytes / frame 0x30**, with **zero guards** and the existing O2/g3 profile.
Production Make equals the independent full-image prediction. Installed
qualification and a fresh ELF recount pass.

Total **4,561 / 5,514 (82.72%)**, Game **3,888 / 4,841 (80.31%)**, Init
**492 / 492**, Debugger **181 / 181**; zero address drift,953 different.
**126 additional matches** are required for85%. Converted functions stay
**5,514 / 6,048 (91.17%)**,86.19% of bytes; the progress CSV is unchanged.

## Source, interface and behavior

Owner `conker/src/game_130CB0.c`; VA`0x15103910..0x15103AA0`,
ROM`0x130DC0..0x130F50`. The seven o32 arguments are the record prefix,
callback-value output, volume output, unused pan/cents/effects pointers and
pending sound-ID pointer. Original `func_10011624` assembles precisely this
interface at VA`0x10011848..0x10011884`, with JALR at`0x1001187C`.
The obsolete unprototyped local declaration and zero-return stub are removed.

The shared 40-byte record prefix view is hoisted before the callback. Its
offset0xC member is now signed `volume`, consistent with registration and
dispatcher use. This is a private prefix view, not a claim that the full
retail `struct15` is40 bytes. No shared headers or other function bodies change.
Both the raw and padded93-word `func_15103AA0` remain byte-identical, along
with all three other owner neighbors and all constant pools. Previous
unchanged neighbor semantic receipts are reused, not claimed as fresh tests.

The callback caches its actor and snapshots three floating coordinates into
signed halfwords. It interprets the low16 countdown as **signed**, unlike the
neighbor's low15 mask. A new pending sound ID replaces the high16 bits,
clears the current ID and pending output, and emits command0x5B0 with
25000/100/120 parameters. Otherwise it subtracts the frame ticks with32-bit
wrap and narrows to signed16. A nonpositive result publishes the old high
sound ID, volume and callback-value1, then clears the packed word.

The zero-count path publishes the volume and callback value before reading
the handle. A zero handle emits0x5B1 and returns1. Otherwise an unequal actor
handle is stopped, the record handle is reloaded after that call and stored
through the **cached actor**, then bit0x80 is cleared. The surviving paths
preserve the high word, merge the countdown and return0.

Names describe measured use and are not claimed as recovered debug names.
The unsigned tick operand prevents signed32 overflow in native C while
preserving every retail word, including signed16 narrowing and its wrap.
Null pending is permitted only on zero-count paths; required outputs and
actor accesses must be valid. Native coordinates stay within the signed32
conversion domain. Sparse addresses, overlapping pointer/word storage and
incoming-home aliases are guest-only qualifications.

## Direct compiler match

The initial semantic body was103 words / frame56. Inlining the packed-word
temporary restored frame48. Copying the expiry token through its output
restored100 words; declaring the signed16 countdown before the actor pointer
placed its call-save atSP+0x2E. Expressing the actor-handle comparison in its
retail operand order removed the last difference. No guard, alternate
profile, source register binding, assembly insertion or dead-word omission
is used. Raw body SHA256:
`0a1c26305badfde1376e786df71e91e159b7ff21051411160077da226848ab9c`.

## Independent qualification

The primary tools checkout and an isolated sibling overlay each pass the
same **five-test suite before and after installation**:

- 1,032 independent guest cases per stream: signed extremes, subtraction
  wrap, high IDs, pending replacement, outputs, aliases and helper effects.
- 177 access-fault prefix pairs, five executed instruction negatives and
  three fired incoming-pan-home boundaries. All99 words reachable from the
  normal entry are visited. Retail also retains dead word 77, an actor-handle
  load following an unconditional return branch. Its word and predecessors
  are explicitly checked, no internal branch targets it, and all 100 raw
  words are byte-identical.
- 746 SDK32 native cases each at O0/O2/O3 with strict aliasing, UBSan and
  float-cast-overflow checks; eight executed source negatives per profile.
  Expected fields and call snapshots are serialized from the independent
  Python model, not a second C implementation.
- Six independently linked GNU relocation rebases /12 links compare all400
  bytes. All400 single-byte and five binding corruptions are rejected;
  three full-image corruption controls fail closed.
- 32 scenarios through the original 15-word dispatcher call window, executed
  once with original and once with C instructions. Output pointers,
  stack arguments, nested helper observations and the return boundary agree.

The original constructor builds the callback address at ROM`0x1311D8` and
passes it to `func_1000FA64`. Full-ROM census finds this one adjacent
LUI/ADDIU construction, zero literal address words and zero direct J/JAL
targets. Arbitrary computed references are not excluded. Caller and
registration source/assembly inputs are hash-pinned. The connected test
covers the actual call window; providers remain bounded opaque models.
There is no full-parent, hardware or gameplay acceptance claim.

Initial test-harness failures were corrected before acceptance: a control
changed ignored MFC1 bits, another lacked an expiry-triggering input, and
the bounded caller fixture lacked a sentinel continuation key. The final
negatives execute effective changes, and the original continuation fires.

## Production, tools and documentation

The real three-command Make owner recipe matches the private padded object.
Both normal-C and independently synthesized generated padders agree across
all five owner functions. Actual production Make matches the strict
**291-byte** full-image delta: only this function body and its12-to400-byte
symbol extent change. There are no exclusions or metadata permutations.
All 6,051 function entries retain addresses, every other body remains
unchanged, and all 189,088 protected data bytes across 720 owners are exact.
All 1,897 frozen inputs are checked; guards, layouts, original assembly,
Makefile, unrelated objects and the conversion CSV are unchanged.

Production ELF SHA256:
`ad9b9f732a139efd4bbe13a078cf738bdf9f77062d8e2b9076f10f9a5cd05efe`.
`make tools-check` passes. The actual dirty `64CBFD Tools` sibling remains
untouched; its HEAD, raw status and 343 dependency hashes are preserved.
The 910-file overlay selects 339 identical sibling files, 565 explicit primary
fallbacks, five task files and an empty bootstrap. Both installed suites
import byte-identical dependencies apart from that bootstrap.

Graphify's native update refuses a shrinking graph; the retained graph gets
a scoped five-code-file AST merge and explicit manifest-to-function edge.
Old node IDs are checked before and after the merge. The commit-hook
producers must be observed terminal before preserving historical heading
aliases and sealing the final graph hash. This is a scoped refresh, not a
full-corpus extraction. The checkpoint packet stores the final graph seal.

Private evidence: `conker/build/game-sound-countdown-15103910-private/`,
including raw probes, qualification receipts, paired suites, production
audit, frozen copies and current handoff. Root README changes only the two
aggregate matching rows; five concise documentation indexes link here.

## Next

Continue with the remaining constructor `func_15103C14` in this owner,
VA`0x15103C14..0x15103E38` (137 body words plus two alignment words in its
slot; remeasure from the layout before qualification). Inspect its random
selection, actor validation and both callback-registration paths independently.
Preserve both newly exact sound callbacks. The older 591-word
`func_150BBB5C` remains private and uncredited. Keep the full 85% goal active.
