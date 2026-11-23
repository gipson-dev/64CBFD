# 2646 - Effect preset packet direct match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_150C04C0` in `conker/src/game/generated_EC420.c` replaces its false
zero-return placeholder with the complete particle preset builder. All
**98 words emit directly from C** in the original **152-byte frame**, with
**zero guards, insertions or omissions**. Both owner padders and the actual
Make recipe preserve the other nine functions, pools and diagnostics.

Production: **4,627 / 5,528 (83.70%) total**, **3,954 / 4,855 (81.44%) Game**,
zero address drift, **901 different**, **72 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Conversion and byte rows remain unchanged.

Original: `conker/asm/EC420.s`, line 1465; VA `150C04C0..150C0648`,
ROM `ED970..EDAF8`, 392 bytes. Its external bindings comprise the call to
`func_15150400` and ten data symbols.

## Source and ABI recovery

The six arguments are position pointer, optional `ExtendedState15F680`
pointer, word resource ID, byte enable flag, byte channel and word context.
The position is copied as three words, preserving signed zero and NaN payloads.
The resource ID remains a full word. The enable flag tests all eight bits;
the channel is read from its big-endian byte argument home. The only literal
caller discards the return, so the recovered builder has a void interface.

The local 100-byte preset contains count 9 plus random range 4, position,
speed/vertical ranges, lifetime halfwords 80/60, size/jitter values, the state
pointer, chance/offset/aspect values, three local-data pointers, radius 78,
the boolean flag, kind 14 and four extra bytes. The angle packet contains
signed halfwords `{0, 255, -50, 35}`. The local resource, one-entry size table
initialized from `D_800A0108` and extra float initialized from `D_800A0170`
remain live through the synchronous consumer call. The two padding bytes
at preset+0x5A are intentionally left untouched.

Field offsets and widths follow the original complete consumer in
`conker/asm/17CAF0.s`, not its unfinished source placeholder. In particular,
preset+0x34 passes the state pointer to the already recovered actor factory;
that factory copies its nine-word state. The original caller prepares a
nine-word state and places its position immediately afterward. No consumer,
shared header, caller body, compiler profile or padder implementation changes.

The first source form had 98 words but frame 144 and a direct byte-store
boolean. A semantic word temporary for the boolean restores the original
V0 lifetime and frame 152. Four remaining stores exposed a field-mapping
error: chance/offsets occupy +0x38/+0x3C/+0x40, while aspect 10 occupies +0x44.
Correcting those fields produces the complete direct match without guards.

## Focused qualification

Five gates pass freshly in each tools setup before adoption. Installed runs
freshly repeat the complete-owner, actual Make and independent image gate;
four semantic gates are explicitly reused only after exact source, raw object,
binding, original target, native artifact, manifest and import hashes agree.

- Raw C, padded C and original target each pass **128 direct cases** and
  **four guest alias cases**. Full private memory, GPR/FPR, HI/LO, ordered
  accesses, calls and packet observations agree. Every target word executes.
  An independent field oracle checks every initialized field, the complete
  angle packet, all three local pointer values and untouched padding.
- The complete original **32-word `func_15074C00`** runs with each target
  stream across **ten cases**. Selector 5 and 0x85 exercise the enabled path;
  other selectors exercise the gate. The state preparer and packet consumer
  are bounded providers. This is complete original-caller coverage within
  that boundary, not execution of the full particle subsystem or gameplay.
- **156 fired memory-access fault-prefix triples** compare full memory,
  GPR/FPR, HI/LO, calls and trace, including both flag outcomes, two stack
  phases, home mutation and a guest-only position/packet overlap. Provider
  internals, asynchronous faults and hardware remain outside this model.
- Actual SDK32 **O0/O2/O3 each pass 196,608 cases**, sweeping every enable
  byte and channel byte under three high-word patterns, full resource/context
  words, optional state pointers and floating payloads. The noinline typed
  consumer checks all named fields and pointed-to locals. UBSan and strict
  aliasing are enabled. Six source controls fail comparison: low-bit-only
  enable, byte-only resource, missing state, wrong chance, wrong aspect and
  wrong extra size. Native tests do not read uninitialized padding.
