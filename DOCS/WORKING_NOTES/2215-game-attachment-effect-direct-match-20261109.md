# Attachment Effect Direct Match - 2026-11-09

`func_150EEE00` replaces a false zero-return placeholder with the original
owner-mask gate, attachment transform and effect submission. All **80 words
/320 bytes** emit directly from C under existing **O2/g3**, with original
**0x60 frame**, no padding and **no guards or profile/binding changes**.

Production: Total **4,284 /5,513 (77.71%)**, Game **3,611 /4,840 (74.61%)**,
Init **492/492**, Debugger **181/181**, zero drift; **1,229** still different.
**127** more exact functions reach4,411/5,513 and80%. Conversion rows stay fixed.

## Recovered body and source shape

Owner `conker/src/game/generated_11C2B0.c`; original `conker/asm/11C2B0.s`.
VA150EEE00..150EEF40, ROM11C2B0..11C3F0. RA is saved at SP+0x34;
there are no saved S registers. Incoming A0 home is SP+0x60. A1's complete
word is saved at+0x64, with its narrowed working byte stored again at+0x67
in the first call's delay slot. Private float vector+0x54, six-byte Header
+0x4C, three integer coordinates in Header2+0x40.

```c
void func_150EEE00(u8 *owner, u8 selector);
```

- Return when owner word+0x94 AND D_800A163C[selector] is nonzero.
- Otherwise call func_150EEF80(owner,selector,255,1), ignoring its return.
  Reload owner and selector homes after the provider, then owner+0x1D4.
  A zero matrix pointer skips the remaining work.
- Transform the selected D_800A15F0 three-float record into the private
  vector with func_15143134. Its matrix address is the live base plus
  D_800A1638[selector]*64 bytes. Records are12 bytes; the two index/mask
  tables each have four bytes, and the offset table has12 floats.
- Set Header type3 and code-1 before the random call. After its return,
  set the halfword to((u32)random%3)+4 and the kind byte to0. Reload and
  truncate the live vector components into Header2. Submit
  func_151602C0(&header,&coordinates,255,255,255,255,255,0,0,255,1),
  then pass the live float vector to func_150F0A24. Header's final padding
  byte is left untouched.

The first screen's80-word/frame0x60 draft still had36 word differences.
Writing the gate's operands in retail's source order removes four. Using
the actual byte stride `(f32 *)((u8 *)D_800A15F0+selector*12)` removes the
remaining32 register/scheduling differences directly, without normalization.
Unsigned byte-stride and12*selector alternatives also match. Header-first
and integer-first local orders fail; they are not used.

## Necessary helper interface change, without matching credit

The same owner's still-unfinished `func_150EEF80` needs its recovered
`s32(u8 *owner,u8 selector,u8 value,s32 flags)` declaration for the original
byte-argument call sequence. Keeping the old unprototyped call creates a
different promoted-selector lifetime. A function-pointer cast emits an
indirect call and adds an instruction. Scoped declarations conflict with
the old zero-parameter definition, and IDO rejects unnamed definition
parameters. These alternatives were rejected rather than altering compiler
behavior or silently changing the call ABI.

Its placeholder definition now carries those four named arguments and an
explicit unfinished-body comment. It still returns0. IDO emits the four
incoming-word stores at SP+0/+4/+8/+12, followed by zero result, return and
NOP: **7 words**, previously3. This is a required interface correction,
**not a recovered helper body or a byte-exact function**. It earns **zero
matching credit**. Its entire28-byte prefix and symbol extent12->28 are
independently specified in the complete-image predictor. The target is the
only original aligned ROM caller of this helper; all42 other owner bodies
remain unchanged.

Original helper entry/early-return tests cover its real incoming homes,
low-byte third input, full fourth input, null owner and selector rejection.
They do not qualify the helper's large effect-producing body. No assembly,
data substitution or additional guard hides the unfinished implementation.

## Caller, table domain and portability boundary

The aligned ROM census finds one target JAL: ROM9DB5C/VA150706AC in
`func_15070690`. It forwards D_800D154C, (command-0x3E)&255 and an extra
third word containing the original command. The target ignores that A2
word. Its original two-formal body is retained: adding a third formal
emits81 instructions, and a variadic definition emits82. Neither matches.
The existing legacy cross-TU call with an extra argument is qualified as
the original N64 machine interface; no portable C claim is made for that
extra-argument invocation. Native tests call the typed two-argument target.
The caller's source/object and complete13-word routine remain unchanged.

The complete16-word dispatcher `func_15071D38` reads D_800D1580, indexes
D_80086150, and calls the nonzero entry with that same command. The wrapper
appears at table entries0x3E/0x3F, ROM22AD08/22AD0C, producing selectors0/1
on that registered route. Both registrations and the complete route are
checked in original and linked images. This establishes those two routes,
not whole-script or gameplay acceptance.

