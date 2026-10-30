# 1853: Active actor alternate-key lookup match

Date: 2026-10-29. Target `func_1505EFD0`, owner `game_83300`.
VA `0x1505EFD0..0x1505F0AC`, ROM `0x8C480..0x8C55C`: 220 bytes /55 words,
filling the entire retail slot. There are no alignment words in this slot.

The zero-return placeholder becomes `struct127 *func_1505EFD0(s32 key)`.
It scans the first 25 records in inline `D_800CC2D0[26]`, returning the first
record whose `interaction_state` word is nonzero and whose unsigned alternate-key `unk127`
byte equals the complete signed 32-bit argument. It returns NULL if no record
matches. Reserved slot 25 is excluded. Negative and greater-than-255 arguments
cannot match. The local forward declaration is repaired; existing callers'
pointer ABI is preserved without shared-header changes. Unknown key meaning
is left as `key` / `unk127`, rather than inventing an actor identity name.

Advancing the actor pointer before the loop counter in the for-update
expression recovers retail's opening schedule and four-record unrolled loop.
The first slot is peeled by IDO. All 55 linked words emit directly from C,
with the existing O2/g3 profile and zero guards, inserted/omitted words,
frame adjustments or compiler-profile changes. The routine is a leaf with
no stack frame or stores. Three duplicate loads at offsets 0x58, 0x7C and
0xA0 are unreachable after return paths; all 52 reachable words are covered.

Two unlinked immediate words differ because IDO uses `D_800CC2D0+0x32C`
and `D_800CC2D0+0x127`, while original assembly names those addresses
`D_800CC5FC` and `D_800CC3F7`. Eight relocations resolve to identical code.
Original and selected functions link identically under the retail layout
and three additional layouts exercising signed-low-half carry boundaries.
No word patch or binary normalizer is used for these ordinary linker addends.

- Eight fresh canonical methods pass independently in both tools copies,
  together with shared tools checks. Production reruns two installed checks
  per copy and reuses six semantic checks only after complete module, input
  and qualified-artifact identity checks. The older tools mirror retains
  1,997 inherited dirty paths and receives three new files; it is not committed.
- Guest: 3,572 cases /7,144 original-and-compiled executions, literal complete
  machine-state and memory agreement. Cases cover all 256 key bytes, every
  record slot including the excluded reserved record, null results, duplicates,
  inactive records, high-bit/noncanonical active words, full-word invalid keys,
  and two stack alignments. There are 108 access-prefix comparisons, three
  relocated layouts /180 cases, and two sparse-memory first-slot hits. There
  are no helper calls or guest/native byte-order alias exclusions for this
  read-only lookup.
- Native32 O0/O2/O3 each pass 3,572 cases with UBSan. The fixture verifies the
  0x32C structure stride, alternate-key offset 0x127, return pointer and unchanged bytes
  across all 26 records. Seven effective controls reject: searching reserved
  slot 25, skipping slot zero, ignoring the active word, signed key-byte reads,
  narrowing the argument, reading the other key field and always returning NULL.
  The installed freestanding native32 SDK path is used; no packages are installed.
- The sole aligned direct call is in original parent `func_15119938` at
  VA `0x15119D5C` / ROM `0x14720C`. Its JAL delay instruction clears A0,
  so the original caller always searches key zero. The two-word window runs
  108 cases covering absent keys, first and later matches, reserved-slot
  exclusion, active-word values, stack alignments and incoming A0 values, proving the delay instruction overrides the incoming
  argument. Full-ROM scans find this one JAL, no direct J, and no aligned
  full-pointer reference. The caller's large C body remains a stub; its
  interface evidence comes from original `conker/asm/142560.s`. Earlier
  float/vector work and subsequent distance/event logic are preconditions;
  no complete-parent, FCSR or gameplay acceptance is claimed.
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

Fresh adopted-ELF count: **3,930/5,506 (71.38%)**, Game **3,257/4,833 (67.39%)**,
Init 492/492 and Debugger 181/181, zero drift. **200** more are required for
4,130 exact C functions. Tools committed first: `ea775071b7b94dbfb7f875b22fb9afbdd8a5416c`. No push.
Root README receives only two updated aggregate rows; function details stay here.

The scoped eleven-file AST refresh retains or uniquely relocates all 50,259
previous nodes and preserves 104,179 valid old directed relationships. One
obsolete s32 return relationship retires for the recovered actor-pointer
interface. Original constant-zero caller-window and array-alias evidence is attached to the
function. Outside-scope manifest rows and global analytics remain historical;
this is not a full-corpus extraction or reclustering claim.

Artifacts: `conker/build/game-active-actor-secondary-key-lookup-match/`. Next screen
`func_150AE280` still needs all qualification gates. The previously recovered lookup
`func_1505EEF4` and its key at+0x13F remain unchanged; 88-owner-neighbor and
whole-image checks explicitly preserve it. No counterpart is counted by analogy.
The parked `func_151A084C` remains uncredited, as do all other private candidates.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The 75% matching goal remains active.
