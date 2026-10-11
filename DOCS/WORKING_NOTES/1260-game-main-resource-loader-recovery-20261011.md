# Game Main Resource Loader Recovery

Date: 2026-10-11. Continue
[Note 1259](1259-game-resource-extras-loader-direct-match-20261011.md)
under [the agent workflow](../AGENT_WORKFLOW.md). Previous goal turn made
verified progress and banked the complete extras-loader direct match.
Single Codex writer, zero Claude calls. Full Game matching goal stays active.
Commit authorized checkpoints tools-first, no push.

## Complete Scope And Baseline

- Full func_1503CF20: VA 0x1503CF20..0x1503D368,
  ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes, retail frame 0x78.
- Owner conker/src/game/generated_6A3D0.c; complete asm/6A3D0.s lines 11..308.
- Consumer entry HEAD fba6e3c95981ded3cbadb131a8b25e44317811ee, clean.
- Mounted tools entry HEAD 563924a549deca698404ad5955cde2b6f1feabb0, clean.
- Older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a,
  287 dirty entries; preserve all existing work.
- Old C is a 12-byte zero-return stub. This recovery covers the complete
  routine, not an easier neighbor or only the successful loader prefix.
- Baseline ELF SHA-256:
  8b43e9619177ab0f1a8065094300796e24d39d51ca4fc929d37124bbcd1c0dcb.
- Baseline owner SHA-256:
  a0b5a3b085da38a972e866ad6b1d1fbaba284eca12389297b88ef324c86a8fdf.

Freeze original source/ELF/guard/progress/rodata/symbol/layout/auto-assignment
bytes and hashes in ignored game-main-resource-loader-test. The original
baseline is immutable, including after installation. Inspect both complete
retail call sites at 0x1502DC0C and 0x1503DAF4: identity, unused word,
config pointer, extras word, unsigned actor flag byte promoted to fifth word.
Refine the owner forward declaration accordingly. Recover the auxiliary
helper's s32 return declaration; the older caller still ignores that result
and its entire compiled fingerprint is unchanged.

## Complete Behavior

Return zero for identity 0xFF, signed identity >= 0xBB or an already-present
main table entry. Do not invent a lower-bound/nonnegative check. The unused
second word is homed by retail but has no subsequent semantic read.
Request func_1502B6BC(&output,7,NULL,2,1,identity); NULL returns error one.
Publish block +0x38 into the main resource slot.

Publish header words into all six pointer/word tables in retail order,
then unsigned/truncated size/count tables. The boundary selects the published
first table word, falling back to the published primary descriptor base.
Preserve modulo-32-bit subtraction and logical shift before u16 truncation.

The primary relocation loop starts with the newly stored truncated count,
then rereads live unsigned D_800C4778 after each child callback. Reload the
descriptor base separately before relocation and before reading the child.
The secondary loop uses a cached unsigned header word count, but still
reloads its live base. Header changes after that cached read cannot shorten
this loop. Recover the separate four-byte cursor and index lifetimes.

Publish extras count as unsigned division by 12/truncated u16 and another
count as logical shift by four/truncated u16. Nonzero extras invokes the
complete banked func_1503DC3C. Only a zero result runs the live-count/list
event loop with five arguments (value,0,0,0x3E,0).

Gate subsequent helpers on zero error. Ignore func_1503D984's return, preserve
func_1503D804's failure. Config +0x18 bit 0x4000 or fifth-word bit one gates
func_150028BC; any nonzero return sets error bit eight. Preserve later
two-word helper calls and their error propagation/short circuits.

On failure, conditionally free D_800C6360 without inventing a NULL store
to that table. Call func_1503DD1C, then reread auxiliary/secondary slots,
conditionally free and NULL each. Finally reread the main slot and free
its current pointer minus 0x38, then NULL it. Callbacks can change future
slots or the current main pointer. Return the accumulated error.

## Compiler Recovery, Not Yet Matching

