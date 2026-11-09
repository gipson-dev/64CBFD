# Game rotated vertex quad guarded match - 2026-11-09

func_1513E13C now matches its complete **90-word / 360-byte** retail slot.
The complete semantic C emits **88 words**, retaining the natural **0x50-byte
frame**. **55 expected-word/relocation guards**, including two measured NOP
insertions, normalize floating register allocation, private spills and store
scheduling. This is a guarded match; raw compiler output is not byte-exact.
The conversion inventory is unchanged.

Fresh production totals: **4,295 / 5,513 (77.91%)** total and **3,622 / 4,840
(74.83%)** Game. Init remains 492/492 and Debugger 181/181, with zero address
drift and **1,218** different C functions. **116** more accepted matches reach
4,411/5,513 and at least 80%. README changes only these aggregate rows.

## Source and matching boundary

Owner: conker/src/game_169510.c. Original assembly:
conker/asm/nonmatchings/game_169510/func_1513E13C.s.
VA 1513E13C..1513E2A4; ROM 16B5EC..16B754. Preserve the seven-argument void
interface: struct210 output, center X/Y/Z, half width/depth and byte angle.

Name the first result sine and the second cosine. The actual quarter-wave
table starts at 1.0 and ends at zero: helper(angle - 64) supplies sine and
helper(angle) supplies cosine. Preserve the two calls, byte wrapping and fresh
argument homes. Keep the first result's measured reloads through a volatile
float and the reused x-minus/z-minus stack value through a one-element array.
Those are measured code-shape choices, not evidence of original variable names
or qualifiers. No artificial frame padding is introduced.

Compute each corner with the original float32 grouping; reassociation changes
values near 2^24. Truncate through explicit signed32 casts before narrowing
into the twelve signed halfword corner fields at +40/+50/+60/+70. Reuse the
truncated center Y for all four vertices. The explicit signed32 casts preserve
IDO output and express the retail conversion width before halfword wrapping.
The remaining record bytes, headers, helper and shared declarations stay fixed.

The previous C emitted 85 words. The selected form emits 88; all arithmetic,
calls and twelve stores already exist in semantic C. Guards append NOPs after
compiled offsets +0x0B0 and +0x0E8 to recover the measured MFC1 scheduling gaps.
Both inserted words are zero, and no word is omitted. Positive guest cases
visit all 88 raw and all 90 normalized/retail root words. The instruction model
does not qualify hardware interlock timing or full private-state equivalence.

## Focused checks and callers

Six focused checks pass before and after installation in both tools
environments. The sibling run uses a read-only overlay for the six new
modules. Each receipt fingerprints task modules and loaded dependencies.
No unrelated legacy suite is described as freshly executed.

- Independent guest geometry: **694 cases per raw, normalized and retail
  body**, **2,082 executions**, plus **768 connected runs of the original
  27-word trig helper** and **24 independent entry/helper/table/stack rebases**.
  Verify the installed helper equals retail. Cover every angle byte, upper
  incoming angle garbage, negative extents, signed truncation, wide legal
  coordinates, halfword wrapping, helper-entry record snapshots, callback
  clobbers, guest-only incoming-home mutation/retargeting, caller-stack output,
  all public bytes and saved-register/stack contracts.
- Native32 O0/O2/O3 with UBSan: **6,144 geometry/callback cases per profile**,
  real SDK struct210 layout, complete record canaries and ten effective source
  controls at every profile. Controls catch wrong quarter direction, stale trig
  result, coordinate, truncation, corner sign/stride, width, reassociation,
  early output and padding writes. All ten IDO-compiled variants also have
  independent guest witnesses; compiler/interpreter errors are not witnesses.
- Both padders reject every stale expected word and a stale relocation:
  **56 rejections per padder**. Missing/corrupt inserted NOPs fail the complete
  target body/extent gate, four controls per padder. Four whole-image byte
  corruptions and invalid payload/bindings/scope are rejected.
