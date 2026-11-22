# 2640 - Compact sprite lifetime and motion updater

Date: 2026-11-22. The full 85% matching goal remains active.

`func_15167E0C` in `conker/src/game_1944C0.c` replaces its false zero-return
placeholder with complete lifetime, alpha fade, fixed-point motion, animation,
callback and cleanup C. All **195 raw words** normalize to all **195 retail
words and named relocations**, in **frame 32**, with **38 guarded rows** and
**zero insertions or omissions**. Raw C is not byte-exact.

Original: `conker/asm/nonmatchings/game_1944C0/func_15167E0C.s`.
VA `15167E0C..15168118`; ROM `1952BC..1955C8`; 780 bytes.

Production: **4,622 / 5,528 (83.61%) total**, **3,949 / 4,855 (81.34%) Game**,
zero address drift, **906 different**, **77 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Conversion rows remain unchanged.

## Recovered body and ABI

The signed 16-bit remaining counter at `0x38` has an immortal `0x7FFF`
sentinel. Other values subtract the low 32-bit tick word, store/reload as
signed 16-bit, and clamp negative results to zero while setting completion.
The signed fade step at `0x3A` runs only when positive. If it is smaller than
unsigned alpha `0x3F`, alpha is reduced; otherwise remaining becomes zero and
completion is set. Alpha itself is deliberately left unchanged on that path.

The signed update selector at `0x2F` skips only `-1` or a null table entry.
The one-pointer update callback runs before the second lifetime test. The
completion flag is sticky: a callback can restore remaining and permit motion,
while an earlier expiration still causes completion afterward. Both callback
boundaries preserve the caller-owned incoming argument home; guest tests can
retarget the subsequent record through it.

For a nonzero remaining counter, signed 16-bit vertical velocity first gains
acceleration, with its store/reload preserved. Coordinates use eight fraction
bits: Y is updated before X, then Z, with a fresh live tick load for each.
Packed adds and products preserve the low 32 bits, followed by a signed
coordinate store and unsigned fraction-byte store. The source uses explicit
unsigned arithmetic around shifts/products to avoid signed overflow.

For nonzero animation speed, the frame bound is `(texture[4] << 8) - 1`,
captured before writing phase. The phase update stores/reloads signed 16-bit.
Upper flag `0x20` and lower flag `0x40` terminate. An ordinary upper crossing
sets history flag `0x80`; flag `2` reflects phase and reverses speed. Other
paths repeatedly subtract/add the bound with a signed 16-bit store/reload
on every iteration. A generic modulo shortcut changes boundary behavior.
Frame count zero yields bound `-1`, with finite but potentially long wrap paths.

If completion is set, signed selector `0x48` skips only `-1`; a selected
completion function has no null guard. Cleanup follows the completion callback
and reloads the record argument afterward. Its decision is not undone by a
completion callback changing remaining.

`CompactSpriteState` is a local measured 76-byte partial view, not a claim
about an original type name. Opaque regions retain unidentified contents.
Its 19 used field offsets are asserted under actual SDK32 types: texture10,
phase1C/speed1E, XYZ20/22/24, X/Z velocity26/28, fractions2C/2D/2E,
update selector2F, Y velocity30/acceleration32, remaining38, fade3A, alpha3F,
flags44 and completion selector48. The local declaration becomes a void
one-pointer function. Existing callback-table declarations and shared headers
are unchanged; explicit pointer casts preserve their established guest ABI.

## Source and normalization evidence

The first complete source already had 195 words and frame 32. Inverting the
second lifetime condition into retail's fallthrough shape reduced 133 word
differences to 84. A natural sequential packed-coordinate form reduced them
to 38 and preserved the original animation/control tail directly. Discarded
source screens and reports remain private and receive no extra credit.

The normalized routine retains every raw instruction origin exactly once.
There are no inserted/omitted words, opcode substitutions or relocation
retargets. The motion block's independent load schedule and temporary-register
roles are normalized; all named relocations stay identical. A symbolic
bitvector/dependency model proves equal seven-store expressions/order,
retained speed/pointer/flag/SP/RA/HI/LO, and tick reads after public store
counts 1/3/5. No record-field store overlaps another field's moved load.

The compiler saves the private completion byte at SP+`0x1F`; retail uses
SP+`0x1B`. Two expected-word guards relocate its store/reload. The store
dominates the reload on the dispatched callback path, and both skip paths
bypass the reload. Both homes lie outside the outgoing argument area and
saved RA; incoming argument home SP+`0x20` remains unchanged. The source
introduces no frame scaffolding or fake fields for this private slot.

## Qualification and production audit

