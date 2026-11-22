# 2623 - Surface angular effect direct byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_15194408` emits all **96 retail words directly from semantic C**, using
the existing retail pool binding and **zero target guards, insertions or
omissions**. Fresh production totals are **4,606 / 5,528 (83.32%)** and Game
**3,933 / 4,855 (81.01%)**, with zero address drift and 922 different functions.
Init remains 492/492 and Debugger 181/181. **93 more matches** reach 85%.

## Recovered source, surface and ABI

Source: `conker/src/game/generated_1C1150.c`; preserved assembly:
`conker/asm/1C1150.s:520`. VA `0x15194408..0x15194588`, ROM
`0x1C18B8..0x1C1A38`, 384 bytes, frame 152, S0 at SP+0x20, RA at SP+0x24.
The O2/g3 profile and all 11 call/address relocation sites are preserved.
Raw instruction SHA256:
`81e1f0f77d3768a97b69bb72381d489ba8635bbd251a1bdbc6ca9fa29634d5ed`.

Both actual callers pass a source actor in A0 and the selected actor in A1.
The first argument is saved but unused. The old integer view of the wrapper
`func_15194588`'s second argument is repaired to `u8 *`; all 17 emitted wrapper
words remain identical. No shared header declaration or caller object changes.

Actor kinds 0 through 4 share the body. It calls `func_151AE7B0` with scale
0.6, duration 90, channel 255 and category 1, then obtains the 36-byte
`HeightResult71820` surface through `func_1504715C`. The local surface view
contains height, nine signed vertex halves, metadata, flags/state and value;
it is not a float matrix. Recovered compatible layouts supply the eight-byte
angle descriptor and 68-byte localized trail.

Position is loaded after both services: X/Z from actor+0x14/1C and Y from
actor+0x18 plus 50. Angles are 0/255/-63/35. The trail supplies time 6/3,
scales from `D_800A8294/8298`, radii 13/8, counts 12/5, request selectors 3/2,
durations 30/30, modes 100/100, selector zero, chance `D_800A829C`, values
16/15 and request zero. The final call is
`func_15153F18(&angles, &trail, &surface, 255, 1)` under its recovered ABI.
No padding initialization is invented. The selector store follows the three
final value stores to recover the retail schedule.

## Compact pool and neighbor guard precondition

The owner already uses `RETAIL_RODATA_SYMBOL := jtbl_800A8258_game`. Its new
five-entry compiler table starts at compact offset 40 and every entry names
the target body at +56. The retained GameData table at `0x800A8280`, ROM
`0x24CD40`, supplies the same five `0x15194440` pointers.

Compact rodata grows from 64 bytes (15 entries plus alignment) to 80 bytes
(20 entries). The first ten existing entries retain their owners and offsets.
The five later `func_15194794` entries move from offsets 40..56 to 60..76,
with their target owner and relative +96 unchanged. The complete raw neighbor
delta is its single LO16 addend at +0x54: `0x8C2E0028 -> 0x8C2E003C`.

Accordingly, exactly one existing CSV **expected** word advances from 0x28 to
0x3C. Its replacement remains `0x8C2E0000`, and its original retained-table
binding `jtbl_800A82BC_game` is unchanged. Guard count, replacement words,
relocation contracts and every other CSV byte are preserved. The stale old
expected word is explicitly rejected. No new target guard is introduced.
All **28 padded neighbors** and their relocations remain byte-identical.

## Fresh validation and strict image

Run `python3 -m unittest tools.tests.test_game_surface_angular_effect_15194408_match -v`.
All five tests pass before and after installation in primary tools and an
isolated sibling overlay, with exact Python and non-Python fingerprints.
The real dirty sibling is preserved. Shared `make tools-check` passes.

1. The complete owner compiles with unchanged diagnostics. The natural mixed
   GLOBAL_ASM Make recipe executes five commands and produces the independently
   padded object exactly. Both padders retain all 96 target words. Sixteen
   independent GNU links check four emitted forms and table/constant/callee
   rebases, including HI16 carry boundaries and the compact/original table alias.
2. The guest model runs 1,696 cases per stream, covers all 96 words, all 256
   kind bytes, both stack phases, float transport boundaries, service changes
   to kind/position/constants and guest-only incoming-home mutations. Complete
   private memory, registers, ordered accesses and calls agree across the raw,
   padded and original streams, including 94 sampled access-fault prefixes.
   Five corrupt table-pointer controls fail, and 251 invalid kinds never read
   any table byte. Fault evidence concerns instructions, not portable C faults.
3. The two actual three-word caller windows at `0x15074FB8` and `0x151945B0`
   run 60 cases per stream with the complete target connected. They verify
   both actor arguments, the velocity-store delay and the A1-reload delay.
   Missing-delay controls are effective. Complete 35/17-word parent bodies
   and the 89/56/168-word surface/attach/submit providers are statically retail
   exact; only the two caller windows are executed in this check. Provider
   internals use explicit mutating contracts. The ROM/loaded-pointer census
   finds the two direct calls and no aligned pointer literals, without excluding
   computed references.
4. Defined SDK32 native fixtures run 6,144 cases at each of O0/O2/O3 with
   strict aliasing and UBSan. Pointer width and all three descriptor extents
   and field offsets are asserted. Ten effective incorrect-source controls
   cover kind gate, attach scale/duration, wrong actor, height, angle, count,
   selector, scale source and early position capture. Native fixtures do not
   rewrite incoming argument homes or read indeterminate C padding.
5. The independent whole-ELF prediction equals production exactly:
   **344 changed bytes, zero exclusions**. The declared target slot and symbol
   size 12->384 change, plus three closed adjacent absolute-symbol permutations:
   `D_800A8298/D_8008FAD0`, `D_800D2890/D_800E0DA0`, and
   `D_800A8F9C/D_8009FC9C`. Six symbol records and 66 name bytes retain every
   named attribute. These bytes are predicted explicitly, never ignored.
   All 189,088 GameData bytes / 720 owners remain exact. Conversion rows and
   all other function bodies/addresses/extents are preserved.

## Production and continuation

The actual production rebuild and recount pass. ELF SHA256:
`0e551d7a155c1b7083ce2310c90dc56e24e9ed9270f1d80ee6bc47a9720fdd4f`. Prior consumer `4bb620c5e900905f953b90ed4a9f3f1118a5c5b5`;
prior tools `3bbc6c4135a189fd0b90a3253c46f2a81e23e58a`. Tools are committed before the consumer.
The pre-existing duplicate generated_12D630 recipe warning remains recorded.
The README receives only its Total and Game aggregate row changes.

The available host scene configuration/input was audited read-only. It consumes
binary words and symbols and supplies no direct import for this recovered C.
No host build or Release changes, full provider/parent execution, hardware or
gameplay acceptance are claimed. Zero advisory calls; the prior authentication
failure was not retried.

Continue with adjacent `func_151945CC` (114 words / frame 0xB0). It shares the
surface/trail layouts, but snapshots position before its providers, uses a
double Y+270 operation, retains a signed intermediate heading halfword and
gates category lookup/submission on the actual classifier result. The private
read-only next-function audit records its separate acceptance boundary.
The private position, camera, matrix and history candidates remain uncredited.

Graph maintenance: the native update exited 1 with all
70,321 prior IDs retained. The subsequent serial scoped extraction
covers 7 C/Python files with no missing AST sources, producing
70,366 nodes / 163,445 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
