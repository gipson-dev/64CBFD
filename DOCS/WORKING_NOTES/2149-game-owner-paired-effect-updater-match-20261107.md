# Two-channel owner effect updater matched

Date: 2026-11-07. Continues [Note 2148](2148-game-owner-record-lookup-and-switch-match-20261107.md)
from consumer `cd0afd445cbd86e904ec07f91481a05023a5b36a` and tools
`d96d7f7f5738c13fdb1c869e7f7c4711157f24e6`, toward the active 80% goal.
This turn contributes one fully qualified match.

## Complete callback and typed data

`func_1518BD60` in `conker/src/game/generated_1B8F40.c` now has its complete
**214-word / 856-byte** C body, VA `0x1518BD60..0x1518C0B8`, ROM
`0x1B9210..0x1B9568`. The interface is `void (OwnerPairRecord *)`; the prior
zero-return placeholder supplied a false return contract. Raw C differs in
58 words. Checked guards reproduce every retail word after a symbolic role
audit and guest/native qualification. No instruction is inserted or omitted.

The recovered 68-byte record contains the previously identified owner request,
two signed timers, and two pairs of previous x/z coordinates. Request fields
retain the measured base/range and inclusive-choice roles established in
Note 2148. Native SDK assertions check every relevant size and offset.

Each of the two channels first subtracts the live global tick, with explicit
32-bit wrapping arithmetic. The decrement happens even when the owner gate
fails. A valid owner needs a non-NULL pointer, a nonzero first word, a nonzero
field at +1D4, and the matching unsigned tag at +3B. A channel whose timer has
not expired copies the owner's signed coordinates without sampling randomness.

An expired channel makes nine calls in the original order: integer RNG, angle,
quarter-turn angle, float RNG, integer RNG, integer RNG, integer RNG, float RNG,
then the 15-argument effect factory. The first unsigned remainder uses the
second signed-16 limit plus one; the angle helper receives its low byte and
that byte minus 64. The first float samples speed from base/range. The timer is
reset to unsigned random modulo 23 plus 5. The first choice limit controls the
request count, which wraps to a byte after adding 3; payload size is count*12+8.
Duration is unsigned random modulo 21 plus 80, with mode/active both 1.

The second float samples gravity. Velocities are speed*quarter, zero, and
speed*angle. The threshold is captured once before the loop, while tick is
reloaded per channel. Kind is captured before the second float call; flags,
owner metric, category and context remain live afterward. Flags include mask 0x08,
alpha is 255, and the channel byte uses `255 - ((ownerMetric >> 5) << 6)`.
The render record retains its seven original words and final defined bytes 0/9.

The factory gets all 15 typed arguments. Allocation failure still proceeds to
coordinate updates. On success, the created object's payload at +98 receives
the source record pointer at +48 and the current channel byte at +4C. The owner
is reloaded after an expired channel's factory call. An unexpired channel uses
the owner already checked at its gate. The second coordinate access retains
the original further owner reload after the first store.

The real 288-byte frame naturally places the 32-byte render object at SP+B8,
32-byte descriptor at SP+DC, and 28-byte request at SP+FC. Source declarations
are actual scalar/aggregate locals; there is no fabricated padding object or
frame guard. Request has 9 defined bytes, descriptor 24, and render 30. The
remaining 29 bytes retain their original unwritten behavior. Guest checks use
seeded private bytes. Native providers check defined inputs before initializing
only those holes; no portable value is claimed for indeterminate production
bytes, and the lower allocator remains bounded.

## Derivation and source experiments

The first draft emitted 215 words with a 304-byte frame. Reusing scalar
temporaries, recovering the actual record arrays, and retaining explicit call
sequencing recovered the exact length/frame. Testing the timer array directly
also recovers the original temporary-register lifetime. A named copied timer
value had unnecessarily kept a separate V0/V1 role live through the owner gate.
Normal O2/g3 remains selected. No-unroll profiles 0/1/2 changed none of the
screened bodies and provided no benefit, so Makefile/profile are unchanged.

