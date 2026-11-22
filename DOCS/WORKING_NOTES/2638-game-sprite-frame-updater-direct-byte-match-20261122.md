# 2638 - Sprite frame updater direct byte match

Date: 2026-11-22. The full 85% matching goal remains active.

`func_15168870` in `conker/src/game_1944C0.c` replaces its false zero-return
placeholder with the complete sprite phase updater. All **111 C words** and
named relocations match all **111 retail body/slot words directly**, with
**frame 24**, **zero guards**, no insertion, omission or trailing padding.
Original: `conker/asm/nonmatchings/game_1944C0/func_15168870.s`.
VA `15168870..15168A2C`; ROM `195D20..195EDC`; 444 bytes.

Production: **4,620 / 5,528 (83.57%) total**, **3,947 / 4,855 (81.30%) Game**,
zero address drift, **908 different**, **79 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Conversion rows and the guard CSV are unchanged.

## Source, record view and callback ABI

The local unspecified-argument s32 placeholder declaration becomes a void
function receiving one `SpriteFrameState *`. This is the measured one-pointer,
void-return guest register ABI of the descriptor's update callback. Shared
headers and other declarations are unchanged. `SpriteFrameState` is a local
184-byte partial view: `phase` at `0x98` and `speed` at `0x9A` are signed 16-bit fields;
`flags` at `0xA8` is unsigned 16-bit, `textureIndex` at `0xB0` unsigned 8-bit,
and `callbackIndex` at `0xB2` signed 8-bit. Unrecovered regions stay
opaque. The SDK cleanup receives an explicit `struct102 *` cast. This records
the observed view and guest ABI, not a recovered original type name.

For nonzero speed, the routine captures the texture metadata frame-count byte
before writing phase, adds speed*tickScale using explicit unsigned 32-bit low-bit
arithmetic, and stores/reloads signed 16-bit phase. The bound is `(frames<<8)-1`.
Reflection flag `0x40` uses signed remainder and negates speed; terminal flag `0x4`
writes `phase = -1`. Ordinary wrapping repeatedly subtracts/adds the bound with a
signed 16-bit store/reload every iteration. Replacing those loops with a generic
modulo changes large-period and signed-boundary behavior. Zero speed skips
arithmetic but still reaches the callback/cleanup path.

Callback selector `-1` skips dispatch; a null table slot also skips it. Otherwise
the one-record callback executes. The final phase is read after the callback,
and a value of `-1` calls `func_1516972C`. Callback mutations can trigger or prevent
cleanup. The texture frame-count capture order matters when metadata aliases
the phase/speed bytes. The selected source retains that order explicitly.

Initial source screening exposed a late frame-count capture and an extra
pointer warning. Capturing a temporary `frames` before the phase store emits
the exact 111-word routine. Signed and unsigned tick-expression variants emit
the same words; the selected unsigned form avoids signed multiply/add overflow.

## Qualification and scope

- The complete owner preserves all 41 other raw/padded functions, constant
  pools and compiler diagnostics. The actual three-command Make recipe
  reproduces the entire qualified owner. The production build does not touch
  the guard CSV and uses ordinary source dependencies.
- Raw, padded and retail guest streams each pass 2,658 cases, plus 36 rebase
  runs. They cover signed phase/speed boundaries, zero/large/negative tick
  words, all frame-count/texture/selector bytes, bounce/terminate/wrap modes,
  null/absent callbacks, aliases and bounded provider mutations. The private
  fixture originally overlapped metadata with the simulated stack; moving
  metadata to a distinct checked region corrected that fixture. All receipts
  use the corrected region. Extended table indices are mapped guest extensions.
- Six retail words are unexecuted: 34, 40, 69, 75 are compiler DIV break 7/6 traps;
  44 and 79 are duplicate unreachable ANDIs. Byte-derived bounds are never zero,
  and signed 16-bit numerators cannot reach INT_MIN, so divide faults are not
  invented as ordinary portable domains. Frame count 0 gives bound `-1`; a wrap
  path can take 32,768 signed 16-bit steps. The bounded interpreter accommodates it.
