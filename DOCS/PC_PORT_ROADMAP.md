# PC Port Roadmap

This is a forward-looking plan, not a status report. As of this writing the
repository is a ROM decompilation project only: there is no PC build target,
no windowing/input code, and no renderer outside the original N64 RCP
pipeline. Nothing described below has been started unless a step is marked
`[done]`.

The phases are ordered by dependency, not by date. There are no target dates
here on purpose - decomp projects like this progress in bursts tied to
contributor time, not calendar time. For live decomp completion numbers, run
`make -C conker progress` or see [PROJECT.md](PROJECT.md#current-progress).
For what's actively being worked on right now, see
[WORKING_NOTES.md](WORKING_NOTES.md).

## Guiding decision: hand-port vs. static recompilation

Before Phase 1 tooling work starts, pick one approach:

- **Hand-port** - rewrite the decompiled C against a new PC-native runtime
  (SDL2/GLFW + OpenGL/Vulkan), function by function, discarding libultra.
  This is the traditional path older N64 PC ports used. It only works well
  for code that has already been decompiled and matched, so it's gated by
  decomp progress (currently 9.60% total, see PROJECT.md).
- **Static recompilation** - run a MIPS-to-C recompiler (the approach used by
  projects such as N64Recomp/Zelda64Recomp and the sm64 static-recomp forks)
  over the ROM's compiled code, then pair the recompiled output with
  hand-written high-level implementations of the RSP graphics/audio
  microcode and the libultra OS layer. This does **not** require the
  underlying code to be decompiled first, so it can start earlier, at the
  cost of the recompiled portions staying opaque MIPS-shaped C rather than
  readable source.

These aren't mutually exclusive: a common pattern is to statically recompile
everything, then progressively replace recompiled functions with the
hand-decompiled equivalents as decomp coverage grows. Record the decision
made (and why) in [WORKING_NOTES.md](WORKING_NOTES.md) once it's made, and
update this file's Phase 1 accordingly.

## Phase 0 - Prerequisites (current work)

This is the decompilation project as it exists today. It isn't blocking to
*start* Phase 1 under the static-recompilation path, but the following make
every later phase cheaper and safer:

- [ ] Continue matching `init`/`game`/`debugger` sections (`make -C conker progress`).
- [ ] Finish mapping the ROM layout (see the layout notes in [PROJECT.md](PROJECT.md#rom-layout-notes)).
- [ ] Document the RSP microcode(s) in use (F3DEX-family display lists,
      `libultra`'s `gbi.h`/`gs2dex.h` already in `conker/include/2.0L/PR/`)
      well enough to know which graphics commands a renderer needs to support.
- [ ] Document the audio microcode/sequence format (`n_libaudio.h`,
      `libaudio.h`) well enough to know what an audio backend needs to emulate.
- [ ] Locate and document controller/PIF input handling (how the game reads
      `OS_INPUT`/`osContGetReadData` and maps buttons/stick to game actions) -
      this is the hook point for keyboard/mouse/controller remapping in Phase 4.
- [ ] Finish the asset format work in [ASSET_FORMATS.md](ASSET_FORMATS.md) -
      the model/texture/audio containers are what a PC renderer and audio
      backend will need to load directly (or convert once, offline).

## Phase 1 - Toolchain and build target

- [ ] Decide hand-port vs. static recompilation (see above) and record the decision.
- [ ] If static recompilation: evaluate N64Recomp (or an equivalent) against
      this ROM's compiler (IDO 5.3) and RCP configuration; produce a first
      recompiled build that at least links.
- [ ] Stand up a separate PC build target (new top-level directory or
      sibling repo, e.g. `pc/` or `conker-pc/`) with its own CMake/Makefile,
      independent of the ROM-matching build in `conker/`.
- [ ] Pick the windowing/input library (SDL2 or GLFW) and the graphics
      backend abstraction (raw OpenGL, or a cross-API layer if targeting
      Vulkan/D3D12 later).
- [ ] Get a minimal "hello triangle" window running from the PC build target
      as a smoke test, unrelated to game code.

## Phase 2 - OS/runtime shim

Replace what the game currently gets from libultra with PC equivalents,
using the headers already extracted in `conker/include/2.0L/PR/` (`os.h`,
`os_cont.h`, `os_ai.h`, `abi.h`, etc.) as the contract to satisfy:

- [ ] Threading/scheduler shim (`os_internal.h`, viManager/scheduler
      equivalents) - N64 games assume cooperative multi-threading; decide how
      that maps onto a PC main loop.
- [ ] DMA/memory shim - N64 code issues `osPiStartDma`-style calls against a
      cartridge ROM layout; on PC this becomes direct reads from extracted
      assets (see [ASSET_FORMATS.md](ASSET_FORMATS.md)).
- [ ] VI/framebuffer timing shim - replace `os_ai.h`/VI retrace assumptions
      with a PC frame loop (this is also where an uncapped framerate option
      becomes possible - track separately, see Phase 8).
- [ ] Save data shim - EEPROM/`os_eeprom.h`/flash-pak (`os_flash.h`) access
      replaced with plain files on disk.

## Phase 3 - Graphics pipeline

- [ ] Implement an RSP/RDP display-list interpreter (F3DEX2-family commands
      from `gbi.h`/`gs2dex.h`) that walks the game's existing display lists
      and issues modern draw calls - this is the single largest chunk of new
      code in the whole roadmap.
- [ ] Render at the original internal resolution and aspect ratio first;
      resolution/aspect changes are a Phase 8 concern.
- [ ] Get textures loading directly from the documented RGBA5551 asset
      containers (assets00-05 per [ASSET_FORMATS.md](ASSET_FORMATS.md)).

## Phase 4 - Input: keyboard, mouse, controller

The original game only understands an N64 controller read through the PIF
(`os_cont.h`). None of the following exists yet:

- [ ] Map SDL2/GLFW gamepad input to the game's existing controller-read
      call sites identified in Phase 0, so a modern controller (Xbox/PS/etc.)
      works as a drop-in replacement first.
- [ ] Add a keyboard+mouse control scheme as a second input profile (e.g.
      WASD + mouse-look), since the original game has no such input model to
      fall back on - this needs new control-mapping code, not just a shim.
- [ ] Add a rebindable input config (file or in-game menu) rather than
      hardcoding one scheme.
- [ ] Controller rumble/vibration mapping, if the target APIs support it.

## Phase 5 - Audio

- [ ] Reimplement or port the sequence/sample playback currently done by the
      audio RSP microcode (`n_libaudio.h`) against a PC audio backend
      (e.g. SDL2 audio, miniaudio).
- [ ] Load audio directly from the documented MP3 streams (assets16) and the
      `"B1"` sample-bank format (assets17) per [ASSET_FORMATS.md](ASSET_FORMATS.md).

## Phase 6 - First playable milestone

This is the "playable in a keyboard/mouse/controller sense" target the rest
of the roadmap builds toward:

- [ ] Boots to the title screen without a ROM loaded through an emulator.
- [ ] Loads at least the first playable level.
- [ ] Keyboard+mouse and controller input both functional per Phase 4.
- [ ] Save/load functional per the Phase 2 save shim.
- [ ] Runs at a stable frame rate matching the original timing.

## Phase 7 - Stabilization

- [ ] Triage and fix crashes/undefined behavior surfaced by recompiled or
      hand-ported code that never had to run outside an emulator's
      forgiving environment.
- [ ] Add a settings menu (video, audio, controls) instead of config files only.
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
