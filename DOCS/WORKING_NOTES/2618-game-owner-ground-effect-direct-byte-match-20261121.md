# 2618 - Owner ground-effect constructor direct byte match

Date: 2026-11-21. The wider goal remains **85% total exact C**.

`func_15191BE0` replaces its zero-return placeholder with the complete owner
ground-effect packet constructor. Production now matches **4,601 / 5,528
(83.23%) total**, **3,928 / 4,855 (80.91%) Game**, Init 492/492 and
Debugger 181/181, with zero address drift and 927 different C functions.
**98 additional matches** are needed for 85% at this denominator. No conversion
rows or byte-coverage denominator changed.

## Source and retail evidence

- Owner: `conker/src/game/generated_1BF090.c`; original `conker/asm/1BF090.s`.
- VA `0x15191BE0..0x15191D54`, ROM `0x1BF090..0x1BF204`: 93 words/372 bytes,
  frame `0xA8`, RA at `SP+0x2C`, no saved general registers and no alignment tail.
- The ordinary O2/g3 profile emits the entire retail body directly. Three
  `R_MIPS_26` bindings call `func_1504715C`, `func_15149130` and `memcpy`.
  There are zero guards, inserted words or omitted words. Existing Makefile,
  guard CSV, shared SDK headers and retail inputs are unchanged.
- Raw instruction SHA256:
  `d3d149898c8507d988d63ac4c428d371b4ebc0da045f1d89027d0ad9d9483759`.
- All seven other owner functions, their bindings, pools and compiler
  diagnostics are unchanged. The existing unrelated implicit-conversion warning
  is retained.

The 104-byte `OwnerGroundEffect1BF090` records the owner pointer and identity
byte `+0x3B`, a copied 12-byte position, the masked channel byte shifted by 6,
zero and two floats, a 36-byte `HeightResult71820` surface snapshot, and the
remaining float/halfword/byte settings. The surface view follows the already
recovered helper's actual layout.

The surface helper runs before later settings are loaded from argument homes.
Lifetime is signed 16-bit: exactly `-1` requests duration 300 and flag 0; every other
value, including other negatives, passes through with flag 1. The factory gets
kind 29, render 29, size 104, the priority byte and context. Its existing SDK
declaration uses the legacy `struct37 *` size token; the local declaration is
compatible with the real definition. A successful result receives the packet
at `+0x28`; the function returns the original allocation pointer across the
copy call. A null owner returns null before reading position.

The first semantic draft had the correct 93-word/frame 168 shape but 22 stack
offset differences. Declaring the result pointer before the packet restored
the original packet home `SP+0x3C` and result home `SP+0xA4`, yielding full
identity. No artificial locals, inline assembly or instruction patches were
added. Uninterpreted packet values retain offset-based names.

## Qualification and production gates

The reusable entry point is
`python3 -m unittest tools.tests.test_game_owner_ground_effect_15191be0_match -v`.
All five focused checks passed before installation and after production
rebuild, in both the primary tools checkout and the isolated sibling overlay.
Imports and non-Python data dependencies are fingerprinted; the actual dirty
`64CBFD Tools` checkout and its dependency bytes are preserved.

1. Raw C and generated padded output equal the complete retail payload and
   bindings. The natural Make recipe executes 3 commands with no membership
   override. The independently predicted whole ELF equals the actual link:
   **278 changed bytes, zero exclusions and zero metadata permutations**.
   The only declared changes are the target slot and its symbol size12->372.
   Every other linked function/address/extent and all protected GameData
   remain unchanged:189,088 bytes, 720 owners,zero different bytes/owners.
2. Guest execution covers 6,976 cases per retail/raw/padded stream, all 92
   reachable target words and the one statically unreachable word13 in the
   literal-byte check. Full RAM, private stack, registers, ordered accesses,
   return values and calls agree. Tests include all relevant narrow widths,
   null/overlapping inputs, seeded padding, helper mutations and 153 access-fault
   prefixes. 256 additional cases per stream connect the original 49-word
   factory and 11-word byte-copy loop. Four instruction controls are effective.
3. Native SDK32 runs 12,288 cases at each of O0/O2/O3 with strict aliasing and
   UBSan. Valid owner/result objects, packet offsets/extents and the exact SDK
   factory signature are checked. Seven semantic controls fail as intended.
   All defined packet bytes are compared; parent C padding is not constrained.
4. The complete 110-word retail caller `func_151925C4` is executed with all 256
   actor-type values, both null and present owners, result outcomes, lifetimes,
   helper effects and stack phases: 8,192 cases per target stream. All 18
   arguments are independently checked against immutable retail tables.
  108 caller words execute; words 9 and 40 are unreachable duplicate loads/
   assignments in the retail control flow. Skip-call and wrong-delay-slot
   controls are effective. The current caller remains an unchanged placeholder;
   this proves its original ABI, not a recovered caller implementation.
5. Six independent GNU links compare retail/raw/padded code at two code bases.
   All three target call relocations agree with independent binding. The target
   has no HI16/LO16 relocations, so no target signed-low carry claim is made.

Actual production Make and the fresh ELF recount passed. Production ELF SHA256:
`057d3b1279e8cb3ea5e0c356b8fbc1b4565bed36db9b33848de627035b586a0f`. `make tools-check` passed. The existing duplicate
`generated_12D630` recipe warning is retained separately from compiler results.
Prior unchanged neighbor suites are not described as freshly rerun suites.

Surface construction uses an explicit 36-byte write contract in target tests.
The actual surface helper and factory are already byte-exact; the current
`memcpy` is non-matching and is qualified here by its bounded byte-copy
contract, separately from original-helper execution. Guest incoming-home and
overlap probes are not portable C alias guarantees. There is no full allocator,
FCSR, hardware, emulator, gameplay or host acceptance claim.

## Host applicability and audit scope

The available sibling `64CBFDOGL` currently contains the saved scene-recompile
configuration rather than a complete host source checkout. Its N64Recomp
configuration consumes code bytes and symbols, not this C source. The saved
input does not contain this complete retail window or its prologue, and the
configured symbols file is absent. No source import or host equivalence is
inferred. Host files, builds and frozen Release artifacts were not changed.

Baseline consumer:`693c952a7d38d1ac1bde94a2098d8725c3b01372`; tools:`e818b138365f2866688a1377fc902c666ac6cf8a`.
Codex performed implementation and validation with zero advisory/model calls;
the prior Claude authentication failure was not retried. No push, ROM/save
change or broad conversion batch is included. Tools are committed before the
consumer. Graph maintenance and actual commit-hook completion are recorded
below before the final immutable checkpoint is accepted.

## Resume boundary

Inspect `func_15191D54` next in this owner, or independent `func_151BEB20` from
the remaining census. The earlier camera event `func_15096A68` remains private:
matching-length/frame drafts still differ in instruction scheduling and
saved-role lifetimes. Its detailed private handoff preserves those experiments;
none is installed or credited. Keyed history `func_15188F84`, sequence query
`func_15022024` and camera transition `func_15128030` also remain uncredited.
Handwritten decoder/stack-recovery slots must not be counted as ordinary C
conversions without their separate ABI/boundary audits.

Graph maintenance: the native update exited 1 with all
70,060 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,104 nodes / 160,823 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