Retail has no table bounds check. Native C qualification covers all four
valid entries0..3, finite conversions and defined Header fields. Guest
checks cover every byte selector using the actual neighboring retail
read-only bytes, high incoming words, artificial private-home mutations,
wrapped matrix addresses and invalid-float integer-indefinite results.
Those cases do not establish portable out-of-bounds C behavior, hardware
FCSR/NaN/trap semantics or host/gameplay parity. The source comments on the
unchecked four-entry domain; no new runtime gate changes retail behavior.

## Qualification and image audit

- **112 frozen inputs**, complete raw/padded owner, exact register-mask
  union and literal-pool equality. All **42 unaffected functions** remain
  identical. Both padders agree on all44 functions. The actual three-command
  Make recipe reproduces the qualified object with zero compiler diagnostics.
- All320 target bytes and11 relocation sites are pinned. Single-byte and
  binding-name corruption controls reject. Retail-slot, helper-prefix,
  named-symbol and out-of-scope image corruption also reject.
- Entire-ELF prediction permits exactly **313 changed bytes, zero exclusions**:
  the target's retail body and extent12->320; the explicit helper argument
  homes/28-byte prefix and extent12->28; two closed three-symbol metadata
  cycles. The cycles reorder(D_800A15F0,D_80097BC0,D_800A19C0) and
  (D_800A163C,D_800A5E8C,D_800A1B8C), retaining every named value/type/section.
  They are predicted symbol/string ordering, not altered code/data bindings.
  All **6,052 function addresses**, **189,088 protected bytes /720 owners**,
  other bodies, guards, headers, Makefile and progress CSV remain fixed.
- **1,792 guest cases per body**, every one of the80 instructions visited,
  full literal state/access-order agreement. Provider snapshots qualify
  unsigned random remainder, ignored first result, reloads after resource,
  owner/selector-home and vector mutations, packet fields and live last call.
- Six independent GNU links pass **30 rebased candidate cases**, including
  six wrapped-base cases. **122 paired fault prefixes** compare
  GPR/FPR/HI/LO, memory, calls/snapshots, trace, dispatched word, PC and delay
  origin. Private-home, invalid-domain and fault cases remain guest-only.
- **96 complete wrapper cases per body** and **256 complete dispatcher-route
  cases per body** cover both registered commands, high/wrapped original
  commands, stack phases and all64 provider-mutation combinations.
- **16 original helper ABI cases** execute its entry window or complete
  early returns; **32 typed-placeholder connection cases per body** qualify
  its exact argument-home writes and ignored return. Helper matching credit0.
- **16 real point-transform connections per body** execute the original
  98-word helper's float-matrix path(58 words visited) and all40 words of
  the handwritten matrix helper. Both are baseline byte-exact. Independent
  balanced single-precision RNE results, diagnostic globals and later packet
  conversion agree. Fixed-matrix conversion/translation paths are outside
  this connection. The RNG's18-word baseline is exact; RNG execution/state
  remains an opaque provider here, with arbitrary32-bit returned words.
- Native32 **O0/O2/O3 each pass448 cases**, with trap UBSan, typed mixed
  argument ABI, Header6/Header2 12-byte sizes, owner offsets0x94/0x1D4,
  all owner bytes/word fields, defined packet fields and live vectors checked.
  Header padding is not read. All **16 compiled incorrect bodies** fail
  observably in IDO execution and every native profile; no execution error
  is swallowed as a semantic counterexample.

Seven fresh checks pass in both tools environments before and after install.
Both shared smoke checks are fresh; three unchanged shared regressions per
copy are explicitly reused by exact fingerprints. The sibling loader uses
an isolated three-module overlay, retaining its own available dependencies;
ten absent transitive modules, including the prior matrix model, are read
from mounted tools with exact dependency fingerprints recorded in the replay
and explicit-connection-fallbacks receipts. No sibling file is overwritten.

Production Make compiles only this owner, with zero compiler diagnostics;
ELF and recount agree with prediction. The inherited whole-ROM checksum
mismatch still makes make all exit2; existing duplicate Make recipe warnings
remain. Routine review uses zero Claude calls.

Tools commit before consumer; sibling tools2434 inherited dirty paths and
host frozen Release remain untouched. Graphify uses scoped AST refresh with
retention evidence and zero semantic API calls, not full-corpus extraction.
Fresh target command: `python3 -m unittest
 tools.tests.test_game_attachment_effect_150eee00_match -v` under WSL.
Receipts: conker/build/game-attachment-effect-150EEE00-match/.
Next queue: func_150F20F0, pending fresh audit; no credit assigned.
The80% goal remains active.

Production ELF SHA-256: e514b506e825ad0332137f8406aad09dbfdb44516b8c2c9b54d5fe4f2a2679e9.
Guard SHA-256: 6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7(unchanged).