- Retail census finds two aligned JALs, ROM **169A44** and **169AE4**, and no
  aligned literal address values. Both actual recovered C wrappers,
  **func_1513C4EC** and **func_1513C5B0**, run connected to the actual quad C
  at all three native profiles: **30,720 cases per profile**, including direct
  geometry cases, allocation failure/success, all factory arguments, temporary
  position payload and allocated-pointer return. The factory remains bounded.
  Existing legacy pointer/int and struct17/struct167 warnings are scoped only
  around the unchanged wrapper definitions in the native fixture.

Nonfinite/out-of-signed32 conversion results remain outside the qualified C
domain. Guest incoming-home mutations qualify the emitted ABI and are not
claimed as portable by-value C callback behavior. Native checks retain the
existing non-strict-aliasing policy. Full gameplay/hardware is not exercised.

## Owner, actual Make and complete image

The ordinary owner retains all **58 raw and padded neighbors**, pools and
register-usage metadata. Preserve its **43 inherited CFE diagnostics** as an
exact normalized multiset; no new diagnostic is accepted. The ordinary padder
audits the complete owner with its existing jtbl_800A5188_game binding. The
independent generated padder audits the complete target only, with target-only
guard rows. It is not claimed to pad every ordinary-owner function.

Unmodified actual Make in a disposable tree emits the predicted object with
ordinary -O2 -g3. Strict whole-ELF prediction permits only the target slot and
its symbol extent from 340 to 360 bytes: **226 changed bytes**, zero unexplained
bytes/exclusions and no symbol permutation. All **6,052** function addresses,
every other linked body, and **189,088 protected Game-data bytes / 720 owners**
stay fixed. Init/Debugger are covered by complete image equality.

Production Make compiles only this owner and matches the predicted object/ELF.
Makefile and conversion CSV stay byte-identical; inherited guards remain an
exact prefix. Normal make all still reaches the inherited ROM checksum
mismatch, exit 2. Fresh match-progress supplies the totals above. Shared smoke
checks run in both tools environments, with three unchanged regression receipts
explicitly reused only after exact test/helper fingerprint comparison.

Production fingerprints:

- ELF: `0c1db222f67988ffb15a4ea9a9238dc69bb5d2691e46a8e43d2f122b5e6ae07d`
- Binary: `4d1bbf0213464f690c52b67f82f81a0ade7fe215cd6c458e902a48f73dc03f91`
- Owner object: `7eacbd060b28d64ae76716a47cf8083a22f0bc3ada8c1397b76d4977449d5fe6`
- Guards: `32583c070dc35bc872dbf4bccd830a0e404777d38435dba71ac933407196da11`
- Makefile: `8e676e04318f8645e6b277ed60ed9f221d8901a5e6a02efd279d478d46a615f8`

## Continuation

Graphify receives a scoped AST refresh with fail-closed retention of unscanned
old nodes. Verify all 58 C definition positions and the one remaining assembly
function. This is not full-corpus semantic extraction. Commit tools before the
consumer pin; preserve the sibling snapshot's 2439 path states and private
inputs. No host-port or frozen Release artifact is changed.

Next target: **func_1505210C** in conker/src/game_77AD0.c, an existing semantic
85-word angle/limit routine. Re-query its graph relationships and inspect the
complete retail body, floating helpers, output-pointer aliases and caller before
probing. It is uncredited and still needs every normal qualification gate.
Its existing overflow-section body and canonical trampoline also require the
complete private-body, trampoline, symbol, program-header and ROM-cursor audit
used in Note 2185; target-slot equality alone will not qualify its adoption.
The separate func_1510D404 investigation remains non-matching with its private
traces retained.

Review: Codex owns implementation and validation. Claude calls attempted and
completed: **0**; focused source, ABI and image evidence settles this routine.
The private candidate receipt records both baseline heads, 650 frozen inputs,
loaded dependencies and each fresh/reused check. No external review is claimed.
