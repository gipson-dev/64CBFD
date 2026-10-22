# Dual-Preset Effect Start Direct C Match

Date: 2026-10-22

## Result

Recover `func_1519E3BC` in `conker/src/game/generated_1CA420.c` from its
zero-return placeholder. Complete C emits **42 words, a 40-byte frame and
four call bindings**, byte-exact without guards. Normal O2/g3, no inserted
instructions, dummy locals, assembly transplant or shared-header changes.

VA1519E3BC..1519E464 / ROM1CB86C..1CB914, ends exclusive.
Preserve `conker/asm/1CA420.s`. The old body was 12 bytes in a 168-byte slot.
One additional exact match, with the converted-C count/denominator unchanged.
Raw unlinked body SHA-256:
`e95175477d503cd2e1d82d7b7b18591b55cfe01084a38d5980d70b18443851a8`.

Keep the address-based public name and descriptive purpose/parameters.
Recover `void func_1519E3BC(u8 *actor, s16 duration, u8 slot, s32 context)`
and add only the canonical `void func_1519E688(void);` declaration. The
existing factory declaration remains unchanged. Do not type or replace the
still-unfinished `func_1519D030` placeholder during this conversion.

## Recovered Contract

Reset the effect group, then submit both preset requests in order:
`(actor,3,300,0,slot,context)` and `(actor,4,300,0,slot,context)`.
Ignore both results. A NULL actor does not suppress either call.
Finally call the controller factory with
`(signed16(duration),6,-1,1,3,0,low8(slot),context)`.
The four call relocations are R_MIPS_26 at offsets0x18/0x3C/0x60/0x90,
targeting reset, the builder twice, and `func_151491F4`, respectively.

Before reset, save RA and all four complete incoming argument words. After
each helper, reload the actor, slot byte and context from their physical
homes. The factory gets the late signed-halfword duration. Guest home mutation
tests qualify this emitted ABI, not portable C parameter-storage guarantees.
The reset has no parameters; live incoming A0..A3 are not its declared inputs.
The factory result survives naturally in V0, but the only real caller ignores
it. Do not invent a typed pointer-return API for this wrapper.

Ordinary default promotions at the unfinished unprototyped builder yield
43 words/frame48 and an extra slot spill. Explicit `(u32)slot` at both calls
recovers 42/frame40 without changing any neighbor. A typed builder prototype
can fit this target but grows its current stub from12 to28 bytes through
incoming-home stores, so it is rejected. Typed function-pointer and wide-slot
forms also fail the complete body. Historical spelling is not unique.

## Original Caller

The prepared aligned retail input has one direct JAL at ROM1CBC88 /
VA1519E7D8 in `func_1519E754`, and no aligned literal target pointer. This
is a static reference scan, not proof about every possible runtime target.
The original caller is49 words/frame40; its production body remains a stub.

Its descriptor is inline at controller+0x28: actor pointer, captured identity
at+0x2C and timer at+0x30. The actor is backed; the early empty gate tests
actor word0, not whether the actor pointer is NULL. A header-zero or identity
mismatch skips the timer/restart and requests cleanup. Otherwise add the
global timestep with 32-bit wrapping. Actor kind0x7C skips restart/cleanup.
For other kinds, a signed updated timer >=201 calls this wrapper with
`(actor,300,controller[0xC],controller[1])`.

The timer branch's delay instruction sets the cleanup flag even when restart
is skipped. Cleanup clears D_800E0920, writes0xFFFF to controller+0xE and
sets byte+0xD bit0. Exercise every original caller word over192 phases,
including timer wrap, identity/header gates, both kinds and two stack phases.
The wrapper result is ignored. No full current-caller restoration is claimed.

Two early full-suite runs failed the caller fixture: the first missed that
delay-slot update; the second still modeled an indirect descriptor. Archive
those failed receipts and count neither as acceptance. Correct the layout,
pass the focused caller check (1 test,5.761s), then rerun both full suites.

## Bounded Helpers

Original/current reset, byte-payload, dispatcher and factory wrappers are
13/12/13/28 words. Execute all their words over12 connected phases.
Reset calls the byte helper for3 and4, then dispatches NULL/command9. The
byte helper dispatches its local byte with command6; do not assert native
values for its three uninitialized alignment bytes. Dispatch forwards the
current D_800A5760 value, command2, payload address and command byte to the
bounded `func_15169260` provider. Factory forwards all eight inputs to the
bounded `func_15149130` core with its extra -1 field.

