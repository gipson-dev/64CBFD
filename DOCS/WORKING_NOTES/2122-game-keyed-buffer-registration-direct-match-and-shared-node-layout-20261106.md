# Keyed buffer registration direct match and shared node layout

Date: 2026-11-06. Continue the 80% goal from consumer
`9f26210b342b6d1c88838e36817e64994a097b40` and mounted tools
`33dcaff2aff95c7c3a8d1aafd8a2fa0357fc0953`.
This completes the next target in
[Note 2121](2121-game-table-payload-spawn-direct-match-and-private-copy-layout-20261106.md).

## Installed result

`func_1518894C`, owner `generated_1B5CC0`, now emits all **67 retail words**
directly from semantic C: VA `0x1518894C..0x15188A58`, ROM
`0x1B5DFC..0x1B5F08`, frame `0x20`, saved S0/S1/RA at SP+`0x14/0x18/0x1C`.
All nine bindings match, with **no new guards or compiler profile changes**.
The recovered interface is `void(s32 key, s32 timer, s32 mode)`. The original
caller ignores the result, replacing its false zero-return placeholder ABI.

The local `ListNode15188A58` type now describes the complete 20-byte node,
sharing the original next pointer at offset `0xC` with the existing append
helper. Header bytes 0..3 are active/kind/cleared/recordSize; mode is byte 4,
byte 5 is retained, timer is signed halfword 6, buffer is pointer 8 and key
is word `0x10`. `D_800DF7CC` is the registration list. The separate cleanup
list `D_800DF7C8` keeps its own type and identity.

The first matching key receives a signed-halfword versus full-signed-word
timer comparison. Only a smaller timer is replaced, storing the incoming
word's low 16 bits; narrowing before comparison would be incorrect for wide
inputs. The mode always receives the incoming low byte. Other existing-node
bytes remain unchanged, including later nodes with duplicate keys.

If no key matches, the routine calls the actual signed-word allocator ABI as
`allocate_memory(20, 1, 0, 0)`, then `allocate_memory(0x180, 1, 1, 0)`.
The first failure exits; the second frees the new node without appending it.
The successful path initializes header bytes to 1, 3, 0, 20, stores mode,
timer, buffer and key, clears all 384 buffer bytes and appends the node.
The allocator's third argument is preserved as a word, without inventing a
clearing meaning. The append helper reads the live head after the providers.
The existing head-view parameter convention is explicit in the cast/comment.

## Recovery of the original schedule

The first ordinary C layout emitted 67 words/frame `0x20`, with five
scheduling differences in the final initialization. Explicit volatile
parameters regressed to 68 words and 56 differences; adding snapshots
returned to 67 words but retained 19 differences. Moving the timer assignment
before the buffer and key assignments recovered every word directly. Moving
it before mode instead retained four differences and was rejected. These
screens remain in the ignored target directory; no rejected schedule is
normalized into a match.

The shared append helper already required historical word guards. Its raw
compiler output remains unchanged, and its complete **17 padded retail
words** remain exact. This change adds no guards and earns no second match
for that existing helper. All **14 raw and padded neighboring functions**
remain unchanged.

Codex is the single writer. Claude calls attempted/completed: **0/0**.
Local source, ABI and compiler evidence settled the reconstruction.

