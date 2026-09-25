# Heist cigar smoke restoration - 2026-09-17

Nine original US ROM routines (4,672 bytes) now replace incomplete reconstructions/placeholders in `conker/src/game/generated_204660.c` using `GLOBAL_ASM` sources under `conker/asm/nonmatchings/generated_204660/`.

| Routine | Original bytes |
| --- | ---: |
| `func_151D7264` | 324 |
| `func_151D75C4` | 352 |
| `func_151D77C8` | 104 |
| `func_151D7830` | 252 |
| `func_151D792C` | 268 |
| `func_151D7A38` | 664 |
| `func_151D80C4` | 1,620 |
| `func_151D8718` | 76 |
| `func_151D7CD0` | 1,012 |

The effect needs both its attachment/emission/draw routines and the manager's indirect modifier `func_151D7CD0`. The modifier is selector 4 in table `0x8008A284`; a zero return retires the trail before it becomes visible. Descriptor flags `0x76` select class 77, separate from class-35 attachment ownership.

`make replace NON_MATCHING=1 -j4` in `conker` and `make NON_MATCHING=1 -j4` at the repository root both return 0. All nine bodies in the linked ELF and packaged ROM match the original extracted bytes, including size and SHA-256. Evidence is `../64CBFDOGL/.codex/heist-don-smoke-20260917/guest-byte-audit.json` and `guest-build-result.json`. The original `baserom.us.z64` is unchanged.

The sibling PC implementation uses selective recompilation of those original routines rather than copying a host ABI into this guest repository. Thirty-three executable smoke checks and nine bubble checks pass. Normal RelWithDebInfo visibly produces rising cigar smoke during the natural Heist loss ending, clears effects on return, and passes repeat movement/Restart/Quit/exit. This is native runtime acceptance plus guest byte/build validation, not an independently played whole-game guest-ROM acceptance claim.

See `../64CBFDOGL/DOCS/WORKING_NOTES/628-heist-cigar-smoke-restored-and-live-lifecycle-qualified-20260917.md` for the incomplete eight-routine candidate, corrected observer, recording caveats, full-suite known failures and final integrity checks. Release, real saves and the original ROM remain preserved. Full multiplayer and exact audiovisual parity remain open.