Native tests compile the actual reset/byte helper C and a bounded dispatcher
provider with a pointer-view input, not the actual native dispatcher body.
Guest tests execute the actual matching dispatcher instructions. The original
132-word effect builder is connected only for its NULL-actor gate (16 visited
words); its non-NULL construction body is not emulated. Its current12-byte
stub remains unchanged. Keep these limits separate from full effects,
allocator, hardware and natural-gameplay acceptance.

## Qualification

Tools: `experiments/game_dual_preset_effect_start.py` and
`tests/test_game_dual_preset_effect_start.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,158.217s | 8 tests,167.671s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,8.439s | 2 tests,13.002s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helper, input and complete-image identity. They are
not fresh installed executions. Both shared tools checks pass (0.311/0.288s).

- 16,384 guest phases cover all256 slots, poisoned upper bits, signed duration
  edges, helper home mutations and two stack phases; another72 use NULL actor.
  All42 root words are visited. Compare exact23 root data accesses, call
  packets and modeled GPR/FPR/HI/LO/RAM/events, including provider clobbers.
- Native32 O0/O2/O3 each pass55,296 selected-body cases with trap UBSan.
  Eight effective wrong-C controls return23 at every optimization: first/second
  preset, reset omission, signed-byte duration, flags, slot, context narrowing
  and NULL-actor call suppression. Batch selected and controls into three
  compiler invocations. The old stub fails the actual call-sequence contract.
- Six independent GNU links/12 rebased phases,184 fired root-access fault
  prefixes and five whole-image corruption controls pass. Guest fault-state
  equality is not a portable C fault/MMU claim. No guards are added or changed.
- Pin26 historical inputs plus the predecessor padded object. Preserve all22
  owner neighbors and raw/padded pools; isolated diagnostics remain empty and
  owner diagnostics unchanged. Three productive shadow Make commands reproduce
  the normal profile and padded object; skip cleanup only.

## Production

Seal15,826 live/cache files, including all1,454 linker objects. Preserve all
1,540 old mirror dirty paths, statuses, hashes and HEAD; add only two task
files, leaving1,542 dirty paths. Do not reset or commit that mirror.
Commit tools first: `33774a8de22fdd128ec11f27d48a55ac9c251e8a`. No push.
Routine Codex-only qualification uses zero Claude calls; no advisory or
provider agreement substitutes for the independent gates.

Normal Make rebuilds the owner, linked ELF and progress CSV in the verified
Linux copy (2.460s). Mark only the unchanged guard manifest old to avoid
unrelated rebuilds. Revalidate live inputs before adopting four generated
outputs. The linker script and conversion CSV remain unchanged. The inherited
duplicate `generated_12D630` recipe warning remains; this is not warning-free.

The independent full-ELF prediction is reproduced with zero exclusions:
**127 changed bytes =126 code bytes +1 target-size metadata byte**.
All other6,054 bodies, all6,055 addresses and all720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
ELF SHA-256:
`a20101cab134c884657b2297912eb50fec0deb7b75da37d3ae46a877bf60e1fd`.
Installed padded owner:
`43de87f3ff4799e73b51d43562bc987b58e47d2cc5cd1fe5e5bd7bfc3bca1565`.

## Handoff

The standard live-ELF matcher reports total **3,732/5,505 (67.79%)** and
Game **3,059/4,832 (63.31%)**. Init492/492 and Debugger181/181 remain exact.
Zero address drift;1,773 different. The75% threshold remains4,129 exact:
**397 more matches are needed**. Queue shapes:1,642 placeholders,122
semantic/other and nine unlocated entries. Next `func_151BC5A4` is screened
only, not edited or credited. Keep `func_1508CAD8`'s862-word stub queued.

Root README changes only aggregate rows. Detailed progress stays here and in
concise indexes. Post-commit graph-worker and every-old-node retention audits
remain private receipts; retain the excluded-corpus/large-HTML caveats without
claiming full re-extraction. Frozen host Release remains untouched.
