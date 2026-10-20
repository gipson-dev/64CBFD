# Actor Position Dispatch Direct C Match

Date: 2026-10-20. Consumer predecessor: `f98952ff`; tools predecessor:
`55e2533`. Commit tools **23bad49** first, then the consumer source/docs/pin.
No push. The wider **75% total C-matching objective remains active**.

## Installed Function

Fit the existing semantic `func_15070C40` in
[game_981E0.c](../../conker/src/game_981E0.c), retaining its original name,
canonical `struct127` / `struct17` types, existing helper declaration and a
purpose comment. VA **15070C40..15070CDC**, ROM **9E0F0..9E18C**.

All **39 words / 156 bytes / frame 64** emit directly from normal **IDO O2/g3**,
with **five original relocations, zero new guards and no Make/profile change**.
The old C emitted 40 words and overflowed its 39-word retail slot. The linked
slot therefore held a trampoline, not those 40 instructions.

The function captures the current actor's XYZ floats at 14/18/1C into a
private three-float vector. Its byte at 124 selects the current actor when
zero, otherwise one-based D_800CC2D0[index - 1], stride **32C**. The selector's
role is deliberately not renamed to "parent" or "owner" without further evidence.
Call func_15103E40(selected, current, &position, mode, 0, 255, 0).
Mode remains unsigned byte. The conditional helper argument restores the
retail selection/register schedule; no dummy locals or frame tricks are added.

## Focused Qualification

[Integration helper](../../tools/experiments/game_owner_position_dispatch.py)
and [six tests](../../tools/tests/test_game_owner_position_dispatch.py) reuse
the existing compiler, balanced C parser, padder, MIPS oracle, native32,
GNU assembler/linker and protected-data checks.

Six pre-install and six installed tests pass in **both** tools copies,
with no failures, errors or skips:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Pre-install | 24.714s | 27.067s |
| Installed | 23.670s | 10.653s |

- **704 cases / 2,816 guest phases** cover every selector byte, every mode byte,
  high argument bits, raw float bit patterns, signed zero, two stack phases,
  current/selected actor aliases and provider mutations. Compare complete
  modeled GPR/FPR/HI/LO/condition, public/private RAM, histories and visits.
  All 39 target words execute across the corpus; preserved ABI registers restore.
- The helper receives all **seven** arguments and the captured three-word
  snapshot. A bounded provider changes the live actor and current-actor global
  after capture without changing the private position snapshot.
- **319 defined native32 cases**, valid selector domain **0..26**, pass
  O0/O2/O3 with trap UBSan. The native typed actor/vector views are checked
  against canonical IDO layout assertions, including byte width, all XYZ
  offsets, selector offset, vector size 12 and actor size 32C.
- Eight compiled semantic controls fail with the expected mismatch: current
  actor only, next selected row, wrong X/Y/Z, wrong mode, flag or sentinel.
  No undefined-index-only failure is counted as a semantic control.
- Independent symbolic GNU assembly is reconstructed from the pristine retail
  opcodes, not the candidate object. It agrees with all five C bindings.
  Three independent global/helper HI16/LO16 rebase sets pass **126 phases**.
- Scan every pristine US Init/Game/Debugger function for direct JALs. The only
  direct sites are **func_15070CDC at 15070CE8** and **func_15070D00 at 15070D0C**.
  Execute both complete nine-word original wrappers in **110 cases**. They
  supply modes 1 and 0 and restore their ABI state.
- Four image negatives corrupt unrelated Game code, protected data, another
  overflow body and the ELF header. Each is rejected.
- Both existing shared tools checks pass; all four task Python copies parse
  and agree byte-for-byte. Routine work uses zero Claude calls.

Selectors 27..255 are guest address-arithmetic tests, not valid native array
indices. Nonfinite/signaling float patterns are copied in the bounded guest
model only; native vectors use finite values. The dispatch helper is a bounded
provider, not executed original helper behavior. Hardware FCSR/MMU, arbitrary
fault-prefix parity, complete gameplay and host-port acceptance are not claimed.

## Owner And Whole Image

Preserve all **327 other raw/padded owner functions**, relocation-normalized
pools, the existing GLOBAL_ASM preprocessing path and inherited diagnostics.
An isolated selected body emits no diagnostics. Five actual productive Make
commands reproduce the qualified raw/padded object under unchanged O2/g3.

The production build passes in **52.727s** and reproduces the independent
first-linked ELF **byte-for-byte**. Its complete prediction has **zero metadata
exclusions** and explicitly accounts for:

- Replacing the target's 156-byte trampoline slot with all 39 retail words.
- Removing only its obsolete **160-byte** overflow body.
- Moving six later overflow bodies down by 160 bytes, preserving every
  instruction in those bodies.
- Relocating four existing jump destinations at **150768DC, 15076D3C,
  150781F4 and 150A7B80**. All retail function entry addresses stay fixed.
- Removing the obsolete local overflow symbol, rebuilding suffix-shared
  symbol strings/name offsets in the same symbol order, and adjusting the two
  overflow ROM-end definitions and exact ELF/program/section headers.
- Preserving every other code/data section and all **189,088 protected
  Game-data bytes / 720 owners**. Do not describe this as "all other raw linked
  instruction addresses unchanged": the six overflow addresses intentionally move.

The ELF shrinks **192 bytes**, from 3,257,636 to 3,257,444. Its SHA-256 is
`6be5792039aeeb4dcef032c8bd4f0803963675db1b41cf19e4e6ec34c01b2e0f`.
ROM, shared structs, retail layout, guard manifest, Makefile and progress CSV
stay byte-identical. The known duplicate generated_12D630 recipe warning remains.
Historical broad neighbor-suite receipts are reused through these closed
whole-image gates, not claimed as freshly rerun tests.

## Progress And Next Target

Fresh full matcher: **3,700/5,505 exact (67.21%)**, Game **3,027/4,832 (62.64%)**,
**1,805 different / zero drift**. Init stays 492/492; Debugger stays 181/181.
The present 75% threshold is 4,129: **429 more matches** remain.

The new ELF-pinned remaining queue contains **1,671 simple zero-return
placeholders, 125 semantic/other definitions and nine unlocated entries**.
Reclassify all emitted functions; reuse unchanged source shapes only through
the pinned predecessor and target-only source proof. This queue is triage,
not ABI or C qualification.

Next **func_151BB044**, VA 151BB044..151BB0E0, ROM 1E84F4..1E8590:
the complete isolated actor-position/sound-constructor expression emits
**39 words / frame 56 / zero differences** with void, u16 and s32 return
declarations. Those three identical outputs do **not** settle the correct
return interface. Audit direct callers, the existing u16 func_1000FA64
interface and callback signature, signed-short coordinate narrowing, finite
float-to-int domain, argument homes, full owner and actual Make/image gates.
Its draft remains **uninstalled / zero matching credit**. Keep the larger
func_1508CAD8 stub queued; do not replace proper semantics for a percentage.

## Checkpoint Boundaries

Keep only aggregate status rows in the root README; detailed recovery updates
belong here and in concise documentation indexes. Commit tools before the
consumer pin. No push. The existing post-commit Graphify hook refreshes the
graph; terminal process/retention evidence belongs in this target's ignored
final-checkpoint receipt.

Preserve the independent mirror HEAD ddbdd16 and **all 1,482** pre-existing
dirty paths/statuses/hashes. Add only the two absent task files, leaving
1,484 dirty paths; do not commit/reset that mirror. No host source, saves,
configuration or frozen Release artifact is changed. The user confirmed that
the previously overwritten `.../Desktop/.vscode/Conkers` file was disposable
compiler scratch; that recovery question is closed.
