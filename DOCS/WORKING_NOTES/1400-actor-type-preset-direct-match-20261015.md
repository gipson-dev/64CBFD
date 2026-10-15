# Actor-Type Preset Direct Match

Date: 2026-10-15. Continue the full additional-source / Game objective from
[Note 1399](1399-packed-color-callback-byte-match-20261015.md).

## Result

Replace `func_1516ED68`'s zero-return placeholder with the semantic four-input
actor-type-gated factory preset in `conker/src/game/generated_19A8B0.c`.
**All 91 raw and production-padded words / 364 bytes match retail directly
from C**, VA `0x1516ED68`, ROM `0x19C218`, frame `0xD0`. No new guard,
compiler-profile change, volatile access or assembly body is used. Preserve
the address-based name and add a concise measured comment.

Use the archive's four-input void interface. The observed direct caller at
`0x15029AA0` ignores the result: after the call, its branch delay sets its own
V0 to 1. Retail still preserves all four incoming argument homes and RA.
The live C/include search finds only this definition, so no shared caller
prototype needs changing in this checkpoint.

## Recovery

The actual gate is the unsigned byte at
`D_800CC2D4[(u32)arg0 * 0x32C]`, equal to `0x3A`. Keep wrapping word index
arithmetic and do not introduce an actor-range check absent from retail.
The archive's word access is incorrect. An explicit byte local reflects the
retail load and restores its V0 allocation; the direct expression form is
91 words / 36 differences. Signed/unsigned word locals also emit identical
words, so the original local declaration is not uniquely recoverable.

On acceptance, submit the complete **49-argument** `func_1516D99C` packet,
including the two `0x124` extents and fixed preset constants. Preserve:

| Incoming Value | Outgoing Argument | Retail Width |
| --- | --- | --- |
| arg0 | 34 | Full word, also used as the actor index |
| arg1 | 31 | Full word |
| arg2 | 47 | Unsigned low byte |
| arg3 | 48 | Full word |

Argument 34's full-word store remains in the JAL delay slot. The real factory
later consumes narrow fields; qualify that storage separately from the
caller's complete physical packet. The rejected gate makes no factory call.

The archived `(u8)arg0` and `(u16)arg1` expressions are not retained in the
recovered source. Under the actual narrow callee prototype, IDO treats those
casts as redundant: both diagnostic bodies still emit all 91 retail words.
They are therefore **ineffective guest negative controls**, not evidence that
the guard is insensitive. Use effective low-bit changes instead. Two separate
native word-capture controls detect the narrowed expression values, while
the real factory-chain test verifies actual narrow-field consumption. Do not
conflate the wide capture provider with the real factory's C parameter types.

## Fresh Qualification

**All 13 installed checks pass in 43.045 seconds**:

- **4,626 paired guest cases** cover all 256 gate bytes, four full input words,
  the complete packet, two stack phases and three provider clobber modes.
  There are 3,096 accepted and 1,530 rejected cases. All 91 instructions are
  visited; exact registers, private stack, access events, saved RA and final
  call-delay store match original code.
- **Ten backed guest aliases** place the type byte in argument homes, the RA
  slot and outgoing packet storage. Predict the byte after the real prologue's
  home stores. **146 paired, fired guest-access faults** preserve partial
  memory, registers and events. This is guest evidence, not portable C fault
  semantics or proof that arbitrary wrapped addresses are valid runtime actors.
- **131,072 native32 cases per O2/O0 profile** cover every byte type for all
  512 actor indices in a deliberately backed test array. Capture all 49 words
  with actual signed-halfword first parameters and explicit word parameters
  thereafter. This fixture is not a claim that the game has 512 valid actors.
- **Eight effective compiled guest negatives** change the gate, stride,
  access width, actor/second-word low bits, flag width, last word or preset.
  All eight also fail native checks. Two additional native-only narrowing
  probes fail the word-capture contract, despite being redundant in IDO under
  the actual prototype. Do not weaken the effective-negative gate.
