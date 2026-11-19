# Note 2569: Ground explosion byte match

Date: 2026-11-19. Consumer baseline `15ada7539ef792c8af0159765eb820e53639608e`;
tools baseline `f136a1adb70b21b241e373a91e16281a5e868d5c`.

`func_15103E40` replaces its GLOBAL_ASM declaration with complete semantic C
and is **byte-exact across 202 body words / 204-word slot / frame 152**.
Four expected-word guards move only one closed floating sample cell from
`SP+0x54` to the retail `SP+0x44`. The original two alignment NOPs remain.
No instruction insertion, omission, profile change or shared-header edit.

Fresh production recount: **4,563 / 5,515 (82.74%)** total and
**3,890 / 4,842 (80.34%)** Game, zero address drift, 952 different functions.
Init 492/492 and Debugger 181/181 remain complete. **125 further matches**
are needed for 85% at this new denominator. Converted counts are
5,515/6,048 (91.19%), 86.23% of bytes;
Game 4,842/5,327 (90.90%), 85.61% of bytes.
Exactly one conversion row changes from ASM to C. The ELF is byte-identical
because the previous production body was already original assembly.

## Source, callers and interface

Owner `conker/src/game/generated_1312F0.c`, VA `0x15103E40..0x15104168`
body, slot through `0x15104170`; ROM `0x1312F0..0x131620`. Original assembly
is retained in `conker/asm/nonmatchings/generated_1312F0/func_15103E40.s`
and the full `conker/asm/1312F0.s` slice. The owner has one function.

Recovered signature returns void and receives source, ground context,
position, mode byte, detail word, slot byte and context word. Three complete
original callers confirm the seven-argument ABI and ignore the result:
18-word `func_1506AB7C`, 18-word `func_1506ABC4`, 39-word `func_15070C40`.
The last uses either the current actor or its indexed source actor and a
three-float position copied into its own frame. Whole-ROM census finds three
direct JALs at ROM `0x9805C`, `0x980A4`, `0x9E174`, and no literal target
words. Computed references are not excluded. Caller/callee inputs are pinned.

The canonical SDK `struct17` supplies three f32 coordinates. A local 36-byte
ground view names height, nine signed vertex halfwords and the flags byte at
offset 0x1C. Narrow local helper prototypes reflect their original stack-home
loads; no global ABI declaration changes. The bounded 500..801 ground lifetime
is passed as an O32 word to its assembly consumer, which reads its low half.
Names describe observed use rather than recovered debug names.

A null source returns without submitting effects. Otherwise the function
opens the explosion, snapshots an elevated probe after that provider, initializes
the ground query, and reloads the lower Y bound after initialization. A successful
query with flag bit 0 supplies a ground-contact point, random size, byte intensity
and lifetime. Its final context argument is deliberately **zero**. The remaining
providers receive either that contact or the original position, two particle
sets, finishing effects, optional mode-dependent actor effects, fresh audio
coordinates and a final randomized burst. Mode 2 chooses IDs 0x42/0x41;
other nonzero modes choose 0x2B/0x2A. Unsigned modulo preserves RNG word extremes.
The final scale constant is the exact retail f32 `0x3FD20C49`, not rounded 1.641f.

## Closed sample-cell guard proof

The raw C body already has every retail opcode, register, binding, frame and
instruction position. Only four SP-relative sample offsets differ:

| Offset | C expected | Retail replacement |
| --- | --- | --- |
| 0xD4 | 0xE7A00054 | 0xE7A00044 |
| 0x104 | 0xC7B20054 | 0xC7B20044 |
| 0x298 | 0xE7A00054 | 0xE7A00044 |
| 0x29C | 0xC7B20054 | 0xC7B20044 |

These are the two SWC1/LWC1 pairs for F0/F18. Only the immediate changes by
-16; SP, FPRs, operation order and all other bits are fixed. Neither cell's
address escapes. Both are disjoint from the 48-byte outgoing area, saved S0/RA
at 0x38/0x3C, exported ground 0x58..0x7B, probe 0x7C..0x87, contact 0x8C..0x97
and incoming arguments. The complete access/export census rejects another
access overlapping either cell or an exposed private-cell pointer. Exhaustive
branch/delay-slot exploration visits 288 abstract states and proves every sample
load follows its store, including stores in JAL delay slots.

