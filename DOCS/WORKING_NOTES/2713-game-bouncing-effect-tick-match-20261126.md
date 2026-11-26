# Bouncing effect tick match - 2026-11-26

`func_150DB114` replaces its zero-return placeholder in
`conker/src/game/generated_108320.c` with a semantic status-returning update.
All **113 linked words / 452 bytes** match the original, with **frame zero,
eight relocation positions and zero instruction guards**. VA
`0x150DB114..0x150DB2D8`; ROM `0x1085C4..0x108788`. There is no alignment
tail, insertion, omission or compiler-profile change. All five complete
neighbor bodies/bindings and the entire word-guard manifest are unchanged.

Production: **4,692 / 5,528 (84.88%) total**, **4,019 / 4,855 (82.78%) Game**,
Init 492/492, Debugger 181/181, zero drift and 836 still different. One new
matching function; no new dispatcher, pool-helper or host matching credit.
**Seven more accepted matches reach 85%.** Conversion rows and denominators
remain unchanged. The wider goal remains active.

The recovered signature is `s32(BouncingEffectOwner150DB114 *)`. The measured
partial owner is 316 bytes, including a 44-byte motion block at 0x110.
Velocity X/Y/Z occupy 0x110/0x114/0x118; scale/rate 0x11C/0x120; stretch Y/Z
0x124/0x128; stretch velocities 0x12C/0x130; damping 0x134; unsigned fade step
0x138. World position is 0x34/0x38/0x3C, output sizes 0x2C/0x30, and unsigned
alpha 0x5C. Retained bytes are preserved. These descriptive type/field names
are inferred from measured behavior, not recovered original source names.

The body captures damping and alpha, damps all three velocities, then adds
velocity times the mutable float delta `D_800BE9A4` to position. Each stretch
factor advances using its own velocity and the current delta, clamps above
1.2 or below 0.8, and reverses only its associated velocity on a clamp.
Scale then advances using its rate and the current delta, and supplies both
size products. Alpha subtracts the unsigned fade byte through a signed-halfword
local. A negative result writes zero and returns zero; equality at zero writes
zero and still returns one. The retail repeated delta reads and ordered FP
operands are preserved.

The exact literal bits are `3F99999A`, `3F4CCCCD`, `3F4CCCCD`. The original
12-byte unit at `D_800A0BE4/BE8/BEC`, ROM `0x2456A4..0x2456B0`, is checked
against the ROM and frozen ELF. Its next word is nonzero `3F360B61`. IDO's
compact object owns those three literals followed by four zero alignment
bytes. Those alignment bytes must never replace the next original value.

The raw C body differs at two unrelocated words, offsets 0xD4/0xD8, solely
because the compact literal references use addends 4/8. Thus raw byte identity
is **not** claimed: 111 raw instruction words already agree; all 113 linked
words agree. `check_bouncing_effect_150db114_pool.py` checks exact literal
bytes/order/padding, section flags, complete raw-body hash, all bindings, and
exclusive pool ownership. It transfers only the six literal relocations to
the original three independent symbols and their two LO16 addends to zero.
No opcode, register, branch or non-relocation operand changes. Both padders
then receive the canonical symbolic compact owner. Original data supplies the
literals; the temporary compiler pool is discarded.

A first single-base binding passed the fixed retail link but failed a signed
low-half carry stress test: reordered same-symbol HI/LO pairs associated one
upper address incorrectly. It was rejected before installation. The final
three-symbol binding passes all 20 GNU links, including a pool straddling
0x8000. The owner-specific US Make rule runs the ordinary O2/g3 compilation,
checked binding, assembly, unchanged generated padder and final assembly.
Five actual Make commands reproduce the complete qualified owner without
diagnostics. The shared padder implementations are unchanged.

The aligned ROM census finds one target pointer at `0x22E79C` and no direct
J/JAL pattern. It is selector 9 of the 42-entry `D_80089CB8` table. The complete
195-word original `func_1513CFE4` passes the owner in A0 at JALR `0x1513D058`
and consumes V0 at `0x1513D064`. Zero requests expiration. Its 32-byte frame,
saved owner, saved expiration byte and unsigned selector are qualified with
the actual instructions. Table bytes and parent body match the original ROM
and frozen ELF.

