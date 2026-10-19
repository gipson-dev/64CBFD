# Parallel Array Reset Complete Match

Verified:2026-10-19. **Installed complete C recovery: all52 words /208 bytes
match retail, including frame8 and the original saved-S0 lifetime.**

Finish `func_1508DA1C`, generated_B3020, VA `1508DA1C..1508DAEC`, ROM
`BAECC..BAF9C`, after
[Note1587](1587-round-robin-slot-selector-complete-match-20261019.md).
Consumer predecessor **3064b493**, tools predecessor **cf919bf**. Bank tools
**958811a** before the consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Capture the initial context from D_800D23B0 and all six output bases before
the first loop. Fill initial-context+EB0 with -1 while index is below the
signed32 count+10. After each store, reload the **current global context**
and its count. If that loop ran, the latest reloaded context also supplies
the second loop's initial signed count+EA4; otherwise use the initial one.

Reset five parallel arrays in this exact per-iteration order:

```text
initial-context+F70  = -1
initial-context+FF0  =  0
initial-context+10F0 = -1
initial-context+1070 =  1
initial-context+12F4 =  0
```

Advance each output by4 but keep its **initial cached base**. After each
group reread D_800D23B0 and count+EA4. Neither bound can be flattened to a
pre-loop count. Both loops skip nonpositive counts; retain every ordered
store and the reused zero index. Array locals are named by confirmed offsets,
not speculative higher-level roles or claimed original source names.

Use a no-argument void operation, not the false zero-return placeholder.
The original V0 contains incidental array-pointer state rather than a
consistent numerical status. Its direct caller at **1509E0F8 / CB5A8**,
JAL0D423687/NOP in CB3D0.s /func_1509DFC4, physically propagates that state
through a branch, RA/S0 restoration and SP+48 epilogue. Do not authenticate
an original C prototype or invent a success flag from that alone. Complete
normalized instructions preserve the literal V0 state too; raw void C has
no promised numerical return. The caller's C remains a separate stub.

## Explicit Layout

Twenty-nine structural source forms compare indexed/pointer loops, index
initializer placement, cursor reuse and declaration order. Initial C emits
54 words/frame16; pointer-walk forms lose the original shape. The accepted
indexed form places the genuine first-loop index initializer before the last
cached output and uses a direct current-context expression in the second
bound. It emits **52 words/frame8**,19 real differences, two bindings and
empty diagnostics in both existing owner profiles. Subsequent offset-only
local renaming emits the identical raw code. No dummy operation, volatile,
physical-register binding, frame patch or compiler-profile change.

`game_parallel_array_reset_layout.py` specifies only pointer/register roles
and the independent second-loop setup copies:

- Restore the early array/index-cursor allocation while keeping the global
  address, context, counter and S0 roles. Decode actual GP fields, never
  immediates, shift amounts or zero registers.
- Keep the bound branch at28. Origins29..33 become30,29,33,31,32. Restore the
  original10F0-pointer copy in the delay slot, defer the F70-pointer copy to
  the taken path, and restore independent constant/pointer-copy order.
  Only scratch-register copies cross that conditional boundary; no memory
  access, branch predicate or displacement moves. This also restores the
  original skipped-loop scratch/V0 state, not a new C return contract.
- Restore the second-loop pointer/constant allocation. Retain all52 source
  origins exactly once, with both HI/LO bindings still at4/8.

The19 expected-word/expected-relocation rows insert or omit nothing. Exact
raw bytes, binding dictionary and normalized SHA gate the closed recipe;
installation also requires the exact qualified source, old manifest prefix
and first-image receipt. Original assembly, retained data, Makefile and
shared padder are untouched.

```text
raw:        e1044cf33288b566d09ddaefd2a95eabca0ba295540ad44f5640058d22036bf4
normalized: 7f154a2e849808aa06216d80c7e1518184b1fe74ff644dfc4c0976b5cfa7363d
```

## Fresh Qualification

The final offset-named source passes **10 pre-install tests in27.999 seconds**
and **10 installed tests in33.908 seconds**, without skips. Reused map/caller
fixtures and raw/normalized executions are not additional independent domains.

- **864 fixtures/two phases:1,728 paired literal executions** agree in full
  GP/FP/LO, private/public memory, ordered events and residual return state.
  Dynamically visit and statically compare all52 words. The same corpus
  checks the raw C object's public memory and **ordered stores** against an
  independent reference, without assigning meaning to V0.
- Four guest-only alias layouts overwrite global context-pointer storage
  with0 during either the early or late stores of either the first or
  second group. **672 phase executions fire a context redirection**. Outputs
  remain on their original bases while the next count comes from the newly
  mapped current context. Null-pointer arithmetic aliases are not portable
  C/native claims or real gameplay behavior.
- **222 fired access-cut pairs**, with every requested cut confirmed, plus
  two huge signed-count prefixes. A separate first-store alias writes -1
  into context-pointer storage; cut5 fires before the ensuing unaligned
  count read at0000000F. Both literal states and the requested address agree.
  Do not claim a completed huge scan, an executed invalid read or a hardware
  exception. The gate fires before the model's alignment check.
