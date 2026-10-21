# Paired SDK Matrix Callback Wrappers Direct C Match

Date: 2026-10-21

## Result

Replace the two zero-return placeholders in
`conker/src/game/generated_1A1E50.c` with complete, purpose-commented C
wrappers using the real SDK `gDPPipeSync` and `gSPMatrix` macros.
Both compile directly with normal O2/g3: no guards, shared-header edits,
compiler-profile changes, raw-word emitters or omitted logic.

| Function | VA body, end exclusive | ROM body, end exclusive | Words | Frame | Selector | Callback table |
| --- | --- | --- | ---: | ---: | --- | --- |
| `func_15174AA4` | `15174AA4..15174B48` | `1A1F54..1A1FF8` | 41 | 40 | byte `+0xC` | `D_8008CD74` |
| `func_15174B48` | `15174B48..15174BEC` | `1A1FF8..1A209C` | 41 | 40 | byte `+0xD` | `D_8008CD7C` |

The second slot also contains the original four-byte alignment NOP at
`15174BEC`; the next function starts at `15174BF0`. This is not an
additional semantic instruction. Each wrapper has six original HI16/LO16
bindings, for 12 total. Keep the assembly reference `conker/asm/1A1E50.s`.

## Recovered Behavior

The actual interface is `Gfx *(Gfx *commands, s32 unused, s32 view)`.
Store the incoming unused word in its retail argument home, emit the pipe
sync and model-view load, then read the descriptor pointer and unsigned
selector. For a nonzero selector, index the selected callback bank and call
it with the command cursor and full view word. Preserve the matrix address
across that call in SP+0x18. Use the callback's returned cursor for the last
model-view load and return the cursor advanced past it. Selector zero skips
only the callback, not the surrounding graphics commands.

Declare the two banks locally as arrays of `Gfx *(*)(Gfx *, s32)`, use the
existing `struct104 *D_800B0DF0` and `Mtx D_80089470` types, and access the
two selector bytes through a legal unsigned-character view. Those bytes
currently live in the existing structure's padding range; do not invent
shared field names or revise unrelated callers to force a match.

Retail emits E7000000/zero, then DA380003/matrix-address before reading the
selector. The callback can redirect the cursor, including backward to an
overlapping valid command range. Preserve ordered stores and the late read.
Do not introduce a NULL-callback guard: only selector zero bypasses dispatch.
Pristine callback banks contain zero entries. Test providers are opaque
fixtures, not evidence of natural callback registration, rendering or gameplay.
Nonzero-selector/NULL-entry qualification stops at the target-zero guest
call packet; it is not a portable C NULL call or hardware-fault claim.

An explicit selector local produced the right 41-word length but frame48
and five differences (words 0, 1, 25, 28, 38). The successful source repeats
the inline byte/index expression; IDO CSE preserves one late read and the
natural frame40. An earlier progress update incorrectly called the rejected
frame32; the measured rejected frame is 48. No scheduling patch is needed.
Alternative unused-argument types did not discriminate historical typing;
retain the conservative word type used by the actual callers.

## Actual Caller Qualification

`conker/src/game_45B80.c` has both real direct callers. Add two local
prototypes, and keep the first caller's existing s32 address-word return
explicit with `(s32)func_15174AA4(...)`. Do not change its public return API.

| Caller | VA body, end exclusive | Words | Frame | Relevant order |
| --- | --- | ---: | ---: | --- |
| `func_15018E88` | `15018E88..15018F08` | 32 | 24 | Optional out-pointer helper, two layer calls, late unused-word read, AA4 |
| `func_15018F08` | `15018F08..15018F80` | 30 | 24 | B48, two layer calls, out-pointer helper |

Execute all 62 original/current caller words over 1,152 phases, including
signed-16 view extension, late `D_800BE9F0` reads and redirected cursors.
Layer/out-pointer helpers remain opaque boundaries, not recovered-provider
claims. The callback prefix is cursor/view; matching incidental private
registers does not establish a larger provider API.

All 16 functions, bindings and pools in the caller owner remain identical.
The complete padded caller object is byte-identical across the prototype
and cast change: 18,220 bytes, SHA-256
`6f93d458b6a4991ee00a8d815534c58451aad5b9864fff79c9ceaf0c9533fafc`.
Only the B48 implicit pointer/integer warning is removed: four warnings
become three, with the remaining diagnostics unchanged after normalization
of paths and line numbers. Leave those unrelated warnings alone.

## Focused Qualification

Tools: `experiments/game_matrix_callback_wrappers.py` and
`tests/test_game_matrix_callback_wrappers.py`, copied byte-for-byte to the
older standalone tools checkout without committing that checkout.

| Run | Primary | Older mirror | Errors / failures / skips |
| --- | --- | --- | --- |
| Complete pre-install suite | 8 tests, 143.170s | 8 tests, 161.581s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 15.131s | 2 tests, 10.043s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under unchanged source,
raw/padded object, helper, input and complete-image identity. They are not
fresh installed executions. Shared tool smoke checks also pass in both copies.

