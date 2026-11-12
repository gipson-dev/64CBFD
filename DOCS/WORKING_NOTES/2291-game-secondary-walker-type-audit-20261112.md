# Secondary walker callback type audit

Date: 2026-11-12. `func_151671E8` walks the same two rows and 101 descriptor
columns as `func_151670C0`, but loads its callback from descriptor offset 4.
The original `func_15019130` frame loop calls it at `0x150192EC` and does not
inspect its return value. Retail registry words at offset 4 are nonzero for
columns 47, 48, 78 and 100; the other 97 are zero.

A private overlay candidate emitted 74 words and agreed with retail in 96
modeled guest cases, but reads a callback pointer through the existing
`struct115.pad0` byte array. That tentative type overlay is not installed or
credited because it needs an effective-type audit. A private header refinement
that names a function-pointer field at offset 4 produced the same candidate
body and left all 41 owner neighbors unchanged in isolated compilation; the
overlay owner comparison changed only `.mdebug`. This is not a full dependent
object audit. A native test using the refined SDK32 layout passed 96 cases and
five negative controls at each of O0, O2 and O3. Retail callback
`func_151ACB60`, registered in column 48, matches the current ELF across all
13 words. A connected guest check executes that retail callback in 32 cases,
covering 44 child calls and 20 calls to its modeled helper; the typed walker
remains a private candidate.

Source-local object-representation alternatives were also screened: bytewise
copy emitted 90 words, while `memcpy` emitted 85 words and introduced calls.
Neither was installed. With the normal Makefile and patch-table timestamp
exclusions, a simulated `structs.h` change adds 25 compiler invocations to the
current no-op build plan. The earlier unfiltered dry run included hundreds of
unrelated pending patch-table rebuilds and does not measure this header change.
No shared header was modified.

Next, qualify the typed field with its exact SDK32 layout and the 25 affected
build objects, auditing each changed section and the complete linked image;
then repeat caller, callback, native and production gates. Until then, this
function remains unmatched and Game progress is unaffected by this audit.
