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

## Follow-up: callback signature and incomplete header dependencies

The real `func_151ACB60` definition accepts `u8 *`; the earlier private
`struct102 *` callback type is therefore not a suitable final signature for
that C definition. A private `void (*unk4)(u8 *)` variant, with an explicit
node conversion at the call, produces the same 74-word candidate and leaves
the 41 neighboring functions unchanged in isolated compilation. Its SDK32
native fixture passes 96 modeled cases and five negative controls at each of
O0, O2 and O3 with undefined-behavior sanitization. The other registered
callbacks are still placeholders, so their eventual C signatures require
separate verification.

The candidate requires 35 word guards with no insertions. Both padding paths
produce the assembled retail function, and reject 70 individually corrupted
guards. These are private qualification results, not a production match.

The 25 commands above describe only the Make dry run; **they are not all of
the header's consumers**. A direct-include inventory found 291 sources naming
`structs.h`, `functions.h` or `variables.h`, of which 290 have existing
object files. Of those 290, 266 do not appear in that dry-run plan, including
`src/game_1944C0.c`. This is a bounded inventory of direct includes and
existing objects, not a count of active or indirect dependencies. The generic
`$(BUILD_DIR)/%.c.o: %.c` rule in `conker/Makefile` does not declare these
headers, unlike some specialized rules, so a header-only edit can leave stale
objects. Do not rely on that dry run to identify the full rebuild set.

For each of the 25 planned compiler commands, a private overlay comparison
of the original header against each typed variant found no changes to the
stored non-debug section bytes and no diagnostic changes; changes were
limited to `.mdebug` or absent. This raw-object probe did not compare NOBITS
section metadata, postprocessed objects, the omitted consumers or a linked
image, and does not close the broader header audit.

Next, establish a complete dependency and clean-build strategy, including
direct and indirect consumers and NOBITS metadata, before modifying the shared
header. Qualify the complete linked image and the callback interfaces, then
repeat caller, native, padding and production gates. Until then, this function
remains unmatched and Game progress is unaffected by this audit.
