# Strip update ordered floating-point recovery and stack frontier - 2026-11-17

The selected private `func_151AD174` draft is now **v82: 491 words / frame
0x308**, against retail's 494 words. Across the complete **544-case finite
matrix**, all **648,522 recorded FP operations** have identical precision,
operation and ordered input bits. Public bytes, provider calls, preserved
registers and coefficient read counts agree. This advances the semantic
recovery; it is **not a byte match or a whole-loop symbolic/FCSR proof**.
The production callback remains its placeholder. No guards or credit are added.

Accepted total remains **4,532 / 5,514 (82.19%)**, Game **3,859 / 4,841
(79.71%)**, Init 492/492 and Debugger 181/181, with zero drift. **155 further
matches** are needed for the active 85% goal. Root README stays unchanged.
The preceding symbolic prefix and allocation milestone is
[Note 2515](2515-game-strip-update-amplitude-lifetime-and-symbolic-prefix-snapshot-relation-20261117.md).

## Target and recovered source order

Owner `conker/src/game/generated_1D92F0.c`, VA 151AD174..151AD92C,
ROM 1DA624..1DADDC, 1,976 retail bytes. The one-pointer void callback is
registered at descriptor+4 for classes 0x2F and 0x4E. The original complete
secondary-list walker remains the caller qualification target.

The source retains the existing countdown, six trig-provider opportunities,
twenty-sample snapshots, gravity/damping/smoothing, reverse spacing constraint
and movement-audio submission. Actual scalar lifetimes and expression staging
recover the missing ordered arithmetic:

- Compute the gravity square before negating gravity, and retain cached
  damping, ceiling and double-precision smoothing coefficients outside the loop.
- Use one guarded do/while reverse loop, preserving the empty-count exit.
- Form all three force products before the three ordered subtractions/stores.
- Use the SDK-style compound double addition for the smoothing contribution.
- Compute later constraint differences in Z/X/Y order and interleave the
  movement absolute values with the three squared differences.
- Separate planar division from gravity multiplication, stage the norm sum,
  and retain a real temporary for each constrained position's final addition.

These use ordinary semantic C values. No volatile hints, padding locals,
compiler-profile changes or forced dummy memory effects are introduced.

The sampled full path previously had 284 FP sequence edits in v43. The measured
progression is v64:152, v75:95, v77:57, v80:19, then v82:0. Both retail and v82
execute 1,671 recorded FP operations in that full-path case. The final broader
matrix comparison includes all existing count, owner, impulse, category, stack
phase, timer, mutable-provider and sound-threshold cases.

## Discriminating checks and rejected fits

Static opcode totals alone hid repeated coefficient reads in v48/v51. Dynamic
observation finds 19 reads of each coefficient in those drafts versus one in
retail. Const declarations in v66 do not fix that: each remains read 19 times.
They are rejected. The selected cached form reads each coefficient once for
each nonempty reverse-loop case and zero times when that loop is empty.

The 491-word force-staging drafts gained **two NOPs**, not the missing spill
store/load pairs. v65 and v67 emit exactly the same raw bytes as v60. Moving
the scalar declaration after a double in v74 grows the frame to 0x310 and is
rejected. Earlier drafts remain in the ignored packet; no word-count-only
candidate is treated as installable.

Two fresh operand-swap controls change raw word266's gravity multiply or
word395's constrained-position addition. Each preserves the sampled public
bytes and calls but fails the ordered-input-bit comparison. These demonstrate
that the new gate checks information absent from the public-result oracle.
They do not establish architectural FP-status behavior.

## Fresh qualification in both tools configurations

All **five focused tests pass fresh** in both the primary checkout and the
task-overlay/sibling configuration, with zero failures, errors or skips:

- Complete-owner compilation: all 32 neighbors, pools and bindings preserved;
  selected 491-word raw body and frame 0x308 pinned by digest.
- 544 cases per retail/raw stream, 648,522 ordered FP operations compared,
  complete declared public RAM/calls and preserved registers; word coverage
  489/494 retail and 486/491 raw.
- The prior strict 142-word opening checker still explores 18 paths and 30
  visited shared-prefix call boundaries; the generic snapshot-row induction
  and all six entry/snapshot negative controls pass. This relation reaches
  retail word175, not a claim of 175 byte-identical words.
- Exact selected C at native32 O0/O2/O3, plus four effective wrong-score,
  decay, signed-countdown and smoothing controls: seven executions, 544 cases.
- The original 74-word registered caller: 64 cases per stream, both class
  registrations, rows and list depths; 73-word coverage and wrong-pointer
  rejection. Two additional operand-order controls reject as described above.

The native fixture's decay mutant now recognizes the field expression
independently of the local pointer spelling. It remains effective with the
explicit record view. All seven generated forms for both historical v20 and
v43 bodies are independently checked identical before/after this helper fix.

The first passing run's private-stack diagnostic used a fixed fixture address.
That diagnostic was corrected to use each execution's restored incoming SP,
including both phases 0 and 8. Its receipts are retained, and both complete
final suites run fresh from a new immutable snapshot after the correction.

## Remaining private state and adoption gates

The phase-aware matrix still differs in four private words: **SP+0x84,
SP+0xA0, SP+0xAC and SP+0xB0**. The gravity square is stored at A0 rather than
84, and the original first force-input Y/Z deltas spill to B0/AC while the
draft keeps them in FP registers. Static retail additionally has two LWC1,
two SWC1 and one DIV.S; raw has two extra NOPs. The static division difference
is the original split zero/nonzero norm path versus the compiler's shared
division. This needs an explicit branch/delay and state relation.

Next complete the gravity/reverse-loop private-state relation, recover or
prove the stack-home/allocation and split-division normalization, then qualify
both padders, independent rebases, actual Make and strict full-image prediction
before installation and recount. The finite ordered trace does not prove
arbitrary aliases, NaNs/FCSR, fault-state, hardware or host gameplay behavior.

## Production and reproducibility

The final 1,517-input snapshot retains 1,515 immutable snapshot links and two
copied corrected task files, with zero live-worktree hardlinks. Its preceding
snapshot had 1,512 retained links and five copied task files. All final inputs
are checked before and after the suites. Production retains all 698 objects,
all 189,088 protected bytes/720 owners, source, guard CSV and compiler profile.
Actual ELF recount and shared tools checks pass with unchanged totals.
Production ELF SHA256:
`7c1c2f7ef67741c05a3d512530e777e9e4e4de6f29df28ebc8a22e9b95e4af90`.
Selected raw SHA256:
`d3408ea6ebd5cbbbf188e34aecbf49e0c6ea6b39ab389091e7ad4d20ddaf8c9b`.

Run `python3 -m unittest tools.tests.test_game_strip_update_151ad174_ordered -v`
with a fresh owned `CBFD_STRIP_UPDATE_ORDERED_WORK` path. Final receipts and
actual helper origins are in the ignored `ordered-final-v2/` packet. The dirty
sibling retains its 2,434 paths and 339 scoped dependency fingerprints. The
host directory has diagnostics only; no host source, Release or save changes.
No additional Claude call is used. Commit tools before consumer notes/pin.
