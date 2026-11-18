# Cached-target callback steering factor and complete private-value relation - 2026-11-18

`func_150B963C` now passes a complete **77-path finite-value/private-state
relation** with a corrected cached steering-factor lifetime. All **400 related
private/incoming bytes**, an additional eight untouched source-only bytes and
two retail spill words related through source value histories are accounted
for. **The selected source remains uninstalled and uncredited**:434 words /
frame392, versus438 retail words /frame384. No byte-normalization plan or
production adoption is claimed by this milestone.

Production remains **4,550 /5,514 (82.52%)** total, Game **3,877 /4,841 (80.09%)**,
Init492/492, Debugger181/181, zero drift,964 different and **137 more matches**
to85%. The root README remains unchanged. No production source, guards, object,
ELF, compiler profile or conversion input changes.

Starting commits: consumer `a915ef2fa0adf2278876e118de535702f6067eeb`, tools
`bfce85335bc5940b41d86806d37b3d34bbe682cd`. All1,763 baseline inputs and the
seven separately frozen semantic artifacts remain exact: **1,770 protected
inputs**, no live-input links. The prior bounded behavior recovery is
[Note2547](2547-game-cached-target-terminal-callback-semantic-recovery-and-matching-boundary-20261118.md).
The new `game_target_terminal_150b963c_fitting`, `_fitting_manifest`,
`_fitting_native`, `_proof` and `test_*_fitting` artifacts retain this stage.
The ignored `adoption-relation` packet contains source screens, instruction/
layout inventories, public/private diagnostics, objects and final receipts.

## Steering-factor lifetime recovered before fitting

The prior437-word draft reloads D_8009FE00 after each actor steering write.
Retail loads it once and retains it across all three updates. The independent
symbolic public-memory model invalidates ordinary reads after every public
write or opaque call, retaining possible public aliases. Under that model the
old draft's Y update uses a new-epoch factor, while retail retains the earlier
factor. The retained `public-old.json` diagnostic identifies this difference.
The earlier finite concrete tests used separate actor/constant buffers, so
their passing results did not prove that stronger read-lifetime property.
This is a modeled alias/lifetime difference, not observed gameplay evidence.

The new C uses a named block-local **steeringFactor**, loaded once before the
three updates. It preserves the original cached target reloads, helper order,
late reads, byte/halfword widths, branch returns and uninitialized extra bytes.
No volatile declarations, dummy padding, fixed-register assembly or shared
header/profile changes are introduced. All63 bindings are retained, together
with seven unchanged owner neighbors and normalized pools.

Natural declaration/scope screens show the tradeoff rather than hiding it:
the selected body is **434 words /frame392**, with a source-only eight-byte
gap. Its raw text SHA is
`c3c0be295122110c29af380a567ed76002e484d0d4c397d62208f62a182a141f`.
The independently assembled original remains438 words /frame384, SHA
`8e685932a8b23237203b87b45e54aeaa87b8d8a69637993bcf9a24f5fbb7fbf5`.
Source shape is not counted as byte identity; normalization and adoption remain
open. This revised body supersedes the437-word draft for further fitting.

## Complete relation and explicit private projection

Both instruction streams execute **all77 complete paths**. Every434 source
word and438 retail word is visited, with no skipped instruction. Public writes,
helper arguments, returns, read epochs, division obligations, saved GPR/FPR/
SP/RA custody, descriptor bytes and private snapshots at every service agree
under the declared relation.

Offsets below are relative to the incoming SP. The source frame plus16 incoming
bytes has408 bytes; retail has400. The map is a bijection from400 source bytes
onto all400 retail bytes, plus the separately retained eight-byte source gap:

| Source interval | Retail relation |
| --- | --- |
| [-392,-288) | offset+8 |
| [-288,-284) | offset+16 |
| [-284,-268) | offset+268 |
| [-268,-264) | offset-8 |
| [-264,-260) | offset-16 |
| [-260,-8) | offset-8 |
| [-8,0) | source-only; unchanged entry bytes, no access or exposure allowed |
| [0,16) | identity |

This maps outgoing homes, saved registers, both RNG spills, burst/extra/spray,
query position and sine/cosine homes. **It is not literal private-byte identity.**
Retail's Z word at[-8,-4) and distance word at[-4,0) have no physical source
spills. Their values instead come from the actual source target-Z load at
instruction28 and squared-distance add at41. Both source instructions are
checked before capturing their value histories. Those histories start with
the related entry bytes, then follow the actual computed values. Retail's
Z reload is still executed; its value must match the source expression.

