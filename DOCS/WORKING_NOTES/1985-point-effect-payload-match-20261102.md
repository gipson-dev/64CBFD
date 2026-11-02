# 1985 - Attached-point particle payload recovered as guarded C

Verified2026-11-02. Production **4,052/5,507(73.58%)**; Game **3,379/4,834
(69.90%)**, Init492/492, Debugger181/181, zero address drift,1,455 different.
One installed match, unchanged C inventory. **79 more** reach4,131/5,507 and75%.
The wider goal remains active; this checkpoint is progress, not completion.

## Recovered interface and payload

`func_15193660` in generated_1C0B10.c is now
`void func_15193660(u8 *owner, s32 mode, s32 extra)`.
Its original101-word slot is VA15193660..151937F4, ROM1C0B10..1C0CA4,
with152-byte frame. Both incoming argument homes retain full32-bit stores.

Gate null owner, zero ownerword0 and null attachedpointer at owner+1D4.
Resolve attached point10 through func_15142314 into payload.position, then
initialize a120-byte local particle descriptor. First words are now accurately
named **baseCount=8** and **countRange=7**: the original consumer computes
baseCount + RNG % (countRange+1), requesting8..15 particles. Other field names
retain offsets where gameplay meanings remain unknown. Nine global floats
D800A81C0..D800A81E0 are captured after the point resolver, not before it.
Pass the local payload, low mode byte and full extra word to func_15152520.
The mode/extra homes are reloaded after the resolver, preserving guest changes.

All118 defined bytes, including point coordinates, signed halfwords, eight
color bytes and four positive-zero float words, are initialized. Final bytes
+76/+77 remain untouched. Native tests never inspect uninitialized padding;
guest execution compares the full120-byte packet and its access trace.

## Source shape and checked normalization

The initial source emitted100 words/frame152. Two zero groups spelled alike
were merged into one FP register definition. Using integer-zero expressions
for values[0]/[3] and float-zero expressions for values[5]/[8] recovers both
retail definitions and the full101-word length. Assignment grouping preserves
literal load/store order and the late mode/extra reloads. The first two field
names were refined after observing the complete original count calculation;
raw instruction identity and the complete linked image were reverified.

RawSHA256:
`2dc0abcb7bb9b7465c0dc27a06e64724908e7a45cdfda395c10b59e825df5c79`.
Eighteen expected-word guards normalize only:

- Three words of one dead caller-scratch pointer role (A3 versus V0).
- Twelve words closing the FP0/2/12/14 definition-and-store role cycle.
- Three independent LUI/constant setup words. The D800A81E0 HI16 relocation
  moves with its instruction; expected and replacement binding sets are checked.

No inserted/omitted instructions, frame changes, rewritten payload addresses,
functional patches or padding compensation. Guard history is preserved, with
exactly18 new rows for this function. Independently assembled original,
normalized and raw objects are GNU-linked at three code/helper/global layouts,
including signed-low-half carry boundaries. Original and normalized slots
match all404 bytes; the ordinary raw source is qualified separately.

The committed symbolic interpreter walks all101 instructions and derives63
ordered observations. All reads, store addresses and values, branch predicates,
helper arguments and saved-register roles agree. Calls occur at34hex and17C.
It models both delay slots before observing arguments and caller clobbers after
calls. Raw dead caller-scratch registers are deliberately not equated. FP role
changes are bit copies, not arithmetic reassociation; the saved FP bank is fixed.

## Fresh qualification and limits

- Root:1,187 cases across three layouts,3,561 cases/10,683 executions across
  original, normalized and raw C. Every101 root words, every mode byte and125
  access-prefix triples execute. Full memory, calls, packets, traces and saved
  roles agree; original/normalized complete machine state agrees. Lazy invalid
  gates leave later reads unmapped. Cases include full-width owner gates,
  null attachment, point-provider global/owner changes, guest home/padding
  probes, finite/subnormal/signed-zero and NaN constant-word copies.
