# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for Nintendo 64.
The project reconstructs the original game code and data in a form that can be
built, studied, and matched against the retail ROM.

> [!IMPORTANT]
> This repository does not contain game assets or ROM files. You must provide
> your own legally obtained copy of the game.

Current measurements, verified build state, and the active resume boundary are
maintained in [Current Decomp Status](DOCS/CURRENT_STATUS.md). PC-port progress
and cross-project boundaries are maintained separately in the
[PC Port Roadmap](DOCS/PC_PORT_ROADMAP.md).

## Status

Snapshot verified on 2026-09-28. "Converted" means a function has C source;
"byte-exact" means its linked instructions match the retail game. See
[Current Decomp Status](DOCS/CURRENT_STATUS.md) for the detailed handoff.

| Section | Converted functions | Converted bytes |
| --- | ---: | ---: |
| Total | 5,466 / 6,041 (90.48%) | 85.58% |
| Init | 495 / 538 (92.01%) | 90.48% |
| Game | 4,790 / 5,321 (90.02%) | 85.06% |
| Debugger | 181 / 182 (99.45%) | 99.19% |

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | `[#############-----------]` 2,878 / 5,466 (52.65%) | 1 | 2,587 |
| Init | `[###################-----]` 393 / 495 (79.39%) | 1 | 101 |
| Game | `[############------------]` 2,304 / 4,790 (48.10%) | 0 | 2,486 |
| Debugger | `[########################]` 181 / 181 (100.00%) | 0 | 0 |

The latest Game recoveries replace `func_151E89A0`, `func_151E966C`, and
`func_151E9D18`'s zero-return placeholders with semantic HUD/status renderers.
`func_151E89A0` remains non-matching at 803 real word differences.
`func_151E966C` and `func_151E9D18` are now byte-exact across all 427 and 273
words. Their recovered SDK graphics macros emit the full semantic routines;
relocation-aware guards normalize 116 persistent stack/register scheduling
words in the former and two independent scheduling words in the latter. See
[Working Notes 364](DOCS/WORKING_NOTES/364-game-hud-status-renderer-reconstruction-20260928.md),
[365](DOCS/WORKING_NOTES/365-game-player-status-row-renderer-reconstruction-20260928.md),
[366](DOCS/WORKING_NOTES/366-game-team-counter-panel-reconstruction-20260928.md),
[367](DOCS/WORKING_NOTES/367-game-team-counter-panel-byte-match-20260928.md),
and [368](DOCS/WORKING_NOTES/368-game-player-status-row-renderer-byte-match-20260928.md).