- Both full-owner and isolated-target padders remain direct-exact.
  **12 GNU links / 96 guest rebase runs** cover four independent code,
  callee and HI16/LO16 data arrangements, including signed-low-half carry
  and a different J26 region. Four wrong-word/binding controls fail.
  The generated padder rejects an oversized nonzero body; the generic
  padder's supported overflow trampoline also fails exact comparison.
- `make tools-check` passes. The actual sibling tools HEAD, dirty state and
  retained dependency hashes are preserved using a disposable overlay with
  explicit primary fallbacks. Existing duplicate Make recipe and legacy
  compiler warnings remain; changed-owner diagnostics do not grow.
  Routine Claude calls: 0. No sibling host import/build or Release change.

The literal aligned-edge census finds one direct call at `15074C68` in
`func_15074C00`, with no aligned exact-word pointer in the pinned binary.
Computed or separately materialized pointers are not excluded. The existing
source caller already submits the six measured arguments and ignores return.

## Independent whole-image audit

The actual linked ELF equals the independent prediction across **all bytes**:
**476 changed bytes, zero exclusions**. The target's 392-byte slot and symbol
size 12->392 change. Eleven symbol records reorder in closed name-preserving
groups, with their exact list pinned in the fixture manifest. This is metadata
ordering, not address drift or an allowance for other function/data changes.

The independent reference recompiles the frozen OLD owner with OLD guards,
requires its entire padded object to equal the old production object, then
replaces only this target with independently assembled original instructions.
It does not compile recovered target C into the reference. The predictor
requires identical ELF geometry, the complete named-definition multiset
after the one declared size update, and complete nonconflicting reconstruction
of the string pool. It reconstructs and compares the literal full ELF; no
symbol/string section is excluded. The exact eleven ordering records are
checked on every gate. An initial packaging assertion assumed no reordering;
the reviewed closed ordering is now explicit, and the full gates rerun.

All **189,088 protected Game data bytes across 720 owners**, other loaded
bytes, function addresses, other extents, guard history, conversion rows,
headers, profiles and private inputs remain fixed. Fresh production Make and
live recount establish the totals. Documentation and graph cache changes are
accounted for separately in the final input bank. Source matching does not
establish host or gameplay acceptance.

Raw target SHA256: `fac39e0be9956fb4397a83bdedc0a243b015a71571c07c5f5da8f70cbab9d4ff`.
Qualified full-owner SHA256: `30ab5e8363bbb7d4f1abc211b1d32f10c70649df73d836ebaf8872f5f7bb7ff1`.
Production ELF SHA256: `8c2363aee5eeb20a66bf5b7a37d5e79cf3dea975f163f704bd1ac94c1527c2a3`.

```sh
python3 -m unittest tools.tests.test_game_effect_preset_150c04c0_match -v
```

Artifacts: `conker/build/game-effect-preset-150c04c0-private/`. The fixture
fails closed when its phase inputs change. Codex owns implementation and
validation. Tools are committed before the consumer pin; no push.

## Next work

The previous direct recovery remains banked in
[Note 2645](2645-game-paired-preset-factory-requests-direct-match-20261122.md).
The separate `func_150A6760` decoder forms remain private and uncredited;
[Note 2644](2644-game-visibility-bitplane-decoder-private-recovery-20261122.md)
retains their limits. The next same-owner stub is `func_150BFFE0`, 127 words,
frame 160, ROM `ED490..ED68C`. It snapshots actor coordinates before an
eight-argument `func_15136C3C` call, then submits a local descriptor to
`func_15153634`. The existing 108-byte descriptor layout in
`generated_1D0840.c` at line 751 and its byte-argument consumer prototype
provide a starting interface; verify it against the complete consumer ASM.
Continue toward the full 85% matching goal with 72 further matches required.
