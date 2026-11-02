# 1983 - Random basis position recovered as guarded C

Verified 2026-11-02. Production now **4,050/5,507 (73.54%)**; Game is
**3,377/4,834 (69.86%)**, Init492/492 and Debugger181/181. Zero address drift,
1,457 different. **81 more** exact C functions are needed to reach4,131/5,507
and75%. This adds one match without changing the C inventory.

## Recovered interface and behavior

`func_1514F808` in generated_17CAF0.c replaces its zero-return placeholder with
`void func_1514F808(f32 *basis, f32 scale, f32 *output)`.
The complete60-word retail slot is VA1514F808..1514F8F8, ROM17CCB8..17CDA8;
the original48-byte frame and argument homes are retained.

Call integer RNG and save the full result. Call floating RNG in a separate
statement, then read the live radius at basis[10]. Pass the low random byte,
the sampled radius, and two local float outputs to `func_15143874`. For each
component i=0,1,2, write:

    output[i] = ((basis[i+4] * first + basis[i+7] * second) + basis[i+1]) * scale;

Each component is a separate full expression. X is stored before Y's source
loads, and Y before Z's. This matters when output overlaps the basis. Provider
mutations must remain visible. Incoming scale and output homes are reloaded
after the sampler in emitted guest code; deliberate incoming-home changes are
guest-only evidence. Standard native C does not claim arbitrary access to
inaccessible argument homes.

The selected declaration order places random atSP+20, first atSP+28 and second
atSP+2C. The source keeps a separate sample statement to prevent the premature
parameter reads found in the preceding oscillator recovery. Declaration and
expression screens are retained as private evidence; none justified a frame,
instruction-count or evaluation-order compromise.

## Seventeen checked FP-role guards

Raw C emits60 words/frame48 with the same three JAL relocations at18/20/4C.
Its SHA256 is
`5e5525a4a3c923eee0f9c5a106d417674cf5adf926201306a71ba664598d3e3e`.
Seventeen expected-word rows normalize floating register choices and commutative
operand order. There are no inserted instructions, stack changes, rewritten
addresses, functional patches or padding compensation.

The committed verifier derives symbolic binary32 value roles through the entire
instruction stream. Loads remain ordered symbolic observations; every value
crossing into a GPR/helper argument or output store must agree. It checks all
non-FP words and memory addresses are identical, that calls occur at18/20/4C,
that output stores occur at84/B0/DC, and that all callee-saved FP registers are
untouched. Comparison does not equate arbitrary caller-clobbered FP scratch
register contents. The proof is restricted to finite operands and intermediates;
guest execution explicitly checks that boundary. NaN payloads and FCSR behavior
are not claimed. Three independent GNU links verify all call bindings and the
independently assembled original slot.

## Fresh qualification

- Root corpus:840 cases, three layouts,2,520 cases /7,560 executions across
  original, normalized and raw C. All60 root words and all256 low-byte angles
  execute.116 access-prefix triples agree. Memory, GPRs, saved FP registers,
  calls, HI/LO, PC/delay state and all memory-access traces agree. Tests include
  provider changes, sequential basis/output aliases, caller-stack outputs and
  incoming-home mutation cases.
- Original math chain:388 cases /1,164 executions cover all95 instructions in
  integer RNG18, floating RNG25, sampler25 and lookup27. All256 lookup angles
  execute. Retained helpers and the65-word table match retail. Independent
 64-bit RNG recurrence and folded lookup arithmetic agree; these connected
  cases use no opaque provider. Retail floating RNG scale is37800080.
- Native32:362 cases at each O0/O2/O3, typed float arrays, complete packet/fence
  comparison and UBSan. Nine effective controls per profile reject wrong angle
  masking, unmasked angle, radius field, premature radius capture, origin,
  axis, swapped local outputs, caching all axes before stores and lost scale.
  Inputs and intermediates are finite; guest argument-home changes are excluded.
- Complete aligned-ROM call census: three JAL sites at15150008,15153D88 and
 151D0E38; no literal target pointers. Original caller windows9/9/7 words at
 1514FFEC,15153D6C and151D0E24 each cover144 cases /432 executions, totaling
 432 cases /1,296 executions. They construct scale bits and the three-argument
  o32 call, exercise canonical stack outputs at+A8/+A8/+C0, and preserve F20/F26.
  Return values are not consumed. These are bounded original windows, not
  complete-parent or gameplay acceptance claims.

A provisional fixture put an external output at the model's stack address;
the collision was detected and corrected before qualification. Output, alternate
output, auxiliary basis and caller state now have explicit disjointness checks.
The failed receipt remains private. No production fix was inferred from that
harness error.

## Owner, production and image proof

All40 raw and padded neighbors, constant pools and zero compiler diagnostics
are preserved. Five actual generated-owner Make commands reproduce the
independently qualified object. Padding uses the original17CAF0.s; existing
assembly-backed neighbors remain intact.

The independent prediction changes only the240-byte target slot and its symbol
size12->240. It equals both private and production ELF byte-for-byte:
`40b181d8e957f4afd4d70bab07dabb3874995809488ad1b40ae99a63001a12f4`.
All6,052 function addresses,6,051 other bodies, the entire named-definition
multiset, map and189,088 protected data bytes across720 owners stay fixed.
There are zero exclusions or metadata permutations.

Five focused methods and shared checks pass in each tools copy. After actual
production Make, two installed compile/image checks per copy pass; unchanged
pinned semantic results are explicitly reused. Test-label, module-description
and error-description cleanup was additionally checked for behavioral AST
identity; installed checks and shared checks pass again afterward. No semantic
suite is misrepresented as fresh after those description-only changes.

The full17,779-file predecessor seal changes only source, padded object, guard
CSV and ELF before documentation. No dependent-object exceptions. Native adoption
verifies the predecessor seal before copying reviewed files and independently
recounts the actual mounted ELF. The focused snapshot contains1,108 files;
24 canonical preparation artifacts are pinned. New helper declarations are
local to the owner; no shared-header repair or host-port change is needed.

## Next work

Continue `func_151937F4`, generated_1C0B10.c, original asm/1C0B10.s,
ROM1C0CA4..1C0D94:60 words/frame88. Retail gates a null owner and its first
word, constructs a sparse effect payload on the stack, then calls15134DAC
with a zero second argument. Two direct original calls are at150254C0 and
150997D8. Recover the interface, live owner byte, payload padding/field widths,
helper consumption and caller use before installing or crediting it. No candidate
has been screened yet. Preserve all parked experiments, including sound-start's
unresolved epilogue. The75% goal remains active; no push or pause.