- Native SDK32 at O0/O2/O3 each passes 1,942 cases with strict aliasing and
  UBSan. Typed record layout, full record/metadata/callback state, provider
  observations, and canaries pass. Numeric-byte aliases use explicitly
  little-endian native fixtures, while guest fixtures use big-endian words.
  Native selectors are `-1` or `0..21`; textures `0..69`, supported by the adjacent
  linker symbols. Incoming-home mutation and extended indices stay guest-only.
- Fifteen effective native source controls reject positive-speed-only logic,
  wrong metadata byte/tick/sign/period/flags, missing speed reflection,
  modulo shortcuts, late frame capture, omitted/wrong callback, early cleanup
  decisions and wrong cleanup sentinel.
- The complete original/current/private-image 74-word `func_151670C0` dispatcher
  passes 2,304 cases per stream with the 111-word callback connected. Actual
  descriptor column 14, offset 0 at `8008B780` contains `15168870`; ROM `230240` is its
  sole aligned pointer literal. Full aligned ROM census finds no direct JAL
  or direct-J. Two controls reject missing registration and node argument.
  The parent's captured next pointer survives contracted cleanup clearing
  the current node's next field. Its saved ABI and both rows agree.
- Across eight cases, 103 access-fault triples compare complete memory,
  ordered trace, calls, observations, GPR/FPR and HI/LO state. These are emitted
  guest boundaries; FCSR, timing, asynchronous writes and provider-internal
  faults are not modeled. Callback/cleanup internals remain bounded contracts.
- Both isolated padders and 12 GNU links across four carry boundaries match.
  Four altered-word/relocation controls fail exact comparison. With no target
  guards, guard rejection is not claimed for those controls.
- The entire production ELF equals an independent literal prediction with
  **359 changed bytes, zero exclusions**: 444 retail target bytes, symbol size
  12->444, and a bounded symbol/string swap of `func_150CBCE0` and `D_800E0E2C`.
  The established permutation helper verifies preimages, contiguous strings
  and unchanged canonical named definitions. The initial 41 unpredicted bytes
  are fully accounted for. Loaded code/data outside the target and all 189,088
  protected GameData bytes across 720 owners remain fixed.
- Six focused gates run fresh in each tools configuration before adoption.
  After installation each configuration reruns the source/Make/full-image
  gate and reuses five semantic gates only after exact artifact, dependency,
  data, source and binding fingerprints agree. The reused native binaries
  and source are hashed too. These five gates are explicitly reused, not
  reported as fresh installed executions. `make tools-check` passes.
- The real sibling's HEAD/dirty work and dependency hashes are preserved;
  paired tests use a disposable overlay that runs its own Make padder.

Raw target SHA256:
`4b750550766c8a0122f148357e24ce5fa17dc8331d5e205d50e6c78064753498`.
Qualified complete owner SHA256:
`4f68f0fbd40337d17a90c0d0190121fffecf36bf157489aa037fd286e45f13a2`.
Production ELF SHA256:
`72c26384fe1ea2ba99709dd5dbf157b8099ccd9cfd56224312b4d7c5aa7dcb90`.

```sh
python3 -m unittest tools.tests.test_game_sprite_frame_update_15168870_match -v
```

The focused packet requires frozen consumer inputs and fails closed on
changed fingerprints. Artifacts:
`conker/build/game-sprite-frame-update-15168870-private/`.
Codex owns implementation/validation; Claude calls attempted/completed: 0/0.
Local original/compiler, independent model, native SDK and full caller evidence
resolve this routine. Host applicability is read-only; no host/Release changes,
push, hardware or gameplay acceptance is claimed. Continue remaining Game work.

Graph maintenance: the native update exited 1 with all
71,293 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
71,355 nodes / 171,512 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
The native scan protected the larger existing graph from a smaller corpus; the scoped merge supplies this update.