For the unmodified raw stream, fixtures and resulting full memory/trace state
are related by a bijection exchanging just these two four-byte cells. Original
and guarded streams compare literal physical state. Registers, FP operations,
calls, PC/delay state and all public/exported addresses stay equal; fault-state
instruction identity is normalized only at the four certified PCs. Arbitrary
invalid aliases into future callee-private storage are outside the C contract.
Raw-body SHA and every relocation fail closed. Existing CSV bytes remain an
exact prefix with precisely these four rows appended.

The retained fingerprint-locked CFE/UOPT/UGEN observation uses only newly owned
compiler children and preserves output, with child/driver completion. It observes
saved component 16, outgoing area 48, local area 88 and frame 152. Those are
compiler layout fields, not a claim about runtime timing or a saved-register
byte census. The float sample home remains a proved compiler allocation choice.

## Focused qualification

Primary and isolated sibling-overlay tools each pass the same five-test suite
before and after installation:

- 420 independent cases per original/raw-C/guarded stream: source/query/flag
  gates, effect modes, unsigned RNG boundaries, finite float rounding, helper
  mutations and guest-only incoming-home overwrites. Raw code is executed as
  emitted, with only the private memory relation described above.
- 308 access-fault prefix triples and six effective instruction negatives.
  Normal paths cover 197 body words. The unreachable move at word 92 and
  four unsigned-to-float correction words 185..188 remain byte-checked with
  all 202 words and the two alignment NOPs. Fault prefixes qualify guest
  instruction order; the numerical model does not emulate FCSR or hardware.
- 377 actual SDK32 C cases each at O0/O2/O3, strict aliasing, UBSan and
  float-cast-overflow checks, with nine executed source negatives per profile.
  Independent Python snapshots serialize provider order, argument words,
  ground vertices and retained local/public vectors. Native byte accessors
  avoid float/integer aliasing, the Linux entrypoint aligns its stack, and
  retained local pointers are used only during the root function's lifetime.
- The C language leaves the two integer RNG argument evaluations unordered.
  GDB confirmed GCC's reverse ordering at the ground call. The native reference
  therefore accepts either of two complete independently derived ground payloads,
  while preserving the same RNG stream and provider mutations; it does not mix
  individual fields from the alternatives. Exact retail RNG order is established
  by the actual IDO object and guest tests. This is an explicit portability
  boundary, not a claim that arbitrary compilers emit retail behavior.
- Six independent GNU relocation rebases /12 links compare all 808 body bytes;
  all raw bytes/bindings and strict-image alignment have effective corruption
  controls. All three complete original callers pass 48 scenarios per stream.
  Opaque providers remain bounded; no gameplay/hardware acceptance is claimed.

Both independent padders agree. The actual three-command generated-C Make
recipe is selected using a pure-C source fixture and equals the independent
padded object. Production processes the real CSV dependency change in
288.806 seconds. All 6,051 function bodies/addresses and the entire
linked ELF remain byte-identical. All 189,088 protected data bytes in 720
owners stay exact, with no image exclusions or symbol permutations. Every
other frozen input is unchanged. `make tools-check` passes.

Production ELF SHA256:
`9b320fb779551fc6177517b4112c16729369e7cdc4180cb111961a43161d2c91`.

The real dirty `64CBFD Tools` sibling retains its HEAD, raw status and 343
dependency hashes. The 920-file overlay contains 339 matching
sibling files, 575 primary fallbacks, five task files and one empty bootstrap.
Both installed suites import identical bytes apart from that bootstrap.

Root README receives aggregate conversion/matching rows only. Five concise
indexes link here. Graphify's native update refuses shrink; a scoped five-file
AST merge retains old IDs. The literal manifest reference and historical
heading IDs are sealed only after the consumer hook's observed producers exit.
This is not a full-corpus extraction. Ignored evidence and resume checkpoint:
`conker/build/game-ground-explosion-15103e40-private/`.

Routine work used zero Claude calls. Host-port source and frozen Release
remain untouched; decomp matching does not establish host gameplay behavior.

## Next

The graph and live ELF confirm all four converted functions in adjacent
`conker/src/game/generated_131620.c` already match: `func_15104170`,
`func_151041E4`, `func_1510448C`, `func_151044F4`. Preserve them. Next inspect
the 48-word ASM slot `func_15104520` in `conker/src/game/generated_1319D0.c`,
VA `0x15104520..0x151045E0`, ROM `0x1319D0..0x131A90`. Its current original
assembly bytes match; a C conversion still needs its own semantic/ABI gates
and a fresh denominator. Original assembly: `conker/asm/1319D0.s`.
Preserve the sound routines and the older private 591-word `func_150BBB5C`
candidate. The full 85% matching goal remains active.
