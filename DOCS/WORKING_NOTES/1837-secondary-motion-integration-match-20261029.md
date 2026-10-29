# 1837: Secondary motion integration match

Date: 2026-10-29. Target `func_150CB008`, owner `generated_F5800`.
VA `0x150CB008..0x150CB0DC`, ROM `0xF84B8..0xF858C`: 53 instructions.
Its fixed slot extends one alignment word to VA `0x150CB0E0`, ROM `0xF8590`.

The zero-return placeholder is replaced by a complete `s32 (u8 *record)`
integrator. It advances position at offsets 0x38/0x3C/0x40 using the global
frame step `D_800BE9A4`. Vertical motion includes the original ordered
acceleration-times-step-times-step-times-0.5 term, followed by a vertical
velocity update at 0x48. Angular coordinates 0x20/0x24/0x28 advance using rates
0x50/0x54/0x58. The function returns 1. Repeated time-global reads and the
single-precision operand/grouping order remain significant when data alias
the global or carry quiet-NaN payloads.

All 53 original instructions are byte-for-byte identical to the previously
qualified `func_150CA07C` in this same owner. Its recovered complete C body and
ordered arithmetic oracle are reused with this target's own frozen snapshot,
entry/slot, bindings, registration, guards and production audit. This is a
separate emitted function; the earlier match and all other owner bodies stay
fixed. Thirty-three expected-word and binding guards normalize a closed
compiler register allocation and independent scheduling. No instructions are
inserted or omitted, no arithmetic operand order is changed, and there is no
stack frame. Matching is guarded byte-exact C, not direct compiler output.

The whole aligned ROM scan finds no JAL encodings to this entry and exactly
one full pointer, at ROM 0x22E380 / VA 0x800898C0. It is index 4 of table
`D_800898B0`. The original 13-word dispatch window in `func_151321D0`,
VA 0x15132244 / ROM 0x15F6F4, passes 96 cases with the actual table index,
zero-index skip, argument, result and preserved flag. Earlier parent gates
remain preconditions; the parent C placeholder receives no conversion credit.
Computed or encoded references are not excluded by the aligned scan.

Validation passed independently in both tools copies:

- Eight fresh checks per copy plus each shared tools check. Installed validation
  reruns two methods per copy; the other six are reused only under complete
  input/module/qualified-artifact identity.
- 1,296 guest cases / 3,888 executions cover original, normalized and raw C;
  all 53 original words execute. Full normalized GPR/FPR/memory/events/access
  traces equal retail. Global/record aliases and ordered quiet-NaN payloads
  are tested; hardware FCSR behavior is not claimed.
- Native32 O0/O2/O3 each pass 648 cases with UBSan and reject six effective
  controls. Native NaN payload identity is not claimed.
- 81 dispatched access-prefix pairs preserve literal normalized state. Three
  GNU relocation layouts pass 108 cases. All 212 raw-byte/two-binding and
  33 guard-preimage corruption controls reject, as does the arithmetic-order
  source control.
- Complete compact and padded owners preserve all 18 neighbors and pools.
  Three actual Make commands reproduce the qualified object with zero C
  diagnostics. The inherited duplicate-recipe Make warning remains.
- Strict independent full-image prediction equals production: 158 changed
  bytes = 157 target code + 1 target extent. No metadata rearrangement or
  comparison exclusion. All 6,055 other disassembled bodies and all function
  addresses remain fixed; 189,088 protected Game bytes / 720 owners remain exact.

Fresh adopted-ELF recount: **3,914/5,506 (71.09%)** total and
**3,241/4,833 (67.06%)** Game. Init remains 492/492, Debugger 181/181, zero
drift. The conversion inventory CSV is unchanged. **216** additional matches
reach the 4,130 threshold. Tools commit first: `18421e1923dcd3546452d72673b69f640d3ad183`.

The scoped native Graphify refresh retains or uniquely relocates all 49,450
previous nodes and preserves all 102,567 previous directed relationships,
including context. The s32 return type stays valid; no old type edge retires.
Outside-scope manifests and communities remain historical. This is not a
full-corpus extraction or a gameplay/hardware acceptance claim.

Earlier private screens remain uncredited: `func_150A613C` has a custom
register interface requiring a parent closure; `func_150495B0` still needs a
supported frame/local reconstruction. An enlarged scratch array with unused
elements is not adopted. Their compiler/profile evidence remains in the
preceding record-key build directory. Other parked candidates remain private.

Artifacts: `conker/build/game-secondary-kinematic-integration-match/`.
Next screened target: `func_150832AC`; screening is not qualification.
The older tools mirror preserves all 1,949 inherited dirty paths plus these
three new tools. No push, host-port, Release, save/editor or memory changes.
Zero Claude calls; existing identical retail/C evidence resolves this recovery.