The 58 guards are accepted only after checking the complete raw body hash,
all 13 bindings, and every changed region:

- The invariant setup permutes independent address/constant initialization
  and exchanges the live zero/threshold FP roles. Corresponding LO16 bindings
  move together. Physical callee-saved register spills/restores are unchanged.
- The timer branch's delay schedule is closed for expired and unexpired paths.
  S4 carries the current channel before an expired path's first call. The raw
  unexpired-path S4 assignment is dead before restoration; no helper observes it.
  Coordinate addressing and the successful backlink retain the same index.
- One speed multiply changes commutative operand order. A straight-line
  symbolic verifier closes both channel indices' factory setup: all seven
  ordered public reads, all 19 independent private writes, all 15 arguments,
  and floating value expressions agree. Unsupported instructions fail closed.
- Coordinate reads/stores remain ordered after the factory, including the
  reload between output stores. The zero initialization, byte increment and
  below-two loop condition prove the only indices are 0/1. Frame/save/restore
  and all instructions outside proved regions are fixed.

The arithmetic proof uses finite intermediate values and private frames
disjoint from live input objects. It does not equate raw intermediate scratch
registers, raw instruction fault prefixes, FCSR exception behavior, or hardware
gameplay. The normalized body is byte-exact and receives separate fault checks.
Independent proof controls reject a changed factory argument, public read,
loop boundary and frame; rejection does not rely only on the whole-body hash.

All eight other owner bodies/bindings remain fixed both raw and padded. The
whole existing 48-byte switch pool is unchanged. Raw register masks change
only from GPR A31FFFFE/FPR000F0DF1 to GPR E3FFFFFE/FPR3FFF0FF1, matching the new
saved-register use. Both .reginfo and .options are checked completely apart
from these exact fields and the .options file offset following object geometry.
All padded pools are unchanged. Both owners compile without C diagnostics.
The old guard CSV is preserved byte-for-byte, with 58 rows appended. All 112
core/header snapshots remain checked.

## Fresh qualification

Eight checks pass before and after installation in both tools configurations:

- **2,406 guest cases per body**, retail/raw/padded, cover both channels, all
  angle-input byte patterns, all owner gates, timer wrap, signed-16/unsigned modulo,
  pointer aliases through successful backlinks, captured versus live fields,
  provider mutations and allocation failure. All private bytes and preserved
  GPR/FP registers agree on return. All 210 defined-input reachable root words
  are visited. The four unchanged divide-zero BREAK words at57/78/104/116 are
  outside the defined C modulus domain; no divide-zero execution is claimed.
- **512 additional connected cases per body** execute all 151 retained helper
  words: integer RNG 18, float RNG 25, angle lookup 27, factory 70 and byte-copy 11.
  Original helper ELF bytes equal retail. The actual 65-word lookup is used;
  every angle branch, including NEG.S, is covered. Integer/float draws share
  the 64-bit seed. All15 root factory arguments and 11 lower allocator arguments,
  NULL/success paths, descriptor/render copies, and root backlinks are checked.
- **586 fired access cuts**, including 79 delay-slot cuts, compare complete
  normalized/original state, memory, trace, PC and delay markers. All owned
  64-bit RNG accesses are tracked. Raw fault identity is explicitly not claimed.
- **16 caller-window cases per body** execute the actual 10-word list-dispatch
  window in `func_151670C0`, including the empty-chain skip and saved-next store
  in the JALR delay slot. The sole aligned callback literal is ROM2305B4 /
  VA8008BAF4: `D_8008B4A8 + 31*52`. There are no direct JAL or tail sites.
  The callback receives one record pointer and its return is ignored. The
  complete parent remains outside this recovery.
- **Six independent GNU links** exercise all 13 bindings and nine JAL sites in
  three layouts, including signed low16 carries; twelve rebased execution cases
  per body pass.
