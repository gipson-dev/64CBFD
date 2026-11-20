# Note 2583: Trail emitter frame provenance and private refinement

Date: 2026-11-20. Consumer baseline `f4a4e71abd6d773b210325333e9413f79980a3c6`;
tools baseline `57d7dd9183c783043b91c0fa658145f4a3f93308`.

`func_151058B4` now has a tested private source refinement with **197 words,
frame 248, 12 aligned differences**, down from 24. Retail remains **197 words,
frame 240**. The frame is not fixed. Live source remains GLOBAL_ASM, with **zero
matching credit** and no installed guards, conversion row or production change.
The 85% objective stays open. Root README aggregate rows are unchanged.

The private direction interface now agrees with the actual recovered definition:
`void func_15143794(s16, s16, f32, vertex *)`. The packet contains a real `vertex`
member, passed by address, rather than declaring a separate `f32 *` interface.
This is a proposal only; neither live owner is edited. Replacing the separate
initial sample local with the RNG expression preserves public behavior and
recovers twelve opening-schedule words without altering the loop's order.

## Observed storage provenance

The full owner and isolated target emit identical target instructions and
relocations. A fingerprint-locked debugger runs only newly owned compiler
children. CFE/UOPT inputs are copied before their consumers run, with fired
watchpoints, input hashes, successful child and driver exits, and unchanged
text, functions, relocations and pools. No compiler binary is changed.

| Form | CFE M bytes | UOPT M bytes | UGEN aligned locals | Saved | Outgoing | Frame | Words |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Prior canonical | 124 | 128 | 128 | 96 | 24 | 248 | 197 |
| Refined, correctly typed | 120 | 124 | 128 | 96 | 24 | 248 | 197 |
| Anonymous emitter control | 116 | 116 | 120 | 96 | 24 | 240 | 200 |

UGEN writes frame values `0 -> 96 -> 120 -> final`. Its temporary pool,
temporary extent and temporary base remain empty/zero. Thus this measured
overage is not late UGEN spilling.

The UOPT extent watch at prepared memory `0x1001C4B4` first fires in
`f_readnxtinst` at native PC `0x489857`, importing the CFE M extent. It next
fires at native PC `0x450CF3` inside **`f_spilltemps`**, adding exactly four bytes.
The actual spill image is checked against the live expression table, including
its identity, four-byte size and new extent. It is expression **14** in the old
canonical and **9** in the refinement. The qualified canonical mode5 listing
identifies the common expression as the incoming record address **plus 40**:
`record + 0x28`, the inline emitter address. The named emitter has M home -12
in that canonical frontend. Mode5's suppressed real-number output is not used
as valid timing or cost evidence.

The anonymous emitter control removes the four-byte source home and this
additional reservation. Its watch fires at the imported extent and never
grows it. The positive canonical probe establishes that the same observer
detects real growth. Although this control reaches frame 240, it emits 200
words and changes allocation/division code. It is not an installable match.

The upstream [IDO spill allocator](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptreg2.c)
was consulted as background. Prepared-compiler native observations, not an
assumed upstream structure layout, establish the local addresses and identities.
The first raw stack snapshot was not an IChain; the final observer explicitly
follows the spill image through the current stack slot and validates its table
entry. No identity is inferred from an arbitrary stack word.

## Rejected interface shortcut

A compact-angle screen reaches 197 words/frame 240 by changing the direction
helper's pitch declaration to `s32`. The actual recovered helper defines **s16**
pitch and a **vertex pointer**. This screen is rejected despite its attractive
length and frame. The final tools compile the actual helper body with the
correct prototype and verify its complete target equals the production object;
an intentionally widened pitch prototype fails compilation as incompatible.
No shared declaration, callee or caller is changed to accept this screen.

Other retained diagnostic screens include register hints, pointer lifetime and
cursor forms, scalar narrowing, initial sample lifetime, and address expressions.
They are not alternative installed sources. Register hints preserve the old
248-byte frame. Integer-reuse is a deliberately invalid lifetime control and
must not be selected. The correct frame alone is insufficient acceptance.

