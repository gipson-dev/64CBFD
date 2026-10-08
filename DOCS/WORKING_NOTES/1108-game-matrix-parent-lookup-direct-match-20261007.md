# Game Matrix Parent Lookup Direct Match

Date: 2026-10-07

## Scope And Baseline

Continue Game matching from commit `da99b2b8` and
[Note 1107](1107-game-matrix-pair-bank-phase-and-key-lifetime-fit-20261007.md).
The next successful conversion is `func_1503195C`, the linked-list lookup
used by recursive matrix-pair resolver `func_15031070`.
Retail is **28 words / 112 bytes / no stack frame**, VA
`1503195C..150319CC`, ROM `5EE0C..5EE7C`.

Replace its `GLOBAL_ASM` pragma in the
[production owner](../../conker/src/game/generated_5D2C0.c) with complete C.
All **28 words emit directly as retail** with the owner's existing IDO
`-O2 -g3` / MIPS2 profile, no expected-word guards, filler, profile edits,
new types or shared-header changes. The original assembly remains available
as reference; it is no longer the production implementation of this function.

## Recovered Contract

The routine caches the actor's unsigned group byte at `+0x3B`. Group zero
returns zero without reading global list head `D_800C3EE0`. Otherwise it
walks the chain at node `+0x54`, matching both node group byte `+0` and
node key byte `+6`. The full incoming key word is compared with the byte;
values above 255 or negative argument bit patterns are not truncated.

Ordinal zero returns the first matching node, ordinal one the second, and
so on. Only matching nodes consume the ordinal. Use `u32` for the local
ordinal decrement so all incoming 32-bit patterns have defined wrapping
arithmetic; the external three-word guest ABI is unchanged. The SDK-only
owner retains its existing weak forward declaration and word-valued return,
which is used as a guest pointer by its callers. Do not import the unrelated
shared `struct126` layout into the resolver.

The current node's group is read before its next word; the next word is
required even when this node will be returned immediately. The node key is
read only when the group matches. No new actor-null, node-bounds, list-length
or cycle gate is added. Tests use bounded acyclic lists, not a production cap.

The exact source shape combines the two predicates, tests nonzero ordinal
before decrementing it, and advances `current = next` in both matching and
mismatching arms. Factoring out the advance or using post-decrement changes
the loop's branch-likely/decrement schedule. The repeated advance is retained
because it recovers the original instructions, not because both forms have
different ordinary results.

## Source And Behavioral Qualification

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_matrix_parent_lookup_candidates.py)
retains **52 source forms** and the two existing `-O2`/`-O1` profile screens.
The [ten tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_matrix_parent_lookup_match.py)
qualify **58 distinct source/profile combinations / 2,784 ordinary executions**;
only `combined-inverse1-advance1` is raw exact. Required-read order and private
stack behavior are not claimed for every control. The lower-optimization
controls need mapped stack storage and comparison of public memory, unlike
the selected zero-frame leaf; these fixture assumptions were corrected before
counting the controls as qualified.

Selected-body qualification includes:

- **7,168 guest cases**: all 256 group and key byte values, full-word key and
  ordinal boundaries, three list rotations, empty/short/long lists, both SP
  phases, first/later/no match, duplicate matches and group-zero early return.
  Compare ordered reads, full return and GP register file against retail,
  preserved source memory, no writes/calls and saved SP/GP/RA. The only
  unvisited retail word is unreachable duplicate move index 22.
- Two lazy cases and **nine required-read faults**, including null actor,
  missing head/group/key/next and later-node reads. Check identical error and
  preceding read trace; the next word remains required on immediate success.
- **12,779,520 native 32-bit cases plus one lazy gate**, actual selected C,
  valid aligned node storage, all group/key bytes, four extra full-word keys,
  eight ordinal values, eight list lengths and three rotations. Node bytes
  remain unchanged. This is not a native invalid-pointer/private-stack proof.
- **32 recursive resolver fixtures / 128 executions**, all four C/retail
  resolver-lookup combinations, both pages/SP phases, failed routes and the
  four-parent chain. Execute the actual lookup and resolver instructions;
  compare public outputs/calls/traces. Full wrapper private equivalence stays open.