- SDK **native32 UBSan**, O0/O2/O3, passes 350 cases per profile with all 20
  effective negative controls. Typed sizes/offsets, every defined packet field,
  all 15 arguments, complete heap fences, both backlinks, every angle byte and
  byte-wrapped counts are checked. Controls include early range capture, late
  kind capture, live threshold reload, wrong modulo/stride/argument and the stub.
- All 856 raw-byte,13 binding, four independent symbolic-role and six whole-image
  corruption controls are rejected.

The connected-data assertion caught an older synthetic float-RNG scale copied
into the first fixture draft. The frozen production ELF's actual constant at
8009F740 is **37800080**, and the fresh connected checks use that exact value.
No production constant is changed. The local executor adds the finite NEG.S
operation required to cover the original lookup's negative quadrants; shared
oracle modules are unchanged.

Both tools copies also run fresh shared smoke checks. Three unchanged shared
regression receipts are reused only after exact helper/test fingerprint checks.
The sibling uses its own compiler/parser/padder/base oracle/native command and
lookup reference; its missing pool auditor and tracked64-bit RNG executor are
explicit, fingerprinted mounted fallbacks. New modules use a disposable overlay.
Windows Git checks all2434 inherited dirty sibling paths unchanged. Claude calls:0.

## Production checkpoint and next target

Actual Make compiles only generated_1B8F40.c once under ordinary O2/g3, with
zero C diagnostics. The linked ELF equals the literal **661-byte prediction
with zero exclusions**. Only this function's body and symbol size 12 to 856 change,
plus one reviewed metadata permutation: D_800A7440/D_8009E720 exchange symbol/
string slots while retaining their complete definitions. No ELF range is
excluded. All 6,052 function addresses, other bodies, progress.csv, Makefile,
and 189,088 protected Game bytes across 720 owners remain fixed. The inherited
duplicate 12D630 recipe warning and expected unfinished-ROM checksum exit 2 remain.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,219 / 5,512 (76.54%) | 0 | 1,293 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,546 / 4,839 (73.28%) | 0 | 1,293 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**191 more** matches reach the current 4,410 threshold for 80%.

- ELF: `326836ce96a1eaafa5ca835465c74a783934737c4c608f86d29bf211b1a9057d`.
- Binary: `cb5510c338359fc95d183d360fdeaa097f6d598e133083dc614b4f8186ff6801`.
- Guard CSV: `5cef039754c4e0bbc2f63202b3e345c31158277e74f76e062bfe90b48b75a97c`.
- Unchanged Makefile: `4e252a768e0bbb7b7c29dcdefb9bc54c94788dc62c3ce486864d817a7efadd5c`.

Reproduce with `python3 -m unittest tools.tests.test_game_owner_paired_effect_match -v`.
Receipts live in `conker/build/game-owner-paired-effect-1518BD60-match/`.
Production uses `make -C conker -o retail_word_patches.us.csv -o Makefile` for
ELF/progress, expected unfinished-image `all`, then `match-progress NON_MATCHING=1`.
The frozen shared dependency timestamps avoid a broad rebuild; the new guards
are still read by the actual padder.

Tools commit precedes source/guards/docs/pin. README receives aggregate rows
only. Historical status-index text is checked unchanged as UTF-8. Graphify
refresh is scoped/fail-closed and retains old nodes outside changed paths;
this is not full-corpus extraction.

Next: **func_1518C540**, the 15-word counter-to-alpha callback in this owner,
VA1518C540..1518C57C / ROM1B99F0..1B9A2C. Recover its signed input scaling,
upper saturation, byte store and return behavior before qualifying C. The
larger 290-word renderer func_1518C0B8 remains a separate unfinished body.
Preserve handwritten 150A6FA0/150A76F0, unrelated work, private inputs/saves and
frozen host Release. Keep the wider 80% goal active.
