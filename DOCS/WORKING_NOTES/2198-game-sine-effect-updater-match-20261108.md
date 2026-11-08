# Sine Effect Updater Match - 2026-11-08

`func_150F7E20` now has its semantic **78-word /312-byte C body**, original
**0x28 frame**, and **three expected-word guards**. All normalized words match
retail. The isolated body, complete owner, both padders and actual Make agree.
The literal full-image prediction changes **226 bytes**, with zero exclusions
and no metadata permutations.

Production: Total **4,267 /5,513 (77.40%)**, Game **3,594 /4,840 (74.26%)**,
Init **492 /492**, Debugger **181 /181**, zero address drift. **1,246** converted
functions remain different; **144** more exact functions reach4,411 /5,513 and
the active80% goal. Conversion denominators and progress CSV are unchanged.

## Interface, bindings and recovered behavior

Owner `conker/src/game/generated_124920.c`, original `asm/124920.s`.
VA **150F7E20..150F7F58**, ROM **1252D0..125408**. Interface:

```c
s32 func_150F7E20(u8 *effect);
```

The effect contains a state block at+0x110. Its float fields are remaining
time+0x18, phase+0x1C, rate+0x20, center+0x24 and amplitude+0x28. The local
SineEffectState124920 type names these measured roles without inventing a
whole engine record layout or renaming the exported retail function.

1. Multiply effect float+0x128 by D_800A1BD8, convert to unsigned32 and store
   the low byte at+0x5C. Scale bits **40CF684C** mean6.481481552124023, not255.
   Its original owner is `asm/data/246680.rodata.s`, ROM246698. Retain the
   complete unsigned-conversion fallback, CFC1/CTC1 protocol and unreachable
   duplicate MFC1. The input conversion restores its saved control value
   before sinf; do not replace the unsigned cast with a signed cast.
2. Call sinf with effect+0x12C. The incoming effect home is saved in the JAL
   delay and reloaded afterwards. Read amplitude and center after that call;
   write sine*amplitude+center to effect+0x30, then+0x2C.
3. Read phase, rate and global delta D_800BE9A4. Submit phase+rate*delta to
   func_15144B68, save/reload the block pointer across it, then store the
   returned phase. Reload delta after the call, decrement remaining time,
   store/reload it, and return0 only when it is less than0.0f. Zero, negative
   zero and unordered NaN comparison retain the original return behavior.

The sole aligned function pointer is **D_80089CB8[36]**, VA80089D48 /
ROM22E808, owned by `asm/data/22E730.rodata.s`. There are no direct J/JAL or
interior entry pointers. The original15-word registered-call window in
**func_1513CFE4**, VA1513D038..1513D074 /ROM16A4E8..16A524, passes the record,
saves/restores it and the signed removal byte, sets removal to1 on a zero
return, and freshly reloads byte+0x71. The target is therefore s32(u8*), not
a return-ignored callback. The complete parent is outside this qualification.

## Three closed normalization words

Raw C already has the78-word size,0x28 frame, RA+0x14, incoming effect+0x28,
call sites, public accesses and lifetimes. Declaration-order and arithmetic
shape screens leave three independent allocation differences:

| Word | Raw | Normalized | Meaning |
| --- | --- | --- | --- |
|48|46008482|46100482|Swap the two MUL.S inputs; destination F18 stays fixed.|
|55|AFA20018|AFA2001C|Save the block pointer at private SP+0x1C instead of+0x18.|
|59|8FA20018|8FA2001C|Reload that same pointer from the paired private home.|

The qualifier derives these changes from register fields and the closed
private-home pair. Neither home overlaps outgoing argument words, saved RA
or the incoming effect home. The address never escapes; the only intervening
callee, func_15144B68, is a frozen stack-free24-word leaf. There are no frame
size changes, insertion/omission guards, public address rewrites, general
register remapping or compiler-profile changes. Guard history is preserved
byte for byte before appending the three checked rows. Raw SHA256:
`97b55c588bc0db7097dc4e5a4a4eb034cb377099ffb9512351292d2ec54ab25c`.

That original wrap helper is already byte-exact. Its period D_800A56A4 has
bits **40C90FDB**, from private `assets/249F40.bin` at ROM24A164. Its repeated
single-precision subtraction/addition keeps an exact positive-period endpoint
instead of mapping it to zero. Connected tests bound finite inputs to a few
periods; infinite inputs would not terminate and are not executed here.

## Qualification and model limits

Six focused checks pass sequentially before and after installation against
mounted and sibling tools, with source and dependency fingerprints.

