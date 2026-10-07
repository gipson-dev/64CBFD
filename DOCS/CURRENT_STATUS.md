# Current Decomp Status

Last verified: 2026-10-07

This page is the short, current handoff for `64CBFD`. Historical experiments
remain in [WORKING_NOTES.md](WORKING_NOTES.md); detailed session handoffs live
under [WORKING_NOTES/](WORKING_NOTES/).

## Repository state

- Branch: `master`
- The restoration baseline is banked in coherent commits beginning after
  `2ed3523` (`tool updates`): generated-slice assembly support, restored guest
  routines, OGL reference tooling, RGBA5551 tooling, and documentation.
- Before checkpointing, `git status --short` reported 123 changed tracked paths
  and 37 untracked paths. The empty personal `DOCS/user notes.md` remains
  preserved locally and excluded through `.git/info/exclude`.
- The broad assembly restoration in the current tree is buildable, but it
  reduced the number of functions represented in C. It improves original-code
  coverage and port support; it is not C-decomp completion.

## Measured progress

Actor-gated packet match:
[Note 1077](WORKING_NOTES/1077-game-actor-gated-packet-match-20261007.md).
`func_15143E94`:98 words/frame0x38, full-word command/flags and byte return.
Signed-byte snapshot count, health/checker gates, live context, two RNG calls
and partially initialized eight-byte packet recovered. Eleven checked guards
normalize only the closed opening schedule; branch target/dependencies and
private layout unchanged. Scope the checker ABI locally, shared headers untouched.
8192 paired guest/362 callback-RNG/18856 native/12 original caller-pair cases,
six negatives, poisoned padding and actual owner/pool/padder/stale gates qualify.
US ELF/audit passes; only target changes across6059 slots, all addresses/extents/
protected sections/720 owners/10855 prior guards unchanged,10866 total.
Exact3349/5465 (61.28%), Game2676/4792 (55.84%),2116 different, zero drift;
conversion unchanged. README aggregate matching rows only.
All131 post-link regression tests pass in692.507s; final10 packet tests rerun
after trace/frame-reporting improvements pass in61.780s. Zero skips/errors/
failures.59 documents/3668 relative links/zero broken; tools/syntax/diff and
final post-regression linked audit pass.
Next98-word cursor updater `func_1514401C`; sampler exits/oriented27 offsets
stay open. No sibling/Release/save/runtime, complete-caller/hardware/gameplay,
host adoption or push.

Record-query direct match:
[Note 1076](WORKING_NOTES/1076-game-record-query-direct-match-20261007.md).
`func_151438D8`:272 direct C words/frame0x60, no guards/profile changes.
Typed pointer return,11 field groups, u16 any/all masks, matched range helper
and last-match selection recovered. Scope the legacy table-array declaration
to this owner; shared headers/other owners stay unchanged.
12288 paired guest/196608 native/1470 range/120 field/32 original caller-fragment
cases, four negatives, copied owner/624-byte pool/two warnings and actual
padder qualify. US ELF passes; only target changes across6059 slots, all
addresses/extents/protected sections/720 owners/10855 guards unchanged.
Exact3348/5465 (61.26%), Game2675/4792 (55.82%),2117 different, zero drift;
conversion unchanged, README aggregate rows only. All121 post-link tests pass
in445.383s, zero skips/errors/failures;58 docs/3657 relative links/zero broken,
tool/syntax/diff checks pass. Final post-regression audit passes.
Next sampler exit recovery or
forward placeholder `func_15143E94`; oriented27 private offsets remain open.
No sibling/Release/save/runtime, whole-caller/hardware/gameplay or push.

Range-clamp byte match:
[Note 1075](WORKING_NOTES/1075-game-range-clamp-byte-match-20261007.md).
`func_15143D18`:36 words/frame0x10; using the argument pointers directly recovers
the original saved-pointer shape. Thirteen expected-word guards normalize only
temporary GPR allocation, with no frame/arithmetic/control/ordering changes.
3750 paired guest/1250 native/250 original call-delay cases and copied-owner/
actual-padder gates pass. Only target changes across6059 slots; all addresses,
protected sections/720 data owners and10842 prior guards unchanged,10855 total.
Exact3347/5465 (61.24%), Game2674/4792 (55.80%),2118 different, zero drift.
Conversion unchanged; README updates aggregate rows/date only.
All111 post-link tests pass in368.274s, zero skips/errors/failures;
57 documents/3646 relative links/zero broken, tool/syntax/diff checks pass.
Thirty further sampler exit/storage controls find no exact form. Sampler and
oriented builder remain uninstalled. Next sampler exit recovery or272-word
record query `func_151438D8`. No sibling/Release/save/runtime, gameplay or push.

Area-sampler recovery, not installed:
[Note 1074](WORKING_NOTES/1074-game-area-sampler-qualified-recovery-20261006.md).
`func_151432BC` now has a qualified signed-descriptor/five-input C candidate:
252 words, original frame0x50, 109 positional differences against254 retail
words. Remaining work is two shortened block exits/shared RA reload and the
circle RNG-byte store schedule. No broad guards, source/profile changes or
new matching count. Ten tests pass in18.864s:1024 independent guest cases,
48 conversion controls,1536 original-angle cases,64 complete original caller
cases,256 actual32-bit native cases, six negatives and copied-owner gates.
Candidate and original preserve external writes/calls and saved state under
these bounded tests; general FCSR/real RNG/gameplay remain unqualified.
Root README and production totals remain Note1073. See the note's resume steps.
Final24-test neighboring regression passes in34.986s, zero skips/errors/failures;
152 compiler controls find no exact candidate. All6059 production slots,
protected sections/720 data owners/10842 guards unchanged;56 docs/3633 relative
links/zero broken. Tools/syntax/diff checks pass. No production rebuild or push.

Point-transform assembly-to-C match:
[Note1073](WORKING_NOTES/1073-game-point-transform-assembly-to-c-match-20261006.md)
converts `func_15143134`:98 words/frame0x78, typed three-input ABI, live
diagnostics, fixed/float matrix paths and null/zero translation fallback.
31 relocation-checked guards normalize only the closed saved-register cycle
and independent save ordering; no frame/control/arithmetic rewrite.
1950 paired guest,180 original-helper,144 native and39 original call/delay
sites/234 seeded cases qualified; six negatives, actual padding/stale metadata
and copied-owner preservation. All6059 linked slots are unchanged from the
exact assembly baseline, including all addresses/extents and protected sections.
All720 Game-data owners/189088 bytes exact, warnings2->2,10811 prior guards
unchanged,10842 total. Converted5465/6042 (90.45%), Game4792/5321 (90.06%);
exact3346/5465 (61.23%), Game2673/4792 (55.78%),2119 different, zero drift.
Next254-word placeholder `func_151432BC`; oriented27 private offsets stay open.
All92 focused post-link tests pass in371.491s, no skips/errors/failures.
55 documents/3623 relative links/zero broken, tools/syntax/diff checks pass.
README changes aggregate tables only. No sibling/Release/save/runtime, host
adoption, whole-caller/hardware/gameplay acceptance or push.

Texture resolver match and original table binding:
[Note1072](WORKING_NOTES/1072-game-texture-resolver-match-and-table-binding-20261006.md)
recovers `func_1514306C`:50 C-emitted words, no frame, exact signed-index/
low-kind-byte/unsigned-threshold behavior.72 compiler controls, two exact O2/g3
forms. Two checked HI16/LO16 guards bind only the compact table reference to
the original800A562C asset table; no instruction scheduling/register/frame edits.
All12 pre-install checks pass in53.365s:13824 paired guest,19200 native,
486 complete102-word cache-caller/50-word resolver cases, ten negatives,
actual post-processing/padding/stale guards and three independent pool checks.
US ELF/6059-slot audit passes, only target changes. Protected sections/720
data owners/189088 bytes and warnings2->2 unchanged;10809 historical guards
retained,10811 total. Exact3345/5464 (61.22%), Game2672/4791 (55.77%),
2119 different, zero drift; conversion unchanged. README aggregate rows only.
All81 focused post-link tests pass in315.971s, no skips/errors/failures;
54 documents/3611 relative links/zero broken, tools/syntax/diff checks pass.
Next98-word `func_15143134`,
currently original assembly; recover point/output/Mtx ABI and status/helper
boundaries. Oriented27 private offsets remain open. No sibling/Release/save/
runtime, host adoption, original submit/render/gameplay acceptance or push.

Texture-cache submission match:
[Note1071](WORKING_NOTES/1071-game-texture-cache-submission-match-20261006.md)
recovers `func_15142E24`:102 direct retail words/frame0x40 under unchanged
O2/g3, no guards. Typed source/attachment ABI, signed packed shifts, live flags,
cache-hit gates and observable retail attachment same-value store.
32 controls; ten pre-install tests pass in39.947s:2304 paired guest,88 homes,
486 original-resolver,6912 native and nine original call/delay pairs, negatives,
actual padding and copied-owner preservation. US ELF/6059-slot audit passes:
only target changes; protected sections/720 exact data owners/189088 bytes,
10809 guards and two warnings unchanged. Exact3344/5464 (61.20%),
Game2671/4791 (55.75%),2120 different, zero drift; conversion unchanged.
All52 post-link tests pass in215.511s, no skips/errors/failures; tools/syntax/
diff checks pass,53 documents/3596 relative links/zero broken links.
Root README updates aggregate rows only.
Next50-word `func_1514306C` remains a placeholder; original instructions
qualified, not recovered C. Oriented142/frameB8/27 private differences remain;
ten extra matrix-storage controls find no improvement. No sibling/Release/save/
runtime, host adoption, whole-caller/submit-helper/gameplay acceptance or push.

Oriented matrix original-frame recovery, not installed:
[Note1070](WORKING_NOTES/1070-game-oriented-matrix-original-frame-recovery-20261006.md)
recovers `func_15142600`'s original142 words/frame0xB8 from in-place direction
normalization. Only27 private stack immediates differ:ten direction references
are four bytes low; seventeen matrix references are eight bytes low. All input
homes, early temporaries, arithmetic, call position and saved-state words agree.
128 maintained controls, no exact candidate. Thirteen tests pass in120.279s:
2448 six-body guest cases,1224 native caller cases per candidate across five
candidates,144 original caller/converter cases per body, eighteen compiled
negatives, two actual padder bodies and five copied builder owners.
All6059 production slots/720 data owners/10809 guards/protected sections remain
the Note1069 baseline; source and root README unchanged. No new matching count.
Recover the remaining private placement from legitimate C before installation.
General FCSR/conversion, native NaN payload/private trace identity and gameplay
acceptance remain outside the bounded gates. No sibling/Release/save/runtime,
host adoption or push.

All41 focused neighboring tests pass in185.411s, zero skips/errors/failures;
52 documents/3585 relative links/zero broken links, tools/syntax/diff checks pass.

Row-scaled matrix match and oriented-layout follow-up:
[Note1069](WORKING_NOTES/1069-game-row-matrix-match-and-oriented-layout-20261006.md)
recovers `func_15142838`:55 direct words/frame0x58 under unchanged O2/g3,
no guards. Nine-input pointer/float ABI, original rotation provider, translations
before row scaling, and original guMtxF2L call. Typed local declaration and
output cast leave `func_15133760`'s24 retail words and all31 caller-owner raw
functions unchanged. Sixteen controls;2160 paired guest/full trace/storage,
192 float-edge,36 guest-only home,288 original caller/converter and1176 native
caller cases, nine compiled negatives and actual padding qualification.
Only this builder changes across6059 slots; all10809 guards, protected sections,
720 Game-data owners and both owners' two warnings unchanged.
Exact3343/5464 (61.18%), Game2670/4791 (55.73%),2121 different, zero drift;
converted counts/bytes unchanged. All40 focused post-link tests pass in119.063
seconds, no skips/errors/failures.

Oriented `func_15142600` remains uninstalled:64 maintained controls now include
142/frameC8/47 and142/frameD0/44 stack-only candidates. The former recovers
direction slots exactly; the latter recovers early delta/horizontal/up slots.
Twelve tests qualify five guest bodies and four native candidates, retaining
all previous acceptance boundaries. Recover legitimate142/frameB8 layout next;
do not install stack/frame rewriting. Rotation provider is still bounded and
original conversion qualification finite/exact integral only. No sibling/
Release/save/runtime, hardware FCSR, gameplay acceptance, host adoption or push.

Initial oriented matrix recovery checkpoint, not installed:
[Note1068](WORKING_NOTES/1068-game-oriented-matrix-recovery-20261006.md)
qualifies `func_15142600`'s two-point basis, normalization, row/column scaling,
start-point translation and twelve-input caller ABI.32 maintained SDK controls:
142 words/frame0xB8/84 differences; a closer142/frame0xC8 challenger has57
differences, all stack immediates. Every non-stack instruction already agrees.
Eleven tests pass in39.018 seconds:2448 three-body guest cases,1224 native
caller cases per candidate,144 complete original caller/converter cases per
body, nine compiled negatives, native integer-load rejection, actual padding
and copied-owner preservation. Typed caller correction is copy-only; eight
caller-owner functions stay unchanged. Both builder copies preserve92 neighbors,
pools and two warnings. No candidate or guards installed; root README and
production baseline stay unchanged. Recover the challenger's private layout
and original frame0xB8 next, without a stack/frame rewrite. Scope and remaining
verification gates are recorded in Note1068.

Scaled matrix recovery:
[Note 1067](WORKING_NOTES/1067-game-scaled-matrix-match-20261006.md)
recovers `func_151424F4`:67 direct words/frame0x68, no guards/profile changes.
Typed output pointer and eleven float inputs; original rotation call, translation
stores, separately rounded column*row and matrix-element products, guMtxF2L ABI.
Correct local caller declaration/three float loads in `func_15133510` without
changing its30 retail words or any of its owner's31 raw functions.
16 controls;6480 paired guest/full trace/storage cases,696 float edges,48
guest-only home probes,3372 native caller cases, ten compiled negatives and
a native integer-load rejection.432 connected cases execute all30 original
caller/67 builder/115 converter words on finite exactly integral conversions.
Rotation provider remains a model; general FCSR/NaN conversion, helper
restoration and gameplay acceptance are not claimed.
Only builder changes across6059 slots; all10809 guards, protected sections/
720 owners and both owners' two warnings unchanged. Exact3342/5464 (61.16%),
Game2669/4791 (55.71%),2122 different, zero drift; converted counts/bytes
unchanged. All77 focused post-link tests pass in531.767 seconds, no skips/
errors/failures;49 docs/3546 relative links/zero broken, tools/syntax/diff
checks pass.
Next142-word `func_15142600`, frame0xB8: oriented basis from two points,
normalization, scaling, translation and fixed conversion. That checkpoint's
sixteen initial scratch controls gave143 words/frame0xC8/138 differences under
O2/g3, then uninstalled/unqualified. Current qualified controls and remaining
frame recovery are in the oriented-matrix section above. No sibling/Release/
save, runtime, host adoption, gameplay acceptance or push change.

Scaled descriptor recovery:
[Note 1066](WORKING_NOTES/1066-game-scaled-descriptor-match-20261006.md)
recovers `func_15142180`:80 direct words/frame0x70, no guards/profile changes.
Typed five-input void ABI, original76-byte descriptor, three-word position copy,
four separately rounded scale products and live D_800A5470/5474 reads. Submit
descriptor/position-subrecord pointers with0,255,1; opaque third input retains
all32 bits.64 controls;10800 paired guest cases/full traces/storage,2240 edge
cases,28 guest-only private overlap/home probes,20992 native cases,42 original
call/delay-pair cases and12 semantic negatives. Native excludes only private
padding61..63; helper/full callers, hardware FCSR and gameplay remain unvalidated.
Only target changes across6059 slots; all10809 guards, protected sections/720
owners, original pool and two owner warnings unchanged.
Exact3341/5464 (61.15%), Game2668/4791 (55.69%),2123 different, zero drift;
converted counts/bytes unchanged. All65 focused post-link tests pass in513.711
seconds, no skips/errors/failures;48 docs/3533 relative links/zero broken,
tools/syntax/diff checks pass.
Next67-word `func_151424F4`, frame0x68: float matrix construction, separately
rounded row/column scaling, translation and guMtxF2L call. Sixteen initial
controls find a direct candidate, not installed or qualified. No sibling/Release/
save, runtime, host adoption, gameplay acceptance or push change.

Random descriptor recovery:
[Note 1065](WORKING_NOTES/1065-game-random-descriptor-match-20261006.md)
recovers `func_15141F78`:96 direct words/frame0x78, no guards/profile changes.
Typed six-input void ABI, original40-byte descriptor with unsigned byte fields,
two ordered integer draws and one float draw; submit all16 arguments, including
the address source+4 rather than its stored value.64 controls;6912 paired guest
cases/full traces/storage,944 byte/float-edge cases,48 guest-only home probes,
57856 native cases,144 connected original call/delay-pair cases and12 semantic
negatives. The original full callers/RNG/submit helper and hardware FCSR are not
executed by those bounded fixtures. Native excludes three unspecified padding
bytes; exact guest stack provenance retained. Only target across6059 slots;
all10809 guards, protected sections/720 owners and two owner warnings unchanged.
Exact3340/5464 (61.13%), Game2667/4791 (55.67%),2124 different, zero drift;
converted counts/bytes unchanged. All54 focused post-link tests pass in528.932
seconds, no skips/errors/failures;47 docs/3521 relative links/zero broken,
tools/syntax/diff checks pass.
Next80-word `func_15142180`, frame0x70:76-byte descriptor, copied three-word
position, live constants and five-argument submit ABI. No sibling/Release/save,
runtime, host adoption, gameplay acceptance or push change.

Effect-record updater recovery:
[Note 1064](WORKING_NOTES/1064-game-effect-record-updater-match-20261006.md)
recovers `func_15141E38`:80 words/frame0x60,56 direct plus24 closed guards.
Typed void actor/index ABI; refresh every matching live record, create/copy/
link only when none matched. Minimal12-byte request retained; four private
payload-home guards restore retail's three uninitialized tail bytes, not a
new initialized field.7680 three-body guest/7680 native cases,1728 connected
search cases,3072 guest/1536 native checked-caller cases,36 guest actor-home
probes and ten semantic negatives. Normalized/retail full traces/storage agree;
native comparison excludes only three unspecified request-tail output bytes.
Copied owner93 functions: only target changes, warnings3->2, original pool
unchanged. Production only target across6059 slots; old10785 guards unchanged
plus24, protected sections/720 owners unchanged. Exact3339/5464 (61.11%),
Game2666/4791 (55.65%),2125 different, zero drift; converted unchanged.
All56 focused post-link tests pass in430.719 seconds, no skips/errors/failures;
46 docs/3509 relative links/zero broken, tools/syntax/diff checks pass.
Next96-word `func_15141F78`, frame0x78:
descriptor/RNG construction, float call ABI and live source reads need recovery.
The old commented draft dereferences source+4, but retail passes that address.
No allocator/link-helper restoration, host/gameplay/hardware acceptance,
sibling/frozen Release/runtime or push change.

Context-classifier recovery:
[Note 1063](WORKING_NOTES/1063-game-context-classifier-match-20261006.md)
recovers `func_15141CC0`: all57 words directly from C, no frame or guards.
One signed32-bit world read, four overrides and full-width context switch.
Existing pool anchor retains the16-entry table at addend0x218 after both
actor tables; all150 targets and the original640-byte owner are unchanged.
16 controls,15822 paired guest,5308551 native and2688 connected dispatcher
cases; eight compiled semantic negatives. Only target changes across6059
slots; all10785 guards, protected sections and720 data owners unchanged,
warnings3->3. Exact3338/5464 (61.09%), Game2665/4791 (55.63%),2126 different,
zero drift; converted counts/bytes unchanged. All32 focused tests pass in
277.833 seconds, no skips/errors/failures;45 docs/3497 links/zero broken,
tools/syntax/diff checks pass.
Next `func_15141E38`:80 words/frame0x60, still a placeholder. The intervening
37-word `func_15141DA4` is already exact. Preserve live search/cursor lifetime,
refresh all matching records, then allocate/link only when none matched.
Eight initial controls: private-cursor O2/g3 candidate fits80 words but has
frame0x58 instead of0x60 and37 differences; not installed or qualified.
No sibling/Release/runtime/host adoption, hardware/gameplay acceptance or push.

Actor-classifier recovery:
[Note 1062](WORKING_NOTES/1062-game-actor-classifier-match-20261006.md)
recovers `func_15141C0C`:all45 words directly from C, no frame or new guards.
Unsigned actor byte+4,19 mapped IDs/categories0..10, default11. Existing owner
rodata anchor preserves both original45/89-entry switch tables and drops the
compiler's private pool/padding.32 controls,8192 two-body guest,16384 native
and4608 connected dispatcher cases, six compiled negatives. Only target changes
across6059 slots; all10785 guards and protected sections/720 owners unchanged,
warnings3->3. Exact3337/5464 (61.07%), Game2664/4791 (55.60%),2127 different,
zero drift; converted counts/bytes unchanged. All24 focused post-link tests
pass in257.759 seconds, no skips/errors/failures; final eight-test ownership/
measured-frame rerun passes in36.264 seconds.44 docs/3485 links/zero broken;
tools/syntax/diff checks pass.
Next57-word `func_15141CC0`:16 initial controls give a direct candidate, not
installed/qualified; preserve the neighboring context-table anchor offset.
No sibling/Release/runtime/host adoption, hardware/gameplay acceptance or push.

Effect-dispatch recovery:
[Note 1061](WORKING_NOTES/1061-game-effect-dispatch-match-20261006.md)
recovers `func_15141A7C`:100 words/frame0x48,75 direct plus25 closed guards.
Explicit scoped helper-result sequencing preserves the live classifier lookup
on native C as well as IDO. Repeated record selectors, signed payload/counts,
live list links and registered cursor aliases remain.13824 three-body guest,
69632 connected retail-classifier,70848 actual32-bit native,288 cursor-alias,
864 guest caller/240 native wrapper cases and compiled negatives qualify the
contract. Raw C's one extra private-read site is explicitly bound, not blanket
stack-filtered. Only target changes across6059 slots; original10760 guard rows
unchanged,25 appended. Protected sections/720 data owners unchanged; warnings
3->3. Converted counts/bytes unchanged; exact3336/5464 (61.05%), Game2663/4791
(55.58%),2128 different, zero drift. All48 focused post-link tests pass in
495.394 seconds, no skips/errors/failures; final portable-prefix test rerun
passes.43 documents/3473 relative links/zero broken; tools/syntax/diff pass.
Next45-word actor classifier `func_15141C0C`:two fixed retail switch tables.
No helper-C/gameplay/hardware/host adoption, sibling/Release/runtime or push.

Historical effect-dispatch investigation, superseded by Note 1061:
[Note 1060](WORKING_NOTES/1060-game-effect-dispatch-investigation-20261006.md)
continues after banked `e5bf72e0` with100-word/frame0x48 `func_15141A7C`.
112 controls: live selector99/26; private cursor-write candidate100/21.
All100 retail words derive from a phased S0/S1 swap, closed prefix/query
scheduling and equivalent private cursor operations, without installation.
13824 guest cases per pairing;100-word source adds13764 proven private cursor
reads, all other traces/storage/calls equal. Connected real classifiers/list
search:69632 cases pass on each99/100-word pairing,128 helper words mapped/122
reached;100-word source binds110976 extra private reads, other traces equal.
Native/negative/relocation/padder/production
gates remain. All6059 production slots/10760 guards/protected sections unchanged.
Game2662/4791 exact,2129 different, zero drift. No sibling/Release/runtime/push.

Position-projection recovery:
[Note 1059](WORKING_NOTES/1059-game-position-projection-match-20261006.md)
recovers `func_1514182C`: all 63 words / frame 0x80 directly from C under
existing O2/g3, no guards. Delta declarations before the matrix recover its
retail SP+0x34 layout. Preserve all live origin reads before output stores and
the separate scale-then-500 multiplications. The float-height caller
`func_15141928` remains exact across its 18-word slot. Effect-only void ABI;
incidental guest F0 is qualified separately, not a native return contract.
15488 finite/guest-home cases, 144 connected retail SDK cases, 360 connected
caller cases, 9600 native finite cases, 720 special-float cases on each guest
body and native C, 36 controls and ten compiled negatives. Only target changes
across 6059 slots; protected sections, 720 Game-data owners and 10760 guards
unchanged, owner warnings 0->0. Converted counts/bytes unchanged; exact total
3335/5464 (61.04%), Game 2662/4791 (55.56%), 2129 different, zero drift.
All 37 focused post-link tests pass in 206.840 seconds, no skips/errors/failures;
41 documents/3453 relative links/zero broken; compileall/diff/tools checks pass.
Next `func_15141A7C`: 100 words / frame 0x48; repeated callback-table reads,
live list iteration and connected classifier ABI need recovery. No host,
hardware/FCSR/gameplay acceptance, sibling/Release/runtime or push change.

Historical position-projection investigation, superseded by Note 1059:
[Note 1058](WORKING_NOTES/1058-game-position-projection-investigation-20261006.md)
continues from banked `e1298167` with63-word/frame0x80 `func_1514182C`.
60 compiler controls. The fitting63-word/31-difference candidate fails24/108
origin-alias cases; cached origin values agree in all126 bounded guest cases
but emit67 words/frame0x88/47 differences. Identity rotation is modeled;40
connected retail coordinate-helper words execute. Float height/caller and
return ABI, alias-preserving footprint, native/negative/production gates remain.
No source/guard/count change; Game2661/4791 exact,2130 different, zero drift.
No next-function acceptance, sibling/Release/runtime or push change.

Actor-event dispatch recovery:
[Note 1057](WORKING_NOTES/1057-game-actor-event-dispatch-match-20261006.md)
recovers `func_151416E8`:55 words/frame0x18, all direct under existing O2/g3,
no guards. Repeated volatile selector/table lookups, byte command, live event
gate, cleanup/signed status stores and unsigned N64 payload address retained.
60724 two-body guest/262144 actual32-bit native cases;32 controls/nine compiled
negatives. Only target changes across6059 slots; protected sections/720 owners
and10760 guards unchanged, owner warnings0->0. Converted unchanged; exact
total3334/5464 (61.02%), Game2661/4791 (55.54%),2130 different, zero drift.
All28 focused post-link tests pass in246.167 seconds, no skips;39 docs/3432
links/zero broken. Next63-word `func_1514182C`:16 initial controls give63 words/
frame0x80/31 differences. Matrix translation row, float height ABI and caller need
qualification; no next-function installation, host/hardware/gameplay acceptance
or sibling/Release/runtime/push change.

Piecewise envelope recovery:
[Note 1056](WORKING_NOTES/1056-game-piecewise-envelope-match-20261006.md)
recovers `func_151415D4`:69 words/no frame, existing O2/g3,56 direct plus13
closed FPR-lifetime guards. Scoped factors recover rise store/branch/nop
directly;6480 three-body guest/3240 native finite cases,324 special-float
cases,18 bounded loops,32 controls/eleven negatives. Strict/live/unchecked
semantics retained. Audit: only target across6059 slots; protected sections/
720 owners unchanged,10747 old guards plus13, owner warnings0->0. Converted
unchanged; exact total3333/5464 (61.00%), Game2660/4791 (55.52%),2131 different,
zero drift. All19 focused tests pass in61.523 seconds, no skips (nine new/ten
changed metadata methods, not all earlier suites).38 docs/3420 links/zero
broken, tools/compileall/diff checks pass. Next55-word `func_151416E8`,16
initial controls; selected47/frame0x18/49 differences, no qualification or
installation. No hardware/FCSR/gameplay/host acceptance,
shared-header or sibling/Release/runtime change.

Previous envelope investigation:
[Note 1055](WORKING_NOTES/1055-game-piecewise-envelope-investigation-20261006.md)
starts `func_151415D4` from banked `adbeca4e`:69-word/no-frame retail envelope,
32 compiler controls, selected68 words/52 differences (product-first49).
720 two-body finite guest storage/access cases and eight bounded unchecked-loop
runs pass.65 raw/66 retail reachable words; three duplicate preludes untouched.
One missing rise-branch word plus allocation/branch differences remain; native,
special-FP, negative, padder and production gates pending. No installation,
guard/profile/image change. Current exact counts below remain unchanged.

Timed interpolation recovery:
[Note 1054](WORKING_NOTES/1054-game-timed-interpolation-match-20261006.md)
recovers `func_15141478`:59 words/frame0x30, existing O2/g3,50 direct plus nine
derived private-pointer-home/commutative FP guards. Explicit RNG call ordering,
strict-negative expiry, live post-call fields and unclamped smoothing retained.
8640 finite/432 private-home/1008 special-FP three-body guest cases;
4320 finite/504 special-FP native cases,32 controls and ten compiled negatives.
Completed production audit: only target across6059 fixed slots; protected
sections/720 owners unchanged,10738 old guards plus nine, owner warnings0->0.
Converted unchanged; exact total3332/5464 (60.98%), Game2659/4791 (55.50%),
2132 different, zero drift. All18 focused post-link tests pass in55.115 seconds,
no skips: nine new plus nine changed metadata tests, not all101 earlier tests.
36 docs/3401 links/zero broken; tools/compileall/diff checks pass.
Next69-word `func_151415D4` piecewise envelope:16 initial controls, selected
68 words/no frame/52 differences, still a production placeholder. No hardware/
FCSR/gameplay/host claim or sibling/frozen Release/build/save/runtime change.

Grid/channel updater recovery:
[Note 1053](WORKING_NOTES/1053-game-grid-channel-updater-match-20261006.md)
recovers `func_151412BC`: 96 words/frame0x18, existing O2/g3, 53 direct words
plus43 guards derived from two closed register cycles and independent LO16
address scheduling. All branch/delay/arithmetic shapes retained, normalized
V0=4; owner-local table/pointer casts, no shared-header or data change.
1728 three-body guest storage/trace cases, signed bounds/byte cycling, 864
native cases and ten negatives; nine tests include144 compiler controls.
Only target across6059 fixed slots, protected sections/720 owners unchanged;
10695 guards plus43, total10738, owner warnings0->0, zero new. Converted
unchanged; exact total3331/5464 (60.96%), Game2658/4791 (55.48%), 2133 different,
zero drift. All92 retained post-link tests and the corrected nine-test updater
rerun pass (239.123 seconds), no skips;101 unique current tests qualified.
Initial combined run's sole caller-fixture failure is corrected/documented;
35 docs/3389 relative links/zero broken. Tools/compileall/diff checks pass.
Next59-word `func_15141478` randomized interpolation:112 initial controls.
New both-pointer-early form gives59/frame0x30/nine differences; derived six
private-slot/three commutative FP changes reproduce all words,2160 finite guest
storage/callback/access cases pass. No native/padder/full match installation.
Sibling grid updater
already retail-translated; no hardware/gameplay/host claim, sibling/Release
change or push.

Payload-copy wrapper recovery:
[Note 1052](WORKING_NOTES/1052-game-payload-copy-wrapper-match-20261006.md)
recovers `func_151407D0`: 53 words/frame0x40, existing O2/g3, 43 direct words
plus ten closed success-schedule/branch guards with counter HI16 movement.
Descriptor pre-mutations, failure, live copy/selector/counter and allocation
return qualified. Correct callee `func_1513D524`'s false void/word-descriptor
ABI; all28 direct words unchanged. 40 controls, 5376 ordinary/65536 byte-pair
guest cases, 72 join/1440 connected cases, 132352 native cases/ten negatives.
Only target across6059 fixed slots, protected sections/720 owners unchanged;
10685 guards plus ten. Two ABI warnings removed (45->43), target owner0->0,
zero new. Converted unchanged; exact total3330/5464 (60.94%), Game2657/4791
(55.46%), 2134 different, zero drift. All92 post-link tests pass in901.823
seconds, no skips; 34 docs/3377 relative links/zero broken.
Next96-word `func_151412BC` grid lookup: preliminary correct frame/length,
53 differences; 1728 two-body guest storage/trace cases agree, raw V0 still
differs. Native/complete ABI/match unqualified, no installation. Larger
`func_151408A4` unrecovered.
Sibling outer wrapper already retail-translated; no full allocator/dispatch/
hardware/gameplay/host claim, sibling/Release change or push.

List-key sorter recovery:
[Note 1051](WORKING_NOTES/1051-game-list-key-sort-match-20261006.md)
recovers `func_151406AC`: 72-word body/73-word slot, frame0x138, existing
O2/g3, 54 direct instructions plus 18 register-only lifetime guards and trailing
nop. Stable equal-key ordering, captured successor and live link repairs;
5760 two-body full-storage guest cases, 65535 two-body bypass values, 960
native storage, 65536 native signed-value and 65535 native bypass cases.
Strict guest boundaries preserve retail's null-head write and negative-key
sentinel walk; no safety/cycle fixes. Production link/audit pass: only target
changes across 6059 fixed slots, protected sections/720 owners unchanged;
10667 existing guards plus18, 45 unchanged warnings, zero new. Converted
counts unchanged; exact total3329/5464 (60.93%), Game2656/4791 (55.44%),
2135 different, zero drift. 33 docs/3365 links/zero broken.
All 83 post-link regression tests pass in 839.818 seconds, no skips.
Next adjacent 53-word `func_151407D0` allocation/copy wrapper, including the
false void return of its `func_1513D524` callee. Sibling sorter already has
retail-translated instructions with host cycle guards; leave it unchanged.
No full dispatch/hardware/gameplay/host claim, sibling/Release change or push.

Basis-vector quad builder recovery:
[Note 1050](WORKING_NOTES/1050-game-basis-quad-builder-match-20261006.md)
recovers `func_15140410`: 167 words/frame 0x68, existing O2/g3, 165 direct
plus two independent load scheduling guards. Captured scaled components,
live translations, fresh-copy slot reloads and original-pointer return qualified
with 24 controls, 1728 standalone/324 actual-backend/198 float/144 actual-owner
two-body guest cases, 576 native storage and all 65536 signed-view null cases.
Only target slot changes across 6059 fixed slots; protected sections and 720
data owners unchanged, 10665 existing guards preserved plus two. Typed owner
call removes exactly three old warnings, leaving 45 unchanged and zero new;
all 13 wrapper instructions remain exact. Converted counts unchanged;
exact total 3328/5464 (60.91%), Game 2655/4791 (55.42%), 2136 different,
zero drift. All 75 focused post-link tests pass in 765.095 seconds, no skips;
32 docs/3353 relative links/zero broken. Tools, compileall and diff checks pass.
Next adjacent `func_151406AC`: 72-word body/73-word slot, non-null list and
sentinel-key preconditions need further qualification. Preliminary 100 controls:
correct body/frame, 18 remaining differences; 864 valid-list and 65535 nonzero
bypass two-body guest cases agree with retail, not yet installed/native-qualified.
Sibling generated reference
still contains a zero-return placeholder; no host adoption/runtime claim or
sibling source/build/save/frozen Release change or push.

Cached quad builder recovery:
[Note 1049](WORKING_NOTES/1049-game-cached-quad-builder-match-20261006.md)
recovers `func_15140190`'s false stub: 134 words/frame 0xD0 under existing
O2/g3, 129 direct plus five independent first-corner scheduling guards.
24 controls, 864 two-body actual-matrix guest cases/all 174 chain words,
864 native full-storage cases and all 65536 native signed-view null cases.
Live fresh-copy slot reloads, translation reads, original return and escaped
cursor updates preserved. Only quad slot changed across 6059 slots; all
addresses/sizes, protected sections and 720 owners unchanged, 10660 existing
guards preserved plus five. 48 owner warnings unchanged, zero new. Converted
counts stay 5464/6042 and Game 4791/5321; exact total 3327/5464 and Game 2654/4791,
2137 different, zero drift. 31 docs/3341 links/zero broken. All 66 focused
post-link tests pass in 741.875 seconds, no skips.
Next adjacent 167-word `func_15140410` basis-vector quad builder; no full
backend/orientation/hardware FCSR/gameplay/host claim, sibling/Release change
or push.

Vertex attribute initializer direct C conversion:
[Note 1048](WORKING_NOTES/1048-game-vertex-attribute-initializer-direct-match-20261006.md)
converts retained `func_151400D0`: all 48 direct words/frame zero, existing
O2/g3, no guards/profile/shared header/data. Owner-local void/pointer ABI and
constructor cast corrected; all 217 constructor/two-helper words unchanged.
Transient flag stores, signed colors and alias-sensitive read order qualified
with 24 controls, 456 two-body guest cases, 65536 halfword cases, 131072 native
standalone, 3072 two-body actual-chain guest and 131072 actual-chain native
cases. All 6059 linked slots identical to assembly checkpoint; protected
sections/720 owners/10660 guards intact. 48 preexisting warnings unchanged,
zero new. Converted total 5464/6042, Game 4791/5321; exact total 3326/5464,
Game 2653/4791, zero drift, 2138 different. All 60 focused post-link tests
pass in 730.693 seconds, no skips; 30 docs/3329 relative links have no breaks.
Next recover 134-word `func_15140190` cached quad builder's false C stub;
no full backend/hardware/gameplay/host adoption, sibling source/build/save/
frozen Release change or push.

View corner initializer direct C conversion:
[Note 1047](WORKING_NOTES/1047-game-view-corner-initializer-direct-match-20261006.md)
converts retained `func_1513FFF4`: all 55 direct words/frame eight, existing
O2/g3, no guards/profile/shared header/data. Owner-local void/pointer/byte
prototype and constructor call recovered; constructor's 114 words unchanged.
Unsigned dimension underflow, variant corner stores, index-255 no-access gate
and captured dimensions qualified with 40 controls, 8192 two-body guest cases,
65536 byte-pair cases, 15 no-access cases, 256 two-body aliases, 589824 native
helper and 131072 connected native cases. 1536 two-body actual constructor/
helper cases cover all 169 chain words. All 6059 linked slots are identical
to the assembly checkpoint; protected sections/720 owners/10660 guards intact.
48 owner warnings unchanged, zero new. Converted total 5463/6042, Game
4790/5321; exact total 3325/5463, Game 2652/4790, zero drift, 2138 different.
All 52 focused post-link tests pass in 713.368 seconds, no skips.
Next inspect retained 48-word
`func_151400D0` vertex-attribute helper; no full backend/hardware/gameplay/
host adoption, sibling source/build/save/frozen Release change or push.

Source effect constructor direct match:
[Note 1046](WORKING_NOTES/1046-game-source-effect-constructor-direct-match-20261006.md)
recovers `func_1513D2F0`: all 114 words directly, frame 0x38, existing O2/g3;
no new guards/profile/shared header/data. Captured allocator flags, live
88-byte descriptor copy, helper setup, default sentinel and inclusive live
view bound. 97 compiler controls, 6912 two-body guest cases, 2048 width
cases, 18 two-body raw-default cases, 576 actual-wrapper guest cases,
131072 native constructor and 576 connected native cases. All 114 words
covered; wrapper/constructor path covers 204 reachable words. Only target
changes across 6059 fixed slots; protected sections/720 owners/10660 guards
intact. The owner's 48 preexisting warnings are unchanged; zero new warnings.
Total 3324/5462, Game 2651/4789 exact, zero drift, 2138 different.
All 43 focused post-link tests pass in 487.777 seconds, no skips. Constructor no longer a
placeholder; backend helpers remain callbacks in qualification. Next inspect
raw-assembly helper `func_1513FFF4`, not full gameplay/host acceptance.
No sibling source/build/save/frozen Release change or push.

Source-backed effect packet direct match:
[Note 1045](WORKING_NOTES/1045-game-source-effect-packet-direct-match-20261006.md)
recovers `func_1519ED84`: all 96 words directly, frame 0xA0, existing O2/g3;
no guards/profile/shared header/data edits. 88-byte packet preserves five
alignment bytes; twelve-argument handoff and conditional pointer publication.
98 compiler controls, 3456 three-body guest cases, 65536 width/byte-pair
sweeps, 128 three-body float cases, 576 connected-placeholder cases,
131072 opaque native and 192 actual-consumer native cases. Linked audit:
only target changes across 6059 fixed slots; protected sections/720 owners/
10660 guards intact; owner diagnostics empty. README total 3323/5462,
Game 2650/4789 exact, zero drift, 2139 different. All 34 focused post-link
tests pass in 497.803 seconds, no skips. Constructor `func_1513D2F0` still a placeholder; consumer
`func_1519EF04` remains exact. Next recover that 114-word constructor;
no complete gameplay/host claim, sibling/frozen Release change or push.

Source-backed actor packet recovery:
[Note 1044](WORKING_NOTES/1044-game-actor-source-packet-byte-match-20261006.md)
recovers `func_1519EB8C`: 102 words/frame 0xB8, semantic C with 14 guards
for a closed opening schedule, existing O2/g3. No new profile/shared header/
data. 124-byte descriptor preserves eight alignment bytes; conditional
source-pointer payload publication. 56 controls, 3456 three-body guest cases,
65536 halfword sweeps, 384 float-boundary cases, 131072 opaque native and 192
actual-constructor native cases. Linked audit passes: only target changes
across 6059 fixed slots; protected sections and 720 data owners stay intact.
10660 guards, exactly 14 new target rows; owner diagnostics empty. README
total 3322/5462 (60.82%), Game 2649/4789 (55.31%) exact, zero drift,
2140 different. All 56 focused post-link tests pass in 281.571 seconds,
no skips.
Constructor remains semantic/non-matching, not complete backend/hardware/
gameplay/host adoption. Next `func_1519ED84`. No sibling/Release change or push.

Effect-configuration packet direct match:
[Note 1043](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md)
recovers `func_1519EA78`: all 69 words directly, frame 0x70, existing O2/g3;
no new guards/profile/shared header/data. Complete 60-byte packet, unsigned
selector, separate float local and eight typed call arguments. 32 controls;
1296 two-body guest cases, 65536 width sweeps, 100 two-body raw-float cases
and 131072 native cases. All 69 words covered. Only target changes across
6059 slots; protected sections/720 owners/10646 guards intact. Owner
diagnostics empty. README total 3321/5462, Game 2648/4789 exact; zero drift,
2141 different. All 26 focused post-link tests pass in 219.250 seconds,
no skips. The 228-word `func_15152190` callee
is still a C placeholder; no complete effect-path/gameplay/host claim.
Next `func_1519EB8C`'s actor packet. No sibling/frozen Release change or push.

Address-record allocator direct match:
[Note 1042](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md)
recovers `func_1519E970`: all 37 words directly, frame 0x20, existing O2/g3;
no new guards/profile/shared header/data. Seven typed arguments, pointer
return, retained allocator/list linking and ordered payload stores. 48
controls; 1152 cases each in three two-body guest modes, 65536 selected width
sweeps and 131072 native cases. All 85 chain words covered. Only target
changes across 6059 slots; protected sections/720 owners/10646 guards intact.
Owner diagnostics empty. README total 3320/5462 and Game 2647/4789 exact,
zero drift, 2142 different. All 77 focused post-link tests pass in 468.864
seconds, no skips. Next `func_1519EA78`'s
configuration-packet wrapper. No complete caller/FCSR/gameplay/host adoption,
sibling/frozen Release change or push; Game remains active.

Conditional packet allocator direct match:
[Note 1041](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md)
recovers `func_1519E6BC`: all 38 words directly, frame 0x38, existing O2/g3;
no new guards/profile/shared header/data. Post-cleanup global gate, failure
publication and captured 12-byte packet with three untouched alignment bytes.
24 controls; 3072 cases each opaque/connected-cleanup/connected-allocation,
two bodies, plus 1536 selected code-byte sweeps and 18432 native cases.
138 reachable chain words execute; 140 linked words bound. Only target changes
across 6059 slots; protected sections/720 owners/10646 guards intact.
Baseline/current owner diagnostics empty. README total 3319/5462 and Game
2646/4789 exact, zero drift, 2143 different. All 71 focused post-link tests
pass in 369.862 seconds, no skips. Next
`func_1519E970`'s seven-argument record allocator. No complete caller/FCSR/
gameplay/host adoption, sibling/frozen Release change or push; Game stays active.

Random selector/output direct match:
[Note 1040](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md)
recovers `func_1518E5D8`: all 37 words directly, frame 0x18, existing O2/g3;
no new guards/profile/header/data. Seven-pointer ABI and ordered output stores;
retained selector's third RNG and sequential palette reads remain intact.
24 compiler controls; 4096 opaque / 16384 connected-selector / 8576 fully
connected guest cases and 14528 native cases. All 86 wrapper/helper/RNG words
covered. Whole linked audit: only target changes across 6059 slots;
protected sections/720 data owners/10646 guards unchanged. Four owner warnings
match baseline. README now total 3318/5462 and Game 2645/4789 exact, zero
drift, 2144 different. All 65 focused post-link tests pass in 310.324 seconds,
no skips. Next
`func_1519E6BC`, conditional allocator/packet wrapper still a stub. No complete
caller/FCSR/gameplay, sibling/frozen Release change or push; Game stays active.

Actor position-queue wrapper direct match:
[Note 1039](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md)
recovers `func_1517D5FC`: all 37 words directly, frame 0x28, existing O2/g3;
no new guards/profile/header/data. Signed coordinate ABI, actor stride/float
capture and shifted selector. 32 controls; 24576 opaque / 37936 connected
guest cases, 8192 opaque / 49152 connected native cases. All wrapper/helper
words covered; retained 33-word helper and its 29 old guards unchanged.
All 59 post-link tests pass in 255.215 seconds, no skips.
Only target changes across 6059 slots; protected sections/720 owners/10646
guards intact. Baseline/current owner diagnostics empty. README now total
3317/5462 and Game 2644/4789 exact, zero drift, 2145 different. Next
`func_1518E5D8`, RNG/selector/output wrapper still a stub. No complete caller/
FCSR/gameplay, sibling/frozen Release change or push; Game stays active.

Alternate actor-dimension direct match:
[Note 1038](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md)
recovers `func_1515C244`: 41 direct C words plus two retail padding words,
complete 43-word slot exact under existing O2/g3. No frame/guards/profile/
header/data change; local signed +0xE8 cast preserves the shared unsigned field.
16 controls; 43008 two-body guest cases / 21504 native cases. Forty reachable
words execute, impossible delay and padding structurally bound. All 52
post-link tests pass in 228.619 seconds, no skips. Only target
changes across 6059 slots; protected sections/720 owners/10646 guards intact.
Baseline/current owner compiles have empty diagnostics. README now total
3316/5462 and Game 2643/4789 exact, zero drift, 2146 different.
Next `func_1517D5FC`, 37-word coordinate/actor queue wrapper still a stub.
No full callers/FCSR/gameplay, sibling/frozen Release change or push.

Actor-dimension/position direct match:
[Note 1037](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md)
recovers `func_1515C1A0`: all 41 words directly, no frame/guards/profile/data
change. Real actor/point layouts, signed dimensions/vertical offset and
ordered overlapping outputs. 16 compiler controls; 36864 two-body guest
cases / 18432 native cases. Forty reachable words execute; one unreachable
delay word is structurally bound. All 47 post-link tests pass in 193.845
seconds, no skips. Only target changes across 6059 slots; protected
sections/720 owners/10646 guards intact. Both baseline/current
owner compiles have empty diagnostics. README now total 3315/5462 and
Game 2642/4789 exact, zero drift, 2147 different. Next `func_1515C244`,
the adjacent signed +0xE4/+0xE6/+0xE8 twin. No full callers/FCSR/gameplay,
sibling/frozen Release change or push; Game matching stays active.

Projection-wrapper investigation:
[Note 1036](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md)
banks 20 O2/g3 controls for `func_15144CEC`; none matches the 101-word retail
slot/frame 0x48. All candidates use frame 0x50. The 58-word synthetic-return
matrix helper chain is linked retail-exact. Three compiler/identity tests pass
in 14.634 seconds, no skips; no execution/alias qualification or source install.
All 6059 slots/protected sections/720 data owners/10646 guards unchanged;
matching totals remain 3314/5462 total, 2641/4789 Game, zero drift.
Next inspect `func_1515C1A0`; projection and pair-clamp frames remain open.
No sibling/frozen Release change or push; Game matching stays active.

Descriptor shape-measure direct match:
[Note 1035](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md)
recovers `func_1514462C` across all 56 words directly under existing O2/g3,
no frame/guards/profile/data change. Pointer prototype and two float externs
replace the stub's false integer-address signature. 48 compiler controls;
21504 three-body guest cases and 10752 native cases cover signed dimensions,
all flag bytes, wrapped product and ordered float rounding. All 55 reachable
retail words execute; the one unreachable load is structurally bound.
All 58 combined tests pass in 94.861 seconds, no skips.
Only target changes across 6059 slots; protected sections/720 owners/10646
guards intact despite header-triggered rebuild. Three owner warnings equal
the independently compiled baseline source and headers. README now total
3314/5462, Game 2641/4789 exact, zero drift, 2148 different. Next inspect
101-word `func_15144CEC`, still a zero-return projection-wrapper placeholder.
Pair-clamp frame remains open. No full callers/gameplay/FCSR, sibling/frozen
Release change or push; Game matching remains active.

Pair-clamp backend audit:
[Note 1034](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md)
banks nine locally evidenced O2/g3 uopt controls. All accepted with empty
diagnostics; none recovers the saved-pointer frame or reduces 36 differences.
Seven emit the same body, one changes a closed three-word temporary lifetime,
one emits 35 words with caller-home copies. No production/profile/data/guard
or aggregate change. All nine pair tests pass in 35.646 seconds, no skips.
Next recovery candidate: adjacent `func_1514462C`,
still a zero-return placeholder; its isolated semantic form emits all 56
retail words directly, pending qualification and linked installation.

Pair-clamp register-lifetime follow-up:
[Note 1033](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md)
banks 128 further compiler controls after `fe925393`: separate parameter/local
register hints do not recover `func_15143D18`'s frame. All O2/g3 bodies equal
the committed 29-word recovery; O1/g3 bodies are oversized with frame 0x20.
1536 guest corner runs preserve ordered access traces and footprints;
all 51 combined tests pass in 93.572 seconds, no skips. All 6059 slots,
protected sections/720 owners/10646 guards equal the committed checkpoint.
No production/guards/profile/data or aggregate-count change. Continue the
saved-pointer allocation/frame and branch-likely/shared restore tail.
This function remains non-matching at 36 aligned differences; Game stays active.

Integer pair-clamp access recovery, still non-matching:
[Note 1032](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md)
recovers `func_15143D18`'s ordered XOR exchange and sequential endpoint clamps.
29 emitted words, frame zero, seven padding words in the 36-word slot;
all 36 aligned words still differ. No guards/profile/header/data change.
92 compiler controls find no exact body. 24576 guest cases cover all retail
words; the old body agrees on final outputs but differs in 7168 access traces.
12288 native cases pass; all 50 combined tests pass in 64.519 seconds, no skips.
Only target changes across 6059 slots; protected
sections/720 owners/10646 guards intact. Three owner warnings equal baseline.
README aggregates remain total 3313/5462 and Game 2640/4789 exact, zero drift,
2149 different. Next: this function's saved-pointer frame/register lifetimes
and branch-likely return tail. No gameplay/caller-domain expansion, sibling
or frozen Release change or push. Game matching remains active.

Indexed state-save direct match:
[Note 1031](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md)
recovers `func_15123934` across all 38 words directly from C, frame 0x18,
real actor/header definitions, no guards/profile/data change. Correct 2/4-byte
indexing, sequential overlapping saves, callback argument and pre-call mark.
32 compiler controls; 7680 opaque / 4736 connected three-way cases, six
zero-mask non-returning prefixes and 2520 native cases. All wrapper/callback
words covered; unchanged production callback already 14/14 exact. All 43
tests pass in 48.052 seconds, no skips. Only target changes across 6059;
protected sections/720 owners/10646 guards intact. Five owner warnings
verified identical to baseline. README: total 3313/5462, Game 2640/4789 exact,
zero drift, 2149 different. Next: `func_15143D18`, existing 24-word C versus
36-word retail XOR-swap/clamp, 36 differences. Full gameplay/callers/valid
domain expansion remain unqualified. No sibling/frozen Release change or push.

Random-reload timer direct match:
[Note 1030](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md)
recovers `func_150D26F0`: all 39 words directly under existing O2/g3, frame
0x20, no new guards/profile/data. Typed record fixes the array body's 14
differences. 76 compiler controls; 896 gate / 1920 reload / 48 trap three-way
cases and 1408 native cases cover every retail word. Preserve wrapped timer
subtraction, unsigned remainder, post-callback fields and break 7. All 35
tests pass in 20.151 seconds, no skips. Only timer changes across 6059 slots;
protected sections/720 owners and all 10646 guards intact. README: total
3312/5462, Game 2639/4789 exact, zero drift, 2150 different. Next: recover
38-word `func_15123934`'s indexed field-save/update/callback pass. Full
dispatcher/RNG/gameplay and hardware trap delivery remain unqualified.
No sibling/frozen Release change or push; Game matching goal stays active.

Float-reference packet wrapper direct match:
[Note 1029](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md)
recovers `func_150C2804`: all 37 words directly from C under existing O2/g3,
frame 0x38, no guards/profile/data/header change. 24 compiler controls;
2304 opaque and 256 float-pattern three-way cases, 288 connected-retail-callee
cases and 14400 native cases. Full wrapper/callee word coverage; live inspection
confirms the unchanged production callee already matches all 50 retail words,
superseding the stale placeholder claim below. All 92 tests pass in 233.716
seconds; eight packet tests rerun with the callee assertion pass in 6.375
seconds, no skips. Only this slot changes across 6059; all protected
sections/720 owners and 10646 guards unchanged. README: total 3311/5462,
Game 2638/4789 exact, zero drift, 2151 different. Next: inspect 39-word
`func_150D26F0`, still a placeholder. No gameplay/
FCSR/complete allocator, sibling/frozen Release or push claim.

Linked-record position tail match:
[Note 1028](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md)
closes `func_150E6FAC` across all 72 retail words using three expected-word /
empty-relocation guards and one saved-RA insertion. Raw C remains 71 words
with 15 aligned differences; no source/profile/frame change. 3360 three-way
guest cases, all reachable retail words, independent emitter/stale-anchor
checks. Only this slot changes across 6059; protected sections/720 owners and
all old guards intact. All 84 tests pass in 267.948 seconds, no skips.
README: total 3310/5462 and Game 2637/4789 exact,
zero drift, 2152 different. Next ordinary candidate: `func_150C2804`, 37-word
packet dispatcher still a placeholder. Edge helper remains at 102 differences.
No full gameplay/FCSR/helper implementation, sibling/frozen Release or push claim.

Graph edge crossing scope audit:
[Note 1027](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md)
rejects 101 scope/plane/aggregate/operand controls without improving the
102-difference helper. All 6059 slots match the prior checkpoint; no production,
guard, profile or data change. Counts/README unchanged. Next inspect closest
remaining C match `func_150E6FAC`'s return tail. The edge helper remains open;
no full-chain/FCSR/gameplay, sibling/frozen Release or push claim.

Graph edge crossing lifetime improvement:
[Note 1026](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md)
improves `func_15086D94` from 151 to 102 real differences. All 207 words now
emit from C without padding; frame 0x80 still differs from retail 0x90.
The saved prefix and complete outer-loop tail match directly, with one count
load. 209 new controls; qualification now compares retail and three C bodies
across 2177 cases, plus 288 native footprints; all 62 tests pass, no skips.
Only the helper changes across
6059 slots; root/parent, protected sections, 720 owners and 10643 guards intact.
README/counts unchanged: Game 2636/4789 exact, zero drift, 2153 different.
Next: frame/minimum home and normal/side/constant lifetimes. Full helper-chain/
FCSR/gameplay acceptance remains separate; the Game matching goal stays active.

Graph edge crossing semantic recovery:
[Note 1025](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md)
replaces `func_15086D94`'s zero-return placeholder with its complete horizontal
crossing pass. Not byte-exact: 206 body words / 207-word slot, frame 0x78,
151 differences. Preserve retail's last-fraction result and 100.0f initial
minimum. Thirty-nine forms / 78 controls; 2177 three-way guest cases, 198/207
retail words exercised, 288 native footprints; all 58 combined tests pass,
no skips. Only the helper changes across
6059 slots; root/parent, protected sections, 720 data owners and 10643 guards
unchanged. README/counts stay 3309/5462 total and 2636/4789 Game exact, zero
drift, 2153 different. Next: helper frame/private homes and normal lifetimes;
parent remains at 282 differences. Full helper-chain/FCSR/gameplay acceptance
is still separate. Its 151-difference checkpoint is superseded by Note 1026
above; the Game matching goal remains active.

Root neighbor lookup direct match:
[Note 1024](WORKING_NOTES/1024-game-root-neighbor-lookup-direct-match-20261006.md)
recovers `func_15085DF8` across all 168 words directly from C, frame 0x80,
no guards/profile/overflow. Seventy controls; 3275 three-way guest cases,
166 executable words (two always-annulled retail delays), 1536 native cases.
All 45 lookup/parent/lifetime/visitor tests pass, no skips. All 6059 addresses/
lengths survive; only lookup and the five-float geometric placeholder ABI
change. Parent bytes and protected sections/720 owners/all guards unchanged.
README aggregates updated: 3309/5462 total, 2636/4789 Game exact, zero drift,
2153 different. Its still-placeholder geometric-helper boundary is superseded
by Note 1025 above; neither helper nor parent is matched. Full geometry/
lookup/caller/gameplay and FCSR acceptance remain separate.

Zone/player selection lifetime improvement:
[Note 1023](WORKING_NOTES/1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
retains the typed query pointer in `func_1508B3F8`: 369 emitted words, no padding,
frame 0x140; differences fall from 340 to 282. Still not byte-exact. No new
guards/profile/assembly/overflow or query enlargement. Ninety-one additional
controls; 2990 four-way guest cases, full parent/visitor coverage and 1424
native footprints. All 17 qualification/lifetime and 13 visitor regression
tests pass. Only parent changes across 6059 slots; protected sections, all
720 Game-data owners and 10643 guards intact. README/counts unchanged.
Next: retail query/private homes and saved address lifetimes; retained
370-word / 233-difference control remains oversized and uninstalled.
The lookup-placeholder boundary at that checkpoint is superseded by Note 1024
above; full helper-chain/gameplay remains unqualified.

Zone/player neighbor selection semantic recovery:
[Note 1022](WORKING_NOTES/1022-game-zone-neighbor-selection-recovery-20261006.md)
replaces `func_1508B3F8`'s placeholder with the complete parent pass. Not a
byte match: 367 body words plus two padding nops, frame 0x140, 340 differences.
No new guards/profile/assembly/overflow. 58 controls; 2990 three-way guest
cases, all 369 parent / 84 connected visitor words and 1424 native footprints.
14 qualification and 60 shared-oracle regression tests pass, no skips.
Audit preserves all 6059 slot addresses/
lengths: only parent and four argument homes in the still-placeholder root
lookup change. Protected sections/720 data owners and all guards intact.
Counts/README aggregates unchanged: Game exact 2635/4789, zero drift.
Next: parent query homes/address lifetimes; a retained 370-word / 257-difference
form exceeds the slot by one word. Full lookup/caller/gameplay unqualified.

Recursive record-neighbor visitor byte match:
[Note 1021](WORKING_NOTES/1021-game-record-neighbor-visitor-match-20261006.md)
replaces `func_1508B2A8`'s zero-return placeholder with its complete 84-word
recursive X/Z threshold visitor. Frame 0x30 and five saved-register lifetimes
match; six guards normalize two complete V0-to-V1 temporary lifetimes.
No compiler override, insertion/omission or assembly edit. Twenty-four controls
complete; 13 qualification tests and 49 focused regressions pass, no skips.
4096 leaf and 4608 recursive three-way cases, full instruction coverage,
2304 native footprints, signed-count and physical-alias checks preserve the
retail mask collisions, strict threshold and fresh count/global reads.
Only target changes across 6059 slots; protected sections/720 data owners and
all 10637 older guards unchanged. Counts: 3308/5462 total, 2635/4789 Game
exact, zero drift, 2154 different. README aggregates updated. Next: inspect
parent `func_1508B3F8`; full parent/FCSR/gameplay remains unqualified.

Record dispatcher direct match:
[Note 1020](WORKING_NOTES/1020-game-record-dispatcher-direct-match-20261005.md)
closes `func_15040CC8` across all 38 words, removing its overflow trampoline.
Integer record ABI plus divide-by-one index update retain retail's signed
index, three saves and frame 0x28; no divide, guards or profile override.
45 controls, 12288 three-way guest cases and full instruction coverage;
16 matching/native tests and 39 shared-oracle regressions pass, no skips.
Audit removes only the target overflow symbol: 16 later bodies shift by
-156 bytes with identical hashes; 13 trampolines only retarget their first
jump word. All other surviving slots/lengths and retail addresses intact.
Protected sections/720 data owners and all 10637 older guards unchanged.
Counts: 3307/5462 total, 2634/4789 Game exact, zero drift, 2155 different.
README aggregate tables updated; callback bodies/timing/gameplay unqualified.
Continue Game matching; 1508B2A8 is an 84-word recursive visitor placeholder.

Position/radius append direct match:
[Note 1019](WORKING_NOTES/1019-game-position-radius-append-direct-match-20261005.md)
replaces `func_1508B20C`'s false zero-return placeholder with all 39 words
emitting directly from semantic C. Signed count, post-increment, truncated
XYZ and squared radius preserve five fresh base reads and store order.
No guards, header/profile/assembly change. All 34 compiler controls complete;
nine qualification tests pass, including 8192 three-way guest cases,
252 bounded actual-caller cases and 65536 native cases. All 39 words covered.
Only target changes across 6060 slots; protected sections/720 data owners
and all 10637 older guards remain intact. Another 57 regression tests pass.
Counts: 3306/5462 total, 2633/4789 Game exact, zero drift, 2156 different.
README aggregate tables updated; full caller/FCSR/gameplay unqualified.
Continue Game matching; 15040CC8 needs a new saved-register/loop lifetime
shape, while the triangle read/frame boundary remains open under 1017.

Actor context dispatcher byte match:
[Note 1018](WORKING_NOTES/1018-game-actor-context-dispatcher-byte-match-20261005.md)
closes `func_15044380` across all 107 words. A per-visit enable pointer
recovers frame 0x68 / saved context +0x5C; 15 relocation-aware guards close
one complete allocation cycle, independent initialization schedule and
commutative add. Nineteen controls; 6184 three-way guest cases cover all
107 instructions. Nine matching tests pass, no skips. Only target changes
in 6060 slots; all protected sections and 720 data owners remain exact.
Counts: 3305/5462 total, 2632/4789 Game exact, zero drift, 2157 different.
README aggregate tables updated; helper-chain/gameplay acceptance not claimed.
Continue Game matching; triangle read/frame lifetimes remain open under 1017.
All 320 affected-slice tests pass in 57.212 seconds, no skips; tools,
whitespace and 2982 relative links pass. All 19 compiler controls reproduce.

Triangle cached-iterator audit:
[Note 1017](WORKING_NOTES/1017-game-actor-triangle-cached-iterator-audit-20261005.md)
banks 78 controls and 1914 bounded comparisons. Cached reads recover 1/1,
but lower raw scores require 0x150-0x160 frames; mixed bounds exceed the
slot. None is installed. Production, counts and README are unchanged.
Next Game target: `func_15044380`'s 107-word frame/register match.

Triangle reduced-frame recovery:
[Note 1016](WORKING_NOTES/1016-game-actor-triangle-reduced-frame-and-read-lifetime-screen-20261005.md)
reduces `func_1502F490` from frame 0x160 / 273 differences to 0x140 / 242.
All seven retail array homes remain intact; all 302 body/slot words emit
without new guards/profile/padding. Still non-matching: retail frame is
0x138, and the actor argument plus early ID/count read lifetimes differ.
Seventy-seven controls include 4488 bounded comparisons; scope-only forms
do not reduce the frame, and frame-only forms do not match the body.
64 focused tests and the five final frame probes pass, no skips; only target
changes in 6060 slots. Protected sections/data/CSV and README totals stay
intact. Next: last eight frame bytes, original read and SDK-loop lifetimes.
All 367 regression tests pass in 527.136 seconds, no skips; includes the
final read-history probe. Tools, staged whitespace and 2993 relative links
pass. This is not full read-lifetime/hardware or PC gameplay acceptance.

Triangle private-home recovery:
[Note 1015](WORKING_NOTES/1015-game-actor-triangle-private-home-recovery-20261005.md)
recovers all seven retail array homes by declaration-only changes. Installed
`func_1502F490` improves from 275 to 273 differences; 298 / 302 words, frame
0x160 still wrong versus retail 0x138. No array enlargement, added padding, guards
or profile change. Thirty-six declaration/loop controls include 1848 bounded
comparisons; oversized cursor forms are not installed. Only target changes
in 6060 slots; protected sections/data owners and CSV remain intact.
README/counts unchanged. Next: excess reserved homes and SDK-loop lifetimes
while retaining the now-correct array placement. Not a new exact function.
All 60 focused tests pass in 269.380 seconds; the 362-test regression corpus
passes in 818.122 seconds, no skips. Tools, staged whitespace and all 2983
checked relative links pass. Fresh live ELF agrees with the accepted slots.

Triangle lifetime/first-match audit:
[Note 1014](WORKING_NOTES/1014-game-actor-triangle-lifetime-and-overlapping-range-audit-20261005.md)
banks 34 controls; 29 fitting forms pass 1914 bounded guest comparisons.
Frames 0x148/0x138/0x130 alone do not recover retail allocation or fitting
length. An initialized-weight form has 274 differences but remains a
limited-qualified candidate, not an installed fix. The explicit overlapping-
range gate now passes and rejects last-match overwrites; native references
expand to 64512 plus 33 aliases. Production/README counts are unchanged.
Next: reserved homes and mixed scalar/array placement, preserving original
argument spills and separate early/SDK pointer lifetimes.
All 57 focused checks pass in 309.237 seconds, no skips; tools, whitespace
and 2981 links pass. All 6060 slots and protected sections/data owners stay
unchanged or retail-exact; the prior full corpus is not rerun in this audit.

Post-checkpoint triangle layout audit:
[Note 1013](WORKING_NOTES/1013-game-actor-triangle-layout-screen-20261005.md)
banks ten array/output-cursor forms and 120 bounded guest comparisons after
`623b96ae`. None improves the installed 298-word/frame 0x160/275-difference
transform. Reordering changes bytes, not these metrics; explicit XYZ cursors
grow to 308 words and are not installed. Production/README counts remain
unchanged. Next: actual spill/first-use lifetimes and edge/matrix-loop shapes.

Actor triangle remap: [Note 1012](WORKING_NOTES/1012-game-actor-triangle-remap-semantic-recovery-and-matrix-tail-restoration-20261005.md)
replaces `func_1502F490`'s placeholder with complete semantic C: 298 body /
302 slot words, frame 0x160, 275 differences; retail frame is 0x138.
The required 40-word matrix leaf is restored to original assembly, preserving
the retained tail's A0/T9/F0/F2/F4 interface. This is not a new C byte match.
All 53 focused tests pass; 1715 three-way guest cases, 57344 native reference
cases and 33 native aliases include actual phase/matrix/tail connections.
Only these two slots change in 6060; protected sections, 720 data owners and
CSV stay intact. Counts: 3304 / 5462 total, 2631 / 4789 Game, zero drift,
2158 different. Conversion falls by one when false C becomes retained ASM.
README aggregates updated. Next: transform frame/array/loop byte matching.
No full hardware-FPU/PC gameplay claim or sibling/frozen Release change.
All 355 combined tests pass in 829.704 seconds, no skips; tools, whitespace
and 2965 relative links pass. The C transform remains non-matching.

Actor buffer copy: [Note 1011](WORKING_NOTES/1011-game-actor-buffer-copy-direct-match-20261005.md)
recovers `func_1502F948`'s ordered gates, cached ID, allocation ABI and fresh
copy inputs. All 45 words / frame 0x28 emit directly under default IDO;
no guards or compiler override. Qualification covers 13461 three-way guest
cases, 163840 native reference cases and 16384 native gate cases, including
bounded actual allocator-wrapper/SDK-copy connections. Only target changes
in 6060 slots; protected sections, all 720 data owners and CSV remain intact.
Counts now 3304 / 5463 total, 2631 / 4790 Game, zero drift; README aggregates
updated. Caller remains 109 differences. Next: `func_1502F490`'s complete
302-word semantic recovery, not just its already-qualified early return.
Heap-core/full transform/PC gameplay acceptance is not claimed.
All 41 focused checks pass in 173.674 seconds; all 343 combined checks pass
in 690.045 seconds, no skips. Tools, whitespace and 2955 relative links pass.
Conversion/47 retained Init ASM and sibling/frozen Release remain unchanged.

Actor reference coordinate phase: [Note 1010](WORKING_NOTES/1010-game-actor-reference-coordinate-phase-match-20261005.md)
recovers `func_1502F3C8`'s 25-slot scan, five-argument transform call and fresh
post-call Y/bound comparison. All 50 words / frame 0x30 are linked exact;
default IDO has 16 differences closed by relocation-aware prelude/register/
schedule guards. Only target changes in 6060 slots; protected sections and
all 720 Game-data owners remain exact. Counts now 3303 / 5463 total,
2630 / 4790 Game, zero drift. README aggregates updated. Caller remains
109 differences; transform owner remains a placeholder. Full transform/FPU
exception/gameplay acceptance is not claimed. Next: `func_1502F948`.
All 30 focused checks pass in 99.051 seconds and all 332 combined checks
pass in 374.293 seconds, no skips. Tools, whitespace and 2941 relative links
pass; conversion/Init ASM and sibling/frozen Release remain unchanged.

Actor pass lifetime audit: [Note 1009](WORKING_NOTES/1009-game-actor-pass-lifetime-audit-and-helper-handoff-20261005.md)
banks 176 reproducible compiler controls without changing production. None
improves `func_1502BEE4`'s 109 differences; correct stack homes or 176-word
length alone do not prove the retail schedule. Twenty focused checks pass in
47.471 seconds, no skips, including 48 new bounded guest comparisons.
README aggregates and linked baseline remain unchanged. Next: recover the
connected 50-word `func_1502F3C8` phase helper; caller matching remains open.

Game actor pass layout progress: [Note 1008](WORKING_NOTES/1008-game-actor-pass-array-layout-and-connected-selector-20261005.md)
reduces `func_1502BEE4` from 115 to 109 differing words, with 175 body / 176
slot words and frame 0x88. Depth/queue arrays now match SP+0x3C/SP+0x58 and
queue-count spill matches SP+0x38; maximum-depth spill remains SP+0x78, not
retail SP+0x34. No new guards/profile override. Nineteen focused checks pass,
including 400 new connections to the already-exact selector and dispatcher,
1171 total three-way cases and 16384 native reference cases. Only target
changes in 6060 slots; protected sections and patch CSV remain intact.
Counts stay 3302 / 5463 total, 2629 / 4790 Game, zero drift. README aggregates,
conversion/Init ASM and sibling/frozen Release unchanged. Next: remaining
maximum-depth spill, address lifetimes and retail instruction schedule.
All 321 combined checks pass in 289.549 seconds, no skips; tools and
whitespace checks pass. The function remains non-matching at 109 words.
All 2934 checked relative documentation links resolve.

Game actor update pass semantic recovery: [Note 1007](WORKING_NOTES/1007-game-actor-update-pass-semantic-recovery-and-captured-order-20261005.md)
replaces `func_1502BEE4`'s placeholder with live mask/activity scans,
predecessor-depth capture and stable ordered updates. It is not byte-exact:
174 body / 176 slot words, frame 0x88, 115 differences, no new guards/profile
override. All 771 three-way cases, including 257 actual connected dispatcher
cases, and 16384 native independent-reference cases pass. All 176 retail words
execute; wrong-shift/recheck controls fail and cyclic-prefix checks preserve
retail nontermination/wrapping. Seventeen pass/dispatcher focused checks pass,
no skips. Only target changes in 6060 slots; previous exact recoveries and
patch table stay intact. Rebuild: 3302 / 5463 overall, 2629 / 4790 Game, zero
drift. Conversion/47 Init ASM functions, README aggregates and sibling/frozen
Release unchanged. Next: finish this caller's stack layout and scheduling.
All 319 combined checks pass in 305.557 seconds, no skips; protected sections,
tools, whitespace and 2927 relative links pass.
After banking `981ec732`, eight further local-storage controls pass 64
boundary cases but do not improve the match. Eighteen focused checks pass
in 39.427 seconds; production remains unchanged at 115 differences.

Game actor update dispatcher direct recovery: [Note 1006](WORKING_NOTES/1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md)
recovers `func_1502BD84`, all 88 words / frame 0x20 directly under default
IDO, no guards/profile override. Callee inspection recovers the carried slot
argument to `func_1502EEF4`; the missing-slot negative control now fails the
ABI-aware fixture. All 5194 full three-way cases, 49152 native cases/two native
mutations and 48 actual callee prefixes pass. Nine focused tests, no skips.
Prefixes stop before the callee loop; full gameplay/update acceptance remains
separate. Only target changes in 6060 audited slots. Rebuild: 3302 / 5463
overall, 2629 / 4790 Game, zero drift. Protected sections/tools pass; patch
table, conversion/47 Init ASM functions and sibling/frozen Release unchanged.
README aggregates updated. All 311 combined checks pass in 257.161 seconds,
no skips; whitespace/relative links pass. Next: `func_1502BEE4`, 176-word
caller placeholder.

Game actor display-list scan recovery: [Note 1005](WORKING_NOTES/1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md)
recovers `func_1502BAD0`, all 173 words / frame 0x48. Default IDO emits the
semantic scan; eleven expected-word guards normalize a closed constant-register
cycle and equality operand order only. All 4868 three-way target cases and
194123 native cases pass, including signed alpha gates, live callback state,
full table/cursor chains and SDK packets. Thirteen focused tests pass, no skips.
All 172 reachable words execute; a retained dead load is proved unreachable
and byte-exact. Only target changes across 6060 slots; placeholder helpers/
callers remain unchanged, not qualified as full renderers. Rebuild: 3301 / 5463
overall, 2628 / 4790 Game, zero drift. Protected sections/tools/whitespace pass;
README aggregates updated. Conversion/47 Init ASM functions and sibling/frozen
Release unchanged. All 302 combined regression checks pass in 265.481 seconds,
no skips; touched relative links resolve. Next: `func_1502BD84`, 88-word actor
update dispatcher.

Game resource-size query direct recovery: [Note 1004](WORKING_NOTES/1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md)
recovers `func_1502B9B4`, all 69 body / 71 slot words and frame 0x68
directly under default IDO O2/g3, no guards/profile override. Three-u64
scratch, incoming descriptor at entry SP-0x14, both aligned-header choices
and live full-word DMA header result are preserved. Native qualification
uses positive descriptor-writing paths and explicit MIPS u64 alignment only.
All 5670 boundary, 972 actual lookup/cache, 384 native connected and 72
Init caller prefixes pass. The latter stops before bank load; full audio
startup is not claimed. Caller declaration aligned and all 214 slot words
stay retail-exact. All 6060 slots audited: only target changes.
Rebuild: 3300 / 5463 overall, 2627 / 4790 Game, zero drift.
Protected sections/tools/whitespace/links pass. All 272 combined checks
pass in 239.593 seconds, no skips.
README aggregates updated; conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502BAD0`, 173-word / frame 0x48
25-actor display-list routine in `game/generated_58F80.c`.

Game counted-pointer resource loader direct recovery: [Note 1003](WORKING_NOTES/1003-game-counted-pointer-loader-direct-match-and-full-caller-20261005.md)
recovers `func_1502B7F0`: all 60 words / frame 0x48 directly from default
IDO O2/g3, no guards/profile override. A for-loop update resolves the final
two store schedules. Private size, incoming descriptor at entry SP-0x14,
post-block output-home reread and final pointer-store/size-reload aliases
remain intact; native cases use positive descriptor-writing paths only.
All 1470 boundary, 162 actual-callee, 72 connected global-alias and 432 full
Game caller cases pass. Shared variadic declaration and sole active caller's
cast are aligned; its complete 112-word slot stays exact, including original
unsigned division/fallback behavior. All 6060 slots audited: only target
changes. Rebuild: 3299 / 5463 overall, 2626 / 4790 Game, zero drift.
Protected sections/tools/whitespace pass. All 261 combined checks pass in
217.336 seconds, no skips.
README aggregates updated; conversion/Init ASM, patch table and sibling/frozen
Release unchanged. Next: `func_1502B9B4`, size-query wrapper with compressed
header read and stack-phase-dependent alignment, 69 body words / frame 0x68.

Game optional-size resource loader direct recovery: [Note 1002](WORKING_NOTES/1002-game-optional-size-loader-direct-match-and-live-output-aliases-20261005.md)
recovers `func_1502B5C8` from its zero-return placeholder. All 61 words / frame
0x50 emit directly under default IDO O2/g3, no guards/profile override. The
incoming descriptor at entry SP-0x18 remains separate from the initialized-one
fallback at SP-0x10. Zero-depth seeds, live output/descriptor rereads and
distinct allocation-failure sizes are preserved; native tests qualify positive
descriptor-writing paths only, not defined native indeterminate-local behavior.
All 2940 boundary, 324 actual-callee, 72 connected global-alias and 108 full
Game caller cases pass. Six caller declarations/casts are aligned and complete
retail-exact slots/frames remain unchanged. Protected Init code/data, Debugger
code and Game data remain exact. All 247 final checks pass in 246.404 seconds,
no skips; tools/whitespace pass. Rebuild: 3298 / 5463 overall,
2625 / 4790 Game, zero drift. README aggregates updated; conversion/Init ASM,
patch table and sibling/frozen Release unchanged. Next: `func_1502B7F0`,
60 words / frame 0x48: stores a pointer through its first argument but returns
the separate size, unlike its obsolete commented void approximation.

Game buffer variadic wrapper direct recovery: [Note 1001](WORKING_NOTES/1001-game-buffer-variadic-wrapper-direct-match-and-incoming-descriptor-frame-20261005.md)
recovers `func_1502B8E0` from its zero-return placeholder. All 53 words / frame
0x48 emit directly under default IDO O2/g3, no guards/profile override. The
physical incoming descriptor at wrapper-entry SP-0x14 remains seed-sensitive
on zero depth; this preserves target instructions, not defined native C.
Native cases use positive depths with descriptor-writing lookup only.
All 2268 boundary, 600 actual-callee, 14 connected zero-depth and 48 full Game
caller cases pass; eight mismatch prefixes stop at the original syscall.
Both maintained caller slots/frames remain exact after prototype alignment;
`func_150169A0` is still a placeholder, so its assembly is reference-only.
Protected Init code/data, Debugger code and Game data remain exact.
All 232 final checks pass in 178.769 seconds, no skips; tools/whitespace pass.
Rebuild: 3297 / 5463 overall, 2624 / 4790 Game, zero drift.
README aggregates updated; conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502B5C8`, 61 words / frame 0x50,
including its optional size-output aliases and unwritten zero-depth descriptor.

Game caller-buffer resource-loader direct recovery: [Note 1000](WORKING_NOTES/1000-game-caller-buffer-resource-loader-direct-recovery-and-syscall-boundary-20261005.md)
recovers `func_1502B224` from its zero-return placeholder. All 75 words / frame
0x30 emit directly under default IDO O2/g3, no guards/profile override. Cap
rounding, raw DMA, compressed header capture/live scratch and retained decode
count are preserved. Native/boundary/600 actual-callee caller cases pass;
40 mismatch-prefix cases stop at the real handwritten syscall boundary.
Returning error hooks qualify only conditional continuation, not trap recovery.
All 221 final checks pass in 161.605 seconds, no skips; protected Init
code/data, Debugger code and Game data remain exact.
Rebuild succeeds: 3296 / 5463 overall, 2623 / 4790 Game, zero drift. README
aggregates updated; conversion/Init ASM, patch table and sibling/frozen Release
unchanged. Next: `func_1502B8E0`, 53 words / frame 0x48, retaining its verified
zero-depth incoming-frame descriptor dependency rather than initializing it away.

Game variadic table-address resolver recovery: [Note 999](WORKING_NOTES/999-game-variadic-table-address-resolver-recovery-and-connected-init-caller-20261005.md)
recovers `func_1502B020` from its zero-return placeholder. All 60 linked words
match with frame 0x48 and two checked independent loop-store guards, not a
direct compiler match. SDK argument consumption, initialized-one zero-depth
behavior and final output-store/descriptor-read order remain intact. Boundary,
actual lookup/cache hit/miss and connected retail Init sound-caller cases pass;
the latter covers 42/43 reachable caller words without faking an impossible
size-zero/nonzero-address result. Both Init callers use the recovered variadic
prototype; full rebuild retains Init exactness. All 210 final checks pass in
172.769 seconds, no skips; both caller slots and protected Init code/data,
Debugger code and Game data remain exact. Totals: 3295 / 5463 overall,
2622 / 4790 Game, zero drift. README aggregates updated; conversion/Init ASM
and sibling/frozen Release unchanged. Next: resource loader `func_1502B224`,
75 words / frame 0x30, including compressed-length mismatch handling.

Game variadic table-range wrapper recovery: [Note 998](WORKING_NOTES/998-game-variadic-table-range-wrapper-recovery-and-guarded-loop-stores-20261005.md)
recovers `func_1502B110` from its zero-return placeholder. All 69 linked words
match with retail's 0x48 frame and two checked independent loop-store guards;
raw C differs at those two stores only, no profile override. SDK varargs,
default root, descriptor masking/gates and unconditional final consumption
remain intact. All 8316 boundary and 200 actual-callee three-way cases pass,
alongside 1386 native boundary and 544 actual-C connected cases. Full consumer
rebuild succeeds. All 199 final checks pass in 148.664 seconds, no skips;
protected Init code/data, Debugger code and Game data remain exact.
Totals: 3294 / 5463 overall, 2621 / 4790 Game, zero drift.
README aggregates updated; conversion/Init ASM unchanged. Sibling/frozen
Release untouched. Next: recover SDK-varargs table-address resolver
`func_1502B020`, 60 words / 0x48 frame, with optional output alias gates.

Game table-range loader direct recovery: [Note 997](WORKING_NOTES/997-game-table-range-loader-direct-recovery-and-caller-qualification-20261005.md)
replaces `func_1502AF04`'s false zero-return placeholder with its semantic
DMA/in-place pair-offset body. All 71 words and the 0x40 frame emit directly
under default IDO O2/g3, no guards/profile override. Safe call-argument shape
avoids a rejected raw-exact unsequenced read/write trial. All 6336 native,
12672 instruction and 60 connected retail-wrapper cases pass; both stack
phases and buffer alignment/unsigned wrap contracts hold. All 190 final
checks pass, no skips, with protected sections exact after rebuilding.
Totals: 3293 / 5463 overall, 2620 / 4790 Game, zero drift. README aggregates
updated; conversion/Init ASM and patch table unchanged. Sibling/frozen Release
untouched. Next: recover variadic table-range wrapper `func_1502B110`,
69 words / 0x48 frame, retaining SDK varargs and descriptor-length gating.

Game cached lookup guarded match: [Note 996](WORKING_NOTES/996-game-cached-lookup-frame-and-guarded-miss-path-match-20261005.md)
matches all 159 linked `func_1502AC88` words. Address-parameter lifetime and
declaration order recover the full body, retail 0xA0 frame and exact cache-hit
path. Raw C still differs at twelve miss-path words; checked guards normalize
closed temporaries and equivalent buffer roundup on an 8-aligned N64 stack.
All 11088 three-way connected cases preserve ordered memory/call events and
returns; native 1056-case hit aliases and every omitted-guard control pass.
All 183 final combined checks pass, no skips; protected-section identity holds
after the full consumer rebuild. Totals: 3292 / 5463 overall, 2619 / 4790 Game,
zero drift. README aggregate tables updated; conversion/Init ASM unchanged.
Sibling/frozen Release untouched. Next: recover `func_1502AF04`'s 71-word
DMA table-range loader and in-place offset adjustment from its placeholder.

Game cache installer guarded match: [Note 995](WORKING_NOTES/995-game-cache-installer-alias-preserving-word-copy-and-guarded-match-20261005.md)
matches all 97 linked `func_1502AB04` words with the alias-preserving one-word
offset copy and 41 expected-word guards. Not a direct compiler match: raw C
fits the full slot and 0x28 frame but has 41 differences. Seven peel guards,
four bulk address-allocation guards and thirty bulk schedule/register guards
preserve all branches/calls and normalize only independent stores between
identical reads. All 2550 new three-way cases and every omitted-guard control
pass. The native partial-overlap rejection and 833-alias corpus remain intact.
All 176 final combined checks pass, no skips, with complete Init/Debugger/data
identity after the full consumer rebuild. Totals: 3291 / 5463 overall, 2618 / 4790 Game,
zero drift. README aggregate tables updated; conversion/Init ASM unchanged.
Sibling/frozen Release untouched. Next: cached lookup `func_1502AC88`,
158 / 159 body/slot words, 156 raw differences, 0xA0 frame in both forms.

Game cache installer frame recovery: [Note 994](WORKING_NOTES/994-game-cache-installer-frame-recovery-and-pair-copy-alias-gate-20261005.md)
recovers `func_1502AB04`'s complete 19-word prologue and 0x28 frame by preserving
an explicit count local across `bcopy`. Scalar pair copies remain intact.
Production still differs: 87 / 97 body/slot words, 74 differences instead of
93, no guards/profile change. The 128-form screen finds a raw-exact two-word
aggregate copy, but it fails a native partial-overlap witness and is rejected.
All 171 final combined checks pass, no skips; 833 bounded native aliases and
2550 three-way instruction traces preserve live reads and final cache memory.
The alias-preserving one-word-copy trial
fits 97 words with 41 differences but remains experimental. Exact/conversion
totals unchanged; README aggregate tables remain current. Sibling/frozen
Release unchanged. Next: qualify the word-copy scheduling differences or find
a directly matching scalar/word shape without weakening the alias contract.

Game block loader direct match: [Note 993](WORKING_NOTES/993-game-block-loader-direct-output-size-and-frame-match-20261005.md)
matches all 86 `func_1502B350` words directly under the unchanged default
IDO O2/g3 profile, including retail's 0x30 frame. Output-size expression shape,
explicit failure branches and one size local resolve all 78 prior differences;
no guards, profile override or interface changes. The 37-form / 296-trial
screen reproduces the match; all 165 combined checks pass, no skips.
Connected resource fixtures and complete Init/Debugger/data identity hold.
Totals: 3290 / 5463 overall, 2617 / 4790 Game, zero drift. Neighboring
relocator/variadic loader remain exact. README aggregate tables updated;
conversion/Init ASM and sibling/frozen Release unchanged. Next: 97-word
cache installer `func_1502AB04` (87 body words, 93 differences, frames 0x20/0x28).

Game offset relocator guarded match: [Note 992](WORKING_NOTES/992-game-offset-relocator-typed-scan-and-guarded-bulk-match-20261005.md)
matches all 72 linked `func_1502B4A8` words with a typed automatic-count scan
and seventeen checked bulk temporary-register guards. Not a direct compiler
match: raw C has seventeen differences, no frame or padding; the 186-form
screen finds no direct match. All 161 combined checks pass, including 5113
three-way relocation cases and every omitted-guard rejection control.
Full consumer rebuild and complete Init/Debugger/data identity hold.
Totals: 3289 / 5463 overall, 2616 / 4790 Game, zero drift; conversion/Init ASM
unchanged. The 77-word variadic loader remains directly exact. README aggregate
tables updated; sibling/frozen Release unchanged. Next: 86-word block loader
`func_1502B350` (77 body words, 78 differences, C/retail frames 0x38/0x30).

Game variadic loader direct match: [Note 991](WORKING_NOTES/991-game-variadic-resource-loader-direct-stack-match-20261005.md)
matches all 77 words of `func_1502B6BC`, including retail's 0x50 frame,
nullable-output prologue and private descriptor at sp+0x38. Separate fallback
selection and local declaration order resolve all seventeen differences
directly from C, with no guards/profile/interface changes. The 83-form screen
reproduces the result; all 155 combined checks pass, no skips, with actual
variadic/connected source fixtures and complete Init/Debugger/data identity.
Totals: 3288 / 5463 overall, 2615 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README aggregates updated; no host/frozen Release change. Next:
72-word offset relocator `func_1502B4A8` (65 body words, 71 raw differences).

Game attachment guarded match: [Note 990](WORKING_NOTES/990-game-attachment-walker-guarded-register-match-20261005.md)
matches the complete 45-word linked `func_15168E54` slot with nine expected-word
guards for a closed cursor/opcode allocation and equality operand order.
Unguarded C still differs at nine words; production source/profile are unchanged.
Thirty-six source forms do not directly match. All 154 combined checks pass,
including 1427 actual-leaf three-way traces, twenty mutation cases, 458752
native command cases and incomplete-allocation rejection controls. Full consumer
rebuild succeeds; complete Init/Debugger/data and recent direct matches hold.
Totals: 3287 / 5463 overall, 2614 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README updated; sibling already has this retail sequence, no host/
frozen Release change. Next: 77-word variadic loader `func_1502B6BC`.

Game resource helper match: [Note 989](WORKING_NOTES/989-game-resource-helper-address-word-direct-match-20261005.md)
completes all 46 words of `func_151336A8` directly from C. The inline unsigned
O32 address-word cast restores retail's final `v1`/`a1` handoff, without guards,
profile or public-interface changes. Three new checks reproduce nineteen source
forms and pin raw slot/neighbor identities. All 148 combined checks pass,
including actual resource/texture connections; complete Init/Debugger/data hold.
Totals: 3286 / 5463 overall, 2613 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README aggregates updated. Sibling already has this retail-sequence
helper; no host/frozen Release changes. Next near-match: `func_15168E54`.

Game immediate release match: [Note 988](WORKING_NOTES/988-game-immediate-texture-release-direct-frame-match-20261005.md)
completes all 46 words of `func_1510D7AC` directly from table-indexed C.
The captured signed priority remains; default O2/g3 now emits retail's 0x28
frame and ID spill/reload. No guards/profile/padding changes. A 51-variant
screen and three regression checks pin partial-frame rejection controls and
five unchanged neighboring spans; the existing full lifecycle suite retains
callback mutation and connected release/maintenance/reload qualification.
All 65 final combined checks pass, no skips; complete Init/Debugger/data stay exact.
Totals: 3285 / 5463 overall, 2612 / 4790 Game, zero drift; conversion and Init
ASM counts unchanged. README aggregate snapshot updated. Sibling still has
a placeholder, no host/frozen Release changes. Next near-match: `func_151336A8`.

Game cleanup rematch: [Note 987](WORKING_NOTES/987-game-nullable-cleanup-typed-pointer-direct-rematch-20261005.md)
restores `func_150F631C`'s complete nineteen-word direct C match. Typed pointer
fields recover four register/scheduling words against the current callee
prototype, with no guards or profile change. Five new checks cover 343 native
callback cases, an independent integer-field rejection control, raw retail
identity and six unchanged neighbors. Fresh totals: 3284 / 5463 overall,
2611 / 4790 Game, zero drift; conversion counts and Init ASM unchanged.
All 62 combined checks pass, complete Init/Debugger/data stay exact. README
aggregate snapshot updated; sibling/frozen Release unchanged. Next near-match
is the four frame/spill words in `func_1510D7AC`; light-selector gate stays open.

Game light-selector experiment: [Note 986](WORKING_NOTES/986-game-light-selector-candidate-fitting-and-connected-frame-witness-20261005.md)
recovers full fourteen-argument `func_1515D914` as experimental C. No-unroll
O2/g3 fits 2212 body / 2224 complete bytes in the 2404-byte slot, versus
default 2444 / 2448. All three profiles pass 17410 standalone pairs each;
192 retail-derived native cases and 168 caller-relative seed products hold.
However, twelve actual caller/callee witnesses expose the C renderer's
0xB8 versus retail 0x98 frame: a first directional light reads a different
physical seed, changes count 1 to 3 and moves the final cursor sixteen bytes.
Positional-first controls agree. All 109 final combined checks pass, no skips;
complete existing Init/Debugger/data remain exact. Keep the production stub.
Resolve connected stack lifetime before adoption; helper algorithms, hardware
and pixels remain open. README totals and sibling/frozen Release unchanged.

Init bitmap unsigned sentinel: [Note 985](WORKING_NOTES/985-init-bitmap-unsigned-one-past-record-fitting-20261005.md)
tests one-past unsigned stop arithmetic with ordered scalar and grouped-record
captures. No-unroll record C fits nineteen body words with no XOR, but sixteen
positions differ; store remains in the branch delay instead of the increment.
Whole text stays 80 bytes. Initial scalar read reversal is caught and fixed
experimentally with volatile views, at three words' cost. Fourteen new checks
qualify 1098 completed pairs and eighteen prefixes, including a wrapped zero
stop and a false-empty rejection control. All 154 combined checks pass, no skips;
48 old preprocessing selections and complete existing Init/data plus Game data
hold. No production adoption, README total or sibling/frozen Release change.

Init pause-resume decision: [Note 984](WORKING_NOTES/984-init-pause-resume-current-conversion-readiness-20261005.md)
freshly confirms 492 C / 47 ASM entries: seventeen investigation targets and
thirty intentional boot/SDK/hardware/context owners. No replacement is ready
for production adoption. Bitmap fits nineteen body words but differs at seventeen;
MMIO fits eleven but differs at nine O2/g3 or eight O1 words. Current connected
decoder is freshly reproduced at 4496 / 3984 bytes, 512 over; best formatter
connection remains 608 / 412, 196 over. Entry/frame/placement/stack gates remain.
All 140 fresh focused and byte-depth identity checks pass, no skips; complete
existing Init code/data and Game data remain exact. Bitmap loop/tail is the
first small target. Paused Game experiments, production owners, README totals
and sibling/frozen Release stay unchanged; this is not a production relink.

Game renderer: [Note 983](WORKING_NOTES/983-game-viewport-renderer-semantic-recovery-20261005.md)
recovers full `func_1510B9D0`, its public cursor/s16 interface and legacy caller
casts. C fits 347 / 356 words; frame 0xB8 versus retail 0x98, 343 differences,
no guards/profile override. Fourteen new checks qualify 5379 paired traces,
including 96 actual helper/updater/color/identity connections, 4608 native cases
and four invalid prefixes. Captured suppression/actor and late base/page/table
reloads hold under mutations. All 95 final combined checks pass in 52.200 seconds,
no skips, after shared-header rebuild/link; complete existing Init/Debugger/data
and caller/adjacent identities hold. Downstream transform/finalizer/effect
placeholders and submission/pixels remain open. README totals, Init owners and
sibling/frozen Release unchanged. Next full target: 601-word `func_1515D914`.

Game command helper: [Note 982](WORKING_NOTES/982-game-viewport-command-helper-semantic-recovery-20261005.md)
replaces `func_1510B7B4`'s placeholder with its complete twelve-packet SDK body.
It emits 103 / 105 words with two padding NOPs, no frame/calls/guards/profile
override; 104 raw differences remain. Twelve new checks qualify 65600 native
cases, 97 complete ordered retail/C traces and three invalid-input prefixes.
Late page/base/table aliases retain repeated reads; a cached-page control fails.
All 81 combined checks pass in 19.953 seconds, no skips, after fresh owner build,
padding and link. Complete existing Init/Debugger/data remain exact. README
totals and sibling/frozen Release unchanged. Note 983 above subsequently recovers
full renderer `func_1510B9D0`; these fixtures do not prove submission or pixels. Init still
has 47 ASM owners, seventeen investigation targets and thirty intentional.

Init bitmap grouped view: [Note 981](WORKING_NOTES/981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)
tests direct/local volatile record addressing for the captured start/end and
late signed count. Optimized body fits nineteen words while retaining the
two-based mask, but seventeen differ: XOR loop and original schedule remain
unresolved. Complete standalone text stays 80 bytes after alignment. Ten new
checks qualify 1002 completed ordered retail/C traces and twelve bounded prefixes,
including aliases, wrapping model addresses and unused-field read rejection.
All 138 final combined checks pass in 70.804 seconds, no skips; complete existing
Init slots/code/data and Game data remain retail-exact. All 44 old-shape host/
guest preprocessing selections hold. No original-type provenance or production
adoption is inferred. README, production sources and host/Release unchanged.

Init packed-width fitting: [Note 980](WORKING_NOTES/980-init-packed-bit-width-screen-and-restored-candidate-20261005.md)
screens a wide bit-count local and both packed fields on the byte-depth lead.
Optimized public builder saves one/three words, but trailing alignment absorbs
them: complete C/adapter allocation stays 4496 bytes. Both profiles gain eight
bytes of builder frame and call bound. Reject before semantic qualification;
restore the candidate exactly, no selector or test-code change retained.
All 83 fresh restored connected/native/owner/slot/call/reporting checks pass in
345.010 seconds, no skips. Complete existing Init code/data and Game data remain
retail-exact. Note 979's unchanged candidate retains its full masked corpus
evidence; discarded trial images receive none. Still 512 bytes over, with
entry/frame/private-stack/hardware gates open. Production, README and host/Release unchanged.

Init byte-depth full corpus: [Note 979](WORKING_NOTES/979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
qualifies the banked packed O2/g3 candidate across all 507 retail pages in each
masked CU1 mode: 1014 paired runs pass in 1604.214 seconds, no skips. Both
terminals report 4496 executable bytes, 3248 descent and 80-byte known-neighbor
clearance; this is not private-stack reservation proof. The instruction hash,
allocation and eight during-run source hashes hold. After receipt verification,
reporting-only failure gates and two mocked controls are added; all 32 supporting
checks pass in 1.483 seconds, no skips. The full corpus is not repeated for
that reporter-only change. No production adoption: still 512 bytes over retail,
with original entry/frame/placement, reservation and hardware gates open.
Init remains 492 C / 47 ASM: seventeen investigation targets, thirty intentional
owners. README totals, production sources and host/Release stay unchanged.

Init MMIO fitting: [Note 978](WORKING_NOTES/978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md)
tests a new volatile record view of the adjacent RAM publications. Direct
record text saves sixteen bytes versus the fully volatile scalar control in
three profiles, but still has nine O2/g3 or eight O1 word differences. Explicit
locals regress O1 to seventeen words/eight-byte frame. Nine new checks qualify
sixty ordered retail/C traces with no external reads and rejection controls for
store order, width and added reads. Retain the handwritten assembly; grouped
addressing is not original-type provenance or a closed register/schedule match.
Production declarations, owners, README totals and host/Release stay unchanged.
All 128 combined checks pass in 66.503 seconds, no skips; complete existing
Init slots/code/data and Game data remain retail-exact. No production relink
or hardware acceptance is claimed.

Init bitmap fitting: [Note 977](WORKING_NOTES/977-init-bitmap-all-ones-mask-fitting-and-retail-loop-boundary-20261004.md)
adds an opt-in unsigned all-ones mask and arithmetic control. The mask variant
fits nineteen optimized body words but has seventeen raw differences; IDO
rematerializes the constant, keeps the XOR loop and changes the retail tail.
Standalone optimized text stays 80 bytes: alignment absorbs the body word.
Reject adoption: this is size fitting, not a scheduling-only match. Nine new
checks qualify 1002 completed retail/C pairs and twelve prefixes; all 119
combined checks pass, no skips. Forty disabled-selector preprocessing checks
confirm unchanged Shapes 1..20. All existing Init slots/code/data and Game
data remain exact. Production owners, README totals and host/Release unchanged.
Next bitmap work must address the direct branch/increment delay and original
two-based tail, not another mask-only substitution. MMIO remains next small target.

Remaining Init decision: [Note 976](WORKING_NOTES/976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md)
retains 47 ASM owners: seventeen investigation targets and thirty intentional
boot/SDK/hardware/context routines. No replacement is ready. The new sixteen-
case byte-depth cache matrix improves neither complete text nor stack; a
persistent parent-mask recurrence grows O2 by 32 bytes and worsens O1 stack.
The recurrence source/selector are removed and banked source contents restored.
Best qualified decoder remains 4496 / 3984 bytes (512 over, actual adapter
included). Bitmap remains 20 / 19 words, MMIO full eleven-word match unresolved,
formatter connection 196 bytes over. Details and concrete adoption gates live
in the dedicated note. Fresh 78 decoder/owner/slot/call and 43 bitmap/MMIO/
formatter checks pass, no skips; all existing Init code/data and Game data
remain retail-exact. README totals and production owners stay unchanged.

Init byte-depth fitting: [Note 975](WORKING_NOTES/975-init-builder-byte-depth-induction-and-rejected-replication-helpers-20261004.md)
qualifies an opt-in byte-offset builder depth. Both packed profiles save sixteen
complete executable bytes: optimized C 4320 + actual 176-byte adapter = 4496,
512 over retail. Builder public/region is 330 / 398 words, frame 200, unchanged
400-byte core call bound and 3248 total descent. All 58 connected/native tests
plus twenty separate inventory/slot/call checks pass, no skips; ordered physical
table publications and both disabled packed hashes are checked. Aligned-end O2
grows sixteen bytes, so no default change. Two out-of-line replication helpers
regressed text/stack and were removed before semantic qualification. Production
Init remains 492 C / 47 ASM, all raw slots/full existing Init/data exact; no
README aggregate, production relink, full corpus, hardware or host/Release claim.
Next: another 512 complete bytes plus entry/frame/private-stack ownership.

Init decoder fitting: [Note 974](WORKING_NOTES/974-init-decoder-complement-low-mask-fitting-trial-20261004.md)
adds an opt-in complemented shared-mask expression. Two instruction words
change, but complete optimized text stays 4336 C + 176 adapter = 4512 bytes,
528 over retail. All 59 connected/native/ledger checks pass across two runs, no skips;
20 separate inventory/slot/call checks and tool checks pass. Default packed
instruction hashes remain intact; all 47 production ASM slots and complete
existing Init code/data plus Game data remain exact. The builder's 401-word
region contains a 333-word public unit and 68 embedded-helper words; next
sustained Init fitting is builder/shared-call structure and whole-image costs.
No adoption, production relink, full guarded corpus, README aggregate change,
sibling/Release change or hardware/gameplay acceptance is claimed.

Palette updater: [Note 973](WORKING_NOTES/973-game-palette-updater-and-connected-color-qualification-20261004.md)
recovers `func_1510CB10`: 168 / 170 words, retail 0x68 frame, 135 raw differences,
no guards/profile override/drift. Fourteen new checks qualify 398353 native cases,
1251 complete paired traces and three invalid-slot prefixes. Actual angle-helper/
updater/color/writer connections pass; captures, late reloads, byte-wrap-before-
clamp and both phase stores are retained. All 257 combined checks pass, no skips;
fresh source compile/padding/link preserves complete Init code/data, Debugger
code, Game data and previous identities. README aggregates unchanged. Next
full caller `func_1510B9D0` (356 words) is subsequently recovered in Note 983;
Note 982 recovers command helper `func_1510B7B4` (105-word slot).
Full renderer/RSP/RDP/natural effects and matching stay open.
Sibling already has updater plus gated diagnostics; no host/Release changes.

Palette color emitter: [Note 972](WORKING_NOTES/972-game-palette-color-emitter-byte-match-and-segment-connection-20261004.md)
finishes the interrupted `func_1510CDB8` recovery: all 42 words match directly
from actual SDK macros, frameless, no guards/profile override/drift. Six added
tests cover 262144 native alpha cases, 812 complete paired big-endian traces
and three invalid-index prefixes; actual color -> writer connections pass.
The complete module records 1710 paired traces. All 243 combined checks pass,
no skips, after forced source compile/padding/link/progress/matcher; complete
Init code/data, Debugger code and Game data remain exact. Total 3283 / 5463,
Game 2610 / 4790 exact, 2180 different, zero drift. README changes matching
aggregate rows only. Note 973 above subsequently recovers palette updater
`func_1510CB10` and qualifies its bounded color/writer connection.
Full render caller/RSP/RDP/natural effects and staged producer remain open.
Sibling already has the original emitter; no host/frozen Release changes.

Requested Init pause resume: [Note 971](WORKING_NOTES/971-init-pause-resume-remaining-assembly-decision-20261004.md)
latest recheck starts from clean banked HEAD `36b67c92` and freshly passes
110 focused checks in 63.319 seconds, no skips. Init remains
492 C / 47 ASM entries (12252 ASM bytes); every retained owner/raw slot and
complete existing Init code/data plus Game data remain retail-exact. Seventeen
entries are investigation targets, thirty intentional assembly. No replacement
is ready: best freshly checked bitmap is 20 / 19 words, decoder 528 bytes over,
formatter 196 over; MMIO's full eleven-word C match remains unresolved.
No new compiler hypothesis or production relink is claimed. Historical
interrupted Game edits are now banked by Notes 972 and 973; no source edits
were pending at this resume. Next requested Init work is a new bitmap
branch/delay-slot fitting hypothesis, followed by justified MMIO scheduling
or connected decoder fitting, not another broad conversion batch.
Production Init, README aggregates and sibling/frozen Release unchanged.

Queued segment writer: [Note 970](WORKING_NOTES/970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md)
recovers `func_1510D8C0` using the SDK macro: 40 / 44 words, frameless,
38 raw differences, no guards. Ten new tests connect actual reset/append/write;
898 paired big-endian instruction traces qualify data/store order, byte aliases,
unsigned segments and cached/late count reads. Every body instruction is covered.
Counts above eight use extended fixtures only, not real queue-safety acceptance.
All 237 combined checks pass, no skips; fresh link preserves exact queue helpers,
complete Init code/data, Debugger code, Game data and previous identities.
Sibling writer is already recompiled; no host/Release change. Next direct render
dependency was 42-word color emitter `func_1510CDB8`; Note 972 above completes
its source recovery and bounded writer connection.
Raw matching, full caller/rendering and staged producer remain open. README unchanged.

Immediate texture release: [Note 969](WORKING_NOTES/969-game-immediate-texture-cache-release-recovery-20261004.md)
recovers `func_1510D7AC` from its zero-return stub. All 46 words fit; 42 match
directly, with four frame/spill differences (C 0x38 versus retail 0x28).
No guards. Six new tests cover all 65536 priority/activity byte pairs, all 7762
IDs, staged callback ordering and actual resolver/retain/release/maintenance/
reload. All 227 combined checks pass, no skips; fresh link preserves full
Init code/data, Debugger code, Game data and prior identities. The sibling's
active immediate-release body remains a zero-return stub; host synchronization
and real allocator/DMA/decoder/gameplay are separate. Note 970 subsequently
recovers queued segment writer `func_1510D8C0`; staged producer and matching remain open.
README aggregates, production Init and frozen Release unchanged.

Texture metadata and maintenance: [Note 968](WORKING_NOTES/968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
finishes the interrupted `func_15003570` / `func_1510D404` recoveries: 58 / 62
and 125 / 129 words, 54/119 raw differences, no new guards. Maintenance's C
frame is 0x40 against retail 0x60. Seventeen new checks qualify bounded metadata,
all signed priorities/work counters, callback ordering and the actual connected
cache lifecycle. All 221 combined checks pass, no skips; fresh link retains full
Init code/data, Debugger code, Game data and exact initializer/startup slots.
The two pending edits described by Notes 966/967 are now qualified and banked.
Actual guest DMA/decoder, staged producer, hardware diagnostics and natural
effects remain separate. Note 969 subsequently recovers 46-word immediate cache
release `func_1510D7AC`. README aggregates and sibling/frozen Release stay unchanged.

Init decoder fitting: [Note 967](WORKING_NOTES/967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md)
tests literal/length, distance and combined immutable table-value capture.
Two variants save one optimized compressed-decoder word, but trailing alignment
absorbs it: optimized packed images retain 4336 C bytes plus 176 adapter bytes,
4512 executable against 3984 retail. Reject adoption; the gap remains 528 bytes. All 151 trial
checks and twenty ownership/section audits pass, no skips; three final size
reruns verify padding attribution. Default instruction images remain unchanged;
full linked Init code/data and Game data stay exact. No production Init/README
changes; Game metadata/maintenance was separate and uncommitted at that
checkpoint, subsequently qualified by Note 968 above.

Requested Init resume: [Note 966](WORKING_NOTES/966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md)
rechecks 492 C / 47 ASM entries after the interrupted build finishes. All 110
focused checks pass, no skips; every retained owner/raw slot and full Init
code/data plus Game data remain exact. New preincrement bitmap emits 32/20/32
words across O2/no-unroll/O1, against nineteen retail; 501 completed model pairs
and six prefixes pass, but the best form has an extra bias and wrong delay-slot
schedule. Reject adoption. Seventeen investigation targets and thirty intentional
ASM owners remain; decoder is 528 bytes over, connected formatter 196 over.
Pending Game metadata/maintenance edits built but were not behavior-qualified or
banked by that Init checkpoint; Note 968 resolves their bounded source gates.
README totals and production Init are unchanged.

Texture setup/resolution/attachment: [Note 965](WORKING_NOTES/965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md)
recovers `func_1510CE60`, `func_1510D0EC` and `func_15168E54`: 152 / 163,
155 / 162 and 45 / 45 words, with 159/142/9 differences and retail frame sizes.
No new guards. Sixteen new tests connect actual helper/setup/resolver/attachment
and release, including all 7762 valid IDs, signed priorities, allocation failures,
cleanup ordering and aliases. All 204 combined checks pass, no skips; fresh link
retains full Init code/data, Game data, exact leaves and prior recoveries. Setup's
first unwritten scratch paths remain unqualified. Note 968 subsequently recovers
expanded-size metadata loader `func_15003570` (62 words) and cache maintenance
`func_1510D404` (129 words), qualifying the bounded connected lifecycle.
Actual guest DMA/decompression and natural effects remain open.
README/sibling/Release unchanged.

Remaining Init decision refresh: [Note 964](WORKING_NOTES/964-init-remaining-assembly-current-conversion-decisions-20261004.md)
confirms 492 C / 47 assembly entries (12252 ASM bytes) after the fresh production
link. All 102 focused checks pass, no skips; every retained ASM slot and complete
Init code/data plus Game data remain retail-exact. Seventeen investigation
targets remain, thirty owners stay intentional assembly. No candidate is ready:
decoder executable is 528 bytes over, best connected formatter 196 over, and
neither small leaf has a complete match. Start with a new bitmap compiler-shape
hypothesis; no broad Init conversion batch or README aggregate change.

Asset cache and block loading: [Note 963](WORKING_NOTES/963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md)
recovers cache installer `func_1502AB04`, lookup `func_1502AC88` and block loader
`func_1502B350`: 87 / 97, 158 / 159 and 77 / 86 words, with 93, 156 and 78 raw
differences, no new guards. Fourteen new tests qualify cache ordering, metadata,
allocation/decode-result semantics and the actual lookup/block/variadic/relocation
connection. All 188 combined checks pass, no skips; fresh link retains full
Init code/data, Game data, prior recoveries and exact callers. Note 962's unwritten
lookup metadata gate is now resolved in source. Note 965 subsequently recovers
setup/attachment and their resolver; Note 968 resolves metadata loading and
bounded cache lifecycle. Guest DMA/decompression, byte matching and natural
effects remain separate gates.
No sibling/Release changes. README counts remain unchanged.

Variadic resource loader: [Note 962](WORKING_NOTES/962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md)
recovers `func_1502B6BC` and relocation helper `func_1502B4A8`. The loader fits
all 77 words / retail 0x50 frame, 17 raw differences; relocation fits 65 body
words in 72, 71 differences. No new guards. Typed variadic caller interfaces
preserve three complete exact caller slots. Fourteen new tests connect actual
constructor/helper/loader/relocation and other callers; all 174 combined checks
pass, no skips. Fresh link preserves full Init code/data, Game data and prior
recoveries. At that checkpoint lookup `func_1502AC88` (159 words) and block loader
`func_1502B350` (86 words) still had placeholders; Note 963 subsequently recovers
both; Note 965 recovers deeper setup/attachment and the texture resolver. Actual
guest loading and zero-depth/negative-depth calls remain unqualified. Metadata
loading/cache maintenance source and bounded lifecycle gates are resolved by
Note 968; PC child synchronization and natural effects remain open. README unchanged.

Extended child constructor: [Note 961](WORKING_NOTES/961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md)
recovers `func_1513264C` and `func_151336A8` from their placeholders. Bodies
fit 255 / 256 and 45 / 46 words, with 184 and nine raw differences, no guards.
The pointer wrapper remains fifteen-word exact. Fifteen new tests connect the
actual child/constructor/resource helper; all 160 combined checks pass, no skips.
Fresh link preserves complete Init code/data, Game data and prior recoveries.
Its loader gate is subsequently recovered by Note 962 and lookup/block bodies
by Note 963; Note 965 recovers deeper `func_1510CE60` / `func_15168E54` and their
resolver; Note 968 resolves metadata and bounded cache lifecycle. PC
synchronization and natural effects remain open; retained Init assembly and
README aggregates are unchanged.

Extended child callback: [Note 960](WORKING_NOTES/960-game-extended-child-emission-semantic-recovery-20261004.md)
recovers code-0x37 `func_150E93DC`, its 124-byte descriptor and typed pointer
wrapper. C fits 206 body words / 0x138 frame in the 208-word slot, with 200
raw differences and no guards. The wrapper remains exact across fifteen words.
Thirteen new tests and all 145 combined checks pass, no skips; fresh link
preserves complete Init code/data, Game data and prior recoveries. Retail's
28-byte extra payload and descriptor holes remain unspecified. Constructor
`func_1513264C` was still a placeholder at that checkpoint; its body and resource
helper are subsequently recovered by Note 961. PC synchronization and natural effects
remain separate gates. Init assembly and README aggregates are unchanged.

Init decoder fitting: [Note 959](WORKING_NOTES/959-init-decoder-packed-parent-and-bit-tail-fitting-trials-20261004.md)
tests new opt-in parent packing and shared-refill/inline bit-tail shapes.
Optimized complete images grow to 4528 and 4544 bytes, so reject both; the
retained 4512-byte candidate remains 528 bytes over retail. All 105 connected
trial checks plus twenty baseline audit/ledger checks pass, no skips.
Default-option instruction images remain unchanged; full existing Init code/data
and Game data stay exact. No production adoption or README aggregate change.
Next fitting work must reduce the complete image and resolve entry/stack ownership.

Requested Init resume: [Note 958](WORKING_NOTES/958-init-resume-remaining-assembly-readiness-20261004.md)
freshly verifies 492 C / 47 assembly entries, all retained owners/slots and
complete existing linked Init code/data and Game data. All 102 checks pass,
no skips. Seventeen entries remain investigation targets; thirty established
boot/hardware/context/SDK owners stay assembly. No replacement is ready to
adopt: decoder remains 528 bytes over, best connected formatter 196 over,
and small leaves lack complete retail matches. Older bitmap forms do fit
nineteen words but remain non-matching. Init source and README unchanged;
the separate Game child placeholder is not edited by this assessment.

Extended weighted emitter: [Note 957](WORKING_NOTES/957-game-extended-weighted-emitter-semantic-recovery-20261004.md)
recovers `func_150E9178`'s complete code-0x36 body and 60-byte child payload.
C fits all 153 words / 0xF8 frame, with 54 differences and no guards. Eleven
new tests connect the real creator and all four actual position-writer modes;
all 132 combined tests pass, no skips. Fresh link preserves full Init code/data,
Game data, exact neighbors and prior recoveries. README aggregates unchanged.
The PC source still has an emitter stub, so synchronization is separate. Next
recover code-0x37 child `func_150E93DC` (208 words); this historical placeholder
gate is subsequently resolved by Note 960. Its constructor and downstream/
gameplay qualification remain open.

Game child-emission callback: [Note 956](WORKING_NOTES/956-game-child-emission-callback-recovery-and-fitting-20261004.md)
finishes `func_150E8D5C` and its typed pointer interfaces. Two flag shifts resolve
the interrupted 225-word build failure: C fits 219 words / 0x120 frame in the
224-word slot, with 213 raw differences and no guards. Fresh relink preserves
complete Init code/data, Game data and exact constructor/wrappers/helpers.
Thirteen new tests qualify the actual child/wrapper/spherical bodies and parent
payload connection; all 121 combined tests pass, no skips. Child-placeholder
and fitting gates are resolved in source
and tests, not gameplay; README aggregates unchanged. The sibling PC source
still has a zero-return child stub, so host synchronization remains open.
Its sibling `func_150E9178` is subsequently recovered by Note 957; downstream
rendering and byte matching remain separate tasks.

Init bitmap right-shift trial: [Note 955](WORKING_NOTES/955-init-bitmap-fill-value-right-shift-mask-trial-20261004.md)
tests reusing `0xFF` for the final mask. IDO rematerializes the constant and
retains XOR: 20 optimized words against nineteen retail. Eight new tests
qualify 501 completed model pairs/six prefixes; 34 combined tests pass, no skips.
Reject adoption; Init ownership, existing exact code/data and README unchanged.
Older nineteen-word one-based-mask forms also exist but do not match retail.
Its subsequent Game-child fitting recovery is completed by Note 956.

Init resume: [Note 954](WORKING_NOTES/954-init-resume-conversion-decision-and-interrupted-game-build-20261004.md)
confirms 492 C / 47 assembly entries (12,252 retained bytes). All retained
owners/slots and the existing ELF's complete Init code/data and Game data are
exact. Ninety-three focused tests plus one freshly compiled decoder size check
pass, no skips. Two small leaves remain candidates, but no replacement is ready
to adopt; decoder is still 528 bytes over, and connected glyph fitting/ownership
remain open. Thirty boot/hardware/SDK owners stay assembly. README unchanged.
Its interrupted Game build then failed at 225 words against 224; that gate is
now resolved by Note 956's fitted child, chain tests and fresh production link.

Game descriptor-position writer: [Note 953](WORKING_NOTES/953-game-descriptor-position-writer-and-weighted-chain-recovery-20261004.md)
restores all four `func_1514470C` modes and the void interface. Semantic C fits
179 words / 0x78 frame in the 218-word slot, with 196 raw differences and no
guards. Eleven new tests connect the actual weighted caller/writer/helpers;
all 100 combined tests pass. Fresh relink preserves complete Init code/data,
Game data and exact neighbors; sibling already has its recompiled writer.
The uninitialized-position placeholder gate is resolved in source/tests, not
accepted gameplay. Its child callback `func_150E8D5C` is subsequently recovered
by Note 956 and sibling `func_150E9178` by Note 957. Matching totals/README unchanged.

Init address-difference trial: [Note 952](WORKING_NOTES/952-init-bitmap-address-difference-induction-trial-20261004.md)
tests a new unsigned subtraction/zero-branch shape for `func_10005BE0`.
IDO removes XOR but introduces a second induction variable: 22 O2 words
against nineteen retail. Eight new tests qualify 501 pairs/six bounded prefixes;
93 combined Init tests pass. Reject adoption; all retained owners and linked
Init code/data/Game data remain exact, README totals unchanged. Next broader
semantic recovery remains the pending Game emitter's position-writer dependency.

Init resumed assessment: [Note 951](WORKING_NOTES/951-init-resume-conversion-readiness-and-repeatable-audit-20261004.md)
freshly verifies 492 C / 47 assembly and all retained raw linked slots.
Two small leaves remain C candidates; ten decoder and five diagnostic entries
need connected recovery, while thirty original boot/hardware/SDK owners stay
assembly. Seven new audit checks, 78 retained contract/compiler tests and 46
freshly compiled decoder tests pass: 131 across three runs, no skips. Best
decoder remains 4512 bytes against 3984 retail; glyph path is also oversized.
Full existing Init code/data and Game data are exact. No Init replacement is
ready to adopt; production ownership and README totals stay unchanged.

Game weighted emitter: [Note 950](WORKING_NOTES/950-game-weighted-event-emitter-semantic-recovery-20261004.md)
recovers `func_150E8B1C`'s complete code-0x33 weighted emission body. It fits
144 words and the original 0xC8 frame, but 44 words differ; no guards added.
Eighty-two tests and fresh link pass; full Init/Game data and exact neighbors
are preserved. Aggregates/README unchanged. Its then-placeholder position
writer is now restored by Note 953 and child callback `func_150E8D5C` by Note 956.
Downstream/runtime gates remain, so the actual guest pipeline is not qualified.

Game event payload creators: [Note 949](WORKING_NOTES/949-game-event-payload-creators-and-connected-dispatch-match-20261004.md)
finishes the preserved `func_150E8A80` and `func_150E90DC` edits. Both match
all 39 words directly, original 0x48 frames, no guards; actual dispatcher/timer
chains cover head mutations, failures, payload snapshots and extra RNG draws.
Seventy-two tests and fresh production link pass; Init, Game data and exact
neighbors remain intact. Game 2609 / total 3282 exact, zero drift. README
matching rows updated; next inspect `func_150E8B1C` and its updater contract.

Init bitmap equality-exit trial: [Note 948](WORKING_NOTES/948-init-bitmap-equality-exit-lifetime-trials-20261004.md)
tests cursor-address versus captured-end masks inside the equality exit.
Both remove XOR but emit 21 optimized words against nineteen retail, adding
an unconditional back edge and second return. Eight new tests / 1,002 pairs
and twelve bounded prefixes pass; all 78 combined tests pass. Reject both.
Production Init ownership,
README totals and the two unfinished Game edits remain unchanged.

Init remaining assembly: [Note 947](WORKING_NOTES/947-init-remaining-assembly-conversion-map-20261004.md)
maps all retained entries and confirms 492 C / 47 assembly, 12,252 ASM bytes.
All retained owners/slots and complete existing linked Init code/data remain
retail-exact; seventy focused tests pass. Bitmap/MMIO are small C candidates,
not qualified adoptions; decoder/glyph need connected fitting and ownership.
README totals stay unchanged. Two unfinished Game creator/test edits remain
preserved separately; this assessment does not qualify or commit them.

Game event/packet/sound dispatch: [Note 946](WORKING_NOTES/946-game-event-packet-and-sound-dispatch-direct-match-20261004.md)
recovers `func_150E8930`, all 84 words directly matching with original 0x38
frame and no guards. Its corrected no-argument call preserves all 28 timer
caller words. Sixty-five tests and fresh link pass; complete Game data, Init
sections and neighboring exact owners remain intact. Game 2607 / total 3280
exact, zero drift; README matching rows updated. Next recover `func_150E8A80`,
then `func_150E90DC`; both list-triggered creators are still placeholders.

Game world-emitter dispatch: [Note 945](WORKING_NOTES/945-game-world-emitter-dispatch-direct-byte-match-20261004.md)
recovers `func_150E81A8`'s selected world position, descriptor and random packet.
All 129 words match directly from C, original 0x90 frame, no guards. Fifty-nine
tests and a fresh production relink pass. Full Game data and Init code/data
stay exact, as do both curves and all three adjacent assembly owners. Game
2606 / total 3279 exact, zero drift; README matching rows updated. Next semantic
target is the verified `func_150E8930` placeholder; Init ownership unchanged.

Init bitmap exit-edge trials: [Note 944](WORKING_NOTES/944-init-bitmap-exit-edge-control-flow-trials-20261004.md)
tests separate-final-store and taken-edge-increment forms. The latter removes
XOR but adds an entry jump: twenty words, still over nineteen retail. Eight
new / 54 combined tests pass; 1,002 new paired executions and twelve bounded
prefixes qualify alias/wrap traces. Reject both for production; Init owners
and README totals unchanged. Game `func_150E81A8` remains the next actionable
semantic recovery under the broader decomp goal.

Init resume assessment: [Note 943](WORKING_NOTES/943-init-resume-linked-baseline-and-conversion-shortlist-20261004.md)
confirms 492 C / 47 assembly entries and the current production ELF's complete
164,048 code / 17,376 data bytes retail-exact, including all retained slots.
Sixty-two focused tests pass. Bitmap/MMIO remain the two small C candidates;
none is ready to adopt. Decoder remains 528 linked bytes over retail, and
connected glyph fitting/ownership remain open. Latest requested work is Init
assessment; the pending Game placeholder is separate. README totals unchanged.

Game physical data repair: [Note 942](WORKING_NOTES/942-game-physical-data-order-and-literal-pool-restoration-20261004.md)
restores retail owner order, four missing pools and the table's no-padding
assembly profile. Fresh full link succeeds; all 189,088 physical Game-data
bytes / 720 owners match retail. Pan coefficient is correct at 0x800A1350.
Fifty-three tests pass; Init code/data remain exact and both curves retain
194/212 direct matches. Aggregate counts unchanged. The earlier layout/build
gate is resolved statically; guest gameplay acceptance is still separate.
Next semantic target: `func_150E81A8`'s verified zero-return placeholder.

Init unsigned-induction trials: [Note 941](WORKING_NOTES/941-init-bitmap-unsigned-induction-guest-qualification-20261004.md)
reject two new bitmap shapes: unsigned equality is byte-identical to the
20-word pointer control; countdown emits 22 words against nineteen retail.
Eight new / 46 combined tests pass, including 1,002 completed retail/C pairs
and twelve bounded prefixes with alias/fence rejecting controls. Production
Init ownership/counts remain unchanged. Its then-open Game link gate is now
resolved by Note 942; the rejected bitmap forms are not production conversions.

Init pause-resume decision: [Note 940](WORKING_NOTES/940-init-pause-resume-conversion-decision-20261004.md)
recounts 492 C / 47 assembly entries and verifies all retained source owners.
Fifty-four focused tests pass, including fresh connected formatter trials.
Bitmap/MMIO remain the smallest C candidates; no replacement is ready to adopt.
Decoder is still 528 linked bytes too large; glyph fitting/ownership remain open.
Preserved pre-edit ELF Init code/data matched all retail bytes. Note 942 now
also verifies a successfully rebuilt production ELF with exact Init sections.

Game curve update: [Note 939](WORKING_NOTES/939-game-curve-update-direct-match-and-data-placement-gate-20261004.md)
recovers `func_150E7C9C` and confirms the payload cursor. All 212 words emit
directly from C, original 0xA8 frame, no guards; builder remains 194/194 exact.
Thirty-two focused tests pass, including the actual builder/update/helper chain.
Fresh matcher Game 2605 / total 3278 exact, zero instruction address drift.
**Layout gate resolved by Note 942:** the displaced coefficient is restored to
0x800A1350 with value 0x3EDCEE77, and the complete data image is exact.
Instruction/data matching still does not establish guest gameplay acceptance.

Game random curve record: [Note 938](WORKING_NOTES/938-game-random-curve-record-direct-byte-match-20261004.md)
recovers `func_150E7994`'s packet, allocator, metadata and sampled curve body.
All 194 words emit directly from C, with original 0xC8 frame and no guards.
Twenty-six focused tests pass; fresh link has no drift. Game 2604 / total
3277 exact, 2186 different. README matching rows updated; conversion counts
unchanged. Next inspect `func_150E7C9C`; Init production ownership unchanged.

Game random edge emitter: [Note 937](WORKING_NOTES/937-game-random-edge-emitter-semantic-recovery-20261004.md)
replaces `func_150E76D0`'s placeholder with its four-variant descriptor builder.
Twenty-one focused tests pass, including both actual dispatcher/helper paths.
Body 155 / slot 177 words, original 0xB0 frame, 171 differences, no guards/drift.
Semantic recovery, not a byte match; aggregates unchanged. Next inspect
adjacent placeholder `func_150E7994`; Init production owners remain unchanged.

Init split-validation trial: [Note 936](WORKING_NOTES/936-init-split-destination-validation-interface-trial-20261004.md)
tests a one-cell/scalar-return setup interface. O2 624 text / 64 stack and
O1 720 / 56 do not improve the independent controls. All 1,728 paired fixtures
and sixteen combined tests pass. Keep assembly production owners; pick up
Game alternate emitter helper `func_150E76D0` from Notes 924/925 next.

Init shared setup trial: [Note 935](WORKING_NOTES/935-init-shared-formatter-setup-text-stack-tradeoff-20261004.md)
saves sixteen linked bytes, but increases nested stack: O2 608 bytes / 80
stack, O1 688 / 56. All 1,152 paired fixtures and sixteen combined tests pass.
Helper measurement is call-target guarded. Retain opt-in only; fitting and
ownership gates remain open, production counts unchanged.

Init connected C formatters: [Note 934](WORKING_NOTES/934-init-connected-semantic-c-formatters-and-layout-cost-20261004.md)
recovers both formatter bodies calling the C writer directly. Two profiles /
576 paired fixtures and fifteen combined tests pass, including string/output
alias timing. O2 allocated text is 624 versus 412 connected retail bytes;
both profiles descend 48 bytes. Fitting/adapter/ownership remain open.

Init glyph adoption boundaries: [Note 933](WORKING_NOTES/933-init-glyph-adapter-production-placement-and-stack-boundaries-20261004.md)
pins nine inherited-stack and six overlay-stack diagnostic formatter sites.
Experimental C address is occupied by `func_10008F90`; no adjacent leaf-slot
extension is free. Overlay frame containment is conditional, not ownership.
Twenty focused tests pass; retain adapter as experimental, no conversion.

Init glyph adapter: [Note 932](WORKING_NOTES/932-init-connected-glyph-c-adapter-qualification-20261004.md)
qualifies the C writer through real formatter callers: 280 connected plus
five direct-leaf pairs, seven new / twenty combined tests pass. Adapter fits
the 120-byte leaf slot, but combined allocated text is 248 bytes and stack
descent is 56 bytes. Production placement/stack ownership remain open.

Init glyph fitting: [Note 931](WORKING_NOTES/931-init-glyph-pixel-seeding-and-countdown-fitting-20261004.md)
reduces the ordinary-ABI semantic writer from 31 to 29 words using low-halfword
pixel seeding and countdown loops. Eight variants / 2,128 paired fixtures pass;
sixteen combined tests plus a separate footprint check pass. Body fits, but
connected adapter/stack/layout and byte matching remain open. No conversion.

Init semantic glyph trial: [Note 930](WORKING_NOTES/930-init-semantic-glyph-writer-differential-qualification-20261004.md)
qualifies three compiled profiles against retail ordered memory operations
and bounded aliases: 798 paired fixtures, sixteen combined tests pass.
Smallest body is 31 words against 30 retail, before adapter cost; O1 uses a
32-byte frame. ABI adapter, fitting and ownership remain open. No conversion.

Init connected formatters: [Note 929](WORKING_NOTES/929-init-connected-glyph-formatter-contracts-20261004.md)
executes interior destination setup, both formatter callers and real glyph
writer. Pins null-buffer return links, all signed-byte mappings and hex
delay-slot predecrement/cursor effects. Five new / twenty-four combined tests
pass. Semantic C/alias and adapter qualification remain open; no conversion.

Init glyph contract: [Note 928](WORKING_NOTES/928-init-glyph-writer-register-and-pixel-contract-20261004.md)
pins `func_10007D28`'s nonstandard register inputs, two-destination ordered
8x8 pixel writes, 0x248 row stride and sixteen-byte cursor result. All 262
rendering fixtures / four new tests pass; nineteen combined tests pass.
Connected formatter/interior-entry qualification and adapter work remain open.
No production conversion or aggregate change.

Init unsigned-range bitmap trials: [Note 927](WORKING_NOTES/927-init-bitmap-unsigned-range-comparison-trials-20261004.md)
reject two new bounded-buffer predicate shapes. Both still emit twenty O2
words against nineteen retail; `sltu` replaces XOR without solving schedule.
Eleven shapes / 869 host fixtures and 33 retained-contract tests pass.
Production owners, aggregate counts and README remain unchanged.

Init readiness refresh: [Note 926](WORKING_NOTES/926-init-remaining-assembly-readiness-refresh-20261004.md)
recounts 492 C / 47 assembly routines, with 151,796 / 12,252 bytes. Bitmap
and MMIO remain small C candidates, not production-ready replacements.
Qualified decoder is 528 linked bytes too large; reservation, entry/frame and
hardware/context gates remain open. All 38 focused tests pass, no skips.
Ordered next steps are in the note; no source conversion or README change.

Game positioned emitter descriptor: [Note 925](WORKING_NOTES/925-game-positioned-emitter-descriptor-recovery-20261004.md)
recovers `func_150E75A0`'s initialized descriptor fields, submission and result
propagation. Callee's 0x58-byte copy pins extent; unwritten padding/tail stay
unwritten. Six new tests / sixteen combined pass, including real dispatcher/
helper integration. Body 74 / retail 76 words, 69 differences, no guards/drift.
Aggregate counts unchanged; alternate helper `func_150E76D0` remains a placeholder.

Game random dispatcher: [Note 924](WORKING_NOTES/924-game-probability-gated-random-dispatch-recovery-20261004.md)
recovers both `func_150E7290` branches and shared sound/command/packet tail.
Five new tests / fifteen combined pass. Production has 195 body words in its
196-word slot, 183 differing positions, original 0x68 frame and no guards/drift.
Adjacent helper call ABIs are typed, but their bodies remain placeholders.
Three preceding exact slots stay exact; aggregate counts/README unchanged.

Game fixed/random parameters: [Note 923](WORKING_NOTES/923-game-fixed-random-parameter-initializer-match-20261004.md)
recovers `func_150E71E4`'s vector-derived value, three fixed fields and four
random samples. All 43 words match directly from C, no guards. Five new tests
/ fourteen combined pass; fresh matcher Game 2603 / total 3276 exact, zero
drift. README aggregate rows updated; detailed behavior remains in the note.

Game vector random parameters: [Note 922](WORKING_NOTES/922-game-vector-random-parameter-initializer-match-20261004.md)
recovers `func_150E70EC`'s two vector-derived values and six sampled fields.
All 62 words match directly from C without guards, including square-root
intrinsic and ordered publication. Five new tests / fourteen combined pass;
fresh matcher Game 2602 exact / total 3275, zero drift. README rows refreshed.

Game linked-record exit trials: [Note 921](WORKING_NOTES/921-game-linked-record-position-exit-layout-trials-20261004.md)
tests five exit shapes across four profiles; none matches retail. Return/goto
variants retain the 71-word shared-RA tail under O2/g3; O1 emits 89 words.
All twenty host shape/test runs pass. Production's 15 differences and all
aggregate counts remain unchanged; retained driver makes the trials reproducible.

Game linked-record matching refinement: [Note 920](WORKING_NOTES/920-game-linked-record-position-stack-and-float-shape-20261004.md)
reduces `func_150E6FAC` from 38 to 15 differing positions by restoring local
declaration order and float operand source shape. All 57 non-branch words
before the return tail match directly; thirteen tests pass. Still 71 body
words versus 72 retail, no guards/drift. Return-tail layout remains open.

Game linked-record position: [Note 919](WORKING_NOTES/919-game-linked-record-position-semantic-recovery-20261004.md)
replaces `func_150E6FAC`'s zero-return placeholder with lookup, randomized
radius/angle offsets and fallback coordinates. Five new tests / thirteen
combined pass; independent IDO body fits. Production has 71 body words in
the original 72-word slot, 38 differing positions, zero guards and no drift.
This is semantic recovery, not a new exact match; README totals unchanged.

Init bitmap qualifier/sentinel trials: [Note 918](WORKING_NOTES/918-init-bitmap-store-qualifier-and-sentinel-trials-20261004.md)
reject nonvolatile stores (20 O2 words, unchanged from control) and an
end-plus-one sentinel (33 O2 words, 20 with unrolling disabled), against
nineteen retail words. Nine shapes pass 711 host fixture combinations;
33 retained-contract tests pass. No production conversion or aggregate change.

Game random range position: [Note 917](WORKING_NOTES/917-game-random-range-position-recovery-and-match-20261004.md)
recovers `func_150E6F18` as a direct 37-word C match without guards. Unsigned
six-pointer selection, pointer capture before float RNG, field reads after
that call and sequential overlapping output are preserved. Fourteen focused
tests pass; fresh matcher Game 2601 exact / total 3274, zero drift.
Init remains 492 C / 47 assembly; the qualified decoder is still 528 bytes
too large, with reservation, entry/frame ownership and hardware gates open.

Game position sound adapter: [Note 916](WORKING_NOTES/916-game-object-position-sound-adapter-and-init-return-contract-20261004.md)
recovers `func_1509F6E8`'s nullable lookup, truncated coordinates and handle
forwarding as a direct 37-word C match. Corrected Init `func_10010F88` u16
return remains exact across 29 words; complete Init code/data remain retail.
Thirteen tests pass; fresh matcher Game 2600 exact / total 3273, zero drift.
README aggregate rows updated; unrelated actor/timeline work remains unstaged.

Game status record reset: [Note 915](WORKING_NOTES/915-game-status-record-reset-recovery-and-match-20261004.md)
finishes `func_151E5034` as semantic C: sixteen selected zero stores with
retail pointer reloads. All 37 linked words match directly, no guards; nine
focused tests pass. Fresh ELF/matcher: Game 2599/4790 exact, total 3272/5463,
zero drift. Conversion totals unchanged; README aggregate rows refreshed.
Unrelated actor/timeline work remains uncommitted and excluded from this recovery.

Init dynamic fitting trials: [Note 914](WORKING_NOTES/914-init-rejected-dynamic-symbol-and-header-gate-fitting-20261004.md)
rejects symbol-before-drop (no text saving, O2 core bound +40) and encoded
header mask gate (O2 core text +16). All 16384 header predicates agree, but
neither fitting result improves the candidate. Qualified source restored
exactly; fifteen focused checks pass. Current linked 4512 / 528 excess unchanged.

Init distance operation O2 CU1-set corpus: [Note 913](WORKING_NOTES/913-init-distance-operation-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 818.478 seconds, no skips. With Note
912, both masked CU1 modes qualify 1014 paired runs for this fixed candidate:
text 4512, descent 3248, low `0x80031D60` / margin 80, hashes unchanged.
Twenty-two supporting checks pass. Next: fitting (528 excess), reservation,
entry/frame ownership and hardware/context; production/README unchanged.

Init distance operation O2 CU1-clear corpus: [Note 912](WORKING_NOTES/912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 826.726 seconds, no skips. Text 4512,
descent 3248, minimum SP `0x80031D60` / margin 80 confirm Note 911's saving;
six candidate hashes hold. Twenty-two supporting tests pass. Matching CU1-set
corpus, fitting (528 excess), reservation and production gates remain open.

Init distance operation local: [Note 911](WORKING_NOTES/911-init-distance-operation-local-fitting-20261004.md)
retains an opt-in distance entry operation snapshot: packed O2 linked text
4512, sixteen saved / 528 excess; descent remains 3248. O1 complete size
unchanged. Bounded run: 45 passes / one corpus skip; separate backreference
storage guard passes. Default text identical; changed full corpora and
fitting/reservation/production gates remain open. README unchanged.

Init bitmap value-lifetime trials: [Note 910](WORKING_NOTES/910-init-bitmap-shared-fill-mask-lifetime-trials-20261004.md)
rejects a shared fill/mask variable (same 20-word O2 text as control) and
postdecrement variant (22 words), versus retail nineteen. Seven shapes pass
553 host fixture combinations; 33 retained-contract tests pass, no skips.
Experiments remain reproducible; production ownership and totals unchanged.

Init resume readiness: [Note 909](WORKING_NOTES/909-init-resume-conversion-readiness-audit-20261004.md)
recounts 492 C / 47 assembly functions and verifies all remaining assembly
source owners. All 38 focused checks pass, no skips. Bitmap/MMIO matching
remains open; the qualified dynamic-order decoder is 544 bytes too large,
with reservation/ownership/hardware gates open. No production conversion or
README aggregate change. The note provides the current ordered work list.

Init startup thread contract: [Note 908](WORKING_NOTES/908-init-startup-thread-stack-top-and-constructor-contract-20261004.md)
executes pinned call preparations and retail constructor. Stack tops
`0x8002D8B0` / `0x800318B0`, saved SP top-minus-sixteen; constructor writes
end at object +0x130, but later +0x230 FPR footprint remains protected.
Private-gap sentinels and executed crossing-store controls pass; 25 combined
tests pass. This strengthens neighbor evidence, not full reservation ownership.

Init replication deficit trials: [Note 907](WORKING_NOTES/907-init-rejected-builder-replication-span-deficit-trials-20261004.md)
rejects entry-unit and byte-unit remaining-span loops: both grow O2 core text
32 bytes and call bound sixteen; O1 also grows. Source restored exactly,
17 focused retained-builder/size/ledger tests pass. Qualified dynamic-order
candidate remains 4,528 linked / 544 excess; production and README unchanged.

Init dynamic order O2 CU1-set corpus: [Note 906](WORKING_NOTES/906-init-dynamic-order-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 836.723 seconds, no skips. With Note
905, both masked CU1 modes cover 1,014 paired pages for this unchanged
candidate. Text 4,528, descent 3,248, low `0x80031D60`, margin 80 and hashes
match. Fitting (544 excess), reservation and production/hardware gates open.

Init dynamic order O2 CU1-clear corpus: [Note 905](WORKING_NOTES/905-init-dynamic-order-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 835.460 seconds, no skips. Text 4,528,
descent 3,248, low `0x80031D60`, known-neighbor margin 80 confirm Note 904's
tradeoff; six recorded hashes fixed. Matching CU1-set corpus remains open,
along with fitting (544 excess), reservation and production/hardware gates.

Init dynamic order cursor: [Note 904](WORKING_NOTES/904-init-dynamic-order-cursor-text-stack-tradeoff-20261004.md)
retains an opt-in initializer countdown: packed O2 text 4,528 (32 saved,
544 excess) at eight more stack bytes; O1 text grows sixteen. Whole bounded
suite 45 passes / one corpus skip; 192 all-count prefix runs and separate
alignment/ledger checks pass. Default text exact. Changed-candidate full corpora
and production gates remain open; qualified baseline remains Notes 901/902.

Init bitmap return-lifetime trials: [Note 903](WORKING_NOTES/903-init-bitmap-return-value-lifetime-trials-20261004.md)
tests returning the advanced cursor or captured end + 1. Both retain the XOR
loop and grow optimized bodies to 21 words versus retail 19. Host behavior
and return checks pass; 33 retained-contract tests pass. No production match
or signature change; qualified pointer-owned decompressor remains unchanged.

Init pointer-owned O2 CU1-set corpus: [Note 902](WORKING_NOTES/902-init-pointer-owned-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 823.148 seconds, no skips. With Note
901, both masked CU1 modes now cover 1,014 paired pages for this unchanged
candidate. Text 4,560, descent 3,240, low `0x80031D68`, margin 88 match;
source hashes fixed. Fitting (576 excess), reservation and production gates open.

Init pointer-owned O2 CU1-clear corpus: [Note 901](WORKING_NOTES/901-init-pointer-owned-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 819.113 seconds, no skips. Packed
executable text 4,560, descent 3,240, minimum SP `0x80031D68`, known-neighbor
margin 88; six recorded source hashes unchanged. Combined-candidate CU1-set
qualification remains open, as do 576-byte fitting excess and production gates.

Init pointer-owned tight adapter: [Note 900](WORKING_NOTES/900-init-pointer-owned-tight-adapter-fitting-20261004.md)
combines guest input/workspace ownership with two omitted adapter stores.
Body 176, packed executable text 4,560 O2 / 5,968 O1; bounds unchanged.
O2 rodata moves sixteen bytes below the original default layout, removing
the intermediate alignment gap. Corrected bounded run: 44 passes / one corpus
skip, executed stale-read controls active. Default text exact. O2 still 576
over retail; new full corpora and production ownership/hardware remain open.

Init tight adapter: [Note 899](WORKING_NOTES/899-init-tight-adapter-return-scheduling-and-alignment-20261004.md)
adds opt-in RA delay-slot load, combined SP restore and word-aligned subsection.
Body/executable section falls 192 -> 184; packed text 4,568 O2 / 5,976 O1,
bounds unchanged. Linked O2 rodata still starts at the same aligned address:
eight-byte gap means no proven whole footprint saving. Whole bounded run
41 passes / one corpus skip; separate dependency test passes. Default adapter
text identical. Changed-adapter corpora/production gates open; README unchanged.

Init helper trials: [Note 898](WORKING_NOTES/898-init-global-mask-and-explicit-abi-copy-trials-20261004.md)
rejects global low-mask replacement (O2 bound +8, O1 text +16) and explicit
ABI copy (O2 text +16). Both restored exactly; sixteen focused tests pass,
no skips. Qualified O1/default O2 unchanged; no production/README change.

Init core return trials: [Note 897](WORKING_NOTES/897-init-core-return-control-flow-trials-20261004.md)
rejects success-first (size/bound neutral) and shared-result (O2 text +16,
bounds +24 O2 / +8 O1). Exact source restored; ten focused core/ledger/size
tests pass, no skips. Qualified O1/default O2 remain unchanged; no production
or README change.

Init fixed-length endpoint trials: [Note 896](WORKING_NOTES/896-init-fixed-length-cursor-endpoint-trials-20261004.md)
rejects distance cursors and relative literal endpoints: no complete O2
text saving, all grow O1 sixteen bytes; some initializer frames grow eight.
Exact qualified source restored; nine ledger/size/full-initializer tests pass,
no skips. Qualified O1/default O2 unchanged; production and README untouched.

Init packing trials: [Note 895](WORKING_NOTES/895-init-builder-wide-operation-and-header-packing-trials-20261004.md)
rejects wider operation and combined-header packing. Both remove two public
O2 builder words but save no whole text and add eight bytes to both call bounds.
Exact qualified source restored; twenty focused tests pass, no skips.
Qualified O1 remains 5,984 linked; default O2 remains 4,576 / 592 excess.
Production/defaults/README unchanged.

Init scan-deficit O1 CU1-set corpus: [Note 894](WORKING_NOTES/894-init-scan-deficit-o1-full-masked-cu1-set-corpus-20261004.md)
passes all 507 paired pages in 971.161 seconds, no skips. With Note 893:
1,014 paired pages across both masked modes. Text 5,984, descent 3,200 equals
bound, minimum SP 0x80031D90 / margin 128. Twenty-six supporting checks pass;
six source hashes hold. Both O1 corpus gates checked off; changed-option O2,
fitting/reservation/ownership/hardware remain. Production/README unchanged.

Init scan-deficit O1 CU1-clear corpus: [Note 893](WORKING_NOTES/893-init-scan-deficit-o1-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 paired pages in 975.542 seconds, no skips. Linked text 5,984,
maximum descent 3,200 equals bound, minimum SP 0x80031D90 / neighbor margin
128. Twenty-six supporting gates pass; six source hashes hold. Matching O1
CU1-set, changed-option O2 and production ownership/hardware gates remain.
Production/README unchanged; default best O2 remains 4,576 / 592 excess.

Init scan-deficit fitting: [Note 892](WORKING_NOTES/892-init-builder-inplace-scan-deficit-fitting-20261004.md)
adds an opt-in bounded in-place deficit scan. Packed O1 core falls 32 bytes
to 5,792 / linked 5,984; packed O2 stays 4,384 / linked 4,576 (592 excess).
Frames/bounds unchanged. Whole bounded run: 39 passes / one corpus skip;
separate executed-branch gate passes across six images. Default packed text
matches prior baseline exactly. Changed-option full corpora remain open;
production and README unchanged.

Init mask-lifetime trials: [Note 891](WORKING_NOTES/891-init-mask-before-refill-lifetime-trials-20261004.md)
rejects moving pure masks before refill: take-bits grows both core profiles
sixteen bytes, lookup grows both thirty-two, with unchanged call bounds.
Exact source restored; fifteen focused call/ledger/lookup checks pass.
Qualified linked O2 remains 4,576 / 592 excess; no production/README change.

Init builder sort-offset trials: [Note 890](WORKING_NOTES/890-init-builder-sort-offset-local-trials-20261004.md)
rejects explicit local offsets in both store orders: neither reduces complete
O2 text, both raise O2/O1 call bounds eight bytes. Both edits removed, source
blob restored exactly; seventeen semantic/ledger tests pass. Qualified linked
O2 remains 4,576 / 592 excess. No production or README change.

Init current conversion decision: [Note 889](WORKING_NOTES/889-init-current-assembly-conversion-decision-20261004.md)
rechecks 492 C / 47 assembly functions (151,796 / 12,252 bytes). Bitmap and
MMIO remain small matching candidates; the connected decoder has qualified
experimental C but is still 592 linked bytes too large. Thirty-three focused
tests pass, no skips. Resume fitting and ownership gates, not already completed
frame/adapter recovery. No production conversion or README change.

Init guarded CU1-set corpus: [Note 888](WORKING_NOTES/888-init-live-sp-guard-full-masked-cu1-set-corpus-20261004.md)
passes all 507 live-SP-guarded packed O2/g3 paired pages in 804.839 seconds,
no skips. With Note 887: 1,014 guarded paired pages across both masked modes.
Text 4,576 / 592 excess; descent 3,240 equals bound, minimum SP 0x80031D68 /
known-neighbor margin 88. Twenty-six supporting gates pass; nine source hashes
hold. Both guarded corpus gates checked off; fitting, full reservation,
entry/frame ownership and hardware/context remain. Production/README unchanged.

Init guarded CU1-clear corpus: [Note 887](WORKING_NOTES/887-init-live-sp-guard-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 live-SP-guarded packed O2/g3 paired pages in 806.976 seconds,
no skips. Text 4,576 / 592 excess; observed descent 3,240 matches bound,
minimum SP 0x80031D68 / known-neighbor margin 88. Twenty-six supporting
gates pass; nine source blobs hold. Guarded CU1-clear checked off; matching
guarded CU1-set, fitting, full reservation and hardware/ownership remain.
Candidate/production sources and README unchanged; unrelated Game preserved.

Init live-SP write guard: [Note 886](WORKING_NOTES/886-init-live-sp-write-fence-and-negative-qualification-20261004.md)
adds a separate fixture rejecting private-stack writes below current SP.
Executed below-frame store corruption is rejected across six builds and both
masked modes, even above the old neighbor fence. Whole bounded suite has
37 passes / one corpus skip; thirteen storage regressions pass. Size/bounds
unchanged, packed O2 4,576 / 592 excess. New guarded corpus and full reservation
remain open; previous corpus evidence stays scoped to its old fixture.
Production/defaults/README and unrelated Game work unchanged.

Init MMIO published-address trial: [Note 885](WORKING_NOTES/885-init-mmio-published-address-dataflow-trial-20261004.md)
measures five profiles using D_80038070 as the hardware-store destination.
O1 eliminates the read and retains the address, but adds a register copy
and delay-slot store; no complete eleven-word match. Other profiles either
exceed the slot or retain an extra read. Ten bounded store traces pass;
three production MMIO assembly tests pass. No production/profile/guard or
README changes; decoder-qualified baseline and unrelated Game work preserved.

Init descending count-clear trials: [Note 884](WORKING_NOTES/884-init-builder-descending-count-clear-trials-20261004.md)
measures post-/pre-decrement clears of all 17 buckets. Neither reduces
complete O2 core text; post-decrement adds eight bytes to both core bounds,
and both forms grow O1 text. Both removed, source restored exactly.
Thirteen focused retained gates pass, including direct builder boundaries.
Qualified linked O2 stays 4,576 / 592 excess; production/README unchanged.

Init stored-loop fitting trials: [Note 883](WORKING_NOTES/883-init-stored-output-cursor-and-countdown-trials-20261004.md)
measures an output pointer cursor and a length countdown. Both grow whole
packed core text sixteen bytes in O2/O1 and enlarge the stored frame;
maximum core bounds stay 392/352 because another path dominates. Both
removed, source restored exactly. Thirteen focused retained gates pass,
including bad-complement bit state. Qualified linked O2 remains 4,576 /
592 excess; production/defaults/README and unrelated Game work unchanged.

Init core-limit fitting trials: [Note 882](WORKING_NOTES/882-init-core-limit-predicate-and-local-lifetime-trials-20261004.md)
measures an unsigned workspace-distance gate and a local-limit variant.
Raw O2/O1 entry bodies save two/one words, but padding leaves core text
4,384/5,824 unchanged; local-limit raises O1 core bound from 352 to 360.
Both forms removed, source restored to the qualified blob. Twelve focused
retained tests pass; Notes 880/881 corpus evidence still applies to the
unchanged baseline. Linked O2 4,576 / 592 excess; production/README unchanged.

Init direct-load CU1-set corpus: [Note 881](WORKING_NOTES/881-init-direct-fpr-adapter-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed O2/g3 paired pages with masked CU1 set in
790.940 seconds, no skips. Together Notes 880/881 qualify 1,014 paired pages
across both masked modes, per-page callee-return guard active. Linked text
4,576 / 592 excess; observed descent 3,240 matches bound, minimum SP
0x80031D68 / known-neighbor margin 88. Eleven supporting gates pass and eight
source blobs hold. Both direct-load corpus gates checked off; fitting,
ownership, hardware/context and full reservation remain. Production/README unchanged.

Init direct-load CU1-clear corpus: [Note 880](WORKING_NOTES/880-init-direct-fpr-adapter-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 fresh packed O2/g3 paired pages with masked CU1 clear in
808.272 seconds, no skips. Linked text 4,576 / 592 excess; observed descent
3,240 matches bound, minimum SP 0x80031D68 / known-neighbor margin 88.
Eleven supporting gates pass and all eight recorded source blobs hold.
Direct-load CU1-clear checked off; matching CU1-set, fitting/ownership/
hardware/reservation remain open. Production/defaults/README unchanged.

Init direct FPR load adapter: [Note 879](WORKING_NOTES/879-init-direct-fpr-load-adapter-fitting-20261004.md)
adds opt-in LWC1 publication of sixteen stack words, reducing adapter body
and aligned text from 256 to 192 bytes. Packed O2/g3 linked text is 4,576,
592 over retail; core text/bounds stay unchanged. Separate word-load receipts
preserve existing context gates and default assembled text matches HEAD.
Fresh bounded suite: 36 passed / one corpus skip in 254.545 seconds;
eleven shared/default regressions pass. All six observed descents match bounds.
New-option full corpus, fitting/ownership/hardware remain open; Notes 877/878
qualify only the previous adapter. Production/README unchanged.

Init current callee-adapter CU1-set corpus: [Note 878](WORKING_NOTES/878-init-callee-adapter-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired pages with masked CU1 set
(0x2400FF00), 792.002 seconds, no skips. Together with Note 877 this
qualifies 1,014 paired pages across both masked modes, with callee-return
guard active on every page. Linked text 4,640 / 656 excess; observed descent
3,240 matches bound, minimum SP 0x80031D68 / neighbor margin 88. Sixteen
supporting gates pass; all source blobs hold. Current corpus gates checked
off; fitting/ownership/hardware/reservation remain. Production/defaults/README unchanged.

Init current callee-adapter CU1-clear corpus: [Note 877](WORKING_NOTES/877-init-callee-adapter-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired retail pages with masked
CU1 clear (0x0400FF00), 839.425 seconds, no skips. The callee-return boundary
guard runs on every page. Linked text 4,640 / 656 excess; observed descent
3,240 equals bound, minimum SP 0x80031D68 / known-neighbor margin 88.
Sixteen supporting gates pass; decoder/adapter/test blobs unchanged. Current
CU1-clear gate checked off; matching CU1-set now passes in Note 878, while
fitting/ownership/hardware remain open. Production/defaults/README totals unchanged.

Init pointer/argument ownership trials: [Note 876](WORKING_NOTES/876-init-unretained-pointer-argument-ownership-trials-20261004.md)
measures direct input argument, workspace address from state and their
combination. Neither aggregate profile improves; workspace-only grows O1
sixteen bytes. Two corresponding adapter-store omissions shrink body to 248
but aligned text stays 256, linked O2/O1 stays 4,640/6,080. Both sources
restored exactly; fifteen focused retained-config gates pass. No trial
semantic qualification, new option or production count change; current corpus
and fitting/ownership/hardware remain open.

Init callee-preserving adapter fitting: [Note 875](WORKING_NOTES/875-init-callee-preserving-core-adapter-fitting-20261004.md)
adds opt-in omission of ten duplicate S0-S7/GP/FP reloads, retaining saved
frame cells and RA restoration. Adapter body/aligned text is 256/256 versus
296/304; all six shapes save 48 linked bytes, packed O2 4,640 / 656 excess.
All observed descents match bounds. Fresh whole suite has 34 passes / one
corpus skip; strengthened instruction-clobber guard and sixteen helpers pass.
The initial mistaken S0-reload probe is documented. Omitted-option adapter
text matches baseline. Changed corpus and fitting/ownership/hardware remain;
production/defaults/README unchanged, unrelated Game work preserved.

Init lookup exit-shape trials: [Note 874](WORKING_NOTES/874-init-lookup-exit-shape-and-offset-predicate-trials-20261004.md)
measures child-gated common return and offset predicates on Note 873.
Common return saves raw helper words, but neither form reduces complete
packed text or core bounds; both removed with exact source restoration.
Operation caching is ruled out by the single existing load. All 256 byte
classifications pass a host algebra probe; fifteen restored-config gates pass.
Retained option remains 4,688 linked O2 / 704 excess, changed corpus open.
Production/defaults/README unchanged; unrelated Game work preserved.

Init explicit-first-refill lookup fitting: [Note 873](WORKING_NOTES/873-init-explicit-first-refill-lookup-fitting-20261004.md)
adds opt-in `--lookup-first-refill` (requires shared lookup). Packed O2/O1
core save sixteen bytes; linked O2 is 4,688 / 704 excess. No shape grows
linked text or stack; all six observed descents match static bounds. Final
guest run: 33 passes / one corpus skip in 241.971s, plus sixteen supporting
passes. Omitted-option O2/O1 text matches qualified baseline exactly.
Notes 871/872 qualify that baseline, not this changed option; changed corpus
and fitting/ownership/hardware remain open. Production/defaults/README unchanged.

Init current allocation-table CU1-set corpus: [Note 872](WORKING_NOTES/872-init-allocation-table-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired pages with masked CU1 set
(status 0x2400FF00), 804.532 seconds, no skips. Together with Note 871 this
qualifies 1,014 paired pages across both masked modes on unchanged current
source. Text 4,704 / 720 excess; observed descent 3,240 matches bound,
minimum SP 0x80031D68 / known-neighbor margin 88. Fifteen supporting gates
pass. Current full corpus gates checked off; fitting/ownership/hardware/
complete-reservation and resume gates remain. Production/defaults/README unchanged.

Init current allocation-table full corpus: [Note 871](WORKING_NOTES/871-init-allocation-table-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 freshly compiled packed-remaining O2/g3 paired retail pages
with exception-masked CU1 clear (status 0x0400FF00), 798.099 seconds, no skips.
Linked text 4,704 / 720 excess; observed descent 3,240 equals bound, minimum
SP 0x80031D68 / known-neighbor margin 88. Fifteen helper/selection tests pass.
This qualifies the current toggle/parent-cursor/allocation-table combination,
not merely the earlier source. Its CU1-set follow-up now passes in Note 872;
fitting/ownership/hardware gates remain open. Production/defaults/README totals unchanged.

Init stride-only replication trials: [Note 870](WORKING_NOTES/870-init-rejected-stride-only-replication-capture-20261003.md)
rejects standalone stride capture with indexed for or gated do/while fills.
Both add eight bytes to builder frames and core call bounds; neither improves
text across profiles. Source restored exactly. Fresh retained-config guest
suite passes 32 tests / one intentional corpus skip in 260.739 seconds;
all six observed descents match bounds, packed O2 linked text stays 4,704.
Production/defaults/README unchanged; full changed corpus remains open.

Init remaining helper subsets: [Note 869](WORKING_NOTES/869-init-rejected-take-bits-mask-and-drop-inlining-20261003.md)
rejects mask-only and mask-plus-drop inlining inside take_bits. Mask-only
holds O2 but grows O1 16 bytes; combined grows both 32 bytes, with no core
call-bound benefit. All three mask/drop subsets now have current-base
receipts. Source restored exactly, fourteen focused gates pass; no retained
option, production conversion or README count change. Continue structural
dataflow/caller fitting rather than repeating these subsets.

Init shared-helper fitting: [Note 868](WORKING_NOTES/868-init-rejected-take-bits-drop-inlining-20261003.md)
rejects drop-only inlining inside take_bits: packed O2 grows 16 core bytes,
O1 grows 32, with no core call-bound improvement. Source is restored exactly
to HEAD and fourteen focused gates pass. Fresh inventory remains 492 C /
47 assembly rows, with 12,252 assembly bytes. No production conversion;
the two small candidates still lack full-slot matching C, and the retained
decompressor experiment remains 720 linked bytes over budget. README unchanged.

Init table-derived allocation fitting: [Note 867](WORKING_NOTES/867-init-builder-table-derived-allocation-fitting-20261003.md)
adds opt-in direct table/header/commit dataflow. Packed O2 falls to 4,704
linked bytes / 720 excess, public builder 333 words; packed O1 text holds.
All six stack bounds hold. The new observer is corrected to retail's s3
counter at 0x10006C38, not its once-at-return FPR19 write, and ordered
allocation values pass across six builds. Fresh corrected guest run has
32 passes / one corpus skip, plus fourteen helper passes; all observed
descents match bounds. Omitted-option text matches baseline. Defaults/production/
README totals unchanged; changed corpus and fitting/ownership/hardware remain open.

Init parent-ascent cursor fitting: [Note 866](WORKING_NOTES/866-init-parent-ascent-offset-cursor-fitting-20261003.md)
adds opt-in descending parent-offset traversal. Packed O2 falls to 4,720
linked bytes / 736 excess with unchanged 392-byte core bound and 200-byte
builder frame. Packed O1 text/bound hold. Other profiles are mixed: frame
O2 saves 32 bytes; frame/aligned O1 grow 16, and aligned bounds grow eight.
Active root-descent and short-tree guard checks pass; 31 guest tests pass,
one corpus skip, plus fifteen focused passes. All observed descents match
static bounds. Rejected mask-reuse forms are removed, omitted-option text
matches baseline. Defaults/production/README totals unchanged; corpus and
fitting/ownership/hardware remain open. Unrelated Game work preserved.

Init current cache/sort fitting: [Note 865](WORKING_NOTES/865-init-toggle-cache-interactions-and-rejected-sort-cursors-20261003.md)
re-measures cache and parent/sorted-array interactions on the changed Note
864 base. All 44 fresh object receipts are no better than the base on
O2/O1 text and stack bound. Both new sorted-length cursor loops are worse
and removed; experiment source is restored exactly. Sixteen focused gates
pass, no skips. Packed O2 stays 4,736 / 752 excess; next structural targets
are allocation/parent ascent and shared-call overhead. Defaults/production/
README totals unchanged; unrelated Game work preserved.

Init reversed-code increment fitting: [Note 864](WORKING_NOTES/864-init-builder-reversed-code-toggle-first-loop-20261003.md)
adds opt-in toggle-first increment. Packed O2 public builder falls 341 to
338 words, with padding holding linked text at 4,736 / 752 excess. Packed
O1 saves 16 linked bytes, frame O1 32, aligned O2/O1 16; all stack bounds
hold. Exhaustive 131,070 host code/mask pairs pass; final checks are 44
pass / one corpus skip, with all observed descents matching static bounds.
Both omitted-option text sections
match the banked baseline. Notes 862/863 remain qualification for that
baseline, not this changed option. Defaults/production/README totals unchanged.

Init revised offset-sum CU1-set corpus: [Note 863](WORKING_NOTES/863-init-offset-sum-full-masked-cu1-set-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 retail pages with masked CU1 set
in 814.477 seconds. With Note 862, both masked modes now bank 1,014 paired
page executions for the unchanged Note 861 source. Terminal text/descent/
known-neighbor clearance match at 4,736/3,240/88. Sixteen corpus/helper
checks pass, no skips. Return to builder/shared-helper fitting: 752 linked
bytes remain over retail. Other profiles and ownership/hardware remain open;
production/defaults/README totals unchanged, unrelated Game work preserved.

Init revised offset-sum CU1-clear corpus: [Note 862](WORKING_NOTES/862-init-offset-sum-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 paired retail pages with
exception-masked CU1 clear in 790.137 seconds. This covers the Note 861
repeat-value/offset-sum/reused-accumulator combination, not the older build.
Terminal text/descent/known-neighbor clearance are 4,736/3,240/88; sixteen
corpus/helper checks pass with no skips. Matching CU1-set corpus is now
banked in Note 863 above.
Further fitting (752 bytes), other profiles and ownership/hardware remain
open. Production/defaults/README totals unchanged; unrelated Game work preserved.

Init offset accumulator stack recovery: [Note 861](WORKING_NOTES/861-init-builder-offset-accumulator-lifetime-stack-recovery-20261003.md)
reuses the dead availability variable in the opt-in prefix loop. All text
sizes hold; aligned O2/O1 and packed O2 call bounds fall eight bytes.
Packed O2 retains 4,736 linked bytes / 752 excess with restored 392-byte
core bound, 200-byte builder frame and 88-byte known-neighbor clearance.
Fresh checks pass: 43 tests, one corpus skip; all observed descents match
static bounds and both omitted-option text sections match the banked baseline.
This supersedes Note 860's stack penalty, not its historical evidence.
Notes 862/863 now qualify both masked corpus modes for this packed profile.
Defaults/production/README totals remain unchanged; further fitting and
other-profile/ownership/hardware gates stay open.

Init builder offset-sum fitting: [Note 860](WORKING_NOTES/860-init-builder-running-offset-sum-text-stack-tradeoff-20261003.md)
adds an opt-in unsigned prefix sum. Packed O2 linked text falls to 4,736,
752 over retail, but its call bound grows from 392 to 400 and known-neighbor
clearance falls from 88 to 80 bytes. The unchanged 4,752-byte baseline stays
available; this is a text/stack tradeoff, not a dominating or production
replacement. Ordered prefix stores pass all six shapes at depth boundaries.
Fresh checks pass: 43 tests, one intentional corpus skip; observed packed
descent matches its 3,248-byte bound. Changed full corpus,
further fitting and ownership/hardware gates remain open. Defaults/totals unchanged.

Init rejected copy/refill fitting: [Note 859](WORKING_NOTES/859-init-rejected-match-copy-refill-trials-and-size-ledger-20261003.md)
measures four dataflow variants; none improves the selected packed profile.
All trial branches/selectors are removed and the committed Note 858 source
is restored exactly. Fresh baseline and fifteen focused checks pass. Ledger
separates 464 core-excess bytes plus 304 adapter bytes: best linked text stays
4,752, 768 over retail. Next fitting target is builder/shared-call overhead;
its 415-word region includes a 343-word public body and 72 helper words.
Fresh changed-fill corpus/ownership/hardware remain open; defaults/totals unchanged.

Init dynamic repeat fill fitting: [Note 858](WORKING_NOTES/858-init-dynamic-repeat-value-selection-and-cursor-end-fill-20261003.md)
retains opt-in once-selected repeat values and cursor-end fills after the
overflow gate. Frame O2 saves 32 linked bytes, aligned/packed O2 16, all
O1 32; stack costs stay unchanged. Best bounded-qualified O2 is 4,752,
768 over retail. The dynamic body fits its 257-word slot by size only.
All 504 contexts, 132 builders and ordered zero/nonzero staging writes pass:
43 tests pass, one corpus skip. Notes 856/857 remain full qualification for
the prior 4,768-byte no-new-option build, not this changed fill. Fitting and
fresh corpus/ownership/hardware gates remain open; production/defaults/totals unchanged.

Init current-combination CU1-set corpus: [Note 857](WORKING_NOTES/857-init-simple-seed-full-masked-cu1-set-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 retail-page comparisons with
exception-masked CU1 set in 784.455 seconds. Notes 856/857 bank both masked
modes for the current combination: 1,014 paired runs. Both receipts retain
text/descent/clearance 4,768/3,240/88; corpus/helper checks this turn total
fourteen pass, no skips. Return to structural fitting: 784 linked bytes
remain over retail. Other-profile/ownership/hardware/resume gates stay open;
production/defaults/README totals unchanged.

Init current-combination CU1-clear corpus: [Note 856](WORKING_NOTES/856-init-simple-seed-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 retail pages on freshly compiled packed/remaining O2/g3
with exception-masked CU1 clear in 800.807 seconds. Linked text/descent/
clearance remain 4,768/3,240/88. Full context, memory and poisoned-state
checks pass; corpus/helper checks total fourteen pass, no skips. This is
new evidence for Note 855, not reassigned histogram-only receipts. Changed
CU1-set corpus and 784-byte fitting gap remain open, along with other-profile/
ownership/hardware gates. Production/defaults/README totals unchanged.

Init option interaction fitting: [Note 855](WORKING_NOTES/855-init-cache-interaction-matrix-and-simple-seed-combination-20261003.md)
measures all 32 cache/builder combinations on both packed profiles. Adding
only existing arithmetic simple-operation selection wins all size/bound
metrics. All O2 links save 16; O1 saves 32/32/16, with unchanged stack costs.
Best packed O2 is 4,768, 784 over retail; descent/clearance remain 3,240/88.
All 492 bounded contexts and 132 builders pass, including literal/EOB and
signed stale-word cells. Final module/helper/default checks: 42 pass, one
corpus skip. Fitting and changed corpus/ownership/hardware remain open;
production/source bodies/adapter/defaults/README totals unchanged.

Init ABI seed fitting: [Note 854](WORKING_NOTES/854-init-abi-seed-pointer-cursor-and-ordered-register-copy-20261003.md)
retains an opt-in six-word seed pointer cursor with ordered read/write gates.
Frame O2 saves 64 linked bytes; aligned/packed O2 save eight stack bytes.
O1 grows 32/32/16 linked bytes with unchanged bounds. Best packed O2 remains
4,784, 800 over retail; observed descent improves to 3,240, clearance 88.
All bounded gates pass: final module/helper/default checks total 41 pass,
one corpus skip. Structural fitting and changed corpus/ownership/hardware
remain open; production, adapter, defaults and README totals unchanged.

Init adapter state fitting: [Note 853](WORKING_NOTES/853-init-core-owned-state-initialization-and-adapter-fitting-20261003.md)
omits six redundant adapter stores behind an opt-in assembler symbol.
Poisoned fields and read-before-write checks pass all 492 bounded contexts;
default adapter object stays byte-identical. All six linked images save 16:
best packed O2 is 4,784, 800 over retail, with unchanged stack depth.
Final bounded/helper/default checks: 39 pass, one corpus skip. Structural
fitting and changed corpus/ownership/hardware remain open; production,
defaults and README totals unchanged.

Init dynamic repeat fitting: [Note 852](WORKING_NOTES/852-init-dynamic-shared-repeat-extraction-and-stack-fitting-20261003.md)
retains opt-in shared repeat extraction. All O2 shapes save eight stack bytes;
all O1 shapes grow eight. Aligned O2 saves 16 linked bytes, while best packed
O2 remains 4,800, 816 over retail. All 492 bounded contexts, 114 builders,
six initializers and 48 direct header/alignment comparisons pass. Active
codes 16/17/18 and each overflow are verified; final module/helper checks:
36 pass, one corpus skip. Changed corpus and structural fitting remain open;
production, defaults and README totals unchanged.

Init stored length fitting: [Note 851](WORKING_NOTES/851-init-stored-shared-length-extraction-and-failure-bit-state-20261003.md)
retains opt-in shared 16-bit extraction with explicit failure-count restoration.
All O1 linked builds shrink 32, frame O2 16; best packed O2 stays 4,800,
816 over retail after padding. All 444 bounded contexts, 114 builders, six
initializers and 48 direct header/alignment comparisons pass. A delay-slot-aware
gate proves bad/valid restoration behavior; final module/helper checks total
35 pass, one corpus skip. Structural fitting and changed corpus/hardware/
ownership remain open; production, defaults and README totals unchanged.

Init packed header fitting: [Note 850](WORKING_NOTES/850-init-byte-packed-header-load-and-unaligned-core-qualification-20261003.md)
retains opt-in byte-packed guest header loads with enforced (4,1) layout and
actual LWL/LWR pairs. All six linked images shrink 32; best O2 is 4,800,
816 over retail, with unchanged stack bounds. All 432 bounded contexts,
114 builders, six exact initializers and 48 direct unaligned/header-format
comparisons pass. Negative layout and helper/ledger checks pass: 34 tests
pass, one corpus skip. Changed corpus and hardware/ownership remain open;
production, defaults and README totals unchanged.

Init stream fitting: [Note 849](WORKING_NOTES/849-init-stream-masked-dispatch-and-buffered-byte-rewind-fitting-20261003.md)
combines opt-in masked dispatch and buffered-byte rewind. Best linked O2 is
4,832, leaving 848 over retail; all six shapes shrink 16 with unchanged stack
bounds. All 432 bounded contexts, 114 builders and six exact initializers pass:
17 tests pass, one corpus skip. A zlib-valid constructed stream proves rewind
executes (11 bits, one byte, three remaining); sampled retail pages did not.
Continue fitting; changed corpus and ownership/hardware remain open.
Production, defaults and README totals unchanged.

Init fixed-length pointer fitting: [Note 848](WORKING_NOTES/848-init-fixed-length-pointer-ranges-and-complete-table-qualification-20261003.md)
retains an opt-in four-range pointer initializer. Best packed O2 linked text
falls to 4,848, leaving 864 over retail; O1 grows 48 bytes. All 420 bounded
contexts, 114 direct builders and six complete initializer comparisons pass:
16 tests pass, one corpus skip. Exact 318-store sequence, all 2,632 table
bytes and unchanged stack bounds are verified. Continue fitting; changed full
corpus and ownership/hardware remain open. Production/defaults/totals unchanged.

Init builder operation fitting: [Note 847](WORKING_NOTES/847-init-builder-operation-selection-fitting-and-rejected-dataflow-trials-20261003.md)
retains opt-in arithmetic operation selection. All 420 bounded contexts and
114 direct builder comparisons pass; 15 tests pass, full corpus skips.
Frame/aligned O2 shrink 32/16 bytes; all O1 shapes shrink 16. Packed O2 builder
saves two words but padding absorbs them: best linked text remains 4,864,
880 over retail. Prefix/countdown trials are removed. New-option full corpus,
fitting and ownership/hardware remain open; production/defaults/totals unchanged.

Init histogram CU1-clear corpus: [Note 846](WORKING_NOTES/846-init-histogram-cursor-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 changed packed O2/g3 pages with masked CU1 clear in 768.820
seconds. Notes 845/846 now bank both masked CU1 modes: 1,014 paired runs.
Text/descent/clearance remain 4,864/3,256/72. Return to builder/shared-helper/
adapter fitting; 880 linked bytes remain. Other profiles, complete ownership
and hardware/resume remain open. Production and README totals unchanged.

Init histogram full corpus: [Note 845](WORKING_NOTES/845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md)
passes all 507 retail pages on the changed packed/remaining O2/g3 source,
exception-masked entry with CU1 set. Terminal run: 744.102 seconds, linked
text 4,864, maximum descent 3,256, minimum SP 80031D58, neighbor clearance 72.
Next qualify CU1 clear, then continue fitting; 880 linked bytes remain over
retail capacity. Other profiles, complete reservations and hardware/resume
remain open. Production Init and README aggregates unchanged.

Init decoder histogram fitting: [Note 844](WORKING_NOTES/844-init-builder-histogram-cursor-fitting-and-bounded-qualification-20261003.md)
retains an opt-in histogram pointer loop, saving 16 packed core bytes in both
IDO profiles. Best linked text is 4,864, still 880 over retail capacity.
All 420 bounded stream/context and 114 direct builder comparisons pass;
15 tests pass, one intentional full-corpus skip. Packed O1 stack grows eight
bytes; O2 retains its 72-byte known-neighbor clearance. Changed full corpus,
fitting and complete ownership remain open. Inventory is still 492 C / 47
assembly rows; production and README totals unchanged.

Init debugger entry/footer: [Note 843](WORKING_NOTES/843-init-debugger-entry-frame-and-seeded-resume-footer-20261003.md)
executes retail early exits and explicitly seeded footer predicates. Frame is
`0x50` bytes with `0xFA8` image gap; completed paths restore saved registers/SP.
Conditional runnable, syscall-EPC advance and recognized-fatal outcomes pass.
All 62 focused tests pass. UI/TLB-generated premises, full hardware/resume and
reservations remain unproven. Next return to decoder fitting; production,
decoder/adapter and README totals unchanged.

Init diagnostic cleanup: [Note 842](WORKING_NOTES/842-init-post-diagnostic-page-state-cleanup-and-continuation-20261003.md)
executes real return-tail/table-clear/bitmap words under explicit external-call
stubs: unmap indices 2-31, 1,016 table zeros, correct bitmap masks and 513
inclusive cache operands. Zero/nonzero debugger result selects saved fault/
requeue continuation; static decoder bytes remain unchanged by CPU stores.
All 58 focused tests pass. Debugger entry, actual hardware/stubbed effects and
continuation execution remain open; production, fitting and totals unchanged.

Init diagnostic placement: [Note 841](WORKING_NOTES/841-init-diagnostic-overlay-placement-and-positive-pool-bounds-20261003.md)
executes retail overlay/SP/DMA/TLB argument arithmetic. Debugger reuses the
page pool at its next 64 KiB boundary, image 4960/SP 5958/mapping span 20000.
All 256 positive direct-count allocator cases back these extents; zero/tiny
pools do not inherit that bound. All 54 focused tests pass. Real DMA/TLB,
debugger/post-fault cleanup and complete ownership remain open; production,
fitting and README totals unchanged.

Init loaded table loop: [Note 840](WORKING_NOTES/840-init-retail-loaded-page-table-loop-write-footprint-20261003.md)
executes all 19 retail words over 508 offsets. Exactly 2,032 bytes are rewritten;
the 16-byte DMA tail and following input guard remain unchanged. Six relocated/
small-count cases and zero-count skip pass. All 41 focused tests pass. Actual
DMA/cache, other loaded writers, diagnostic storage and full reservation ownership
remain open; fitting, production and README totals unchanged.

Init block-local writer census: [Note 839](WORKING_NOTES/839-init-block-local-storage-writers-and-fr1-fixture-correction-20261003.md)
finds 55 Init/1 Debugger candidates, including 33 stores: startup pointer
publications, 35500 clear and wrapper saved context. Lexical tracking is not
all-path ownership proof. The callback fixture's old FPR-pair interpretation
is corrected to FR=1 and passes both IDO profiles. All 34 focused tests pass;
loaded-pointer/loop/diagnostic storage, complete ownership and fitting stay open.
Production and README totals unchanged.

Init static literal census: [Note 838](WORKING_NOTES/838-init-static-storage-literal-census-and-enclosing-bss-clear-20261003.md)
finds 9 Init and 1 Debugger adjacent literal pairs in the audited storage
interval; zero Game candidates is not absence proof. Startup clear-call
arguments cover enclosing BSS 8002D4B0..80043B40, not individual reservations.
All 17 focused tests pass. Scheduled-apart/computed/pointer/DMA writers and
complete capacities remain open; production, fitting and README totals unchanged.

Init syscall fault route: [Note 837](WORKING_NOTES/837-init-syscall-fault-dispatch-and-disabled-diagnostics-route-20261003.md)
executes ROM-pinned dispatch/fault/diagnostic-disabled slices. Syscall routes to
generic fault; state/flags become 1/2. With no event queue, control reaches the
scheduler boundary and seeded EPC remains at the syscall. Diagnostic bit 2000
instead enters the debugger body. All 32 focused tests pass. Full exception
entry, queued delivery, scheduling/resume, enabled diagnostics and reservations
remain unqualified; fitting and production/README totals unchanged.

Init real cleanup callback: [Note 836](WORKING_NOTES/836-init-retail-cleanup-callback-null-path-and-fatal-slot-20261003.md)
executes ROM-validated retail wrapper/renderer words with compiled Init sweep
C in both IDO profiles. Clearing the render-list global takes the null branch,
skips renderer frees and preserves sweep heap ownership in the fixture. The
fatal slot is pinned as syscall plus NOPs, not a returning C callback. All 28
focused tests pass. Async writes, syscall dispatch/resume, static reservations
and decoder fitting remain open; production and README aggregates unchanged.

Init guest tag lifetimes: [Note 835](WORKING_NOTES/835-init-guest-tag-sweep-and-retag-lifetime-contract-20261003.md)
qualifies both sweep bodies and the retag helper in fresh O2/g3 and O1 IDO
guest builds. Aging frees tag 2 and decrements 3/4; full sweep frees 1-4 while
preserving 5/FF. Pool/bitmap tag FF survives these sweeps. All 25 focused tests
pass. Real Game cleanup callback effects, fatal/reservation ownership and
fitting stay open; no production or README aggregate changes.

Init guest free/resize qualification: [Note 834](WORKING_NOTES/834-init-guest-free-reinsertion-and-resize-coalescing-20261003.md)
executes fresh, unguarded IDO C in both O2/g3 and O1 big-endian guest profiles.
All 512 private-heap resize cycles reclaim the heap; middle reinsertion,
two-sided coalescing and adjacent live payload/tag preservation also pass.
All 22 focused tests pass. Real fragmentation, tag-sweep/fatal lifetimes,
complete decoder ownership and fitting remain open. No production or README
aggregate changes; pending Game work is preserved.

Init page-pool retry contract: [Note 833](WORKING_NOTES/833-init-page-pool-retry-and-zero-count-fallback-contract-20261003.md)
pins the complete setup slot and executes success/retry/failure cases with
allocator stubs. Zero previous count can conditionally publish end=start-1;
native production-C tests show zero requests can allocate nonzero storage.
Positive requested counts therefore do not prove positive post-fallback count.
All 26 focused tests pass. No real failure reachability or complete ownership
claim; production, decoder/adapter, fitting and README aggregates unchanged.

Init storage boundaries: [Note 832](WORKING_NOTES/832-init-storage-boundaries-page-table-cache-and-output-pool-20261003.md)
executes pinned startup/table, cache-operand and output-pool arithmetic. The
2,048-byte table DMA ends at input start; max page DMA remains 3,072 with a
440-byte workspace gap. The inclusive cache sweep emits 257 operands and
crosses the workspace address range, so it is not input-capacity evidence.
Ten focused tests pass. Complete reservation/free-list/fallback/fault ownership
and fitting remain open; no production, decoder/adapter or README changes.

Init explicit CU1 corpus modes: [Note 831](WORKING_NOTES/831-init-explicit-corpus-cu1-modes-and-clear-full-pass-20261003.md)
adds set/clear/both selection with unchanged defaults and mode-local receipts.
All 507 masked CU1-clear pages pass loop-lookup packed O2 in 741.930 seconds;
text/descent/margin remains 4,880/3,256/72. That profile now has separate full
passes for both entry modes. Nine focused tests pass; ordinary corpus discovery
still skips. Other profiles, ownership/fault bounds and the 896-byte fitting
excess stay open. No production, decoder/adapter or README aggregate changes.

Init loop-lookup full masked corpus: [Note 830](WORKING_NOTES/830-init-loop-lookup-full-masked-corpus-20261003.md)
passes all 507 pages on the changed packed/remaining O2/g3 variant, masked
Status 0x2400FF00 and CU1 set, in 759.786 seconds. Linked text/descent is
4,880/3,256, lowest SP 0x80031D58, margin 72 bytes. Other full-corpus
profiles/mode, ownership/fault bounds and fitting remain open; 896 text bytes
over retail. No production, default-profile or README aggregate changes.

Init shared lookup loop: [Note 829](WORKING_NOTES/829-init-shared-lookup-loop-fitting-and-context-qualification-20261003.md)
adds an opt-in shape with 420 bounded context comparisons across six profiles
and both CU1 modes. Smallest linked text falls 16 bytes to 4,880 (896 over
retail); descent/margin remain 3,256/72. The nested-path gate executes. Across
two runs, 29 tests pass and one corpus test skips. At that checkpoint, full
changed-source corpus,
ownership/fault bounds and fitting remain open. Defaults and production unchanged.

Init shadow fitting: [Note 828](WORKING_NOTES/828-init-shadow-fitting-trials-and-helper-attribution-20261003.md)
rejects five size-only cursor/cache hypotheses; none reduces O2 text. All
temporary source edits are removed and restored compilation reproduces the
baseline. The builder's 424-word ledger includes 78 helper words; its actual
body is 346 words (53 over retail), narrowing the next fitting investigation.
Combined text remains 4,896 bytes; no new execution or production conversion.

Init full masked shadow corpus: [Note 827](WORKING_NOTES/827-init-full-masked-shadow-corpus-20261003.md)
passes all 507 retail pages with Status 0x2400FF00, CU1 set, and the
packed/remaining O2/g3 profile in 709.832 seconds. Linked text/descent remains
4,896/3,256, lowest SP 0x80031D58, neighbor margin 72 bytes. Other full-corpus
profiles/mode, complete ownership, synchronous-fault bounds and fitting remain
open. No production owner, implementation or README aggregate changes.

Init exception-entry masking: [Note 826](WORKING_NOTES/826-init-exception-entry-mask-and-masked-context-qualification-20261003.md)
executes the original IE/EXL clear prefix and pins the direct TLBL route.
Six profiles/both CU1 modes pass 72 new masked vector/sample comparisons,
bringing bounded shadow coverage to 420. All 29 focused tests pass. Corpus
context selection now distinguishes generic from exception-masked Status;
Note 825's full-page receipt remains generic, not relabeled. At this checkpoint,
full masked corpus,
storage ownership, synchronous-fault bounds and fitting stay open. No production
implementation, ownership, cost or README aggregate changes.

Init retail context footprint and first shadow corpus: [Note 825](WORKING_NOTES/825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
finds the SDK OSThread header is 0x1B0 bytes but retail's 32-FPR save/restore
footprint is 0x230. The neighbor guard now ends at 0x80031D10. All 507 pages
pass packed/remaining O2/g3 with CU1 set and that corrected guard: text/descent
4,896/3,256, lowest SP 0x80031D58, margin 72 bytes. All 23 focused tests pass;
the six-profile bounded shadow domain still passes 348 comparisons. Remaining
full-corpus profiles/mode, complete ownership and fitting stay open. No production
ownership, shared SDK header or README aggregate changes.

Init distance-builder/multiblock history: [Note 824](WORKING_NOTES/824-init-distance-builder-and-multiblock-fpr-history-20261003.md)
adds 144 gated context comparisons, bringing shadow coverage to 348 across
six profiles and both CU1 modes. Distance errors, accepted special trees,
multiple dynamic blocks, fixed/stored history and retained-snapshot errors pass.
Scratch f0-f11 are also checked before the wrapper's final f0 reload.
All 19 adapter/shadow/provenance tests pass. Costs and production ownership
are unchanged; full shadow corpus, actual storage ownership and fitting stay open.

Init semantic scratch-FPR publication: [Note 823](WORKING_NOTES/823-init-semantic-scratch-fpr-publication-20261003.md)
adds an opt-in 116-byte shadow state and 320-byte adapter. All 204 new bounded
context comparisons match retail across six compiled profiles, including both
CU1 modes, match-copy history, partial failures and three ROM samples.
All 110 focused tests pass, including the native all-retail-page semantic check.
Smallest combined text/descent is 4,896/3,256: still 912 text bytes over retail.
Full shadow corpus, original allocation ownership and fitting remain open.
Production Init stays 492 C / 47 assembly rows; README aggregates unchanged.

Init FPR/failure-frame recovery: [Note 822](WORKING_NOTES/822-init-fpr-provenance-and-failure-frame-corrections-20261003.md)
maps f1-f11 saves to actual live GPRs and dynamic decoding variables. Sorted
symbols now use retail signed comparisons; an opt-in frame variant preserves
the distance-root seed on literal-builder failure. All 103 focused tests pass,
including 90 matching seeded context runs and 30 unseeded frame-gap receipts.
Smallest seeded combined text/descent is 4,432/3,168, 448 text bytes over retail.
Scratch FPR publication, complete CU1-set compatibility, ownership and fitting
remain open. Production ownership and README totals unchanged.

Init original-call adapter: [Note 821](WORKING_NOTES/821-init-original-core-call-adapter-and-exception-context-20261003.md)
executes the retained exception wrapper around an isolated compiled-core adapter.
Sixty CU1-clear vector/retail-page context runs preserve full FPR/GPR state and
match decoding; six CU1-set probes expose remaining f1-f11 scratch differences.
All 95 focused checks pass. The adapter adds 224 linked text bytes: smallest
combined text is 4,384 (400 over retail), with observed/bounded core-call descent
3,144 bytes. Original storage ownership, CU1-set compatibility and fitting stay
open. Production Init assembly and README counts unchanged.

Init compiled retail corpus: [Note 820](WORKING_NOTES/820-init-all-retail-pages-through-compiled-guest-core-20261003.md)
passes all 507 retail pages through six linked IDO core images: 3,042 core
runs and compiled fixed initializations agree with retail, zlib and pristine
output. Maximum workspace writes are 3,564 bytes; maximum input reads are
3,057 bytes, with every run inside its own rounded DMA span (maximum 3,072).
All 83 focused regressions and 18 additional final-source representative core
runs pass. The note distinguishes the corpus-loaded fixture from its later
guard-seeding correction. Private buffers/O32 calls do not establish original
entry ABI, allocation ownership or hardware behavior. Production counts unchanged.

Init compiled connected paths: [Note 819](WORKING_NOTES/819-init-compiled-guest-stream-core-and-fixed-initializer-qualification-20261003.md)
executes 288 linked guest stream/core comparisons and 288 compiled fixed-table
initializations across six profiles. Stored/fixed/dynamic, mixed blocks, strict
limits, core alignment/workspace clamps and partial errors match retail. All
74 combined checks pass, including builder regressions. Full retail-page guest
replay and original-entry/hardware gates remain open; production counts unchanged.

Init compiled guest builder: [Note 818](WORKING_NOTES/818-init-compiled-guest-builder-differential-execution-20261003.md)
executes six fresh linked IDO builder images (three shapes, O2/g3 and O1) in
a bounded MIPS model. All 186 case/image comparisons agree with retail table/
scratch/state results and preserve saved O32 registers. All 63 combined tests
pass. This qualifies compiler words for the builder only, not connected guest
paths, original FPR entry ABI or hardware. Production counts/text unchanged.

Init builder symbol cursors: [Note 817](WORKING_NOTES/817-init-builder-symbol-cursor-and-capacity-qualification-20261003.md)
reaches packed remaining-count O2 4,160/376 (176 bytes over retail), trading
eight stack bytes for 32 text bytes. Aligned/end gives 4,192/360; retain uncached
no-cursor 4,224/352 as the lower-stack point. All 130 new native tests, two
rejection tests and twenty final-source guest compiles pass. Full-capacity
288-cell comparisons cover both cursor modes. Production owners/counts unchanged.

Init builder scan lead: [Note 816](WORKING_NOTES/816-init-builder-leaf-fill-and-bounded-length-scan-trials-20261003.md)
removes redundant bounds after the all-zero histogram return. Packed O2 reaches
4,192/368 and aligned 4,224/352, sixteen text bytes smaller at unchanged frame
bounds. Leaf-base capture gives no lead benefit. New unit/helper accounting
shows the old 413-word builder region contains 357 builder + 56 lookup words;
the scan trial has 352 + 56. All 135 focused tests and twenty final-source
guest compiles pass; production owners and README counts remain unchanged.
All 1,544 project tool tests pass at this checkpoint.

Init slot correction: [Note 815](WORKING_NOTES/815-init-decompressor-semantic-slot-ledger-correction-20261003.md)
adds generated retail/C slot accounting and guards the actual retail call roles.
Notes 812-813 had swapped dynamic `func_10006424` (257 words) with compressed
`func_10006E00` (167), and mislabeled the fixed wrapper. Cursor dynamic fits
at 220 words; compressed fits at 100. Builder's 413/293-word overrun is now
the main fitting target. Aggregate deficit remains 224 bytes; original-entry
ABI/storage gates and production Init assembly remain unchanged.
All 1,421 tool tests pass; eight fresh guest objects retain their text hashes.

Init lookup trials: [Note 814](WORKING_NOTES/814-init-dynamic-code-lookup-capture-and-inline-mask-trials-20261003.md)
qualifies full lookup capture, mask-only capture and inline mask calculation.
All 178 focused tests, all 1,415 project tool tests and 26 final-source guest
compiles pass, but no mode
improves O2 fitting. Inline removes the direct helper edge yet adds text;
captures increase stack. Retain cursor-only 4,208/368 and 4,240/352 comparison
points. Default hashes, production owners and README counts unchanged.

Init dynamic cursor lead: [Note 813](WORKING_NOTES/813-init-dynamic-length-base-and-pointer-cursor-trials-20261003.md)
improves packed/cached-builder O2 to 4,208 text bytes / 368-byte core call-frame
bound, 224 bytes over retail. Aligned cursor gives 4,240/352. Length base capture
alone or combined regresses stack. All 159 focused tests and 28 final-source
guest compiles pass, along with all 1,237 project tool tests. Cursor bounds
retain the 316-cell physical frame and
partial-error state. Production counts and original-entry ABI gates unchanged.

Init rolled-state trials: [Note 812](WORKING_NOTES/812-init-rolled-scratch-cache-and-local-allocation-trials-20261003.md)
reduces packed/bounded cached O2 text to 4,224 bytes, 240 over retail, at a
400-byte core call-frame bound. Uncached aligned remains the 4,256/384 lower-stack
lead. Local allocation capture gives no rolled benefit. All 102 focused tests
and all 1,078 project tool tests pass, along with 24 post-edit guest compiles.
A verified per-routine ledger distinguishes body/alignment words and exposes remaining
slot overruns and missing original wrappers. No production/README count change.

Init no-unroll lead: [Note 811](WORKING_NOTES/811-init-parent-byte-addressing-and-no-unroll-profile-20261003.md)
reduces frame-backed aligned/bounded O2 text to 4,256 bytes and core call-frame
bound to 384, leaving 272 bytes over retail. Parent byte addressing does not
improve it. All 71 focused native tests and 26 warning-clean guest compiles pass;
all 976 project tool tests also pass. Source and CLI dependency guards reject
byte-parent mode without frame tables. The new native checks cover
wrapped guest labels independently of native pointers. No production
conversion, original-entry hardware qualification or README count change.

Init workspace-base trial: [Note 810](WORKING_NOTES/810-init-builder-workspace-base-capture-trial-20261003.md)
adds opt-in pointer capture and 78 passing focused tests. Sixteen warning-clean
guest compiles and all 905 project tool tests pass. The guest receipts
show no text/stack improvement: aligned/bounded frame-backed O2
grows to 5,232 bytes / 408-byte core call-frame bound. Fewer workspace-field loads
are offset by more stack accesses. Default instruction bytes remain unchanged;
retain the previous uncached leads and exact production assembly.

Init combined builder qualification: [Note 809](WORKING_NOTES/809-init-decompressor-combined-builder-qualification-20261003.md)
tests aligned/packed entries with bounded shifts. All seventy focused tests and
all 827 project tests pass, along with eight warning-clean guest compiles.
Frame-backed packed O2 text is 5,184
bytes with a 408-byte core call-frame bound; aligned O2 is 5,200/400. Packing
trades sixteen text bytes for eight stack bytes and regresses O1 text. Its
607-word builder remains 314 words over retail, locating the main size deficit.
Production owners and README aggregates remain unchanged.

Init entry/shift trials: [Note 808](WORKING_NOTES/808-init-decompressor-entry-alignment-packing-and-bounded-shift-trials-20261003.md)
pins entry size/alignment/fields and tests direct leaf packing. Bounded builder
shifts improve frame-backed text to 5,200/5,424 bytes and core call-frame bounds
to 400/296 bytes, still overlong. All 757 tests pass, including sanitized
semantic/retail corpus and generated-tree checks; all 28 guest compiles are
warning-clean and default instruction bytes are unchanged. All modes remain opt-in; no
production owner or README aggregate change.

Init codegen trials: [Note 807](WORKING_NOTES/807-init-decompressor-flat-bit-helper-and-builder-base-codegen-trials-20261003.md)
measures a flat bit helper and two builder-base capture shapes. The smallest
frame-backed text is 5,216 bytes, still 1,232 over retail, with a larger builder
frame. Flattening reduces the stored-path frame bound but grows text. All remain
opt-in; no production conversion or README aggregate increase is claimed.
All 664 project tool tests pass, including 4,056 retail-page native C calls;
sixteen guest compiles are warning-clean and default object text is unchanged.

Init storage boundaries: [Note 806](WORKING_NOTES/806-init-exception-storage-boundaries-and-all-retail-core-page-survey-20261003.md)
extends the retained-core survey to all 507 retail pages; maximum workspace
write span is 3,564 bytes on page 50. A fresh guest probe measures SDK
`OSThread` at `0x1B0`, while retail 32-FPR context accesses extend to `0x230`.
Page-table DMA ends exactly at input; wrapper tests preserve the known context
footprint and numerical gap. These are observed boundaries, not allocation
capacity or a new production C conversion. README aggregates unchanged.

Init exception context: [Note 805](WORKING_NOTES/805-init-exception-decoder-fr1-full-width-fpr-context-model-20261003.md)
adds a connected FR=1 model using the actual wrapper/core words, full-width
FPR saves/reloads and explicitly unknown MTC1 upper halves. Both CU1 paths and
malformed streams are covered; the unconditional f0 delay load is preserved.
This is not hardware acceptance or allocation ownership. Production assembly,
README aggregates and the remaining C text/stack gates are unchanged.

Init retail page qualification: [Note 804](WORKING_NOTES/804-init-retail-page-dma-and-exception-core-address-qualification-20261003.md)
checks all 507 original Game pages against pristine decompressed bytes. Maximum
rounded DMA is 3,072 bytes, leaving 440 bytes before exception workspace.
Three selected retained-core calls pass at handler input/workspace/SP addresses;
all 98 Init tests pass. This is bounded model evidence, not full exception
context, allocation ownership or a production conversion. Aggregates unchanged.

Init frame-backed C: [Note 803](WORKING_NOTES/803-init-decompressor-frame-backed-c-and-guest-call-frame-bounds-20261003.md)
implements isolated physical scratch, guest table-address translation, and
fixed/dynamic root aliases. Fourteen frame-backed tests and all 95 Init tests
pass, including the maximum 316-cell domain and five call-analysis tests.
Guest state is 40 bytes plus a caller-owned `0xA88` frame; text is still
5,312/5,600 bytes. Conservative direct-call C frame bounds are 416/328 bytes,
excluding caller storage/adapter/context. No production owner changes;
text/stack generation and connected exception/adapter qualification remain open.
All 570 project tool tests and guest/tool/build/matcher checks pass; both
complete Init sections remain independently retail-exact.

Init decompressor frame mapping: [Note 802](WORKING_NOTES/802-init-decompressor-physical-frame-mapping-and-contract-tests-20261003.md)
adds an explicit physical `0xA88` view, guest/native offset checks, and nine
scratch/interface tests. All 76 Init tests pass. Sixteen table cells, 316
length cells, initializer output aliases, and pointer/index translation are
pinned; direct/wrapped modeled stack low-water is `0xA88`/`0xA98`.
All 551 project tool tests, guest layout checks, and project checks pass;
the linked matcher and both independent retail-exact Init sections are preserved.
The exception caller's unconditional FPR restore delay is preserved as an
open hardware-context boundary. This is not an adapter or production conversion;
next prototype frame-backed scratch C and qualify connected context ownership.

Post-pause Init assessment: [Note 801](WORKING_NOTES/801-init-post-pause-assembly-conversion-assessment-20261003.md)
freshly verifies 492 C / 47 assembly rows, all 67 Init tests, 492/492 exact C
functions, and both complete retail-exact Init sections. Bitmap/MMIO remain
small C-expressible candidates without a demonstrated matching replacement.
The tested decompressor C needs original ABI/frame recovery and a fitting
layout; SDK/boot/privileged assembly is not ordinary missing-C backlog.
No new Init conversion or aggregate change is claimed. Pending uncommitted
Game updater source/tests are preserved and outside this assessment.

Game actor-step dispatcher: [Note 800](WORKING_NOTES/800-game-actor-step-dispatcher-recovery-and-match-20261003.md)
replaces `func_1507C22C`'s zero-return placeholder with its 25-record scan and
conditional update dispatch. All 62 words match with seven independent address-
setup scheduling guards. Ten new tests, forty focused tests, and all 532 tool
tests pass; final argument-form rerun/build/matcher and section checks pass.
At the Note 800 checkpoint, connected updater/predicate placeholders remained
open, so it was not gameplay acceptance. Pending uncommitted `func_1507BDB0`
recovery needs its own final review, documentation, and coherent checkpoint;
the current Init assessment does not finish that Game handoff.
Init bitmap ordered-store trials in [Note 799](WORKING_NOTES/799-init-bitmap-volatile-store-scheduling-trial-20261003.md)
remain non-matching; production Init ownership and both exact sections are preserved.

Init guest-layout follow-up: [Note 798](WORKING_NOTES/798-init-decompressor-guest-layout-trial-and-conversion-boundary-20261003.md)
compiles the isolated decompressor with IDO O2/g3 and O1: 4,928/5,328 text bytes
versus the retained 3,984-byte region, with a 2,668-byte explicit state object.
Neither profile is an exact owner replacement. Two oversubscribed-tree fixtures
match the retained model; all nine semantic tests and all 522 tool tests pass. Both complete Init
sections remain independently retail-exact, and tool/build/matcher checks pass.
Init remains 492 C / 47 assembly rows. Next conversion work requires a new
bitmap/MMIO code-generation hypothesis or connected ABI/frame recovery; do
not repeat completed profile matrices or manufacture conversion with guards.

Init isolated C follow-up: [Note 797](WORKING_NOTES/797-init-connected-semantic-c-candidate-and-differential-oracles-20261003.md)
implements connected semantic decompression in an experimental, unlinked file.
Nine differential tests, all 67 focused Init tests, and all 522 tool tests
pass; tool checks pass.
Table/output/state comparisons include exceptional publication behavior.
Production remains exact assembly; guest layout/ABI and remaining malformed/
alias/context qualification precede any conversion claim.

Init connected-stream follow-up: [Note 796](WORKING_NOTES/796-init-dynamic-multiblock-and-core-entry-oracles-20261003.md)
adds eleven dynamic/mixed-block/core-entry tests; all 58 focused Init tests
and all 513 tool tests pass. Connected oracles now cover valid stored/fixed/dynamic streams,
repetition/error behavior, cursor rewind, both header skips, and saved-register
restoration. Production remains assembly. Next is isolated semantic C tested
against these oracles before any matching owner replacement.

Init compressed-decoder follow-up: [Note 795](WORKING_NOTES/795-init-compressed-decoder-fixed-stream-and-error-oracles-20261003.md)
adds ten fixed-stream/error oracle tests. All 47 focused Init tests, all 502
tool tests, and tool checks pass; both full Init sections remain retail-exact. Fixed streams match
zlib; output publication and malformed-stream differences are pinned as
bounded-model evidence. Production remains assembly; dynamic/multi-block/core
qualification precedes a connected C replacement.

Init table-builder follow-up: [Note 794](WORKING_NOTES/794-init-decompressor-table-builder-interface-and-canonical-oracles-20261003.md)
characterizes extra register inputs, table records, canonical lookups, and
fixed allocation indices explaining both retained root pointers. Nine builder
tests, all 37 focused Init tests, and all 492 tool tests pass; tool checks pass. Production remains
assembly; compressed-decoder/dynamic/error qualification is still required.

Init decompressor follow-up: [Note 793](WORKING_NOTES/793-init-decompressor-shared-contract-and-stored-block-oracle-20261003.md)
maps the shared frame and integer FPR contract and adds eight stored-block/
interface tests. All 28 focused Init tests, all 483 tool tests, and tool checks
pass; zlib stored
oracles cover payloads through 65,535 bytes. Production remains assembly.
Table-builder/fixed/dynamic/error qualification precedes connected C recovery.

Latest Init-only resume: [Note 792](WORKING_NOTES/792-init-resume-remaining-assembly-conversion-decision-20261003.md)
re-verifies all twenty focused Init tests, 492/492 exact C rows, and both
complete retail-exact sections. The 47 remaining assembly rows are unchanged.
Bitmap caller-domain and conditional allocator separation are characterized;
new matching code-generation evidence is needed for bitmap/MMIO conversion.
The other 45 rows are retained SDK/hardware or connected-interface work.
No new conversion, production Init edit, or README aggregate change is claimed.

Fresh `progress.csv` and linked retail comparison on 2026-10-03:

| Section | C functions | Raw assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,463 / 6,042 (90.42%) | 579 | 1,930,924 / 2,256,728 (85.56%) |
| Init | 492 / 539 (91.28%) | 47 | 151,796 / 164,048 (92.53%) |
| Game | 4,790 / 5,321 (90.02%) | 531 | 1,759,488 / 2,072,880 (84.88%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 3,271 / 5,463 (59.88%) | 0 | 2,192 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,598 / 4,790 (54.24%) | 0 | 2,192 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Game `func_1507C324` converts its retained nineteen-word assembly to semantic
nested float copy/clamp C. Eight stale-checked guards normalize only a closed
FPR permutation; the complete 76-byte slot remains byte-exact. Fourteen new
tests, thirty focused copy/clamp/dimension tests, and all 475 tool tests pass;
full rebuild/project checks pass. Earlier exact slots, ten non-matching hashes,
restored spans, and both Init sections are preserved. C count/bytes rise by
one/76 and exact-C count rises by one; README changes only aggregate tables.
Next inspect the connected `func_1507BDB0` / `func_1507C22C` placeholders before
recovering their interfaces. See
[Note 791](WORKING_NOTES/791-game-nested-float-copy-clamp-conversion-and-match-20261003.md).

Game dimension helper `func_1507C3E0` now replaces its empty body with retail
type/subtype selection, state overrides, distinct radii, attachment expansion,
optional scaling, and ordered nullable halfword outputs. Sixteen focused tests
and all 461 tool tests pass; build/project checks pass. It remains non-matching:
310 body words plus ten padding nops, 312 differences, no new guards/profiles.
The adjacent refresh wrapper and retained leaf remain exact; earlier Game
regressions and both complete Init sections are unchanged. Aggregates/README
were unchanged for that checkpoint. Its then-pending `func_1507C324` conversion
is completed in Note 791; dimension matching and whole-chain acceptance remain
open. See
[Note 790](WORKING_NOTES/790-game-actor-dimension-helper-semantic-recovery-20261003.md).

Init allocator `func_10003C6C` now corrects a duplicate twelve-byte header
addition in its rear-allocation C path, found by production-body host tests.
Six allocator tests establish conditional valid-heap separation from bitmap
configuration storage; all alignment classes and both directions are covered.
All twenty focused Init tests and all 445 tool tests pass.
The existing guarded retail layout is refreshed to 231 rows for the corrected
257-word C body and trailing nop. Full rebuild/matcher, independent allocator
and complete Init-section comparisons, and Game regressions pass. This is a
semantic correction, not an assembly-to-C conversion or direct compiler match;
Init/README aggregates are unchanged. See
[Note 789](WORKING_NOTES/789-init-bitmap-allocator-provenance-and-rear-bound-correction-20261003.md).

Init bitmap `func_10005BE0` now has eight instruction-word-driven contract tests,
including invalid-count and alias timing. The only direct retail resize call
has statically positive counts 107..362; indirect/external calls and allocator
provenance remain unproven. All fourteen focused Init tests, all 439 tool tests,
and project tool checks pass. Assembly ownership, section parity, aggregates,
and README are unchanged. Next establish allocator provenance and a new compiler/dataflow
hypothesis before conversion trials. See
[Note 788](WORKING_NOTES/788-init-bitmap-retail-caller-domain-and-edge-contract-20261003.md).

Game `func_1510F800` now explicitly forwards its s32 context argument to the
retained setter. All eight words remain directly byte-exact with no guards or
profile changes. Fifteen focused/integrated tests and all 431 tool tests pass;
build/project checks pass. Twenty-six earlier exact slots, nine prior hashes,
restored spans, and both Init sections are unchanged; the setter's retained
256-byte interval independently matches. Aggregates/README are unchanged.
Its then-pending dimension helper is semantically recovered in Note 790;
whole-chain acceptance and the earlier dispatcher/matrix/query matching remain
open. See
[Note 787](WORKING_NOTES/787-game-context-forwarding-interface-recovery-20261003.md).

Game `func_1504452C` replaces its zero-return placeholder with the three-vertex
offset/origin/coefficient transform, not a context dispatcher. All 75 words
match; twenty expected-word guards normalize only closed register cycles and
two independent origin-load schedules. Eleven focused tests and all 416 tool
tests pass; full rebuild/project checks pass. Earlier exact slots, nine prior
non-matching hashes, restored spans, and both Init sections are unchanged.
README matcher aggregates are updated. Its then-pending explicit context
forwarding is recovered in Note 787; the setter remains assembly and dimension
helper recovery remains open. See
[Note 786](WORKING_NOTES/786-game-three-vertex-transform-recovery-and-match-20261003.md).

Game `func_15044380` replaces its zero-return placeholder with the complete
actor/context dispatcher, preserving descending/optional ascending passes,
live eligibility, preparation-time context capture, and final reset/byte restore.
Fourteen focused tests and all 405 tool tests pass; build/project checks pass.
It remains non-matching: 107 body words, no padding, twenty differences, no new
guards/profiles. All 22 exact regression slots, eight prior non-matching hashes,
restored spans, and both Init sections are unchanged. Aggregate tables/README
are unchanged for that recovery. Its then-pending `func_1504452C` is recovered
as a vertex transform in Note 786. Dimension recovery and the context wrapper's
explicit argument remain open, so whole-chain acceptance is open. See
[Note 785](WORKING_NOTES/785-game-actor-context-dispatcher-semantic-recovery-20261003.md).

Game `func_15044660` replaces its false zero-return C placeholder with the
complete original actor-preparation assembly. All 156 words / 624 bytes match.
Special actor types load a stack word not initialized by the routine, so
ordinary C recovery needs a reachability/stack-provenance decision rather than
an invented index value. Its interface is void(actor, x, y, z), not s32(void).
The C count decreases by one; exact-C counts are unchanged. Its then-pending
dispatcher `func_15044380` is recovered in Note 785; its dimension helper
remains a placeholder. See
[Note 784](WORKING_NOTES/784-game-actor-preparation-restoration-and-stack-boundary-20261003.md).

Game `func_15047700` now replaces its empty body with the reflection look-at
matrix builder, retail-specific degenerate-axis branches, and complete
direction/color output with preserved padding. Fourteen focused tests and
all 388 tool tests pass; build/project checks pass. It remains non-matching:
282 body words plus six padding nops, 245 differences, no new guards/profiles.
Both matrix wrappers and nineteen earlier exact routines remain exact; seven
non-matching hashes, restored spans, and both Init sections are unchanged.
Next inspect the earlier actor/context placeholder cluster `func_15044380`
and its preparation dependency `func_15044660`. See
[Note 783](WORKING_NOTES/783-game-reflection-look-at-matrix-semantic-recovery-20261003.md).

The latest Init pause resume reassesses remaining assembly. Fresh inventory
still reports 492 C / 47 assembly rows; all 492 C rows and both complete Init
sections match retail. Six focused Init tests pass. Only bitmap `func_10005BE0`
and MMIO `func_100038E0` remain bounded ordinary-C candidates, with no proven
matching replacement. Prefer a genuinely new bitmap dataflow/provenance
hypothesis; do not repeat the completed compiler matrices. The follow-up at
clean baseline `21070c9` re-verifies both sections and six focused tests, and
records the bitmap's unchecked resize argument, configured-pointer lifetime,
and post-fill count reload. Caller-domain/allocator provenance remains open.
Production Init and
README aggregates are unchanged; pending Game work is preserved. See
[Note 782](WORKING_NOTES/782-init-pause-resume-conversion-assessment-20261003.md).

Game `func_15047390` now replaces its empty body with the complete SDK-grounded
look-at matrix builder, including retail's three exact-zero length fallbacks
and ordinary `sqrtf` calls. It remains non-matching: 188 body words plus two
padding nops, 171 differences, no new guards or compiler profiles. Twelve
focused tests and all 374 tool tests pass; full build/project checks pass.
The fixed-matrix wrapper is exact; nineteen prior exact neighbors, six
non-matching hashes, restored spans, and both Init sections remain unchanged.
Aggregate tables/README are unchanged. The then-pending reflection builder
`func_15047700` is now recovered in Note 783 and remains non-matching. See
[Note 781](WORKING_NOTES/781-game-look-at-matrix-semantic-recovery-20261003.md).

Game `func_150472C0` now converts retained assembly to the complete void
descriptor-to-height-result builder. All 52 words match directly without new
guards or profiles. It preserves the eighteen-byte coordinate copy, separate
flag expressions, post-publication state reload, and final value read. Eight
focused tests and all 362 tool tests pass; full build/project checks pass.
Eighteen exact neighbors, six non-matching hashes, restored spans, and both
Init sections remain unchanged. Its then-pending matrix builder
`func_15047390` is now recovered in Note 781 and remains non-matching. See
[Note 780](WORKING_NOTES/780-game-descriptor-height-result-builder-direct-match-20261003.md).

Game `func_1504715C` now replaces its zero-return placeholder with the complete
void actor-to-height-result builder. It copies or synthesizes the nine vertex
coordinates, preserves result padding, and publishes metadata/state/entity
ownership with retail's alias-sensitive read order. It remains non-matching:
85 body words plus four padding nops, 76 differences, no new guards/profiles.
Twelve focused tests and all 354 tool tests pass; full build/project checks
pass. Eighteen exact neighbors, five query hashes, restored spans, and both
Init sections remain unchanged. Aggregate tables and README are unchanged.
Its then-pending descriptor/result builder `func_150472C0` is now recovered
in Note 780; this actor builder's byte matching remains open. See
[Note 779](WORKING_NOTES/779-game-actor-height-result-builder-semantic-recovery-20261003.md).

Game `func_15046D00` now replaces its zero-return placeholder with the complete
outer highest-height combiner. All 161 words match directly without new guards
or profiles. Ties/unordered comparisons select the context-3 non-entity result;
both failure paths clear only flag bit 2. Twelve focused tests and all 342
tool tests pass; full build/project checks pass. Seventeen exact neighbors,
five non-matching query hashes, restored spans, and both complete Init sections
remain unchanged. Converted totals are fixed; one different C row becomes
exact. Its then-pending actor/result builder `func_1504715C` is now recovered
in Note 779 and remains non-matching. See
[Note 778](WORKING_NOTES/778-game-outer-highest-combiner-direct-match-20261003.md).

Game `func_1504697C` now replaces its zero-return placeholder with the complete
highest entity/terrain combiner. All 161 words match directly without new
guards/profiles. Both early rejection and the both-failed fallback clear only
flag bit 2, preserving state/value. Twelve focused tests and all 330 tool
tests pass; full build/project checks pass. Sixteen exact neighbors, four
entity-query hashes, restored spans, and both Init sections remain unchanged.
The terrain highest query retains its documented 76 differences and prior
hash. Converted totals are unchanged; one different C row becomes exact.
Its then-pending outer combiner `func_15046D00` is now recovered in Note 778. See
[Note 777](WORKING_NOTES/777-game-entity-terrain-highest-combiner-direct-match-20261003.md).

Game `func_150466F8` now converts retained assembly to the complete entity/
terrain lowest-height combiner. All 161 words match directly without new guards
or profiles. It snapshots both records before querying, interprets both
returns through their low byte, and gives terrain precedence on ties or
unordered comparisons. Failure clears only flag bit 2. Twelve focused tests
and all 318 tool tests pass; full build/project checks pass. Fifteen exact
neighbors, four entity-query hashes, restored spans, and both entire Init
sections remain unchanged. Its then-pending highest entity/terrain combiner
`func_1504697C` is now recovered in Note 777. See
[Note 776](WORKING_NOTES/776-game-entity-terrain-lowest-combiner-direct-match-20261003.md).

Game `func_15046460` now replaces its zero-return placeholder with the complete
highest-height combiner. All 166 words match directly with no new guards or
profile changes. Early rejection clears state/value and flag bit 2; the
both-failed fallback instead retains the selected record's state/value and
clears only bit 2. Ten new tests and all 306 tool tests pass; full build and
project checks pass. Prior recovered neighbors/spans and both entire Init
sections remain unchanged. Converted totals are unchanged; one different C
row becomes exact. Its then-pending entity/terrain combiner `func_150466F8`
is now recovered in Note 776. See
[Note 775](WORKING_NOTES/775-game-highest-height-combiner-direct-match-20261003.md).

Game `func_150461D0` now has its complete lowest-height combiner in semantic
C instead of retained assembly. All 164 words match directly without new
guards or compiler profiles. It snapshots both complete result records before
count preparation, truncates both query returns to bytes, and chooses the
lower height with second-result precedence on ties/unordered comparisons.
Ten new tests and all 296 tool tests pass; the full code build and project
checks pass. Neighboring recovered routines, collector/producer spans, and
both complete Init sections remain unchanged. Its then-pending highest-height
combiner `func_15046460` is now recovered in Note 775. See
[Note 774](WORKING_NOTES/774-game-lowest-height-combiner-direct-match-20261003.md).

Game `func_15045D48` now has its complete context-3 entity lowest-height query
in semantic C instead of retained assembly ownership. It uses scratch
`D_800D3830`, the exact retail lowest-height sentinel, state `3`, and a cached
entity pointer for the later flag read. Its 145-word slot contains 144 body
words plus one padding nop, with 72 differences and no new guards. Fifteen
new tests and all 286 tool tests pass; full code build and project checks pass.
Prior recovered spans and both complete Init sections remain exact. This adds
a converted row, not an exact match. Its then-pending combiner `func_150461D0`
is now recovered in Note 774; entity-query matching and gameplay qualification
remain open.
See [Note 773](WORKING_NOTES/773-game-context3-entity-lowest-height-query-recovery-20261003.md).

Game `func_15045AE4` now has the complete context-2 entity highest-height
query instead of a zero-return placeholder. It uses scratch `D_800D37E0`,
the retail -10000 sentinel, state `2`, and late entity-index/base reloads.
Its 153-word slot contains 150 body words plus three padding nops, with
88 differences and no new guards. Fifteen new tests and all 271 tool tests,
full code build, and project checks pass. Previously recovered spans and
both entire Init sections remain exact. Aggregate tables are unchanged.
Its then-pending `func_15045D48` is recovered semantically in Note 773;
matching and natural gameplay qualification remain open.
See [Note 772](WORKING_NOTES/772-game-context2-entity-highest-height-query-recovery-20261003.md).

Game `func_15045880` now has its complete entity-indexed lowest-height query
in semantic C, replacing retained assembly ownership. Its 153-word slot is
150 body words plus three padding nops, with 88 word differences and no new
guards. Fifteen new tests cover metadata, helper reloads, and result/candidate/
entity-table aliasing; all 256 tool tests, full code build, and project checks
pass. Earlier recovered spans and both entire Init sections remain exact.
This adds a converted row, not an exact C match. Its then-pending adjacent
`func_15045AE4` placeholder is recovered semantically in Note 772;
lowest/highest entity-query matching and gameplay qualification
remain open. See
[Note 771](WORKING_NOTES/771-game-entity-lowest-height-query-semantic-recovery-20261003.md).

Game `func_150470B0` and its four-argument dispatch `func_15046C00` now
match all 43 and 32 words directly from semantic C. Eleven new integrated
tests cover the opposite-bound cached query and both caller shapes; all 241
tool tests, full code build, and project checks pass. Correcting the existing
three-argument `func_1504530C` signature preserves its exact 120 bytes.
No new guards or profile changes; retained fallback assembly remains untouched.
Earlier recovered spans and both complete Init sections remain exact. Its
then-pending entity lowest-height query is recovered semantically in Note 771; the
highest-height entity query's 72 differences and gameplay acceptance are open.
See [Note 770](WORKING_NOTES/770-game-opposite-cached-height-query-and-dispatch-direct-match-20261003.md).

Game `func_15045800` now dispatches through the recovered cached-height
status query `func_15047004`. Both match directly from semantic C: 32 and
43 words, no new guards or profile changes. Twelve integrated tests exercise
the actual cached query, dispatch, and fallback wrapper; all 230 tool tests,
full code build, and project checks pass. Both sibling dispatch wrappers,
earlier recovered spans, and both complete Init sections remain exact.
Its then-pending opposite-bound query is completed in Note 770; downstream
entity-query matching and natural gameplay qualification remain separate.
See [Note 769](WORKING_NOTES/769-game-cached-height-query-and-dispatch-direct-match-20261003.md).

The resumed Init audit confirms 47 assembly rows / 12,252 bytes, with all
492 C rows exact and both complete code/data sections matching retail.
Only `func_100038E0` (44 bytes) and `func_10005BE0` (76 bytes) remain bounded
ordinary-C candidates; neither has a proven matching replacement after the
documented compiler trials. The other 45 rows retain SDK, hardware, boot, or
shared-register contracts. No Init source conversion is claimed. See
[Note 768](WORKING_NOTES/768-init-remaining-assembly-current-decision-20261003.md).

Game `func_15045780` is now semantic C and matches all 32 words directly,
without guards or profile changes. Five new tests cover the early-rejection
flag mask, two-count buffer, raw return forwarding, helper mutations, NaNs,
and all halfword selectors. All 218 tool tests and project checks pass;
both complete Init sections and previously restored spans remain exact.
The entity query retains its 72 differences. Its then-pending dispatch wrapper
`func_15045800` and cached query `func_15047004` are completed in Note 769;
natural gameplay qualification is separate. See
[Note 767](WORKING_NOTES/767-game-entity-height-wrapper-direct-match-20261003.md).

The shared-register entity producer and its return/cleanup closure now match
all 520 retail bytes across three entries. Explicit secondary-count pointer
types preserve both C helpers' exact bytes. This removes one false C inventory
row, not three, and does not add a C match. All 213 tool tests, full build, and project checks pass;
both complete Init sections and earlier collector/query spans remain exact.
Its then-pending `func_15045780` wrapper is converted in Note 767; gameplay qualification
and the entity query's 72 differences remain separate. See
[Note 766](WORKING_NOTES/766-game-entity-scan-producer-assembly-restoration-20261003.md).

Game `func_15045F8C` now has its complete entity-indexed highest-height query.
It remains non-matching: 144 body words plus one padding nop, 72 differences,
no new guards. Twelve new tests cover metadata, entity-address publication,
flag combinations, and alias-sensitive reloads. All 208 tool tests, full build, and project checks
pass; recovered neighbors, collector group, and both Init sections remain exact.
Matching aggregates did not change for that recovery. Its then-placeholder
upstream `func_150A6568` producer is restored in Note 766; natural wrapper
qualification remains open. See
[Note 765](WORKING_NOTES/765-game-entity-height-query-semantic-recovery-20261003.md).

Game `func_1504554C` now has its complete context-3 highest-height query.
All 114 words match with fifteen strict guards for the same closed compiler
layout sets as the preceding lowest-height query. Thirteen new tests and all
196 tool tests pass; full build and project checks pass. Recovered neighbors,
collector/context group, and both complete Init sections remain exact.
Its then-pending `func_15045F8C` is recovered semantically in Note 765; the
upstream producer and wrapper qualification remain open. See
[Note 764](WORKING_NOTES/764-game-context3-highest-height-query-recovery-20261003.md).

Game `func_15045384` now has its complete lowest-height query/result body.
All 114 words match with fifteen strict guards for a private spill slot,
closed count/index register swap, and equivalent vertex-copy pointer schedule.
Thirteen new tests and all 183 tool tests pass; the full build and project
checks pass. Neighbors, the collector/context group, and both whole Init
sections remain exact. Its then-pending `func_1504554C` query is completed
in Note 764. See
[Note 763](WORKING_NOTES/763-game-lowest-height-query-recovery-20261003.md).

The handwritten collector/context group now matches all 5,712 retail bytes,
replacing 23 placeholder entries across six inventory groups. All 167 tool
tests pass. This restores original code, not six new C conversions.
See [Note 760](WORKING_NOTES/760-game-collector-context-assembly-restoration-20261003.md).

The resumed Init assessment still finds 47 assembly rows / 12,252 bytes.
Only the 44-byte MMIO leaf and 76-byte bitmap leaf are bounded C candidates;
neither has a proven matching replacement. Both entire Init sections remain
exact. See [Note 761](WORKING_NOTES/761-init-resume-conversion-decision-20261003.md).

Twenty further partial-volatility/profile trials still do not match the
eleven-word MMIO leaf. All emitted store traces pass; original assembly stays
in production. Three new baseline regression tests and all 170 tool tests
pass. Both complete Init sections remain exact. Its then-pending Game
`func_15045384` recovery is now completed in Note 763; see
[Note 762](WORKING_NOTES/762-init-mmio-partial-volatility-trials-20261003.md).

Game `func_150450CC` now has its complete highest-height candidate selection,
vertex copy, optional metadata, and result-flag body instead of a zero-return
placeholder. It remains non-matching: 143 body words plus one padding nop fill
the 144-word slot, with 76 differing word positions and no new guards. Eleven
new tests and all 164 tool tests pass; the full build and project checks pass.
Previously recovered spans and both entire Init sections remain exact.
Matching aggregates were unchanged by that C recovery. Its then-placeholder
collector is now restored as original shared-register assembly in Note 760;
natural gameplay qualification remains separate. See
[Working Note 759](WORKING_NOTES/759-game-highest-height-query-semantic-recovery-20261002.md).

Game `func_15044CE4` now explicitly returns the overlap result to its record
callback caller. The complete 23-word span remains directly exact, without
guards. Six new tests cover every signed-halfword scale, result forwarding,
load/store aliasing, unrelated-byte preservation, and actual wrapper/overlap
integration. All 153 tool tests, the full build, and project checks pass;
all recovered neighboring spans and both entire Init sections remain exact.
Matching totals do not change. Its then-pending `func_150450CC` recovery is
now completed semantically, but remains non-matching, in Note 759. See
[Working Note 758](WORKING_NOTES/758-game-position-scale-overlap-wrapper-return-20261002.md).

Game `func_15044B78` now replaces its zero-return placeholder with the complete
oriented player/record overlap test. All 91 words match; six strict guards
remap three private integer stack slots without changing any other instruction.
Its angle helper `func_15048A40` now explicitly returns `f32` and remains exact
across all twelve words. Sixteen new 32-bit tests and all 147 tool tests pass;
the full build and project checks pass. Constructor, allocator, and list pass
spans remain exact, as do both entire Init sections. Its then-pending callback
return contract in `func_15044CE4` is now completed by Note 758. See
[Working Note 757](WORKING_NOTES/757-game-oriented-record-overlap-match-20261002.md).

The resumed Init audit rebuilt the production baseline and reconfirmed all
492 Init C rows and both entire Init code/data sections byte-exact. The 47
remaining assembly rows / 12,252 bytes include two deferred small-leaf C
experiments; neither has a proven matching replacement. No Init conversion
or aggregate change is claimed for that audit. Its interrupted Game draft
was preserved in stash object `5b554b70ce671454878a1025fec26b93ad457153`.
Note 757 now completes that recovery in production; retain the stash only as
historical WIP, not as a patch to apply over the completed source.
See [Working Note 756](WORKING_NOTES/756-init-resume-verification-and-conversion-boundary-20261002.md)
for the remaining groups, acceptance gates, and exact draft-resume command.

Game `func_15044A28` now replaces its zero-return placeholder with the complete
record-list callback/delay/lifetime pass. All 84 words match directly without
guards; constructor and allocator spans remain exact. Fifteen new 32-bit tests
cover mutation, cached-next traversal, unlink-before-release-mark ordering,
delay timing, and word wrap. All 131 tool tests, project checks, and the full
code build pass; both entire Init sections remain exact. Next downstream
dependency was `func_15044B78`, now completed by Note 757. See
[Working Note 755](WORKING_NOTES/755-game-record-list-processor-direct-match-20261002.md).

Game `func_15044964` now replaces its null-return placeholder with the complete
common-header allocator and tail-list registration routine. All 49 words
match directly from C without guards; its 37-word constructor remains exact.
Ten new 32-bit tests include the actual constructor-to-allocator path with
only the heap call mocked. All 116 tool tests, project checks, and the full
code build pass; both entire Init sections remain exact. Its then-pending list
processor dependency is now completed by Note 755. See
[Working Note 754](WORKING_NOTES/754-game-common-record-allocator-direct-match-20261002.md).

Game `func_150448D0` now replaces its zero-return placeholder with the complete
position/scale record constructor. All 37 words match directly from C under
the existing profile, without guards. Seven new 32-bit tests and all 106 tool
tests, project checks, and the full code build pass. Both entire Init sections
remain exact. At that checkpoint the common allocator still had a null-return
placeholder; Note 754 now completes that source dependency, without gameplay
qualification.
See [Working Note 753](WORKING_NOTES/753-game-position-scale-constructor-direct-match-20261002.md).

Game `func_15040CC8` now replaces its zero-return placeholder with the complete
thirty-record callback dispatcher and post-dispatch cleanup. It remains
non-matching: the 38-word retail slot routes to a 39-word semantic overflow
body. Eight new 32-bit tests and all 99 tool tests pass; the full code build
and project checks pass, and both entire Init sections remain exact. Aggregate
counts do not change because the placeholder already counted as C. Resume
ordinary recovery at `func_150448D0`; see
[Working Note 752](WORKING_NOTES/752-game-record-dispatcher-semantic-recovery-20261002.md).

Game `func_1501CDC0` now replaces its zero-return placeholder with the complete
row-destination byte fill. All 37 words match; two strict guards normalize
only independent opening arithmetic/counter scheduling. Six 32-bit behavior
tests cover stride, fill bounds, row isolation, duplicates, and pointer reloads.
All 91 tool tests, the full build, and project checks pass. Both entire Init
sections remain byte-exact. See
[Working Note 748](WORKING_NOTES/748-game-row-destination-byte-fill-match-20261002.md).

The resumed Init-only assessment reconfirms all 492 C rows and both entire
linked Init sections exact. Of 47 remaining assembly rows, two small leaves
are deferred C rewrite candidates: `func_100038E0` and `func_10005BE0`.
Neither has a proven matching replacement. The other 45 rows retain SDK,
privileged, shared-frame, or nonstandard-register contracts. No source or
progress totals changed; no rebuild was performed for this audit. The Init
experiment order and acceptance gates are in
[Working Note 749](WORKING_NOTES/749-init-remaining-assembly-resume-assessment-20261002.md).

Twenty additional isolated MMIO trials across five source shapes and four IDO
profiles also produce no exact `func_100038E0` body after resolving relocations
at the retail addresses. Production assembly remains unchanged. New results
include pointer-lifetime and return-delay evidence, not a completed conversion.
Resume the bounded Init experiments at bitmap leaf `func_10005BE0`; see
[Working Note 750](WORKING_NOTES/750-init-mmio-pointer-lifetime-profile-trials-20261002.md).

The bitmap follow-up completes 55 shape/profile comparisons without an exact
`func_10005BE0` body. All eleven source shapes pass 65 host behavior cases
twice each, but this is not a production conversion. Both small Init leaves
remain deferred pending a new source/compiler rationale. Keep the verified
assembly baseline; ordinary Game work can resume at `func_15040CC8`. See
[Working Note 751](WORKING_NOTES/751-init-bitmap-loop-mask-profile-trials-20261002.md).

Game `func_151DE85C` now replaces its zero-return placeholder with the complete
menu-state reset. All 35 words match directly from C without guards or a
compiler override. Five new tests cover call ordering, globals, object bytes,
call mutation, and repeated reset. All 85 tool tests, the full build, and
project checks pass. Both entire Init sections remain byte-exact. See
[Working Note 747](WORKING_NOTES/747-game-menu-state-reset-direct-match-20261002.md).

Game `func_151D2F00` now replaces its zero-return placeholder with the complete
descriptor-record constructor. All 36 words match; six strict guards normalize
only the independent allocator argument-setup schedule. Five new behavior tests
cover failure, forwarding, descriptor copy, bookkeeping resets, and every
flag-byte value. All 80 tool tests, the full build, and project checks pass.
Both entire Init sections remain exact. See
[Working Note 746](WORKING_NOTES/746-game-descriptor-record-constructor-match-20261002.md).

Game `func_151BD21C` now replaces its zero-return placeholder with the complete
owner/selector event handler. All 40 words match; nine strict entries normalize
register reuse, flag-store scheduling, and one inserted return-delay nop with
its two branch-displacement adjustments. Eight 32-bit source-behavior tests
and all 75 tool tests pass; the full build and project checks pass. Both complete
Init sections remain byte-exact. See
[Working Note 745](WORKING_NOTES/745-game-owner-selector-event-handler-match-20261002.md).

Game `func_151B1918` now replaces its zero-return placeholder with the complete
eleven-child-slot cleanup. All 35 words match; six strict guards normalize
one equivalent cursor-relative address and independent counter scheduling.
Seven new source-behavior tests execute the actual C in a freestanding
32-bit fixture, preserving the guest slot stride. All 67 tool tests, the
full build, and project checks pass. Both complete Init sections remain exact.
See [Working Note 744](WORKING_NOTES/744-game-eleven-child-slot-cleanup-match-20261002.md).

Game `func_151A4900` now replaces its zero-return placeholder with the complete
threshold-scaled record update. All 39 words match; eleven strict guards
normalize one independent counter-reload scheduling rotation and two
commutative multiply operand orders. Seven new source-behavior tests and all
60 tool tests pass, along with the full build and project checks. Both complete
Init sections remain byte-exact. See
[Working Note 743](WORKING_NOTES/743-game-threshold-scaled-record-update-match-20261002.md).

Game `func_15163504` now replaces its zero-return placeholder with position
publication from three independent float pointers followed by optional callback
dispatch. All 41 words match directly from C without guards or a compiler
override. Six source-behavior tests and all 53 tool tests pass; the full build
and project checks pass. Both complete Init sections remain byte-exact. See
[Working Note 742](WORKING_NOTES/742-game-position-publication-and-callback-direct-match-20261002.md).

Game `func_1515FFEC` now replaces its zero-return placeholder with the complete
41-word compact-record lifecycle: flags at `0x0E`, selector at `0x0F`, timer
at `0x12`, and callback table `D_8008B0D0`. Two strict guards normalize only
completion-flag spill width. The existing lifecycle fixture now tests both
record layouts independently; all 47 tool tests and the full build pass.
Both complete Init sections remain exact. See
[Working Note 741](WORKING_NOTES/741-game-compact-timed-callback-record-match-20261002.md).

Game `func_15158224` now replaces its zero-return placeholder with the complete
41-word timed-callback lifecycle using selector offset `0x12` and table
`D_8008AE00`. Two strict expected-word guards normalize only completion-flag
spill width across the callback. Eight new source-behavior tests and all 39
tool tests pass; the full build and linked comparison pass, and both complete
Init sections remain exact. See
[Working Note 740](WORKING_NOTES/740-game-secondary-timed-callback-record-match-20261002.md).

Game `func_15157FE8` now replaces its zero-return placeholder with the complete
dual projection-matrix emitter. All 36 words match directly from SDK-macro C
without guards or a profile override. Three source-behavior tests pass; all
31 tool tests and the full code build pass. Both complete Init sections remain
exact. See [Working Note 739](WORKING_NOTES/739-game-dual-matrix-emitter-direct-match-20261002.md).

Init `func_10001420` is now represented in semantic C and matches its complete
nine-word memory-clear slot. Six relocation-aware expected-word guards
normalize only the closed register allocation; no instructions are inserted
or removed. Three source-behavior tests pass, and both complete Init sections
remain byte-exact after the full rebuild. Init retains 47 assembly rows /
12,252 bytes. See
[Working Note 736](WORKING_NOTES/736-init-memory-clear-leaf-conversion-20261002.md).
Five bounded compiler trials for MMIO leaf `func_100038E0` preserve its
assembly ownership: none establishes a direct eleven-word C match. The best
count-matching trial still changes address reuse and the return delay slot.
See [Working Note 737](WORKING_NOTES/737-init-mmio-leaf-bounded-compiler-experiment-20261002.md).
Bitmap initializer `func_10005BE0` also remains assembly after three compiler
trials. The count-fitting candidate passes 65 host behavior cases but has no
direct match or completed extraction from the shared assembly owner. See
[Working Note 738](WORKING_NOTES/738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md).

Game `func_15145128` now matches all 50 words after restoring the retail
optional-length/reciprocal expression shape and output multiply order. Three
expected-word guards normalize only the leaf frame, fallback local address,
and stack restore. Nine source-behavior tests cover zero vectors, omitted
outputs, in-place operation, and output-pointer aliasing. The neighboring
cross product remains exact, and both complete Init sections remain exact.
See [Working Note 734](WORKING_NOTES/734-game-vector-normalizer-match-20261002.md).

Init `__n_CSPHandleMIDIMsg` now matches all 954 words directly from semantic
C, including Rare's custom envelope, oscillator, controller, and notification
paths. Restored interleaved audio data ownership places the physical jump
tables at their retail addresses; six original floats restore three omitted
constant slots. Direct whole-section comparison now confirms all 164,048
Init code bytes and all 17,376 initialized-data bytes byte-exact. This is
linked-image evidence, not a gameplay qualification or a claim that the
remaining original assembly must become C. See
[Working Note 733](WORKING_NOTES/733-init-midi-handler-and-complete-init-image-match-20261002.md).

The remaining Init assembly was reassessed in
[Working Note 735](WORKING_NOTES/735-init-retained-assembly-reassessment-20261002.md).
No further compiler-generated recovery is established. That audit identified
three small custom leaves as possible C rewrite experiments. Note 736 now
completes `func_10001420`; `func_100038E0` is deferred after bounded trials,
and `func_10005BE0` is deferred after its separate bounded experiment.
This distinction concerns C representation versus proven original provenance.

The supported Init C-conversion queue is complete. The ordinary Game overlap
dependency `func_15044B78` now matches all 91 words. Its record allocator,
position/scale constructor, and list pass remain exact, without gameplay
qualification of downstream callbacks. Its 23-word position/scale wrapper
`func_15044CE4` now explicitly forwards the result and remains directly exact.
`func_150450CC` now has a recovered semantic body but remains in the
non-matching queue at 76 real word differences. Audit its handwritten
`func_150A3A70` collector/cleanup group as a complete register-contract unit;
that dependency remains a placeholder. Another ordinary source recovery can
resume at `func_15045384`, without resolving that collector gap.
`func_15040CC8` has a recovered semantic body but remains in the separate
non-matching/overflow queue; its retail-slot matcher reports 36 differences.
Keep `func_150A76F0` in its handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue.

Init `__sinf` now matches all 112 words directly from SDK-grounded C in a
separate generated slice. A scoped linker anchor restores its original
constant block, which had drifted by `0x30` bytes behind absolute symbol
assignments. Direct comparisons confirm the complete routine and 224 bytes
of math/NaN constants. No word guards or compiler override are required.
See [Working Note 732](WORKING_NOTES/732-init-sdk-sine-recovery-and-constant-layout-match-20261002.md).

The Game timed callback lifecycle `func_1513B798` now matches its complete
41-word slot. It decrements the optional signed timer, dispatches the indexed
completion callback, and releases the record when either path completes. Two
guarded words normalize only IDO's completion-flag spill width across the
indirect call. See
[Working Note 728](WORKING_NOTES/728-game-timed-callback-lifecycle-match-20261002.md).

The Init sequence-event and tempo-meta handlers now match all 69 and 179
words. The meta body had been omitted by the static-function build path and
masked by an absolute assignment; explicit layout ownership restores it and
the correct call relocation. Its separate inventory row raises the Init
denominator to 539. Direct assembly review also corrects the previous
classification of `func_10006380`: it uses shared live-register and stack
state and retains assembly ownership. The follow-up audit recovered Init
`__sinf` as a second compiler-generated candidate. Both it and the 954-word
`__n_CSPHandleMIDIMsg` are now completed. The following audit separated optional
custom-leaf rewrites from the handwritten/shared-register remainder. See
[Working Note 731](WORKING_NOTES/731-init-remaining-assembly-conversion-triage-20261002.md) and
[Working Note 730](WORKING_NOTES/730-init-meta-handler-layout-and-assembly-provenance-correction-20261002.md).

The Game resource-descriptor chain callback `func_15133FD8` now matches its
complete 38-word slot. It walks the counted eight-byte descriptor array and
threads `func_15133EEC`'s display-list result through each entry. Three guarded
words normalize one commutative operand order and two independent scheduling
slots. See
[Working Note 727](WORKING_NOTES/727-game-resource-descriptor-chain-callback-match-20261002.md).

The Game resource-table prefix offset calculator `func_1510D374` now matches
all 36 retail words directly from C. It starts at linker base `D_1A37E0` and
sums the requested unsigned-halfword lengths from `D_80091D20`; IDO emits the
retail remainder loop and four-entry unroll without guards or a profile
override. See
[Working Note 726](WORKING_NOTES/726-game-resource-table-prefix-offset-match-20261002.md).

The Game owner-ID effect payload constructor `func_150F5C08` now matches all
36 retail words directly from C. It recovers the four-argument contract,
12-byte owner/ID payload, object allocation, and conditional payload copy
without guards or a profile override. The aggregate figures above already
included this live-tree match in the preceding measurement. See
[Working Note 725](WORKING_NOTES/725-game-owner-id-effect-payload-constructor-match-20261002.md).

The Game effect payload constructor `func_150F4D5C` now matches all 36 retail
words directly from C. It recovers the fixed five-argument contract, typed
12-byte payload, effect allocation, and conditional payload copy without
guards or a profile override. See
[Working Note 724](WORKING_NOTES/724-game-effect-payload-constructor-match-20261002.md).

The Game actor water-state flag transition `func_150DF820` now matches its
complete 40-word slot. It retains the staged actor-flag writes, tests the
attached actor's `in_water` byte, publishes the 750-unit state value, and
dispatches the dry-state transition when that value is already active.
Sixteen guarded words normalize one closed integer-register allocation chain.
See
[Working Note 723](WORKING_NOTES/723-game-actor-water-state-flag-transition-match-20261002.md).

The Game selector/vector output initializer `func_150B060C` now matches all
41 retail words directly from C. It stores the selector lookup, returns zero
on failure, and on success publishes two constants plus three converted
signed-halfword coordinates. No guards or profile override are required. See
[Working Note 722](WORKING_NOTES/722-game-selector-vector-output-initializer-match-20261002.md).

The Game special-event mode dispatcher `func_15015F40` now matches all 31
retail words directly from C. The retained `assets/23B040.bin` data establishes
the eight special events in its 38-entry table, and an object-specific rodata
anchor preserves retail table ownership without expected-word guards. See
[Working Note 721](WORKING_NOTES/721-game-special-event-mode-dispatch-match-20261002.md).

The Game sentinel coordinate distance `func_15086BD0` now matches its complete
40-word slot. It returns zero for either `0xFF` index and otherwise computes
the Euclidean distance between signed XYZ coordinates in two 16-byte records.
Thirteen expected-word replacements and two checked insertions normalize the
closed compiler schedule and retain retail's duplicate return. See
[Working Note 720](WORKING_NOTES/720-game-sentinel-coordinate-distance-match-20261002.md).

The Game object-control reset `func_150634E4` now matches all 35 retail words
directly from C. It canonicalizes an object through `D_800CC2D0`, clears two
attached-state bytes, dispatches controls `0x1D` and `0x1E`, and clears three
object-control bytes. The corrected typed pool contract and unsigned array
index recover retail's exact division and shift/add scaling without guards.
See
[Working Note 719](WORKING_NOTES/719-game-object-control-reset-match-20261002.md).

The Game sixteen-word varargs adapter `func_15042E3C` now matches all 36
retail words directly from C. Its true varargs signature homes the incoming
register arguments and lets IDO reproduce retail's four-way-unrolled aligned
copy into a local word array. No expected-word guards or compiler-profile
override are required. See
[Working Note 718](WORKING_NOTES/718-game-sixteen-word-varargs-adapter-match-20261002.md).

The Game trailing marked-record compactor `func_1503DDD0` now matches its
complete 40-word slot. It marks a selected 20-byte record with state bit `2`
and removes trailing marked records from the active count. Correcting
`D_800C6650` to its pointer-owned table contract restores retail indexing;
sixteen expected-word guards normalize one closed compiler loop schedule. See
[Working Note 717](WORKING_NOTES/717-game-trailing-marked-record-compactor-match-20261002.md).

The Game indexed resource lazy-loader `func_1503D774` now matches all 36 retail
words. It preserves existing entries in `D_800D1C90`, loads missing resource
kind `0x11`, returns two on failure, and publishes the wrapper's first pointer
on success. Six expected-word replacements and one checked omission normalize
the closed IDO result-publication schedule. See
[Working Note 716](WORKING_NOTES/716-game-indexed-resource-lazy-loader-match-20261002.md).

The Game table-pointer relocator `func_1503D484` now matches all 35 retail
words directly from C. It walks eight-byte records through sentinel `999`,
rebases each present pointer-like word through `func_1503D438`, and publishes
the record count in `D_800C5A90`. No expected-word guards or compiler-profile
override are required. See
[Working Note 715](WORKING_NOTES/715-game-table-pointer-relocator-match-20261002.md).

The Game slot-state updater `func_1502FD70` now matches all 40 retail words.
It restores the category-`0x1D` fast path, byte-state sentinel handling,
optional-object fallback, and scaled state increase. Correcting `D_800D2040`
to its byte-array contract restores the indexed accesses; seventeen
expected-word guards normalize only IDO sentinel allocation and fallback
scheduling. See
[Working Note 714](WORKING_NOTES/714-game-slot-state-updater-match-20261002.md).

The Game configurable randomized record spawner `func_1500F9D0` now matches all
37 retail words directly from C. It shares the random type and fixed allocation
contract of `func_1500F378`, but publishes the caller's fifth argument as the
record byte at `0x30`. See
[Working Note 713](WORKING_NOTES/713-game-configurable-randomized-record-spawner-match-20261002.md).

The Game randomized record spawner `func_1500F378` now matches all 37 retail
words directly from C. It selects a random type in `10..137`, allocates the
fixed-form record, and publishes four signed halfword values plus its active
byte. No expected-word guards or compiler-profile override are required. See
[Working Note 712](WORKING_NOTES/712-game-randomized-record-spawner-match-20261002.md).

The Game paired object-state transition `func_150CF0A0` now matches all 40
retail words directly from C. Depending on the caller's low state bits, it
either dispatches the existing-state handler or gates and sets objects `0xFE`
and `0xFD` to state two. No expected-word guards or compiler-profile override
are required. See
[Working Note 711](WORKING_NOTES/711-game-paired-object-state-transition-match-20261002.md).

The Game delta-intensity limiter `func_150BA424` now matches all 39 retail
words directly from C. It rejects a negative float delta, derives and caps two
scaled intensity candidates, writes their minimum to byte field `0x5C`, and
retains retail's unsigned-byte result check. No expected-word guards or
compiler-profile override are required. See
[Working Note 710](WORKING_NOTES/710-game-delta-intensity-limiter-match-20261002.md).

The Game plane-side predicate `func_150A2E4C` now matches all 38 retail words.
It converts the signed origin coordinates, evaluates the plane expression, and
returns whether the result is non-positive. Twenty expected-word guards
normalize IDO's floating-point register allocation and instruction schedule;
the linked 152-byte span is identical to retail. See
[Working Note 709](WORKING_NOTES/709-game-plane-side-predicate-match-20261002.md).

The Game path-state routines `func_150778F0` and `func_1507A528` now match all
46 and 62 retail words directly from C. Correcting `D_800D2108` from inline
byte storage to a pointer-owned path-count table restores their missing load,
register allocation, wrapping, and directional state-update schedules without
guards. See
[Working Note 708](WORKING_NOTES/708-game-path-count-pointer-contract-match-20261002.md).

The Game randomized-step callback `func_1518F7C4` now matches all 37 retail
words. It accumulates a timestep-scaled randomized delta, performs the object
update, and optionally dispatches through the signed callback selector at
offset `0x88`. Twenty-two stale-guarded rows normalize IDO's frame, retained
record pointer, call delays, and callback branch layout. See
[Working Note 707](WORKING_NOTES/707-game-randomized-step-callback-match-20261002.md).

The Game position-sample ring recorder `func_1515CF9C` now matches all 37
retail words. It appends a 12-byte position and float sample while capacity
remains, advances and wraps the write cursor, or writes signed status `-1`
when full. Four expected-word guards normalize only the five-word reset/exit
schedule, including one inserted branch. See
[Working Note 706](WORKING_NOTES/706-game-position-sample-ring-recorder-match-20261002.md).

The Game geometry-mode command helper `func_15142B7C` now matches all 37
retail words directly from C. It emits clear/set geometry-mode commands only
for uncached bits and merges those bits into the two cached mode masks. Using
the original SDK graphics macros restores retail's cursor lifetime and store
schedule without guards or a compiler-profile override. See
[Working Note 705](WORKING_NOTES/705-game-geometry-mode-command-helper-match-20261002.md).

The Game global-position query `func_150FCF1C` now matches all 37 retail words
from recovered C. A null coordinate source returns `1.0f`; otherwise it
converts three signed halfwords to a float vector and forwards that vector,
two fixed full-width parameters, and `D_800A1F2C` to `func_15165BB0`. Four
expected-word guards normalize only IDO's persistent local-vector stack
offset. See
[Working Note 704](WORKING_NOTES/704-game-global-position-query-match-20261002.md).

The Game scaled indexed-global updater `func_1509DF20` now matches all 37
retail words directly from C. After its event-state and global-mode gates, it
scales the event value by `1/65536`, writes the result to two indexed float
tables, and marks the corresponding status byte. Retaining the repeated event
reads reproduces the complete leaf schedule without guards. See
[Working Note 703](WORKING_NOTES/703-game-scaled-indexed-global-updater-match-20261002.md).

The Game payload-record initializer `func_1518BCD0` now matches all 36 retail
words directly from C. It allocates a selector-scoped record, copies the
caller’s 0x1C-byte payload into offset `0x10`, and initializes two independent
five-bit random fields. The recovered byte-sized selector contract and direct
null-return path reproduce the complete allocation schedule without guards.
See
[Working Note 702](WORKING_NOTES/702-game-payload-record-initializer-match-20261002.md).

The Game color-driver callbacks `func_150D149C` and `func_150D1B40` now match
their complete 37- and 36-word slots directly from C. Each advances three
float fields through `func_151467A4` with its own fixed ranges and then
publishes the truncated first component with two retained global channels.
An explicit derived pointer and the retail full-width integer publisher
contract recover both layouts without guards. See
[Working Note 701](WORKING_NOTES/701-game-color-driver-callback-family-match-20261002.md).

The Game script-result flag callback `func_150C7350` now matches its complete
36-word slot directly from C. It applies the base `0x80004000` flags, invokes
the six-argument script query, and sets or clears bit `0x00400000` from the
result. The direct early-return form reproduces the branch-likely layout and
trailing padding word without guards. See
[Working Note 700](WORKING_NOTES/700-game-script-result-flag-callback-match-20261002.md).

The Game randomized event-descriptor builder `func_150FFC3C` now matches all
35 retail words directly from C. When the nested owner exists, it constructs
the seven-byte duration, variant, one-hot mask, and terminator record before
submitting it through `func_151D8868`. The semantic byte-array form reproduces
the complete branch and call schedule without guards. See
[Working Note 699](WORKING_NOTES/699-game-randomized-event-descriptor-match-20261002.md).

The Game vector-argument forwarding wrapper `func_150E3340` now matches all
35 retail words directly from C. It duplicates a three-word vector into the
first six callee arguments, supplies the fixed mode and scale, forwards a
three-float position, and preserves the final word and signed-halfword
arguments. The direct call expression recovers the complete retail schedule
without guards. See
[Working Note 698](WORKING_NOTES/698-game-vector-argument-forwarder-match-20261002.md).

The Game timer/position updater `func_150CBA30` now matches all 35 retail words
directly from C. It decrements the signed timer, applies its scaled motion to
two position fields while the timer remains positive, and conditionally lowers
the state byte from a shifted signed value. Testing the reloaded timer directly
preserves retail's separate register lifetimes without guards. See
[Working Note 697](WORKING_NOTES/697-game-timer-position-byte-clamp-match-20261002.md).

The Game resource-teardown finalizer `func_15080C64` now matches all 36 retail
words directly from C. It gates teardown on the active flag and record state,
invokes `func_15080BE8`, sets the non-`0x29`/non-`0x2E` global flag, and
completes and clears an optional pending record. Direct global indexing
recovers retail's temporary allocation without guards. See
[Working Note 696](WORKING_NOTES/696-game-resource-teardown-finalizer-match-20261002.md).

The Game attachment-state transition callback `func_15074664` now matches all
35 retail words directly from C. It detects state-one entry and exit, invokes
`func_10011FDC` with `5` or `0`, reloads the potentially changed attachment,
and writes the requested state byte. An unsigned state comparison and one
shared final assignment reduce the former 37-word overflow to retail's exact
slot without guards. See
[Working Note 695](WORKING_NOTES/695-game-attachment-state-transition-match-20261002.md).

The Game trigonometric lookup `func_150489B0` now matches all 36 retail words.
It restores the four quadrant ranges, reflected table indexes, and signs for
the byte-angle result. Thirty-one words emit directly from C; five guarded
indexing words preserve retail's shift-before-negate schedule. Its adjacent
quarter-turn wrapper remains exact through seven stale-checked schedule words
after correcting the callee's `f32`/`u8` contract. See
[Working Note 694](WORKING_NOTES/694-game-trigonometric-lookup-match-20261002.md).

The Game timer-expiry callback `func_1503EEC0` now matches all 35 retail
words. It runs the per-entry update, subtracts the global tick count from the
signed timer while retaining the full-width result for the expiry test, stores
the truncated halfword, and dispatches the indexed callback on expiry.
Sixteen words emit directly from C; nineteen stale-checked words preserve the
retail allocation and schedule, including both global-address relocation
pairs. See
[Working Note 693](WORKING_NOTES/693-game-timer-expiry-callback-match-20261002.md).

The Game attachment-state updater `func_150333A8` now matches its complete
38-word slot. It handles the global disable mode, clears an attached object's
state byte for active attachments, and otherwise derives byte `3` from the
reference-height equality and `+300.0f` threshold tests. Thirty-one words emit
directly from C; seven stale-checked words preserve an equivalent closed
floating-branch and delay-slot store layout. See
[Working Note 692](WORKING_NOTES/692-game-attachment-state-updater-match-20261002.md).

The Game group-record activator `func_150227BC` now matches all 35 retail
words. It walks the selected 30-byte ID row, resolves each active ID through
`func_151149AC`, and sets byte `0x6E` on the returned record while re-reading
the group count. Thirty-three words emit directly from C; two stale-checked
rows normalize only the independent row-offset and index-initialization
schedule around the opening branch. See
[Working Note 691](WORKING_NOTES/691-game-group-record-activator-match-20261002.md).

The Game counted resource-owner teardown `func_151EDB58` now matches all 33
retail words directly from semantic C. It releases the auxiliary resource and
owner allocation before walking the owner's count-sized pointer array. The
frame, saved-register lifetime, branch-likely delay slots, release order, and
loop schedule require no expected-word guards or compiler-profile override.
See
[Working Note 690](WORKING_NOTES/690-game-counted-resource-owner-teardown-match-20261002.md).

The Game event-record matcher `func_151D7538` now matches its complete 35-word
slot. Selector `0x3D` compares the object's embedded word and tag byte against
the incoming record and destroys the object when either matches; other
selectors forward both embedded-field addresses through `func_15149514`.
Fourteen stale-checked rows, including one checked insertion, preserve the
retail pointer lifetime and closed compiler register allocation without
changing either call relocation. See
[Working Note 689](WORKING_NOTES/689-game-event-record-matcher-match-20261002.md).

The Game mode-offset adjuster `func_151CD224` now matches its complete 39-word
slot. It samples the object's control value, derives a scaled adjustment from
the embedded record at offset `0x70`, and applies the positive or negative
mode-specific output at offset `0x14`. Six stale-checked rows, including one
checked insertion, preserve retail's shared record-base and mode-register
allocation; the remaining arithmetic and branch schedule emit from semantic
C. See
[Working Note 688](WORKING_NOTES/688-game-mode-offset-adjuster-match-20261002.md).

The Game output-default initializer `func_151B498C` now matches all 34 retail
words. It initializes thirteen caller-provided outputs with two packed mode
words, eight `0xFF` values, one zero, and two byte selectors before returning
success. The complete function emits directly from semantic C without guards
or a compiler-profile override. See
[Working Note 687](WORKING_NOTES/687-game-output-default-initializer-match-20261002.md).

The Game threshold/intensity updater `func_151A787C` now matches all 35 retail
words. It applies two signed threshold tests, advances two halfword fields by
an elapsed-tick-scaled step, and writes timer-scaled byte outputs. Nineteen
words emit directly from semantic C; sixteen stale-checked words normalize one
commutative multiply and a closed compiler register/scheduling cycle. See
[Working Note 686](WORKING_NOTES/686-game-threshold-intensity-updater-match-20261002.md).

The Game tick-compensated damping callback `func_1519C4E4` now matches all 34
retail words. It repeats two floating-point damping updates for every elapsed
tick, then conditionally lowers the byte at offset `0x5C` from the timer and
parameter scale. The complete function emits directly from semantic C without
guards or a compiler-profile override. See
[Working Note 685](WORKING_NOTES/685-game-tick-compensated-damping-callback-match-20261002.md).

The Game clamped height-byte updater `func_1518B1D8` now matches all 35 retail
words. It derives a nonnegative byte from the smaller of a scaled object field
and half the truncated height delta, clamps each upper bound to `0xFF`, and
stores the result at offset `0x70`. Twenty-five words emit directly from
semantic C; ten stale-checked suffix words preserve retail's compiler phi
register and equivalent branch schedule. See
[Working Note 684](WORKING_NOTES/684-game-clamped-height-byte-match-20261002.md).

The Game active-row wrapper `func_1517F4D8` now matches all 35 retail words.
It returns the incoming handle for inactive timer or mode rows and otherwise
forwards the indexed three-byte parameter row to `func_1517F08C`. The complete
routine emits directly from semantic C without guards or profile overrides.
See [Working Note 683](WORKING_NOTES/683-game-active-row-wrapper-match-20261002.md).

The Game mode dispatcher `func_15170EC4` now matches all 34 retail words after
restoring its mode-2 and mode-`0x10` parameter sets and low-byte argument
forwarding. Its sparse switch, calls, and shared epilogue emit directly from
semantic C without guards or profile overrides. See
[Working Note 682](WORKING_NOTES/682-game-mode-dispatcher-match-20261002.md).

The Game packed two-axis integrator `func_1516F864` now matches all 34 retail
words after restoring its signed high-byte and unsigned low-byte velocity
loads, global time-scale multiplication, and packed position accumulation.
Thirty-two stale-checked words preserve only compiler register allocation;
the arithmetic and instruction schedule already match. See
[Working Note 681](WORKING_NOTES/681-game-packed-two-axis-integrator-match-20261002.md).

The Game resource-release loops `func_1514795C`, `func_151571C4`, and
`func_15158A20` now match all 33 retail words apiece after restoring their
inclusive indexed scans, conditional frees, and trailing-slot releases. The
Game height/state predicate `func_15159084` also matches all 39 words; one
stale-checked word preserves retail's commutative floating-equality operand
order. See
[Working Note 680](WORKING_NOTES/680-game-resource-release-family-and-height-predicate-match-20261002.md).

The Game resource-release loop `func_151325C8` now matches all 33 retail
words after restoring its inclusive indexed scan, conditional frees, and
trailing-slot release. The Game vertex rotation helper `func_151436B4` also
matches all 34 words after making the fourth trigonometric result explicit so
IDO retains retail's call-before-store schedule. Both emit directly from
semantic C without expected-word guards or profile overrides. See
[Working Note 679](WORKING_NOTES/679-game-resource-release-and-vertex-rotation-match-20261002.md).

The Game angular integrators `func_1511515C` and `func_151151FC` now match all
40 retail words directly from semantic C. The related displacement extender
`func_15115EDC` matches all 35 words after restoring its position snapshot,
motion update, and record-type-`0x4B` extrapolation. One stale-checked word
preserves the retail cross-declaration record-pointer register. See
[Working Note 678](WORKING_NOTES/678-game-angular-motion-update-family-match-20261002.md).

The Game render-parameter wrappers `func_1510E7A4`, `func_1510E82C`, and
`func_1510E8BC` now match all 34, 36, and 37 retail words. Their recovered
word-accurate signatures preserve raw coordinate payloads, mixed stack load
widths, default bounds, and the final mode argument while adapting calls to
`func_1510E950`. All three emit directly from semantic C without expected-word
guards or compiler-profile overrides. See
[Working Note 677](WORKING_NOTES/677-game-render-parameter-wrapper-family-match-20261002.md).

The Game owner-event callback `func_15100230` now matches all 35 retail words.
It destroys the object when event `0x48` matches either owner identity field
and otherwise forwards the event with the embedded owner record. A
function-specific `-O1 -g3` object preserves its caller-spilled callback ABI;
28 stale-checked words normalize the closed instruction schedule and both call
relocations. See
[Working Note 676](WORKING_NOTES/676-game-owner-event-callback-match-20261002.md).

The Game state-flag updater `func_150F9A20` now matches its complete 36-word
slot directly from C. It queries condition `0x4025`, selects mutually exclusive
`0x80` and `0x08` state flags, and writes either `85.0f` or zero to field
`0x190`. No expected-word guards are required. See
[Working Note 675](WORKING_NOTES/675-game-condition-state-flag-match-20261002.md).

The Game command-row loop `func_150413FC` now matches all 33 retail words. It
walks a zero-terminated command-byte stream, advances its associated row by
eight bytes per command, translates each command through `func_15041480`, and
threads the result through `func_15041508`. The complete loop body and frame
emit from semantic C; nine stale-checked words normalize only the independent
prologue schedule. See
[Working Note 674](WORKING_NOTES/674-game-command-row-loop-match-20261002.md).

The Game object teardown `func_15106E78` now matches all 32 retail words
directly from C. It restores the type-indexed destructor callback, releases
the two optional child objects, and tears down the embedded record. The two
adjacent teardown-and-finalize wrappers now carry the recovered pointer ABI;
all three routines remain byte-exact without guarded words. See
[Working Note 673](WORKING_NOTES/673-game-object-teardown-match-20261002.md).

The Init sound-event dispatcher `_n_handleEvent` now matches all 1,363 retail
words, completing the Init code-function matcher queue at 487 / 487. It
restores resource resolution, voice allocation and startup, envelope timing,
pan/volume/pitch/effect updates, retry scheduling, cleanup, channel-volume
events, and child-sound dispatch. Its typed 1,241-word body is expanded by 122
checked insertions; 87 rows verify compact-object relocations. The independent
5,452-byte comparison is exact with SHA-256
`583662222304bf87a3b24bc9495055b930b2076e36ecb37183fa5612a36b8525`.
The separate shifted Init-rodata issue at absolute dispatcher table
`jtbl_8002C708_init` remains a data-layout/runtime qualification task. See
[Working Note 672](WORKING_NOTES/672-init-sound-event-dispatcher-match-20261002.md).

The Init compact-sequence voice handler `__n_CSPVoiceHandler` now matches all
684 retail words. It restores SDK event dispatch, envelope and oscillator
updates, MIDI/meta forwarding, Rare's mix and control events, restartable
play/stop behavior, voice cleanup, and channel-mask transitions. Its semantic
body compiles to 667 words; 667 stale-checked rows preserve retail's closed
layout, including 17 insertions and 45 relocation-aware rows. See
[Working Note 671](WORKING_NOTES/671-init-compact-sequence-voice-handler-match-20261001.md).

The Init path-relative spatial query `func_1000A750` now matches all 580
retail words. It restores nearest-node selection, adjacent-segment choice,
point-to-segment projection, endpoint clamping, and the final handoff to the
already matched attenuation/pan calculator. Its readable 404-word compiler
body is expanded to retail's unrolled layout by 401 stale-checked rows,
including 176 insertions and 19 relocation-aware rows. See
[Working Note 670](WORKING_NOTES/670-init-path-projection-query-match-20261001.md).

The Init 64DD interrupt handler `__osLeoInterrupt` now matches its complete
441-word retail slot. It restores the disk-presence gate, DMA-busy recovery,
mechanical and buffer-manager interrupt handling, read/write sector transfer,
C1/C2 error bookkeeping, track transitions, and completion notification. The
compiler emits 440 words; 323 match directly, 117 stale-checked rows normalize
the closed allocation and relocation layout, and the layout tool supplies the
retail trailing `nop`. See
[Working Note 669](WORKING_NOTES/669-init-64dd-interrupt-handler-match-20261001.md).

The Init conversion helper `func_10002718` now matches its complete 422-word
retail span. It restores character, signed/unsigned integer, floating-point,
pointer, string, `%n`, percent, and fallback conversions using the shared SDK
formatter descriptor. The 338-word compact body emits 42 retail words
directly; 296 stale-checked rows include 87 insertions, three omissions, and
four relocation-aware rows. See
[Working Note 668](WORKING_NOTES/668-init-conversion-helper-match-20261001.md).

The Init formatted-output dispatcher `func_100020D0` now matches its complete
402-word retail span. It restores literal-run output, format-flag parsing,
width and precision arguments, length modifiers, conversion dispatch, and
chunked field padding through the caller's output callback. The 361-word
compact body emits 95 retail words directly; 266 stale-checked rows include
44 insertions, three omissions, and ten relocation-aware rows. See
[Working Note 667](WORKING_NOTES/667-init-formatted-output-dispatcher-match-20261001.md).

The Init numeric formatter `func_10001AA8` now matches its complete 370-word
retail span. It restores fixed, scientific, and general-format placement,
precision trimming, decimal insertion, exponent emission, and width padding.
The 365-word compact body emits 87 retail words directly; 278 stale-checked
rows include 13 insertions, eight omissions, and three relocation-aware rows.
See
[Working Note 666](WORKING_NOTES/666-init-numeric-formatter-match-20261001.md).

The Init sound-record updater `func_10011624` now matches its complete
357-word retail span. It restores bounded record traversal, stale-handle
release, listener-relative volume and pan, callback dispatch, voice creation,
incremental parameter updates, and distance-driven pitch smoothing. The
semantic compact body emits 64 retail words directly; 293 stale-checked rows
include one insertion and 20 relocation-aware rows. See
[Working Note 665](WORKING_NOTES/665-init-sound-record-updater-match-20261001.md).

The Init instrument channel loader `func_1001B7D0` now matches its complete
345-word retail span directly from C. It restores resource resolution and
release, per-sound relocation, envelope and instrument-default transfer,
missing-resource state, and selected-program tracking. Its exact retail size,
stack slots, repeated channel indexing, and all relocations emit without
guards. See
[Working Note 664](WORKING_NOTES/664-init-instrument-channel-loader-match-20261001.md).

The Init audio-environment controller `func_10012020` now matches its complete
336-word retail span. It restores five environment modes, transition-state
ramps, oscillator-driven pitch targets, master gain, and two-channel parameter
updates. The generated switch table is retargeted to retail rodata; 225
stale-checked rows include one padding insertion and 103 relocation-aware
rows. See
[Working Note 663](WORKING_NOTES/663-init-audio-environment-controller-match-20261001.md).

The Init sequence transition dispatcher `func_1000D96C` now matches its
complete 300-word retail span. It restores existing-record teardown, child
allocation and attachment, mode-specific fades, shared-channel handling, and
record reinitialization. The semantic compact body emits 73 words directly;
220 stale-checked rows include seven schedule insertions and 20
relocation-aware rows. See
[Working Note 662](WORKING_NOTES/662-init-sequence-transition-dispatcher-match-20261001.md).

The Init SDK floating-point formatter `func_10001550` now matches its complete
296-word retail span. It restores `%f`, `%e`, `%E`, `%g`, and `%G` conversion,
including special values, decimal scaling, digit generation, and rounding.
The semantic C preserves retail's exact extent and control flow; 176
stale-checked rows, including 10 relocation-aware rows, normalize the closed
IDO allocation and frame-layout difference. See
[Working Note 661](WORKING_NOTES/661-init-sdk-float-formatter-match-20261001.md).

The Init audio channel updater `func_1000D2F8` now matches its complete
280-word retail span. It restores pending-sequence changes, child-channel
promotion and teardown, callback dispatch, volume ramps, and linked-channel
validation. The semantic C has retail's exact extent and control-flow order;
113 stale-checked words normalize IDO allocation and scheduling. The corrected
channel-index ABI also keeps its 133-word caller `func_1000D758` byte-exact
with two scoped guards. See
[Working Note 660](WORKING_NOTES/660-init-audio-channel-updater-match-20261001.md).

The Init audio subframe builder `func_1001FB40` now matches its complete
296-word retail span directly from C. It restores optional opening-command
interception, per-bus filter dispatch, mixer selection, effect-state refresh,
and the ADPCM and pole-filter command stream. Recovered SDK audio macros and
the original dual loop-increment form emit every retail word and relocation
without guards. See
[Working Note 659](WORKING_NOTES/659-init-audio-subframe-builder-match-20261001.md).

The Init channel event and timer updater `func_1000CEAC` now matches its
complete 275-word retail span. It drains the selected channel queue, expands
event masks into sixteen timer slots, applies the four event modes, updates
the active voice state, and decrements paired timers with the current frame
step. The semantic C has the exact retail extent; 230 stale-checked rows,
including 41 relocation-aware rows, normalize IDO's closed allocation and
layout differences. See
[Working Note 658](WORKING_NOTES/658-init-channel-event-timer-update-match-20261001.md).

The Init audio-runtime bootstrap `func_10008F90` now matches its complete
271-word retail span. It installs audio callbacks, derives frame sample counts,
initializes the synthesis parameter areas and record pools, allocates command
buffers, creates four queues, and starts the audio thread. A scoped
macro-enabled function object preserves the already matched neighboring
routines; 139 checked rows include eight insertions and 45 relocation-aware
rows. See
[Working Note 657](WORKING_NOTES/657-init-audio-runtime-bootstrap-match-20261001.md).

The Init bidirectional heap allocator `func_10003C6C` now matches its complete
258-word retail span. It applies allocation-class alignment, searches from
either end of the free list, splits or consumes the selected block, repairs
both physical and free-list links, and refreshes the largest-free-block record.
The semantic C has the exact retail extent; 216 stale-checked rows, including
42 relocation-aware rows, normalize IDO's closed allocation and scheduling
differences. See
[Working Note 656](WORKING_NOTES/656-init-bidirectional-heap-allocator-match-20261001.md).

The Init packed spatial-audio state updater `func_1000BF60` now matches its
complete 252-word retail span. It starts sound `0x22`, performs three spatial
queries, updates the changed volume and position channels, handles two mode
transitions, and returns the refreshed packed state. The semantic C emits 250
words with retail's `0x60` frame; 111 stale-checked rows, including two checked
insertions and two relocation-aware rows, normalize IDO's allocation and
scheduling. See
[Working Note 655](WORKING_NOTES/655-init-packed-spatial-audio-state-match-20261001.md).

The Init scheduler and render thread `func_100049E0` now matches its complete
244-word retail span. It restores the seven-class message loop, registered
client notifications, delayed task timer, SP yield/completion paths, pending
graphics-task dispatch, idle render advance, and guarded controller reads.
The semantic C emits 239 words; 150 stale-checked rows, including five checked
insertions and 44 relocation-aware rows, normalize IDO's frame, allocation,
switch, and unreachable epilogue schedule. See
[Working Note 654](WORKING_NOTES/654-init-scheduler-render-thread-match-20261001.md).

The Init audio-library bootstrap `func_10008180` now matches its complete
214-word retail span. It initializes the audio heap and synthesizer, loads and
relocates the bank and sequence metadata, normalizes all 150 sequence lengths,
creates three sequence players, and configures the sound player. The semantic
C emits 213 words; 64 stale-checked rows, including one checked insertion and
10 relocation-aware moves, normalize IDO's frame, local, loop, and player
setup allocation. See
[Working Note 653](WORKING_NOTES/653-init-audio-library-bootstrap-match-20261001.md).

The Init `bcopy` slot is restored to its original handwritten assembly instead
of the non-matching simplified C substitute. Direct comparison confirms all
196 words, including the optimized overlap-safe forward and backward copy
paths and three padding words, match retail. Because the authoritative matcher
tracks C rows only, this moves one function and 784 bytes from the C totals to
raw assembly without changing the byte-exact C numerator. See
[Working Note 652](WORKING_NOTES/652-init-handwritten-bcopy-restoration-20261001.md).

The Init resource-request manager `func_10009CBC` now matches its complete
208-word retail span. It resolves encoded resource requests, acquires or
evicts manager nodes, allocates and clears rounded buffers, performs cache
maintenance, submits PI DMA, and handles existing resource references. See
[Working Note 651](WORKING_NOTES/651-init-resource-request-manager-match-20261001.md).

The Init spatial attenuation and pan calculator `func_1000A420` now matches its
complete 204-word retail span. It selects planar or three-axis distance,
computes clamped attenuation, derives listener-relative pan when requested,
and writes the optional raw-distance result. See
[Working Note 650](WORKING_NOTES/650-init-spatial-attenuation-pan-match-20261001.md).

The Init resource-completion manager `func_1000A03C` now matches its complete
195-word retail span. It drains completed resource messages, moves matching
nodes between manager lists, relocates resource tables, releases idle entries,
and services the deferred cleanup flag. See
[Working Note 649](WORKING_NOTES/649-init-resource-completion-manager-match-20261001.md).

The Init audio-event parameter updater `func_1000F85C` now matches its complete
48-word retail span. It validates the sound handle, converts pitch cents to
the event's floating-point bit representation, normalizes selector `0x11`,
and dispatches to the active sound state. See
[Working Note 648](WORKING_NOTES/648-init-audio-event-parameter-update-match-20261001.md).

The Init handle-record lookup `func_1000FEF0` now matches its complete 40-word
retail span. Its no-unroll profile is selected per function so neighboring
matches retain their established object profile. See
[Working Note 647](WORKING_NOTES/647-init-handle-record-lookup-match-20261001.md).

The Init active-record lookup `func_1000FF90` now matches its complete 35-word
retail span. It scans the active 0x30-byte record array with two independently
optional selectors and rejects disabled records. See
[Working Note 646](WORKING_NOTES/646-init-active-record-lookup-match-20261001.md).

The Init listener/audio update `func_10011BB8` now matches its complete
180-word retail span. It restores listener snapshots, active audio-record
compaction, and the two-channel transition update. See
[Working Note 645](WORKING_NOTES/645-init-listener-audio-update-match-20261001.md).

The Init PRENMI shutdown thread `func_100052A0` now matches its complete
180-word retail span. It restores thread shutdown, controller-motor cleanup,
the two timed waits, cache writeback, and the terminal park loop. See
[Working Note 644](WORKING_NOTES/644-init-prenmi-shutdown-thread-match-20261001.md).

The Init packed audio-state updater `func_1000C530` now matches its complete
174-word retail span. It restores queued state transitions, sound-slot
parameter updates, transition expiry, and the high-byte fade trigger. See
[Working Note 643](WORKING_NOTES/643-init-packed-audio-state-updater-match-20261001.md).

The Init integer formatter `_Litob` now matches its complete 168-word retail
span. It restores signed magnitude handling, octal/decimal/hex digit emission,
precision zero-fill, and field-width padding. See
[Working Note 642](WORKING_NOTES/642-init-integer-formatter-match-20261001.md).

The Init common system initializer `__osInitialize_common` now matches its
complete 168-word retail span. It restores CPU/FPU setup, PIF initialization,
the four exception vectors, cache and RDB setup, clock-rate adjustment, the
cold-reset NMI clear, and the 64DD Leo interrupt probe. See
[Working Note 641](WORKING_NOTES/641-init-common-system-initializer-match-20261001.md).

The Init sound-slot dispatcher `func_10010BE8` now matches its complete
164-word retail span. It validates and reuses caller handles, scans the
16-entry sound table for an available unreserved slot, advances the slot
generation, applies the global effect mix, converts pitch cents, and starts
the selected bank sound. See
[Working Note 640](WORKING_NOTES/640-init-sound-slot-dispatcher-match-20261001.md).

The Init boot loader `func_10001194` now matches its complete 163-word retail
span. It restores memory clearing, framebuffer setup, compressed Game-image
loading, relocation-table decoding, and final subsystem startup. See
[Working Note 639](WORKING_NOTES/639-init-boot-loader-thread-match-20261001.md).

The Init music-control callback `func_1000BCBC` now matches its complete
169-word retail span. It restores initial channel setup plus the scene-gated
distance and event-level updates; 70 stale-checked rows normalize IDO's two
float-to-unsigned conversion schedules. See
[Working Note 638](WORKING_NOTES/638-init-music-control-callback-match-20261001.md).

The Init PI device-manager thread `func_10002E50` now matches its complete
148-word retail span directly from semantic C. The recovery includes the
custom direct-PI ownership handshake, the canonical libultra DMA/EDMA and
loopback dispatch order, and the retail jump table. See
[Working Note 637](WORKING_NOTES/637-init-pi-device-manager-loop-match-20261001.md).

The full debugger inventory is complete: all 181 C-classified tracked rows are
linked byte-exact, and the sole remaining assembly row, the original
handwritten 40-word CP0/TLB routine `func_16003650`, independently matches all
40 retail words. It remains assembly by design because IDO C cannot emit its
`mtc0`, `tlbr`, and `mfc0` instruction sequence. Thus all 182 debugger rows
are accounted for and exact; 181 / 181 is only the C-matcher denominator.

The percentage increase from the old July matching snapshot remains primarily
denominator driven: the exact count is now 3,040, while
508 functions moved from C back to assembly. The paired event-swap pass added
two byte-exact functions and the debugger rectangle-fill, float-formatter,
glyph-blitter, `_Printf`, context-display, memory-view, and debugger-main-loop
passes added one each after the restoration baseline. The subsequent game
pass completed `func_15135480`, the final four one-difference game rows, and
the subsequent small game queue through `func_1509D054`; `func_150A7A00` was
then correctly restored from a false C placeholder to its original trampoline,
followed by handwritten PRNG seed setter `func_150ADACC`, the guarded
scalar-temporary match for `func_150BDB3C`, the guarded set-bit temporary
match for `func_150F33B0`, and the relocation-preserving opening-load match
for `func_151254F4`; `func_1515FB70` was then restored from a false C model
to its original nine-word assembly extent, followed by the guarded register
normalization for `func_1505841C`, indexed-slot clear `func_150F02A0`, and
call-ABI correction for `func_151B2FA0`, and byte-offset expression recovery
for `func_150770E4`.
Handwritten byte-fill loop `func_150A7770` is restored from its false C model
to the original eight-word assembly extent. Packed fixed-point reader
`func_1515F008` is byte-exact through guarded pointer/value register
normalization. Packed-byte scalers `func_1516F8EC` and `func_1516F91C` are
byte-exact through symmetric guarded temporary-register normalization, while
`func_1516F984` matches from a source-level scaled-field lifetime.
Viewport setup `func_15019BB8` is byte-exact through guarded frame-size and
relocation-preserving address-register normalization.
Sound-command wrapper `func_1509F6B0` is byte-exact through guarded incoming
argument spill/reload scheduling.
`func_150C7930` is restored to its original 14-word assembly ownership because
IDO eliminates retail's dead `temp_v0 + 0x1E0` expression.
`func_150CDB6C` is byte-exact through guarded destination-pointer
materialization and schedule normalization.
`func_15108B80` is byte-exact through guarded terminal/countdown register
lifetimes and commutative pointer-add operand order.
`func_1513A594` is byte-exact after correcting its forwarded byte ABI,
retaining the post-call field read, and guarding the empty branch shape.
`func_1515F0AC` is byte-exact from its signed float clamp C body plus three
guarded scheduling entries that move the independent lower-clamp `lui` into
the first FP comparison slot and omit IDO's resulting hazard `nop`.
`func_1516706C` is byte-exact after recovering its post-tested callback-table
loop, distinct `D_8008CB70` end symbol, and two guarded low-half address words.
`func_15168A9C` is byte-exact directly from typed link removal plus explicit
row/index byte lifetimes; no guarded retail words are needed.
`func_15179AB8` is byte-exact directly from a backward active-object scan that
sets flag `0x2` on the first eligible object.
`func_15194AB4` is byte-exact directly from C after correcting its return type
to `void` and expressing the two state mappings as a `switch` with a default
selector assignment after the object-flag store.
`func_151957B0` is byte-exact directly from a nonempty-first doubly linked-list
tail insertion that preserves retail's repeated old-tail load. Its former
trailing return pair is now correctly tracked as independent no-op
`func_15195824`, which is also byte-exact directly from an empty `void` body.
`func_151A8A20` is byte-exact directly from a typed callback-table dispatcher
that clamps selector bytes above the three-entry table to slot zero.
`func_151A8F1C` is byte-exact directly from a five-argument coordinate-transform
wrapper followed by a single float-component copy.
`func_151AA17C` is byte-exact from its recovered two-call stack-record dispatch
and final object callback, plus ten guarded scheduling and local-slot words;
all call relocations and delay slots already matched directly.
Structural twin `func_151AA210` is independently byte-exact from the same C
shape and ten separately guarded words across its own retail span.
`func_151CF844` is byte-exact directly from a null-gated five-argument record
forwarder; its branch-likely return path and call delay slot need no guards.
`func_151423D8` is byte-exact through symmetric guarded quadrant and table-index
register normalization.
`func_15155EF8` is byte-exact through guarded outer/child pointer register
lifetimes while preserving all three call relocations.
Adjacent `func_151D7770` and `func_151D779C` are byte-exact from source-level
child/destination pointer ordering and retail's wider byte-mask spelling.
`func_1509F248` is byte-exact from an explicit unsigned-halfword narrowing
that restores retail's high-half extraction and call-delay-slot schedule.
`func_150C5EFC` is restored to its original 17-word assembly extent because
IDO removes retail's otherwise dead child-pointer update before the call.
Its structural twin `func_150C682C` is restored for the same ownership reason,
with its distinct child-field clear preserved.
`func_150EA904` is byte-exact through eight guarded, relocation-preserving
base/index and byte-update register lifetime words.
`func_1515D480` is byte-exact through eight guarded frame-size and local-slot
words while preserving both call relocations.
`func_151AB180`, the `+0x70` member of the dead child-pointer family, is
restored to its original 17-word assembly extent.
`func_151EF610` is restored to its original 12-word assembly extent because
IDO retains one global address register, while retail uses independent load
and store relocations and places the store in the return delay slot.
`func_150771F0` is byte-exact through nine guarded argument-load and selector
schedule words, including eight explicitly declared relocation moves.
`func_15080200` is byte-exact from a source-level chained assignment that
restores retail's two retained global-address registers and three-store order.
`func_1510E634` is byte-exact from the typed `Gfx` writer idiom plus a guarded
two-word expansion that restores the original and advanced cursor lifetimes.
`func_1512D6B0` is byte-exact through nine guarded record-index, global-base,
and 176-byte stride temporary-register words.
`func_15166FD8` is byte-exact through the same guarded display-list cursor
expansion pattern, independently verified across its 14-word slot.
`func_15196330` is byte-exact through nine guarded pointer/selector register
words; its frame, control flow, callbacks, and relocations were already exact.
Structural twin `func_151963B4` is independently byte-exact through the same
nine guarded register words and its distinct final-call relocation.
Adjacent state-clear callbacks `func_1519F108` and `func_1519F168` are
independently byte-exact across 24 words each. Their recovered C is shared
apart from the final callback; symmetric guarded scheduling restores retail's
derived field-base lifetime and branch targets.
`func_151A09B4` is byte-exact directly from C after recovering its byte-flag
gate, child pointer or selector-byte match, and two-call teardown path.
`func_151B4E4C` is byte-exact directly from the established three-float vector
wrapper idiom, forwarding three more floats and two actor record bytes.
`func_151EFF94` is byte-exact directly from its two-fixed-argument variadic
formatting wrapper, including successful-output null termination.
`func_15044CE4` is byte-exact from its position/scale initializer plus seven
guarded register-lifetime words.
`func_151B3040` is byte-exact directly from C after recovering its two calls
over adjacent embedded records. An explicit `arg0 + 0x150` base and a volatile
byte argument reproduce retail's stack lifetime and second-call address reuse;
no guarded retail words are needed.
`func_151C9ED4` is byte-exact after recovering its event-`0x21` broadcast to
four handlers and final `D_8008CD00` clear. Four guarded frame and local-slot
words preserve retail's 40-byte allocation while the call schedule, saved
register lifetime, relocations, and behavior come directly from C.
`func_151D13E0` is byte-exact directly from C after recovering its null-gated
owned-object teardown, three separate flag updates, linked-record clear, and
owner-slot release. Retail's repeated slot loads and complete leaf schedule
need no guarded words.
`func_151E4E00` is byte-exact directly from C after recovering its state reset,
mode-3 transition, and five-argument dispatch for event `0x1D`. Its first
global clear naturally occupies the preceding call's delay slot; no guarded
words are needed.
`func_10012588` is byte-exact after the clean full regeneration removed its
stale address-drift classification. No address-drift rows remain.
`func_15155780` is byte-exact after recovering its six-argument record
allocation, null return, four field initializers, and notification call. Eight
guarded words normalize only the independent success-path schedule; see
[Working Note 485](WORKING_NOTES/485-game-record-allocator-initializer-match-20260929.md).
`func_151557FC` is byte-exact directly from C after recovering its find-or-create
path, float update, and actor-table-dependent state/timer initialization; see
[Working Note 486](WORKING_NOTES/486-game-record-find-or-create-update-match-20260929.md).
`func_1515FF74` is byte-exact directly from C after recovering its allocation
arguments, explicit null return, and eight-byte payload copy; see
[Working Note 487](WORKING_NOTES/487-game-small-record-copy-allocator-match-20260929.md).
`func_150C7D7C` is byte-exact directly from C after recovering its source
position query and three offset, truncated halfword outputs. Its 32
instructions and one trailing retail padding word match without guards; see
[Working Note 488](WORKING_NOTES/488-game-offset-position-halfword-writer-match-20260929.md).
`guMtxIdentF` is byte-exact after recovering its unrolled mixed float/integer
identity-matrix stores and O3 profile. Five guarded words normalize only the
compiler's equivalent diagonal-constant FP register; see
[Working Note 489](WORKING_NOTES/489-game-identity-matrix-initializer-match-20260929.md).
Adjacent impact-effect dispatchers `func_15194320` and `func_15194394` are
byte-exact directly from grouped switches over source states zero through
four. Their separate five-entry jump tables retain retail rodata ownership;
see
[Working Note 490](WORKING_NOTES/490-game-impact-effect-dispatch-pair-match-20260929.md).
Init arena-anchor initializer `func_10003BD0` is byte-exact across all 28
words after recovering its repeated global-head access shape. Twenty
stale-checked guards preserve one closed compiler schedule, including the
single inserted low-half word for retail's retained final-anchor pointer; see
[Working Note 491](WORKING_NOTES/491-init-arena-anchor-initializer-match-20260929.md).
Handwritten libultra cache routines `osInvalICache` and `osWritebackDCache`
are restored from empty C placeholders to their original 32-word assembly
bodies. Both complete 128-byte spans match retail; see
[Working Note 492](WORKING_NOTES/492-init-handwritten-cache-routine-restoration-20260929.md).
Init record-key updater `func_100100E0` is byte-exact across all 29 words
after recovering its nonempty pointer-range scan. Twenty stale-checked guards
normalize only one closed `$v0`/`$v1` allocation cycle; see
[Working Note 493](WORKING_NOTES/493-init-record-key-updater-match-20260929.md).
Game water-buoyancy response `func_15058F24` is byte-exact across all 135
words after preserving the original blend factor for the initial velocity
scale. Thirty stale-checked guards normalize only IDO scheduling and temporary
register allocation; see
[Working Note 494](WORKING_NOTES/494-game-water-buoyancy-response-match-20260929.md).
Init sound-handle lookup `func_1000F4D8` is byte-exact across all 36 words
directly from C after recovering its one-time in-place identifier mask; see
[Working Note 495](WORKING_NOTES/495-init-sound-handle-lookup-match-20260929.md).
Game audio DMA reader `func_151F3C4C` is byte-exact across all 75 words after
reusing its callback-state local for the DMA result. Eleven stale-checked
guards normalize two closed compiler register-allocation cycles; see
[Working Note 496](WORKING_NOTES/496-game-audio-dma-reader-match-20260929.md).
Game byte-state reset `func_15010600` is byte-exact across all 32 words after
recovering six scalar clears and a paired 12-byte array loop. Four
relocation-aware stale checks normalize only one independent scheduling
window; see
[Working Note 497](WORKING_NOTES/497-game-byte-state-reset-match-20260929.md).
Game height-gated action selector `func_1506DC10` is byte-exact across all 37
words after removing a false callback parameter. One stale-checked guard
preserves retail's commutative floating-equality operand order; see
[Working Note 498](WORKING_NOTES/498-game-height-gated-action-selector-match-20260929.md).
Game path-node spawn randomizer `func_15079790` is byte-exact across all 60
words after restoring separate actor/path-table lookups for its X and Z
updates. The complete routine emits directly from C with no guards; see
[Working Note 499](WORKING_NOTES/499-game-path-node-spawn-randomizer-match-20260929.md).
Game opcode-record byte counter `func_150027F8` is byte-exact across all 32
words after restoring its integer-address ABI and repeated eight-byte indexed
loads. Fourteen stale-checked guards normalize only the closed `v0`/`a1`
record-index/opcode allocation cycle; see
[Working Note 500](WORKING_NOTES/500-game-opcode-record-byte-counter-match-20260929.md).
Game six-word actor query `func_151420F8` is byte-exact across all 34 words
after recovering its aggregate template copy, signed actor-index division, and
explicit success branch. The complete function emits directly from C with no
guards; see
[Working Note 501](WORKING_NOTES/501-game-six-word-actor-query-match-20260929.md).
Game actor-slot selector `func_1503F964` is byte-exact across all 35 words
after replacing its false zero-return placeholder with the wrapped 25-slot
actor scan. Fourteen relocation-aware stale checks normalize only the closed
`a0`/`v1` index/table-base allocation cycle; see
[Working Note 502](WORKING_NOTES/502-game-actor-slot-selector-match-20260929.md).
Game group-value appender `func_15022640` is byte-exact across all 31 words
after recovering its duplicate scan, 30-byte row indexing, and count update.
The corrected integer value ABI and separate signed loop-bound lifetime emit
the complete routine directly from C with no guards; see
[Working Note 503](WORKING_NOTES/503-game-group-value-deduplicating-append-match-20260929.md).
Game display-list address relocator `func_15168F08` is byte-exact across all
31 words after recovering signed opcode parsing, index-based cursor updates,
and retail's two-step mask/add stores. Eighteen stale checks normalize only one
closed constant/cursor allocation chain; see
[Working Note 504](WORKING_NOTES/504-game-display-list-address-relocator-match-20260929.md).
Game cached resource setup `func_1517A9A8` is byte-exact across all 30 words
after recovering its selector cache gate, 20-byte output record, shifted
resource index, and nine-argument setup call. Six stale checks normalize only
one independent call-argument scheduling window; see
[Working Note 505](WORKING_NOTES/505-game-cached-resource-setup-match-20260929.md).
Game byte-selected coefficient clamp `func_15182F58` is byte-exact across all
33 words after recovering its 24-byte coefficient row, integer-times-40
scale, and mutually exclusive lower/upper clamp. The complete routine emits
directly from C with no guards; see
[Working Note 506](WORKING_NOTES/506-game-byte-selected-coefficient-clamp-match-20260929.md).
Game reference-counted resource release `func_1518CA04` is byte-exact across
its complete 31-word tracked slot after recovering its reserved-index gate,
short-circuit byte decrement, and two cleanup calls. It emits directly from C
with no guards; see
[Working Note 507](WORKING_NOTES/507-game-reference-counted-resource-release-match-20260929.md).
Game five-state impact dispatcher `func_15194794` is byte-exact across all 31
words after recovering its two unconditional setup calls and grouped state
switch. Two relocation-aware stale checks retarget only the generated jump
table reference to the retained retail table; see
[Working Note 508](WORKING_NOTES/508-game-five-state-impact-dispatch-match-20260929.md).
Game subsystem-state initializer `func_151DDBA0` is byte-exact across all 32
words after recovering its setup call, global mode clears, three subsystem
calls, and paired ready flags. The complete routine emits directly from C
with no guards; see
[Working Note 509](WORKING_NOTES/509-game-subsystem-state-initializer-match-20260929.md).
Game timed HUD fade helper `func_151EC178` is byte-exact across all 30 words
after recovering its saturated alpha ramp, white modulation call, fixed text
resource draw, and unchanged display-list return. Nineteen stale checks
normalize one collapsed compiler merge and the displaced call tail; see
[Working Note 510](WORKING_NOTES/510-game-timed-hud-fade-helper-match-20260929.md).
Game resource teardown `func_15080BE8` is byte-exact across all 31 words after
recovering its primary release, conditional three-allocation cleanup, owner
slot clear, and tagged final teardown. Four stale checks normalize only the
optional-allocation load/test register; see
[Working Note 511](WORKING_NOTES/511-game-resource-teardown-match-20260929.md).
Game two-angle trigonometric updater `func_150A0D14` is byte-exact across all
30 words after recovering its two scaled input angles and paired cosine/sine
outputs. The complete routine emits directly from typed C with no guards; see
[Working Note 512](WORKING_NOTES/512-game-two-angle-trigonometric-updater-match-20260929.md).
Game resource slot-array teardown `func_150B6D78` is byte-exact across all 33
words after recovering its standalone release, ten-slot allocation scan,
owner clears, and final state transition. Two relocation-aware guards
normalize only independent address-finalization words; see
[Working Note 513](WORKING_NOTES/513-game-resource-slot-array-teardown-match-20260929.md).
Game owner-payload object spawn `func_150BDE90` is byte-exact across all 31
words after recovering its eight-byte local payload, fixed object-creation
request, and conditional copy to object offset `0x28`. The complete routine
emits directly from C with no guards; see
[Working Note 514](WORKING_NOTES/514-game-owner-payload-object-spawn-match-20260929.md).
Game indexed resource-chain teardown `func_150C0A48` is byte-exact across all
30 words after recovering its signed-index table walk, resource releases,
and post-release owner table reloads. The complete routine emits directly
from C with no guards; see
[Working Note 515](WORKING_NOTES/515-game-indexed-resource-chain-teardown-match-20260929.md).
Game owner-identity object spawn `func_151001B4` is byte-exact across all 31
words after recovering its eight-byte identity payload, fixed object request,
and conditional copy to object offset `0x28`. The complete routine emits
directly from C with no guards; see
[Working Note 516](WORKING_NOTES/516-game-owner-identity-object-spawn-match-20260929.md).
Game fixed-payload object spawn `func_1514D978` is byte-exact across all 31
words after recovering its 32-byte payload, allocation, copy, and tag-`0x13`
registration. The complete routine emits directly from C with no guards; see
[Working Note 517](WORKING_NOTES/517-game-fixed-payload-object-spawn-match-20260929.md).
Game record-window initializer `func_15183974` is byte-exact across all 31
words after recovering its five-word record indexing, two conditional record
initializations, and fourth-word copy. Four guarded words preserve one
equivalent record-pointer spill slot; see
[Working Note 518](WORKING_NOTES/518-game-record-window-initializer-match-20260929.md).
Game record-match release wrapper `func_1518F49C` is byte-exact across all 32
words after recovering its five-argument forwarding call, selector gate, and
two comparison keys. The complete routine emits directly from C with no
guards; see
[Working Note 519](WORKING_NOTES/519-game-record-match-release-wrapper-20260929.md).
Game callback-state setup `func_151E4E64` is byte-exact across all 33 words
after recovering its two setup calls, counter-controlled halfword flag, and
conditional callback/state installation. The complete routine emits directly
from C with no guards; see
[Working Note 520](WORKING_NOTES/520-game-callback-state-setup-match-20260929.md).
Game 25-byte group append `func_1502225C` is byte-exact across all 33 words
after recovering its per-group deduplication scan, append, and count update.
The complete routine emits directly from C with no guards; see
[Working Note 521](WORKING_NOTES/521-game-25-byte-group-deduplicating-append-match-20260929.md).
Game collision-classifier wrapper `func_15046C80` is byte-exact across all 32
words after recovering its four-argument ABI, three-way classification, and
class-zero delegation. The complete routine emits directly from C with no
guards; see
[Working Note 522](WORKING_NOTES/522-game-collision-classifier-wrapper-match-20260929.md).
Game secondary collision-classifier wrapper `func_15046F84` is byte-exact
across all 32 words after recovering its matching four-argument dispatch and
`func_15046D00` class-zero path. The complete routine emits directly from C
with no guards; see
[Working Note 523](WORKING_NOTES/523-game-secondary-collision-classifier-wrapper-match-20260929.md).
Game bounded table-buffer append `func_1507EBB8` is byte-exact across all 32
words after recovering its selector-indexed source and length tables, strict
40-byte bound, copy, and count update. The complete routine emits directly
from C with no guards; see
[Working Note 524](WORKING_NOTES/524-game-bounded-table-buffer-append-match-20260929.md).
Game coordinate-query wrapper `func_150A32B4` is byte-exact across all 31
words after recovering its stack-local `struct127`, coordinate field writes,
query submission, and inverted success result. The complete routine emits
directly from C with no guards; see
[Working Note 525](WORKING_NOTES/525-game-coordinate-query-wrapper-match-20260929.md).
Game randomized effect wrapper `func_150B6754` is byte-exact across all 35
words after recovering its two PRNG ranges, incoming byte/context forwarding,
and eight-argument effect call. The complete routine emits directly from C
with no guards; see
[Working Note 526](WORKING_NOTES/526-game-randomized-effect-parameter-wrapper-match-20260929.md).
Game motion-threshold updater `func_150CC638` is byte-exact across all 32 words
after recovering its flag gate, scaled byte limit, record threshold, and paired
float accumulation. Thirteen stale-checked guards normalize only IDO's
equivalent register/address schedule, including two retained pointer words;
see
[Working Note 527](WORKING_NOTES/527-game-motion-threshold-updater-match-20260929.md).
Game mode-selected color wrapper `func_150D22F4` is byte-exact across all 32
words after recovering its callback ABI, record-byte selection, paired
all-white/all-zero channel arguments, and signed selector forwarding. The
complete routine emits directly from C with no guards; see
[Working Note 528](WORKING_NOTES/528-game-mode-selected-color-wrapper-match-20260929.md).
Game current-player threshold dispatcher `func_150DEB58` is byte-exact across
all 34 words after recovering the `0x9A0` player-record view, float threshold,
embedded record pointers, and signed mode forwarding. The complete routine
emits directly from C with no guards; see
[Working Note 529](WORKING_NOTES/529-game-current-player-threshold-dispatch-match-20260929.md).
Game fixed resource-constructor wrapper `func_1514DBB8` is byte-exact across
all 32 words after recovering the complete 16-argument `func_15160A58` call,
resource pointer, and fixed constructor parameters. The routine emits directly
from C with no guards; see
[Working Note 530](WORKING_NOTES/530-game-fixed-resource-constructor-wrapper-match-20260929.md).
Game owner-payload allocation wrapper `func_1514F3CC` is byte-exact across all
32 words after recovering its 12-byte stack payload, fixed allocator request,
and conditional copy to returned-object offset `0x28`. The routine emits
directly from C with no guards; see
[Working Note 531](WORKING_NOTES/531-game-owner-payload-allocation-wrapper-match-20260929.md).
Game randomized RGBA initializer `func_15152ABC` is byte-exact across all 31
words after recovering its unsigned random remainders, five-entry RGB table,
byte-width index, and alpha range. It emits directly from C with no guards; see
[Working Note 532](WORKING_NOTES/532-game-randomized-rgba-initializer-match-20260929.md).
Game descriptor-copy allocator `func_15157898` now matches all 32 words
directly from C; see
[Working Note 533](WORKING_NOTES/533-game-descriptor-copy-allocation-wrapper-match-20260929.md).
Game indexed slot teardown `func_15172CA8` now matches all 32 words directly
from C; see
[Working Note 534](WORKING_NOTES/534-game-indexed-slot-teardown-event-pair-match-20260929.md).
Game four-resource teardown `func_1519F400` now matches all 35 words directly
from C; see
[Working Note 535](WORKING_NOTES/535-game-four-resource-teardown-match-20260929.md).
Game motion-threshold update `func_151AFC08` now matches all 32 words using its
semantic C body and the established duplicate-function guard set; see
[Working Note 536](WORKING_NOTES/536-game-second-motion-threshold-update-match-20260929.md).
Game linked-endpoint event handler `func_151B70B4` now matches all 36 words
after recovering its zero-event detach state and event-`0x2D` endpoint
replacement behavior. Nineteen stale-checked guards normalize one closed IDO
register/scheduling cycle; see
[Working Note 537](WORKING_NOTES/537-game-linked-endpoint-event-handler-match-20260929.md).
Game reflected byte-position update `func_151E55A8` now matches all 33 words
directly from semantic C after recovering its signed step, boundary reflection,
and direction toggle; see
[Working Note 538](WORKING_NOTES/538-game-reflected-byte-position-update-match-20260929.md).
Init primary/child record lookup `func_1000B1FC` now matches all 38 words
directly from semantic C after restoring its two original three-entry indexed
loops; see
[Working Note 539](WORKING_NOTES/539-init-primary-child-record-lookup-match-20260929.md).
Game indexed constructor wrapper `func_1501D1D4` now matches all 33 words
directly from semantic C after restoring its seven-argument constructor call,
two local outputs, and success/failure slot update; see
[Working Note 540](WORKING_NOTES/540-game-indexed-constructor-wrapper-match-20260929.md).
Game indexed 64-bit flag query `func_1501D2C4` now matches all 33 words
directly from semantic C, including retail's `__ll_lshift` helper ABI and
split high/low-word test; see
[Working Note 541](WORKING_NOTES/541-game-indexed-64-bit-flag-query-match-20260929.md).
Game auxiliary-state allocator `func_1503B7C0` now matches all 32 words
directly from semantic C after exposing the state pointer at `struct126`
offset `0x11C` and recovering its initialization; see
[Working Note 542](WORKING_NOTES/542-game-auxiliary-state-allocator-match-20260929.md).
Game packed-byte rate updater `func_15077404` now matches all 44 words after
recovering its signed 16-bit result truncation, negative clamp, and active or
fallback packed-byte stores. Thirty-three guarded source words and one
inserted scheduling word normalize the closed compiler allocation cycle; see
[Working Note 543](WORKING_NOTES/543-game-packed-byte-rate-update-match-20260930.md).
Game state-three convergence scanner `func_1509CDDC` now matches all 34 words
after restoring its initial slot processing and repeated 204-byte scans; see
[Working Note 544](WORKING_NOTES/544-game-state-three-convergence-scan-match-20260930.md).
Game object-position forwarding adapter `func_1509F77C` now matches all 33
words directly from C after exposing its three truncated coordinate locals;
see [Working Note 545](WORKING_NOTES/545-game-object-position-forwarding-adapter-match-20260930.md).
Game absolute-value ordering helper `func_150AD9A0` is restored from its false
zero-return C placeholder to its original handwritten 32-word assembly body;
see [Working Note 546](WORKING_NOTES/546-game-handwritten-absolute-ordering-helper-restoration-20260930.md).
The Game motion timestep integrator `func_150DEACC` now matches its complete
140-byte span directly from C; see
[Working Note 547](WORKING_NOTES/547-game-motion-timestep-integrator-match-20260930.md).
The Game record-type eligibility predicate `func_150EC3D4` now matches its
complete 136-byte span directly from C; see
[Working Note 548](WORKING_NOTES/548-game-record-type-eligibility-predicate-match-20260930.md).
The Game type-0x28 object sweep `func_150FDD10` now matches its complete
144-byte span through five guarded allocation words; see
[Working Note 549](WORKING_NOTES/549-game-type-28-object-sweep-match-20260930.md).
The Game camera-vector forwarding wrapper `func_1510B32C` now matches its
complete 132-byte span through eight guarded ABI/register words; see
[Working Note 550](WORKING_NOTES/550-game-camera-vector-forwarding-wrapper-match-20260930.md).
The Game indexed countdown finalizer `func_1510D694` now matches its complete
140-byte span directly from C; see
[Working Note 551](WORKING_NOTES/551-game-indexed-countdown-finalizer-match-20260930.md).
Its state-two structural twin `func_1510D720` also matches its complete
140-byte span directly from C; see
[Working Note 552](WORKING_NOTES/552-game-state-two-countdown-finalizer-match-20260930.md).
The Game two-tag record index scan `func_1511A410` now matches its complete
132-byte span through 13 guarded scheduling/register words; see
[Working Note 553](WORKING_NOTES/553-game-two-tag-record-index-scan-match-20260930.md).
The Game mode-gated object cleanup wrapper `func_1511A738` now matches its
complete 136-byte span directly from C; see
[Working Note 554](WORKING_NOTES/554-game-mode-gated-object-cleanup-wrapper-match-20260930.md).
The Game indexed saved-state restorer `func_151239CC` now matches its complete
136-byte span through two guarded stack-slot words; see
[Working Note 555](WORKING_NOTES/555-game-indexed-saved-state-restorer-match-20260930.md).
The Game bit-zero state-operation callback `func_1514E89C` now matches its
complete 132-byte span directly from C; see
[Working Note 556](WORKING_NOTES/556-game-bit-zero-state-operation-callback-match-20260930.md).
The Game owner-list cleanup `func_1514EDF0` now matches its complete 128-byte
span through three guarded local-stack operands; see
[Working Note 557](WORKING_NOTES/557-game-owner-list-matching-node-cleanup-match-20260930.md).
The Game two-entry selection event callback `func_15158B3C` now matches its
complete 148-byte span through ten guarded scheduling/register rows; see
[Working Note 558](WORKING_NOTES/558-game-two-entry-selection-event-callback-match-20260930.md).

## Verified build state

These commands passed from the current checkout on 2026-09-30:

```sh
make -C conker replace NON_MATCHING=1 -j4
make -C conker build/conker.us.elf
make -C conker match-progress NON_MATCHING=1
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

The successful non-matching build establishes that the current source links
and emits `conker.us.bin`. It does not establish a matching ROM hash or fresh
end-to-end gameplay acceptance.

## Resume boundary

Current Init task: recover the 954-word `__n_CSPHandleMIDIMsg`. Note 730
supersedes the earlier `func_10006380` segment-splitting recommendation and
the address-drift explanation in Note 729. Preserve the exact sequence/meta
handlers and retain the handwritten `init_5AB0` calling conventions.

1. The restoration baseline is banked. Do not fold a broad conversion batch
   into it; future work should start from a new focused commit.
2. Debugger is complete: 181 / 181 C-classified rows and the one handwritten
   assembly routine are linked byte-exact. Preserve the guarded
   `func_16000B14` normalization while broader matching continues.
3. The original `func_150AD780`/`func_150AD78C` trig slice is restored, and
   `func_150849A0` is byte-exact from a source-level index-lifetime fix, and
   `func_150636A4` is byte-exact through a guarded nested-pointer lifetime
   normalization, and `func_1514672C` is byte-exact through a guarded
   relocation-preserving load reorder. `func_15199980` is byte-exact from an
   explicit callback-pointer lifetime, `func_1505D024` is byte-exact through
   guarded call-argument register normalization, and `func_15071A64` is
   byte-exact from corrected stack-local declaration order, and
   `func_15087DCC` is byte-exact from separating the global base load from the
   indexed record pointer, and `func_1509D054` is byte-exact through guarded
   call-argument lifetime normalization. The five-word `func_150A7A00` is now
   restored as its original synthetic-return assembly trampoline,
   `func_150ADACC` is restored as handwritten assembly, `func_150BDB3C` is
   byte-exact through guarded scalar-temporary normalization, and
   `func_150F33B0` is byte-exact through guarded set-bit temporary
   normalization, and `func_151254F4` is byte-exact through guarded
   relocation-preserving opening-load scheduling. The nine-word
   `func_1515FB70` is restored to assembly ownership after its C model proved
   unable to preserve the retail undefined-return branch shape.
   `func_1505841C` is byte-exact through guarded FP-temporary and global-load
   register normalization. `func_150F02A0` is byte-exact after making its
   base-pointer and index lifetimes explicit and guarding the remaining
   temporary-register choices. `func_151B2FA0` is byte-exact after correcting
   its forwarded argument and callee declaration from `s16` to `s32`.
   `func_150770E4` is byte-exact after expressing its table lookup as retail's
   combined 812-byte stride. Handwritten `func_150A7770` is restored to its
   original eight-word assembly extent after the C model overflowed the slot.
   `func_1515F008` is byte-exact through six guarded, non-relocating
   pointer/value register choices. The adjacent `func_1516F8EC`,
   `func_1516F91C`, and `func_1516F984` cluster is byte-exact, completing the
   six-difference game tier. `func_15019BB8` is now byte-exact through seven
   guarded frame/address words. `func_1509F6B0` is byte-exact through seven
   guarded spill/reload scheduling words. `func_150C7930` is restored to its
   original 14-word assembly extent after exhaustive C forms could not retain
   its dead pointer update. `func_150CDB6C` is byte-exact through seven
   guarded, non-relocating destination-pointer schedule words.
   `func_15108B80` is byte-exact through seven guarded, non-relocating
   countdown register words. `func_1513A594` is byte-exact after correcting
   the forwarded byte ABI and retaining its post-call field read, with three
   guarded words for retail's empty branch shape. `func_151423D8` is
   byte-exact through seven guarded, non-relocating quadrant/table-index
   register words. `func_15155EF8` is byte-exact through seven guarded,
   non-relocating outer/child pointer lifetime words. Adjacent 11-word
   `func_151D7770` and `func_151D779C` are byte-exact from source-level
   pointer ordering and mask recovery, completing the seven-difference game
   tier. `func_1509F248` is byte-exact from source-level unsigned-halfword
   narrowing. `func_150C5EFC` is restored to its original 17-word assembly
   extent after IDO removed its dead pointer update. Structural twin
   `func_150C682C` is restored for the same reason. `func_150EA904` is
   byte-exact through eight guarded, relocation-preserving base/index and
   byte-update register words. `func_1515D480` is byte-exact through eight
   guarded frame and local-slot words. `func_151AB180`, the `+0x70` member of
   the dead child-pointer family, is restored to its original 17-word assembly
   extent. `func_151EF610`, the final eight-difference game row, is restored
   to original assembly ownership. `func_150771F0` is byte-exact through a
   relocation-aware argument-load schedule. `func_15080200` is byte-exact
   from chained global assignment. `func_1510E634` is byte-exact through the
   generated-slice guarded-expansion path. `func_1512D6B0` is byte-exact
   through guarded record-index register lifetimes. `func_15166FD8` is
   byte-exact through an independently guarded display-list cursor expansion.
   `func_15196330` and structural twin `func_151963B4` are byte-exact through
   independently verified guarded `v0`/`v1` lifetimes. `func_151E5F64` is
   byte-exact from source-level positive-branch control-flow recovery, with no
   guarded words. `func_151E81EC` is byte-exact from a four-word state struct,
   chained assignment, and six guarded paired-store relocation words.
   `func_1502EA0C` is byte-exact through ten guarded packed-byte scheduling
   and register words. `func_15033E84` is byte-exact from source-level
   next-pointer lifetime and loop-condition assignment recovery.
   `func_15094F40` is byte-exact through the guarded generated-slice cursor
   expansion. Structural relative `func_15096934` is independently byte-exact
   through its own guarded cursor expansion and state-byte clear.
   `func_150CF578` is byte-exact from source-level scalar and product
   lifetimes, with no guarded words. `func_150DE2C4` is byte-exact from a
   source-level short-circuit OR condition, also with no guarded words.
   Former placeholder `func_151318E8` is byte-exact as a source-level
   repeated float-scale loop while its caller remains exact. `func_15133A50`
   is byte-exact through source-level sum/store scheduling plus nine guarded
   FP-register words. `func_15133E3C` is byte-exact from a two-word aggregate
   initializer and corrected pointer ABI, with no guarded words. Continue
   through `func_151581D8`, now byte-exact through ten guarded prologue and
   argument-schedule words. `func_151D74B0` is byte-exact from source-level
   record-construction order, completing the ten-difference game tier.
   `func_150717E0` is byte-exact through eleven guarded local-record pointer,
   call-relocation, and epilogue schedule words. `func_15074A94` is byte-exact
   from a source-level interpolation expression plus eleven guarded FP-register
   words. `func_1507EEB8` is byte-exact from a source-level fixed reverse loop
   with no guarded rows. `func_150B6D34` is byte-exact from a simplified
   record-activation loop plus nine guarded cursor/register schedule words.
   `func_151090DC` is byte-exact from a typed two-word aggregate initializer
   and corrected pointer ABI, with no guarded rows. `func_15141564` is
   byte-exact from multiplication-first position scheduling plus two guarded
   base-pointer local-slot words. `func_15178E14` is byte-exact from corrected
   byte and forwarded-result callee contracts, with no guarded rows.
   `func_151ACA20` is byte-exact from candidate-first local declaration and a
   direct signed four-bit scaling assignment, with no guarded rows.
   `func_1501CFF8` is byte-exact from direct global count expressions and local
   lifetime ordering, with no guarded rows. `func_15031E2C` is byte-exact from
   twelve guarded register-schedule words, including two relocation-preserving
   table-address words. `func_150337E4` is byte-exact from direct field update,
   comparison, and table-index expressions, with no guarded rows.
   `func_1504BA38` is byte-exact through twelve guarded, non-relocating words
   that restore retail's three-byte record pointer and value-register
   lifetimes. `func_150882B0` is byte-exact from pointer-first local ordering,
   final `arg0` pointer reuse, and ten guarded schedule words that explicitly
   move the global relocation pair. `func_1508B194` is byte-exact from a
   source-level early-zero branch plus five guarded record-table base/index
   words. `func_150E33CC` is byte-exact through twelve guarded scheduling
   words that preserve its call relocation while restoring retail's `v0`
   value lifetime and call-delay argument move. `func_15131D4C` is byte-exact
   directly from a typed three-word aggregate copy and pointer-correct callee
   declaration, with no guarded words. `func_151355B8` is byte-exact after
   volatile field accesses retain retail's duplicate store, plus five guarded
   loaded/result register words. `func_15168800` is byte-exact directly from
   an explicit early null return, with no guarded words. Continue with 18-word
   `func_151E5FAC` is byte-exact from duplicated fallback returns, positive
   threshold control flow, and twelve guarded relocation/scheduling words,
   completing the twelve-difference game tier. `func_15002560` is byte-exact
   from an explicit top null test, scalar sibling-offset result, and two
   guarded commutative pointer adds. `func_150356C8` is byte-exact after
   simplifying its increment lifetime, plus nine guarded scheduling words
   that move the `D_800C3F08` low relocation. `func_15043B70` is byte-exact
   directly from a scalar ternary that restores retail's explicit two-arm
   chunk-selection merge. `func_1507A3E8` is byte-exact through thirteen
   guarded byte-load and merge-schedule words that preserve all four global
   relocation pairs. `func_1507FF94` is byte-exact after retaining a volatile
   local-record pointer across its first call, plus five guarded prologue
   scheduling words. `func_15085B70` is byte-exact directly from reversing
   its null condition so the zeroing path precedes the populated path, with no
   guarded rows. `func_150A7A14` is restored to its original thirteen-word
   assembly continuation because it returns through `t9` as the second half
   of `func_150A7A00`'s synthetic-return trampoline. `func_150CFBEC` is
   byte-exact directly from an outer record-pointer lifetime and repeated
   volatile source-field loads, with no guarded rows. `func_15131918` is
   converted from a placeholder to byte-exact C by typing its two callers'
   scale fields as floats and implementing the two-component scaling loop.
   `func_1514143C` is now byte-exact with thirteen guarded words that preserve
   retail's embedded-base lifetime and two inserted schedule words after
   source-only layout probes folded or grew a frame. `func_15144B68` is now
   byte-exact after a named result local restored retail's FP-register lifetime
   and two guarded words restored the independent opening compare/copy
   schedule. `func_1518F858` is now byte-exact directly from an explicit early
   return and volatile signed-byte index, restoring retail's repeated load,
   branch-likely epilogue, and callback-table register lifetimes.
   `func_1519072C` is now byte-exact directly from a contiguous local aggregate
   that preserves retail's `sp + 0x1C` record-pointer spill and `sp + 0x20`
   record across both calls. `func_1519582C` is now byte-exact from volatile
   pointer source plus eight guarded relocation/scheduling words that preserve
   retail's opening `v0`/`v1` global-address preload. `func_151A9024` is now
   byte-exact with thirteen guarded words that preserve retail's argument-home,
   byte-narrowing, early-epilogue, and call-relocation schedule.
   `func_151C9B64` is now byte-exact directly from corrected branch semantics
   and an explicit nested-pointer lifetime; no guarded words are required.
   The tied 13-word `func_151F892C` and `func_151F8960` rows are explicitly
   handwritten and consume non-ABI live registers, so they are excluded from
   the C-restoration queue. `func_1502C380` is now byte-exact directly from an
   assignment chain that preserves its destination-address and loaded-value
   lifetimes. `func_150A7B80` is now byte-exact after expressing its eight
   clears explicitly and using fourteen guarded overflow-slot words to retain
   retail's native 64-bit stores and diagonal writes. `func_1516A770` is now
   byte-exact directly from a delimiter-splitting loop: it replaces each
   `0xBD` byte with zero and returns the replacement count plus one.
   `func_1518F45C` is now byte-exact directly after its scalar array became a
   one-word aggregate and the callee's record parameter became `void *`.
   `func_151A5130` is now byte-exact after its indirect callback expression
   explicitly forwards all three incoming arguments, restoring the signed
   halfword narrowing and live-register ABI. `func_1508F060` is now byte-exact
   after correcting its state-block base to selected row two and applying nine
   guarded rows with three insertions for retail's explicit pointer arithmetic.
   `func_1518F89C` is now byte-exact from a typed float-record view plus twelve
   guarded scheduling words that retain the field base and both call delay
   slots. `func_151A561C` is now byte-exact directly from the same one-word
   aggregate and `void *` callee contract used by `func_1518F45C`.
   `func_151D343C` is now byte-exact from the third one-word aggregate and a
   corrected shared `func_15169260(void *, ...)` contract, with no matcher
   regressions. `func_1519F3B8` is now byte-exact from a typed four-word record
   plus nine guarded scheduling rows and one inserted reload.
   `func_15160274` is now byte-exact directly from a fourth one-word aggregate
   and a corrected local pointer contract. `func_151BD750` is now byte-exact
   through fifteen guarded FP scheduling rows and two inserted terminal words.
   `func_151417C4` is now byte-exact directly from a typed two-word aggregate,
   byte-typed first argument, and one-byte array local. `func_15144BC8` is now
   byte-exact directly after its normalized angle became an explicit `ret`
   local. `func_150718E4` is now byte-exact from corrected local ordering plus
   ten guarded post-random-call register words. `func_150142AC` is now
   byte-exact directly from a signed index and explicit invalid-range return.
   `func_15088270` is now byte-exact from a separate index lifetime plus ten
   guarded scheduling words. `func_15188A58` is now byte-exact after recovering
   its offset-`0x0C` linked-list append plus thirteen guarded control-flow
   words. Skip handwritten `func_151F892C` and `func_151F8960`; continue with
   20-word ordinary-C placeholder `func_1509F660`, now byte-exact directly
   after recovering its nullable lookup and two-way callback dispatch.
   `func_151C4510` is now byte-exact from explicit destination lifetimes plus
   fifteen guarded FP scheduling words. `func_150C78E0` is now byte-exact from
   seven guarded rows, including one inserted dead pointer advance and two
   moved global relocations. `func_15130230` is now byte-exact directly after
   explicitly passing its incoming `arg0` to the selected scene callback; no
   guarded rows were needed. `func_1506C32C` is now byte-exact directly after
   sharing one local across its choice-count and selected-index phases and
   placing the choices array between its scalar locals. `func_150CFDB8` is now
   byte-exact directly after removing its redundant pointer copy, mutating
   `arg0` across the record loop, and giving `max` and `next` retail's
   lifetimes. `func_150CFE3C` is now byte-exact after recovering its nested
   active-buffer state and adding six guarded base/register scheduling words.
   `func_15167010` is now byte-exact after deriving its table bound from the
   cursor and guarding retail's frame, saved-register, relocation, and end
   pointer lifetimes. `func_15167D84` is now byte-exact through thirteen
   guarded CFG/register-scheduling rows affecting its fifteen-word tail.
   `func_151D2E5C` is now byte-exact after correcting its owner-pointer call,
   recovering four explicit local lifetimes, and guarding one commutative
   branch word. `func_150104F0` is now byte-exact after recovering its chained
   zero assignment and guarding six base/store words, including one inserted
   result materialization. `func_150492CC` is now byte-exact through sixteen
   guarded floating-point and relocation-scheduling words that preserve its
   authored divisions by `2.0f`. `func_150767F4` is now byte-exact through
   sixteen guarded register-scheduling words; its existing C computes an
   indexed object's horizontal angle and triggers `func_15075400` when the
   masked delta is inside the doubled tolerance. Keep 17-word
   `func_150721A4` parked: its live C is intentionally retained despite a
   measured three-word compiler overflow. `func_1507A428` is now byte-exact
   through sixteen guarded global-load, relocation, and packed-value register
   words. `func_15084CB0` is now byte-exact after recovering its scalar
   lifetimes and indexed `u16` table access, plus seven guarded signed-loop and
   epilogue words. `func_15086D48` is now byte-exact after recovering indexed
   16-byte record access, plus six guarded signed-loop and fallback-epilogue
   words. `func_150F631C` now matches directly after recovering its owner
   lifetime and volatile repeated first-field reads. `func_15131958` now
   matches directly after restoring the count-controlled three-component
   vector scaling loop and correcting its local call signatures.
   `func_151419D0` is now byte-exact after sharing the source endpoint lifetime
   across both event paths and guarding one commutative branch operand-order
   word. `func_15143874` now matches directly after correcting its signed
   angle ABI and recovering explicit narrowed-angle and lookup-result
   lifetimes. `func_15147D1C` now matches directly after restoring the indexed
   callback's object, scalar, and normalized-byte arguments. `func_1515C158`
   is now byte-exact after restoring its two-row linked-list reset and
   guarding thirteen persistent IDO pointer-coloring words. `func_1515D520`
   is now byte-exact after recovering direct head testing and typed tail
   insertion, plus four guarded frame/scheduling words. `func_151635A8` is now
   byte-exact after correcting the indexed callback ABI and preserving two
   volatile table reads, plus fifteen guarded rows that normalize seventeen
   persistent scheduling/register words and insert the two missing epilogue
   words. `func_15168A4C` is now byte-exact after recovering its typed
   row/column list-head insertion and explicit scalar index lifetimes, plus
   four guarded `a2`-versus-`t0` register-color words. Keep generated
   `lwl`/`lwr` helpers `func_151F892C` and `func_151F8960` in the raw-assembly
   queue. `func_150747E4` is now byte-exact after recovering separate selected
   slot, decremented index, full update value, and actor-pointer lifetimes,
   plus ten guarded relocation/register-scheduling words. Continue with
   `func_150849CC`, now converted from its zero-return placeholder and
   byte-exact after restoring both selector paths, optional index output, and
   indexed byte return, plus three guarded CFG rows retaining one retail
   branch. `func_1508CA88` is now byte-exact after restoring its signed
   wrapping-counter CFG and preserving the independent final global-pointer
   reload with two guarded relocation-aware rows. `func_15116930` is now
   converted from its zero-return placeholder and byte-exact directly from C
   after retaining the owner-slot address through the state gates. Continue
   with 21-word `func_1511F92C`, which is now converted from its zero-return
   placeholder and byte-exact directly from C after restoring its nullable
   lookup and three-halfword copy. The 18-word `func_15130374` is now converted
   and byte-exact directly from C after correcting its six-argument forwarding
   ABI. The 21-word `func_1515572C` is now converted and byte-exact directly
   from C after restoring its typed two-word template copy and dispatch call.
   The 19-word `func_15178B98` is now converted and byte-exact directly from C
   after restoring its selector-based linked-list lookup. Continue with
   The 18-word `func_1519257C` is now converted and byte-exact directly from C
   after restoring its gated two-stage byte result. Continue with 19-word
   `func_151B82CC` is now byte-exact after correcting its callback signature,
   forwarding all three inputs, and retaining the child-pointer lifetime.
   The 19-word `func_1506AC0C` is now converted and byte-exact directly from C
   after restoring its typed object-selector record and dispatch call. The
   19-word `func_150881CC` is now byte-exact after retaining its clean scaled
   table-read C behavior and guarding five IDO register-scheduling words. The
   30-word `func_15088780` is now byte-exact directly from C after removing a
   one-use record pointer and restoring base-plus-scaled-index operand order.
   The 24-word `func_1509E8A0` is now converted and byte-exact directly from C
   after restoring its three-argument callback contract and two-case selector
   dispatch. The 21-word `func_150A34B0` is now converted and byte-exact
   directly from C after restoring its byte-`0x14` rejection, low-flag gate,
   and forwarded `func_150A3504` call. The 20-word `func_150A7CB0` is now
   byte-exact after restoring its floating identity element and guarding the
   final three-word store/return schedule. The adjacent 20-word
   `func_150A7DA0` is now byte-exact after restoring the four floating
   diagonal stores and three raw translation words, with six guarded
   register/schedule words. The 18-word `func_150ADA20` PRNG step is restored
   to original handwritten assembly ownership after the equivalent C was
   confirmed to compile as a 19-word overflow trampoline. The 30-word
   `func_150CFE98` buffer-advance helper is now byte-exact after recovering
   its one-use pointer and result lifetimes, with seven guarded frame/spill
   words. The 21-word `func_150F34A0` float threshold mapper is now converted
   from its zero-return placeholder and byte-exact directly from C, with no
   guarded words. The 20-word `func_150FADC8` event-bit callback is now
   converted from its zero-return placeholder and byte-exact directly from C,
   with no guarded words. Continue with 21-word `func_15133DE8`, the next
   ordinary Game C row with eighteen real differences. That 21-word
   `func_15133DE8` record/owner match callback is now converted from its
   zero-return placeholder and byte-exact directly from C after retaining the
   record identifier lifetime, with no guarded words. The current queue has
   advanced through `func_151E4E64`, whose complete 33-word callback-state
   setup now matches directly from C with no guarded words.
   `func_15106E78` is parked on a closed 30-versus-32-word caller-saved
   allocation cycle. Init `func_1000FF90` is now byte-exact across its complete
   35-word span. The 32-word auxiliary-state allocator
   `func_1503B7C0` is now byte-exact directly from C with no guards.
   `func_150413FC` is parked on a five-versus-four saved-register allocation
   cycle. The 44-word packed-byte rate updater `func_15077404` is now
   byte-exact with 33 guarded source words and one inserted scheduling word.
   The 34-word state-three convergence scanner `func_1509CDDC` is now
   byte-exact through 18 guarded contraction/scheduling rows.
   The 33-word object-position forwarding adapter `func_1509F77C` is now
   byte-exact directly from C. The handwritten 32-word `func_150AD9A0` is now
   restored to assembly ownership and exact independently. The 35-word motion
   timestep integrator `func_150DEACC` is now byte-exact directly from C.
   The 34-word record-type eligibility predicate `func_150EC3D4` is now
   byte-exact directly from C. The 36-word type-0x28 object sweep
   `func_150FDD10` is now byte-exact through five guarded allocation words.
   The 33-word camera-vector forwarding wrapper `func_1510B32C` is now
   byte-exact through eight guarded ABI/register words. The 35-word indexed
   countdown finalizer `func_1510D694` and its state-two structural twin
   `func_1510D720` are now byte-exact directly from C. The 33-word two-tag
   record index scan `func_1511A410` is now byte-exact through 13 guarded
   scheduling/register words. The 34-word mode-gated object cleanup wrapper
   `func_1511A738` is now byte-exact directly from C. The 34-word indexed
   saved-state restorer `func_151239CC` is now byte-exact through two guarded
   stack-slot words. The 33-word bit-zero state-operation callback
   `func_1514E89C` is now byte-exact directly from C. The 32-word owner-list
   cleanup `func_1514EDF0` is now byte-exact through three guarded local-stack
   operands. The 37-word two-entry selection callback `func_15158B3C` is now
   byte-exact through ten guarded scheduling/register rows. The 35-word
   transformed-position short writer `func_1516441C` is now byte-exact
   directly from C. The 33-word three-entry position queue writer
   `func_1517D578` is now byte-exact through 29 guarded allocation/scheduling
   words. The 33-word selector display-list appender `func_15183BA4` is now
   byte-exact directly from C. The 33-word command-`0x1D` payload allocator
   `func_1518AADC` is now byte-exact through ten guarded scheduling words.
   The 33-word object-selector payload wrapper `func_15192920` is now
   byte-exact through 17 guarded scheduling words. Its 33-word structural twin
   `func_151B1AB0` is also byte-exact through an independently scoped copy of
   the same schedule guards. The 35-word midpoint-timestep integrator
   `func_151CEA20` is now byte-exact through 21 guarded FP scheduling words.
   The 34-word global mode-state updater `func_151D66F0` is now byte-exact
   directly from C. Init `__osProbeTLB` is restored to its original
   handwritten CP0/TLB ownership, and its complete 48-word slot independently
   matches retail. The 44-word signed-position effect dispatcher
   `func_15013D38` is now byte-exact through five guarded setup-schedule words.
   The 33-word table-record dispatcher `func_15024130` is byte-exact through
   one guarded commutative address-add word. The 34-word byte-table index
   lookup `func_15041480` is byte-exact directly from C under its recovered
   no-unroll profile. The 35-word scripted-position effect dispatcher
   `func_15076768` is byte-exact through five guarded scheduling words.
   The 35-word random-duration selector `func_1507F4C0` is byte-exact through
   six guarded frame/stack-allocation words. The 34-word owner-payload
   allocator `func_150B0C58` is byte-exact directly from C. Continue with
   The 37-word fixed-point coordinate interpolator `func_150B73F0` is
   byte-exact through 24 guarded register-allocation words. Continue with
   The 34-word command-`0x38` owner-payload allocator `func_150D5440` is
   byte-exact directly from C. The 35-word owner-event dispatcher
   `func_150F15F8` is byte-exact through nine guarded identity-register words.
   The 34-word object-entry matrix builder `func_150F2518` is byte-exact
   through seven guarded address-register words. The 34-word command-`0x5C`
   owner-payload allocator `func_150F2C8C` is byte-exact directly from C.
   The 35-word event-`0x3E` owner dispatcher `func_150F7310` is byte-exact
   through 12 guarded identity-register and load-schedule words. Resume Init
   matching from its remaining 87 different C rows. The 48-word `osMapTLB`
   slot is restored from its empty C placeholder to original handwritten
   CP0/TLB assembly and independently matches all 192 bytes. The 44-word
   `osInvalDCache` slot is likewise restored to its original handwritten cache
   routine and independently matches all 176 bytes. The 40-word `osSetIntMask`
   slot is restored to its original handwritten CP0/MI mask routine and
   independently matches all 160 bytes. The 42-word identifier dispatcher
   `func_1000DE1C` is byte-exact through two guarded local-array address words.
   The adjacent 41-word record cleanup `func_1000DEC4` is byte-exact directly
   from C after recovering its combined 32-bit tail clear and original
   non-prototype state-query call schedule.
   The following 59-word channel-transition updater `func_1000DF68` is
   byte-exact through 12 guarded clamp/store/epilogue scheduling words.
   The 51-word channel level/mask updater `func_1000E588` is byte-exact
   directly from recovered semantic C with no guards. The 46-word fixed-point
   parameter wrapper `func_10010E78` is byte-exact through one guarded
   commutative multiply word; its other 45 words emit directly from C. The
   40-word `bzero` row is restored from an approximate byte loop to original
   handwritten libultra assembly and independently matches all 160 bytes. The
   54-word released-node recycler `func_1000A348` is byte-exact through 19
   guarded manager-register and reusable-list scheduling words. The 52-word
   actor-coordinate refresh callback `func_1000EE70` is byte-exact through 18
   guarded temporary-register words; its frame, control flow, call, and actor
   update behavior emit directly from C. The 49-word mode-flag dispatch
   wrapper `func_1000CAE4` is byte-exact directly from semantic C with no
   guarded words. The 52-word packed-timer callback `func_1000EDA0` is
   byte-exact through 11 guarded temporary-register words after restoring its
   real seven-argument ABI and expiry dispatch. The 54-word single-node
   release recycler `func_10009BE4` is byte-exact through 26 guarded manager,
   sentinel, and reusable-list scheduling words. The 58-word halfword-table
   selector `func_10011EB8` is byte-exact after two bounded guards restore
   retail's redundant mapped-input copies and move the existing call
   relocation. SDK helpers `__osLeoAbnormalResume` and `__osLeoResume` are
   byte-exact directly from their recovered `-O1` libultra C bodies with no
   guards. The 60-word `osLeoDiskInit` is byte-exact from its recovered `-O1`
   initializer plus seven bounded guards that normalize one shared-address
   schedule and preserve the retail extent. The 68-word
   `_VirtualToPhysicalTask` is byte-exact directly from its recovered SDK
   copy-and-convert body with no guards. The 57-word spatial channel-value
   updater `func_1000C934` is byte-exact through 18 guarded value-register and
   epilogue scheduling words. The 60-word actor sound dispatcher
   `func_10010630` is byte-exact through 54 guarded saved-value, argument, and
   relocation scheduling words. The 65-word dual-framebuffer clear
   `func_10003ACC` is byte-exact through 57 guarded register-allocation and
   loop-scheduling words after recovering its scalar first fill and
   remainder-plus-four-pixel second fill; see
   [Working Note 600](WORKING_NOTES/600-init-dual-framebuffer-clear-match-20260930.md).
   The 67-word record mask filter `func_1000CDA0` is byte-exact after
   recovering its narrow mask ABI, validation gates, conditional flag update,
   and post-call index reload. Eighteen guards normalize its local slot and
   default-return schedule; see
   [Working Note 601](WORKING_NOTES/601-init-record-mask-filter-match-20260930.md).
   The 71-word entry mask value updater `func_1000E46C` is byte-exact
   directly from C after recovering its saturated percentage conversion,
   channel dispatch, mask update, and signed set-bit walk. Reusing the
   incoming value and mask parameters preserves retail's saved-register
   lifetimes without guards; see
   [Working Note 602](WORKING_NOTES/602-init-entry-mask-value-updater-match-20260930.md).
   The 70-word active-entry mode dispatcher `func_1000E2F4` is byte-exact
   after recovering its three-entry scan, channel stop/release paths, and
   final mode-byte store. Twelve guards normalize one non-relocating metadata
   test register cycle; see
   [Working Note 603](WORKING_NOTES/603-init-active-entry-mode-dispatcher-match-20260930.md).
   The 74-word chunked PI DMA reader `func_100046E4` is byte-exact after
   recovering its thread-selected queue, cache invalidation, `0x14000`-byte
   transfer loop, and blocking completion waits. Four guards normalize only
   the frame and message-local offsets; see
   [Working Note 604](WORKING_NOTES/604-init-chunked-pi-dma-reader-match-20260930.md).
   The 83-word spatial-volume callback `func_1000C7E8` is byte-exact after
   recovering its active-state setup and clamped radial channel calculation.
   Fifty guards normalize one closed IDO floating-point allocation and
   instruction schedule; see
   [Working Note 605](WORKING_NOTES/605-init-spatial-volume-callback-match-20260930.md).
   The 84-word framebuffer task dispatcher `func_10004DB0` is byte-exact
   after restoring its nonblocking task receive, VI framebuffer gates,
   countdown update, and phase dispatch. Nine guards normalize the remaining
   local branch schedule; see
   [Working Note 606](WORKING_NOTES/606-init-framebuffer-task-dispatcher-match-20260930.md).
   The 84-word nonrepeating random selector `func_1000F568` is byte-exact
   after recovering its bounded selection, per-record availability mask,
   cyclic fallback scan, and mask replenishment. Eleven guards normalize five
   shifted branches, five commutative operand orders, and one optimized-away
   reset assignment; see
   [Working Note 607](WORKING_NOTES/607-init-nonrepeating-random-selector-match-20260930.md).
   The 84-word planar direction encoder `func_1000B060` is byte-exact after
   recovering its vector normalization, signed-angle fold, caller offset,
   range bands, and encoded return value. Twenty-six guards normalize one
   closed FP/integer allocation and schedule; see
   [Working Note 608](WORKING_NOTES/608-init-planar-direction-encoder-match-20260930.md).
   The 85-word nearest-listener spatial query `func_100114D0` is byte-exact
   after recovering its inclusive entry scan, unsigned squared-distance
   selection, coordinate setup for `func_1000A420`, and fixed-point output
   scale. Fifty guards normalize one closed allocation and call schedule; see
   [Working Note 609](WORKING_NOTES/609-init-nearest-listener-spatial-query-match-20260930.md).
   The 97-word pending note-end query `func_1001ADA4` is byte-exact after
   restoring its SDK queue scan, accumulated event time, note-end selection,
   and allocated-to-free-list transfer. Twenty replacement guards and one
   checked insertion normalize the closed relink/return tail; see
   [Working Note 610](WORKING_NOTES/610-init-pending-note-end-query-match-20260930.md).
   The 91-word controller-pak read packet builder `__osPackRamReadData` is
   byte-exact after restoring Conker's opening 16-word PIF RAM clear. Its full
   packet construction and retained slot padding emit directly from C with no
   guards; see
   [Working Note 611](WORKING_NOTES/611-init-controller-pak-read-packet-builder-match-20260930.md).
   The 88-word channel-state initializer `func_1000E934` is byte-exact after
   recovering its paired table fills, per-channel reset and state clears,
   record-table clear, and 12 sentinel stores. Twenty-nine stale-checked
   guards normalize independent compiler scheduling, including six moved low
   relocations; see
   [Working Note 612](WORKING_NOTES/612-init-channel-state-initializer-match-20260930.md).
   The 91-word deferred-record compactor `func_10011310` is byte-exact after
   recovering its delay countdown, resource-slot release, survivor count, and
   unaligned in-place record compaction. Fifty-nine stale-checked guards,
   including ten checked insertions, preserve retail's rematerialized global
   addresses and integer-index schedule; see
   [Working Note 613](WORKING_NOTES/613-init-deferred-record-compactor-match-20260930.md).
   The 92-word audio-DMA cleanup routine `func_100099BC` is byte-exact after
   recovering its completion-queue drain, generation-expiry scan, active-list
   unlink, and free-list splice. Fifty-six stale-checked replacement guards
   and one checked insertion normalize the closed compiler allocation and
   branch schedule; see
   [Working Note 614](WORKING_NOTES/614-init-audio-dma-cleanup-match-20260930.md).
   The 93-word channel attachment routine `func_1000B3D4` is byte-exact after
   recovering its direct-parent replacement path, three-slot allocator scan,
   and idle-child retirement path. Sixty-five words emit directly from the
   recovered C; 28 stale-checked replacements normalize three closed register
   allocation cycles with no relocation rewriting; see
   [Working Note 615](WORKING_NOTES/615-init-channel-attachment-match-20260930.md).
   The 94-word SDK entrypoint `osCreateViManager` is byte-exact after
   restoring its event queues, manager state, priority handling, interrupt
   gate, and VI thread startup. Its complete routine emits directly from C
   with no guards; see
   [Working Note 616](WORKING_NOTES/616-init-create-vi-manager-match-20260930.md).
   The adjacent 102-word VI manager thread `viMgrMain` is also byte-exact
   after restoring the canonical retrace dispatch, client notification,
   timer interrupt, and 64-bit timekeeping loop. All opcodes emit directly
   from C; ten stale-checked relocation-only guards bind its discarded
   function-local static to the retail retrace-counter address. See
   [Working Note 617](WORKING_NOTES/617-init-vi-manager-main-match-20260930.md).
   The 96-word controller-pak write packet builder `__osPackRamWriteData` is
   byte-exact after restoring Conker's 16-word PIF RAM clear and the canonical
   channel-prefix loop shape. Its complete slot emits directly from C with no
   guards; see
   [Working Note 618](WORKING_NOTES/618-init-controller-pak-write-packet-builder-match-20260930.md).
   The 94-word audio-record cleanup and dispatch routine `func_1000E17C` is
   byte-exact after recovering its three passes over the twelve-record pool.
   Eighteen stale-checked replacements normalize one closed allocation and
   address-completion schedule; five relocation-only guards retain the three
   independent retail address lifetimes. See
   [Working Note 619](WORKING_NOTES/619-init-audio-record-cleanup-dispatch-match-20260930.md).
   The adjacent 140-word controller-pak write transaction
   `__osContRamWrite` is byte-exact after restoring Conker's per-attempt
   16-word PIF RAM initialization and status clear, then removing a redundant
   error reassignment so the existing channel error remains authoritative.
   Its complete routine emits directly from C with no guards; see
   [Working Note 620](WORKING_NOTES/620-init-controller-pak-write-transaction-match-20260930.md).
   The 104-word audio thread `func_10009400` is byte-exact after recovering
   its message loop, two-frame audio submission cycle, completion receive,
   shutdown dispatch, audio-manager close, and terminal receive loop. Twenty-
   seven stale-checked guards normalize local stack placement, one closed
   `s3`/`s4` allocation swap, and the close schedule; see
   [Working Note 621](WORKING_NOTES/621-init-audio-thread-loop-match-20261001.md).
   The 105-word nearest-anchor forwarding helper `func_1000F6B8` is byte-exact
   after recovering its signed-coordinate inputs, nearest-record scan, retained
   relative vectors, and twelve-argument `func_1000A420` dispatch. Sixty-eight
   stale-checked rows normalize 69 compiler-allocation and scheduling words,
   including relocation-aware address and call movement; see
   [Working Note 622](WORKING_NOTES/622-init-nearest-anchor-forwarder-match-20261001.md).
   The 109-word DMA page-cache helper `func_100097CC` is byte-exact after
   recovering its active-page hit scan, free-node allocation and doubly linked
   list repair, 0x800-byte DMA setup, frame stamp, and odd-address restoration.
   Thirty-five words emit directly from semantic C; 74 relocation-aware,
   stale-checked rows normalize compiler register allocation and scheduling.
   See
   [Working Note 623](WORKING_NOTES/623-init-dma-page-cache-helper-match-20261001.md).
   The 115-word object-aware audio dispatcher `func_10010FFC` is byte-exact
   after recovering its validity gates, camera-specific direct dispatch,
   three-quarter volume path, object-type scale lookup and clamp, position
   truncation, and spatial forwarding call. Eleven words emit directly from
   semantic C; 104 relocation-aware, stale-checked rows normalize a persistent
   compiler scheduling displacement and its resulting register allocation.
   See
   [Working Note 624](WORKING_NOTES/624-init-object-audio-dispatch-match-20261001.md).
   The adjacent 109-word audio request allocator `func_1000FA64` is byte-exact
   after recovering its bounded 32-entry allocation, callback-dependent flag
   setup, optional coordinate replacement, packed request initialization,
   cents-to-ratio conversion, queue submission, and committed-handle return.
   Nine words emit directly from semantic C; 100 relocation-aware,
   stale-checked rows normalize IDO's stack, scheduling, and register choices.
   See
   [Working Note 625](WORKING_NOTES/625-init-audio-request-allocator-match-20261001.md).
   The 119-word allocator free/coalescing routine `func_10004074` is also
   byte-exact after recovering its interrupt-protected physical-block merges,
   free-list repair and sorted insertion, tail update, and largest-free-block
   cache maintenance. Twenty-four words emit directly from semantic C; 95
   relocation-aware, stale-checked rows normalize IDO's frame, allocation,
   branch, and scheduling choices. See
   [Working Note 626](WORKING_NOTES/626-init-allocator-free-coalescing-match-20261001.md).
   The 145-word controller-pak read routine `__osContRamRead` is byte-exact
   directly from C after restoring the retry-time 16-word PIF RAM reset and
   preserving `CHNL_ERR` as the no-pak result instead of redundantly assigning
   the same value. No expected-word guards are used. See
   [Working Note 627](WORKING_NOTES/627-init-controller-pak-read-match-20261001.md).
   The 117-word direct PI copy routine `func_1000480C` is byte-exact after
   recovering its ownership and PI-busy waits, aligned word-copy path,
   two-byte-misaligned halfword path, and conditional PI-manager restart.
   Its 113-word semantic C body is normalized to retail's frame, saved-register
   allocation, and schedule by 112 stale-checked relocation-aware rows,
   including two inserted epilogue words. See
   [Working Note 628](WORKING_NOTES/628-init-direct-pi-copy-match-20261001.md).
   The 120-word packed audio-state transition routine `func_1000C350` is
   byte-exact after recovering its first-entry setup, mode-specific channel
   updates, level-0x1D state synchronization, and packed return value. All but
   one word emit directly from semantic C; one stale-checked guard preserves a
   commutative equality branch's retail operand order. See
   [Working Note 629](WORKING_NOTES/629-init-packed-audio-state-transition-match-20261001.md).
   The 125-word actor event/audio dispatcher `func_1000EFB4` is byte-exact
   after recovering its actor-presence gates, terminated actor-ID scan,
   position/result output, and three event-specific sound paths. Its complete
   500-byte body emits directly from semantic C without word guards. See
   [Working Note 630](WORKING_NOTES/630-init-actor-event-audio-dispatch-match-20261001.md).
   The 124-word actor positional-audio creator `func_10010154` is byte-exact
   after recovering its direct camera path, actor-ID-specific range and flag
   policy, prior-handle retirement, and positional replacement allocation.
   Seventy-eight words emit directly from semantic C; 46 stale-checked rows
   normalize IDO's remaining register allocation and scheduling. See
   [Working Note 631](WORKING_NOTES/631-init-actor-positional-audio-creator-match-20261001.md).
   The 126-word sequence-buffer replacement routine `func_10008CE8` is
   byte-exact after recovering its bounded stop polling, old-buffer release,
   8-byte metadata lookup, aligned replacement copy, and player restart.
   Semantic C emits 121 words directly; five stale-checked rows normalize two
   independent IDO stack-slot selections. See
   [Working Note 632](WORKING_NOTES/632-init-sequence-buffer-replacement-match-20261001.md).
   The 126-word threshold audio-state callback `func_1000B638` is byte-exact
   after recovering its player-value gate, level-specific channel transitions,
   and separate level-`0x27` effect bit. Semantic C emits 114 words directly;
   12 stale-checked rows normalize one closed register-allocation cycle and one
   stack-slot selection. See
   [Working Note 633](WORKING_NOTES/633-init-threshold-audio-state-callback-match-20261001.md).
   The 133-word actor secondary-audio creator `func_10010344` is byte-exact
   after recovering its direct camera path, actor-specific positional policy,
   prior-handle retirement, and replacement allocation. Semantic C emits 115
   words directly; 18 stale-checked rows normalize register allocation and an
   independent store schedule, including two relocation-aware rows. See
   [Working Note 634](WORKING_NOTES/634-init-actor-secondary-audio-creator-match-20261001.md).
   The 133-word three-channel audio-mix coordinator `func_1000D758` is
   byte-exact after recovering its record classification, prioritized channel
   policy, three-channel refresh, and frame-parameter forwarding. Semantic C
   emits 112 words directly; 21 stale-checked rows normalize one closed
   register-allocation cycle, including four relocation-preserving rows. See
   [Working Note 635](WORKING_NOTES/635-init-three-channel-audio-mix-coordinator-match-20261001.md).
   The 139-word audio-task submission routine `func_100095A0` is byte-exact
   after recovering its AI backlog policy, aligned output selection,
   `n_alAudioFrame` call, scheduler-task construction, queue submission, and
   command-buffer toggle. Semantic C emits 68 words directly; 71 stale-checked
   rows normalize compiler allocation and scheduling while preserving all
   relocation targets. See
   [Working Note 636](WORKING_NOTES/636-init-audio-task-submission-match-20261001.md).
4. Init's `__osGetSR`, `osGetCount`, `__osSetCompare`, `__osSetSR`, and
   `__osSetFpcCsr` placeholders are restored to original low-level assembly
   ownership. Their complete 16-byte padded spans match retail independently.
   The 26-word `func_1000FE88` is now byte-exact through two guarded,
   non-relocating current-pointer spill/reload words; its recovered C behavior
   is unchanged. The adjacent handwritten interrupt pair `__osRestoreInt` and
   `__osDisableInt` is also restored from false C placeholders; both complete
   32-byte spans match retail. The 22-word `func_100043B4` is now byte-exact
   through a guarded six-word store/call/epilogue schedule, including an
   explicit relocation move and retail's otherwise dead pointer adjustment.
   The 47-word `func_1000FD38` is also byte-exact through six guarded words
   that retain retail's loop bound across no-call iterations and refresh it
   only after a resource-release call. The nine-word `func_10001420` is now
   restored from its overflow-trampoline C model to its original handwritten
   memory-clear loop; its full 36-byte span matches retail independently. The
   11-word `func_100038E0` is likewise restored from an equivalent but
   compiler-shaped C model to its original handwritten MMIO setup body; its
   full 44-byte span matches retail independently. The empty
   `osWritebackDCacheAll` C placeholder is now replaced by its original
   handwritten 12-word cache-operation loop; its full 48-byte span matches
   retail independently. The empty `osUnmapTLB` placeholder is likewise
   replaced by its original 16-word CP0/TLB body; its full 64-byte span matches
   retail independently. The explicitly handwritten 13-word unaligned-load
   helpers `func_151F892C` and `func_151F8960` are now restored from false
   zero-return placeholders; both complete 52-byte spans match retail.
   The 19-word `func_151444DC` integer range wrapper is now byte-exact directly
   from C after expressing both adjustment loops as `do/while`, recovering
   retail's two branch-likely delay-slot updates without guarded words.
   The 20-word `func_151464B8` active-player-mask predicate is also byte-exact
   directly from C after recovering its byte return type, explicit loop
   initialization order, and masked-value lifetime. The final register-only
   mismatch was resolved with optimized-away expressions; no guarded retail
   words are used. Continue ordinary Game reconstruction with the 20-word
   generated-slice placeholder `func_1514ED3C`. That linked-list lookup is now
   reconstructed and byte-exact directly from typed C after retaining separate
   current/next pointer lifetimes and declaration order. Continue with
   20-word `func_15178BE4`. That node initializer is now reconstructed and
   byte-exact directly from typed C. The following 20-word `func_15187FC0`
   indexed color extractor is also reconstructed and byte-exact directly from
   typed C. The 21-word `func_15190400` event-owner release handler is now
   byte-exact directly from typed C as well. The following 21-word
   `func_15191B8C` unregister-and-broadcast wrapper is also byte-exact directly
   from typed C. The 21-word `func_151A4F7C` embedded-owner release handler is
   now byte-exact directly from typed C as well. The 21-word
   `func_151B22F4` slot-state predicate is also byte-exact directly from typed
   C. The 23-word `func_151D73A8` callback dispatch is now byte-exact after
   preserving retail's two volatile index and entry reads. The adjacent
   `func_151A8584`/`func_151A85D4` pair is now exact through symmetric guarded
   callback-path scheduling; see Working Note 482. The 20-word `func_1502E474`
   conditional submission wrapper and
   33-word `func_150319CC` two-pass list lookup and 21-word `func_151087FC`
   event-flag handler, 21-word `func_150EC45C` preset wrapper, and 20-word
   `func_150F2390` conditional stack-record wrapper are now byte-exact directly
   from C. The former `func_150F1684` two-local register boundary is resolved
   by the guarded match in Working Note 475.
   The 21-word `func_1514A498` motion-decay update is also byte-exact after one
   guarded word preserves retail's equivalent `multu v0,t7` operand order.
   `func_15155FD4` is now byte-exact after eight guarded words normalize the
   owner/end register allocation; see Working Note 484. The 20-word
   `func_15181DC8` per-slot reset is byte-exact after two
   guarded words preserve retail's redundant second floating zero. The
   21-word `func_1518F108` two-component decay twin is also byte-exact after
   one guarded word preserves retail's equivalent `multu v0,t7` operand
   order. The 20-word `func_15192308` embedded-address setup wrapper is now
   byte-exact directly from a typed six-argument call. The 20-word
   `func_151A73EC` bounded embedded-owner release helper is also byte-exact
   directly from nested typed C. The 20-word `func_151AF338` float ABI adapter
   is now byte-exact directly from a typed seven-argument wrapper. The 20-word
   `func_151B4C1C` embedded cleanup and callback-dispatch wrapper is now exact
   directly from typed C. The twin 20-word `func_151B50A4` float ABI adapter
   is also byte-exact from the same typed wrapper shape. The 21-word
   `func_151B7678` validated-position reader is now exact from a typed pointer
   chain and short-circuit failure condition. The 22-word `func_151B8318`
   optional matching-record release gate is now exact from typed C and an
   explicit record-word lifetime. The 22-word `func_151D8D5C` two-event
   release callback is now exact from a typed callback signature and explicit
   event branches. The 20-word `func_15083FB0` object-index wrapper is now
   exact after correcting the local `func_15083E90` byte-parameter and pointer
   return contract. The 22-word `func_1515D030` reverse-slot update is now
   exact from a signed decrement and one shared result variable.
   `func_1506EF5C` is now byte-exact after restoring retail's repeated active-
   object reads and guarding its register allocation; see Working Note 483.
   Keep `guMtxIdentF` parked at its measured compiler scheduling boundary.
   The former `func_1507A4D4` boundary is now
   resolved by the guarded match in Working Note 474. The 21-word `func_15178750`
   conditional callback wrapper and the previously hidden two-word
   `func_151787A4` table callback are now separately inventoried and exact.
   The 21-word `func_150C522C` four-slot release loop is byte-exact through
   two guarded relocation-aware words that preserve retail's independent
   low-half address-completion schedule. The 21-word `func_150C5F40`
   existing-record/allocator wrapper and its `+0x70` structural twin
   `func_150C6870` are byte-exact directly from typed C. The 21-word
   `func_150C7968` flag-gated optional-record update is byte-exact through
   five guarded schedule/relocation entries, including retail's dead pointer
   advance. The 21-word `func_150EB430` stack-vector sum wrapper is byte-exact
   after reversing commutative source operands and guarding four `a2`/`a3`
   lifetime words. The 21-word `func_15155F3C` state-transition wrapper is
   byte-exact through three guarded state-register words. The former
   `func_15155FD4` boundary is resolved in Working Note 484. The 22-word
   `func_1507A47C` packed actor-mask
   clear is now byte-exact through a named mask local and eighteen guarded
   relocation-aware scheduling words. The 24-word `func_150C5310` mode-flag
   toggle is now byte-exact directly from typed C, including three tracked
   padding words. The 24-word `func_150E2FC0` marker-record swap is now
   byte-exact from typed C plus one guarded equivalent branch-operand word.
   The 26-word `func_15125628` four-timer decrement is restored to its
   original handwritten assembly ownership. Keep `func_150721A4` parked; the
   former `func_151A8584`/`func_151A85D4` boundary is resolved in Working
   Note 482. The 33-word
   `func_1505DFDC` backing-buffer reset is byte-exact directly from C after
   restoring the full-width index, repeated table read, declaration order,
   and source store order. The apparent 60-word `func_150AD8B0` C row is now
   correctly restored to its handwritten 19-word vector cross-product body;
   its generated-slice span also covers 41 already exact padding/helper words.
   The 22-word `func_15131C2C` flag-gated callback dispatcher is byte-exact
   directly from its typed three-argument callback contract. The 24-word
   `func_1515F0AC` signed clamp is byte-exact from C plus three guarded
   scheduling entries. The 21-word `func_1516706C` callback-table loop is
   byte-exact from a post-tested loop plus two guarded relocation-aware words.
   The 29-word `func_15168A9C` list unlink, 23-word `func_15179AB8`
   backward active-object flag scan, 26-word `func_15194AB4` state mapper,
   29-word `func_151957B0` tail insertion, and two-word hidden no-op
   `func_15195824`, 22-word `func_151A8A20` bounded callback dispatcher, and
   20-word `func_151A8F1C` transform wrapper are byte-exact directly from C.
   The 21-word `func_151AA17C` dual event-record dispatch is byte-exact from
   recovered C semantics plus ten guarded scheduling/local-slot words.
   Its 21-word structural twin `func_151AA210` is independently byte-exact
   through the same C shape and separately scoped guards.
   The 21-word `func_151CF844` conditional record forwarder is byte-exact
   directly from C without guarded words. The 21-word `func_151D10E4`
   indexed record forwarder is byte-exact from recovered C semantics plus
   twelve guarded scheduling words, including relocation-aware movement of
   the `D_800AAF9C` table load.
   The 21-word `func_151D4D58` two-mode preset wrapper and 23-word
   `func_151E7E9C` three-way state dispatcher are byte-exact directly from C
   without guarded words. The 22-word `func_15022190` flagged coordinate
   setter, 24-word `func_15023870` null-gated event-byte copy, and 32-word
   `func_15033328` swimming-attachment lifetime callback are also byte-exact
   directly from C. The 22-word `func_1503378C` six-ID type predicate is also
   byte-exact directly from C. The 22-word `func_15044DE8` guarded mode-4
   dispatcher is also byte-exact directly from C. The 22-word
   `func_15088218` fixed-point/float record value is byte-exact from recovered
   C semantics plus nine guarded scheduling words. The false zero-return
   placeholder at `func_150AF738` is now a byte-exact stack-record forwarder
   from recovered C semantics plus fifteen guarded scheduling words. The false
   zero-return placeholder at `func_150BB700` is now a byte-exact event-bit
   updater directly from C. Its false-placeholder template twin
   `func_150D1BD0` is also byte-exact directly from C. The 22-word
   `func_150E411C` eight-argument parameter preset is byte-exact directly from
   C. The false zero-return placeholder at `func_150EB030` is now a byte-exact
   nested state classifier directly from C. The 22-word `func_150FB1E8`
   five-argument two-stage forwarder is byte-exact directly from C. The
   23-word `func_150FB240` signed-halfword mapper is byte-exact directly from
   C. The 22-word `func_150FFD2C` type-and-flag-gated dispatcher and 23-word
   `func_151076A4` volatile callback-table dispatcher are also byte-exact
   directly from C. The 23-word `func_1510A870` paired-record updater is
   byte-exact from recovered C semantics plus one guarded commutative-branch
   operand word. Its 25-word tracked-layout twin `func_1510A8CC` is also
   byte-exact from the same recovered C and guard; 23 words are executable and
   two are trailing layout padding. The 22-word `func_1512D6F0` indexed-record
   reset is byte-exact directly from structured C without guarded words.
   The 23-word `func_1513BA78` two-way type dispatcher is byte-exact directly
   from C after adding typed callee declarations; no guarded words are needed.
   The 37-word `func_15144598` mode-dependent area scaler is byte-exact
   directly from corrected field offsets, signed dimensions, case order, and
   commutative operand order. The 25-word `func_15149BF4` two-axis float
   damping threshold is byte-exact directly from C without guarded words.
   The 23-word `func_1514ECE0` signed-key list search is byte-exact directly
   from C as the halfword-key twin of `func_1514ED3C`, without guarded words.
   The 22-word `func_15159BB0` effect callback adapter is byte-exact directly
   from C with a position vector, zero velocity, and typed effect record.
   The 22-word `func_15172C50` two-table initializer is byte-exact directly
   from a 16-entry C loop whose body IDO unrolls four ways.
   The 22-word `func_15172D28` object state-transition wrapper is byte-exact
   directly from C, including both branch-likely early-return paths.
   The 22-word `func_151749A0` wrapped timer/counter updater is byte-exact
   directly from C with byte-width arithmetic preserved.
   The 22-word `func_1517F75C` inclusive player-timer decay loop is byte-exact
   directly from C with unsigned halfword clamping preserved.
   The 22-word `func_15181D70` enabled player-state initializer is byte-exact
   directly from C as the nonzero twin of `func_15181DC8`.
   The 24-word `func_1518A360` paired endpoint updater is byte-exact from C
   with one guarded commutative branch-operand normalization.
   The 23-word `func_151904BC` callback/resource cleanup is byte-exact from C
   with five guarded branch and call-setup scheduling words.
   The 23-word `func_15197A0C` scaled query wrapper is byte-exact directly
   from C after restoring its incoming argument. The adjacent 24-word
   `func_1519F108` and `func_1519F168` state-clear callbacks are byte-exact
   from shared C shapes plus symmetric guarded address-lifetime and branch
   scheduling normalization. The 23-word `func_151A09B4` conditional child
   teardown is byte-exact directly from C with no guarded words. The 22-word
   `func_151B4E4C` position/effect wrapper is also byte-exact directly from C.
   The 23-word `func_151EFF94` variadic formatting wrapper is byte-exact
   directly from C using the established `&arg1 + 1` argument cursor.
   The 23-word `func_15044CE4` position/scale initializer is byte-exact from
   recovered C plus seven guarded register-lifetime words. The existing C for
   36-word `func_1508855C` is byte-exact with 22 guarded register-lifetime and
   equivalent control-flow scheduling words; its two table relocations retain
   their original identities. The former 26-word `func_150A6500` row contained
   two functions: the recovered 14-word bounded-query wrapper is exact from C
   plus 12 guarded scheduling words, while newly identified 12-word
   `func_150A6538` remains exact original assembly pending a source-grounded
   calling convention. The 23-word `func_150BE438` object-record writer is
   byte-exact directly from recovered C with no guarded words. The 23-word
   `func_150D1410` object-index flag updater is also byte-exact directly from C
   with no guarded words. The 23-word `func_150D2054` six-entry cleanup loop
   is byte-exact directly from C after preserving its byte-width counter and
   indexed array expression. The tracked 25-word `func_150D32FC` event-key
   forwarder, including two trailing layout words, is also byte-exact directly
   from C. The tracked 26-word `func_150DEC28` paired table dispatcher,
   including three trailing layout words, is byte-exact directly from C using
   its original K&R byte-parameter ABI. The 24-word `func_150F4CFC` two-event
   state/teardown handler is byte-exact directly from C using a typed embedded
   state record. The tracked 29-word `func_151002BC` linked-record validator,
   including three trailing layout words, is byte-exact from recovered C plus
   seven guarded scheduling words. The 25-word `func_15125490` water-distance
   classifier is byte-exact from typed recovered C plus a guarded replacement
   of its oversized 26-word IDO body. The 23-word `func_1514EE70` object-request
   wrapper is byte-exact directly from C with no guarded words after restoring
   its callback ABI and typed eight-byte stack request. The 25-word
   `func_1514F130` state-toggle event callback is also byte-exact directly from
   typed C with no guarded words. The 24-word `func_1517F7B4` timer/phase
   updater is byte-exact from recovered C plus five guarded timer-base register
   words. The 25-word `func_151A0950` linked-record event callback is byte-exact
   directly from C with no guarded words. The 24-word `func_151A9060` indexed
   callback dispatcher is also byte-exact directly from C after recovering its
   two-argument callback ABI. The 23-word `func_151C2E94` extended record
   validity predicate is byte-exact directly from C with no guarded words. The
   34-word `func_151DADA0` phase/scale updater is byte-exact from typed embedded
   state C plus four guarded phase-register words. The 24-word Init
   `func_1000B294` owner-reference repair is byte-exact from recovered C, an
   object no-unroll profile, and two relocation-aware scheduling swaps; the
   adjacent `func_1000B548` remains exact after expressing its four-record
   unroll directly in C. The 23-word `func_150233E4` three-slot resource
   cleanup loop is byte-exact from typed C plus two relocation-aware setup
   scheduling swaps. The 24-word `func_1503B95C` indexed flag predicate is
   byte-exact directly from C with no guarded words. The 24-word
   `func_1503DA3C` bounded record-byte lookup is also byte-exact directly from
   C with no guarded words. The 24-word `func_1503F904` actor-position query
   wrapper is byte-exact directly from typed C with no guarded words. The
   24-word `func_15044D40` signed-coordinate event wrapper is also byte-exact
   directly from typed C with no guarded words. The 26-word `func_1507488C`
   packed event-mask updater is byte-exact through guarded register scheduling.
   A full rebuild also exposed and repaired the stale overflow trampoline for
   19-word `func_1506EE60`. The 24-word `func_1507EE58` complementary history
   marker wrapper is byte-exact directly from typed C with no guarded words.
   The 24-word `func_1508434C` counted object-dispatch loop and 24-word
   `func_150B58F0` tagged table-value serializer and 24-word `func_150C1660`
   typed effect-spawn wrapper are also byte-exact directly from typed C with no
   guarded words. The 24-word `func_150DF8C0` mapped record-active predicate is
   likewise exact directly from typed C. The 24-word `func_150F1CB0` actor-state
   byte selector is also exact directly from C. The 24-word `func_150F52B0`
   script-gated high-flag wrapper is likewise exact directly from C. The
   24-word `func_150FB188` actor parameter initializer is byte-exact from typed
   C plus seventeen guarded scheduling, FP-register, and relocation words.
   The 26-word `func_1510281C` and 29-word `func_151028AC` paired object-
   eligibility predicates are byte-exact directly from typed C with no guarded
   words. The 28-word `func_1510FE30` relative hierarchy-index lookup is also
   byte-exact directly from C. The 24-word `func_1513164C` nine-argument dual
   dispatcher and 24-word `func_15133760` typed eight-float forwarding wrapper
   are likewise exact directly from C. The 34-word `func_15142FBC` cache-aware
   render-mode wrapper is exact from structured C plus three guarded scheduling
   words. The 24-word `func_15143DA8` integer range clamp is exact from
   structured C plus nine guarded register-allocation words. The 29-word
   `func_151640C0` category-`0x29` identity filter is likewise exact from
   structured C plus nine guarded register-allocation words. The 27-word
   `func_1515F040` scaled signed fixed-point clamp is exact from typed C plus
   three guarded scheduling/omission entries. The 25-word `func_15166204`
   lifetime updater and expiry path is exact from C without guarded word
   patches. The 24-word `func_1517EA4C` display-list state helper is exact
   directly from three standard RDP macros. The 28-word `func_1518E298`
   linked-position callback is exact directly from C with its explicit
   four-argument callback ABI. The 24-word `func_1519ED24` scaled transform
   copy is exact from typed C plus five guarded setup-scheduling words. The
   27-word `func_1519EF04` fixed-scale transform copy is exact directly from
   typed C. The 28-word `func_151AE640` mode-driven slot updater is exact from
   structured C plus four guarded return-scheduling and branch words. The
   24-word `func_151D5E30` four-handle cleanup loop is exact from typed C plus
   three guarded null-test scheduling words. The 25-word `func_15023440`
   resource-entry reset is exact directly from structured C. The 25-word
   `func_1502DB20` resource-size selector is exact directly from a switch;
   generated-slice rodata relocation retargeting preserves its original
   64-entry jump table. The 26-word `func_1502EE8C` record-byte classifier is
   exact from typed C plus six guarded control-flow words. The 25-word Game
   `func_1503F108` indexed state initializer is exact directly from typed C.
   The 27-word Game `func_15049260` aggregate forwarding wrapper is exact
   directly from typed C. The 25-word Game `func_1507A100` packed path-record
   writer is exact from typed C plus six guarded register words. The subsequent
   ordinary queue through `func_1518804C` is also exact. The 25-word
   `func_1519F48C` linked-record retirement is exact from semantic C plus four
   guarded shared-base words. The 29-word `func_151A931C` identity-gated event
   flag update is exact from typed C plus four guarded early-return words; its
   corrected prototype also removes all 13 guards from exact caller
   `func_151A9024`. The 28-word `func_151928B0` type-result selector is exact
   from structured C plus four guarded shared-epilogue words, with its original
   five-entry jump table retained. The 25-word `func_150ADA68` floating PRNG
   step is restored to original handwritten assembly ownership after its
   equivalent C was confirmed to compile as a 26-word overflow trampoline.
   The 65-word `func_1514563C` line-projection helper is exact after restoring
   retail's dot-product operand order and guarding 18 independent frame and
   output-register choices. The 28-word `func_151B3040` paired embedded-record
   dispatch is exact directly from C with no guard rows. The 25-word
   `func_151C9ED4` four-handler event broadcast is exact from recovered C plus
   four guarded frame/local-slot words. The 26-word `func_151D13E0` owned-state
   teardown is exact directly from C with no guard rows. The 25-word
   `func_151E4E00` state-transition dispatch is exact directly from C with no
   guard rows. The 26-word `func_151E7EF8` code-integrity checksum is also
   exact directly from recovered C with no guard rows. The 163-word
   `func_151E7F60` object-slot spawn/setup routine is exact from semantic C
   plus 24 guarded stack-frame and local-slot words. The 41-word
   `func_151E8214` timed mode transition is exact directly from C with no
   guard rows. The adjacent 76-word `func_151E82B8` marker-table cursor is
   exact from semantic C plus one guarded commuted equality-branch word. The
   adjacent 50-word `func_151E83E8` timed event transition is exact directly
   from C with no guard rows. The adjacent 92-word `func_151E84B0` mode
   callback and indexed-resource setup is exact from semantic C plus two
   guarded frame-size words. The adjacent 49-word `func_151E8620` display-list
   overflow guard is exact from semantic C plus 14 guarded register-lifetime
   and scheduling words. The adjacent 175-word `func_151E86E4` scaled,
   scissored texture-rectangle writer is exact from the existing graphics
   macro plus four guarded vertical-scale register words. The adjacent
   819-word Game `func_151E89A0` HUD/status renderer is now reconstructed from
   its zero-return placeholder as semantic C, uses retail's `0x158` frame, and
   fits its original 3,276-byte slot. It remains non-matching at 803 real word
   differences, so continue its register-lifetime and scheduling pass from
   [Working Note 364](WORKING_NOTES/364-game-hud-status-renderer-reconstruction-20260928.md).
   Its adjacent 427-word `func_151E966C` player-status row renderer is
   byte-exact across retail's `0x6AC` code extent and `0x100` frame. Recovered
   SDK graphics macros and corrected scalar/cursor lifetimes reduce the
   semantic C body from 415 to 116 persistent compiler-only differences;
   relocation-aware expected-word guards normalize those stack-slot,
   register-allocation and scheduling words. See
   [Working Note 368](WORKING_NOTES/368-game-player-status-row-renderer-byte-match-20260928.md).
   The next 273-word `func_151E9D18` team-counter panel is byte-exact with
   retail's `0x444` code extent and `0xA0` frame. Recovered SDK graphics
   macros, corrected scalar types and local layout emit 271 words directly;
   two expected-word guards normalize one independent load/add schedule. See
   [Working Note 367](WORKING_NOTES/367-game-team-counter-panel-byte-match-20260928.md).
   The 20-word Init `func_10001000` entrypoint is restored from its false
   zero-return C placeholder to the original handwritten clear-and-jump
   assembly. Its 14 instruction words plus six retail padding words match
   directly with no guards. See
   [Working Note 369](WORKING_NOTES/369-init-handwritten-entrypoint-restoration-20260928.md).
   The 24-word Init `osMapTLBRdb` routine is also restored from an empty C
   placeholder to its original handwritten CP0/TLB assembly. Its 22
   instruction words plus two retail padding words match directly with no
   guards. See
   [Working Note 370](WORKING_NOTES/370-init-handwritten-maptlbrdb-restoration-20260928.md).
   The 20-word compiler-generated `__osSetHWIntrRoutine` now matches through
   its recovered libultra body and retail `-O1` object profile. The linked
   function span matches directly with no guards. See
   [Working Note 371](WORKING_NOTES/371-init-hardware-interrupt-routine-match-20260928.md).
   The 25-word `func_1000CBF0` channel-parameter updater is now byte-exact
   after restoring its 32-bit argument types and original repeated table
   accesses. See
   [Working Note 372](WORKING_NOTES/372-init-channel-parameter-updater-match-20260928.md).
   The 28-word Game `func_15004CE0` display-list address relocator is also
   byte-exact after recovering signed opcodes, the indexed cursor, and the
   opening opcode double-read. Ten guarded words normalize only compiler
   register allocation and a commutative add; see
   [Working Note 373](WORKING_NOTES/373-game-display-list-address-relocator-match-20260928.md).
   The 28-word Game `func_15033F70` object-state filter is byte-exact after
   recovering the global disable gate, attached-object type exclusions, and
   state-byte clear. All 28 words emit directly from C with no guards; see
   [Working Note 374](WORKING_NOTES/374-game-object-state-filter-match-20260928.md).
   The ordinary Game queue through 26-word `func_15157F80` is now byte-exact.
   It appends the fixed and indexed matrix commands, advances the display-list
   cursor twice, and sets the caller's ready byte. The recovered `gSPMatrix`
   form emits directly without guards; see
   [Working Note 387](WORKING_NOTES/387-game-display-list-matrix-pair-match-20260928.md).
   The following 26-word Game `func_15168B44` packed-counter update is also
   byte-exact. Its recovered typed state preserves retail's observable
   two-store packed-word update, timer refresh, and available-count path;
   twenty scoped guards close one IDO register-allocation and scheduling
   cycle without changing control flow or relocations. See
   [Working Note 388](WORKING_NOTES/388-game-packed-counter-state-match-20260928.md).
   The 26-word allocator-copy wrapper `func_15169900` and adjacent 26-word
   setup twins `func_1518E66C` and `func_1518E6D4` are now byte-exact from
   semantic C. Their recovered full-width ABI, typed record layout, allocator
   and setup calls, payload copy, and final state stores emit directly with no
   guards or compiler overrides; see
   [Working Note 389](WORKING_NOTES/389-game-allocator-copy-and-setup-pair-match-20260928.md).
   Adjacent object-ID state twins `func_151993E4` and `func_1519944C` are now
   byte-exact after recovering their six-entry identifier scan and clear/set
   writes into `D_800E0900`. Two scoped guards per function normalize only
   the retained object-ID register; see
   [Working Note 390](WORKING_NOTES/390-game-object-id-state-pair-match-20260928.md).
   The second clear/set pair `func_1519BEB8` and `func_1519BF20` is also
   byte-exact from the same six-ID semantic scan. Two scoped object-ID
   register-lifetime guards per routine close the only compiler differences;
   see
   [Working Note 391](WORKING_NOTES/391-game-second-object-id-state-pair-match-20260928.md).
   The following 26-word Game actor-target transform `func_151A4E34` is now
   byte-exact after recovering its null-target gate, actor type-nibble gate,
   64-byte target indexing, and transform-helper call. One scoped guard
   preserves only retail's commutative address-add operand order; see
   [Working Note 392](WORKING_NOTES/392-game-actor-target-transform-match-20260928.md).
   The 29-word Game timed-record lifecycle `func_1519EA04` is now byte-exact
   after recovering its enabled timer decrement, optional owner-field clear,
   and record deletion. It emits directly from semantic C with no guards; see
   [Working Note 393](WORKING_NOTES/393-game-timed-record-lifecycle-match-20260928.md).
   The 124-word Game entrypoint `func_15007830` is now byte-exact after
   recovering its startup sequence, five-entry state dispatch, signed
   halfword parameters, shared cleanup, and permanent main loop. Sixty-six
   scoped guards normalize one closed saved-register allocation cycle and two
   omitted unreachable epilogue words; see
   [Working Note 394](WORKING_NOTES/394-game-entrypoint-main-loop-match-20260928.md).
   The 30-word packed-coordinate callback `func_1518CCA8` is now byte-exact
   after recovering its packed X/Y offset update, zero-Z gate, and low-nibble
   callback dispatch. Ten scoped guards normalize one closed temporary-
   register allocation cycle; see
   [Working Note 395](WORKING_NOTES/395-game-packed-coordinate-callback-match-20260928.md).
   The 27-word 64-bit flag setter `func_1501D258` is now byte-exact after
   recovering its global enable gate and indexed bitset update. The complete
   routine emits directly from typed semantic C with no guards; see
   [Working Note 396](WORKING_NOTES/396-game-indexed-64-bit-flag-setter-match-20260928.md).
   The 26-word per-entry cleanup loop `func_15022754` is now byte-exact after
   recovering its indexed count pointer and dynamic post-call bound reload.
   It also emits directly from semantic C with no guards; see
   [Working Note 397](WORKING_NOTES/397-game-per-entry-cleanup-loop-match-20260928.md).
   The 33-word linked-list match dispatcher `func_150303E4` is now byte-exact
   after recovering its explicit zero-key return and pre-call next-pointer
   lifetime. It emits directly from semantic C with no guards; see
   [Working Note 398](WORKING_NOTES/398-game-linked-list-match-dispatcher-match-20260928.md).
   The 27-word current-record vector copier `func_1503A60C` is now byte-exact
   after recovering its destination pointer and three alias-sensitive source
   lookups. It emits directly from semantic C with no guards; see
   [Working Note 399](WORKING_NOTES/399-game-current-record-vector-copy-match-20260928.md).
   The 28-word five-bucket byte canonicalizer `func_1503D5F0` is now
   byte-exact after recovering its directly indexed nested-loop source and
   retail no-unroll compiler profile. No guards are required; see
   [Working Note 400](WORKING_NOTES/400-game-five-bucket-byte-canonicalizer-match-20260928.md).
   The 27-word two-word bit test `func_1503E1F4` is now byte-exact after
   recovering its low/high flag-word selection and shared zero-return tail.
   MIPS variable-shift masking supplies the high-word bit index. No guards are
   required; see
   [Working Note 401](WORKING_NOTES/401-game-two-word-bit-test-match-20260928.md).
   The 28-word owner status-byte clear `func_150806A8` is now byte-exact after
   recovering its two guarded byte clears and alias-sensitive owner-pointer
   reload. No guards are required; see
   [Working Note 402](WORKING_NOTES/402-game-owner-status-byte-clear-match-20260928.md).
   The 28-word seven-group byte canonicalizer `func_15084D00` is now
   byte-exact after recovering its table search and widening the cached input
   byte to reproduce retail's register allocation. No guards are required; see
   [Working Note 403](WORKING_NOTES/403-game-seven-group-byte-canonicalizer-match-20260928.md).
   The 27-word resolved-object dispatch wrapper `func_1509F5F4` is now
   byte-exact after recovering its optional validation and narrowed forwarding
   call. No guards are required; see
   [Working Note 404](WORKING_NOTES/404-game-resolved-object-dispatch-wrapper-match-20260928.md).
   The 27-word packed-record activation routine `func_150A0264` is now
   byte-exact after recovering its active/secondary flag updates, alias-safe
   source-value load, destination clear, and packed-field replacement. Twelve
   stale-checked guards normalize only a closed temporary-register allocation
   cycle; see
   [Working Note 405](WORKING_NOTES/405-game-packed-record-activation-match-20260928.md).
   The 27-word indexed coordinate setter `func_150A3444` is now byte-exact
   after recovering its signed 16-bit inputs and three direct stores into a
   52-byte record. Its alias-sensitive global-pointer reloads emit directly
   from C with no guards; see
   [Working Note 406](WORKING_NOTES/406-game-indexed-coordinate-setter-match-20260928.md).
   The 30-word staged halfword ramp `func_150B71A8` is now byte-exact after
   recovering its first-field priority, frame-scaled increments, and `0x1000`
   clamps. The complete branch-likely and early-return shape emits directly
   from C with no guards; see
   [Working Note 407](WORKING_NOTES/407-game-staged-halfword-ramp-match-20260928.md).
   The 29-word event-linked object removal filter `func_150BE150` is now
   byte-exact after recovering its event-byte narrowing, direct payload match,
   and event-zero linked-pointer match. An explicit payload local recovers the
   final retail load schedule; no guards are required. See
   [Working Note 408](WORKING_NOTES/408-game-event-linked-object-removal-match-20260928.md).
   The 27-word two-event command dispatcher `func_150C19C0` is now byte-exact
   after recovering its event-to-command mapping, owner lookup, and always-one
   return. A two-case switch emits the retail forward-branch layout directly
   from C with no guards; see
   [Working Note 409](WORKING_NOTES/409-game-two-event-command-dispatch-match-20260928.md).
   The 28-word global-gated parameter dispatcher `func_150C7870` is now
   byte-exact after recovering its two global flag tests and alternate numeric
   argument sets. The recovered `f32` callee prototype restores the retail
   register-only call convention; no guards are required. See
   [Working Note 410](WORKING_NOTES/410-game-global-gated-parameter-dispatch-match-20260928.md).
   The 27-word single-byte allocation payload wrapper `func_150D0134` is now
   byte-exact after recovering its narrow formal arguments, pointer-returning
   allocator signature, and eight-byte local payload buffer. All words emit
   directly from C with no guards; see
   [Working Note 411](WORKING_NOTES/411-game-single-byte-allocation-payload-match-20260928.md).
   The adjacent 27-word float event-payload wrapper `func_150E8854` is now
   byte-exact after recovering its event-allocation arguments, `10.0f`
   payload, successful-allocation gate, and four-byte payload copy. Semantic C
   emits 25 of 27 words directly; two expected-word guards preserve retail's
   lower local stack slot. See
   [Working Note 412](WORKING_NOTES/412-game-float-event-payload-match-20260928.md).
   The adjacent 28-word float timer reset `func_150E88C0` is now byte-exact
   after recovering its frame-delta subtraction, negative-timer random reseed,
   and follow-up event call. All words emit directly from semantic C with no
   guards; see
   [Working Note 413](WORKING_NOTES/413-game-float-timer-reset-match-20260928.md).
   The 29-word record selector-bit test `func_15114050` is now byte-exact after
   recovering its active-record gate, selector `-1` shortcut, `0xA0`-stride
   record index, and per-selector mask lookup. All words emit directly from
   semantic C with no guards; see
   [Working Note 414](WORKING_NOTES/414-game-record-selector-bit-test-match-20260928.md).
   The 27-word packed-resource lazy initializer `func_15116110` is now
   byte-exact after recovering its empty-handle gate, packed selector and byte
   extraction, seven-argument resource lookup, returned-handle store, and
   packed-word clear. Semantic C emits 20 words directly; seven guards
   preserve one closed independent mask/register scheduling cycle. See
   [Working Note 415](WORKING_NOTES/415-game-packed-resource-lazy-init-match-20260928.md).
   The 27-word partial-zero payload allocator `func_1514DA38` is now
   byte-exact after recovering its 28-byte local record, intentionally
   untouched payload word, allocation, copy, and type-`0x13` dispatch. Local
   declaration order reproduces retail's stack map; all words emit directly
   from semantic C with no guards. See
   [Working Note 416](WORKING_NOTES/416-game-partial-zero-payload-allocation-match-20260928.md).
   The 34-word three-coordinate equality classifier `func_15159230` is now
   byte-exact after recovering its unsigned mode argument, exact float
   comparisons, zero result for a full coordinate match, and mode-selected
   mismatch results. Semantic C emits 22 words directly; eleven guarded tail
   words preserve retail's ordinary branches and shared return instead of
   IDO's equivalent branch-likely folding, and normal slice padding retains
   the final `nop`. See
   [Working Note 417](WORKING_NOTES/417-game-coordinate-equality-classifier-match-20260928.md).
   The 27-word resource-install callback `func_15166F6C` is now byte-exact
   after recovering its four-argument callback ABI, global resource-pointer
   install, and nine-argument setup dispatch. Forwarding the installed global
   reproduces retail's retained destination address and complete call schedule;
   all words emit directly from semantic C with no guards. See
   [Working Note 418](WORKING_NOTES/418-game-resource-install-callback-match-20260928.md).
   The 28-word record-mediated dispatch `func_15173C90` is now byte-exact
   after recovering its narrowed record lookup, null gate, high-bit-cleared
   flags, table index, and five-argument dispatch. Semantic C emits 26 words
   directly; two expected-word guards preserve retail's ordering of two
   independent call-argument staging instructions. See
   [Working Note 419](WORKING_NOTES/419-game-record-mediated-dispatch-match-20260928.md).
   The 28-word owned cleanup-list teardown `func_15178DA4` is now byte-exact
   after recovering its resource stop, deletion-safe list walk, owner match,
   and final record teardown. Function-scope declaration order preserves the
   saved next-node cursor and retail stack slot; all words emit directly from
   semantic C with no guards. See
   [Working Note 420](WORKING_NOTES/420-game-owned-cleanup-list-teardown-match-20260928.md).
   The 27-word mapped three-byte-row dispatcher `func_1517F3A0` is now
   byte-exact after recovering its selector mapping, zero-map passthrough,
   packed row lookup, and six-argument dispatch. The early-return source shape
   reproduces retail's shared epilogue; all words emit directly from semantic
   C with no guards. See
   [Working Note 421](WORKING_NOTES/421-game-mapped-three-byte-row-dispatch-match-20260928.md).
   The 27-word event callback-table dispatcher `func_15190550` is now
   byte-exact after recovering its event-`0x2A` pre-handler, object callback
   index, nullable lookup, and three-argument forwarding call. Its typed body
   emits all words directly with no guards. See
   [Working Note 422](WORKING_NOTES/422-game-event-callback-table-dispatch-match-20260928.md).
   The 28-word four-pointer cleanup `func_151B222C` is now byte-exact after
   recovering its three-entry indexed release loop and final independent
   pointer release. An `s32` counter explicitly narrowed after each increment
   reproduces retail's saved-register loop; all words emit directly from C
   with no guards. See
   [Working Note 423](WORKING_NOTES/423-game-four-pointer-cleanup-match-20260928.md).
   The 29-word dual-layout owner release `func_151CB49C` is now byte-exact
   after recovering its event-`0x21` direct-owner comparison and event-zero
   nested-owner comparison. An explicit referenced-object local reproduces
   retail's register allocation; all words emit directly with no guards. See
   [Working Note 424](WORKING_NOTES/424-game-dual-layout-owner-release-match-20260928.md).
   The 28-word signed record-command writer `func_15034340` is now byte-exact
   after recovering its `0x32C`-byte record indexing, signed control-byte
   gate, command-6 output, and signed value scaling by 200. The deliberate
   second control-byte read and cursor update reproduce retail directly; all
   words emit from semantic C with no guards. See
   [Working Note 425](WORKING_NOTES/425-game-signed-record-command-writer-match-20260928.md).
   The 30-word gated active-object scan `func_150347E8` is now byte-exact
   after recovering its global disable gate, fixed `0x32C`-byte record walk,
   two active-pointer checks, and per-record dispatch to `func_15034728`.
   Scoping the end pointer inside the gate reproduces retail's opening address
   schedule; all words emit directly with no guards. See
   [Working Note 426](WORKING_NOTES/426-game-gated-active-object-scan-match-20260928.md).
   The 27-word signed XZ coordinate-query wrapper `func_15045714` is now
   byte-exact after recovering its query-mode selection, float truncation,
   signed-16 coordinate narrowing, selector forwarding, and output store.
   Twenty-four words emit directly from semantic C; three expected-word
   guards normalize one closed position-pointer register cycle. See
   [Working Note 427](WORKING_NOTES/427-game-signed-xz-coordinate-query-match-20260928.md).
   The 30-word quaternion hemisphere normalizer `func_15049C40` is now
   byte-exact after recovering its four-component dot product and in-place
   negation of the second quaternion when that dot product is negative. All
   30 words emit directly from semantic C with no guards. See
   [Working Note 428](WORKING_NOTES/428-game-quaternion-hemisphere-normalizer-match-20260928.md).
   The 38-word floor-threshold state trigger `func_1506D6B4` is now byte-exact
   after recovering its two early exits, health-dependent state selection,
   packed global update, and callback. Thirty-two words emit directly from
   semantic C; six guards normalize one commutative FP operand order and one
   closed integer temporary cycle. See
   [Working Note 429](WORKING_NOTES/429-game-floor-threshold-state-trigger-match-20260928.md).
   The 28-word indexed halfword-sequence dispatcher `func_15080784` is now
   byte-exact after recovering its nullable sequence gate, byte-index end
   check, optional nonzero halfword submission, and index advance. All 28
   words emit directly from semantic C with no guards. See
   [Working Note 430](WORKING_NOTES/430-game-indexed-halfword-sequence-dispatch-match-20260928.md).
   The 28-word `func_150B1DB0` is restored from its false zero-return C
   placeholder to original handwritten assembly ownership. Its two-block
   64-bit mask/rotate transform, trapping pointer increments, and complete
   linked span match retail. See
   [Working Note 431](WORKING_NOTES/431-game-handwritten-two-block-word-transform-restoration-20260928.md).
   The 35-word callback-gated record-state updater `func_150D0034` is now
   byte-exact after recovering the volatile signed callback selector and the
   promoted `~1` status-byte mask. All words emit directly from semantic C
   with no guards. See
   [Working Note 432](WORKING_NOTES/432-game-callback-gated-record-state-update-match-20260928.md).
   The 30-word allocation payload wrapper `func_150D02B4` is now byte-exact
   after recovering its signed-halfword parameter and 12-byte local record
   whose initialized eight-byte prefix is copied. All words emit directly
   from semantic C with no guards. See
   [Working Note 433](WORKING_NOTES/433-game-eight-byte-allocation-payload-match-20260928.md).
   The 28-word subtype-2 allocation payload wrapper `func_150D04C4` is now
   byte-exact after recovering its signed-halfword parameter and eight-byte
   local buffer. All words emit directly from semantic C with no guards. See
   [Working Note 434](WORKING_NOTES/434-game-single-byte-subtype2-payload-match-20260929.md).
   The 28-word damped motion-state integrator `func_150D13A0` is now
   byte-exact after recovering its five floating-field updates, three scale
   constants, and final state-refresh call. All words emit directly from
   semantic C with no guards. See
   [Working Note 435](WORKING_NOTES/435-game-damped-motion-state-integrator-match-20260929.md).
   The 29-word validated payload dispatcher `func_150ECB8C` is now byte-exact
   after recovering its target-state and selector gates, shared failure
   invalidation, and six-byte payload dispatch. All words emit directly from
   semantic C with no guards. See
   [Working Note 436](WORKING_NOTES/436-game-validated-payload-dispatch-match-20260929.md).
   The 28-word fixed payload-setup wrapper `func_150ECC00` is now byte-exact
   after recovering its two calls, fixed argument tuple, and volatile selector
   byte. All words emit directly from semantic C with no guards. See
   [Working Note 437](WORKING_NOTES/437-game-fixed-payload-setup-wrapper-match-20260929.md).
   The 28-word two-slot resource cleanup `func_150F739C` is now byte-exact
   after recovering its indexed release loop and final owner cleanup call.
   Twenty-three words emit directly from semantic C; five guards normalize
   one redundant temporary and a closed counter-register cycle. See
   [Working Note 438](WORKING_NOTES/438-game-two-slot-resource-cleanup-match-20260929.md).
   The 28-word actor-indexed spatial-effect wrapper `func_150FFB6C` is now
   byte-exact after recovering its position forwarding, actor index and
   halfword derivation, flag merge, and final effect call. All words emit
   directly from semantic C with no guards. See
   [Working Note 439](WORKING_NOTES/439-game-actor-indexed-spatial-effect-wrapper-match-20260929.md).
   The 30-word mode-gated table-value updater `func_15108BC0` is now
   byte-exact after recovering its owner-relative record lookup, sentinel
   handling, mode-byte gate, and `0x44`-byte table indexing. Nineteen words
   emit directly from semantic C; eleven guarded normalizations preserve the
   independent table-address/register schedule and explicit return-delay
   `nop`. See
   [Working Note 440](WORKING_NOTES/440-game-mode-gated-table-value-match-20260929.md).
   The 30-word two-command record updater `func_15109064` is now byte-exact
   after recovering its command `0x1D` payload copy and command `0x1E` state
   toggle. Twenty-six words emit directly from semantic C; four guarded
   normalizations preserve one commutative add and the explicit copy-path
   return schedule. See
   [Working Note 441](WORKING_NOTES/441-game-two-command-record-update-match-20260929.md).
   The 28-word record-ID lookup `func_151149AC` is now byte-exact after
   recovering its reserved-zero handling and bounded scan of `0xA0`-byte
   records for a matching ID at offset `0x72`. All words and four relocations
   emit directly from semantic C with no guards. See
   [Working Note 442](WORKING_NOTES/442-game-record-id-lookup-match-20260929.md).
   The 29-word multiplayer-slot reset `func_151298C0` is now byte-exact after
   recovering its multiplayer-mode gate and three indexed writes to the
   `0x24`-byte slot table. All words and six relocations emit directly from
   semantic C with no guards. See
   [Working Note 443](WORKING_NOTES/443-game-multiplayer-slot-reset-match-20260929.md).
   The 28-word per-slot mode initializer `func_15181D00` is now byte-exact
   after recovering its zero and active-mode state paths across four parallel
   tables. All words and twelve relocations emit directly from semantic C
   with no guards. See
   [Working Note 444](WORKING_NOTES/444-game-per-slot-mode-initializer-match-20260929.md).
   The 28-word command `0x1E` record builder `func_1518AB60` is now byte-exact
   after recovering its allocator call, null return, owner and selector
   fields, and two cleared words. Twenty-six words emit from semantic C; two
   guarded words preserve retail's selector reload/store register allocation.
   See
   [Working Note 445](WORKING_NOTES/445-game-command-1e-record-builder-match-20260929.md).
   The 28-word position-descriptor dispatch wrapper `func_151C9AC0` is now
   byte-exact after recovering its raised owner position, generated descriptor,
   and five-argument dispatch. All words and both call relocations emit
   directly from semantic C with no guards. See
   [Working Note 446](WORKING_NOTES/446-game-position-descriptor-dispatch-match-20260929.md).
   The 30-word child-pointer release loop `func_151BFB2C` is now byte-exact
   after recovering its primary pointer release and two-entry child array.
   A byte-canonicalizing loop assignment and source-ordered address expression
   reproduce retail's counter feedback and commutative add without guards. See
   [Working Note 447](WORKING_NOTES/447-game-child-pointer-release-loop-match-20260929.md).
   The 30-word selector-transition dispatcher `func_151AE06C` is now
   byte-exact after recovering its admission query, requested/current selector
   comparison, and conditional replacement path. One guarded word preserves
   a commutative equality-branch operand order. See
   [Working Note 448](WORKING_NOTES/448-game-selector-transition-dispatch-match-20260929.md).
   The 32-word timer and position updater `func_15174920` is now byte-exact
   after recovering its capped timer subtraction, expiry clear, and two signed
   position accumulators. All tracked words and both global relocations emit
   directly from semantic C with no guards. See
   [Working Note 449](WORKING_NOTES/449-game-timer-position-update-match-20260929.md).
   The 61-word projection clamp `func_15145548` is now byte-exact after
   expressing both fallback vector copies as whole-structure assignments.
   This restores retail's raw three-word copy schedule and the floating-point
   temporary allocation used by the upper clamp. All words and the helper-call
   relocation match directly from semantic C with no guards. See
   [Working Note 450](WORKING_NOTES/450-game-projection-clamp-match-20260929.md).
   The 29-word forwarding wrapper `func_1503F5B8` is now byte-exact after
   recovering its six-argument signature and typed twelve-argument call to
   `func_1505E0C4`. The complete frame, argument schedule, object-byte load,
   call relocation, and return emit directly from C with no guards. See
   [Working Note 451](WORKING_NOTES/451-game-multi-argument-forwarder-match-20260929.md).
   The 28-word active-object state updater `func_1507C370` is now byte-exact
   after recovering its bounded `D_800CC2D0` traversal and three-halfword
   pointer dispatch to `func_1507C3E0`. All words, seven relocations, and the
   loop delay-slot update emit directly from C with no guards. See
   [Working Note 452](WORKING_NOTES/452-game-active-object-state-update-match-20260929.md).
   The 29-word packed descriptor builder `func_15095060` is now byte-exact
   after recovering its optional descriptor publication, direct-or-indexed
   source selection, and packed halfword/byte copies into `D_800D2C90`.
   Relocation-aware expected-word guards normalize IDO's repeated global-base
   materialization, table-index schedule, and temporary-register lifetimes.
   See [Working Note 453](WORKING_NOTES/453-game-packed-descriptor-builder-match-20260929.md).
   The 28-word three-record dispatch loop `func_15096D08` is now byte-exact
   after recovering its mode gate, nonempty-record test, and early exit on a
   nonzero `func_15096A68` result. Its complete frame, saved-register
   lifetimes, branch-likely update, call relocation, and epilogue emit directly
   from semantic C without guards. See
   [Working Note 454](WORKING_NOTES/454-game-three-record-dispatch-loop-match-20260929.md).
   The 32-word type-gated random remainder writer `func_15084C30` is now
   byte-exact from typed C plus 14 guarded register-allocation words. See
   [Working Note 455](WORKING_NOTES/455-game-random-remainder-writer-match-20260929.md).
   The 29-word coordinate-event wrapper twins `func_150B3E74` and
   `func_150B3EE8` are now byte-exact directly from C. Each truncates the
   object's three position floats to signed halfwords, dispatches event
   `0x221` with duration `0xFA0`, and invokes its distinct final callback.
   See [Working Note 456](WORKING_NOTES/456-game-coordinate-event-wrapper-twins-match-20260929.md).
   The 28-word actor-slot creation adapter `func_150E32D0` is now byte-exact
   directly from C after recovering the 14-argument `func_150E3020` ABI, its
   zero/default fields, and the one-based result conversion. See
   [Working Note 457](WORKING_NOTES/457-game-actor-slot-creation-adapter-match-20260929.md).
   The 29-word type-`0x64` record allocator `func_15104170` is now byte-exact
   directly from C after recovering its `void` contract and complete record
   initialization. See
   [Working Note 458](WORKING_NOTES/458-game-type64-record-allocator-match-20260929.md).
   The 30-word auxiliary-record reset `func_1511A7C0` is now byte-exact
   directly from C, including its live-count float-array clearing loop and
   branch-likely base reload. See
   [Working Note 459](WORKING_NOTES/459-game-auxiliary-record-reset-match-20260929.md).
   The 29-word zero-payload record dispatcher `func_1514DAA4` is now
   byte-exact after recovering its object flag update, two-word zero payload,
   allocation, payload copy, and event-`0x13` dispatch. Two fail-closed guards
   preserve only the independent payload-size and retained-object spill
   schedule around the allocator call. See
   [Working Note 460](WORKING_NOTES/460-game-zero-payload-record-dispatch-match-20260929.md).
   The 17-word packed-byte submission wrapper `func_150721A4` is now
   byte-exact. Ordinary-object padding now honors guarded omission before its
   overflow decision, allowing three redundant IDO moves to be removed; nine
   guarded words preserve retail's equivalent register lifetimes and call
   schedule. See
   [Working Note 461](WORKING_NOTES/461-game-packed-byte-submission-wrapper-match-20260929.md).
   The 31-word accelerated-motion integrator `func_1515B994` is now
   byte-exact after recovering its timestep-based position and velocity
   updates plus the averaged-velocity secondary accumulation. Fourteen
   fail-closed guards preserve retail's equivalent floating-point register
   lifetimes and independent load/store schedule. See
   [Working Note 462](WORKING_NOTES/462-game-accelerated-motion-integrator-match-20260929.md).
   The 29-word object-record cleanup `func_1518E308` is now byte-exact
   directly from C. It clears two owner fields, releases live pointers from
   100 fixed-size records, and zeroes the complete record array. See
   [Working Note 463](WORKING_NOTES/463-game-object-record-cleanup-match-20260929.md).
   The 29-word oscillation/angle updater `func_151B8BE0` is now byte-exact
   from semantic C plus seven guarded floating-point temporary choices. See
   [Working Note 464](WORKING_NOTES/464-game-oscillation-angle-update-match-20260929.md).
   The 30-word type-selector state handler `func_15033440` is now byte-exact
   directly from C, including its shared selector path and branch-likely
   exits. See
   [Working Note 465](WORKING_NOTES/465-game-type-selector-state-handler-match-20260929.md).
   The 30-word owned float-array allocator `func_15036C70` is now byte-exact
   directly from C after retaining its initialization constant once across
   the repeated owner-pointer loads. See
   [Working Note 466](WORKING_NOTES/466-game-owned-float-array-allocator-match-20260929.md).
   The 30-word paired-mask predicate `func_1503EF4C` is now byte-exact from
   semantic C plus two commutative-operand guards, taking the Game matcher
   above 50%. See
   [Working Note 467](WORKING_NOTES/467-game-paired-mask-predicate-match-20260929.md).
   The 30-word classifier fallback wrapper `func_1504530C` is now byte-exact
   directly from C. Its unhandled switch path intentionally preserves the
   classifier's return value, matching retail. See
   [Working Note 468](WORKING_NOTES/468-game-classifier-fallback-wrapper-match-20260929.md).
   The 30-word descriptor-install wrapper `func_15094F70` is now byte-exact
   directly from C, including its ten-argument final dispatch. See
   [Working Note 469](WORKING_NOTES/469-game-descriptor-install-wrapper-match-20260929.md).
   The adjacent 30-word variable-tail descriptor wrapper `func_15094FE8` is
   also byte-exact directly from C. See
   [Working Note 470](WORKING_NOTES/470-game-variable-tail-descriptor-wrapper-match-20260929.md).
   The 30-word conditional record-dispatch wrapper `func_15095A90` is now
   byte-exact directly from C. See
   [Working Note 471](WORKING_NOTES/471-game-conditional-record-dispatch-wrapper-match-20260929.md).
   The 30-word descriptor float-forwarding adapter `func_150B9D14` is now
   byte-exact directly from C. See
   [Working Note 472](WORKING_NOTES/472-game-descriptor-float-forwarding-adapter-match-20260929.md).
   The 30-word normalized coordinate-output routine `func_1510B958` is now
   byte-exact from recovered C plus five guarded opening address/index words.
   See
   [Working Note 473](WORKING_NOTES/473-game-normalized-coordinate-output-match-20260929.md).
   The 21-word packed-mask setter `func_1507A4D4` is now byte-exact from its
   explicit mask local plus sixteen guarded packed-byte scheduling words. See
   [Working Note 474](WORKING_NOTES/474-game-packed-mask-setter-match-20260929.md).
   The 22-word event identity-release handler `func_150F1684` is now byte-exact
   from recovered C plus seven guarded identity-comparison register words. See
   [Working Note 475](WORKING_NOTES/475-game-event-identity-release-handler-match-20260929.md).
   The 26-word audio DMA prefetch wrapper `func_151F3D78` is now byte-exact
   directly from recovered C after restoring retail padding for its owning
   audio object. The clean full regeneration also cleared the stale address
   drift classification on unchanged Init routine `func_10012588`; every
   section now has zero drift rows. See
   [Working Note 476](WORKING_NOTES/476-game-audio-dma-prefetch-wrapper-match-20260929.md).
   The 31-word float-state scaler `func_151339D4` is now byte-exact directly
   from C after recovering its accumulated position field and six scaled
   float fields. See
   [Working Note 477](WORKING_NOTES/477-game-float-state-scaler-match-20260929.md).
   The 29-word angular state integrator `func_150AFBF4` is now byte-exact
   after recovering its timestep update, angle wrap, sine transform, and
   scalar output. See
   [Working Note 478](WORKING_NOTES/478-game-angular-state-integrator-match-20260929.md).
   The 30-word object type/status mapper `func_150B66DC` is now byte-exact
   directly from C after recovering its normalized three-way selector and
   target status-byte updates. See
   [Working Note 479](WORKING_NOTES/479-game-object-type-status-mapper-match-20260929.md).
   The 30-word parameter-block call adapter `func_15133510` is now byte-exact
   directly from C after recovering its three integer and eight float field
   arguments. See
   [Working Note 480](WORKING_NOTES/480-game-parameter-block-call-adapter-match-20260929.md).
   The 30-word list-node allocator wrapper `func_1514EBA4` is now byte-exact
   after recovering its allocator call, null return, and initialized payload,
   links, and signed key. Six guarded words preserve two independent retail
   scheduling cycles. See
   [Working Note 481](WORKING_NOTES/481-game-list-node-allocator-wrapper-match-20260929.md).
   Adjacent 20-word optional-callback teardown wrappers `func_151A8584` and
   `func_151A85D4` are now independently byte-exact after recovering their
   distinct callback tables and final calls. Symmetric guarded normalization
   preserves retail's path-sensitive object spill schedule. See
   [Working Note 482](WORKING_NOTES/482-game-optional-callback-teardown-pair-match-20260929.md).
   The 22-word packed indexed-byte updater `func_1506EF5C` is now byte-exact
   after recovering its sentinel/mode stores, packed selector, and two indexed
   byte writes through four repeated active-object reads. See
   [Working Note 483](WORKING_NOTES/483-game-packed-indexed-byte-updater-match-20260929.md).
   The 21-word two-owner linked-list lookup `func_15155FD4` is now byte-exact
   after recovering its two-owner scan and node-key comparison. Eight guarded
   words normalize one closed owner/end register-allocation cycle. See
   [Working Note 484](WORKING_NOTES/484-game-two-owner-linked-list-lookup-match-20260929.md).
   `func_10003BD0` is now byte-exact across its complete 28-word Init span.
   The tied Init cache-maintenance routines are now restored to original
   handwritten assembly ownership. Game object teardown `func_15106E78` is
   now byte-exact directly from semantic C. The 33-word command-row loop
   `func_150413FC` is also byte-exact from semantic C plus nine prologue-only
   scheduling guards. The 36-word state-flag updater `func_150F9A20` and
   35-word owner-event callback `func_15100230` are now byte-exact. The
   `func_1510E7A4`/`func_1510E82C`/`func_1510E8BC` render-parameter wrapper
   family is also byte-exact. The angular integrators `func_1511515C` and
   `func_151151FC`, plus displacement extender `func_15115EDC`, are now
   byte-exact. The 38-entry retail asset now establishes `func_15015F40`'s
   authoritative dispatch membership, and the function is byte-exact. Keep
   handwritten register-contract fragment `func_150A76F0` in the raw-assembly
   workstream.
   Keep `func_15194320` and `func_15194394` parked behind generated-slice
   jump-table/rodata ownership rather than introducing unresolved switches.
   Keep the documented lower-difference compiler cases parked. The tied Init
   cache rows remain in their SDK ownership lane.
   Keep the previously documented smaller special cases parked.
   Do not model control-register access through synthetic C or guarded
   retail-word replacement.
5. Treat raw-assembly conversion as a separate queue. Start by reviewing the
   smallest game-owned rows in `progress.csv`; exclude SDK, CP0, handwritten,
   and mixed code/data routines before converting anything.
6. After every source change, relink and rerun `match-progress`. Update public
   percentages only from a fresh linked scan.

The baseline and candidate list are in [Working Note 001](WORKING_NOTES/001-decomp-status-and-resume-boundary-20260924.md).
The completed pair and compiler-shape evidence are in
[Working Note 002](WORKING_NOTES/002-paired-event-swap-byte-match-20260924.md).
The completed debugger rectangle fill and guarded scheduling normalization are
in [Working Note 003](WORKING_NOTES/003-debugger-rectangle-fill-byte-match-20260924.md).
The completed context display and its guarded allocation normalization are in
[Working Note 007](WORKING_NOTES/007-debugger-context-display-byte-match-20260925.md).
The four completed game near-matches and generated-slice patch support are in
[Working Note 012](WORKING_NOTES/012-generated-near-match-normalization-20260925.md).
The final debugger inventory and handwritten-routine byte audit are in
[Working Note 013](WORKING_NOTES/013-debugger-completion-audit-20260925.md).
The two restored assembly boundaries are in
[Working Note 014](WORKING_NOTES/014-small-game-assembly-boundaries-20260925.md).
The two completed game record setters are in
[Working Note 015](WORKING_NOTES/015-game-record-pointer-byte-matches-20260925.md).
The completed two-field identifier check is in
[Working Note 016](WORKING_NOTES/016-game-identifier-check-byte-match-20260925.md).
The completed indexed counter update is in
[Working Note 017](WORKING_NOTES/017-game-indexed-counter-byte-match-20260925.md).
The completed packed-field writer is in
[Working Note 018](WORKING_NOTES/018-game-packed-field-writer-byte-match-20260925.md).
The completed two-difference game queue is in
[Working Note 019](WORKING_NOTES/019-final-two-difference-game-matches-20260925.md).
The restored original trigonometry slice is in
[Working Note 020](WORKING_NOTES/020-game-trigonometry-assembly-restoration-20260925.md).
The completed indexed-byte lookup is in
[Working Note 021](WORKING_NOTES/021-game-indexed-byte-lookup-match-20260925.md).
The completed nested-pointer update is in
[Working Note 022](WORKING_NOTES/022-game-nested-pointer-update-match-20260925.md).
The completed float-bound load reorder is in
[Working Note 023](WORKING_NOTES/023-game-float-bound-load-order-match-20260925.md).
The completed optional-callback cleanup is in
[Working Note 024](WORKING_NOTES/024-game-optional-callback-match-20260925.md).
The completed call-argument normalization and closed three-difference queue are
in [Working Note 025](WORKING_NOTES/025-game-call-argument-register-match-20260925.md).
The completed stack-local layout correction is in
[Working Note 026](WORKING_NOTES/026-game-stack-local-layout-match-20260925.md).
The completed global-base pointer lifetime is in
[Working Note 027](WORKING_NOTES/027-game-global-base-pointer-match-20260925.md).
The completed optional-pointer call lifetime is in
[Working Note 028](WORKING_NOTES/028-game-optional-pointer-call-match-20260925.md).
The restored synthetic-return trampoline is in
[Working Note 029](WORKING_NOTES/029-game-synthetic-return-trampoline-20260925.md).
The restored handwritten PRNG seed setter is in
[Working Note 030](WORKING_NOTES/030-game-prng-seed-setter-restoration-20260925.md).
The completed scalar-temporary normalization is in
[Working Note 031](WORKING_NOTES/031-game-scalar-temporary-match-20260925.md).
The completed set-bit temporary normalization is in
[Working Note 032](WORKING_NOTES/032-game-set-bit-temporary-match-20260925.md).
The completed opening-load scheduling normalization is in
[Working Note 033](WORKING_NOTES/033-game-opening-load-schedule-match-20260925.md).
The restored no-op callback assembly boundary is in
[Working Note 034](WORKING_NOTES/034-game-noop-callback-restoration-20260925.md).
The completed motion-scale register normalization is in
[Working Note 035](WORKING_NOTES/035-game-motion-scale-register-match-20260925.md).
The completed indexed-slot clear is in
[Working Note 036](WORKING_NOTES/036-game-indexed-slot-clear-match-20260925.md).
The completed call-ABI correction is in
[Working Note 037](WORKING_NOTES/037-game-forwarded-call-abi-match-20260925.md).
The completed table-stride expression recovery is in
[Working Note 038](WORKING_NOTES/038-game-table-stride-match-20260925.md).
The restored handwritten byte-fill loop is in
[Working Note 039](WORKING_NOTES/039-game-handwritten-byte-fill-restoration-20260925.md).
The completed packed fixed-point reader is in
[Working Note 040](WORKING_NOTES/040-game-packed-fixed-point-reader-match-20260925.md).
The completed packed-value scaling cluster is in
[Working Note 041](WORKING_NOTES/041-game-packed-value-scaling-cluster-20260925.md).
The completed viewport setup normalization is in
[Working Note 042](WORKING_NOTES/042-game-viewport-setup-frame-match-20260925.md).
The completed sound-command wrapper scheduling is in
[Working Note 043](WORKING_NOTES/043-game-sound-command-wrapper-match-20260925.md).
The restored dead-pointer-expression assembly boundary is in
[Working Note 044](WORKING_NOTES/044-game-dead-pointer-expression-restoration-20260925.md).
The completed destination-pointer scheduling is in
[Working Note 045](WORKING_NOTES/045-game-destination-pointer-schedule-match-20260925.md).
The completed countdown register normalization is in
[Working Note 046](WORKING_NOTES/046-game-countdown-register-match-20260925.md).
The completed retained-field wrapper is in
[Working Note 047](WORKING_NOTES/047-game-retained-field-wrapper-match-20260925.md).
The completed quadrant register normalization is in
[Working Note 048](WORKING_NOTES/048-game-quadrant-register-match-20260925.md).
The completed outer/child pointer normalization is in
[Working Note 049](WORKING_NOTES/049-game-outer-child-pointer-match-20260925.md).
The completed source/destination pointer pair is in
[Working Note 050](WORKING_NOTES/050-game-source-destination-pointer-pair-20260925.md).
The completed high-half call wrapper is in
[Working Note 051](WORKING_NOTES/051-game-high-half-call-wrapper-20260925.md).
The restored dead child-pointer assembly boundary is in
[Working Note 052](WORKING_NOTES/052-game-dead-child-pointer-restoration-20260925.md).
The restored structural twin is in
[Working Note 053](WORKING_NOTES/053-game-dead-child-pointer-twin-restoration-20260925.md).
The completed indexed-record flag update is in
[Working Note 054](WORKING_NOTES/054-game-indexed-record-flag-match-20260925.md).
The completed allocation-wrapper frame normalization is in
[Working Note 055](WORKING_NOTES/055-game-allocation-wrapper-frame-match-20260925.md).
The third restored dead child-pointer family member is in
[Working Note 056](WORKING_NOTES/056-game-dead-child-pointer-third-restoration-20260925.md).
The completed slot-cursor allocation is in
[Working Note 098](WORKING_NOTES/098-game-slot-cursor-allocation-match-20260926.md).
The completed chunked-boundary loop is in
[Working Note 099](WORKING_NOTES/099-game-chunked-boundary-loop-match-20260926.md).
The completed packed four-byte reader is in
[Working Note 100](WORKING_NOTES/100-game-packed-four-byte-reader-match-20260926.md).
The completed retained local-record pointer is in
[Working Note 101](WORKING_NOTES/101-game-retained-local-record-pointer-match-20260926.md).
The completed null-first table-populator path is in
[Working Note 102](WORKING_NOTES/102-game-null-first-table-populator-match-20260926.md).
The restored fourth-component trampoline continuation is in
[Working Note 103](WORKING_NOTES/103-game-fourth-component-continuation-restoration-20260926.md).
The completed record-pointer and repeated-field lifetime is in
[Working Note 104](WORKING_NOTES/104-game-record-pointer-repeated-field-match-20260926.md).
The completed two-component scaling loop is in
[Working Note 105](WORKING_NOTES/105-game-two-component-scaling-loop-match-20260926.md).
The completed embedded vertex-copy base lifetime is in
[Working Note 106](WORKING_NOTES/106-game-embedded-vertex-copy-match-20260926.md).
The completed angle-normalization register lifetime and opening schedule are
in [Working Note 107](WORKING_NOTES/107-game-angle-normalization-match-20260926.md).
The completed conditional callback dispatch is in
[Working Note 108](WORKING_NOTES/108-game-conditional-dispatch-match-20260926.md).
The completed four-slot release loop is in
[Working Note 218](WORKING_NOTES/218-game-four-slot-release-loop-match-20260926.md).
The completed existing-record/allocator wrapper is in
[Working Note 219](WORKING_NOTES/219-game-existing-record-wrapper-match-20260926.md).
The completed `+0x70` structural twin is in
[Working Note 220](WORKING_NOTES/220-game-existing-record-wrapper-twin-match-20260926.md).
The completed flag-gated optional-record update is in
[Working Note 221](WORKING_NOTES/221-game-flag-gated-record-update-match-20260926.md).
The completed stack-vector sum wrapper is in
[Working Note 222](WORKING_NOTES/222-game-stack-vector-sum-wrapper-match-20260927.md).
The completed state-transition wrapper is in
[Working Note 223](WORKING_NOTES/223-game-state-transition-wrapper-match-20260927.md).
The completed marker-record swap is in
[Working Note 226](WORKING_NOTES/226-game-marker-record-swap-match-20260927.md).
The restored handwritten four-timer decrement is in
[Working Note 227](WORKING_NOTES/227-game-four-timer-decrement-restoration-20260927.md).
The completed backing-buffer reset is in
[Working Note 228](WORKING_NOTES/228-game-backing-buffer-reset-match-20260927.md).
The restored handwritten vector cross product is in
[Working Note 229](WORKING_NOTES/229-game-vector-cross-product-restoration-20260927.md).
The completed flag-gated callback dispatcher is in
[Working Note 230](WORKING_NOTES/230-game-flag-gated-callback-dispatch-match-20260927.md).
The completed signed fixed-point clamp and guarded omission support are in
[Working Note 231](WORKING_NOTES/231-game-signed-fixed-point-clamp-match-20260927.md).
The completed three-entry callback-table loop is in
[Working Note 232](WORKING_NOTES/232-game-callback-table-loop-match-20260927.md).
The completed indexed-list unlink is in
[Working Note 233](WORKING_NOTES/233-game-indexed-list-unlink-match-20260927.md).
The completed backward active-object flag scan is in
[Working Note 234](WORKING_NOTES/234-game-active-object-flag-scan-match-20260927.md).
The completed state-to-animation selector is in
[Working Note 235](WORKING_NOTES/235-game-state-animation-selector-match-20260927.md).
The completed list-tail insertion and hidden no-op boundary are in
[Working Note 236](WORKING_NOTES/236-game-list-tail-insert-and-hidden-noop-match-20260927.md).
The completed bounded callback dispatcher is in
[Working Note 237](WORKING_NOTES/237-game-bounded-callback-dispatch-match-20260927.md).
The completed coordinate-transform wrapper is in
[Working Note 238](WORKING_NOTES/238-game-coordinate-transform-wrapper-match-20260927.md).
The completed stack-record pointer lifetime is in
[Working Note 109](WORKING_NOTES/109-game-stack-record-pointer-match-20260926.md).
The completed five-global reset ordering is in
[Working Note 110](WORKING_NOTES/110-game-global-reset-order-match-20260926.md).
The completed byte-gated optional call is in
[Working Note 111](WORKING_NOTES/111-game-byte-gated-call-match-20260926.md).
The completed record-value adjuster and its single commutative-multiply guard
are in
[Working Note 375](WORKING_NOTES/375-game-record-value-adjuster-match-20260928.md).
The completed sequence-state advance and its six relocation-aware register
allocation guards are in
[Working Note 376](WORKING_NOTES/376-game-sequence-state-advance-match-20260928.md).
The completed active-record counter, its no-unroll object profile, and four
relocation-aware opening-schedule guards are in
[Working Note 377](WORKING_NOTES/377-game-active-record-counter-match-20260928.md).
The completed record-output accessor and its direct-from-C match are in
[Working Note 378](WORKING_NOTES/378-game-record-output-accessor-match-20260928.md).
The completed actor-position query and its direct-from-C match are in
[Working Note 379](WORKING_NOTES/379-game-actor-position-query-match-20260928.md).
The completed dual event-byte dispatcher and its guarded frame-layout match are
in [Working Note 380](WORKING_NOTES/380-game-dual-event-byte-dispatch-match-20260928.md).
The completed memory viewer and its restored address/data lifetimes are in
[Working Note 009](WORKING_NOTES/009-debugger-memory-view-byte-match-20260925.md).
