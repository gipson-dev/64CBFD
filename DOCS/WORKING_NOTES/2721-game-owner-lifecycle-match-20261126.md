# Actor owner lifecycle direct match - 2026-11-26

`func_151D2F90` replaces the zero-return placeholder in
`conker/src/game_1FFF60.c`. **All 104 words / 416 bytes and all 13 bindings
emit directly from C**, with the original **24-byte frame and zero guards**.
VA `0x151D2F90..0x151D3130`, ROM `0x200440..0x2005E0`; no alignment tail,
insertion, omission, guard CSV, compiler-profile or Makefile change. All
18 raw/padded owner neighbors and pools stay fixed.

Production: **4,700 / 5,528 (85.02%) total**, **4,027 / 4,855 (82.95%) Game**,
Init 492/492, Debugger 181/181, zero address drift, 828 still different.
One matching credit; no conversion-row or denominator change and no new
caller/helper credit. The active **90% goal requires 4,976 matches: 276 more**.

The entry is correctly `void func_151D2F90(struct102 *recordData)`, matching
`struct115.unk0` and the actual registered-list caller. It uses a measured
32-byte record view and the existing canonical `struct127` actor fields:
`interaction_state`, `id`, `unique_id`, `unk74`, `unk1D4`. The record retains
its actor pointer at 0x10, identity byte0x14, signed16 lifetime0x16, flags0x18
and four signed8 callback selectors0x19..0x1C. Type/field names for the local
record view describe measured roles and remain inferred names.

The routine captures the old flags mask 0x02, validates actor state, rejects actor
ID 255 or a changed identity, and releases invalid records. A present actor
matrix pointer at 0x1D4 with low mode nibble other than 15 sets flags mask 0x02;
the opposite condition clears it. Flags mask 0x01 enables live-global tick
subtraction with modulo 16 lifetime truncation. Negative lifetime invokes the
expiry callback unless its selector is -1, then releases the record. A mask 0x02
transition invokes the corresponding begin/end callback. A final update
callback with selector other than -1 and result 0 also releases the record.
This entry has no C return value.
There is no added NULL-actor guard: qualified inputs provide readable actor
storage, and the original invalid-access behavior is preserved in guest code.

The aligned ROM census finds **no direct JAL patterns and one pointer** at
ROM 0x230C00 / VA 0x8008C140. This is the first callback of actual registry
descriptor **0x3E (62), stride 52**, within the original 5,252-byte registry.
The complete original `func_151670C0` list walker uses that callback in both
banks, calls at 0x15167170 and resumes at 0x15167178, ignoring its return value.
Original ASM/ROM/frozen ELF pins agree on all 74 caller words and registry
bytes. The original 36-word `func_151D2F00` factory slot is also retail-exact;
it selects kind 0x3E, copies a 16-byte header to record+0x10 and clears flags
mask 0x02. These static facts do not grant additional helper credit or establish
execution of original allocation/backend helpers. The aligned-pattern census
does not exclude compressed, script-driven or derived references.

The first semantic body had 103 words/frame24. Recovering `wasAttached` as
unsigned8 produced 104 words with 16 differences. Keeping the current state in
another meaningful unsigned8 local, restoring identity operand order and
writing the state comparison as `wasAttached != isAttached` recovered all
original register roles and the final equality-branch operand order naturally.
The selected body also retains exact words after adopting the registry's
`struct102 *` entry and canonical `struct127` actor type. No synthetic local,
volatile field, physical-register assignment or expected-word patch is used.

Validation:

- Both complete owner padders and the actual three-command Make recipe agree
  on the entire padded object. The generated padder uses an explicitly
  **layout-only shim from 19 frozen retail boundaries** for this ordinary C
  owner; its zero words are never treated as recovered instructions. Original
  target truth comes independently from preserved target ASM and ROM.
  All 18 neighbors/pools and the complete guard CSV stay fixed. The existing
  twelve Warning 709/712 messages retain their exact normalized call/text/count
  signatures; no new diagnostics, suppression or unrelated source repair.
