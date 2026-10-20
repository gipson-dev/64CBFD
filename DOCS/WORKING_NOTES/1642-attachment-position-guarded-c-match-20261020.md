# Attachment Position Guarded C Match

Date: 2026-10-20. Consumer predecessor: `5f78429b`; tools predecessor:
`c6aefcc`. Tools **7aa7932** are committed first. No push.
The **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_150C5BD4`'s false zero-return placeholder in
[generated_F2820.c](../../conker/src/game/generated_F2820.c) with the complete
attachment-position update. Preserve its address-based name, add a purpose
comment and use the existing actor's named state, unique-ID and position fields.
VA **150C5BD4..150C5C74**, ROM **F3084..F3124**, **40 words / 160 bytes**,
**24-byte frame**, one R_MIPS_26 call binding, normal **IDO O2/g3**.

The first gate dereferences the attached actor and checks its state word,
not whether the actor pointer is NULL. Return zero for state zero or a saved
identity-byte mismatch. Otherwise copy the actor's three world-position
floats when its matrix table is absent; preserve the original sequential
stores and repeated pointer reads. With a matrix table, pass the local
offset at effect+0xD0, output at +0x24 and matrix base plus the **unsigned
byte index times 64** to `func_15143134`. Return exactly one after success.

The existing callback table `D_80088760` holds this function at entry one.
The callback's Boolean result controls whether its caller removes the effect.

## Single Closed Guard

The semantic C has the exact 40-word extent, frame, branches and lifetimes.
Only word **34 / offset 0x88** differs:

```text
C:      01883021  addu a2,t4,t0
retail: 010C3021  addu a2,t0,t4
```

Append **one** expected-word/no-relocation row to
[the guard manifest](../../conker/retail_word_patches.us.csv). Both instructions
write the same register, use the same inputs and perform commutative wrapping
ADDU without an overflow trap or HI/LO effects. No instruction is inserted,
removed or rescheduled; no register lifetime or compiler profile changes.
This is **guarded semantic C**, not compiler-only byte-exact output.

The original source slot includes unreachable duplicate loads at word indices
**10, 17 and 29**. Preserve all three byte-for-byte; execute and compare the
other **37 reachable target words**, not claim all 40 are visited.
Pointer/addend reversals, integer address forms, compound additions and a
64-byte array view were bounded non-installable screens, not accepted fits.

Keep the entire previous working-tree guard prefix byte-identical:
SHA-256 `7ccd028cda1fdbe5f212c315aa649188f3b88f72b7003cf5573eb5c01d048115`.
The installed manifest is exactly that prefix plus the certified row:
`36513f2bad7fd30dbf191f428a3e0d154726fa4e9bfb619d5f0a36bda28987ae`.
The staged diff adds one row; no line-ending normalization is performed.

## Focused Qualification

[The module](../../tools/experiments/game_attachment_position.py) freezes 13
source/header/assembly/image/build inputs.
[Eight tests](../../tools/tests/test_game_attachment_position.py) pass in both
tools copies, pre-install and installed, with no failures/errors/skips:

| Stage | Primary | Older Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 21.809s | 14.376s |
| Installed source | 13.616s | 14.115s |

- **556 cases / 1,112 three-way phases** compare complete modeled original,
  raw-C and guarded-C state. Check all unsigned matrix indices, nonzero
  signed-word states, both stack alignments, clobbers, exact return values,
  lazy reads and sequential coordinate copies. Twelve overlap cases are
  guest-only; do not claim portable native overlapping struct objects.
- NULL actor input faults at retail's first state read in the bounded guest.
  No defensive NULL behavior is introduced or claimed as portable C.
- **544 native32 cases**, O0/O2/O3 with trap UBSan and FP contraction disabled,
  call the actual C through a typed callback table. Check the actor subset
  layout, exact packets, byte indices/identities, outputs, return and fences.
  **Nine compiled semantic negatives** all reach rejection23.
- Six guard-corruption controls reject wrong expected words, offset/binding,
  changed raw input, missing binding and an actually assembled SUBU replacement.
  The latter produces a wrong matrix packet. Omitting the guard retains the
  measured one-word mismatch; commutative raw C still has the same semantics.
- Scan all pristine functions and aligned ROM words: **no direct JAL**;
  exactly one literal target pointer at **ROM 22D224**, table entry one.
  Execute the complete **79-word func_150C5568 in 56 phases**, including flag
  and signed selector gates, ignored callback selection, success/failure,
  all coordinate comparisons and removal/updated-distance decisions.
  The distance and removal routines remain bounded providers.
- Three independent GNU call rebases pass **54 phases**.
- **90 original math-chain phases** execute **97 of 98** helper words,
  **45 of 46** SDK slot words, all **40 matrix-transform words** and all
  **49 translation words**, including float/fixed matrix formats and zero
  offset. The wrapper cannot reach helper word82: its pointer is non-NULL,
  and that instruction belongs only to the helper's NULL input path.
  The SDK's final alignment word is likewise not executable coverage.
- The preflight fixed missing HI initialization and signed LB support in the
  new oracle. The first full run correctly rejected its overbroad helper
  coverage claim; verify the exact missing NULL-only word before correcting
  the assertion. These are fixture corrections, not production changes.
- Seven strict-image negatives and both shared tools checks pass.
  Hardware/FCSR/MMU, invalid memory, arbitrary matrix/FP domains, full gameplay
  and host-port acceptance remain separate. Routine task: **zero Claude calls**.

The older mirror stays at **ddbdd16**. Preserve all **1,496** pre-existing
dirty statuses/hashes, add only the two absent task files and verify both
copies byte-identical and all four Python files AST-valid. Final dirty count
is **1,498**; do not commit/reset the independently dirty mirror.

## Production And Progress

Preserve **14 other raw/padded owner functions**, bindings, pools and inherited
diagnostics. The actual Make path has **three productive commands**, and its
normal O2/g3 raw/padded output equals the independently qualified objects.

After proving the exact single-owner guard suffix, reuse unaffected objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
```

