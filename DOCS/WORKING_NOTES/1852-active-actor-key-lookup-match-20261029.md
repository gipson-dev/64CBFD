# 1852: First active actor key lookup match

Date: 2026-10-29. Target `func_1505EEF4`, owner `game_83300`.
VA `0x1505EEF4..0x1505EFD0`, ROM `0x8C3A4..0x8C480`: 220 bytes /55 words,
filling the entire retail slot. There are no alignment words in this slot.

The zero-return placeholder becomes `struct127 *func_1505EEF4(s32 key)`.
It scans the first 25 records in inline `D_800CC2D0[26]`, returning the first
record whose `interaction_state` word is nonzero and whose unsigned `unk13F`
byte equals the complete signed 32-bit argument. It returns NULL if no record
matches. Reserved slot 25 is excluded. Negative and greater-than-255 arguments
cannot match. The local forward declaration is repaired; existing callers'
pointer ABI is preserved without shared-header changes. Unknown key meaning
is left as `key` / `unk13F`, rather than inventing an actor identity name.

Advancing the actor pointer before the loop counter in the for-update
expression recovers retail's opening schedule and four-record unrolled loop.
The first slot is peeled by IDO. All 55 linked words emit directly from C,
with the existing O2/g3 profile and zero guards, inserted/omitted words,
frame adjustments or compiler-profile changes. The routine is a leaf with
no stack frame or stores. Three duplicate loads at offsets 0x58, 0x7C and
0xA0 are unreachable after return paths; all 52 reachable words are covered.

Two unlinked immediate words differ because IDO uses `D_800CC2D0+0x32C`
and `D_800CC2D0+0x13F`, while original assembly names those addresses
`D_800CC5FC` and `D_800CC40F`. Eight relocations resolve to identical code.
Original and selected functions link identically under the retail layout
and three additional layouts exercising signed-low-half carry boundaries.
No word patch or binary normalizer is used for these ordinary linker addends.

- Eight fresh canonical methods pass independently in both tools copies,
  together with shared tools checks. Production reruns two installed checks
  per copy and reuses six semantic checks only after complete module, input
  and qualified-artifact identity checks. The older tools mirror retains
  1,994 inherited dirty paths and receives three new files; it is not committed.
- Guest: 3,572 cases /7,144 original-and-compiled executions, literal complete
  machine-state and memory agreement. Cases cover all 256 key bytes, every
  record slot including the excluded reserved record, null results, duplicates,
  inactive records, high-bit/noncanonical active words, full-word invalid keys,
  and two stack alignments. There are 108 access-prefix comparisons, three
  relocated layouts /180 cases, and two sparse-memory first-slot hits. There
  are no helper calls or guest/native byte-order alias exclusions for this
  read-only lookup.
- Native32 O0/O2/O3 each pass 3,572 cases with UBSan. The fixture verifies the
  0x32C structure stride, key offset 0x13F, return pointer and unchanged bytes
  across all 26 records. Seven effective controls reject: searching reserved
  slot 25, skipping slot zero, ignoring the active word, signed key-byte reads,
  narrowing the argument, reading the other key field and always returning NULL.
  The installed freestanding native32 SDK path is used; no packages are installed.
- Two original caller JAL/delay windows, `func_15023870` at VA 0x15023890 /
  ROM 0x50D40 and `func_150979CC` at VA 0x150979D8 / ROM 0xC4E88, each run
  50 cases. They qualify the A3-to-A0 delay move and the incoming A0 home
  store respectively, with the returned pointer preserved. Full-ROM aligned
  JAL/pointer census is retained privately; other callers and complete parent
  bodies are not claimed dynamically qualified by these two windows.
- Complete mixed C/GLOBAL_ASM owner compilation and `pad_c_object` padding
  preserve all 88 neighboring functions and owner pools. The actual five
  Make compilation/postprocessing/padding commands reproduce the exact object.
  Eight inherited C pointer/integer warnings and the inherited duplicate
  generated_12D630 recipe warning remain; no new C diagnostics are introduced.
  All 228 raw-byte/binding controls and 240 full-image corruption controls reject.
- Independent full-image prediction equals production: 179 changed bytes,
  comprising 178 target code bytes plus one function-extent byte. There are
  zero unrelated metadata changes or exclusions. All 6,055 other linked
  bodies and all addresses remain fixed. Protected Game data stays exact
  across 189,088 bytes /720 owners. Guard manifest and conversion inventory
  CSV bytes are unchanged.

Fresh adopted-ELF count: **3,929/5,506 (71.36%)**, Game **3,256/4,833 (67.37%)**,
Init 492/492 and Debugger 181/181, zero drift. **201** more are required for
4,130 exact C functions. Tools committed first: `0285fd53ecb04b3bd0f76eee885e8b50c6b4d63f`. No push.
Root README receives only two updated aggregate rows; function details stay here.

The scoped eleven-file AST refresh retains or uniquely relocates all 50,210
previous nodes and preserves 104,083 valid old directed relationships. One
obsolete s32 return relationship retires for the recovered actor-pointer
interface. Caller-window and original-array-alias evidence is attached to the
function. Outside-scope manifest rows and global analytics remain historical;
this is not a full-corpus extraction or reclustering claim.

Artifacts: `conker/build/game-active-actor-key-lookup-match/`. Next screen
`func_1505EFD0` still needs all qualification gates; the neighboring key lookup
`func_1505EFD0` must be independently qualified rather than counted by analogy.
The parked `func_151A084C` remains uncredited, as do all other private candidates.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% matching goal remains active.
