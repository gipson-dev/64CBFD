# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Decompilation snapshot as of 2026-07-14 (functions converted from raw
assembly to C; byte-matching passes on converted functions are tracked
separately in [Working notes](WORKING_NOTES.md)):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.77% | 1553 / 7644 (20.32%) |
| init | `[#####-------------------]` 20.16% | 232 / 547 (42.41%) |
| game | `[#-----------------------]` 5.11% | 1151 / 6915 (16.64%) |
| debugger | `[#################-------]` 70.26% | 170 / 182 (93.41%) |

Regenerate with `make -C conker progress NON_MATCHING=1` and update both
this table and the one in [Project overview](PROJECT.md).

## Reading order

1. [Project overview](PROJECT.md) - what this repo is, how it is laid out, and how to build it.
2. [Code sub-project](CODE_SUBPROJECT.md) - how the `conker/` code build fits into the full ROM build.
3. [Compressed config sections](CONFIG.md) - how the `config/` YAML files are used for compressed ROM chunks.
4. [IDO 5.3 recomp toolchain](IDO_RECOMP.md) - where the bundled compiler files come from.
5. [Asset formats](ASSET_FORMATS.md) - compression, archive containers, and model/texture/sound payloads.
6. [Working notes](WORKING_NOTES.md) - live log of in-progress work, kept so a crashed session can be resumed.
7. [PC port roadmap](PC_PORT_ROADMAP.md) - phased plan for a keyboard/mouse/controller PC port and a later modern-graphics update.
8. [Update log](UPDATE_LOG.md) - repository documentation, workflow, and maintenance changes.

## Quick notes

- You need your own legally obtained ROM. This repository does not include one.
- Build and extraction commands are expected to run from Linux, WSL, or Docker.
- The `tools/` directories are submodules and keep their own upstream documentation.