- Real helper chain:112 cases/336 executions combine all49 words of the
  retained byte-exact point resolver and the213-word original particle factory
  from ROM. Both float and fixed-point matrix paths execute. All258 non-trap
  helper words execute; four division traps are unreachable for this descriptor.
  Counts8,9,15 exercise repeated loops. An independent reference calculates
  every spawn argument and complete88-byte descriptor/48-byte vector snapshot.
  Integer/float RNG, spherical-vector output and final spawning remain explicit
  opaque providers. These checks do not claim actual gameplay or full providers.
- **The particle factory remains an unrelated zero-return stub in production.**
  Its ROM body is executed only by this test. It receives no restoration or
  matching credit here, and the strict image audit proves it is unchanged.
- Native32:336 cases at each O0/O2/O3 with UBSan, typed owner/attachment layout,
  fences,118 defined payload bytes, finite points and coefficients. Nine
  effective controls per profile reject missing/null/byte-width gates, wrong
  point index, early coefficient capture, mode, extra, signed field and zero sign.
  Native probes exclude inaccessible guest argument-home/padding changes;
  no native NaN/FCSR or portable uninitialized-padding claim.
- Complete aligned-ROM census: JALs at15029198,150700FC and150997C8; no literal
  target pointers. Windows8words@15029188 and4@150997C0 plus complete12-word
  wrapper150700E4 each216cases/648exec (648cases/1,944exec total). The first
  route reads a dynamic mode byte and passes extra0; other routes passFF/1.
  The wrapper loads D800D154C and uses its original24-byte frame. Both large
  parents remain bounded-window checks, distinct from gameplay acceptance.

## Actual Make and complete-image closure

All three raw and padded neighbors and owner pools remain identical, with zero
owner compiler diagnostics. Three actual Make commands reproduce the qualified
object exactly. The entire linked ELF is reconstructed from the frozen baseline
by replacing404 target bytes, changing its symbol extent12->404 and applying
nine closed symbol/name table permutations. Every named definition is preserved;
no bytes or dependent objects are excluded. All6,052 addresses,6,051 other bodies,
189,088 protected bytes and720 data owners remain fixed. The map is reproduced.

The explicit metadata groups are pinned in the committed verifier and checked
against their original contiguous name strings and complete definition fields.
Code, final-byte and every metadata-group negative control are rejected.
Production Make and Native-mounted ELF recount agree. Before documentation,
all17,805 old sealed files were audited: only target source, target object,
guard CSV and ELF changed. No unplanned dependent-object deltas.

ELFSHA256:
`6ed3289ece934063956b8dfac11c99799e7cb6fd72ae7ed46c5a474784bfb16a`.
Both tools copies pass five fresh focused methods plus shared tools checks.
After installation, each passes two fresh compile/image methods; unchanged
semantic checks are reused with current source/code/preparation fingerprints.
Thirty canonical preparation artifacts and1,121 focused inputs are pinned.

## Bank and next action

Build evidence: `conker/build/game-point-effect-payload-15193660-match/`.
Current heads, Native/cache seal, graph-retention proof and resume instructions
are in BANKED_STATUS.json, FINAL_AUDIT.json and HANDOFF.md. Tools are committed
before the consumer pin; no push. README receives only aggregate rows; detailed
recovery stays here with concise links in the five status indexes.

Next **func_15152520**, generated_17CAF0.c:213words/frame256, ROM17F9D0..17FD24.
Its complete original consumer is decoded in the new oracle: particle count,
random lifetime/angles/radius/velocity/scales, spherical-vector provider and
nine-argument final spawn call. Source is still a stub. Recover its ordinary C,
qualify the helper/caller ABI, signed widths, RNG sequencing, original branches
and live payload reads, native controls, raw/padded owner, actual Make and full
linked image before installing or awarding any credit. Do not replace that
work with the current test's mocked RNG/vector/spawn implementations.
