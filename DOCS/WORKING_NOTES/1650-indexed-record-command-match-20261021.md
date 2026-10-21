# Indexed Record Commands

Verified: 2026-10-21. Consumer predecessor `00cf47f6`;
active tools predecessor `62ce8ef`. Tools committed first as `4d6f908`.
The wider 75% C-matching goal remains active.

## Target And Semantics

`func_150A02D0` in
[generated_CD5A0.c](../../conker/src/game/generated_CD5A0.c):
VA **150A02D0..150A0374**, ROM **CD780..CD824**,
**41 words / 164 bytes**, **frame0**. Replace only its zero-return
placeholder, previously different at 39 words, retaining the address-based
name, existing 12-byte record type and a purpose comment.

Recover `s32 func_150A02D0(u32 index, s32 command, const s32 *payload)`.
Commands 0/1 set/clear status bit 0x40 at `D_800D3010 + index*12`,
using one byte load/store and preserving every other bit. Command 2 loads
the complete word at payload +8 before storing to
`D_800D3014 + index*12`, the retail record's +4 value member.
Recognized commands return one; every other full-word command returns zero
without accessing memory. Do not invent active-state, index or NULL checks.

The two globals name overlapping parts of the retail table, not unrelated
state. Keep the already established D_800D3014 spelling from the adjacent
accessor, and independently qualify its relocations. Native tests use
bounded, aligned declared record objects and a separate typed payload.
Guest wrap/alias/fault cases are not portable invalid-pointer C claims.

## Both Actual Dispatch Paths

The aligned pristine image contains one function-pointer literal:
ROM **22CFBC**, VA **800884FC**, slot **10** of `D_800884D4` in
[22BEF0.rodata.s](../../conker/asm/data/22BEF0.rodata.s).
There is no aligned direct JAL to this target.

Execute the complete **92-word** retained-assembly caller
[func_1509BFB0.s](../../conker/asm/nonmatchings/game_C8950/func_1509BFB0.s),
VA **1509BFB0..1509C120**, ROM **C9460..C95D0**, frame48.
Its variadic count controls packet-word copies into `D_800D2F60 +8`;
selector nibble 11 chooses slot10, while the index is masked to 12 bits.
It calls at **1509C100**, forwards v0 unchanged and restores
`D_800D3840`. Cover counts -1/0/1/2/3/4/5/7/8, including the remainder
and four-word unrolled loops, both index endpoints and command defaults.
This does not qualify other callback slots or convert the retained parent.

Also execute all **26 words** of the script window
**150AE12C..150AE194**, ROM **DB5DC..DB644**, in
[DAFA0.s](../../conker/asm/DAFA0.s). Selector zero bypasses the callback.
The selected path clears only selector bits 0xF000, retaining the high
index bits, passes the original packet and forwards the result.
S7 is explicitly nonstandard return-link scratch here, not a preserved
ordinary-C register. Do not infer a complete-parent or hardware claim
from this bounded window.

## Direct C And Tests

Normal O2/g3 produces all **41 words and six bindings** directly, with
**zero new guards**. Plain OR/compound assignment has the correct length
but 18 register-allocation differences. The semantic clear-then-set
expression `(status & ~0x40) | 0x40` recovers the literal allocation.
Do not simplify it back to compound OR without requalifying the emission.
Raw unrelocated SHA-256:
`e1098a22f2f3904b76844a075afc11ad5db9ddba4c01afcaae2af43423628cab`.

Each actual tools copy passes all eight tests before installation:
primary **256.079s**, older mirror **257.997s**, no failures/errors/skips.
Fresh installed tests 1/8 pass in each copy, **1.967s / 1.765s**;
explicitly reuse the other six under unchanged source/object/helper/image
identity, rather than describing them as fresh installed tests.