- The complete owner preserves all **41 neighboring functions**, pools and
  compiler diagnostics. The real three-command Make recipe reproduces the
  entire qualified owner. Shared headers and Make profiles stay fixed.
- Raw, padded and retail guest streams each pass **3,477 cases**, plus
  **36 independent rebase runs**. They cover signed widths, low-bit arithmetic,
  timer/fade equality, all frame-count and signed-selector bytes, null update
  callbacks, sticky completion, metadata aliases, live ticks and both incoming
  argument-home retargets. Extended selectors are explicitly mapped guest
  fixtures, not ordinary portable C array bounds.
- Five words remain unexecuted: 122/128/158/164 are DIV break 7/6 traps, and 175
  is a duplicated unreachable completion setter. The byte-derived bound is
  never zero; signed 16-bit phase and its negation cannot reach INT_MIN. The lower
  zero-frame bounce case exercises the otherwise missed overflow-check branch.
- Native SDK32 O0/O2/O3 each pass **2,710 cases**, strict aliasing and UBSan,
  with all 19 field offsets, full partial records, opaque bytes, metadata,
  callback tables, ordered observations and canaries. Byte aliases use
  explicit little-endian native fixtures. Native selectors are update
  `-1`/`0..21`, completion `-1`/`0..10`, established by adjacent ELF symbols.
  Incoming-home redirection remains guest-only.
- **24 effective source controls** detect timer/fade errors, missing update
  callbacks, lost sticky completion, stale ticks, wrong acceleration/velocity/
  fraction math, late frame capture, wrong periods/flags, modulo shortcuts,
  wrong completion sentinel, cleanup ordering/omission and stopped resuscitated
  motion. Provider internals remain bounded contracts.
- The actual three descriptor registrations at columns **5,59,66**, offset0,
  contain the target in baseline/private/production data. Their ROM pointers
  are `23006C`, `230B64`, `230CD0`. The full original/current/private **74-word
  func_151670C0** update dispatcher executes **324 cases per stream** with the
  complete target connected. Two controls reject missing registrations and
  missing node arguments. Saved next survives contracted cleanup and record
  retargets. Other registered functions are absent from this bounded fixture.
- **229 normalized/retail access-prefix pairs** compare complete memory,
  GPR/FPR, trace, calls, observations and HI/LO. **48 raw/padded/retail public
  store-boundary triples** compare every public store state and call trace.
  Raw load order and private byte placement differ; raw full access/GPR/private
  fault identity is not claimed. FCSR, timing, asynchronous effects and faults
  inside helpers are outside the model.
- Both isolated production padders and **12 GNU links** across four HI16
  carry boundaries match. Six malformed expected-word/binding controls are
  rejected; two wrong replacement controls fail exact output comparison.
- The **entire production ELF** equals an independent prediction with
  **553 changed bytes and zero exclusions**: the 780-byte target and symbol size
  12->780. No symbol/string permutation is needed. All **189,088 protected
  Game data bytes across 720 owners**, all other loaded bytes, addresses,
  extents, conversion rows and the full previous guard-byte prefix stay fixed.
- Six gates run fresh in each tools configuration before installation. Each
  installed run freshly recompiles/replays Make/relinks/compares the full ELF,
  and reuses five semantic gates only after exact artifact, native binary,
  source/binding, import and data fingerprints agree. Those five checks are
  explicit reuses. `make tools-check` passes. The real sibling's HEAD, dirty
  state and 353 dependency hashes stay intact; paired tests use a disposable
  overlay and its own Make padder.

Raw target SHA256:
`769368be309fa38aef2884b9af49ee8e64b4833a69f446ca609dc09385cbd4c2`.
Qualified complete owner SHA256:
`efbc564a71b08ac0d92b1f80166c4690f6d5ba475699371aa47873d614c9ad07`.
Production ELF SHA256:
`c91b7191ff3b1a8eccd3ea6ed21c20396c8dc5022446eb4e741cf91701d95a91`.

```sh
python3 -m unittest tools.tests.test_game_compact_sprite_update_15167e0c_match -v
```

Artifacts: `conker/build/game-compact-sprite-update-15167e0c-private/`.
The packet requires frozen inputs and fails closed on changed fingerprints.
Codex owns implementation/validation; Claude calls attempted/completed: 0/0.
Host applicability is read-only, with no direct C import proposed for the
available binary-based scene configuration. No host/Release changes, push,
hardware or gameplay acceptance. Continue remaining Game functions.

Graph maintenance: the native update exited 1 with all
71,438 prior IDs retained. The subsequent serial scoped extraction
covers 9 C/Python files with no missing AST sources, producing
71,517 nodes / 172,799 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
