# Conditional byte blend and pointer return - 2026-10-31

`func_151CB510` replaces its false zero-return placeholder with a semantic
conditional float blend, unsigned byte conversion and explicit blend-state
pointer return. The full 59-word slot matches retail after seven checked
register-allocation normalizations. This is a guarded C match.

The actual adopted ELF recount is **3,979 / 5,506 (72.27%)** exact C functions;
Game **3,306 / 4,833 (68.40%)**, Init 492/492, debugger 181/181, zero drift.
There are 1,527 different C functions. The 75% threshold remains 4,130,
leaving **151** more exact matches. The goal remains active.

## Recovered contract

Owner `conker/src/game/generated_1F4650.c`; original `conker/asm/1F4650.s`.
VA `0x151CB510..0x151CB5FC`; provided retail-code span `0x1F89C0..0x1F8AAC`.
Signature `ConditionalBlendState *func_151CB510(ConditionalByteBlend *record)`.
It is a leaf with no stack frame or saved registers. Shared headers and the
existing O2/g3 profile are unchanged.

Record+0x70 contains owner*, current float at +0x74 and target at +0x78.
The owner supplies a flag-halfword pointer at +0x36C and peer pointer at +0x3D4;
the peer gate is an unsigned halfword at +0x19E. The target is enabled only when
flags include 0x2000 and peer gate is zero. Otherwise the target is zero.
Current advances by `(target-current)*D_800AAEA8`, whose retail value is
0x3ECCCCCD (0.4f). The low byte of its unsigned conversion is stored at +0x2E.
No visual alpha meaning or extra clamping is assumed.

The original unsigned conversion saves FCSR after the floating arithmetic,
requests truncation, checks conversion errors, uses the 2^31 fallback when
needed, and restores the saved control state. Both unreachable duplicate words
at offsets 0x34 and 0xC8 remain intact. There are 57 reachable words in the
complete 59-word compiler/retail slot.

## Caller-driven return recovery

An earlier private void draft emitted all 59 words directly but was rejected
at ABI qualification. The original `func_15154C90` dispatcher checks V0 after
the indirect call. Retail leaves the blend address, record+0x70, in V0.
The final source explicitly returns that address. Treating it as void, forcing
zero or returning an unrelated non-null address would lose part of the contract.

The complete provided code-input census finds no aligned direct JAL references
and one literal root pointer: ROM 0x22F798 / VA 0x8008ACD8. It is method slot 4
of `D_8008ACC8`, not the earlier actor callback table. The original 60-word
dispatcher is exercised in 864 cases / 3,456 executions, including method masking,
lifetime/expiry gates and byte limiting. Positive cases visit 59 caller words;
four effective forced-zero return controls visit the final zero-result path
and trigger cleanup. Cleanup itself is an explicit bounded model, not a claim
that the complete cleanup routine or gameplay has been executed.

## Checked compiler normalization

The explicit pointer-return C body emits 59 words. Seven expected-word guards
close one cursor allocation: two ADDIU destinations and four memory bases move
from V1 to V0, then the redundant final `move v0,v1` becomes the retail NOP.
Offsets: 0x1C, 0x30, 0x38, 0x3C, 0x5C, 0x68 and 0xE0.
No FCSR instruction, memory-access order, relocation, branch or scalar operation
changes. No words are inserted or omitted. Two D_800AAEA8 HI/LO bindings remain.
All inherited guard rows are preserved byte-for-byte as the manifest prefix.
There are 241 payload/scope/binding corruption controls, 28 guard-field controls
and seven actual padder preimage rejections.

All 45 complete raw/padded owner neighbors and normalized pools remain unchanged.
The existing GLOBAL_ASM owner requires five actual Make commands, including
asm_processor pre/post passes. The qualified Make object is identical. Compiler
and command diagnostics are empty. The two existing duplicate-recipe warnings in
Make's plan stderr are retained and are not counted as commands or new defects.

Strict independent full-image prediction has zero exclusions:
168 changed bytes = 157 root-code bytes + one extent byte + ten metadata bytes.
Metadata is one closed `D_800AAEA8` / `D_800A1178` symbol/string permutation,
with named values/definitions checked independently. All 6,055 other linked
bodies, every function address and 189,088 protected Game data bytes / 720 owners
remain unchanged.

- Compiler target SHA-256: `f4f03d6614164afc94283dbb8f94264e86e1c6e49d19d3f839fa8fb2de52a3d5`.
- Normalized unlinked target: `5ef3fc0e390bc291ab4ea1d1f788aebbadda3d944a3c81aeafcf9784be2fc8f9`.
- Qualified ELF: `6c0b47cec5381a5cb0506af0572c4e9380ac1322a94b6ab37c2d89a200daca75`.

## Behavioral evidence and limits

Guest validation covers 5,943 ordinary cases / 23,772 executions through original,
raw compiler, padded and actual-Make images. Three GNU layouts include HI/LO
carry. It covers short-circuit reads with unmapped disabled fields, 27 aliases,
62 access-prefix cuts (four in branch delays), valid/negative/unsigned-fallback/
invalid conversions and both preserved unreachable words. Normalized images
agree literally; raw execution uses an explicit cursor-register correspondence
at intermediate cuts and differs only in caller-clobbered V1 on final return.
The returned V0 address, memory accesses, FP values and control operations agree.

FP-control tests use the existing bounded nontrapping model. The arithmetic
reference rounds f32 operations to nearest; nondefault rounding-mode fixtures
use exact arithmetic. Temporary conversion state and restoration are checked.
This does not establish arbitrary hardware arithmetic flags, traps or complete
FCSR emulation. Invalid/nonfinite conversions are guest-only.

Native SDK32 C passes 262,158 cases each at O0/O2/O3, with trapping UBSan and
float-cast-overflow checks. All 65,536 flag values and peer gate values are
covered. Native conversion inputs stay in the defined finite unsigned domain;
disabled owners may have a null peer. Exact returned pointers and all record
bytes are checked. Fifteen compiled semantic controls fail by the designated
mismatch exit, not by compilation failure or trap.

## Adoption

Both tools copies pass all eight fresh canonical tests and their shared checks.
Installed source/image gates run freshly in both copies, with six unchanged
semantic checks reused only by complete module/compiler/input/artifact identity.
Tools are committed first at `8abc13890f93d50c79ea53f50bfd2aaa3c3dd998`; consumer source, seven guards, tools pin
and seven docs follow. Root README changes only two aggregate rows. The scoped
graph preserves all old valid relationships and retires the obsolete s32
placeholder return edge after validating the explicit pointer-return source.

Evidence: `conker/build/game-conditional-byte-blend-151CB510-match/`, including
`preparation.json`, `private-semantics-v18.json`, both qualification/installed
receipts, production/adoption proofs, actual recount, full function views,
`graph-final-proof.json` and `BANKED_STATUS.json`.
Next screen: `func_151162D4`. Private candidates remain uncredited until complete gates pass.