- Three **independent original/selected text, table and call rebases** match
  all 91 words across signed-low carry boundaries and verify both gate paths
  and complete packets.
- **256 real wrapper/factory/allocator-chain cases** include 52 gate rejections,
  51 null allocations and 153 registered records. Execute the original 125-word
  factory and 28-word allocator wrapper; compare every initialized record
  field. Only the lower heap and registration providers remain modeled.
  No full heap, gameplay or host-port acceptance is claimed.
- All **29 owner neighbors**, their raw bytes/sizes, normalized pools and
  relative relocations remain fixed. Check the actual caller's four call/
  branch words. Freshly verify all **801 original archive fingerprints**.
- Verify all **52 production input states**, all 52 corrupted immutable
  predecessor captures, the two exact successor inputs/captures, source-text
  and six physical corruption controls. The runtime actor field has no ELF
  payload; flip its actual symbol binding, not nonexistent BSS file bytes.

Reuse existing compiler, MIPS, packet, native32, relocation, factory and ELF
helpers. Prior unchanged suites remain historical receipts, not fresh tests
in this note. Routine work used zero Claude calls.

## Linked Image And Progress

The **3,257,636-byte ELF** equals an independent image predicted before
installation from the frozen predecessor plus the retail target slot and
symbol extent `12 -> 364`. Exactly **280 bytes change**, all target slot/
extent. **Every other ELF byte is fixed**, including the previous named
symbol serialization; there are **zero metadata allowances**. Preserve all
other code, **189,088 protected bytes / 720 owners**, and every guard byte.

Only ELF and owner change among the 52 scoped inputs; **50 remain fixed**.
The entire guard CSV, progress CSV, shared headers, original assembly and
configuration are unchanged. This replaces an already-C-classified stub,
not an extra converted function.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | e76ef88fa8f2d6f5442ce88c79dc512034b6cc1c6ca7d754bb6be13c321708f6 |
| Owner | cc04c9783d3a8a313ae0e2a440cb75df76c90d859c9b5f234cab10b96117bb99 |
| Unchanged guards | 2b2d5139c4d138257f5e0c4ce2d169a2f248aa00d524261167fe8a38ccd9a978 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Fresh official matcher: **Game 2,897/4,828 (60.00%)**, **total 3,570/5,501
(64.90%)**, **1,931 different**, zero drift. The rounded Game percentage is
among converted C functions, not full-game or gameplay completion. Init stays
492/492 and Debugger 181/181 exact; converted counts/bytes stay fixed. Root
README changes only the two affected aggregate rows.

## Banking And Next Work

Bank tools **50205ee** before consumer source/pin/docs. Shared tool checks
pass. Preserve older mirror ddbdd16 and all **659 initial dirty fingerprints**;
copy only four absent owned files for **663 final paths** and verify native
Windows syntax and the standalone ROM-free check. Do not commit/reset that
independently dirty mirror or copy history into it. No push, software install,
account change or host source/build/launch; keep Release frozen.

Evidence is ignored under `conker/build/game-actor-type-preset/`. Reproduce:

```sh
python3 -m tools.experiments.game_actor_type_preset
python3 -m unittest tools.tests.test_game_actor_type_preset tools.tests.test_game_actor_type_preset_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Next recover **func_1516EED4**, **84 words / 336 bytes**, ROM `0x19C384`,
frame `0xD0`, in this owner. The original signed gate is **slot < 4**, with
no added lower-bound check. Read `D_800DD2A0[slot]` as a byte, compare against
the signed word threshold, clear the byte **before** the factory call, and
preserve the full packet even on allocation failure. Do not silently turn
the signed gate into an unsigned range check. Recover both scalar widths and
the gate/clear/call lifetime before installing its C body.

Retain the full failed-comment/binding/unanchored queues in
[Note 1396](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
the inherited-stack renderer deferral and the wider Game objective. The prior
1,717-object audit is not rerun or reclassified as fresh evidence here.