The corresponding source backing bytes at[-276,-268) must remain unchanged
and unaccessed; they are not silently discarded. The eight additional gap bytes
also remain unchanged and unaccessed, with an explicit gap-access rejection.
Snapshots cover all400 target bytes and both source obligations. Thus the
relation accounts for the different internal implementations without pretending
that either source-only area is physically identical to a changing retail spill.

At every service boundary, the proof compares the complete related frame. Previously exposed
query position and all88 burst/136 spray bytes may change again at later calls.
COPY observes and copies all eight extra bytes, including four never initialized
by this routine. It has a specified nonoverlapping copy contract. Public objects
are outside the callee's private frame; services do not inspect unpassed locals,
physical private-address bits or implementation PCs. The full deep providers
and complete larger caller remain unqualified boundaries.

FP equality is a **finite-value/data-dependency relation with equal per-epoch
operation multisets and stable per-call FP control**. Finite addition and
multiplication use commutative-value equality; subtraction and all data
dependencies retain operand order. Independent quiet-epoch operations may
reorder. **Raw FCSR flags, traps, NaN payloads, asynchronous effects and fault-
prefix identity are excluded.** Strict addition/product operand order and
strict FP-operation order are deliberately checked to fail. No hardware
status-equivalence claim is inferred from this finite-value result.

## Fresh paired qualification and controls

Both final configurations pass **five freshly rerun tests**, zero failures/
errors/skips: **98.284s primary /109.804s private
sibling overlay**, with **336 /
336 imported tool fingerprints**. The C changed,
so the old four-check receipts are not reused as current-source validation.
The five new artifacts are sealed; all seven frozen semantic files remain exact.
The overlay uses339 matching sibling files,463 primary fallbacks and five task
files. Real sibling HEAD/status and343 dependency fingerprints remain exact.

- Complete owner/source/binding and independent original assembly checks:
 434/392 versus438/384,63 bindings, all seven neighbors and pools retained.
- **1,920 guest cases per raw/retail stream**, complete88/136 descriptors,
 all eight extra bytes, public memory, service mutations, saved ABI and returns.
- **384 SDK32 cases each at O0/O2/O3**, strict aliasing and UBSan, independent
 retail transcripts, six public windows and ten effective native controls.
 Native observes78/132 initialized packet bytes and four extra bytes;
 untouched-byte observations remain guest-specific.
- **1,920 cases per stream through the genuine16-word func_151321D0 window**
 at15132278..151322B8, including D_80089914[1]'s actor argument, selector0/gate
 skips, callback return-to-gate wiring, flag reload and saved ABI.
- The complete77-path private/finite relation and **16 effective controls**:
 nine actual word changes (duration, copy, volume, timer, query height, tag byte,
 destination height, factor address and source-gap access), four private/history
 projection changes, and three explicit FP-order boundary checks. Unsupported
 opcodes and unbounded paths are not accepted as effective negative evidence.

## Current instruction inventory

After applying only the measured frame/private-address correspondence, the
434-word source inventory differs from retail by one ordinary BEQ versus one
BEQL, plus retail's Z store/reload at SP+0x178, distance store at SP+0x17C and
an additional spray-pointer setup at SP+0x74. Those four added instructions
account for the length gap. The remaining opcode, immediate and relocation
counts agree. The packet's `current-instruction-inventory.json` records this
fresh434-word result; the older437-word inventory is historical.

This diagnostic ignores register allocation, scheduling and branch destinations.
It does not establish a literal fit or authorize guards. The complete relation
above and a separately verified source-derived instruction mapping remain
distinct requirements.

## Preserved production and next work

All1,770 protected inputs remain unchanged, including every production source,
object, guard/history row, progress classification and protected data owner.
The production ELF remains
`186db0ca0f869b6c10bad8f36beb4006859748c3cc110b76babda6fac3e5d42f`. The previous actual matching count is
retained against that unchanged ELF; no new matching gain is claimed. Fresh
`make tools-check` passes. Root README SHA remains
`697062f2ee3651495ca1fd30f9f6bbbcc079a5e1904498a015dafadfce566d4b`.

The native Graphify refresh exited1 after refusing a27,123-node replacement
of the existing66,420-node graph, preserving the original. Scoped AST refresh
and explicit target-reference retention are recorded separately; no forced
overwrite or full-corpus re-extraction is claimed. Routine
work uses zero Claude calls and no REA reconfiguration. The sibling's dirty
work, host captures, frozen Release and real saves remain preserved.

Continue **this function with the434-word cached-factor body**. Derive the
438-word fit from source fields, including the two spill histories and branch-
delay setup, without embedding a retail replacement-word array. Then qualify
both real padders, symbolic rebases/controls and relevant real children; run
actual Make, independent strict image and production audits before installation,
fresh recount, aggregate README updates or matching credit. Tools are committed
before the consumer; the85% goal stays active, without automatic pause or push.
