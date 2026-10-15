# Texture Vertex Span Reconstruction And Private Boundary

## Scope And Steps

Continue the full additional-source/Game objective from clean consumer322d6b6d/
toolsc526e84. The previous turn was verified progress: Note1379 recovered the
matrix pass and its original product dependency. Now inspect all339 words of
func_1510BF60 at1510BF60/ROM139410, frame0xA8, before attempting installation.
Keep the archive read-only, unrelated mirror work intact and host Release frozen.

1. [x] Audit the full original scanner, resolver interface, actual direct calls and additional-source representation.
2. [x] Reconstruct the complete state machine in private semantic C, preserving the backward cursor and nested texture behavior.
3. [x] Screen23 complete compiled forms/controls and qualify the selected draft in guest/native32, packed fields, aliases and effective negative controls.
4. [x] Identify the exact remaining literal/private boundary; keep all production inputs and match totals unchanged.
5. [x] Bank tools first, consumer pin/docs next and post-bank evidence last; continue fitting THIS function rather than skipping to an easier target.
6. [ ] Match private homes, register lifetimes, instruction scheduling and full state/prefix behavior; pass both padder/rebase and independent image gates before installation or credit.

## Original Interface And State Machine

The additional source uses GLOBAL_ASM for this routine, not a reusable C body.
Its file SHA-256 remains4c7932ef. Preserve the public address-keyed name and
infer a private typed interface from original instructions and direct callers:

```c
s32 func_1510BF60(Gfx *commands, s32 resource,
                 u32 *firstVertex, s32 occurrence);
```

Call1510D0EC(resource,&extent,3,0) for its side effects, ignoring its returned
address. Clear *firstVertex AFTER this call. The current actual resolver C is
read for interface evidence, but is not executed by this batch's bounded
provider tests. Do not claim actual allocation, loading or decompression.

The scanner visits three states:

- Search signed command opcodes for the requested occurrence of texture-image
  command0xFD whose payload equals the live D_800B0E58[resource] entry. Opcode
  0xDF before any match returns0. Only matching texture commands decrement the
  occurrence; negative/zero occurrences select the first match.
- Scan forward to vertex opcode1 or a triangle opcode5/6/0x1x. If a triangle is
  found first, search backward for a vertex command and decrement nesting for
  each texture command crossed. In BOTH cases resume ONE COMMAND BEFORE the
  located vertex command. A common-tail increment would incorrectly cancel
  this decrement, losing the preceding command's effects.
- Track unsigned vertex addresses, reset the maximum on each vertex command,
  decode3/6/12 triangle indices and trim the first address only once at nesting0
  after a backward search. A later texture command ends the selected span only
  when incremented nesting becomes positive; opcode0xDF also ends it. Preserve
  the exact unsigned-wrap then signed-shift span calculation, not an invented
  global range over every earlier vertex block.

Original direct calls at ROM139A0C/139BB0 supply display lists D_800B0E00/04,
resource identifiers, a shared output home and occurrence0. The returned count
and first vertex feed texture-coordinate copies. The actual caller1510C4AC is
still a production placeholder; these are original call-site facts, not actual
caller/gameplay acceptance.

## Source Fit And Open Boundary

Use experiments/game_texture_vertex_span.py and tests/game_texture_vertex_span*
in the pinned tools repository. The immutable18-input capture lives under
conker/build/game-texture-vertex-span; never recapture current state or modify
its before fixtures. Existing IDO, parsers, native32 and MIPS helpers are reused;
no compiler, profile, header or REA configuration changes.

The first corrected complete draft is343 words/frame0xA8 with281 word
differences. Separate pointer limits are hoisted into saved registers. Sharing
a meaningful indexEnd variable removes two saved-register lifetimes and gives
the selected explicit-shared-end form339 words/frame0xA8 with259 differences.
All saved-register prologue words and entry resource home match, but the extent
pointer is SP+A4 rather than retail SP+A0; the index array is SP+70 rather than
SP+58, and vertexBase is SP+A0 rather than SP+94. The maximum/count register
roles and end-opcode/return schedule also differ. Equal length is NOT a match.

All23 compiled forms/controls have zero IDO diagnostics. The shared-layout-2
declaration-order control reaches258 differences but does not close the private
boundary. The338-word shared-span-local control and other size/profile shapes
are not substitutes for the retail339-word routine. Not all shape-screened
controls are semantic candidates; only the selected body is fully qualified.
Do not add hundreds of broad guards, fake arrays, physical register bindings,
volatile qualifiers or profile changes to conceal the remaining work.

## Behavioral Qualification

All14 selected research/prior-checkpoint checks pass43.598s. This comprises the
nine scanner tests, two consumer-independent tests and the three preceding
matrix-pass image/corruption/inverse gates. Shared project-tools checks pass.
Earlier separate seven-check42.858s and two pure0.004s receipts are not counted
as a larger fresh suite.

