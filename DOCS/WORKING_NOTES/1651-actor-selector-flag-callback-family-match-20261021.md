# Actor Selector Flag Callback Family

Verified: 2026-10-21. Consumer predecessor `1f85b028`;
active tools predecessor `4d6f908`. Tools committed first as `55e5533`.
The wider 75% C-matching goal remains active.

## Targets And ABI

Replace three adjacent zero-return placeholders in
[generated_1048D0.c](../../conker/src/game/generated_1048D0.c),
retaining their address-based names and adding typed arguments/purpose comments.

| Function | VA Span | ROM Span | Words |
| --- | --- | --- | ---: |
| func_150D7420 | 150D7420..150D74DC | 1048D0..10498C | 47 |
| func_150D74DC | 150D74DC..150D758C | 10498C..104A3C | 44 |
| func_150D758C | 150D758C..150D7630 | 104A3C..104AE0 | 41 |

All three use `void (u8 *actor, u8 *event, u8 command)`, frame0,
zero relocations and zero new guards. The existing typed callback table in
[game_16DC80.c](../../conker/src/game_16DC80.c) already declares this ABI.
Slots **12/13/14** of `D_8008A02C` select these routines. Pristine aligned
ROM scans find only their literals at **22EB1C/22EB20/22EB24**, VA
**8008A05C/8008A060/8008A064**, and no direct JAL to any of them.

The complete caller `func_151416E8` is **55 words**, frame24:
VA **151416E8..151417C4**, ROM **16EB98..16EC74**.
Its current linked C is already byte-identical to the original
[func_151416E8.s](../../conker/asm/nonmatchings/game_16DC80/func_151416E8.s).
It reads actor +0x168 for the table slot, bypasses NULL callbacks, calls at
**15141734** and reloads its command instead of consuming the leaf's
incidental v0. Do not retain the false integer-return placeholder signature.

## Semantics And Direct Fit

Every entry stores the full incoming command register in its SP+8 home
before masking the low byte. Only command **0x36** reads event[0] and
updates the actor. For other commands, neither actor nor event is accessed.
Do not invent NULL, actor-state or selector validation.

The affected fields are the full 32-bit word at +0x58 and three bytes
at +0x28/+0x29/+0x2A. This note describes the measured flag/byte operations,
not a proved gameplay interpretation of those fields.

- func_150D7420: selectors 1/2 set bit1 and bytes (255,0,0).
- func_150D74DC: selector 2 sets bit1 and bytes (255,0,0); selector 1 clears bit1.
- func_150D758C: selectors 1/2 clear bit1.
- All three: selector 3 sets bit1 and bytes (0,255,0).
- Selector zero and every other byte clear bit1 without changing the byte fields.

The selector is read before all field writes. Preserve every other flag bit
and every opaque byte. Source groups case0 with default, keeps cases1/2
separate and places the bit-set expression before the byte stores.
Normal O2/g3 then emits all **132 words / 528 bytes directly from C**.
No compiler-profile changes, register bindings, inserted words or guards.

The initial explicit-zero-case source is 44 instead of 41 words for
func_150D758C. Grouping zero/default restores its extent but leaves five
allocation differences. Moving the bit-set expression before the byte
stores closes them naturally and also directly matches the adjacent variants.
Do not collapse the family into a shared helper or simplify the source shape
without requalifying the original binary layout.

Raw SHA-256 values, also equal to the relocation-free pristine ROM bodies:

| Function | SHA-256 |
| --- | --- |
| func_150D7420 | ec9480cd4f6a3619374bcadf7e04eaab158e903b22a1ec4a79c7de3d8285d469 |
| func_150D74DC | 6a449956418ab2151a459929fe28f771d9ee02b80d4d0ca4581f04a517c042c7 |
| func_150D758C | 57b44ddc4413b32ee8e4bb5be76e8430293e5138f814e878a93775141fd0f56a |

## Tests And Boundaries

Each actual tools copy passes all eight tests before installation:
primary **257.272s**, older mirror **207.548s**, no failures/errors/skips.
Each copy passes two fresh installed tests, **2.190s / 2.059s**.
Explicitly reuse the other six under unchanged source/object/helper/image
identity; do not describe them as fresh installed tests.

- 12,288 leaf phases, all selector bytes, command narrowing, full flag widths and exact accesses.
- 198 guest event/home alias phases, including the full incoming register word at SP+8.
- 387,072 native32 cases per optimization at O0/O2/O3 with trap UBSan.
- Typed fenced actor projections and valid character aliases, plus the actual C parent.
- Eight compiled wrong-C controls effectively rejected; all three old stubs rejected semantically.
- 512 complete dispatcher phases across slots0/12/13/14, including NULL bypass.
- Eight observed helper packets to func_1516972C, modeled as an opaque void boundary only.
- Eighteen independent GNU original/C links and 270 rebase phases.
- 186 fired leaf access-fault prefixes, including home and return-delay stores.
- Nine corrupt complete-image controls, all 26 historical/current pins and the old padded object.