- Guest: 1,324 cases per five identical streams; all 104 words are preserved.
  A separate control-flow proof identifies four orphan copies at offsets 54,
  88,F4,134 (hex), each after an unconditional branch and its delay slot.
  The normal entry reaches100 words, all of which execute in the fixtures.
  No claim that those four unreachable copies executed. Full private memory,
  GPR/FPR, HI/LO, FCSR, ordered traces and 87 fault-prefix quintuples agree.
  An independent reference compares complete public memory and call order
  across owner/identity gates, both state transitions, signed timer wrap,
  status0/nonzero and callback mutations. Incoming argument-home redirection,
  actor/record and global-delta aliases are guest experiments, not portable
  native-C stack semantics. The four actual callback-table cells are pinned
  to ROM/frozen ELF. Valid selector 0 and sentinel -1 are tested; arbitrary
  out-of-table selectors are not newly qualified.
- The complete 74-word/frame 64 caller executes all 74 instructions in 96 cases
  per original/raw stream,96 connected children each. Both list banks,
  empty/single/two-node chains, two incoming stack phases and nested depths
  agree with an independent complete-parent reference. Full private literal
  states and preserved ABI registers agree. Poisoning the child's return
  register with 0,FFFFFFFF,13579BDF leaves public effects and traversal unchanged
  after complete parent execution, confirming the void interface.
- An initial guest fixture placed the actor at 0x40000, which is the reused
  oracle's stack address. The complete caller exposed the collision through
  its saved frame. Actors now use separate 0xA0000/0xB0000 banks, and an explicit
  disjointness assertion prevents recurrence. Guest/caller checks were rerun
  after that correction, before packaging or credit. No production-C change.
- Native: actual selected C in three units,4,096 cases at O0/O2/O3, strict
  aliasing, UBSan traps and LTO type checks. The partial native `struct127`
  view explicitly asserts every accessed canonical field offset; it does not
  claim to reproduce the full actor type. Typed 32-byte record arenas, padding,
  canaries, globals, call arguments and released pointer agree. Opaque
  `noipa` providers mutate reachable record/actor state to test late selector
  reloads. Native code never reads or rewrites incoming stack homes. Ten
  semantic controls finish with comparison exit42; no compile failure, trap
  or signal counts as rejection. Original callback/backend execution is not
  claimed by the replacement providers.
- Both scoped padders expose208 word and26 binding corruptions. Twenty
  independent GNU links and100 guest rebases cross jump regions and signed-low
  carry seams. Generic oversize remains visibly marked; the generated padder
  rejects it. There are no new guards to mask instruction/binding changes.
- Independent frozen old-C plus original-ASM prediction equals the complete
  private and production ELF: **327 changed bytes, zero exclusions**. All
  189,088 protected data bytes across 720 owners stay fixed. ELF SHA256:
  `2320df8ec2e1a0bb9a9fff97463cb8b80c8be3748b6b0cecf16b22fb783874b6`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 98.909 s | 5 fresh / 0 reused |
| preinstall-sibling | 108.233 s | 5 fresh / 0 reused |
| installed-primary | 180.37 s | 5 fresh / 0 reused |
| installed-sibling | 185.838 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh, with matching primary/isolated-sibling
task, source, import and data fingerprints. Shared tools-check passes. Prior
unchanged broad suites are explicitly reused, not called fresh. Frozen inputs:
4029; copies: 2965. The separately dirty real
tools sibling remains intact. Tools commit:
`4cb15265f384c6eaed520b6a21446eabb2533603`. Baseline consumer:
`d15412fa3ed5398fd857b03ad1ff3f6d7003ecb0`. Receipts:
`conker/build/game-owner-lifecycle-151d2f90-private`.

Zero Claude calls or subagents for this routine. The historical generated host
target remains an empty stub and its active implementation is unqualified.
No host transfer/build/launch or Release change, push, gameplay or hardware
acceptance. Scoped Graphify refresh audits all 19 owner definitions, retains
old IDs/qualification metadata, and observes actual hook termination; no
full-corpus extraction claim. README receives aggregate rows/date only.
Continue toward 90% from this sealed checkpoint with another qualified Game
routine, preserving all existing frozen inputs and artifacts.
