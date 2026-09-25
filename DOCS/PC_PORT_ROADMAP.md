# PC Port Roadmap located in another project folder

## Cross-project progress - 2026-09-25

The active Windows port remains in sibling `64CBFDOGL`; this repository owns
the guest decompilation and retail-byte evidence used by that port. The current
measured decomp checkpoint is:

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,493 / 6,038 (90.97%) | 2,545 / 5,493 (46.33%) | 1 | 2,947 |
| Init | 508 / 538 (94.42%) | 387 / 508 (76.18%) | 1 | 120 |
| Game | 4,804 / 5,318 (90.33%) | 1,977 / 4,804 (41.15%) | 0 | 2,827 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Debugger is fully accounted for across all 182 rows. The table keeps the raw
conversion distinction because `func_16003650` is original handwritten
CP0/TLB assembly, but a direct linked-ELF comparison confirms that all 40 of
its words match retail. There is no remaining debugger conversion or matching
work.

The current debugger restoration batch is banked in focused commits.
`func_16001390`, `func_16000F8C`, `func_160014F0`, `func_16001BB4`,
`func_16000590`, `func_16001044`, `func_1600078C`, and `func_16000B14` are
byte-exact in the linked ELF. Debugger matching is complete at 181 / 181. The
game routine `func_15135480` and former one-difference rows `func_150AF2E0`,
`func_151061EC`, `func_15144A74`, and `func_151ACB60` are also byte-exact. See
[Current Decomp Status](CURRENT_STATUS.md) and
[Working Note 012](WORKING_NOTES/012-generated-near-match-normalization-20260925.md).
The complete debugger accounting is recorded in
[Working Note 013](WORKING_NOTES/013-debugger-completion-audit-20260925.md).
The latest game triage restored a shared epilogue and handwritten syscall to
assembly ownership; see
[Working Note 014](WORKING_NOTES/014-small-game-assembly-boundaries-20260925.md).
The next focused game pass completed the two record setters
`func_15087FC4` and `func_15087FEC`; see
[Working Note 015](WORKING_NOTES/015-game-record-pointer-byte-matches-20260925.md).
The following focused pass completed `func_1519C910`; see
[Working Note 016](WORKING_NOTES/016-game-identifier-check-byte-match-20260925.md).
The next focused pass completed `func_1517F448`; see
[Working Note 017](WORKING_NOTES/017-game-indexed-counter-byte-match-20260925.md).
The following focused pass completed `func_15079F6C`; see
[Working Note 018](WORKING_NOTES/018-game-packed-field-writer-byte-match-20260925.md).
The final two-difference pass completed `func_1516968C` and `func_151696DC`;
see [Working Note 019](WORKING_NOTES/019-final-two-difference-game-matches-20260925.md).
The next triage restored the original sine/cosine assembly slice beginning at
`func_150AD780`; see
[Working Note 020](WORKING_NOTES/020-game-trigonometry-assembly-restoration-20260925.md).
The following source-level pass completed `func_150849A0`; see
[Working Note 021](WORKING_NOTES/021-game-indexed-byte-lookup-match-20260925.md).
The next guarded register-lifetime pass completed `func_150636A4`; see
[Working Note 022](WORKING_NOTES/022-game-nested-pointer-update-match-20260925.md).
The following guarded scheduling pass completed `func_1514672C`; see
[Working Note 023](WORKING_NOTES/023-game-float-bound-load-order-match-20260925.md).
The next source-level pointer-lifetime pass completed `func_15199980`; see
[Working Note 024](WORKING_NOTES/024-game-optional-callback-match-20260925.md).
The final three-difference pass completed `func_1505D024`; see
[Working Note 025](WORKING_NOTES/025-game-call-argument-register-match-20260925.md).
The next source-level pass completed `func_15071A64` by restoring the retail
stack-local layout; see
[Working Note 026](WORKING_NOTES/026-game-stack-local-layout-match-20260925.md).

Current host-port progression and acceptance boundaries:

