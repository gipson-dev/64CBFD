# Particle ring tick match - 2026-11-25

`func_150B40E8` replaces its zero-return placeholder in
`conker/src/game/generated_E1280.c`. The complete **107 words / 428 bytes**
match retail: **106 direct words and one checked integer-operand guard**.
The routine is a leaf with **no stack frame**. All four relocation positions
match. No insertion, omission, alignment padding or profile change.
VA `0x150B40E8..0x150B4294`; ROM `0xE1598..0xE1744`.

Production: **4,688 / 5,528 (84.80%) total**, **4,015 / 4,855 (82.70%) Game**,
Init 492/492, Debugger 181/181, zero drift and 840 still different. One new
match; no new parent, factory, constructor or renderer matching credit.
**11 more verified matches reach 85%.** Denominators/conversion rows are fixed.

The signed 32-bit status routine accepts one owner pointer. It captures the
owner+0x94 record table and owner+0x98 auxiliary pointer, and returns 0 when
the signed count is below 2 and auxiliary flag bit 0 is set. Otherwise it
walks backwards from signed head toward the current signed tail, wrapping
negative indices through unsigned capacity. Each record is 36 bytes.
It writes opacity 255, subtracts the integer tick delta through a signed 16-bit
lifetime store/reload, integrates vertical acceleration, then updates X/Y/Z
position and a scalar extent using repeatedly read float delta time.
Y uses the newly updated vertical velocity. Expired records may drain the
tail toward the current index, narrowing tail/count at each step and
wrapping at capacity. The final reference position at owner+0x54 comes from
the tail record when signed count is positive, otherwise three positive
zero floats. Normal completion returns 1. Retained fields remain intact.
Types describe observed prefixes/fields, not complete original structures.

The original 99-word factory 150B3F5C is already byte-exact. It requests 88
auxiliary bytes and 36-byte records, with all three dispatch selectors 7.
The original 115-word constructor 15147A80 matches ROM and frozen/live ELF:
it allocates unsigned request.count times the passed stride, stores the
auxiliary and record pointers at 0x98/0x94, copies the request prefix so its
unsigned count becomes owner.capacity at 0x25, clears ring counters, and
sets dispatch bytes 0x2F/0x30/0x31. These facts establish the partial layout.
Existing factory/constructor source, words and qualification are unchanged.

An aligned whole-ROM census finds one literal at ROM 22ECDC, VA 8008A21C,
and no direct J/JAL patterns. The complete 60-byte original table 8008A200
agrees across ASM, ROM, frozen and live ELF; index 7 names this target.
The already exact original parent 15147740 is 100 words/frame32. Its first
unsigned selector byte is owner+0x2F; JALR 151477C4 passes A0, and the
zero-result test 151477D0..D8 marks expiration. Incoming A1 is not consumed
by the leaf; its first instruction overwrites it from the signed count.
This census does not prove every possible computed indirect call.

The first semantic candidate already matched 107 words, the no-frame shape,
all bindings, and the full ordered FP sequence, but had a four-GPR allocation
cycle. Removing the redundant named count local recovered the allocation
directly. Four bounded declaration/lifetime probes are retained; reversing
the pointer declarations and moving the count capture later were worse.
The selected source has one remaining word at 0x70: `addu a3,t8,v1` versus
retail `addu a3,v1,t8`. Decoder assertions pin the same opcode/destination
and exactly swapped sources. Addition modulo 32 is commutative for all input
bits, cannot trap, and makes no memory access. Thus complete state and
memory-access order agree after every instruction. No FP operand, FCSR,
HI/LO, branch, lifetime or arithmetic association is rewritten.

Guest checks pass **2416 cases per stream across five streams**. Complete
memory, all registers/FPRs, HI/LO, return, ordered FP operands/FCSR and access
traces agree. The independent model covers capacity 1..6 and all head/tail
pairs, signed count/lifetime boundaries, narrowed delta subtraction, early
failure, expiration drains, wraps, coefficient/record/owner/auxiliary
overlaps, stack owner storage and four rounding modes. High capacities 127,
128 and 255 are covered in an explicitly finite no-drain domain. **82
fault-prefix quintuples** agree across all five streams, including raw C.
All 106 reachable words execute; the original load at 150B4118 is unreachable
after the preceding return and remains byte-qualified in the 107-word body.
Four supported instruction controls complete and reject.

