# Carried actor initializer recovered as byte-exact guarded C

`func_1507266C` now uses semantic C in place of its original GLOBAL_ASM body.
Its complete **53-word / 212-byte** slot matches retail with the original
**24-byte frame** and **four guarded register-allocation words**. There are
no added or omitted instructions and no compiler-profile change. The complete
production ELF and padded owner object remain **byte-for-byte unchanged**.

Fresh prepared-cache and live Windows-checkout recounts agree on:

| Section | Exact C | Drift | Different |
| --- | ---: | ---: | ---: |
| Total | 4,022 / 5,507 (73.03%) | 0 | 1,485 |
| Game | 3,349 / 4,834 (69.28%) | 0 | 1,485 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The previous bank was 4,021/5,506. This conversion adds one exact function
and one C inventory entry because the prior implementation was real assembly,
not a zero-return C stub. The rounded total remains 73.03%. The active 75%
threshold is now **4,131/5,507**, requiring **109 more** matches. Conversion
coverage is 5,507/6,045 (91.10%) functions / 86.09% bytes; Game is 4,834/5,324
(90.80%) functions / 85.46% bytes. Root README receives aggregate rows only.

Tools are banked first at `f52f34c5843207a4d702130ded6ce129e9caa110`.

## Recovered body and ABI

Owner/source: `game_981E0`, `conker/src/game_981E0.c`.
VA **1507266C..15072740**, ROM **9FB1C..9FBF0**.
The correct entry interface is `void func_1507266C(void)`; the unused integer
forward declaration is corrected. The original assembly remains as reference.

If D_800BE616 is zero and the current actor's unsigned byte +0x222 is zero,
return immediately. Any nonzero mode byte enables slot zero. Otherwise use
that unsigned selector to obtain the carried actor from the 0x32C-byte pool.
Snapshot the signed high-half parameter and the full packed D_800D1580 command
before any record store. Separate expressions recover retail's register roles;
the compiler merges their global read while preserving the command low byte.

Write these fields, in retail order:

| Offset | Width | Value |
| --- | ---: | --- |
| +0x65 | byte | D_800C3E78 + 1, wrapping to a byte |
| +0x5C | word | signed command high half |
| +0x101 | byte | 4 |
| +0x104 | byte | 0 (`stunned`) |
| +0x125 | byte | 255 (`immune`) |
| +0x218 | word | null |
| +0xE4, +0xE6 | halfword each | zero |
| +0x232 | byte | snapshotted command low byte |
| +0xEC, +0xF0, +0xDC, +0xE0 | float each | 1.0f |

Then **reload the owner byte** and call
`func_151B5BA0(&D_800CC2D0[D_800C3E78], carried)`. This two-argument interface
is verified against the complete original helper: it checks owner type 0x53
and carried type 0x16, then optionally submits
`func_151B4FE0(carried, 255, 1)`. The nested effect routine is an explicit
provider in the bounded tests. The target does not consume a helper result.

## Four-word normalization

The semantic body emits all 53 words. Forty-nine already match; four expected
word guards close the command-snapshot and signed-parameter register change:

| Offset | Compiler word | Retail word | Relocation |
| --- | --- | --- | --- |
| +0x4C | 0x8C420000 | 0x8C430000 | LO16 D_800D1580, retained |
| +0x68 | 0x00021C03 | 0x00033403 | none |
| +0x7C | 0xACA3005C | 0xACA6005C | none |
| +0x98 | 0xA0A20232 | 0xA0A30232 | none |

The full command moves from V0 to V1 and its signed high half from V1 to A2.
The load's base/address and the complete producer/use lifetimes are accounted
for. Guards retain the relocation, store order, branches, frame and helper
interface. They add no instruction and remove no instruction. Four corrupted
expected-word objects and an incorrect relocation expectation all fail closed
through the actual padder, using a complete owner fixture.

Raw C SHA-256:
`efe8d0924f16381ef4f55eae6199493c424f6156150c5a61e24575c71ec592d6`.
The retail slot hash, raw relocation pin and complete prepared-artifact index
are in the public matching module and retained stage.

## Qualification