- **1,380 guest cases**, **16 alias cases** and
  **110 interrupted-access cuts**. All77 reachable words
  execute; unreachable duplicate offset0x88 is retained. Independent complete
  memory, arguments and returns agree. Original and normalized literal states
  agree, including access prefixes and bounded conversion control.
- **84 connected original-wrap cases** reach all24 helper
  words. **36 original registered-caller cases** check
  the return consumer, record reload, signed removal flag and next byte.
- **364 native32 cases per O0/O2/O3 profile**, trapping UBSan,
  typed object/state offsets, complete object canaries, independently computed
  expected values/arguments and **13 effective semantic controls**.
  Float-to-unsigned inputs are finite products in[0,2**32); exceptional and
  negative conversion fallback probes stay guest-only.
- Three independent GNU links and12 rebased executions qualify all eight
  binding sites. All78 word, eight binding,72 register-metadata and four
  whole-image corruption controls reject changes.

Helper providers deliberately mutate state, global delta, incoming homes
and caller-saved registers to verify snapshots and late reloads. Synthetic
private-home retargeting uses each program's actual home. Raw finite public
behavior is compared separately from normalized/original literal equivalence;
raw NaN multiplication payloads and identical private fault addresses are not
claimed. Aliases remain guest probes rather than portable C overlap promises.

The bounded conversion model implements truncation, invalid fallback and
control save/restore; it does not emulate arithmetic exception flags, traps,
condition-bit encoding or every hardware FCSR behavior. Native checks keep
final phase/timer arithmetic finite. Actual sinf accuracy, complete parent
execution, hardware and gameplay are not newly qualified by these checks.

## Owner, literal image, production and preservation

Actual Make retains O2/g3/MIPS2/O32 and all five commands: assembly prepass,
IDO compile, assembly postpass, production padder and GNU as. Preserve the
existing GLOBAL_ASM func_150F7470 and all **17 owner functions /16 neighbors**.
Both padders agree, pools and exact register-mask union are preserved, and
compiler diagnostics are0. No exported interior labels change.

Independent full-ELF prediction replaces only the312-byte body and its
12-to312-byte extent: **226 changed bytes, zero exclusions**. All **6,052**
disassembled entries keep their addresses; every other body, extent and
metadata byte stays fixed. Protected data is exact across **720 owners /
189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals the complete prediction.
Makefile, data bindings and progress CSV stay unchanged. The pre-existing
full-ROM checksum mismatch (make all exit2) and duplicate generated_12D630
recipe warning remain separate from the successful target compile/link and
recount. Fresh shared smoke checks pass in both tools copies; three unchanged
helper regressions per copy are reused by exact fingerprints. All **2,434**
inherited sibling dirty paths remain preserved. **110 frozen inputs** pin the
owner, caller, helper, data owners, headers, layout, ROM and IDO compiler.
Baseline consumer3b4ea03214dafeb2bf3507ffcd83ed6aea332212, tools
11cc9eb4ede7bb0264cc25ee914223a079ffacab. Claude calls:0.

ELF SHA256: `f4208601bcd5314ffb3042742ab771282b39636d13ac8f0834fbd5d36b43d0f1`.
Binary SHA256: `8dd0e4e2ac9db3cd11f22e23e70793d550c271a6c8d0658b992280fcc19d4c2b`.
Owner SHA256: `c0a46d99f9f59bd861514b0baca9814773cfdef8ebbad5071c8c41ac7026722d`.
Guards SHA256: `e2720ab6500e6d9cacd038f8e2f414ce133944971b00f7236ff46503e4bffe91`.

## Resume boundary

Next: **func_15131514**, an uncredited78-word mode-selected four-halfword
output routine in `conker/src/game/generated_15D730.c`, original15D730.s.
VA15131514..1513164C /ROM15E9C4..15EAFC, frame8. Four output pointers occupy
A0..A3; the record is the fifth argument at incomingSP+0x10. Audit all callers,
the mode byte+0x71, nine-entry jump table jtbl_800A3820 and exported interior
labels before drafting. Preserve store/reload ordering for output aliases,
unsigned source bytes, and default `(byte27*byte2B)>>8` alpha. Do not credit
the placeholder or a private candidate until all qualification gates pass.

Receipts: `conker/build/game-sine-effect-updater-150F7E20-match/`.
Tools commit before the consumer pin. Scoped Graphify refresh retains existing
unscanned nodes with explicit evidence; it is not full-corpus extraction.
Host Release stays frozen. The80% goal remains active.