- 2,060 guest cases / 4,120 phases visit all 82 wrapper words. Cover callback
  GPR/FPR clobbers, store/read order, pointer redirection and guest argument-home
  and saved-matrix aliases. Guest-only stack aliases are not native C claims.
- 7,168 native32 cases at each of O0/O2/O3 use trap UBSan, the actual SDK
  macros, fenced typed Gfx arrays, the existing descriptor type and both real
  C callers. Use only legal callback bank indices. Eight compiled wrong-C
  controls are effective; two early-read and two invented-NULL-policy MIPS
  controls distinguish the actual instruction semantics.
- Twelve independent GNU links / 144 rebase phases exercise all 12 bindings,
  signed-low carries and independently movable global anchors. Four hundred
  fired root-access fault prefixes exclude accesses inside connected hooks.
  These qualify emitted order, not portable C faults, FCSR or hardware.
- Eight strict-image corruptions are rejected. Pin 24 historical/current
  inputs, including SDK gbi.h, both owners, original assembly, layout,
  guard manifest, ROM, ELF, symbols, headers and build recipe; additionally
  pin both predecessor objects. Preserve two main-owner neighbors and all
  16 caller functions. Actual Make shadows perform six productive commands.

The initial dense native attempt was explicitly SIGINT-retired with its
owned-process receipt and is not counted as a passing full run. Lossless
fixture compression reduces generated C to 4,800,203 bytes: sparse Gfx
patches are round-tripped against all 192 words, descriptor and call-log
compression asserts the omitted bytes, and every output/fence is still
checked. Immutable reference caching changes cost, not coverage. The stable
compressed harness is the one that passed both full suites above.

## Production And Preservation

The actual sealed-workspace Make exits zero and reproduces both qualified
objects and the first-linked image. Three inherited caller warnings and the
pre-existing duplicate-symbol warning remain. The independent prediction
accounts for every changed byte: **248 = 246 instruction bytes + two
symbol-size bytes**, with zero metadata exclusions or permutations.

Installed ELF SHA-256:
`bba307cc6a04e01abe6d87053b9db3c28a4a76796345608cc9feaeadd24fc02a`.
Installed main-owner object SHA-256:
`6509f900890cc3a372a73c162a6d8e0e84f346f39e299b131fde07a5186288de`.

Audit all 6,056 linked functions: 6,054 other bodies remain fixed, every
address remains fixed, and all 189,088 protected Game-data bytes across
720 owners remain unchanged (SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`).
The complete guard manifest remains unchanged. Keep the unmatched neighbor
`func_151749F8` and existing timer `func_151749A0` untouched.

Seal and compare all 15,777 current live/cache files before production,
then prove the allowed source/object/ELF changes and every static/non-target
input again before and after adoption. Caller object bytes are immutable
even though its source is recompiled. Promote only the two objects, ELF,
linker script and progress CSV. One first production assertion caught an
extra blank line before any cache writes; correcting that whitespace restored
exact qualified-source identity before the successful run.

All 1,516 pre-existing dirty paths/statuses/hashes in the older tools mirror
are preserved; only the two task files are added, yielding 1,518 dirty paths.
Do not commit, reset, clean or stash that independently dirty checkout.
Tools commit `d6164dc83c88b9a7d39a64632c2cf31f8100d345` precedes the
consumer source/docs/pin checkpoint. No push, host build/launch/change or
Claude call. Host Release remains frozen. Root README changes only the
two measured aggregate rows. Refresh Graphify and verify old-node retention
after the consumer checkpoint; retain receipts under the ignored build path.

## Measured Progress And Resume

The literal standard match-progress command runs against the adopted live
consumer ELF and exits zero:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,720 / 5,505 (67.57%) | 0 | 1,785 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,047 / 4,832 (63.06%) | 0 | 1,785 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold is 4,129 exact functions; **409 more** are required.
Do not mark the broader target complete. The ELF-pinned source-shape queue
has 1,652 placeholders, 124 semantic/other entries and nine unlocated entries.
These are triage categories, not ABI or source qualification.

Next is `func_1517B7F8`, 41 words/frame0, in
`conker/src/game/generated_1A89B0.c`, reference `conker/asm/1A89B0.s`,
VA `1517B7F8..1517B89C`, ROM `1A8CA8..1A8D4C`.
Static inspection shows signed position halfwords, counter thresholds,
quadratic integer division, a post-position-store counter reload and ordered
Y/X/Z stores. Qualify its actual four-argument dispatch ABI, unused fourth
argument home, overflow/boundary behavior and input/output/counter aliases
before drafting/installing it. No candidate or matching credit is claimed.
`func_151D710C` is next in the screen; retain the larger 862-word
`func_1508CAD8` owner stub on the queue rather than broad-converting it here.

Private receipts: `conker/build/game-matrix-callback-wrappers/qualified/`
contains snapshots, source probes, raw/padded objects, test logs, Make shadows,
strict image audit, production proof, full live adoption audit, literal matcher,
queue, mirror-preservation proof and checkpoint audits. Keep these private;
no ROM or generated native fixture is committed.