- **4,992 guest cases / 19,968 executions** across retail and two carry-boundary
  rebases: original, guarded owner, actual Make object, and unguarded raw C.
  All 53 words execute. The three exact programs agree on complete machine
  state, visits and access traces. Raw C agrees on public results, call
  arguments, snapshots, memory and access traces; its unmatched register
  allocation is not called full machine identity.
- All selector, mode and owner bytes, signed command boundaries and all low
  command bytes are covered. Guest-only layouts place the owner byte,
  command, current pointer or mode inside the target record. The live owner
  reload, command snapshot, wrapping owner link and callback mutations pass.
  Out-of-array selectors are guest machine tests; native C tests stay within
  the declared 26-record array.
- The **complete original 18-word notification helper** runs in **216 cases /
  864 executions** across three layouts. Forty-two case/layout combinations
  reach the nested effect path. Actual identity gates and outgoing arguments
  agree. The two out-of-body alignment words are not part of this execution
  claim.
- **47 controlled access prefixes / 141 executions** compare complete state
  and traces of the three exact programs. This qualifies guest instruction
  ordering, not portable C fault behavior.
- The full aligned ROM census finds no direct JAL and one pointer literal:
  ROM **22B03C** / VA **8008657C** = **D_800863FC[96]**. The original 19-word
  dispatch window **1506AEB0..1506AEFC** passes **24 cases / 384 executions**,
  with four return-value poisons and both script-index comparison paths.
  Full dispatcher reachability is not claimed.
- Native **O0/O2/O3 each pass 1,704 cases with UBSan**, complete pool/current
  canaries and eight effective controls: mode bypass, AND gate, unsigned high
  half, owner-link increment, stun reset, halfword reset, scale reset, and
  command-low extraction. The callback verifies owner/carried pointers and
  can mutate globals and initialized actor state after the stores.
- All **327 owner neighbors and pools**, and all **36 inherited warnings**,
  remain unchanged. The real five-command Make recipe equals the qualified
  padded object. Independent literal whole-ELF prediction has **zero changed
  bytes**, zero exclusions and zero metadata reorderings. Actual production
  Make reproduces it; all 6,056 addresses/bodies and 189,088 protected Game
  data bytes across 720 owners remain fixed.
- Six public tests pass in each tools copy before installation and again in
  installed state. Shared checks pass in both copies. The older tools mirror
  retains its independent dirty work; only the three owned new files are
  added there and no mirror commit is made.

The first guard corruption fixture supplied an isolated object to a padder
that requires the complete owner; it was corrected before the passing suites.
The first installed audit found the focused snapshot lacked progress.game.csv.
Its original bytes were taken from the untouched Windows checkout and verified
against the complete pre-install seal; all old input rows and the old snapshot
are retained. The installed audit and both suites were then rerun successfully.
Native reporting also corrected the CSV column name from size to length; the
live installed recount and complete changed-file seal audit pass. Failed
receipts are retained and are not reported as passing qualification.

## Bank and continuation

Stage: `conker/build/game-carried-actor-initialize-1507266C-match/`.
The 1,015 focused inputs, source/guard proposals, actual Make recipe/object,
strict first-link ELF, runtime/census results, public suite logs, production
proof and independent Native recount are retained. Canonical prepared evidence
is fingerprinted. The complete ELF remains:
`56dfb862d6a37ea40ec9e0bfdb47acc8a1d1faefbd4d69fdfa26afe27741e3d6`.

The independent relative-direction investigation is recorded in
[Note 1950](1950-relative-direction-cfe-stack-home-recovery-20261101.md): its
stack home now matches, but 34 words still differ and it is uncredited.

Next inspect **func_150A76F0**, owner `generated_D4450`, the smallest remaining
C placeholder in the fresh live recount: **32 retail words / 29 differences**.
Read its complete assembly, ABI and callers before choosing C source. The 75%
goal stays active. No Claude calls, pushes, host/editor or Release changes.

Continuation correction: [Note 1952](1952-aligned-zero-tail-guarded-match-20261101.md) supersedes the
func_150A76F0 queue recommendation above. That routine is handwritten custom-ABI
assembly and remains in the separate register-contract workstream.
