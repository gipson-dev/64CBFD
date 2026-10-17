# Overlay Fade Packet Recovery And Reload Gap

Date: 2026-10-17

Continue consumer **feea492e**, tools **e3da0c4**, after the direct reset in
[Note 1480](1480-overlay-mode-defaults-direct-match-20261017.md). Recover and
qualify the complete neighboring **func_15182670**, but do not replace its
byte-exact assembly with a shorter, nonmatching C body. This checkpoint adds
audit tools and a concrete matching handoff, not a production conversion.

## Complete Routine

- Owner: `conker/src/game/generated_1AC2F0.c`.
- Original: `conker/asm/1AC2F0.s`; preserved standalone nonmatching assembly.
- VA **0x15182670..0x15182748**, ROM **0x1AFB20..0x1AFBF8**.
- Retail **54 words / 216 bytes / frame 0x40**.
- Typed candidate **53 words / 212 bytes / frame 0x40**.
- **45 ordinal differences**, including the one-word length deficit.

The recovered interface is void with four byte-sized color arguments, signed
16-bit duration, byte channel, byte argument 6 and a 32-bit context. Retain
the address symbol; the short candidate comment describes the measured timed
color-overlay behavior without inventing a gameplay-specific name.

For positive signed duration, build an eight-byte packet at SP+0x34:
red, green, blue, alpha and channel at offsets 0..4; untouched padding at
offset 5; signed halfword fade at offset 6, calculated as alpha / duration.
Allocate an event through func_15149130 with the nine physical words
`duration, -1, 0x39, 3, 1, 0, 8, arg6, context`. If nonnull, use the actual
11-word SDK memcpy to copy all eight bytes to event+0x28. Nonpositive
duration makes neither call. The copy uses the SDK size_t prototype.

The candidate uses a properly sized local aggregate, not an out-of-object
copy. Padding is not zeroed. Retail copies its inherited byte at SP+0x39;
the guest oracle preserves that byte, including a scripted allocator change
made before the copy. This does not assert that portable C guarantees a
particular padding value across compilers or optimizations.

The allocator's existing recovered definition types argument 6 as a pointer,
while existing generated call sites use a word-sized payload length. This
uninstalled candidate follows those generated nine-word interfaces. Guest
checks qualify the physical ABI; native checks use a typed mock. Neither
proves whole-program C type compatibility or the complete allocator body.

## Measured Matching Gap

Retail has **three** incoming-duration LH instructions at offsets
**+0x18, +0x30, +0x68**, all from SP+0x52. C has **one**, at +0x18, and
adds a move into A0. Removing two loads and adding one move explains the
one-word length deficit, not complete register/schedule identity.

Moving the fade assignment after the other packet assignments restores late
division-trap checks, but still emits **53 words and one duration load**.
Thus trap placement alone does not restore the reloads. This is measured
evidence, not proof of the original C statement order or a compiler-stage
causal explanation. Do not add volatile, unprototyped calls, fake padding
operations or instruction guards to manufacture a match.

One bounded, read-only Claude advisory was used with no repository tools,
edits or builds. Its proposed fade-last experiment was tested. Its claimed
three-versus-two load count was corrected to **three versus one** from the
actual words. Local packet/receipt material remains under ignored
`conker/build/game-overlay-fade/`; the advice is not a matching certificate.

Complete positive guest execution performs **43 original accesses versus
41 candidate accesses**. All 168 configured access-fault gates fire across
both stack phases, but the access traces differ. No raw private-register,
fault-prefix equivalence, CP0/FCSR or hardware timing acceptance is claimed.
The two trap instructions and two dead overflow-path instructions are not
reachable in the bounded positive-duration/unsigned-alpha domain.

## Qualification

All **seven final tests pass in 124.087s**. The target suite checks the
complete emitted body, not a partial packet:

- **2,430 original/C guest pairs** against an independent full-memory and
  call reference, both stack phases, width truncation, signed gate, null and
  byte-unaligned destinations, inherited padding and three scripted provider
  modes. The actual eleven memcpy words execute; allocator effects are bounded.
- **384 native32 cases per O2/O0 profile**, separate full-body and typed
  caller translation units with UBSan. Check all seven semantic payload bytes
  and all outside canaries; exclude only padding byte 5. All eight effective
  semantic controls must exit 22.
- A zero-padding control deliberately passes the native fields-only checks
  yet changes the guest's copied byte 5. Native agreement is therefore not
  an installation or byte-match certificate.
- **Three independently linked original/C rebase pairs**, moving the entry
  and both actual call targets, **7,290 paired cases**. Preserve the 54/53
  extent difference; never claim equal rebased words.
- **288 paired cases across all four original call sites**. Execute full
  35-word callers at 0x150B6754 and 0x150D66A4, including two scripted RNG
  calls each. Execute original 13-word and 12-word call windows at
  0x15194EF4 and 0x151DC87C to their actual joins. Argument capture follows
  JAL delay slots. This is not the two larger parents or natural gameplay.
- All 53 target-word controls, three relocation-binding controls, 16 pool
  byte controls and **172 protected input entries / 163 distinct paths**
  fail closed. Preserve all **27 raw/padded owner neighbors**, inherited
  16-byte pool and **189,088 Game-data bytes / 720 owners / zero differences**.

The two target bindings are R_MIPS_26 func_15149130 at +0xA8 and memcpy at
+0xBC. Raw candidate SHA-256:
`f56f0f4328bb1f1cf0dfda3b78763c5b89ecdfa2cf0553a4b1a316025cfa95a8`.
The normal padder preserves the complete 53-word C diagnostic unchanged.
Live production retains its GLOBAL_ASM and all 54 original words.

## Bank And Resume

Production source, original assembly, ELF, progress CSV, guards, compiler
profile, layout and build files remain unchanged. Root README stays unchanged
because there is no new matching credit. The earlier 50-word reset remains
installed; the 633-word mirrored renderer and pulse lifetime remain open.

Fresh official matching is unchanged: Game **2,948/4,828 (61.06%)**, total
**3,621/5,501 (65.82%)**, still different **1,880**, zero address drift.
Init **492/492** and Debugger **181/181** remain exact. No normal production
rebuild is needed for an uninstalled diagnostic; all protected live input
hashes, including the existing ELF and source, pass their unchanged gates.

Tools **72f748d** banks four new files first. Four exact task pairs and
**eight ASCII/AST parses** pass. Eleven shared padder tests pass per copy:
active **0.020s + 0.027s**, mirror **0.017s + 0.028s**. Consumer tools-check
passes. The full target suite runs in the prepared consumer, not as a
separately claimed standalone compiler suite.

Preserve mirror HEAD **ddbdd16b** and all **1,037 initial dirty-file hashes**;
only four previously absent task files are copied, giving **1,041 dirty
paths**. No mirror commit/reset or push. No host/frozen Release action,
dependency/provider/configuration change or additional agent call. Existing
duplicate Makefile recipe warnings remain. The truncated-path compiler
scratch was confirmed disposable by the user; no recovery is needed.

Prepared-checkout checks, sequentially:

```sh
python3 -m tools.experiments.game_overlay_fade_packet
python3 -m unittest tools.tests.test_game_overlay_fade_packet -v
python3 -m unittest tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- [x] Recover and audit a complete typed fade packet, actual copy and callers.
- [x] Separate the three-versus-one duration reload gap from trap placement.
- [x] Keep nonmatching C uninstalled, with no new guards or matching credit.
- [ ] Trace the duration home/value lifetime in actual CFE/UOPT input/output;
  test a bounded, defined source shape only after identifying the lost reloads.
- [ ] Require all 54 words, caller ABI and private-state acceptance before
  replacing the original assembly. Continue the wider Game queue and renderer.
