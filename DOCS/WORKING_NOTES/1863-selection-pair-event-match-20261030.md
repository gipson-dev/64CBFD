# 1863: Selection-pair event handler restored from C

Verified 2026-10-30. `func_15158FA4` replaces its zero-return placeholder in
[`generated_185560.c`](../../conker/src/game/generated_185560.c) with the
recovered selection/event/byte-opcode handler. All 56 body/slot words match
retail after 15 expected-word guards limited to integer temporary-register
fields. There are no inserted or omitted instructions, frame changes,
shared-header edits, compiler-profile changes or data-layout changes.

The actual linked recount is **3,940/5,506 (71.56%)** total and
**3,267/4,833 (67.60%)** Game. Init492/492, Debugger181/181 and zero drift
are preserved. The 75% goal remains active: **190** more to 4,130/5,506.
The C inventory and progress CSV remain unchanged.

## Behavior and recovered ABI

The third parameter is an unsigned byte. Opcode zero calls `func_1516972C`
with the selection pointer when its word at0x18 matches event word0, or its
byte at0x1C matches event byte4. The word comparison short-circuits both
byte reads. Opcode4 uses the same gate and passes the selection pointer to
`func_1519F400`. Other opcodes have no effect except45 (0x2D):

- If the current word matches event word0, replace it with event word4 and
  then copy event byte9 into selection byte0x1C.
- Otherwise, if it matches event word4, replace it with the snapshotted event
  word0 and then copy event byte8 into selection byte0x1C.

The byte reads occur after the word stores and remain live when the event
and selection overlap. Original helper arguments are pointers to the selection;
the alternate donor incorrectly passes the opcode and uses word-sized byte
gates, so that body was not adopted.

Registration is the event field at `D_8008B4A8 + 46*0x34 + 0x1C`,
VA0x8008BE1C, ROM0x2308DC. The existing `struct115.unk1C` declaration is a
three-argument void callback. Original dispatch windows forward selection inA0,
event/address inA1 and the low opcode byte inA2, and ignore V0:

| Parent | Original window | Words |
| --- | --- | ---: |
| `func_15169070` | 0x15169160 / ROM0x196610 | 5 |
| `func_15169260` | 0x15169340 / ROM0x1967F0 | 10 |
| `func_1516944C` | 0x15169514 / ROM0x1969C4 | 5 |

The original-ROM aligned census finds one function pointer at0x2308DC and
no direct target JALs. Whole source searches explicitly include ignored
generated files. The original frame is24bytes, RA is saved atSP20, and the
incoming third argument is saved atSP32 before masking. Duplicate words
at offsets0x7C and0x9C are retained and unreachable; all other54 words execute.

## Matching and qualification

Ignored artifacts are in `conker/build/game-selection-pair-event-match/`.
The ordinary source shape emits55words; a scoped second-value local and
inverse mismatch return recover the complete56-word layout and all branches.
Only15 integer register fields remain different. The guards implement checked
role mappings for the first/current/second values and later scratch registers;
opcode bits, branch displacements, memory offsets, literals, helper bindings,
stack homes, RA lifetime and both unreachable words retain their retail shape.
The original guard manifest remains an exact prefix of the new manifest.

- Complete owner:36 raw/padded neighbors and all pools are unchanged. Four
  inherited pointer/integer warnings are reproduced exactly; the selected
  routine emits zero diagnostics. Actual Make uses five commands, including
  the existing asm processor and six preserved `GLOBAL_ASM` functions, and
  reproduces the qualified padded object byte-for-byte.
- Guest:4,192 cases /12,576 executions cover every opcode byte, high input
  opcode bits, word and tag comparisons, helper mutations,128 aliases,
  46 interrupted-access prefixes, and96 cases across three rebased layouts.
  Unhandled opcodes also run with sparse null pointers. All three original
  caller windows pass192 cases total per original/raw/normalized program.
  Original and normalized programs agree on complete machine state; raw C
  agrees on memory, access traces, calls and ABI obligations. Its intentionally
  different caller-saved register choices are not presented as literal equality.
- Native32:2,064 cases each atO0/O2/O3 pass UBSan and nine effective controls,
  checking all record/event bytes, helper identity and pointer arguments.
  The independent native reference accounts for little-endian overlap of a
  byte and a word; the guest reference models original big-endian memory.
  Guest-only aliases and private argument-home behavior are stated separately.
- Fail-closed guards:226 raw-byte/binding corruptions are rejected. Every new
  guard rejects a stale compiled word and an unexpected relocation:30 controls.
  Fifteen guards change register fields only; none inserts or omits a word.
- Link: the full production ELF equals an independent full-file prediction,
  SHA-256 `6cc09cf10990dc908821993067016bf606fd824f044080bda2c876890bf31e80`.
  Exactly151 bytes change:150 code bytes and one symbol-size byte. There are
  zero metadata reorderings and zero exclusions. All6,055 other disassembled
  bodies, every function address, and189,088 protected Game bytes/720 owners
  are fixed. The complete16,933-file seal checks unchanged source and objects.
- Both tools copies pass eight fresh checks and their project-tools check.
  After production, two fresh installed checks run per copy; six unchanged
  semantic checks are explicitly reused through identical module/input/artifact
  fingerprints. Manifest consumers with unchanged guards retain their exact
  object bytes; only the qualified owner is rebuilt.

Helper effects are bounded models. Original helper instruction bodies,
complete parent execution and host-port/gameplay acceptance are not claimed.
The original caller windows, registration, callback arguments, masking and
ignored result are qualified independently of these helper models.

## Banking and continuation

Tools are committed first at **7362283dd76f38f83e4423762722335b60a3489a**, then the consumer pins that exact
commit. No push is performed. Existing dirty work in the older tools mirror
is preserved. Detailed updates stay in this note and documentation indexes;
the root README changes only its two aggregate exactness rows.

Graphify receives a scoped structural refresh with old-node/relationship
retention and source-validated callback/helper edges. This is not a full-corpus
re-extraction. Next screen **func_150F5340** from the actual live ELF queue; previously
deferred candidates remain private and uncredited.
