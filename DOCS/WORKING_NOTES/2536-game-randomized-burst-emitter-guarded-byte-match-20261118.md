# Randomized burst emitter guarded byte match - 2026-11-18

`func_150B82D0` replaces its zero-return C placeholder with the complete
randomized burst emitter. The selected semantic source emits **188 words /
752 bytes**. **44 checked guards**, including16 relocation-bearing rows,
normalize the frame, closed stack homes, two temporary FP roles and eight
immutable literal bindings. No instructions are inserted or omitted.

Actual production recount: **4,546 / 5,514 total exact (82.44%)**, Game
**3,873 / 4,841 (80.00%)**, Init492/492 and Debugger181/181.
There is zero address drift; **968** converted functions remain different.
Conversion inventory and byte percentages are unchanged. **141 more matches**
reach85% at the current denominator. Root README changes only two aggregate rows.

## Source, behavior and portable evaluation order

Owner `conker/src/game/generated_E4070.c`, original `conker/asm/E4070.s:1610`.
VA `0x150B82D0..0x150B85C0`, ROM `0xE5780..0xE5A70`.
Baseline consumer `7eb6dab7a07ac423462e260b53cca3b9e02e5715`, tools
`c2e63640601249a0afd9bb497b7c9d65f2cb0047`.
The complete interface is
`void func_150B82D0(MenuBurstPointE4070 *, f32 *, f32 *, f32 *, u8, s32)`.
The height, slot and context parameters are unused by retail, while the real
parent still passes all six. The existing local Vec3 declaration moves above
the parent; no shared header, factory or parent body changes.

1. Unsigned integer RNG chooses35..60 emissions with `%26+35`.
2. Each iteration chooses heading with `&255`, and signed pitch with `%61-63`.
   The direction provider writes a radius-scaled position. Its Y value is
   multiplied by the current ratio, then the current center coordinates are added.
3. Three float samples choose rotation components scaled by360. A fourth
   chooses velocity magnitude `(sample*1221+1806)*.01`, passed with the same
   heading/pitch to the direction provider.
4. Two further samples choose acceleration X/Z as `(sample*3140-1570)*.01`;
   Y is zero. Four vector buffers stay live across provider calls and loop trips.
5. Explicitly capture the next two float samples in source order. Submit all
   thirteen factory arguments: position, rotation, `(sample0*104+78)*.001`,
   velocity, acceleration, `(sample1*633-1064)*.001`, the exact damping literal,
   1, unsigned integer RNG `%51+75`, 0, 0, 255 and1. Decrement and repeat.

Each emission consumes three integer and eight float RNG calls, two direction
calls and one factory call, after the opening integer RNG. Input pointers may
alias and providers may mutate public inputs and all four exposed vectors.
The native test compares initialized data only. Direction's output is a
write-only three-word vector, consistent with its retained semantic source.
Factory allocation failure and success are modeled. The C interface is void;
guest tests separately check the emitted final V0. This is not hardware or
live gameplay acceptance, and it does not newly qualify the provider bodies.

The earlier inline-argument draft had188 words and a0xE0 frame, but failed
native provider order at O0/O2/O3 because C does not prescribe the order of
independent function arguments. It is rejected and retained privately.
The installed form explicitly captures both samples and passes all three
native optimization levels. Its raw SHA-256 is
`f48099632d71a9a3d4dbe7a3bb0d2d127fc486bb2792ad3cfc4ac6b0460b8b27`.

## Derived normalization and complete loop relation

The source frame is0xE8/232 bytes; normalization restores retail's0xE0/224.
Twenty-two SP-based words adjust seventeen vector accesses/addresses by-12
and five incoming-argument homes by-8. The closed52-byte mapping rotates
48 vector bytes plus four padding bytes. Eight additional source frame bytes
are proved never accessed or passed. They are not observable bytes excluded
to conceal a changed access. A four-word temporary F20/F22 role exchange
preserves FP opcodes, operands, results and operation order. All saved roles
and their custody remain checked.

The compiler introduces32 bytes of literals after the retained40-byte jump
table. All ten table relocation identities and bytes remain fixed after
normalizing compact PCs. Every new literal bit equals the frozen retail
word at `D_8009FD68..D_8009FD84`; old/new alignment is zero and compact data
is unchanged. Both actual padders discard the compiler pool and retain the
original production pools. The sixteen literal HI/LO guards derive their
named relocation identities from the checked source pairs. Replacement
instructions derive from source words; original GNU assembly is the comparison.