## Fresh qualification

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_keyed_buffer_registration_match -v
```

All **eight installed checks** pass in both tools configurations. An ignored
overlay exercises the standalone sibling's actual compiler fixture, object
parser, timing engine and native32 command builder; helper paths and hashes,
new module hashes and mounted fallbacks are recorded. The sibling's six
tracked edits and 2,428 untracked files are preserved.

- **1,823 cases per guest body**, original/raw/padded, cover all 256 mode
  bytes, signed timer boundaries and wide incoming words, first duplicate
  match, both allocation failures, rollback, all 384 cleared bytes, retained
  byte 5, provider mutations and saved-register ABI. All 66 reachable words
  execute; one unreachable duplicate next-load remains literal in the
  complete 67-word comparison.
- **68 aliases per body** cover incoming timer/mode homes, relocated head
  storage and late reads, returned-node/buffer overlap and existing-list
  overlap. **79 own-access fault prefixes** preserve complete literal guest
  state. Private stack aliases are guest-only evidence, not portable C claims.
- **144 connected-helper cases per body** execute the complete original
  **11-word allocator wrapper**, all **39 bzero body words** in its 40-word
  slot and 16 reachable words of the **17-word append helper**. The bzero
  alignment NOP and unreachable append store remain literal. The wrapper's
  five-argument core call is checked as `(a0, a1, a2, 0, a3)`; allocator core
  and free remain bounded models.
- The actual **12-word caller window** runs **768 cases per body**, covers
  all window words, checks its key reload, duration subtraction and signed
  byte delay argument, and overwrites two poisoned void-return values with
  1. The containing 826-word parent is not claimed as fully emulated. The
  aligned retail census finds one JAL at ROM `0x57C44`, with no tails or
  literal function pointers.
- **Nine GNU links** and **90 rebased cases per body** verify both head
  HI16/LO16 pairs and all five helper R26 sites across carry boundaries.
- **6,726 native32 positive calls**, 1,121 rows per direct/callback path and
  O0/O2/O3 profile, use SDK headers, UBSan and the actual shared append C.
  They check the 20-byte layout, defined fields, retained byte, links,
  complete buffer and sentinels. Ten effective controls reject unsigned or
  narrowed timer comparisons, timer decreases, ignored matches, wrong mode,
  missing rollback, wrong allocation size, short clear, cleared byte 5 and
  the wrong append head.
- Fail-closed gates reject 268 raw-byte corruptions, nine altered bindings,
  five complete-image corruptions and the former zero-return stub.

Two fixture assumptions were corrected before the passing full runs. The
default newly allocated node initially collided with simulated SP at
`0x40000`; moving that default to `0x60000` separates ordinary provider
mutations from the explicit stack-alias cases. The append assertion initially
compared its historical guarded raw body against retail; it now checks the
correct padded body and separately preserves raw neighbors. Neither fixture
correction changes the recovered C. Both smoke checks are fresh. Prior shared
progress, word-guard and PC16 receipts are reused only after checking their
unchanged helper hashes; those broad suites are not claimed as freshly run.

## Production closure

All **98 frozen inputs** preserve source, headers, build inputs, original
caller and helper evidence. Compact allocated data and padded pools remain
unchanged. The compact object's `.reginfo` GPR mask changes from `A01F407C`
to `A31FDFFE`; an independent decode of all 67 body words derives that union
from the original mask and target mask `A303DFF6`. The other 20 metadata
bytes are pinned unchanged. Compact metadata is therefore not described as
entirely unchanged. Guard CSV bytes remain identical, including the existing
append guards. This owner emits no compiler diagnostics.

The entire ELF equals the independently predicted image with **203 changed
bytes**, **zero exclusions** and **zero named metadata permutations**.
The prediction changes the complete target slot and its symbol size from
12 to 268 bytes. All **6,052 function addresses** remain fixed; this is the
only changed body. All **189,088 protected data bytes in 720 owners** match.

Actual `make -C conker -j4 build/conker.us.elf progress.csv` equals the exact
prediction. `make -C conker all` retains the expected checksum exit 2 while
the wider decomp image differs from retail. The duplicate `generated_12D630`
Make recipe warning is unchanged. The fresh production recount is:

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,191 / 5,512 (76.03%) | 0 | 1,321 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,518 / 4,839 (72.70%) | 0 | 1,321 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion rows and `progress.csv` remain unchanged. **219 more** matches
reach the current 4,410 threshold for 80%. Production fingerprints:

- ELF: `ef08b2b982eaead134c2541fdce00a57ac40ad7f73ea17eef22f81796b391d05`.
- Owner: `174aa87a776d95d31abf8822740d5db45dbc209d49ec3e008bf5d0d0ae954469`.
- Code binary: `3d0cf7d32351e17698d54e7f8f7f6fc55b687b4681708ded4419712b49827428`.
- Unchanged guards: `b53721d727660eca66ed2771ba8fd8597642b08a123168033628a26ff92fd46b`.

Ignored evidence lives under `conker/build/game-keyed-buffer-registration-1518894C-match/`.
Graphify receives a scoped refresh with old-node retention accounting, without
claiming full-corpus re-extraction. Its existing package/skill warning remains.
Tools are committed before the consumer pin, source, aggregate README rows and
concise indexes. No push, dependency upgrade or host-port gameplay acceptance
is included.

Next: `func_1510D970` in `generated_13AE20`, a 69-word constructor with two
halfword-initialized banks, five incoming argument words, a six-argument
factory call and an optional nine-halfword tail. Verify its live caller ABI,
retained bytes, allocation failure and original loops before credit. Keep
handwritten `func_150A76F0` separate, preserve earlier documented boundaries
and keep the 80% goal active.