Native32 runs the actual selected C body in two translation units against
an independent reference: **8192 cases at each of O0/O2/O3**, strict aliasing,
UBSan traps, LTO type checks and strict FP flags. Typed rings use valid
capacities 1..8 and allocated records; full owner/record/auxiliary arenas,
retained bytes/canaries, globals, return and MXCSR agree. Tests include
signed count/lifetime boundaries, bounded safe signed 32-bit subtraction, all
four rounding modes, finite and subnormal delta-time values. Seven wrong
C variants finish with comparison 42; a signal/trap never counts.
Arbitrary address aliases are guest-only. Termination of arbitrary invalid
ring configurations and portable C fault semantics are not claimed.

The full original parent executes **2304 cases per stream**, including
**480 connected children per stream**, through literal/raw leaves. Each
child matches the independent full-memory/no-frame/FP/status model, and
the parent agrees on lifetime expiry, invalid unsigned selector, skip,
success and failure paths. Second dispatch is zero-skipped; third is
disabled or signed -1-skipped. Three supported controls complete and change
the expiration decision. The expiration helper remains opaque; unrelated
dispatch semantics are not claimed as a new recovery.

Both complete padders preserve all nine raw/padded neighbors, literal pools
and exports (zero interior retail labels). The actual Make route uses three
commands with no diagnostics, GLOBAL_ASM or profile change. Independent
image prediction uses frozen old C plus original target ASM. Actual Make,
reference link, prediction and production ELF agree with **319 changed
bytes, zero exclusions**. All 189088 protected Game data bytes/720 owners,
unrelated bodies/addresses/extents, old guard-prefix bytes and conversion
rows are unchanged. Boundary checks reject two guard corruptions and expose
212 unguarded-word and eight binding corruptions. Twenty GNU links and 100
guest rebases cover high addresses and low-half carries. Both oversized
probes reject.

Selected source SHA256 `52a1ccab71baef3672b93952212b996464735bc9ebbfc5439ec9cbbd80b6a83c`.
Padded owner SHA256 `f1327efe8365b315d369b0c3272fd62eb3a39c3e368bfc48054f477c0a95c2cf`.
Production ELF SHA256 `ccb8e1cd60355c86885d1d0a05343af53a8df390d6bceaa1b1b96414c5d77f31`.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 101.793 s | 5 fresh / 0 reused |
| preinstall-sibling | 128.653 s | 5 fresh / 0 reused |
| installed-primary | 105.788 s | 5 fresh / 0 reused |
| installed-sibling | 111.797 s | 5 fresh / 0 reused |

All 20 final tests are fresh. The isolated second copy uses
2193 immutable dependency links and nine
independent task copies; freeze 3861 inputs /
2785 copies. Task/import/data/profile/artifact fingerprints
agree across copies, and shared tools-check passes. The real dirty tools
sibling is preserved. The native reference was simplified only by removing
unused locals; final suites cover that fixture. No selected body/profile
changed after the private qualification was sealed. The first packaged
owner check caught an assembler-path variable incorrectly replaced by C
text. The generator now selects the source assignment inside the recovery
function. Only the two owned task copies were repaired; the failed receipt,
before/after fingerprints and unchanged selected-source binding are retained
in packet-repair.json. All final suites run afresh after that repair.

Baseline consumer `d356b23af8c5e96c248078dec2a27f37f988f505`.
Tools commit `0673b7716f87d2fc3b356d9a9b41de6fd0251441`.
Receipts: `conker/build/game-particle-ring-tick-150b40e8-private`.
Read-only sibling applicability finds the known historical generated target
is an empty stub; no active host implementation was qualified/transferred.
Zero Claude calls for this routine, no subagents, host build/launch,
Release change, push or gameplay/hardware acceptance. Root README receives
aggregate rows only. Scoped graph retention audits all 10 owner definitions,
including its pointer-returning factory, retains old IDs/proof metadata and
observes actual hook writers terminate before immutable banking. The 85%
matching goal remains active.
