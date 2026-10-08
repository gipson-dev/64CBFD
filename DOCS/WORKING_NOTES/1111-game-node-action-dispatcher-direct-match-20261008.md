# Game Node Action Dispatcher Direct Match

Date: 2026-10-08

## Scope And Baseline

Continue Game matching from commit `658e9649` and
[Note 1110](1110-game-attachment-progress-copy-direct-match-20261008.md).
Recover `func_15031A50`, **113 words / 452 bytes / frame `0x28`**,
VA `15031A50..15031C14`, ROM `5EF00..5F0C4`.
The old body was an already-counted, padded zero-return C placeholder with
110 instruction differences.

The [production owner](../../conker/src/game/generated_5D2C0.c) now contains
the complete action dispatcher. All **113 words emit directly as retail**
under existing `-O2 -g3` / MIPS2. No instruction guards, insertion/omission,
padding promotion, compiler-profile or shared-header changes.
SDK-only callee declarations recover the original one-, two-, three- and
five-word call ABIs. The [Makefile](../../conker/Makefile) adds only the existing
padder's target-specific `RETAIL_RODATA_SYMBOL := jtbl_80096F40_game` mapping.

## Signature And V0

This is a `void` action routine, not a zero-return query. The original caller
at `15030D34` calls it and immediately replaces V0 with its node at `15030D3C`.
The shared function header has no conflicting prototype. Removing the false
placeholder return allows semantic C to emit the original body directly.

Retail's incidental V0 is still checked in the selected guest body: default
and flag-update paths retain the selector, state update retains its pointer,
and callback paths retain their last callback result. This is not a defined
C return contract. Native and alternate-profile controls test the public
effects and calls, not an invented return value for `void`.

## Recovered Contract

Read unsigned selector byte `node+1`. Default paths do not dereference actor.
The compiler reproduces the original split: selectors `0x82..0x90` use fifteen
entries at `80096F40`, and `0x37..0x5E` use forty entries at `80096F7C`.
Selector `0x1D` uses a direct branch; other gaps/defaults have no action.

| Selector | Action |
| --- | --- |
| `0x37` | `func_151001B4(actor)` |
| `0x5A` | Read actor `+0x31C`; when nonnull add `0xAA` to its unsigned halfword `+0x1A6`, wrapping to 16 bits |
| `0x90` | OR actor word `+0x9C` with `0x70` |
| `0x8F` | OR that word with `0xE00` |
| `0x49` | `func_15163BE8(actor, 0xFF, 1)` |
| `0x5D` | Ordered `func_150D3360` then `func_150D5440`, each `(actor, 0xFF, 1)` |
| `0x3D` | `func_151BD828(actor, 0xFF, 1)` |
| `0x1D` | `func_151D74B0(actor, 0, 2, 0xFF, 1)` |
| `0x85`, `0x5E` | OR actor word `+0x9C` with `0x6000` |
| `0x8D` | Call `func_150859AC(0, 6)`; signed result `< 100` selects `D_80090228`, otherwise `D_8009022C`; truncate/store its word to node halfword `+0x18` |
| `0x82` | `func_151D74B0(actor, 6, -1, 0xFF, 1)` |

Keep actor saved across callbacks. The paired callback runs its second action
even if the first changes the selector. The random path stores node in its
incoming home, reloads it after the call, and reads the selected global after
callback mutations. Preserve signed threshold, both boundaries and 16-bit
output truncation. No new node/actor null checks or action gates.

## Table Ownership And Compiler Evidence

Generated `.rodata` contains **55 exact targets / 220 bytes**, followed by four
compiler alignment bytes. Both retail tables remain physically owned by
`asm/data/23B8A0.rodata.s`, not the generated C object. The real padder maps
the two HI/LO relocation pairs to the existing fixed anchor with addends zero
and 60; it does not link the duplicate generated pool or rewrite Game data.

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_action_candidates.py)
and [seven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_action_match.py) retain
**15 distinct source/profile combinations / 3,840 ordinary executions**.
Eight inline/signed-local/register/default forms are raw exact; unsigned-local
forms differ at two signed-versus-unsigned range checks. All controls preserve
ordinary public memory/calls. All-control raw V0, read-order, home and private
equivalence is not claimed.

| Profile | Meaningful Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| `-O2 -g3` | 113 | `0x28` | 0 |
| `-O2` | 113 | `0x28` | 5 |
| `-O1 -g3` | 124 | `0x30` | 123 |
| `-O1` | 124 | `0x30` | 122 |

