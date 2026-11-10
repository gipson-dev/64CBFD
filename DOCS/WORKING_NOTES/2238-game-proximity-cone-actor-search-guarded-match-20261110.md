# Game proximity-cone actor search guarded match - 2026-11-10

`func_150768DC` matches its complete **160-word / 640-byte** retail slot,
VA **150768DC..15076B5C**, ROM **A3D8C..A400C**. Semantic C emits all 160
words with the natural **0x58 frame**; **30 checked guard rows** normalize
register and commutative operand roles. No insertion, omission, compiler
profile, shared declaration or Makefile change.

Production recount: **4,308 / 5,513 (78.14%)** total; Game **3,635 / 4,840
(75.10%)**; Init 492/492 and Debugger 181/181. Zero address drift, 1,205 still
different. The active 80% goal needs **103** more matches to 4,411/5,513.
Conversion CSV/counts stay fixed. README changes only aggregate rows.

## Source recovery and ABI

Owner `conker/src/game_A28B0.c`; object `conker/build/src/game_A28B0.c.o`.
The original assembly in `asm/nonmatchings/game_A28B0/` is retained.
The public interface remains `void(void)`. Locals now identify the candidate,
selected actor, distance, closest bound, own index, cone width, definition,
angle byte and script. No shared field or function names are changed.

The predecessor emitted 161 words and was routed through a private overflow
copy. Recovering the cone-width local as **s32** removes the redundant
post-angle copy from its byte carrier into a promoted comparison register.
Its source field remains the unsigned byte at definition+0x17. Keeping the
angle-byte local u8 preserves retail's copy/scheduling shape; a separate
signed-angle probe did not align. All probes remain in the ignored build dir.

Raw SHA256:
`358290d8b054921ec935c19e86d35b91a3a7c549cc693ab14dec431f93c51c45`.
All 640 bytes, 19 binding sites and owner/function are pinned. The complete
opcode, immediate, branch and relocation structure already agrees with retail.
The 30 guarded operand words close saved-register roles and the commutative
ID-load/compare roles. The two ID reads normalize to retail's order; the
ordinary nonvolatile source comparison allows either read order. No private
home remap or opcode substitution is needed. Both independent target padders
and the complete owner agree with the independently assembled 160 retail words.

## Search and publication contract

Capture D_800D1890*8 as a float distance bound, clear the current actor's
selection byte at 0xA8, then derive its index relative to D_800CC2D0 with the
812-byte actor stride. The canonical actor array contains26 entries, but the
retail search intentionally scans **only indices 0..24**. Preserve that limit.

Reject a candidate when its state is zero, health byte is zero, flag 0x20 is
clear, or its index equals the captured own index. When D_800D1891 is zero,
also reject matching actor IDs. Reject only when absolute vertical distance
is greater than 50.0f; unordered/NaN height comparisons proceed to the helper.
Call1505A72C(current,candidate). Its float result must be **strictly less**
than the current closest bound, so ties retain the earlier selection.

Reload current actor after the distance helper. Capture its definition's
unsigned cone-width byte through D_800D1C90[id]. Call1505A630 with
candidateX-currentX, currentZ-candidateZ and integer argument 0. The returned
u16 supplies the high angle byte. Retain the cone width across this call,
then reload current actor and evaluate:

`((baseHeading>>8) + signedOffset - angleByte + coneWidth/2) & 0xFF`

Accept when that result is strictly below coneWidth. Publish candidate index
plus 0x80 to the live actor's selection byte and update the closest distance.
The signed offset is actor+0x2CA; base heading is u16 at 0x76. Callback tests
change actor, ID, cone byte, positions and script parameters, and clobber all
caller-saved GPR/FPR values, HI/LO and the16-byte outgoing home area.

After the loop, a nonzero selection invokes1507BB28(0,D_800D1893). Reload
current actor for the returned script pointer publication and again before
decrementing it by **one struct216 packet, exactly five bytes**. Read the live
D_800D1892 afterward. If nonzero, reload selection&0x7F, clear that actor's
script pointer, set its script byte at 0x232 and own-index byte at 0x222.
Current-actor aliases within the canonical array and callback mutations pass.
Complete helper algorithms and hardware/visual gameplay are not qualified.

## Complete overflow and ELF prediction

