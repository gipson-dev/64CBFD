# Base color output and typed relay byte match - 2026-11-24

`void func_1513137C(s16 *red, s16 *green, s16 *blue, s16 *alpha,
register u8 *record)` replaces its zero-return placeholder with the full
**102-word / 8-byte-frame** base color selector. Every arithmetic, branch and
store instruction emits directly from C. Two checked address-binding guards
replace the private jump-table binding with the protected retail table; one
LO16 instruction addend changes from 36 to zero. There are no scheduling,
arithmetic, insertion or omission patches.

Production rises from **4,651 to 4,652 / 5,528 (84.15%)**, Game **3,979 / 4,855
(81.96%)**. Init remains 492/492 and Debugger 181/181; zero address drift,
876 functions still different, **47 more matches needed for 85%**.
Only `func_1513137C` receives additional matching credit.

Owner `conker/src/game/generated_15D730.c`; original ASM line 1204,
VA `1513137C..15131514`, ROM `15E82C..15E9C4`, 408 bytes. The fifth argument
is loaded from incoming SP+0x10 into S0; saved S0 occupies new SP+4. The
register parameter recovers that lifetime. This leaf has no calls or saved RA.

## Ordered channels and real interface

Snapshot the unsigned mode byte at record+0x70. Modes 1..8 select the eight
table entries; every other byte, including zero and 128..255, uses default.

| Mode | RGB stores | Alpha store |
| --- | --- | --- |
| 1 | Zero blue, signed halfword reload, green then red | Late (+0x2B * +0x27) >> 8 |
| 2 | Live bytes +0x24/+0x25/+0x26, red/green/blue order | Same late product |
| 3 | Live bytes +0x28/+0x29/+0x2A, red/green/blue order | Same late product |
| 4,6 | Zero alpha, signed halfword reload, blue/green/red | Alpha was written first |
| 5 | Zero blue, signed halfword reload, green then red | Late byte +0x2B |
| 7 | Live bytes +0x24/+0x25/+0x26 | Late byte +0x2B |
| 8 | Live bytes +0x24/+0x25/+0x26 | Zero |
| Default | Each live +0x24/+0x25/+0x26 times a freshly read +0x2C, >> 8 | Zero |

Every product is nonnegative and at most 65025. Halfword outputs may alias
each other or record bytes: stores can change a later component, coefficient,
alpha or mode byte. Preserve the captured selector, signed zero reloads and
the exact live read/store order. Do not cache default's scale across outputs.

The related `func_1513164C` now has a **void, nine-pointer-word interface**:
four base outputs, four secondary color outputs and one record pointer. Its
body calls the existing `func_15131514` selector first, then this selector.
Both target and relay incidental V0 values are ignored by their real renderer
caller. The old s32 return forwarding did not describe a consistent C result.
The typed relay emits its same **24 words / frame 32**, and the existing color
helper emits its same **78 words / frame 8**. Both were already byte-exact;
their additional credit is zero. Native C executes both complete semantic
helpers through the typed relay, rather than substituting a follow-up stub.

An aligned census of the entire pristine ROM finds target JALs only at
15130F6C and 15131694, and the relay JAL only at 15131018. Neither entry has
an aligned function-pointer occurrence. Current C renderer callers remain
placeholders; no other C consumer declaration needs repair.

## Two tables, anchors and full owner

The protected target table `jtbl_800A3800`, ROM 2482C0, contains eight offsets
relative to this function: **34,60,94,C8,E0,C8,FC,120** in hex. The duplicate
C8 entries implement modes 4/6. Its seven interior labels stay at their retail
addresses. The neighboring nine-entry `jtbl_800A3820` remains unchanged too.

Keep the new C definition after the existing color helper, with a typed
prototype before it. This retains the older helper's private table at offset
zero, preserving all existing guard rows and raw neighboring instructions.
The normalized private pool grows from 48 to 80 bytes: the older nine target
identities occupy 0..32 and the new eight occupy 36..64. The original pool's
padding is not claimed as immutable payload. Both sets of function-relative
table targets are independently checked against their protected ROM tables.
Only the new function's HI16/LO16 references change from `.rodata` plus 36 to
`jtbl_800A3800` plus zero. Its entire raw body and binding digest are pinned.

