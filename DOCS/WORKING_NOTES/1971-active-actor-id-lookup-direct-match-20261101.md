# 1971 - Active actor ID lookup recovered directly from C

`func_1505F0AC` now emits all **55 retail words**, with **no stack frame and
zero word guards**. Fresh production Make and Native ELF recounts confirm
**4,039/5,507 (73.34%)**, Game **3,366/4,834 (69.63%)**, zero address drift and
1,468 still different. The 75% threshold is 4,131: **92 more** matches are needed.
The wider goal remains active. This turn adds exactly one production match.

## Scope correction and source recovery

The previous handoff suggested `func_15014220`. A new comparison of the frozen
linked ELF with retail proves that its entire 35-word slot was **already exact
and counted**. Its source is retained, with no new credit. The seven-case compiler
screen remains in `conker/build/game-record-marker-effect-15014220-match/`.
Future selections must first come from the actual ELF difference inventory.

The unmatched inventory identifies `func_1505F0AC`: VA
`0x1505F0AC..0x1505F188`, ROM `0x8C55C..0x8C638`, owner `game_83300`.
Its false zero-return placeholder is replaced by a read-only search over
`D_800CC2D0[0..24]`. Return the first record with a nonzero interaction state
and matching unsigned ID byte at `+4`; otherwise return NULL. Reserved slot 25
is excluded. The search argument remains s32, so negative or greater-than-255
values cannot match a byte. The existing pointer return/header ABI is retained.
Local `actor`, `index` and `id` names and the function comment describe this scope.

The neighboring key-lookup helpers supply an established compiler/test pattern.
The ordinary typed loop naturally emits the retail four-record unrolling and
first-slot fast path under O2/g3; no custom profile or scheduling patch is needed.
Raw C payload SHA-256:
`f2c695803e461196564bcd63c1501cfc01c8df2a9fa02626c97f3201ba8ab8a2`.

Retail object relocations name `D_800CC5FC` (slot one) and `D_800CC2D4` (slot-zero
ID) separately. C expresses both as offsets from `D_800CC2D0`. Their unlinked
payloads/bindings therefore differ, while independent GNU links at the actual
base and three carry-sensitive rebases produce identical full 55-word code.
These address aliases are resolved by the linker, not by word guards.

## Qualification

- Full copied and padded owner comparisons preserve all **88 neighbors** and
  normalized pools. The same **eight inherited warnings** remain, with no new
  diagnostics or changed warning statements. Header/guard manifests are unchanged.
- **14,288 guest cases / 28,576 executions** cover all 256 byte IDs, negative
  and large full-width arguments, inactive/nonzero/signed states, first/last/
  reserved/missing slots, duplicate matches and stack phases. Actual base plus
  three rebase layouts pass complete memory/GPR/FPR/HI/LO/call/access-state
  comparisons between the original and compiled programs. The routine writes
  no memory and preserves saved state. All **52 reachable words** execute;
  duplicate unreachable loads at offsets 0x58/0x7C/0xA0 are identified explicitly.
- **108 access-prefix pairs** pass full bounded model-state comparison. This
  qualifies emitted instruction ordering, not portable C faults or real hardware
  exception-state acceptance. A sparse slot-zero success requires only that
  record's active word and ID byte; no later record mapping is required.
- Native32 O0/O2/O3 positive runs each pass **3,572 cases**, checking the returned
  pointer and every byte of all 26 records. Seven effective O2 controls reject
  reserved-slot inclusion, skipping slot zero, ignoring activity, signed ID byte,
  narrowed argument, wrong byte field and always-NULL return. All runs use UBSan.
- All **four aligned original JAL sites** are checked: ROM 0x919BC, 0xA1170,
  0xA5070 and 0xB0BF0. There are no aligned direct J or pointer-literal matches.
  **640 executions** cover real argument setup and return-pointer consumers.
  Complete small parents `func_15073CB8` (15 words) and `func_15077BB4` (12 words)
  execute, plus bounded 10/12-word windows in `func_150642AC` and `func_150836CC`.
  The latter window covers 11 words; its division-by-zero trap is unreachable
  with the retained constant stride 812. Full large parents are not claimed.
  Null-guarded routes pass; unguarded consumers are exercised only with non-NULL
  results. Root NULL-return behavior is independently covered. No new NULL guard
  is added to the original callers.
- Both tool copies pass **ten preinstall tests**: five new lookup tests and five
  flag-helper regression tests, followed by standalone shared checks. Both copies
  pass five lookup tests and shared checks after production installation. The
  prior flag routine's code is unchanged under the complete linked-body audit.

## Harness address repair

Review found that the flag-effect core's inspection constant `ENTRY` still named
0x15014094, although its FUNCTION, ROM slot, ELF predictor and guest program used
0x15014144. The full 55-word match and previous count remain valid. Correct the
constant and add an assertion coupling it to the independent guest entry value.
The same consistency check is included in this new lookup test. Both copies'
flag regression suites pass afresh before adoption. This small repair is banked
separately from the new tools. The two owned files are synchronized in the older
mirror without committing or overwriting its unrelated existing work.

## Production closure

The five real Make commands emit exactly the qualified padded owner object.
An independent prediction changes only the 220-byte target slot and its ELF
symbol extent from **16 to 220 bytes**. Actual private and production full links
are byte-for-byte equal to that prediction, with **zero excluded bytes**.
All **6,052 function addresses**, **6,051 other bodies**, complete expected named
symbol definitions, ELF length, linker map and guard CSV remain fixed. All
**189,088 protected Game bytes across 720 owners** remain exact. There are no
unplanned dependent object changes. Native's independent actual ELF recount
confirms the additional match.

Production ELF SHA-256:
`5ac59aad2748c59364549a911e4e7ce1576fce3de31e7f440e2d6414250d3fbe`.

## Artifacts and continuation

Stage `conker/build/game-active-actor-id-1505F0AC-match/` retains the input snapshot,
22 prepared-artifact pins, private owner/guest/native/caller/image receipts,
real-Make commands and objects, all preinstall/installed receipts, production
and Native recounts, graph proof, seal and final handoff. Public tools are
`experiments/game_active_actor_id_lookup_match.py` and its three test modules.
Original assembly, private candidates, old archives, unrelated mirror edits,
WSL cache and frozen host Release are preserved. Root README gets aggregate rows
only; details live here and concise current indexes. No push is performed.

Next verified unmatched candidate: `func_15030310`, the 53-word filtered linked-
record operation in `generated_5D2C0`. Inspect its cached next pointer, live actor
key reload, s32 filter argument, countdown/0xFF behavior, helper ABI and actual
callers before installation. Other parked candidates remain uncredited; do not
reuse their old input snapshots as the current baseline without explicit rebasing.
