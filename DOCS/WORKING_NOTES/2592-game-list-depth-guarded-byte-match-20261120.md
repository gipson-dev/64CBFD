# Note 2592: Projected list-depth guarded byte match

Date: 2026-11-20. Consumer baseline `008fed6b4e14f566aaa26bf3a582a9033bd918a4`;
tools baseline `4234c627e309eac0326b1b242bf08c6573013fe2`.
Qualified tools commit: `2e0e069aed61fb29c695454ce02c05049bad3c0b`.

`func_1517EC1C` replaces its zero-return placeholder with complete semantic C.
Its **135-instruction body plus two alignment words** matches retail after
**nine checked normalization rows**. The **72-byte frame**, all helper
arguments and exact exposed output homes emit directly from the existing
O2/g3 profile. Source names describe the recovered fields and behavior, not
recovered debug names.

Fresh production recount: **4,578 / 5,527 (82.83%)** total, **3,905 / 4,854 (80.45%)** Game, zero address drift and 949 still different. Converted totals stay **5,527 / 6,048 (91.39%)**, 86.54% of bytes. Init 492/492 and Debugger 181/181 remain exact. **120 more** matches are needed for 85% at the current denominator.

## Interface, record fields and early returns

Owner `conker/src/game/generated_1AB530.c`; VA `0x1517EC1C..0x1517EE40`,
ROM `0x1AC0CC..0x1AC2F0`. The body ends at `0x1517EE38`; the final eight
bytes are alignment. The interface is `s32(ListRecord1AB530 *, u32 *)`.
The complete aligned ROM census finds one direct JAL at `0x1AB870`, in
`func_1517E28C`, and no literal target pointer. Computed callers are unexcluded.
The original assembly is retained unchanged.

The routine calls the recovered eight-argument `func_1509563C`, passing the
record's XYZ, output screen floats at +0xC/+0x10, local depth/divisor outputs
at **SP+0x2C/SP+0x28**, and maximum depth 4000. A result other than exactly one
returns zero without writing the caller's decoded-depth output or record+0x2C.
The projection helper may still have changed the two screen coordinates.

After a successful projection, flag mask `0x04` enables a facing calculation using
the record's current position, its direction at +0x14..+0x1C, the first camera's
position at +0x2F8..+0x300, and the threshold at record+0x20. It divides the
ordered dot product by the displacement length. A result below the threshold
returns one while leaving both depth outputs untouched. The original caller
really reads its output word on these early-return paths; its old contents are
preserved rather than initialized speculatively.

Otherwise the packed sample at +0x2A selects one of eight depth ranges and an
11-bit mantissa. The decoded value is written first. The viewport scale and
translation are read afterward, followed by the normalized projected depth,
factor 32, unsigned conversion and low-halfword store to record+0x2C.
The private record remains 0x34 bytes; named position/direction/threshold/depth
fields replace opaque spans. Camera stride 0x9A0 and view stride 0x180 remain
fixed; the view exposes its two existing Vp pages at +0x40. All seven other
raw functions, including the previous point projection, remain byte-identical.

## Defined table shifts and closed normalization

The immutable 64-byte table `D_80089630` is independently checked against retail
ROM and the actual production ELF. Its eight shift counts are 6, 5, 4, 3, 2, 1, 0, 0;
all indexed C shifts are therefore defined. The table and its bindings are
unchanged. Guest overlap cases do not write into that const table.

Recovering the success branch, explicit unsigned-halfword sample, private local
order and reused normalized-dot temporary yields 135 words / frame 72 with nine
remaining differences. Two rows swap commutative FP operands at words 47 and 51.
The other seven rows close an F10/F18 scratch-role swap over words 78..96.
Both registers are defined before their first read in that straight-line region
and dead afterward. The same result reaches F6 before conversion. No GPR,
memory instruction, branch, private home, instruction count or relocation is
changed. All 135 instruction origins are retained; none is inserted or omitted.
The derived raw bytes **and all bindings** equal independently assembled retail.
Exceptional FP operand priority is outside the commutative-operand claim.

## Fresh qualification and its limits

Six tests pass before and after installation in each tools configuration.
All **336 imported Python fingerprints** agree. The isolated second bundle has **1047 files**: 347 matching sibling files, 694 primary fallbacks, five task files and one bootstrap. The real dirty sibling preserves its HEAD, complete status and **351 dependency hashes**.

The bounded big-endian MIPS contract passes **1,024 cases per stream**, covering
134 reachable instructions; unreachable duplicate word 123 is pinned by the
complete 135-word match. Both conversion paths execute, including upper unsigned
values, invalid ranges and quiet NaNs. Checks compare public buffers, helper
arguments, return values, saved registers and complete private/incoming memory.
They include helper changes to flags, packed samples, camera and view bases,
plus overlapping record/viewport output stores. Five effective instruction
controls reject the sample shift, depth-store offset, helper limit, control
restore and facing comparison errors.

Native SDK32 passes **844 cases each at O0/O2/O3**, with strict aliasing, UBSan
and three executed source controls. Its mixed halfword/byte fixture explicitly
serializes guest big-endian values into native little-endian typed storage.
Native cases use compatible output objects and the C-defined float-to-unsigned
conversion interval. Heterogeneous guest overlap arrangements and invalid
conversion inputs remain emitted-instruction checks; they are not claimed as
portable C behavior. The model checks the saved conversion-control sequence;
generation of arbitrary arithmetic exception flags and priorities is unmodeled.

A further **112 cases per stream** execute the original four-word caller
window, including its actual A1 stack-output delay slot, recovered function,
result branch and unconditional output load. Projection remains a bounded
provider. Complete parent execution, hardware and natural gameplay are unclaimed.

## Complete image prediction and production closure

Both independent padders agree on the complete object, preserving the other
seven bodies, addresses, extents, bindings and pools. The actual five-command
Make route retains its O2/g3 profile and diagnostics. The target's symbol size
changes from 12 to 540 bytes while its 548-byte retail slot stays fixed.

The independent link also exposes a closed three-name metadata permutation:
`func_1505A630`, `func_15073C48`, `D_800B06BC` becomes
`D_800B06BC`, `func_1505A630`, `func_15073C48`. A baseline-derived prediction
rewrites exactly those contiguous symbol/string records, preserving each named
definition's address, size, type and binding. The permutation accounts for
22 bytes in `.symtab` and 36 in `.strtab`; those sections are not excluded.

Production reproduces the **complete 460-byte prediction**, covering target
code, its size field and that metadata order, with **zero exclusions**:
`165cbb8165b7a082361604cf437faaad940f0c54221b2bfcdfe0116b07397582`.
All 6,051 named function slots/addresses and the **189,088 protected data bytes**
remain fixed. The progress CSV is byte-identical because this routine was
already counted as C. Existing guard bytes remain an exact prefix; only these
nine rows append. Unchanged neighbor receipts are reused by source/object
identity rather than reported fresh.

## Graph and continuation

The native Graphify update remains fail-closed on its reduced corpus. A scoped
six-file AST merge and explicit note/original-assembly references retain all
existing IDs and prior qualification metadata. The commit-hook producers are
observed terminal before retention is sealed. This is not a full-corpus
semantic re-extraction claim.

Codex owns these changes; zero Claude calls, local commits only and no push.
The legacy `64CBFDOGL` path currently has neither Git metadata nor a src tree;
no host-source adoption was performed. Saves and the frozen Release remain
untouched. Continue the active 85% total goal from the new committed baseline.
Next audit the still-unrecovered caller `func_1517E28C` in this owner.