Validation:

- Guest: 2,256 cases per each of five literal instruction streams; 193 access
  fault-cut quintuples. Full memory, GPR/FPR, HI/LO, FCSR, access order and saved
  ABI state agree. All 111 reachable words execute; the two unreachable
  duplicate words at 0x150DB250/0x150DB2CC remain byte-qualified. Cases include
  clamp neighbors, unsigned alpha/fade boundaries, four rounding modes, signed
  zero, small finite values, mutable-delta aliases and stack-adjacent owners.
  This is a bounded finite FP model, not an N64 hardware claim.
- Native: the actual recovered C and independent reference execute in two TUs
  with a typed 316-byte owner / 44-byte motion block. All 8,192 cases pass at
  O0/O2/O3 with strict aliasing, strict FP, UBSan traps and LTO ABI checks.
  Complete owner/canaries, delta, return and MXCSR agree. Seven semantic
  controls complete and fail comparison with exit 42; no trap/signal is
  credited as a successful control. Invalid pointers and hardware NaN/trap
  behavior are outside this native qualification.
- Caller: 5,120 cases per stream, 1,280 connected child calls per stream, with
  full original parent execution on the selected active/lifetime paths. The
  independent child reference checks memory, FP state and return at the real
  return boundary. Two return poisons and an inverted consumer complete and
  change expiration. Other selected callbacks, alpha-fade modes and texture
  animation paths remain unqualified; the final free provider is opaque.
- Both scoped padders expose 226 word corruptions and 16 binding corruptions;
  18 wrong-pool/section controls reject. Twenty GNU links and 100 guest rebases
  cover independent upper-address carries. Oversize remains visible in the
  generic padder and is rejected by the generated padder.
- Independent frozen-old-C plus original-ASM prediction equals the complete
  private and production ELF. Exactly 400 ELF bytes change, with zero
  exclusions. All 189,088 protected Game-data bytes across 720 owners remain
  unchanged. Production ELF SHA-256: `c6c925de5dd93f7965725ebca607596d75a7e90be492ac93ec892b926d9718ec`.

| Phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 293.191 s | 5 fresh / 0 reused |
| preinstall-sibling | 262.296 s | 5 fresh / 0 reused |
| installed-primary | 257.265 s | 5 fresh / 0 reused |
| installed-sibling | 269.221 s | 5 fresh / 0 reused |

The 20 target tests above were fresh against the archived initial Makefile
and manifest. Final review then restored two unrelated pool-check recipes
accidentally caught by a broad private text replacement. The target recipe is
byte-identical. Source, raw target words/bindings/literal pool, all five raw
neighbors, the complete padded owner and full ELF remain qualified unchanged.
Whole compact-object file identity is not claimed. Both restored recipes
also have actual Make argv equal to the frozen baseline. After the correction,
the owner/Make/independent-image check runs fresh in both tools copies; four
unchanged semantic checks per copy are explicitly reused from the archived
installed receipts. Final manifests and all task fingerprints agree across
copies. No prior report is rewritten.

| Final Makefile scope check | Elapsed | Evidence |
| --- | ---: | --- |
| Primary | 83.081 s | 1 fresh / 4 semantic reuses |
| Isolated sibling | 85.359 s | 1 fresh / 4 semantic reuses |

The corrected manifest is committed before the consumer. Shared tools-check passes;
unchanged broad suites are not reported as fresh. Frozen inputs:
3910; snapshot entries: 2842. The isolated
sibling uses 2229 immutable dependency links
and ten independent task files, preserving the independently dirty real sibling.

Baseline consumer `d573176b3b69f6cc197dd682521e8b9faa26197c`.
Tools commit `24342ae8faba8033e6035b5287e6c471d0eeb65a`.
Receipts: `conker/build/game-bouncing-effect-tick-150db114-private`.
The historical generated host target is an empty stub; active host applicability
is unqualified. No host transfer/build/launch, Release change, push, hardware or
gameplay acceptance. Zero Claude calls and no subagents for this function.
Scoped Graphify refresh audits all six current owner definitions, retains old
IDs/qualification metadata, and observes actual commit-hook termination before
publication. README receives aggregate/date rows only.