## Qualification

All **seven pre-install tests pass in 68.216 seconds**, zero skips/errors/failures:

- **61,440 guest executions**, all 256 selectors, six signed random results,
  five state/counter patterns, four callback modes and two SP phases. Independent
  contract checks raw V0, ABI, ordered public reads/writes (including table reads)
  and memory. Full C/retail registers/events agree, all saved registers intact,
  **every one of the 113 words visited**.
- Eight lazy cases and **ten required read/store faults**, null/default actor,
  null nested state, required node/actor/state/global/table storage and post-call
  incoming node home. Exact error, preceding public trace and partial effects agree.
  Arbitrary private-stack aliases are not established.
- **30,720 native32 cases**, complete actual `void` C, valid aligned objects,
  all selectors/boundaries/counter wraps/public mutations. Calls, all ABI words,
  every byte of three objects and both globals agree. No native invalid-pointer,
  private-home or incidental-return claim.
- Four compiled effective negatives: wrong threshold equality, unsigned random
  comparison, wrong flag mask, missing second callback. Calls or public effects
  differ without accepting a fault as successful evidence.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings.
  Target bytes/relocations equal isolated C. The only new pool is target-owned;
  normalized table relocation identities equal the isolated pool.
- Actual padder: **452-byte body/slot, no padding**, original symbolic table
  anchor and two addends, independent entry/anchor/seven-callee/two-global
  links, including a HI/LO carry rebase.

The first run exposed fixture expectations, not production problems: second
table relocation offsets were wrong, and `-O1`'s incidental V0 was incorrectly
treated as a defined `void` return. Corrected expectations retain full selected-
body raw-V0 checks and all public control checks. Callees remain bounded
validating callbacks, not connected full execution or hardware/PC-port acceptance.

All **59 installed action/copy/progress/lookup/key-fit/resolver regression tests
pass in 436.351 seconds**, zero skips/errors/failures. Both actual-wrapper
connection suites and prior alias/home/native/owner/padder gates remain green.
Tools, Python syntax, driver CLI help and whitespace checks pass. Documentation
validation checks **93 documents / 4,062 relative links / zero broken links**.
This is scoped guest/native/tool qualification, not full callbacks or PC-port proof.

## Linked Audit And Progress

The US ELF and conversion CSV rebuild passed through normal Makefile rules.
Adding the target-specific table anchor triggered a broad dependency rebuild;
warnings reappeared in untouched sources, including the existing duplicate
`generated_12D630` recipe warning. Target isolated/copied-owner builds have
zero warnings; no overall warning-free-build claim.

Audit against Note 1110's authoritative ignored
`game-attachment-copy-test/after.json`: only target changes across
**6,058 symbols / 6,042 retail slots**. All **6,057 other symbol bodies**, other
slot addresses/extents, sixteen overflows, protected Init/Debugger/Game-data
sections, **720 exact data owners / 189,088 bytes**, **11,063 guard rows** and
conversion CSV hash are unchanged. Both table ranges equal the generated
targets while the complete original data image remains untouched.

Matching becomes **3,368/5,467 total (61.61%)**, **2,695/4,794 Game (56.22%)**,
**2,099 different**, zero drift. Init 492/492 and Debugger 181/181 remain exact.
Converted counts and byte percentages do not change because the placeholder
was already counted as C. Root README changes only two aggregate matching rows.

New authoritative ignored checkpoint:
`conker/build/game-node-action-test/after.json`, with `audit.py` / `audit.json`.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_node_action_match tools.tests.test_game_attachment_copy_match tools.tests.test_game_attachment_progress_match tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make tools-check
```

## Next Work

Continue Game matching, not complete. Next local body is `func_15031C14`, the
134-word / 536-byte / frame `0x38` actor-resolution and action cleanup routine.
It calls `func_15083E90(node[0])`, gates on null, uses a 48-entry table at
`8009701C`, clears the matching actor flags/counter, constructs two private
callback packets and has final `node+6` cleanup routes. Preserve incoming-home
reloads, required actor reads, private packet addresses and callback order.
Its table starts at previous anchor +220, before this function's compiler
alignment tail; inspect complete-owner pool placement before adding it.
Resolver C84/frame `0x20`/40 differences and wrapper/basis/translator/sampler
boundaries remain open. No sibling, frozen Release, real-save, runtime/hardware
or push action.