- Effective cached-bound C controls: caching the second count changes public
  output on a completed mapped alias; caching the first changes cut5's next
  count address from0000000F to00000EA3. The latter is an access-order
  negative, not a completed native functional negative or hardware fault.
- Native32 **O0, O2 and O2+UBSan** each pass **384 fixtures**, checking all
  1,280 numerical words per buffer, including unchanged fields/padding.
  Generate endian-neutral expected word patches from the independently
  guest-checked reference. Back first counts through48 and second counts
  through32; negative/zero counts include INT_MIN. Retain stack realignment
  and no-strict-aliasing harness policy.
- Five executed native source negatives change the first fill, one-valued
  array, second bound field, final zero fill or first-bound equality. Each
  exits21; positive profiles exit0. No crash/trap is counted as success.
- **100 actual caller-window pairs** execute eight retained words: JAL/delay,
  branch/RA reload, S0 restore, SP adjustment and JR/delay. The caller frame
  is an explicit live-in; no earlier dispatch/full-caller execution is
  claimed. Check literal residual state and preserved saved registers.
- **Three independent GNU maps** agree for all52 words and both bindings,
  including HI/LO carry boundaries. Execute **348 mapped cases** with code,
  global pointer storage and ordinary/aliased contexts rebased.
- Seven raw/binding/recipe corruptions reject. Six actual-padder manifest
  corruptions fire stale-word/relocation checks; three changed-image controls
  fail the strict verifier. Both owner profiles preserve72 neighbors and
  normalized pools; actual padding preserves those bodies/addresses/pools.
  All seven expanded shadow Make commands agree.

## Production And Commits

The first private link matches its exact complete-image prediction on the
first attempt. Production Make reproduces the same3,257,636-byte ELF:
**161 changed bytes =160 target-code bytes +one target-symbol size byte**
(12 ->208). No metadata permutation or broad exclusion. Every other6,056
linked body, every address, all189,088 protected Game-data bytes /720 owners,
historical guard bytes and other frozen inputs stay fixed.

The manifest-triggered rebuild succeeds with inherited duplicate
generated_12D630 recipes and diagnostics from untouched code. Both target
owner profiles have empty diagnostics, not the whole build. Full ignored
log: `conker/build/game-parallel-array-reset/integration/production-build.log`.
Git's existing CRLF advisory is not a CSV or build failure.

```text
owner:  3bd649eeedd4e6bf5fe3fed8de0f2e6446cacfe5155bce52f3e54b5e97c31791
guards: 0cca1083e8dc92310a3b170d9774cb7a2f7c5d07bbbe6528f4e0550067813333
ELF:    6777c5ec8ffd50a7e30a4e1c80fe44ef40de9ce4e177c5208c7d0886907cb995
```

Fresh matching: **Game3003/4832 (62.15%)**, **total3676/5505 (66.78%)**,
Init492/492, Debugger181/181, **1,829 different / zero drift**. Conversion
counts/bytes remain5505/6044 (91.08%),86.08% overall and4832/5323 (90.78%),
85.44% Game: the old placeholder was already counted as C. README aggregates
only; this note owns the function narrative.

Both tools copies pass three setup tests and smoke checks; consumer
`make tools-check` passes. Five new files are identical ASCII/Python-valid
in the standalone mirror. Preserve its ddbdd16 HEAD and all1,338 prior dirty
leaf hashes; add five task files for1,343 dirty leaves, without mirror commit
or reset. Post-commit graph preservation is separately retained in ignored
`integration/graph-audit.json`. No compiler capture, Claude call, REA setup,
sibling host or frozen Release action.

```sh
python3 -m unittest tools.tests.test_game_parallel_array_reset_match -v
python3 -m tools.experiments.game_parallel_array_reset_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

Fresh owner audit: **55/73 exact,18 different**; complete remaining list in
ignored `integration/owner-completion.json`. Continue **func_1508DAEC**, VA
`1508DAEC..1508DC24`, ROM `BAF9C..BB0D4`: **78 words/frame0**,74 real
differences, still a false zero-return stub.

Recover full-word slot/mode inputs, null-context and negative-record rejection,
and the negative-mode query that returns1 without clearing. Nonnegative mode
first clears EB0[slot], then checks record flags+11F4 mask0x2. Keep that early
clear even when the flag rejects further work. Clear F70/10F0 with fresh
context reads. Mode1 sets300 at12F4 and stores truncated actor X, Y+50.0f and
Z at1374/13F4/1474, then uses4 at1070; other nonnegative modes use captured
EAC at1070. Preserve all reload/store order and FP truncation boundaries.

There are **six distinct direct JAL sites**, not nine after duplicated
nonmatching assembly is counted:1508AB28,1508E520 (B3020.s),1509E11C (CB3D0.s),
150ED904,150ED92C,150EDA58 (11A680.s). Add that last caller file to the next
frozen inputs: SHA256
`54a63a8903fd59c8b04b3fcb671926dfac0ba82a81b953280d5311092ee4a94c`.
Derive precise argument/return contracts and native versus guest FP/index
domains before installation. The broader Game decomp/matching goal remains
active; no whole-owner completion is claimed.