Each leaf has one unreachable duplicate load, at **150D74C4**, **150D7574**
and **150D7618**. All 132 words are reproduced statically; natural execution
visits **129**, not 132. The caller similarly visits **53 of 55** words:
its branch and delay at **15141790/15141794** are unreachable under its
earlier command gates. Do not force PC entry and call it normal acceptance.

Native fixtures use aligned typed fields with character views, not unaligned
word overlays. Guest incoming-home aliases/fault prefixes are not portable C
fault semantics or hardware MMU evidence. The opaque helper's implementation,
other callback slots and gameplay acceptance remain unclaimed.
Both shared tool smoke checks pass. Routine work uses zero Claude calls.

## Owner, Production And Preservation

Freeze **26** source/header/assembly/data/layout/build/image inputs and the
old padded owner object, SHA-256:
`1986734cc845ec5722487fe02e2ef1326e74074154750b4497083d5f85f7b360`.
Preserve all **four** raw/padded neighbors and all pools.
Retain both GLOBAL_ASM routines, func_150D765C and func_150D7790.
The three target symbols grow from 12 bytes each to **188/176/164**.

The actual five-command owner Make profile reproduces the qualified raw
functions and padded object. Production runs the actual Make recipe in the
retained Linux-local workspace, after a fresh **15,773-file** live/copy
identity audit. Rebase only the previously qualified source/object/image
delta, add the four absent task-tool copies, and explicitly pin the current
ELF in the refreshed manifest. Do not blindly reuse the previous snapshot.

Production exits0 in **0.748s**. Keep the unchanged guard manifest marked
old to avoid unrelated timestamp-triggered rebuilds. The inherited duplicate
generated_12D630 recipe warning is unchanged.
Fresh installed audits and complete static-input/non-target-object checks
pass before generated-artifact adoption.

The independent first link and production ELF agree on every byte:
**393 changed bytes = 390 instruction bytes + three symbol-size bytes**,
**zero exclusions** and no metadata permutation.
ELF SHA-256:
`49a97dece304461d1fe1b5aec743b2fcaf8c5400a0635fd8aafca87dae3f5dc0`.
Production owner SHA-256:
`4d4a89cb478a4a3a794bd3dba7b1df75a16a344382f5e67a09066c5fb6a81eb1`.

Preserve **6,053 other linked bodies**, all **6,056 addresses**, the entire
guard manifest and **189,088 protected Game-data bytes / 720 owners**.
Data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The full live input check passes again before/after adopting only qualified
generated artifacts and receipts. The literal standard matcher then runs
against the actual live consumer ELF, not just the Linux copy.

Fresh results: **3,718/5,505 total (67.54%)**, **3,045/4,832 Game (63.02%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,787 different**.
Converted counts/bytes are unchanged. The 75% threshold is **4,129**,
leaving **411**. The refreshed queue contains **1,654 placeholders,
124 semantic/other bodies and nine unlocated entries**; screens are not
C/ABI qualification.

Preserve all **1,514** previous older-mirror dirty statuses/hashes and its
`ddbdd16` HEAD; add only the two absent task files, reaching **1,516**.
Never commit/reset/stash/clean that mirror. Active tools are committed first;
the consumer source/docs/pin checkpoint follows. No push.
Root README changes only two aggregate rows. Host builds/source, real
saves/configuration and frozen Release remain untouched.
After committing, wait for both owned Graphify workers and verify the commit
stamp plus old/excluded-node retention. Keep the 75% goal active.

## Next Function

Next is `func_15174AA4` in
[generated_1A1E50.c](../../conker/src/game/generated_1A1E50.c):
VA **15174AA4..15174B48**, ROM **1A1F54..1A1FF8**,
**41 words / frame40**, still a zero-return placeholder.
Retail SHA-256:
`cca542092f9d5b40f7cb4950b801da3973477a73f45f4fb4d63314c5c5204841`.

Static assembly emits PipeSync and matrix commands, reads the byte at
D_800B0DF0's pointee +0xC, optionally dispatches through D_8008CD74,
then emits the matrix command again and returns the advanced cursor.
Determine the real caller/return ABI, unused argument, callback packet,
saved matrix-address lifetime, aliases and SDK macro shape before choosing C.
This is a queued screen, not a draft, installation or matching credit.
Keep func_1508CAD8 queued.

Receipts: `conker/build/game-actor-selector-flag/qualified/`.
Retained workspace: `/tmp/cbfd-two-range-sealed-my0624sa/64CBFD`.
Reverify every next delta and live input/output identity before reuse.
