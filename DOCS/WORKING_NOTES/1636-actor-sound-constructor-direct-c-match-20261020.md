# Actor Sound Constructor Direct C Match

Date: 2026-10-20. Consumer predecessor: `e8479593`; tools predecessor:
`23bad49`. Tools **8061257** are committed first. No push.
Both the preceding and current goal turns make verified matching progress.
The wider **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_151BB044`'s false zero-return placeholder in
[generated_1E73B0.c](../../conker/src/game/generated_1E73B0.c) with the complete
purpose-commented routine, retaining its original name.
VA **151BB044..151BB0E0**, ROM **1E84F4..1E8590**.

All **39 words / 156 bytes / frame 56** emit directly from normal **IDO O2/g3**,
with **three original relocations, zero new guards and no profile change**.
Use the canonical `struct127` actor and the existing registration interface:

`u16 func_1000FA64(u16, s16, s16, s16, s32, u16, s16, s32, void *, s32, s32, s32)`.

The routine registers sound 4A7 at the actor's captured XYZ coordinates,
with amount 0x2000, rate 800, limit 200, callback func_151BB0E0, actor context,
zero auxiliary values and flags 8.

## Return And Conversion Evidence

The earlier isolated void/u16/s32 drafts all emitted identical words. That
alone did not prove an interface. The full pristine direct-call scan finds
only **func_1514F194 at 1514F1CC**, and the complete 93-word caller ignores
the target result. No aligned literal target-address references occur in
the pristine decompressed image; that is a bounded scan, not proof against
every possible dynamically constructed indirect reference.

The wrapper's actual post-call instructions restore RA/SP and return without
changing V0. Its original 109-word registration callee returns either zero or
an **unsigned halfword** from record +24. Retain that observable result with
`u16 func_151BB044(struct127 *actor)` and a direct returned call, rather than
inventing a constant zero result or assuming the author declared it void.
This establishes a faithful executable interface, not the original spelling
of an unavailable source declaration.

Retail first executes `trunc.w.s`, then sign-extends the low 16 bits.
Use **explicit (s16)(s32) casts**, not direct float-to-short casts, to preserve
the word-then-short operation for valid signed-word coordinates beyond the
signed-short range. The prepared MIPS/native32 implementations narrow the
integer word to its low 16 bits. Float-to-word inputs are finite and within
the signed-word conversion domain; out-of-domain conversions are not claimed.

The callback is passed **by address only**. Its original body uses the
sound-record context, word-output pointers and seventh halfword-output
argument, but remains independently unrecovered C. Preserve its existing
old-style unspecified-argument declaration and stub; do not invent a false
zero-argument prototype or claim callback behavior was restored here.
No shared callback/SDK ABI or header is changed.

## Fresh Qualification

[Integration helper](../../tools/experiments/game_actor_sound_constructor.py)
and [seven tests](../../tools/tests/test_game_actor_sound_constructor.py)
reuse the existing compiler, original assembler, object/pool parsers,
padder, MIPS oracle, native32, actual Make and strict image gates.
Extend the existing instruction runner only with the already-established
finite signed-word truncation operation.

Seven pre-install and seven installed tests pass in **both copies**, with
no errors, failures or skips:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Pre-install | 6.176s | 6.513s |
| Installed, sequential reruns | 7.296s | 7.667s |

- **378 cases / 756 modeled phases** check all XYZ capture reads, signed-word
  truncation before signed-short narrowing, all twelve registration arguments,
  full returned handle, provider actor mutations and finished incoming-home
  probes. Compare complete modeled register/FPR/condition/HI/LO state,
  public/private RAM, histories and visits. All 39 target words execute.
- **377 native32 cases** pass O0/O2/O3 with both undefined-behavior and
  float-cast-overflow sanitizers trapping. Check canonical actor size/XYZ
  offsets through IDO layout assertions and native typed field views/canaries.
  The sole physical incoming-home case is guest-only.
- **Ten compiled semantic controls** fail with the expected mismatch: wrong
  sound, X/Y/Z, amount, rate, callback, context, flags, or discarded return.
- Independently assemble the complete original symbolic target; all three
  bindings agree. Three callback/helper rebases, including a signed HI16/LO16
  carry boundary, pass **42 phases** with moved actor buffers.
- Execute **80 phases through the original 109-word func_1000FA64**, with
  **48 fired finalizer calls** and **91 original registration words visited**.
  Check counts 0/1/31/32/33, successful/failed finalization, unsigned handle
  boundaries, all initialized record fields, untouched bytes and count changes.
  The callback-nonzero/flags-8 target does not reach every generic helper path.
- Execute the **complete 93-word original caller in eight phases**, covering
  both global-gate values, allocation outcomes and stack phases. All 93 caller
  words execute; target actor forwarding and preserved registers are checked.
- **Seven strict image negatives** reject unrelated header/code/data,
  target-size, truncation and appended-byte changes.
- Both shared tools checks pass; all four Python copies parse and task files
  agree byte-for-byte. No Claude call was needed.

The ratio provider (argument zero, result 1.0), table finalizer and other
caller providers are bounded contracts, not executions of their complete SDK
implementations. The actual registration and caller instructions are executed.
The callback itself, arbitrary guest faults, hardware FCSR/MMU and full
gameplay/host-port acceptance remain separate.

## Exact Production Image

Preserve all **56 other raw/padded owner functions**, constant pools, existing
GLOBAL_ASM preprocessing and inherited diagnostics. The isolated target has
no diagnostics. **Five productive actual Make commands** reproduce the
qualified object under the unchanged O2/g3 profile.

The production build passes in **19.515s** and exactly reproduces the complete
independent first-link prediction:

- **117 changed ELF bytes**: **116 instruction bytes** and **one symbol-size
  byte**, target extent 12 to 156. No metadata exclusions or cycles.
- All **6,055 other linked bodies**, all **6,056 linked addresses** and all
  **189,088 protected Game-data bytes / 720 owners** remain fixed.
- Shared structs/functions headers, original target/caller/registration assembly,
  registration/caller C, ROM, guard manifest, Makefile and progress CSV remain
  byte-identical. No conversion-row credit is added for already-counted C.
- ELF SHA-256:
  `68e65c6edf8656812c4a8708a0789e1202185415a055241252f6bda855d39406`.
- Installed tests audit the current source/image before reusing historical
  fixtures. Unchanged broad neighbor-suite receipts are reused through the
  whole-image proof, not described as freshly rerun tests.
- The known duplicate generated_12D630 Make recipe warning remains.

## Counts And Next Function

Fresh full matcher: **3,701/5,505 exact (67.23%)**, Game **3,028/4,832 (62.67%)**,
**1,804 different / zero drift**. Init stays 492/492 exact; Debugger stays
181/181. The current 75% threshold is 4,129: **428 more matches** remain.

The new ELF-pinned queue contains **1,670 simple zero-return placeholders,
125 semantic/other definitions and nine unlocated entries**. All emitted
functions are reclassified; unchanged source shapes reuse the strictly
pinned predecessor. Queue entries are triage, not ABI qualification.

Next **func_151CE634**, VA 151CE634..151CE6D0, ROM 1FBAE4..1FBB80:
the initial complete two-phase/two-row linked-list search draft emits
**41 words / frame 0 / 41 differences** against retail's 39 words.
Recover phase/index lifetime and nested-loop scheduling, then qualify table
column domains, node type 11, associated context at +98/+48, linked-list
order/termination, exact pointer return, callers, full owner and image.
The draft is **uninstalled / zero matching credit**; do not normalize its
words or change classifications to inflate the percentage.

Keep README updates aggregate-only and detailed recoveries in working notes.
Commit tools before the consumer pin, with no push. The existing post-commit
Graphify hook refreshes the graph; terminal/retention receipts belong in the
ignored target checkpoint. Preserve mirror HEAD ddbdd16 and all **1,484**
pre-existing dirty paths/statuses/hashes; add only the two absent task files,
leaving 1,486 dirty paths. Host sources, saves, configuration and the frozen
Release checkpoint are untouched.