- 3,872 guest cases compare original versus raw C public memory, return values
  and public provider fields across two SP phases. The private extent pointer
  is checked for a valid stack address, NOT literal pointer equality; its
  different SP offsets are an explicit open boundary. Cover occurrences-1/0/1/2/
  INT_MAX, four external provider modes, signed opcodes, unsigned address
  boundaries, all packed fields, nested texture occurrences and vertex resets.
- All336 normal-entry reachable retail words execute. The three unvisited
  duplicate words1510C044/C098/C210 have no direct branch entry and each follows
  an unconditional branch plus its delay slot. This is a checked normal-entry
  CFG boundary, not a claim about arbitrary jumps into a function's middle.
- Actual scanner C passes1,936 native32 cases per O2/O0 profile, checking all148
  backing words, provider arguments and canaries. Exactly three signed-byte
  opcode loads receive an explicit big-endian opcode bridge; all other body
  text is retained. This is an endian-adapted native test, not native MIPS.
- Another48 guest cases and24 native cases/profile cover eight resource slots
  with output aliases into cache entries and display-list payloads. No private
  stack alias or hardware behavior is inferred from them.
- Seven compiled wrong bodies fail by completed semantic mismatches under IDO
  and native O2/O0: cached texture before the provider, unchanged occurrence,
  wrong packed shift, wrong trim stride, skipped preceding command, signed
  vertex comparison and output clear before the provider. Every native witness
  returns2; crashes are not accepted as evidence.
- Full private return state differs. Of63 paired fired access prefixes,56 differ;
  the first is cut7 at1510BF9C in both executions, with no branch delay. The
  provider has already written distinct private extent homes. Do not describe
  these public-state tests as full scheduling/fault equivalence.
- All13 other raw owner functions, pools, sizes and relative relocations remain
  fixed. Both padders preserve the339-word candidate, including its nonmatch;
  they do not turn it into retail or qualify a production installation.

## Defined-Input Limit

A texture command immediately followed by a vertex command can revisit the
texture before establishing vertexBase and reach the span return with an
undefined local. The independent reference rejects that input. Actual original
machine execution returns different poisoned-stack results at the two SP phases
(85337913 and4255035313). Do not initialize production to invent a retail fix.

Native GCC correctly reports vertexBase may be used uninitialized. The harness
retains that diagnostic and demotes ONLY maybe-uninitialized from Werror; all
other warnings remain errors and any unexpected warning fails. It never calls
this malformed-input path. Ordinary native tests therefore pass only in the
explicitly defined vertex-base domain. Keep signed-extreme occurrence overflow,
private stack aliases, invalid memory, hardware exceptions and actual resource
loading separate from this bounded evidence.

## Preservation And Banking

Every one of18 production input hashes remains fixed, including ELF2131709f,
progress3ad7466c, all guards, both recent owners and original product assembly.
No production C, assembly, header, profile, layout or progress row is changed.
Game2,884/4,829 (59.72%), total3,557/5,502 (64.65%), different1,945, zero drift
remain the last verified production numbers. Root README is deliberately
unchanged because this private reconstruction earns no new match credit.

Freshly verify all801 archive fingerprints. Verify all565 initial dirty mirror
fingerprints and independent ddbdd16 HEAD, confirm five new owned paths absent,
then copy exactly those five. All565 older fingerprints/HEAD remain fixed,
leaving570 expected dirty paths. Five files compile standalone and two
namespace-bound pure checks pass. No reset, mirror commit or history duplication.

The full graph update refuses19,177 versus40,959 nodes and retains19,398 nodes
from2,972 excluded-but-present files. Do not force the smaller graph; await the
consumer's incremental commit worker. No push, Claude call, setup retry or host/
Release operation. The full additional-source/Game and rectangle queues stay open.
Tools1ffbc44 banks the five owned research paths first.

## Post-Bank Verification

Tools1ffbc44 precedes consumer2f46d35a, which banks only the tools pin and
documentation. All7 selected post-bank private-boundary, immutable-production,
undefined-domain, output-alias and preceding matrix image/corruption/inverse
checks pass28.561s. Incremental ELF/progress are up to date. All six Note1379
installed hashes and every18 captured production inputs remain fixed. Both
active checkouts are clean before this receipt; the mirror's entire570-path
dirty state and independent HEAD remain unchanged since the exact owned sync.
The incremental graph worker completes at40,970 nodes/81,131 edges/3,758
communities without forcing the smaller full scan. No producer remains live.
No push, archive edit, mirror-history mutation or host/Release operation.
Continue the same scanner; this checkpoint is not completion of the wider goal.

## Next Action

Continue THIS func_1510BF60. Recover the stack allocation and live maximum/count/
end-opcode roles from the339-word original before choosing any normalization.
Re-run full private and fired-prefix checks after changes, then qualify actual
resolver/caller connections, both rebases and an independently constructed
whole-image delta before production edits or additional C-match credit.
