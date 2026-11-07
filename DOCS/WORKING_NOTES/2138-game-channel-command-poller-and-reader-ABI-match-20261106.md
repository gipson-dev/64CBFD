# Channel command poller directly matched with its Init reader ABI

Date: 2026-11-06. Continues [Note 2137](2137-game-randomized-effect-forwarder-match-20261106.md)
from consumer `bc124189e7a8e2b84e15eb49c49ad46dcce75379` and tools
`1fa48826aa63b022680ef4ad9f21307424f6bac3`, toward the active 80% goal.

## Recovered routine and command format

`func_15080228` in `conker/src/game/generated_AD6B0.c` now emits all
**72 words / 288 bytes directly from C**, with **zero new guards**. VA
`0x15080228..0x15080348`, ROM `0xAD6D8..0xAD7F8`, no alignment tail.
The unchanged O2/g3/MIPS2/O32 profile emits the original **0x138-byte frame**,
256-byte buffer at SP+0x38, S0..S5 saves, RA save, branch-likely delay slots,
signed division sequence and seven relocation bindings. All three neighboring
functions remain fixed before and after padding.

The routine repeatedly requests up to256 bytes. Every nonzero signed32 return
continues the loop, including negative status words. Opcode byte0x4C selects
the channel command; byte3 is an unsigned byte converted to channel-1.
Bytes4..7 contribute their low seven bits in most-significant-first order.
The resulting nonnegative28-bit value is divided by367; a zero quotient
becomes20. The dispatch owner is the live byte D_800D18D0 times0x32C plus
D_800CC2D0, evaluated after the receive callback. Buffer bytes and actor index
can change across calls and must remain live. Capturing the first masked byte
before the following combinations reproduces the original schedule directly.

The original routine has no recognized-packet length check. Guest tests retain
seeded/stale bytes and deliberately escaped-buffer mutations. Native tests
use initialized fields, including a partial packet only after an earlier
complete packet. The original reader consumes a zero-length message then
returns0, leaving subsequent messages queued. For messages longer than256 it
copies255 bytes, appends a zero byte, skips the remainder and returns the full
message length. These behaviors are preserved rather than tightened.

## Reader return type and shared-header audit

The old C definition/header declared `void func_100126E8(s32,s32)` even though
the twelve-word Init wrapper leaves the queue provider's signed count in V0.
The definition and header now use **s32 func_100126E8(u8 *output,s32 capacity)**
and explicitly return the existing `func_15043CA4` result. A local typed
prototype uses its actual `struct105 *` queue, byte pointer and signed capacity.
The complete padded Init owner remains byte-identical:
`56e669d24aee7f3cdaa6e97751260f9a0154a53c89f4fc033d5c6d424309c2a5`.
All seven raw Init functions, loaded pools and register metadata stay fixed.
Its discarded raw .mdebug changes from238,148 to238,152 bytes. Its existing
Warning712 in func_10012588 is unchanged; this task does not widen that API.

Make's header dependency inventory covered25 sources. Intersecting all direct
header includes with the active linker inventory expands the audit to **201
active source owners**, including active `src/game/done/` files. Actual Make
recipes rebuild them first in a copied-header shadow tree, then in production.
Every unaffected loaded section, function, binding and register metadata block
is checked. Auxiliary symbol-number changes in relocation sections are closed
by reconstructing their bytes from unchanged named definitions. Nonloaded
debug/symbol/string changes are recorded with exact sizes and hashes; they are
discarded by the linker. Production changed-section counts: `{'.mdebug': 5, '.symtab': 4, '.strtab': 4, '.rel.text': 4, 'qualified target body, size and seven bindings': 1}`.
The shadow and production whole ELF both equal the independent prediction;
there are **no excluded ELF ranges** and no unreviewed dependent objects.

Raw Game .reginfo and its duplicate .options record gain only the recovered
GPR use mask, A300CF7E to A33FFF7E. Other raw loaded pools stay fixed. Raw
symbol/string/relocation tables reflect the recovered body and its bindings;
discarded raw .mdebug grows from71,956 to72,200 bytes. Padding restores the
complete owner metadata, so all padded pools/metadata match the predecessor.
The inherited
retail-word CSV and Make rules remain byte-identical.

## Focused qualification

Eight methods pass before and after installation in both mounted and sibling
tools configurations. New modules use a disposable overlay for the sibling;
its existing dirty files and Git state are preserved.