- Three effective compiled negatives: truncate the key, accept either predicate,
  or decrement ordinal on mismatch. Each returns a wrong result without a fault.
- Copied owner: **40 functions / 39 unchanged neighbors**, zero warnings,
  identical target and neighbor bytes, sizes, normalized pools and relocations.
- Actual generated-slice padder: meaningful and retail size both **112 bytes**,
  no additional padding, both head HI/LO relocations preserved, independent
  head rebase including a low-half carry links exactly as expected.

All **ten pre-install tests pass in 66.371 seconds**, zero skips/errors/failures.
All **32 installed lookup/key-fit/resolver regression tests pass in 206.762
seconds**, zero skips/errors/failures, including both actual-wrapper connection
suites, aliases, incoming homes, native C, owner and padder checks. This is a
scoped installed regression run, not a new full hardware/PC-port qualification.
Python syntax and module CLI help pass. Documentation validation checks
**90 documents / 4,034 relative links / zero broken links**.
`make tools-check` and scoped staged whitespace checks pass.

## Linked Audit And Progress

Build the US ELF and regenerate the ignored conversion CSV through its normal
Makefile rules. Compare against Note 1107's authoritative ignored checkpoint
`conker/build/game-matrix-pair-key-test/after.json`.

All **6,058 symbols / 6,042 retail slots / sixteen overflows** retain identical
instruction bytes, addresses and extents. The previous assembly was already
retail-exact; the change is its source representation. Protected Init/Debugger/
Game-data sections, all **720 Game-data owners / 189,088 bytes**, and all
**11,063 guard rows** remain unchanged. No target guards. The regenerated
conversion CSV changes exactly one row, `func_1503195C: asm -> c`, adding
112 converted bytes. Reverting only that row in a structured CSV rendering
reproduces the previous checkpoint's SHA-256.

Measured aggregates:

| Section | Converted Functions | Converted Bytes | Byte-Exact |
| --- | ---: | ---: | ---: |
| Total | 5,467 / 6,042 (90.48%) | 85.62% | 3,365 / 5,467 (61.55%) |
| Init | 492 / 539 (91.28%) | 92.53% | 492 / 492 (100.00%) |
| Game | 4,794 / 5,321 (90.10%) | 84.94% | 2,692 / 4,794 (56.15%) |
| Debugger | 181 / 182 (99.45%) | 99.19% | 181 / 181 (100.00%) |

Still different remains **2,102**, address drift zero. Update only the root
README aggregate rows; detailed recovery updates remain in the documentation.
New authoritative ignored checkpoint:
`conker/build/game-matrix-parent-lookup-test/after.json`, with `audit.py` / `audit.json`.
The build passes with the pre-existing duplicate `generated_12D630` recipe warning.

```sh
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_matrix_parent_lookup_match tools.tests.test_game_matrix_pair_resolver_key_fit tools.tests.test_game_matrix_pair_resolver_recovery -v
make tools-check
```

## Remaining Resolver Boundary

`func_15031070` stays **complete C84 / frame `0x20` / 40 differences**, one
meaningful instruction short of retail85. Twelve further isolated probes
remain ignored exploratory artifacts, not ordinarily qualified controls:
old-style argument definitions with raw/typed node forms emit the same C84/40;
attachment/key carriers, with optional bank/parent reuse, instead force C87/C88
and frame `0x28`. They do not recover the V0-to-A1 key move.

Compiler-option guesses `-Wo,-noargmatching`, `-Wo,-noargmatch` and
`-Wo,-nocopyprop` are unrecognized and rejected; they are not supported
profiles. `-O2 -g1/-g2` warn that the file is unoptimized and are rejected too;
the recognized `-O2 -g0` probe is still C84/frame `0x20`/47 differences.
No guessed compiler option or rejected diagnostic becomes a production change.

Continue the missing V0 key load/move and subsequent independent recursive
return/store schedule, or a separate bounded Game match. Do not promote
padding, insert a missing word, or normalize forty branch/read words.
Wrapper key/primary-read, basis private layout, translator and sampler
boundaries stay separately open. No sibling, frozen Release, real save,
runtime/hardware or push action.
