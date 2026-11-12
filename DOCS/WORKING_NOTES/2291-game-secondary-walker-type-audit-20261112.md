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

## Follow-up: complete existing-object header overlay screen

At consumer commit `a774e6f2`, a fresh private `struct115` overlay replaced
`pad0[0x14]` with `void (*unk4)(u8 *)` and 16 remaining padding bytes. The
production header and candidate function were not changed. A conservative
textual include inventory found 292 potentially dependent C sources, 291 with
existing objects. A separately constructed reverse include graph scanned 780
files and found the same 292 sources with no missing source and no computed
includes; `PR/sptaskoff.h` was an unresolved literal include. Both inventories
are subject to conditional-include and include-resolution limitations.

The Make dry-run plan for those existing objects supplied 300 compiler-profile
commands and 58 generated inputs. Paired raw compilations with the unchanged
and overlay headers yielded no differences in the compared non-debug section
bytes or section metadata (including NOBITS), or in diagnostics; all frozen
inputs remained unchanged during the screen. All 58 Make-planned postprocess
comparisons also agreed. A separate object parser checked text, complete
function symbols and named text relocations for all 300 raw and 58 postprocessed
objects and found no differences. This is an isolated object overlay screen,
not a production rebuild, full-image comparison, non-text relocation audit or
coverage of the source without an existing object.

The retail descriptor data was also rechecked across all 101 offset-4 slots:
columns 47 and 78 contain `func_151AD174`, column 48 `func_151ACB60`, and
column 100 `func_151041E4`; the remaining slots are zero. The existing
`func_151ACB60` C definition takes `u8 *`. Retail instructions for each of the
two other currently stubbed callbacks consume the incoming `a0` as a pointer,
but this observation alone does not establish their eventual complete C
interfaces or semantics. Preserve that limitation when qualifying the typed
indirect call.

Private audit scripts and receipts are under
`conker/build/game-secondary-walker-header-screen/`; paired raw objects are in
the receipt's temporary directory and are not durable. Next, qualify the
callback interface and candidate guards, then perform the remaining caller,
padder, rebased-link, actual Make and independent full-image checks before
installing or crediting the walker. The refreshed production ELF still reports
**3,705 / 4,840 (76.55%)** Game and **4,378 / 5,513 (79.41%)** overall, with
zero address drift.

## Follow-up: caller, rebases and connected retail timer callback

At consumer baseline `523ea23d`, the private typed-u8 candidate was checked
through the original `func_15019130` call window at `0x150192EC`: 32 cases
with modeled callbacks passed for the raw candidate and retail body. This
covers the call window only, not complete parent execution.

Both private padder outputs and independently assembled retail were linked at
four low-address patterns for each of the four global symbols: 12 GNU links
agreed with the independently bound relocation words. The same three bodies
agreed at 270 bounded external access-cut prefixes, including machine state
and modeled callback effects. These are interpreter checks, not native or
hardware fault guarantees. The candidate retains 35 guarded words and no
insertions.

A new connected test executes the actual retail `func_151041E4` callback
inside both the raw typed candidate and retail walker for 480 cases. It covers
state 3 and a default state, both rows, zero/one/two-node lists, timer values
around zero, varying tick counts and a modeled release that changes the saved
iterator. The test observed 688 child calls and 488 modeled helper calls; 50
of the callback's 170 instruction positions were visited. The release and sound
helpers remain modeled. A control changing the tick multiplier was rejected in
the state-3 timer boundary case. This does not cover the callback's other
states, floating-point paths, full lifecycle or gameplay. The production C
for `func_151041E4` remains a zero-return placeholder.

A private current-baseline shadow executed the three Make-planned owner
compile/pad/assemble commands using a copied typed header, then linked the
result against the frozen current ELF. All 41 owner neighbors and every
function address were unchanged; the 74 target words bound exactly to retail.
An independent image prediction agreed with all 227 changed ELF bytes and zero
exclusions. The 189,088 protected data bytes were unchanged. The private ELF
SHA-256 is `9c93a0992baa0b942eaafaa3f4b94385dc29f2352d59b5237b3329a08b2947cf`.
This shadow does not install or credit the function, and executing commands
from a Make dry-run plan is not itself a production Make build.

There is still a source-interface issue to resolve before adoption: the
proposed field calls `void (*)(u8 *)`, while the production placeholder
definitions for `func_151041E4` and `func_151AD174` are both `s32` functions
with unspecified parameters. Retail instruction evidence supports a pointer
argument and an ignored return at this walker, but does not make those C
function types compatible. The three retail callback functions must be reconciled
with the eventual C definitions, and the remaining guard/alias, current tools
and production checks completed, before marking a match. Private scripts and
receipts are in `conker/build/game-secondary-walker-header-screen/`.

The smaller callback now has a private semantic reconstruction and bounded
behavior screens; see [Note 2314](2314-game-type64-timer-callback-private-screen-20261112.md).
It is not installed or byte-matched.
