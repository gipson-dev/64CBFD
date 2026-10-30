# Note 1871: record signed halfword approach match

2026-10-30. `func_151193F4`, owner `generated_142560`, replaces its zero-return
placeholder with a recovered `void(u8 *record)` callback. VA
`0x151193F4..0x151194D4`, ROM `0x1468A4..0x146984`: 56 reachable words,
224 bytes, no frame, no helper calls, no alignment tail. The existing O2/g3
owner profile is unchanged. Tools commit: `06f91d2a50aff93c4e58c34fb4fe436e128bb62b`.

## Recovered behavior and interface

The routine initializes record word `+0x84`, when zero, from signed halfword
`+0x12` with bit 31 set. This initialization occurs even when step `+0x7C`
is zero. A nonzero signed step enables the update. The upper 16 bits of word
`+0x3C` are unsigned; their product with word `+0x80` wraps to 32 bits, then
is interpreted as signed and divided by 256 with truncation toward zero.
The signed low half of `+0x84` supplies the origin. Both signed-current and
signed-origin boundaries are retained, including negative fractional products.

Before comparing current and target, byte `+0x73` clears its low two bits.
An already equal current value sets both bits. Otherwise the halfword moves
toward the target, clamping only when the signed distance test passes.
Arrival during this update leaves those bits clear until a later invocation.
Negative and full-width steps retain retail's wrapped add/subtract behavior;
the C uses unsigned arithmetic for these potentially overflowing operations.
The apparently redundant `|= 0` preserves retail's final byte read/store.
No speculative actor or gameplay role is assigned to these record fields.

The aligned retail ROM has no direct JAL to this function and one literal
pointer, ROM `0x22D918`, VA `0x80088E58`, in slot 38 of `D_80088C90`'s
12-byte callback entries. Original installer window `0x1509EBBC`, 22 words,
places the pointer at record `+0x38`; original dispatcher window
`0x15113EE0`, five words, passes the record in A0 and ignores the callback's
result. Both windows are checked against complete assembly source and run
connected to original, raw C, and normalized bodies. The current installer
and dispatcher remain placeholders: no complete parent equivalence is claimed.

## C generation and normalization

The source is complete semantic C. Its raw 56 words have SHA-256
`75ee1936079c6e53d007dab8bf6bd8939c4d9b8bdb6d7ab937b2acb7e96b92bb`.
It has no relocations, stack frame, or inserted/omitted instructions.
Thirty-two expected-word guards recover temporary register allocation,
independent scheduling and a commutative comparison operand order.
Normalized words match retail SHA-256
`04f2a46ec718998596a88ba7724c6b408f323f24453b2a0c5a391c0fdeff78ad`.
This is normalized byte-exact C, not a direct raw compiler byte match.
All previous CSV bytes are preserved as a prefix. No compiler, profile,
layout, shared declaration, or original assembly is changed.

A separate symbolic interpreter decodes every supported instruction in this
closed integer leaf into explicit 32-bit operation DAGs. It explores both
outcomes of each nonconstant branch, including infeasible combinations, and
compares branch predicates, record read/write traces, final writes, HI/LO,
and preserved registers. All 22 terminal paths and 56 words agree. The proof
uses no sampled input constraints or solver assumptions. It does not claim
that the raw temporary GPRs match; its domain is the record-relative integer
leaf, with disjoint fields and MIPS arithmetic right shifts. Independent
guest and native execution additionally check the hand-written reference.

## Qualification

Ignored evidence: `conker/build/game-record-halfword-approach-151193F4-match/`.
The coherent private producer is `semantic_v21.py`, with zero exit status.

- Guest: 2,968 cases / 8,904 executions across original, raw, and normalized
  bodies; all 56 words covered. Public memory and every own memory access
  agree for raw C. Normalized and original complete register states agree.
  Forty-eight access-prefix cuts include seven branch-delay cuts. Signed
  boundaries, flags, disabled/initialization routes and stack-relative record
  placement are included. This is instruction-model evidence, not portable
  C fault or hardware acceptance.
- Callback: original 22-word installer and five-word indirect call windows,
  slot 38, 64 connected cases per body; A0 record and void-result contract,
  subsequent caller increment, and memory results agree.
- Native: 524,288 cases at each O0/O2/O3 with trapping UBSan and checked SDK
  32-bit record offsets. Every halfword input and flag byte is exercised;
  unsigned products, signed division and wrapped steps have independent
  expected results. Nine effective native controls and nine IDO-compiled
  controls reject wrong signedness, rate extraction, rounding, direction,
  flags, and initialization tagging.
- Guards: all 224 raw-byte corruptions plus length, relocation, owner and
  function negatives reject through the full-body fingerprint. Actual padder
  rejects all 32 bad word preimages, one bad binding and one foreign function.
- Owner: all 83 other raw/padded bodies and constant pools are preserved.
  The five actual Make commands reproduce the qualified padded object.
  Selected, owner and executed-command diagnostics are empty. The known
  duplicate `generated_12D630` recipe notice remains in the Make plan.
- Both tools copies: eight fresh canonical target checks and shared tool
  checks pass. Production then runs two fresh installed checks in each copy;
  six unchanged semantic checks are reused only by full module/input/artifact
  fingerprint identity. Reused results are explicitly recorded as such.
- Full image: independently predicted before production; exactly 167 changed
  bytes, 166 in the target slot and one in its symbol extent. No metadata
  cycles or exclusions. All 6,055 other function bodies and all 6,056 function
  addresses remain fixed. All 189,088 protected Game-data bytes / 720 owners
  remain exact. Native adopted ELF and map reproduce the private prediction.

The initial private drivers exposed fixture-only issues: a missing cache-side
snapshot copy, assuming the previous owner's three-command rather than this
owner's five-command Make recipe, and using stack phase 1 instead of the
oracle's supported 0/8. Corrected fresh producers retain those failed receipts
and pass; no guard, compiler or test expectation was relaxed around a product
failure. Declaration permutations, narrow-load casts, volatile probes and
non-equivalent division/type controls remain ignored diagnostic experiments.

## Recount and continuation

Actual adopted ELF SHA-256:
`81837f4f25a6eb7560053415605197f957b3ed3cdd70423729891547536b7334`.
One new exact C function: **3,948/5,506 (71.70%)**, Game
**3,275/4,833 (67.76%)**; Init 492/492, Debugger 181/181, zero drift.
The 75% target is still 4,130/5,506, requiring **182** additional exact C
functions. Conversion inventory CSV bytes are unchanged. No parked candidate
receives credit. The root README changes only its two aggregate matching rows.

Tools are committed before the consumer pin and scoped source/docs commit.
The older tools mirror's 2,051 inherited dirty paths are preserved; only the
three new qualification modules are added, without a mirror commit. No push.
Graphify refresh is scoped to the eleven supported changed C, Python and
Markdown sources; CSV guards are separately bound by exact rows and hashes.
Retain all old nodes/valid directed relationships, retiring only the obsolete
placeholder s32-return edge. Communities and outside-scope freshness remain
historical; no full-corpus extraction or recomputed clustering claim.

Next private screen: `func_15007360`. The matching goal remains active.
Codex owns implementation and validation; routine task uses zero Claude calls
and no REA, browser, dependency, account, or host-port changes.