- **551 packet cases per body** cover all256 opcode, channel and index bytes,
  masked high bits, division boundaries, full-word nonzero statuses, empty
  queues, stale partial packets and callback mutations. All reachable words
  are visited. Word indices39,43,44,45 remain unreachable under the constant
  positive divisor; the entire original guard sequence is still emitted.
- **387 connected cases per body** execute the original12-word Init reader,
  58-word queue receiver,42-word transfer,18-word skip,11-word memcpy and
  51-word dispatcher as applicable. Independent models cover queue wrap,
  zero-length messages,256/260-byte messages, signed count results, channel
  branches and a bounded forward-copy guest alias.
- **812 fired access cuts** compare complete literal guest states. These
  qualify emitted guest instruction prefixes, not portable C fault semantics.
  The zero-return predecessor is rejected as a semantic implementation.
- The only direct caller is func_1501E400 at VA0x1501E500 / ROM0x4B9B0.
  **16 cases** execute its original nine-word conditional window: exactly
  status1 invokes the no-argument poller; the result is unused. Saved integer
  registers, GP, SP, FP and caller live values remain fixed. The full parent
  remains outside this window's acceptance claim.
- **Six independent GNU links**, three layouts and48 cases per body qualify
  all seven bindings, signed-low16 carries, JAL rebases and standalone tails.
- SDK native32 at **O0/O2/O3 with UBSan** runs551 positive cases per profile
  and rejects all eight controls: opcode, byte mask, divisor, zero fallback,
  channel decrement, cached index, positive-only status and lost Init count.
  The actual typed wrapper body and repaired shared header are compiled.
- **288 byte corruptions, seven binding corruptions and six complete-image
  corruptions** fail closed. Both tools copies pass fresh smoke checks; three
  unchanged shared regression receipts are explicitly fingerprinted and reused.

Reproduction uses the prepared retail inputs and frozen packet:

```sh
python3 -m unittest tools.tests.test_game_channel_command_poller_match -v
python3 -m tools.experiments.game_channel_command_poller_header_audit --rebuild
python3 -m tools.experiments.game_channel_command_poller_header_audit --production
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

The production Make invocation additionally supplies `-W <source>` for all201
inventoried sources, preserving their existing individual compiler profiles.
Its exact command, source list, compiler invocations and object accounting are
in the ignored packet. The existing duplicate generated_12D630 recipe warning
and expected unfinished-image checksum failure remain. COUNT/APPLY services
are bounded providers; no hardware or gameplay acceptance is claimed. The broad
rebuild makes207 compiler invocations and reports401 C diagnostics in existing
owners; it is not a warning-free build. The target Game owner has no diagnostics.

## Production result and resume boundary

The full ELF differs in exactly **220 bytes**, confined to the target body
and its symbol size12 to288. All **6,052 function addresses**, conversion rows,
progress.csv and **189,088 protected Game data bytes / 720 owners** stay fixed.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,207 / 5,512 (76.32%) | 0 | 1,305 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,534 / 4,839 (73.03%) | 0 | 1,305 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**203 more** matches reach the current4,410 threshold for80%.

- ELF: `3bb41bdc5405bf8b1b83e6b6a595f590cd45708bf2191f7b51ddabaca79b1d6d`.
- Game owner: `6bedcc1082f7b8d615f8b0f4db78a7d27c35acb6a3143eb4a3304cfe4ad02c40`.
- Code binary: `21ed0ae4574efbf9aedbf71d570747ad2eb87d21dabf49221bb6607c39ce99b7`.
- Unchanged guard CSV: `28d7a491d60ac432579e06040e28e21cd7e074d6a47e5c665d1d466ef42670ee`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence: `conker/build/game-channel-command-poller-15080228-match/`.
Tools commit precedes the consumer pin, source and documentation commit.
Graphify is refreshed with scoped old-node retention checks; this is not a
full-corpus extraction. Root README receives aggregate rows only.

Next: **func_15080500**, generated_AD9B0,72 words/frame0x20, VA
0x15080500..0x15080620, ROM0xAD9B0..0xADAD0. Recover its actor-state command
selection, special0x2B/0x2C handling, availability masks, protected status bytes
and record-offset division before qualification. It remains uninstalled and
uncredited. Preserve unrelated work, private inputs/saves, handwritten
func_150A76F0 and the frozen host Release. Keep the full80% goal active.