The new body fits its canonical640-byte slot and replaces the old trampoline.
The private **644-byte** `__retail_overflow_func_150768DC` is removed. The
game overflow section shrinks **960 -> 316 bytes**. Two later private bodies
move down 644 bytes, with every instruction unchanged. A full scan finds no
remaining jump/call or full-word pointer requiring retargeting to those two
private copies. Every canonical function address remains fixed, and the only
changed canonical body is the target.

The literal full-ELF predictor also removes the private function and owner-file
symbols, compacts their names, reinserts the public name at its deterministic
position, rebuilds symbol/string/section tables and header offsets, adjusts
the overflow segment sizes and reduces the ROM cursor by 640 bytes. It derives
all result bytes from the frozen predecessor and retail target; it copies no
unknown result metadata and excludes no ranges. The final ELF shrinks
**3,255,096 ->3,254,384 bytes**, a **712-byte** reduction. The raw same-offset
diff count 496,790 reflects metadata movement, not that much changed game code.
Function census 6051 -> 6050 removes only the private overflow definition.

All **210 non-target owner functions**, raw/padded pools and register usage
stay fixed. The existing heading-selector table binding and its guard history
remain unchanged. The 13 inherited diagnostics stay 13. Actual five-command
asm-processor/IDO O2-g3/postprocess/generic-padder/assembler output equals the
independent owner. All **189,088 protected bytes / 720 owners** remain exact,
SHA256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Existing duplicate 12D630 Make warnings and expected `make all` checksum exit 2
remain. The production ELF and object exactly equal their qualified predictions.

## Focused evidence and limits

- Guest: 105 cases per raw/normalized/retail body = **315 executions**, plus 12
  rebases. Each visits 158 of 160 words; the negative-width division correction
  is unreachable because the source field is u8. All 25 slots, excluded slot 25,
  own index 25, state/health/flag/ID gates, exact 50 height boundary, NaN/Inf,
  signed angle offsets, aperture edges, distance ties and live effects pass.
  All public bytes, helper snapshots, saved GPR/FPRs and caller homes agree.
- Native SDK32: 105 cases at **O0/O2/O3**, UBSan and **18 effective controls**
  per profile. Canonical actor/definition offsets, 26 actors, 187 definitions,
  sizeof(struct216)==5, retained modeled bytes and helper snapshots pass.
  Endianness and pointer identities are normalized explicitly. A preliminary
  bad-selection control selected an out-of-range actor and trapped; it was
  replaced with an in-range wrong target. That trap is not credited as a
  semantic witness. The candidate itself did not cause that trap.
- Compiler controls: 19 effective IDO mutations, including a stale current
  actor and a cone width reloaded after the angle callback. All 160 word and 19
  binding corruptions are rejected; all 30 stale expected guards are rejected.
  Seven full-image corruptions cover code, overflow, protected data, metadata
  and headers. Four independent GNU links / 12 executions exercise HI/LO carries.
  Compiler, interpreter and fixture failures never count as control witnesses.
- Caller:ROM has no direct JAL/J and one entry pointer at 22B31C, protected
  VA 8008685C =D_80086730[4B]. The complete original 1507BC14 dispatcher remains
  byte-exact C: 100 body words plus 3 alignment words. **126 executions /114
  target invocations** cover script decode, FF skips, timer/flags, null lookup,
  five-byte advancement, target script redirection and real JALR ABI. It visits
  99 body words; word 67 is a dead duplicate byte load. The same 1507BB28 provider
  is distinguished when called by the dispatcher versus the target. It and
  next handler 1507735C remain bounded providers.

Six fresh focused tests pass before and after installation in each tools
environment. Shared smokes are fresh; three unchanged regressions per copy
are explicitly fingerprinted reuses. 728 inputs include the earlier predictor's
source provenance. Sibling validation uses a read-only overlay and preserves
the native Git inventory of 2,434 dirty paths. Tools commit precedes consumer
source/guards/docs/pin. No push or host-port change.

Graphify receives a scoped AST refresh for the owner and six new modules.
The 210 active C definitions, retained ASM and nodes outside changed files are
audited. New-module coverage is recorded as observed, not claimed as a full
corpus extraction. Evidence lives in
`conker/build/game-proximity-cone-150768DC-match/`.

Next: `func_150585F0`, 170 retail words / 73 screened differences, in
`conker/src/game_83300.c`. Recheck its complete routine, types and callers.
The unresolved texture-command candidates remain private/uncredited.
Keep the 80% goal active.