- Training reaches Windy in normal `RelWithDebInfo`; the retained save reloads
  and the second-level Chapters unlock was user-verified.
- Windy's east-pool collision and swimming path are restored. Authored water,
  current and natural dry-ground exit were verified; this was a host-only
  repair and does not require a guest-decomp transplant. See
  [host Note 744](../../64CBFDOGL/DOCS/WORKING_NOTES/744-windy-water-collision-and-swimming-restored-20260924.md).
- The `FLY` cheat is implemented and should be used for mobility while
  scouting and resuming broad single-player progression. The accepted code is
  exactly `FLY`; this does not waive ordinary-movement checks for final route
  acceptance.
- The user reports the current play position is the Death/Grim Reaper area.
  Treat that as the next manual resume marker, not as complete level or visual
  acceptance until a dated runtime witness is recorded in the host project.
- Disabling right-stick C-button emulation (`controller_c_stick: 0`) was
  confirmed to stop controller/camera drift. It is a temporary configuration
  workaround and must be undone during the future matched camera/input pass.
- Ordinary host work remains `RelWithDebInfo`. The latest authorized Release
  artifact is frozen; do not rebuild or launch Release without a new explicit
  instruction.

These host facts are summarized here for dependency planning. The authoritative
implementation queue remains the sibling's
[current status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and
[active roadmap](../../64CBFDOGL/DOCS/roadmap.md).

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

The plan below is a historical proposal for the ROM-decompilation repository.
The PC implementation now lives in sibling `64CBFDOGL`; use the active host
roadmap linked above for implementation status. Unchecked items below do not
mean the corresponding host feature is absent. This repository continues to
own guest decompilation, original-byte validation and ROM builds.

The phases are ordered by dependency, not by date. There are no target dates
here on purpose - decomp projects like this progress in bursts tied to
contributor time, not calendar time. For live decomp completion numbers, run
`make -C conker progress NON_MATCHING=1` or see
[PROJECT.md](PROJECT.md#current-progress). Published milestones are in the
[update log](UPDATE_LOG.md); temporary recovery details are in
[working notes](WORKING_NOTES.md).

## Guiding decision: hand-port vs. static recompilation

Before Phase 1 tooling work starts, pick one approach:

- **Hand-port** - rewrite the decompiled C against a new PC-native runtime
  (SDL2/GLFW + OpenGL/Vulkan), function by function, discarding libultra.
  This is the traditional path older N64 PC ports used. It only works well
  for code that has already been decompiled and matched, so it's gated by
  decomp progress. The restored-assembly baseline currently measures 85.65%
  by converted bytes and 91.04% by tracked functions; byte-exact C is measured
  separately above and in [PROJECT.md](PROJECT.md#current-progress).
- **Static recompilation** - run a MIPS-to-C recompiler (the approach used by
  projects such as [N64Recomp](https://github.com/N64Recomp/N64Recomp),
  Zelda64Recomp, and the sm64 static-recomp forks) over the ROM's compiled
  code, then connect the output to a PC-native runtime. This does **not**
  require the underlying code to be decompiled first, so it can start earlier,
  at the cost of the recompiled portions staying opaque MIPS-shaped C rather
  than readable source.

These aren't mutually exclusive: a common pattern is to statically recompile
everything, then progressively replace recompiled functions with the
hand-decompiled equivalents as decomp coverage grows. Record the decision
made (and why) in [WORKING_NOTES.md](WORKING_NOTES.md) once it's made, and
update this file's Phase 1 accordingly.

## Phase 0 - Prerequisites (current work)

This is the decompilation project as it exists today. It isn't blocking to
*start* Phase 1 under the static-recompilation path, but the following make
every later phase cheaper and safer:

- [ ] Continue matching the `init` and `game` sections (`make -C conker progress`).
- [x] Complete debugger matching: 181 / 181 converted functions are linked
      byte-exact, including the final 286-word `func_16000B14` main loop.
- [ ] Finish mapping the ROM layout (see the layout notes in [PROJECT.md](PROJECT.md#rom-layout)).
- [x] Document the RSP microcode(s) in use (F3DEX-family display lists,
      `libultra`'s `gbi.h`/`gs2dex.h` already in `conker/include/2.0L/PR/`)
      well enough to know which graphics commands a renderer needs to support.
      The sibling now has a working Conker F3DEXBG interpreter feeding RT64;
      exact command and presentation parity remains ongoing.
- [x] Document the audio microcode/sequence format (`n_libaudio.h`,
      `libaudio.h`) well enough to implement the current native audio backend.
      Complete perceptual and gameplay-audio parity remains open.
- [x] Locate and document controller/PIF input handling (how the game reads
      `OS_INPUT`/`osContGetReadData` and maps buttons/stick to game actions) -
      this now backs keyboard, mouse and SDL controller remapping in Phase 4.
- [ ] Finish the asset format work in [ASSET_FORMATS.md](ASSET_FORMATS.md) -
      the model/texture/audio containers are what a PC renderer and audio
      backend will need to load directly (or convert once, offline).

## Phase 1 - Toolchain and build target

- [x] Decide hand-port vs. static recompilation: the port uses static
      recompilation with selected native overrides and restored original bodies.
- [x] Evaluate N64Recomp and the
      [N64 Modern Runtime](https://github.com/N64Recomp/N64ModernRuntime#ultramodern)
      (`ultramodern` plus `librecomp`) against this ROM's compiler (IDO 5.3),
      libultra usage, and RCP configuration; produce a first recompiled build
      that at least links.
- [x] Stand up the separate `64CBFDOGL` sibling with its own CMake build,
      independent of the ROM-matching build in `conker/`.
- [x] Use SDL2 for windowing/input and RT64 as the graphics backend.
- [x] Complete the initial window/render smoke test. The original triangle
      milestone is superseded by visible title, menu and gameplay rendering.

## Phase 2 - OS/runtime shim

Do not start by rewriting the entire libultra layer. The
[N64 Modern Runtime](https://github.com/N64Recomp/N64ModernRuntime#ultramodern)
is a concrete candidate: `ultramodern` already covers threads, controllers,
audio, message queues, timers, RSP task handling, and VI timing, while
[`librecomp`](https://github.com/N64Recomp/N64ModernRuntime#librecomp) bridges
N64Recomp output and supplies features such as overlays, PI DMA, and save
storage. It still expects the game project to provide platform I/O callbacks
and a graphics renderer. Keep it reference-only until a compatibility spike
proves it can support Conker's Rare-specific code and microcode without
forcing changes into the byte-matching ROM build.

Whether reusing that runtime or filling its gaps locally, use the headers
already extracted in `conker/include/2.0L/PR/` (`os.h`, `os_cont.h`, `os_ai.h`,
`abi.h`, etc.) as the contract to satisfy:

- [ ] Finish the compatibility inventory that maps every libultra call used
      by Conker to `ultramodern`, `librecomp`, or a project-owned missing shim.
- [x] Pin the runtime in the separate PC build and keep
      it out of the ROM-matching `conker/` dependency graph.
- [x] Implement the threading/scheduler and message-queue path needed by the
      current PC main loop. Exact scheduler/audio timing parity remains open.
- [x] Implement PI DMA and recomp memory access against the packaged ROM/data
      image. Direct extracted-asset loading remains a separate future path.
- [x] Implement VI/framebuffer timing sufficiently for current title, menu and
      gameplay execution. Stable retail timing and uncapped operation remain
      separate acceptance items.
- [x] Implement file-backed save storage. Retained saves, reloads and
      multiplayer profile persistence have runtime evidence.

## Phase 3 - Graphics pipeline

- [x] Evaluate [RT64](https://github.com/rt64/rt64), the renderer recommended
      by `ultramodern`, against Conker's actual display lists and Rare-specific
      RSP microcode.
- [x] Integrate RT64 and implement the Conker-specific F3DEXBG/RDP path needed
      to walk current game display lists. Remaining commands and exact visual
      parity continue as scoped restoration work.
- [x] Render through RT64's original-resolution and 4:3 configuration before
      treating higher resolution or widescreen as accepted Phase 8 features.
- [ ] Get textures loading directly from the documented RGBA5551 asset
      containers (assets00-05 per [ASSET_FORMATS.md](ASSET_FORMATS.md)).

## Phase 4 - Input: keyboard, mouse, controller

The original game only understands an N64 controller read through the PIF
(`os_cont.h`). The host input bridge now supplies that contract:

- [x] Map SDL2 gamepad input to the game's existing controller-read
      call sites identified in Phase 0, so a modern controller (Xbox/PS/etc.)
      works as a drop-in replacement first.
- [x] Add keyboard movement and optional relative mouse-look as a second input
      profile. Final camera parity is still open, and the confirmed
      `controller_c_stick: 0` drift workaround is temporary.
- [x] Add rebindable input configuration through JSON and
      `conker_settings.exe`, including four controller-port assignments and
      runtime input reload.
- [x] Map game rumble requests to SDL controller vibration. Physical-device
      rumble acceptance remains open.

## Phase 5 - Audio

- [x] Reimplement the sequence/sample playback path against the SDL/native
      audio backend. Recognizable music, dialogue and effects play; complete
      timing, mix and perceptual parity remain open.
- [ ] Load audio directly from the documented MP3 streams (assets16) and the
      `"B1"` sample-bank format (assets17) per [ASSET_FORMATS.md](ASSET_FORMATS.md).

## Phase 6 - First playable milestone

This is the "playable in a keyboard/mouse/controller sense" target the rest
of the roadmap builds toward:

- [x] Boots to the title screen without running through an emulator.
- [x] Loads and progresses through Training into Windy.
- [x] Keyboard, optional mouse-look and controller paths are implemented and
      have scoped gameplay evidence. Complete device/camera parity remains open.
- [x] Save/load is functional; retained adventure saves and multiplayer
      profiles survive application restart in the tested scopes.
- [ ] Runs at a stable frame rate matching the original timing.

## Phase 7 - Stabilization

- [ ] Triage and fix crashes/undefined behavior surfaced by recompiled or
      hand-ported code that never had to run outside an emulator's
      forgiving environment.
- [ ] Add a settings menu (video, audio, controls) instead of config files only.
      The external `conker_settings.exe` input editor is complete for its
      current scope; Video, Audio and Paths are still placeholders.
- [ ] Windowed/borderless/fullscreen and multi-monitor handling.

## Phase 8 - Modern graphics update (longer-term)

Everything here assumes Phase 6 is done and stable. This is explicitly a
"plan for later," not scoped work yet:

- [ ] Uncapped/variable frame rate option (depends on the Phase 2 VI/timing shim).
- [ ] Internal resolution scaling above the original N64 output resolution.
- [ ] Widescreen/ultrawide aspect ratio support (camera and UI both need
      review - N64-era HUDs are frequently hardcoded to 4:3).
- [ ] Texture filtering options (as an alternative to the original's nearest/
      bilinear look) and, further out, an HD texture-pack pipeline built on
      the asset formats documented in [ASSET_FORMATS.md](ASSET_FORMATS.md).
- [ ] Enhanced lighting/shadows beyond what the original RDP pipeline
      produced, once Phase 3's interpreter is solid enough to extend rather
      than just replicate.
- [ ] Evaluate a modern-API renderer path (Vulkan/D3D12, or an existing
      renderer used by comparable recomp projects) as a stretch goal once
      the OpenGL path from Phase 3 is stable - this is the point where
      ray-traced lighting would become realistic to attempt, not before.

## Keeping this file honest

Check off items only once they're actually true, and update the phase text
if the plan changes - this file will go stale fast otherwise. Day-to-day
"what am I doing right now" belongs in [WORKING_NOTES.md](WORKING_NOTES.md),
not here; this file is the map, that file is the current position on it.