The first command rebuilds the changed owner and performs the complete link;
`-o` acknowledges only the proven unchanged guard dependencies for other
owners. No compiler flags, Makefile or timestamps are changed. This is not
a claim that every unrelated owner was freshly recompiled. A later ordinary
Make invocation may rebuild more objects because the manifest is newer.
Broader unchanged suite receipts are reused through the source/prefix and
strict whole-image proof, not represented as fresh reruns.

Production passes in **34.541s**, reproducing the strict independent ELF
prediction: **112 changed bytes = 111 code + one symbol-size byte**,
extent **12 -> 160**, **zero metadata exclusions**.
All **6,055 other bodies**, **6,056 addresses**, and **189,088 protected
Game-data bytes / 720 owners** remain fixed. ROM, original assembly, shared
headers, Makefile and progress CSV are byte-identical. The inherited duplicate
generated_12D630 recipe warning remains, alongside Git's existing CRLF/LF
notice for the manifest; do not call this warning-free.

ELF SHA-256:
`180ab67fdf083d4adb81720eee40f661390c74bcd488f2b2bbbfc7c7b447d1a8`.

Fresh standard matcher: **3,707/5,505 exact (67.34%)**, Game
**3,034/4,832 (62.79%)**, **1,798 different / zero address drift**.
Init remains 492/492; Debugger 181/181. Converted counts/bytes are unchanged.
The threshold is 4,129, leaving **422** more matches. Queue source shapes:
1,664 placeholders, 125 semantic/other and nine unlocated. These are screens,
not qualification or permission to replace real semantics with placeholders.

## Next Target

Queue **func_1514D310**, `generated_179F30.c`, VA **1514D310..1514D3B0**,
ROM **17A7C0..17A860**, **40 words / frame48**. Inspect the +0x2F4 list,
signed descriptor/callback indices, -1 sentinel, cached successor before
callback/removal and both callback tables. Preserve the exact one return.
No draft, installation or matching credit is claimed. Keep
`func_1508CAD8` queued separately.