All **30 other raw/padded definitions**, bindings, other pools and diagnostics
remain fixed, including the typed relay. Both padders produce exact semantic
objects; their ELF metadata bytes differ and are not claimed identical.
The production/generated-padder object is the exact actual-Make reference.

## Fresh qualification

- **5,888 cases per stream**, raw C/generic/generated/retail, cover all 256
  selectors, record/output overlap, output/output overlap and incoming-home
  aliases. Every one of the 102 retail words executes. An independent memory
  model also verifies final HI/LO multiplication results. Private and protected
  tables occupy distinct addresses; only the one corresponding table read is
  mapped when comparing raw traces. All registers and memory otherwise agree.
- **372 normalized/retail fault-prefix triples** compare full state and
  dispatched accesses. Raw private-table prefixes and portable C fault
  behavior are explicitly outside that claim.
- The original **8-word direct-call window** and **16-word relay-call window**
  each pass 512 cases per stream, including stack arguments and FP delay-slot
  stores. An additional 2048 cases per stream execute the complete 24-word
  wrapper and original 78-word color helper with the target. All nine arguments,
  late argument-home reloads, frames and saved registers agree. This does not
  claim the complete renderer dispatcher.
- **5,120 SDK32 native cases plus 2,048 complete C relay cases per profile**
  pass at -O0/-O2/-O3 with strict aliasing and UBSan. A typed halfword canvas
  permits record-byte aliases and precomputed little-endian whole-canvas
  comparison. Native code does not inspect a void result. Twelve source
  controls each emit an observed comparison byte 1; signals and sanitizer
  traps cannot count as successful controls.
- All 102 words and both binding sites have 104 whole-source pin controls.
  Both padders reject eight guarded-address word/binding corruptions and
  preserve 200 non-address corruptions as visible mismatches:208 total.
  Both reject the oversized guarded fixture; no overflow output is credited.
- Four independent code/private/protected-table arrangements pass **16 GNU
  links / 96 guest runs**, including an addend crossing the HI16 carry boundary
  and negative LO16 values. Adjusted HI is shared within each arrangement so
  dead AT can be compared literally; arbitrary-placement AT identity is not
  claimed. Control/table-target equivalence is checked independently.

## Independent image, production and bank

Actual Make replays **five commands**, including asm-processor pre/post steps,
with the real -O2/-g3/MIPS2/o32 profile and reproduces the complete generated
owner. The independent image starts with frozen-before C and original target
ASM. It preserves all seven target interior labels explicitly, including the
distributed padding that occupied the old placeholder's slot, then reconstructs
every named symbol/string record from the frozen baseline. Production equals
that prediction literally: **260 changed bytes, zero exclusions**. Both
protected tables, all 189,088 protected Game data bytes across 720 owners,
unrelated objects/definitions/addresses/extents and the conversion CSV remain
fixed. The entire old guard prefix is retained and exactly two target rows are
appended. Targeted Make holds that dependency old while the changed source
forces this owner to compile; full frozen-input audits check every other output.
The live recount adds exactly one match.

ELF SHA256: `9e2116aca96e92c5d588da13f5dd7c4344125bd3522804528f00156929f253ad`.
Raw body SHA256: `45fa937ad1df5b6378007fba529811c57562285fdd2dff8fd75ef8ae85b65e5f`.
Padded owner SHA256: `3220326c726db49db3fc467fc0a390a1a2129ba12961955e611d5f199a69d7bf`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 95.647s | 5 fresh / 0 reused |
| preinstall-sibling | 122.383s | 5 fresh / 0 reused |
| installed-primary | 112.062s | 5 fresh / 0 reused |
| installed-sibling | 98.874s | 5 fresh / 0 reused |

All reported phases use final source/tool fingerprints; exploratory receipts
are excluded. Shared tools-check passes. Tools commit
`e21334d7cb34014c0f36a3fe2ffd97f8f1a93e71` precedes the source/guards/pin/docs
commit. Both tracked trees are clean at the bank and the real dirty sibling
tools checkout is preserved. No push, host/Release change or build, WSL restart
or Claude call. Graph receipts distinguish normal update, actual hook completion,
scoped AST merge, old-ID/qualification retention and current-definition audits.
The new target prototype and already-exact related functions receive zero
additional credit. This is not full-corpus re-extraction. Root README gets only
two aggregate rows; five DOCS indexes retain all previous bytes.
Keep the 85% goal active. Renderer 15197148 remains private on its older baseline.