## Fresh qualification and remaining gates

Four fresh tests pass in the primary tools checkout and in a **989-file isolated
overlay**. The real dirty sibling's HEAD, raw status and 343 dependency hashes
are preserved. The overlay uses 341 equal sibling files, 643 explicit primary
fallbacks, four task files and one bootstrap. Imported Python dependencies are
hash-paired between both runs. `make tools-check` passes.

- Full copied-owner compilation preserves all ten other functions and constant
  pools. The private wrapper/type recovery still reduces five warnings to two;
  the two unrelated warnings remain. The live owner is not edited.
- **140 guest cases per stream**, with 196/197 words visited, preserve ordered
  helpers, public memory, defined 22-byte header/55-byte packet fields and ABI.
  The unreachable `break 7` at offset 0x1C4 remains literal, not visited.
- **40 original wrapper cases per stream** preserve commands 0x38/0x39 and
  narrowing of the raw command byte. Actual SDK32 C at **O0/O2/O3 each passes
  68 finite cases and 54 C-wrapper cases**, strict aliasing and UBSan. Eight
  compiled semantic mutations fail at runtime. Providers remain bounded mocks;
  this does not qualify the complete sampler, trigonometry or allocator.
- The refined helper pointers remain **eight bytes below retail**, despite
  matching SP-relative bottom/top/packet/header offsets 0x88/0x8C/0x90/0xCC.
  All seven seeded padding differences remain: header 0x16/0x17 and packet
  0x22/0x23/0x33/0x3A/0x3B. No complete copied-padding match is claimed.
- **68 cases retain the public read-order difference**. Retail's source-Y
  read precedes the range globals; the raw refinement still reads range-base
  first. Fault-prefix/all-input CFG/FCSR qualification is unfinished.
- The fresh actual ELF recount remains **4,570/5,521 (82.77%)** total and
  **3,897/4,848 (80.38%)** Game, zero drift, 951 different. Init 492/492 and
  Debugger 181/181 remain exact. At this denominator, 123 more matches reach
  85%; further ASM conversions can increase it. ELF SHA-256 remains
  `d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.

This stage freezes 2,042 predecessor inputs and 128 independent copies before
the documented note/index changes and four new tools. Source, guards, progress,
production owner object and complete live ELF retain their prior bytes. Tools
are committed before consumer docs/gitlink; no push, Claude call, host edit,
save change or frozen Release operation occurs.

## Continue the same target

Resume `conker/build/game-map-trail-emitter-151058b4-frame/` and
`tools/experiments/game_map_trail_emitter_151058b4_frame.py`. The qualified
typed proposal is `qualified-frame/refined.c`, not the rejected ABI screen.
The three frame traces, their copied ucode and `qualified-summary.json`, plus
`qualified-frame/canonical-mode5/qualified-listing.json`, identify the actual
reservation. The refined expression is 9; do not assume old ordinal 14.

Recover local extent at most 120 with the correct s16/vertex interface, 197
words and original physical homes. The now-observed address-expression spill
and the remaining frontend reservation are the next discriminating targets.
Then close public-read/cached-FP scheduling and full copied-byte/fault/CFG/ABI
gates, both padders, actual Make, GNU rebases, strict whole-image prediction,
installed qualification and fresh production/recount before any credit.
These private tests do not justify frame patches or ABI widening.

Reproduce the four checks under prepared WSL:
`python3 -m unittest tools.tests.test_game_map_trail_emitter_151058b4_frame -v`.
Graphify retains old IDs and links active ASM with this explicitly private
refinement and its compiler evidence; the scoped AST refresh is not a full
corpus semantic extraction.

The native graph update first failed with no disk space while preserving all
68,180 old nodes. C: had about 13 MB free. NTFS compression of three ignored
build-evidence folders and the graph recovered room (about 271 MB free at that
measurement), without deleting files. All 366 copied baseline hashes, the graph
bytes and copied compiler-input hashes were verified unchanged afterward. The
subsequent three-file scoped refresh succeeded and retained all old IDs. Disk
headroom remains small; this is not a claim that the wider drive is cleaned up.