The instruction-driven proof covers two paths each through the prefix,
first iteration and arbitrary steady iteration, all248 canonical private /
incoming bytes, ordered FP/FCSR operations, public read epochs, providers,
all four mutable escaped vectors, saved registers and return. All non-saved
private state is arbitrary at the steady cut. The positive signed count
decrements by one; any nonzero successor stays positive. The only dead values
excluded at loop cuts are the two samples, which are redefined before reuse;
all saved FPR values are restored on return. All187 reachable words are
covered, and the unreachable fixed-divisor BREAK at offset0xE4 is preserved.
Sixteen effective negatives exercise homes, divisors, mask, duration,
decrement, return custody, acceleration and each of eight literal bits.
Ordinary mapped/aligned memory, immutable literals and private stack
separation are assumed. Raw fault-register identity, interrupts and hardware
FP exception behavior remain unclaimed.

## Caller and fresh production gates

The original484-word `func_150B7B40` parent is independently GNU-assembled,
bound and compared to ROM. Its real call at0x150B7D78 connects each helper
stream and resumes at0x150B7D80. **The production parent remains its unchanged
12-byte zero-return stub and is neither restored nor credited here.**
Each stream passes129 complete original-parent cases, with128 helper calls,
all187 reachable helper words and483 reachable parent words. The preserved
unreachable duplicate LUI at0x150B7D60 is the parent's only uncovered word.
Final public memory, parent-owned frame bytes, retained outputs, input
pointees, provider calls and GPR/FPR state agree. Dead child-private bytes
are not compared after return. Other parent providers remain modeled.

Both final tools configurations pass six fresh tests without errors/skips:
**219.576s primary / 226.026s private sibling overlay**.
Each fingerprints **333 imported tool files**.

- Both full-owner padders match all188 retail words and named relocations.
  All20 compact and padded neighbors are unchanged. Twelve independent GNU
  rebases,219 raw/binding corruption controls and328 actual CSV corruption
  controls pass or reject as intended.
- Original/raw/normalized guest streams each pass128 cases and6,720 factory
  submissions, including unsigned RNG boundaries, aliases, mutable providers
  and allocation failure. Native32 O0/O2/O3 each passes the same128 cases
  with strict aliasing, UBSan, no-fast-math and contraction disabled. Eight
  source negatives fail with controlled exit3.
- Both configurations produce the same predicted ELF through actual
  Make-derived commands, then reject four whole-image corruptions.
- Production Make compiles only this owner, links the ELF and regenerates
  progress. No prebuilt object is copied. The actual ELF equals the independent
  prediction. The existing duplicate generated_12D630 recipe warning remains.
- Strict audit accounts for **772 changed bytes**,
  with zero exclusions. Five adjacent symbol/string pairs change order;
  each keeps the same named definition, address, extent and flags, and the
  auditor reconstructs every metadata byte rather than excluding the area.
  All6,050
  other linked bodies, all addresses and189,088 protected data bytes are fixed.
  Only one of698 frozen objects changes. Conversion rows and prior guards
  remain fixed; exactly source, guard CSV, owner object and ELF change among
  **1688 frozen inputs**.
- Fresh installed-source compilation reproduces all21 compact functions.
  Production/fresh-raw/fresh-normalized guest and complete original-parent
  checks pass. Unchanged proof/native/padder/rebase receipts are reused only
  by exact fixture hashes. Required tools checks and actual-ELF recount pass.

Production ELF SHA-256:
`46cfd670adb3a01257e59f77734a12a6ce785c3b2807ce7ceb7b154044ad2ed2`.
The sibling tools checkout's2,434 dirty paths, HEAD and343 dependencies are
preserved. Its private overlay uses339 sibling files,390 pinned primary
fallbacks and eight task files. The host sibling contains only `.codex` and
`recomp_scene`; no source/build checkout is available for applying this change.
Host applicability remains unverified; Release and saves are untouched.
No Claude call or push is needed.

## Continuation

Graphify's native update and scoped AST merge have separate receipts, retain
old node IDs and explicitly link the qualification module to the installed
function. This is not full-corpus extraction. Commit tools before the consumer.
Next reconstruct the complete484-word **`func_150B7B40`** using its retained
caller fixture and the two now-qualified particle helpers. Notes2531/2532
retain uninstalled drafts without credit. This adoption adds one exact match;
the85% goal stays active with141 further matches required.