- 7,168 flag/command phases, all 256 flag bytes and all 41 target words.
- 180 guest alias phases, 21 modular guest-index cases and exact read/write order.
- 107,520 native32 cases per run at O0/O2/O3 with trap UBSan and fenced typed objects.
- Eight compiled wrong-C implementations effectively rejected.
- 252 complete variadic-caller phases, visiting every one of its 92 words.
- 56 script-window phases, visiting all 26 words, including selector-zero bypass.
- Six independent GNU original/C links, 84 rebase phases and all six HI/LO bindings.
- Twelve fired target access-fault prefixes, including return-delay stores.
- Seven corrupt complete-image controls, all 26 historical/current input pins,
  the separately pinned old padded object and the entire unchanged guard manifest.

Both shared tool smoke checks pass. Linux-local exported wrapper files needed
their executable mode restored; bytes were unchanged. No compiler replacement,
dependency update, disabled semantic check or production profile change.
Routine work uses zero Claude calls.

## Production And Preservation

Preserve all **four raw/padded owner neighbors**, pools and addresses.
The actual three-command owner Make recipe reproduces the qualified object.
The target symbol changes from 12 to 164 bytes. Independent GNU assembly
of the original equals the C payload and all six bindings.

Reuse the retained Linux-local workspace only after proving all **15,768**
current live/copy input bytes identical. Production runs the actual Make
recipe with the unchanged guard manifest marked old, avoiding unrelated
timestamp-triggered recompilation. Exit0 in **0.469s**. The inherited
duplicate recipe warning for generated_12D630 is unchanged.

The independent first image and production ELF agree on every byte:
**126 changed bytes = 125 instruction bytes + one symbol-size byte**,
**zero exclusions** and no metadata permutation. ELF SHA-256:
`4f4aa719ec9d5aa01e5993ed748c7a7281e8c16200f226b1a308c7f8e953ad0c`.
Production owner object SHA-256:
`ac16c42cf29d212f1163f5c203d940d15a829aa351ad7a43557345f847ad03ea`.

Preserve **6,055 other linked bodies**, all **6,056 addresses** and
**189,088 protected Game-data bytes / 720 owners**, zero differences.
Game-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Adopt only qualified generated artifacts and receipts. Repeat the full
15,768-file live check before/after adoption; all static inputs and
non-target objects remain identical. Source and final image are separately
qualified. No unqualified stale copy is used for matching credit.

The literal standard matcher runs against the **actual live consumer ELF**:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh results: **3,715/5,505 total (67.48%)**, **3,042/4,832 Game (62.96%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,790 different**.
Converted counts/bytes do not change. The 75% threshold is **4,129**,
leaving **414**. The refreshed ELF-pinned queue contains **1,657 placeholders,
124 semantic/other bodies and nine unlocated entries**; these are screens,
not qualification.

Preserve all **1,512** earlier mirror dirty statuses/hashes and its
`ddbdd16` HEAD; add only the two absent task files, reaching **1,514**.
Never commit/reset/stash/clean that older mirror. Active tools are committed
first; the consumer source/docs/pin checkpoint follows. No push.
Root README changes only its two aggregate rows. Host source/builds,
real saves/configuration and frozen Release remain untouched.
After committing, wait for both owned Graphify workers and audit the commit
stamp plus old/excluded-node retention. Do not mark the 75% goal complete.

## Next Function

The refreshed queue selects `func_150D758C` in
[generated_1048D0.c](../../conker/src/game/generated_1048D0.c):
VA **150D758C..150D7630**, ROM **104A3C..104AE0**,
**41 words/frame0**, currently a zero-return placeholder.
Retail SHA-256:
`57b44ddc4413b32ee8e4bb5be76e8430293e5138f814e878a93775141fd0f56a`.

Static assembly shows the low-byte command 0x36 gate, selector-byte cases,
bit1 updates in the +0x58 word and three +0x28..+0x2A byte stores.
Determine the real caller/return ABI, alias order, argument-home store and
unreachable duplicate-load boundary before selecting C. This screen is not
a draft, installation or matching credit. Keep `func_1508CAD8` queued.

Receipts and retained orchestration:
`conker/build/game-record-command/qualified/`.
Linux-local workspace:
`/tmp/cbfd-two-range-sealed-my0624sa/64CBFD`.
Reverify the next delta and all live input/output identities before reuse.
