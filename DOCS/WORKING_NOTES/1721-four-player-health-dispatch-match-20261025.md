# Four-Player Health Dispatch Direct C Match

2026-10-25. Production-qualified, adopted and freshly recounted.

## Recovered Routine

`func_15085ABC` now replaces its zero-return placeholder with complete semantic
C in `conker/src/game/generated_B21B0.c`. Its 44 body words / 176 bytes emit
directly from the existing IDO O2/g3 profile, with frame 0x30, five original
bindings and **zero new guards**. The separate alignment word remains exact.

- Body VA: `0x15085ABC..0x15085B6C`; VROM: `0xB2F6C..0xB301C`.
- Full 45-word slot ends at VA `0x15085B70` / VROM `0xB3020`.
- Canonical interface: `void func_15085ABC(s16 mask)`.
- Use the existing `struct127 D_800CC2D0[26]`, size 0x32C, unsigned `health`
  byte at +0x1CA, and existing unsigned disable byte `D_800D18A8`.
- Capture the signed low halfword before checking the disable flag once.
  Visit slots zero through three in order, selected by the mask's low four bits.
- Read each selected slot's live health immediately before calling
  `func_15085710((s16)slot, 5, health)`. Do not prefetch future health bytes or
  recheck the disable flag after a callback.
- Preserve the full incoming A0 home, S0-S4/RA saves and lifetimes, both
  branch-likely increments and the final stack update in the return delay slot.

The natural bit-first expression `(1 << slot) & mask` recovers retail's AND
operand order without a normalization row. The bindings remain disable HI/LO
at +0x2C/+0x30, actor-table HI/LO at +0x44/+0x48, and helper R_MIPS_26 at +0x7C.

## Caller And Helper

The aligned whole-ROM scan finds one static JAL, VROM `0x46310`, and no aligned
literal target pointers. This does not rule out arbitrary computed calls.
The complete 35-word caller `func_15018DFC`, VA `0x15018DFC..0x15018E88`, is
already byte-exact. Its delay slot at `0x15018E64` loads the signed mask.

`conker/src/game_45B80.c` now supplies the local `void(s16)` declaration rather
than relying on an implicit integer-return declaration. Whole-caller compilation
preserves all 16 functions, bindings, pools and normalized diagnostics. Actual
production Make also preserves the entire caller object byte-for-byte.

The shared helper declaration is `void func_15085710(s16, s32, s32)`; the live
unsigned health byte is promoted to its full third argument. Original helper
mode five, at `0x15085840`, stores that byte at `0x800D2145 + slot * 28`.
Guest tests connect the original 167-word helper and its real 12-entry table,
visiting the 23 words on this mode-five route. Other helper modes are not
qualified here. The current helper's 12-byte zero-return placeholder remains
unchanged and receives **no recovery credit**. Refining its formals changes its
object and was rejected as outside this recovery; no incompatible new helper
prototype is inserted into the owner.

## Qualification

Both tools copies pass **ten fresh pre-install checks**, with zero errors,
failures, skips or reuses: primary 46.728 seconds, older mirror 33.047 seconds.
Both shared tool checks pass as well.

- 3,296 guest phases cover signed/high incoming mask bits, every disable byte,
  unsigned health values, live future-health changes and a callback changing the
  disable flag. All 44 target words execute across the corpus.
- Native32 O0/O2/O3 with trap UBSan cover all 65,536 masks, all 256 gate and
  health-byte values, valid canonical records and twelve effective controls.
  These are individual exhaustive axes and bounded combinations, not every
  possible Cartesian combination. Native aliases are not claimed.
- 240 full original-caller phases cover both outer gates, signed mask passage,
  nested frames and caller-saved clobbers. Outer providers are scripted.
- 96 original-helper phases exercise its real mode-five table dispatch/store.
  This is not full-provider or gameplay acceptance.
- Nine independent GNU links in three layouts cover all five bindings and
  signed-low HI/LO carries; 24 rebased phases and ten additional guest stack
  alias layouts agree in complete state.
- 178 fired target-access fault prefixes agree in complete guest state. They
  qualify emitted guest ordering, not portable C fault semantics.
- All 44 raw-word and five binding corruptions, seven strict-image controls,
  fourteen frozen/live input mutations, a stale installed object and the old
  target stub are rejected.

Whole-owner compilation, the ordinary padder and actual three-command Make
shadow preserve seven neighbors, addresses, extents, pools and the alignment
word. Original assembly, shared headers, profiles and the full guard CSV are
unchanged. The caller's three existing Warning 712 pointer/integer diagnostics
and the duplicate `generated_12D630` Make recipe warning are retained.

The first stack-alias fixture used implicit text alignment and read a leading
padding word; it was corrected to explicit `SUBALIGN(4)` placement without
changing the C. A private Windows-to-WSL runner path was also corrected before
its tests ran. Failed receipts remain separate and are not counted as passes.
Transient Git index locks cleared without deleting locks or stopping unrelated
processes. The final tools commit is scoped to the two tested tool files.

## Production And Adoption

Actual production Make passes in 23.296 seconds and reproduces the strict
**142-byte** independent whole-image prediction: 141 code bytes and one
symbol-size byte, from 12 to 176, with zero exclusions. All 6,054 other linked
bodies and all addresses remain fixed. Protected Game data is exact across
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each copy passes **two fresh installed checks plus eight fingerprinted semantic
reuses**, not ten fresh installed tests. Reuse requires the same complete sealed
inputs, module hashes and seven qualified artifacts, plus literal installed
source, typed caller, target object and ELF equality.

Base qualification tools were banked as `5fcd50fdaa0a39e572c2cade76b1191f5de4a2ad`;
the typed-caller refinement is `ab2eb2e8621bca0d94f1ba9f885d3b3c5a385bab`.
Both precede the consumer commit. The older mirror's 1,652 captured dirty paths
and HEAD are preserved, with only two owned module additions and no mirror
commit, reset or stash. Nothing is pushed.

Native adoption verifies all 16,050 captured files with exactly four explicit
overrides: target source, caller source, target object and ELF. The caller
object is not mutable. The actual adopted Native ELF is streamed without
DrvFS to the fresh GNU recount and equals the independent image:

`f9ac9d10164b603e7a77f0d8018f97b54ec1ef3c67211f3ad15e118b911f4e1d`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,797 / 5,505 (68.97%) | 0 | 1,708 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,124 / 4,832 (64.65%) | 0 | 1,708 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Only `func_15085ABC` leaves the remaining-function queue. Converted totals are
unchanged. The 75% threshold remains 4,129 / 5,505, requiring **332 more exact
matches**; the wider goal remains active. Triage now has 1,579 placeholders,
120 semantic/other definitions and nine parser-unlocated entries. These are
source-shape screens, not additional qualifications.

## Handoff

Next ordinary placeholder: `func_150A2FA4`, owner `generated_CDE80`, 45-word
retail slot. No candidate is installed or credited from that queue entry.
Qualify its actual caller/helper ABI, complete semantics, native/guest behavior,
owner/padder/Make, image and adoption before another count change. Keep existing-C
`func_15014094` and parser-missed `Gfx *func_1510D8C0` separate.

Local receipts remain under ignored `conker/build/game-four-record-mask-dispatch-match/`.
The current helper, complete providers/gameplay and host behavior remain open.
No host/Release artifacts, packages or global configuration were changed;
Claude calls are zero. Root README changes are aggregate match rows only.
