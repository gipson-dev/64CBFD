# Pointer-input quad vertex writer match - 2026-11-26

`func_150DB714` replaces the zero-return placeholder in
`conker/src/game/generated_108320.c` with a typed four-vertex writer reading
live position, angle and extent pointers. **178 words / 712 bytes, frame 88,
seven relocation positions** match after **20 expected-word guards**;
158 words emit directly from C. The original 179-word slot retains its one
NOP tail. VA `0x150DB714..0x150DB9DC`, ROM `0x108BC4..0x108E8C`.
No insertion, omission, compiler-profile or Makefile change. All five raw and
padded neighbors and all pools remain unchanged. The existing N58 literal
binding checker still runs unchanged before both complete padders.

Production: **4,694 / 5,528 (84.91%) total**, **4,021 / 4,855 (82.82%) Game**,
Init 492/492, Debugger 181/181, zero drift and 834 still different. One new
accepted match; **five more reach 85%**. Conversion rows and denominators
are unchanged. No additional caller/helper/host matching credit.

The recovered ABI is `Vtx *(PointerQuadOwner150DB714 *, s16 view)`.
The measured partial owner is 292 bytes, with a 64-byte four-vertex template
at 0xC0, four buffer pointers at 0x100, and five input pointers at
0x110/0x114/0x118/0x11C/0x120. They identify XYZ position, angle, half width,
half height and alpha. Alpha is unused here; the matched updater uses it.
These descriptive names and partial types are inferred, not original names.

The buffer helper receives size 64, the signed view and two output pointers.
The leaf captures its first returned cursor separately, returns null immediately
on failure, and copies the retained template to both pages only when fresh.
It reloads the chosen buffer pointer after the first copy. The angle is
multiplied by the pinned float `D_800A0BF0 = 0x3F360B61` (rounded 256/360),
then truncated. Two byte-angle calls use the low byte of that result and its
quarter-turn subtraction. Unsigned low-word subtraction retains defined C
wraparound. Their returned floats scale the live width source into horizontal
and negated depth components. Four corners use signs X `+,+,-,-`,
Y `+,-,-,+`, Z `+,+,-,-`; every coordinate truncates and narrows into the
vertex halfword. Flags clear, UV/colour remain retained. The originally
captured cursor is returned even if copying redirects the live output cursor.
Input pointers remain live across helper calls and output writes.

S0/RA save at SP+0x20/0x24. Freshness is SP+0x37, phase SP+0x48,
first pointer SP+0x50, cursor SP+0x54, in the matching 88-byte frame.
No dummy local, physical-register declaration or artificial instruction is used.

The guard derivation checks the complete decoded raw stream. Thirteen LW
instructions use modular O32 identities `s0+0x110+field == v1+field` while
S0 and the derived V1 address remain invariant. One pure address initializer
moves across eight instructions independent of V1. This reproduces every
retail word without changing memory access order, FP opcode/operand order,
bindings or source alias assumptions. All 20 guards are unrelocated; the old
guard prefix is preserved. V1 is still read near the end; it is not dead.
Completed private state agrees. Raw access-cut private GPR and EPC identity
inside the moved block is not claimed; public memory, access trace, calls,
FP operations and FCSR agree. The four normalized literal streams additionally
agree on full private state at every tested fault cut.

The target is index 8, ROM pointer `0x22E8FC`, in the 39-entry
`D_80089E1C` table. The entire table and boundary match ROM/frozen ELF.
The complete original 295-word/frame-144 `func_1513DB00` passes owner and
narrowed signed view through JALR `0x1513DC24`, then consumes the pointer
at `0x1513DC30`. Null triggers free/skip. **Its production C remains a
zero-return placeholder**; original-caller qualification is separate from
restoration or gameplay integration. The original 52-word buffer helper,
11-word copy loop and 27-word byte-angle helper receive no new credit.
Angle-helper ROM/frozen ELF, all 65 cosine table floats and the coefficient
are pinned independently; its existing C prototype is `f32 func_151423D8(u8)`.

Validation:

- Both complete padders produce the same qualified owner; all five neighbors
  and pools stay fixed. The existing actual five-command Make recipe produces
  that same owner with zero diagnostics.
- Guest: 1,088 cases per each of five streams, all 178 target words executed,
  and 735 access-cut quintuples. Independent public memory, calls, ordered FP,
  FCSR and pointer-return reference agrees. Completed full private states
  agree. Tests include signed views, null/fresh paths, pointer and pointee
  mutation after angle/copy calls, cursor/return-home changes, bounded aliases,
  and all four rounding modes. Original buffer, copy and angle routines also
  execute separately and together. Allocation remains opaque; finite FP model
  and guest private-home/alias cases are not portable-C or N64 hardware claims.
- Native: actual selected C in three TUs, typed 292-byte partial owner,
  16-byte vertices, live float input aliases and separate providers. All
  16,384 cases at O0/O2/O3 pass with strict aliasing/FP, UBSan traps and LTO
  type checks. Full owner, two buffers, input storage, canaries, provider
  metadata, return and MXCSR agree. Four rounding modes execute. Negative
  views use the null path and float-to-s32 cases remain in range. Seven
  deliberate errors complete with comparison exit 42; no trap or compiler
  failure counts as a semantic rejection. The coefficient fixture uses exact
  pinned bits, avoiding rounding-mode-dependent fixture division.
- Caller: 306 complete cases per original/raw stream with 144 connected
  children, independent semantic-provider counterpart, signed forwarding and
  null return consumers. All 293 reachable parent words execute; duplicate
  default indices 115/146 remain unreachable. Hiding/inventing the leaf's
  return changes complete-parent behavior. Render services/free are opaque;
  semantic-provider private stack identity is not claimed.
- Both scoped padders reject all 40 guarded-word corruptions and expose
  316 unguarded-word and 14 binding corruptions. Twenty independent GNU links
  and 100 guest rebases cover jump regions and coefficient HI/LO carry seams.
  Both reject oversize input. There are no guarded bindings.
- Independent frozen-old-C plus original-ASM prediction equals the entire
  private and production ELF: **508 changed bytes, zero exclusions**.
  All 189,088 protected data bytes across 720 owners remain unchanged.
  Production ELF SHA-256: `375a351b620738f1072e77f2920d1b5ae34e21da1ab801b67cb6dafd24701ec1`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 170.294 s | 5 fresh / 0 reused |
| preinstall-sibling | 148.706 s | 5 fresh / 0 reused |
| installed-primary | 128.102 s | 5 fresh / 0 reused |
| installed-sibling | 128.22 s | 5 fresh / 0 reused |

All 20 packaged target tests are fresh, with matching task/import/data and
source fingerprints across primary and isolated sibling copies. Shared
tools-check passes. Unchanged broad-suite receipts are not reported fresh.
Frozen inputs: 3937; snapshots: 2869.
The independently dirty real sibling remains intact. Tools commit:
`f4a0d9a202b5daed3d1e74b3ca985653fa255d67`. Baseline consumer:
`c0fab8538eb5fa8622ad319bb3aa9ee0e2c44b1f`. Receipts:
`conker/build/game-pointer-quad-vertices-150db714-private`.

Claude completed one tools-disabled, packet-only Sonnet advisory review after
login recovery. An initial `--bare` attempt rejected OAuth locally with zero
API tokens; corrected invocation retained the explicit tool/MCP/hook limits.
Its broad address-formation finding was independently checked. Its claim that
V1 was dead was rejected using actual late reads; unsupported global-alias
assumptions were rejected. The selected expression form preserves pointer
read order and needs no load swap. A mistaken extra swap was rejected by
complete-word identity before packaging. Review grants no matching credit.
No subagents. Earlier count and native-fixture experiments were corrected
privately before sealing; no rejected candidate was installed or credited.

The historical generated host target is an empty stub; active host applicability
is unqualified. No host transfer/build/launch, Release change, push, hardware
or gameplay acceptance. Scoped Graphify refresh audits all six owner
definitions, preserves old IDs and prior qualification metadata, and observes
actual commit-hook termination before publication. README receives only
aggregate/date rows. The 85% goal remains active.