Keep the existing -O2 -g3 -Wo,-loopunroll,0 owner profile. No Makefile,
shared compiler/helper, layout, symbol or word-guard edits.

| Complete Candidate | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Indexed loops, early error initialization | 288 | 0x88 | 286 |
| Separate loop offsets | 286 | 0x88 | 268 |
| Explicit initial-count and cached-count gates | 285 | 0x88 | 281 |
| Indexed loops, late error initialization | 275 | 0x88 | 250 |
| Separate offsets, late error initialization | 273 | 0x88 | 236 |
| Explicit gates, late error initialization, selected | 272 | 0x88 | 273 |

The selected complete body fits the 274-word slot and preserves the initial
count-store branch without an extra public count read. The lower-difference
273-word form is not substituted for this access-order qualification.
Error initialization occurs where it becomes live; it does not drop a path.
Register hints, signed/unsigned local variants and typed helper declarations
did not solve the original register allocation. These are measured candidate
results, not a proven explanation for the compiler's spill decision.

Current target: 272 emitted words / 1,088 bytes, frame 0x88 instead of retail
0x78, 273 raw word differences, no guards. Padding contributes the two unused
tail words only. This is a semantic recovery, not byte-exact matching.

## Fresh Qualification

Ten pre-install tests pass in 20.825s. Ten post-install tests pass in
27.839s; the final ten-test run including an explicit no-target-guards check
passes in 23.402s.

- 1,021 independent-reference cases / 2,042 original/raw executions cover
  all 273 reachable retail words. The remaining 0x1503CF68 comparison is
  statically unreachable: the likely branch skips it on non-0xFF identity,
  while the 0xFF path returns through the preceding unconditional branch.
- Thirty live-loop/cleanup cases / 60 runs: primary growth/shrink, multiple
  base rebindings, cached secondary count under header mutation, event count
  changes, helper return widths, optional cleanup and changed main pointer.
- 175 argument/size/alias cases / 350 runs: signed/wrapping identity words,
  config/fifth-flag/extras gates, unsigned shifts/division/truncation,
  header/publication and table/count cross-role aliases.
- Nine independent original/raw/padded links, three symbol sets and 24
  rebase cases, including signed-LO carry.
- 1,800 fired public-access fault pairs: full public partial memory, access
  and helper-call prefixes compare. Different private frame accesses are
  explicitly not paired. This is emitted guest order, not portable C faults.
- Ten effective freshly compiled IDO negatives: signed identity, presence,
  request kind, publication offset, stale count, extras gate, config mask,
  auxiliary error bit, omitted main free and clearing before free.
- Actual complete native32 C: 6,048 cases at each O2/O0, 12,096 total.
  Compare every modeled memory byte and normalized helper-call trace with
  an independent reference. Missing-main-free control fails effectively.
- All 14 before/after owner neighbors preserve bytes/extents/relocations/
  pools. Isolated/owner target fingerprints agree, zero diagnostics.
  Both actual layout/generated padders preserve every non-target owner byte.
- 768 connected cases / 1,536 runs through actual complete parent, main,
  extras, relocator and buffer code. Map 104/274/56/9/194 words; measured
  reached counts are 41/256/56/9/140 respectively. Compare independent
  parent/main/extras/relocator/buffer memory, access/call and failure results.
  Do not claim every mapped word is dynamically reached by that fixture.

Fixture corrections occurred before installation: the first model buffer
was accidentally placed at STACK; move it to 0x50000. Rebase all actual
objects for cross-table aliases, not only the reference symbols. Insert
needed forward declarations before the main body, not after it. The native
resource header allocation must include the rebound +0x78 pointer's storage,
and dictionary symbol merges must tolerate shared names. No test gate was
disabled to resolve these failures.

Large-count cases shrink via a callback after the first iteration; they do
not claim 65,535 descriptors. Contrived wrapping/negative identities are
emitted-O32 guest cases, not portable C array-domain guarantees. Native32
uses valid modeled identities 0,7,186 and actual four-byte pointers.
Only the private request-output pointer is normalized between frame layouts;
all public memory values and call arguments are compared.

