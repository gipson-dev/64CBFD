# Owner Ray Callback Direct C Match

Date: 2026-10-23. Consumer predecessor `62d2c41a`; tools predecessor
`7ea237d1`. Qualification tools committed first as
`65a27ef4d2d7c6947e8c0d2591d551abc5c6572e`. No push requested/performed.

## Recovered Routine

`func_150F00EC`, owner `conker/src/game/generated_11C2B0.c`:

- VA `0x150F00EC..0x150F0198`, ROM `0x11D59C..0x11D648`.
- All 43 words emit directly from semantic C, frame zero, zero bindings,
  no guards or compiler-profile changes. Symbol size advances from 12 to 172.
- Retail/raw C SHA-256:
  `7155834316b92418b73cdc0c49f35abc0dfc0756d99ae38ccc897057ce7323ba`.
- Recover `s32 func_150F00EC(OwnerRayEffect *effect)`. Keep the address name;
  local `EffectRay*` views describe verified fields, not a shared actor ABI.

The linked owner pointer is at effect +0x178. Test bit zero of its byte
+0x128. While active, copy the three raw position words +0x34/+0x38/+0x3C,
then calculate endpoint components +0x40/+0x44/+0x48 from the owner's current
position plus direction +0x140/+0x144/+0x148 times 500.0f. Set flag bits 1/2
at effect +0x58. While inactive, clear masks 4 and 2 separately. Return one
on both paths. Preserve every other byte and the original assembly.

Declare the motion-view pointer outside the active branch and put the flag
update last in source. That shape preserves retail's early flag snapshot,
sequential position reads/copies, later per-axis reads and flag store before
the final endpoint store. Do not cache a whole source vector or combine the
inactive clears. Overlapping guest layouts make these choices observable.
One redundant flag load at `0x150F0170` is unreachable; retain all 43 words,
without claiming the public paths visit that instruction.

## Actual Caller Boundary

The sole aligned literal ROM pointer is at `0x22E7F0`, VA `0x80089D30`.
It is slot 30 of the 42-entry `D_80089CB8` table in
`conker/asm/data/22E730.rodata.s`. There are no aligned direct JAL references.
The original parent is `func_1513CFE4`, frame 32, in
`conker/asm/nonmatchings/game_169510/func_1513CFE4.s`.

Qualify its complete selected 16-word window `0x1513D034..0x1513D074`:
unsigned byte selector +0x70, zero bypass, table load, pointer-only indirect
call at `0x1513D058`, pointer/expiration homes, signed expiration-byte reload
and return-controlled expiration. The authentic window has no selector range
check. Do not borrow fallback rules from a different dispatcher.

All sixteen window words are visited across 64 phases. A deliberately zero-
returning callback fires the expiration path; normal return one preserves
the saved byte's signed reload. Both original and compiled callback words
agree literally. The parent C remains a zero-return placeholder; the whole
parent, timer/animation paths, other callbacks and gameplay are not recovered
or qualified by this selected-window test. Its source/object are unchanged.

## Focused Qualification

Both tools copies pass six fresh checks before installation and all six
again after installation. No previous behavioral checks are substituted for
fresh checks. Pre-install runs: primary 6.031 seconds, mirror 6.174 seconds.
Installed runs: primary 7.496 seconds, mirror 7.308 seconds. Both shared
`check_project_tools.py` runs exit zero.

- 6,144 guest cases span all 256 active bytes, six flag words and disjoint/
  three overlapping owner/effect layouts. Compare independent sequential
  memory results and literal GPR/FPR/RAM/events/return state.
- Native32 O0/O2/O3 with trap UBSan: 13,824 finite-float cases per optimization,
  all bytes/fences and owner preservation, eight effective wrong-C controls.
  Compile-time checks cover sizes and each recovered field offset. Native
  storage is disjoint and typed; guest overlap does not claim portable C aliasing.
- Nine independent GNU links cover original, qualified padded and actual
  Make objects at three entry addresses. Ninety-six additional cases cover
  rebasing and guest stack overlap.
- All 384 selected access-fault prefixes fire. Original and compiled guest
  state, current PC and branch-delay origin are equal at each prefix. This
  is emitted-instruction evidence, not portable C fault or hardware/FCSR parity.
- Nine strict-image corruptions, including code, neighbors, symbol value,
  size, header, tail and truncation, are rejected. Snapshot/input history and
  the complete guard manifest remain byte-identical.

The first combined run exposed missing signed LB support in the local test
oracle; the second exposed a signed-vs-u32 expected register value. Correct
the target-specific oracle/expectation and retain the failed setup receipts.
Neither is a passing run or a production defect. Final six-test runs are clean.

## Production And Image

Whole-owner and isolated compiler payloads match independent GNU assembly
and retail. All 43 neighboring raw/padded routines and owner pools are fixed.
The actual three-command Make shadow uses normal O2/g3 and emits the complete
qualified object byte-for-byte. Existing duplicate-recipe Make warnings are
unchanged; there are no owner compiler diagnostics.

Independently link the qualified object into the original complete linker
script before installation. Predict the full ELF with exactly the target's
172-byte slot replacement and its existing symbol-size field change.
Actual independent/production images match the prediction literally:

- 134 changed ELF bytes = 133 code bytes + one symbol-size byte.
- Zero metadata/section exclusions, no serialization exceptions or new guards.
- All other 6,054 bodies and all 6,055 addresses are fixed.
- Protected Game data: all 720 owners / 189,088 bytes exact, SHA-256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- Result ELF SHA-256:
  `93964ef8cfe8f569707bfb09c79e34fe17c1f9912c01e4fe8ce2695984c51225`.
- Target object SHA-256:
  `ad260b8c4369b27ffe963c200c964008c65983962e7aa98eafa3ce561e810cac`.

Seal 15,906 files, 29 focused inputs and every one of 1,454 linker objects.
The old disposable Linux cache no longer existed. Rehydrate over native
stdin in 5.375 seconds and byte-verify all inputs, without Linux reading the
Windows project through DrvFS. Restore executable modes while streaming
ELF/shebang inputs, without changing file contents. Production Make exits
zero in 0.619 seconds; only the source, target object and ELF are mutable.

Native adoption verifies every sealed file before and after promoting only
the target object, ELF and unchanged linker-script/progress outputs. Preserve
all 1,580 pre-existing older-mirror dirty paths/statuses/hashes and its HEAD;
add only the two new task tools there, without committing that mirror.
Host Release, saves, configuration, editor and unrelated processes are untouched.

## Live Recount And Next Target

Capture actual adopted Windows ELF bytes and stream them to the standard
matcher, requiring equality with the production and independent-link images.
The fresh matcher exits zero in 1.398 seconds:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,756 / 5,505 (68.23%) | 0 | 1,749 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,083 / 4,832 (63.80%) | 0 | 1,749 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The converted-C denominator is unchanged. Reaching 75% still requires 4,129
exact functions, 373 more than this checkpoint. Remove only `func_150F00EC`
from the ELF-pinned queue: 1,618 placeholders, 122 semantic/other definitions
and nine unlocated entries remain. Next is `func_150FAA40`, 43 words/42
differences, queued only and uncredited. Keep the 862-word `func_1508CAD8`
owner stub separate.

Commit only the nine scoped consumer paths after final input/documentation
and mirror audits; root README receives only two aggregate-row updates.
Refresh Graphify through the normal hook, audit retention/unique relocation
of every one of the 43,836 preceding nodes, and verify all eight changed
C/Markdown hashes, mtimes and memberships. Retain any missing commit-stamp
limitation honestly; never forge a stamp. Retention is not full re-extraction.
