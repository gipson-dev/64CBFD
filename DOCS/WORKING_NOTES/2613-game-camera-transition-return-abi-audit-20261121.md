# Note 2613: Camera transition return-ABI audit

Date: 2026-11-21. Consumer baseline `3f8e1e207bd4b5c6579b40a37022e7f5ccf8d123`, tools baseline
`8c4c1d088f021beffa40c0d7ef4915370c2fb7f1`. Read-only audit tools: `f164dce9a4221afc98d78721dc91102262f60145`.

`func_15128030` remains **uninstalled and uncredited**. Production is still
**4,596 / 5,528 (83.14%)**, Game **3,923 / 4,855 (80.80%)**, zero drift,
932 different and **103 more** matches to 85% at this denominator. No source,
object, linked image, conversion rows, guards or root README figures change.

## Measured ABI evidence

The original slot is **226 words / 904 bytes**, frame **48**, with S0/S1/RA and
the F20/F21 pair saved. VA `0x15128030..0x151283B8`, ROM
`0x1554E0..0x155868`. It initializes or advances the camera record at +0x7F4,
blends position/heading/distance/height and finishes or decrements its timer.

The original caller at **0x15128568** passes the camera in the delay slot,
then tests the complete **V0** register at 0x15128570. It does not compare
against a canonical one. The forced counter and zero-state exits return zero;
the active noncompletion tail explicitly returns one; an unrecognized state
carries the loaded unsigned state into V0. The completion path carries the
primary actor pointer loaded at **0x15128204** through its final angle calls.

Both actual angle routines, `func_15048720` (**14 words**) and `func_15048A70`
(**24 words**), match their original slots in the sealed/current ELF. Their
decoded GPR writes exclude V0. **180 executions** connect the two actual
routines, checking finite wrapped-angle math, stack restoration and preservation
of three distinct seeded V0 values. A changed delay-slot instruction that
clears V0 is an effective negative control. **120 original completion-tail
window cases** at 0x15128348..0x151283A0 check all modeled memory updates,
timer truncation/clamping and exact outgoing V0 values. These are bounded
instruction-window/helper checks, not complete transition or caller acceptance.

## Source screens and adoption boundary

A complete private C draft recovers the transition record and behavior without
changing shared SDK headers. Recovered typed helper arguments remove precisely
the old `func_15124C38(arg0, 0)` warning. All **44 owner neighbors** and pools
remain unchanged in the source screens. Defined-return variants have **231
to 236 words**, with frames 48/56/64; narrower case scopes recover frame 48.
None is a whole-function byte match.

Separate diagnostic controls omit return values on completion/default paths.
They reach **228/229 words, frame 48**, but still do not match. Those controls
are explicitly non-installable: their compilation does not establish the
original C source or a defined portable return contract. No candidate is
counted merely because its frame or length is close. Do not replace the
measured noncanonical returns with Boolean constants or add return/frame
patches to manufacture a match.

Private sources, rejected screens, frozen inputs and receipts are retained in
`conker/build/game-camera-transition-15128030-private/`. The baseline retains
**2,371 hashes / 498 copies**. The read-only public audit regression passes in
both tools configurations, with matching imported-code/data fingerprints;
shared `make tools-check` passes. The actual sibling's preexisting work and
352 dependency hashes are preserved. These checks do not qualify any private
C draft for installation. No native, full-provider, FCSR, hardware or gameplay
acceptance is claimed for the transition reconstruction.

## Next work

Keep the transition draft private until its defined C and exact return ABI can
be reconciled and all normal adoption gates pass. The fresh remaining-function
inventory still confirms 83.14%. Its smallest rows also include coroutine or
shared-entry assembly, so word count alone is not a C-conversion qualification.

Continue matching with **`func_15022024`**, a 91-word record/output query in
`generated_49D30`: inspect the complete owner/profile/callers and freeze a new
baseline from this commit. The **85% goal stays active**.

```sh
python3 -m unittest tools.tests.test_game_camera_transition_15128030_return_audit -v
make tools-check
```