Prior caller/extras/buffer whole-suite receipts remain prior evidence, not
fresh whole-suite runs here. Their installed bytes, guards and helper tools
are unchanged; fresh connected tests and the complete ELF audit cover this
change. Resource request, child relocation, auxiliary/cleanup and allocation/
copy/free internals remain explicitly bounded. No full heap/hardware/renderer/
gameplay or 64-bit host-port acceptance claim.

## Linked Audit And Unchanged Totals

Extent changes 12 -> 1,088 bytes; ELF length remains 3,261,160.
Exactly 828 ELF bytes change: 816 target bytes, two extent bytes and ten
verified existing metadata-order bytes. The receipt's 12 metadata bytes
include the two extent bytes; do not count those twice. Check complete
headers/sections, symbol/name counters and all values, plus the sole target
extent change. Every other ELF byte is identical.

- New ELF SHA-256:
  61eb09430a85aed3fc5fa0229ba87c9bbf749876c396e7f1cd0fe4b277f3be39.
- New owner SHA-256:
  be9b10d5893d895bd5c70ec40e7fdad8b92d43bd9fd5988cfa122b39cc2ff863.
- All 189,088 protected data bytes / 720 owners exact, SHA-256
  0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
- Guard SHA-256 unchanged:
  5eace9a1e712613397671e3d8d61acfcbd1ceaa4a7a73d4377b15d97ff7400c6.
- Conversion CSV unchanged:
  32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
- Rodata source, tracked symbols/layout and ignored auto assignments exact.

Fresh matching unchanged: Game 2,789/4,822 (57.84%), total 3,462/5,495
(63.00%), Init 492/492, Debugger 181/181, zero drift / 2,033 different.
No matching or conversion credit. The old stub was already counted as C.
Root README aggregate rows remain correct, so it is unchanged.

Build and consumer/mounted/older WSL tools checks pass; native new-file
py_compile passes. Keep the existing duplicate generated_12D630 recipe
warning. No native full-check or warning-free full-build claim.

## Ownership And Graph

Tools commit b50347469279bab389e3f67a56f2260b3e99b548 banks only the new
candidate module and focused test before the consumer pin. Copy only these
two absent paths into the older standalone sibling using absolute paths.
Its HEAD and all ten protected existing hashes are unchanged; dirty entries
287 -> 289. No overwrite/reset/older commit or push.

Native Graphify query succeeds, 19 nodes. Native update re-extracts two files
but refuses unsafe shrink 39,751 -> 17,969; retains 19,398 nodes from 2,972
existing excluded files. Preserve version/devcontainer warnings, no force,
purge or install. Before close-out, wait for the consumer commit's detached
hook with fresh log bytes/UTC, fresh Rebuilt tail and zero actual workers.
No OGL/Release/save/editor/private-input changes; Release remains frozen.

## Continue This Same Function

1. Recover the original 0x78 frame and saved S6 error lifetime. Current C
   saves only S0..S5 at +0x1C..+0x30 and RA +0x34; retail saves S0..S6 at
   +0x20..+0x38 and RA +0x3C.
2. Recover private request output and shared scratch layout: retail output
   +0x6C, current +0x84. Retail main-slot/word-offset spills +0x58/+0x5C,
   current +0x48/+0x4C. Preserve every alias/access/callback gate while fitting.
3. Restore the retail 274-word schedule, including unsigned initial-count
   handling, cached secondary bound, argument homes and branch-delay joins.
4. Requalify copied owner, both padders and full linked audit before changing
   guards or claiming any matching credit. Do not use opaque instruction rows
   to mask the broad compiler-layout mismatch.

Keep complete func_1503CF20 as the next target, not an easier neighbor.
Actual deeper helper implementations and runtime acceptance stay separately
open. This recovery does not complete the wider Game matching objective.