The Init entrypoint `func_10001000` is restored to its original handwritten
clear-and-jump assembly instead of the false zero-return C placeholder. Its
complete 20-word slot is byte-exact; see
[Working Note 369](DOCS/WORKING_NOTES/369-init-handwritten-entrypoint-restoration-20260928.md).
The handwritten CP0/TLB routine `osMapTLBRdb` is likewise restored from its
empty C placeholder and matches all 24 words; see
[Working Note 370](DOCS/WORKING_NOTES/370-init-handwritten-maptlbrdb-restoration-20260928.md).
The compiler-generated Init routine `__osSetHWIntrRoutine` now matches all 20
words using its recovered libultra body and retail `-O1` profile; see
[Working Note 371](DOCS/WORKING_NOTES/371-init-hardware-interrupt-routine-match-20260928.md).
The 25-word Init channel-parameter updater `func_1000CBF0` is also byte-exact
after recovering its 32-bit argument types and original repeated table-access
shape; see
[Working Note 372](DOCS/WORKING_NOTES/372-init-channel-parameter-updater-match-20260928.md).
The 28-word Game display-list address relocator `func_15004CE0` is now
byte-exact after recovering its signed command opcodes, indexed command
cursor, and retail double-read of the opening opcode. Ten expected-word
guards normalize compiler register allocation and one commutative operand
order; see
[Working Note 373](DOCS/WORKING_NOTES/373-game-display-list-address-relocator-match-20260928.md).
The 28-word Game object-state filter `func_15033F70` is also byte-exact after
recovering its global disable gate, attached-object type exclusions, and
state-byte clear. The complete function emits directly from C with no guards;
see
[Working Note 374](DOCS/WORKING_NOTES/374-game-object-state-filter-match-20260928.md).
The 27-word Game record-value adjuster `func_15034EB4` is now byte-exact after
recovering its signed global scale, owner multiplier, and optional second-record
update. Twenty-six words emit directly from semantic C; one expected-word
guard preserves retail's commutative floating-multiply operand order. See
[Working Note 375](DOCS/WORKING_NOTES/375-game-record-value-adjuster-match-20260928.md).
The 27-word Game sequence-state advance `func_1507F454` is now byte-exact after
recovering its current-player state lookup, sequence cursor increment, and
zero-terminator reset. Six relocation-aware guards normalize one closed
compiler register-allocation cycle; see
[Working Note 376](DOCS/WORKING_NOTES/376-game-sequence-state-advance-match-20260928.md).
The 27-word Game active-record counter `func_1509CB68` is now byte-exact after
recovering its four-record unrolled scan across all 204 table entries. The
slice uses its retail no-unroll compiler profile; four relocation-aware guards
normalize only the independent opening-address and count-initialization
schedule. See
[Working Note 377](DOCS/WORKING_NOTES/377-game-active-record-counter-match-20260928.md).
The 26-word Game record-output accessor `func_150A3330` is now byte-exact
after recovering its `0x34`-byte record indexing and four output stores. The
complete routine emits directly from C with no guards; see
[Working Note 378](DOCS/WORKING_NOTES/378-game-record-output-accessor-match-20260928.md).
The 31-word Game actor-position query `func_150E36BC` is now byte-exact after
recovering its one-based slot validation, actor-type gate, and three truncated
coordinate outputs. It also emits directly from C with no guards; see
[Working Note 379](DOCS/WORKING_NOTES/379-game-actor-position-query-match-20260928.md).
The 26-word Game dual event-byte dispatcher `func_150F9720` is now byte-exact
after recovering its two-byte pair lookup and repeated command-`0x42` event
submissions; see
[Working Note 380](DOCS/WORKING_NOTES/380-game-dual-event-byte-dispatch-match-20260928.md).

## Build overview

Docker is the easiest supported environment. Native Linux and WSL also work;
native Windows without WSL or Docker is not supported by the matching IDO
toolchain.

1. Clone the repository with its submodules.
2. Place a big-endian US ROM at the repository root as `baserom.us.z64`.
3. Verify and extract the ROM.
4. Build the `conker/` code project.
5. Replace the rebuilt code sections and rebuild the ROM.

```sh
git clone --recursive <repository-url>
cd 64CBFD

make check
make extract
make -C conker extract
make -C conker --jobs
make -C conker replace NON_MATCHING=1
make --jobs
```

Validate the repository-local MIPS object wrappers independently with
`make tools-check`; this does not require a ROM. See
[project tools](DOCS/TOOLS.md) for usage and compatibility notes.

An unmatched development build may end with `build/conker.us.z64: FAILED`.
That means the rebuilt ROM differs from retail; it does not necessarily mean
the compiler or extraction setup is broken. Follow the
[complete build instructions](DOCS/PROJECT.md#normal-build-steps) for version,
ROM byte order, Docker, WSL, and troubleshooting details.

## Contributing

The most useful current work is byte matching game functions, finishing the
small raw-assembly remainder, documenting asset formats, and improving build
tools.

For function work, start with the
[contributor and byte-matching guide](DOCS/CONTRIBUTING.md). It covers the
normal edit/build/measure loop, retail-span constraints, generated slices,
compiler-sensitive patterns, and the checks expected before a change is
published.

## Documentation

Documentation is organized by purpose in the [documentation index](DOCS/README.md):

- **Current status:** [Decomp status](DOCS/CURRENT_STATUS.md) and
  [PC port roadmap](DOCS/PC_PORT_ROADMAP.md)
- **Start and build:** [Project overview](DOCS/PROJECT.md) and
  [code sub-project](DOCS/CODE_SUBPROJECT.md)
- **Contribute:** [Contributor and byte-matching guide](DOCS/CONTRIBUTING.md)
- **Formats and tooling:** [Asset formats](DOCS/ASSET_FORMATS.md),
  [compressed config sections](DOCS/CONFIG.md), and
  [IDO toolchain](DOCS/IDO_RECOMP.md)
- **History:** [Update log](DOCS/UPDATE_LOG.md) and
  [working notes](DOCS/WORKING_NOTES.md)
