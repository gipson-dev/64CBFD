# Game Sphere Callee Storage Recovery

Date: 2026-10-07. Baseline: `b0e758cd`,
[Note 1083](1083-game-sphere-wrapper-direct-match-20261007.md).

Continue `func_151452C4`, VA `151452C4..151454BC`, ROM `172774..17296C`.
Recover the original 126-word length and `0x70` frame in experimental C.
The selected body still differs at 60 words and has incorrect private slots.
It is not installed: retain the exact original assembly, direct 53-word
wrapper and 13-word dot helper. No guards or production source changes.

## Compiler Results

[Maintained driver](../../tools/experiments/game_sphere_callee_candidates.py)
screens 64 O2/g3 forms: 32 array-storage/radius/root controls and 32 union-
storage/member-address/root controls. All compile without diagnostics; none
is exact. The array-overlay forms are compiler controls, not qualified C
replacements. The selected union uses the actual three-component direction
snapshot with structure-copy and float-array views.

| Form | Words | Frame | Word Differences |
| --- | --- | --- | --- |
| Historical volatile-perpendicular trial | 128 | `0x68` | 106 |
| Nonvolatile, three ordinary structures | 126 | `0x68` | 80 |
| Separate magnitude/signed root | 126 | `0x70` | 74 |
| Selected three-float direction union | 126 | `0x70` | 60 |
| Selected union, separate signed root | 126 | `0x70` | 61 |
| Direction array, reuse radius parameter | 126 | `0x68` | 82 |

The selected form recovers X/Y/Z in F0/F12/F14 and the perpendicular-square
store/reload at `SP+0x1C`, without a volatile scalar. Note 1083's proposed
volatile requirement is therefore superseded by this measured compiler result;
the historical trial is retained unchanged for its existing tests.
The dot call remains the sole relocation, `R_MIPS_26:func_15144A74` at `0x1C0`.

Seven ignored exploratory screens retain 228 measurements: declaration order,
register/lifetime hints, radius placement, pointer caching, arrays, names,
scalar storage and unions. Their receipts are research evidence; the maintained
64-form driver reproduces only the array and union families, not all 228.
No unused padding locals, synthetic fourth vector component, profile change,
private-offset rewrite or instruction insertion/deletion is installed.

## Measured Private-Slot Blocker

| Local | Retail Frame Offset | Selected Frame Offset |
| --- | --- | --- |
| Copied direction | `0x58` | `0x64` |
| Copied origin | `0x4C` | `0x58` |
| Final relative vector | `0x28` | `0x4C` |

This is an observable difference, not merely a lower word-match score.
With origin zero, unit-X direction, center `(5,0,0)`, radius one, and the first
point output at callee-frame `+0x58`, retail overwrites its copied direction X
with the first root, four. Its second point X becomes `6 * 4 + 0 = 24`.
The selected C overwrites copied origin X instead, producing `6 * 1 + 4 = 10`.
Both stack phases reproduce **retail 24.0 versus trial 10.0**. The subsequent
dot call also receives different relative-vector slots, `+0x28` versus `+0x4C`.

Do not install this trial or normalize its private offsets with word guards.
The test constructs a bounded frame-sensitive alias; it does not claim that
either known game caller naturally creates this alias.

## Qualification

[Seven recovery tests](../../tools/tests/test_game_sphere_callee_recovery.py)
pass in 14.016 seconds, zero skips/errors/failures.

- 1,404 finite cases cover nine centers, six signed/zero radii, thirteen
  external output/input aliases and two stack phases.
- Another 1,404 cases cover nonzero origins, three-axis and non-unit directions,
  three centers, three radii, thirteen aliases and two stack phases.
- Retail and selected C execute the original wrapper and dot helper. Both
  agree with the independent rounded-float reference on complete external
  memory, ordered external writes, wrapper status and forwarded arguments.
  All 126 original callee and 13 dot-helper words execute.
- Two private-slot probes deliberately disagree as described above. No equal
  private memory, identical raw read schedule or private-alias acceptance claim.
- A miss succeeds with all output buffers unmapped, proving lazy output access.
- Compiled stale-origin and stale-direction controls each change the actual
  helper return from one to zero. Compare direct helper results: the wrapper
  would mask these negative-distance failures by also returning zero.
- Six selected/control compilations pin length/frame/differences/relocation;
  production tests bind the retained assembly, wrapper, dot and absent guards.

The focused recovery/wrapper/projection-schedule/owner-pool regression passes
all 40 tests in 160.675 seconds, zero skips/errors/failures. Project-tool smoke
checks, Python syntax and whitespace pass. Documentation gate passes across
66 documents and 3,749 relative links, zero broken. This is a focused run,
not a new full production checkpoint or a rerun of Note 1082's 206-test suite.

No new native geometry, complete-caller, FCSR/exception, NaN payload/arithmetic,
hardware, gameplay or host-adoption qualification is claimed. The existing
native wrapper tests remain boundary-staging evidence, not callee acceptance.

## Baseline Audit

Retained US ELF audit equals Note 1083 across all 6,059 slots and their
addresses/extents. Protected sections, all 720 Game-data owners covering
189,088 bytes and all 10,953 historical guards are unchanged. Zero new guards.
This is an audit of the retained baseline, not a new production installation.

Matching remains total 3,354/5,465 (61.37%), Game 2,681/4,792 (55.95%),
2,111 different, zero drift. Conversion remains 5,465/6,042, Game 4,792/5,321.
README aggregate rows are already correct and untouched; details remain in DOCS.
No sibling/frozen Release/save/runtime or push work.

## Resume

1. Recover retail's meaningful local storage/lifetime shape: direction `+0x58`,
   origin `+0x4C`, relative `+0x28`, while retaining 126 words/frame `0x70`.
2. Preserve the natural perpendicular-square spill/reload and late live origin/
   direction reads. Re-run the private-slot counterexample and broaden helper
   parameter-home/private-copy alias qualification before installation.
3. Only then classify remaining register/independent-schedule differences;
   do not treat all current 60 differences as guardable scheduling words.
4. Qualify copied-owner/pools/relocations/padder and actual caller boundaries,
   then install narrowly, rebuild, run production regressions and audit.

Sampler `func_151432BC` and oriented `func_15142600` remain open.
Ignored receipts: `conker/build/game-sphere-callee/`,
`conker/build/game-sphere-callee-test/`, and `game-sphere-callee-*` exploratory
directories under `conker/build/`.
