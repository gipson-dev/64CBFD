# Actor transformed/world-position query recovered directly from C

Verified 2026-11-01. `func_1507E1D0` in `game_A9D90` now emits all **53 body
words**, its natural **56-byte frame**, and three original alignment words
directly from C, **without word guards**. Total **4,036/5,507 (73.29%)**, Game
**3,363/4,834 (69.57%)**, zero drift and1,471 different. The 4,131 threshold
requires **95 more matches**. The C inventory and converted-byte totals are
unchanged; this adds one exact C function. The wider goal remains active.

## Semantic body and interface

The retail span is VA `0x1507E1D0..0x1507E2B0`, ROM `0xAB680..0xAB760`:
212 body bytes plus12 alignment bytes. The false integer-returning zero stub
and local placeholder declaration are replaced by:

```c
void func_1507E1D0(struct127 *actor, f32 *x, f32 *y, f32 *z);
```

With an attached matrix, the function forms `{0, actor->y_scale * 30, 0}` and
transforms it through `func_15143134`. Interaction state1 selects matrix+0x300,
state30 selects matrix+0xC0, and other states select the base. It then writes
X/Y/Z in order. Without a matrix, it reads the actor's live world coordinates
after each preceding store. The transformed path captures the z pointer before
the first store and reloads the y pointer afterward; guest aliases preserve
that order. The helper uses the existing three-pointer void interface. Only a
correct local helper declaration is added; no shared header is changed.

The original assembly stays in place. Descriptive names and the short semantic
comment replace the placeholder without renaming its original public symbol.

## Compiler scope resolves the missing word

The earlier best source declared both vectors at function scope and emitted
52 words/frame56/22 differences. The old handoff's missing-constant hypothesis
was incorrect: its unreachable duplicate `li AT,30` already existed in emitted
C. The remaining mismatch involved branch scheduling and RA restore placement.

Supported profile checks ruled out a simple build-profile fix: O2/g3 and O2
both emit52/frame56/22; O1 gives66/65 differences, `-g`74/72, O0 78/76. A draft
O1/g3 screen was rejected by the assembly processor and is not a valid compiler
comparison. The refreshed screen records only the supported profiles.

With the matrix local still outside the conditional, declaring `offset` and
`position` **inside the non-null matrix branch** recovers all53 words exactly.
Putting all three locals inside also matches, but the selected source keeps
the smaller scope change. The original outer branch, RA loads and epilogue
now emit naturally. No constant, filler, instruction insertion or guard is used.

Other fresh semantic forms were ineffective: switch53/28 differences,
independent state tests51/38, member addresses52/22, null-first and single-pass
forms52/47, boolean switch53/40. IDO rejects the nonconstant aggregate initializer;
that failed draft is not credited. Scope changes affect the compiler's internal
representation, but the specific responsible pass was not separately traced.

Selected raw SHA-256:
`8909bfb4b897b226be9f6b0a537a5c7cb4db94424ca4d81b934f4bd5dd68adf5`.
The complete raw payload and its one helper-call binding equal assembled retail.

## Runtime, original helpers and actual callers

- **3,584 guest cases / 14,336 executions**, three address layouts and seven
  alias layouts. Original ASM, isolated C, padded owner and actual-Make programs
  agree in complete state and trace. Tests cover live fallback reads, incoming
  homes, scratch-vector aliases, helper mutations, all matrix selectors, signed
  zero, and preserved GPRs/FPRs/SP. All52 reachable words execute. The53rd word
  is the unreachable duplicate constant after the first selector's branch.
- **79 access-prefix cuts / 316 executions** preserve complete machine states
  and access order. They qualify guest ordering, not portable-C faults or
  hardware EPC/FCSR behavior.
- **1,536 connected-helper cases / 6,144 executions** run both original and
  retained98-word `func_15143134` bodies. The original46-word fixed converter,
  40-word point transform and49-word translation helper are connected from the
  retail ROM. All transform and translation words execute. Zero-offset and
  nonzero-offset paths, floating and fixed matrices, all selectors and public
  aliases agree with the independent reference. Full FCSR/NaN payload and
  physical gameplay acceptance are not claimed.
- Native32 **O0/O2/O3** each pass **2,048 cases / 16,384 executions** including
  seven negative variants. UBSan, full-actor checks and output canaries pass.
  Four portable float-field alias layouts are checked. Incoming-home/private
  scratch aliases are restricted to the guest tests. All seven wrong scale,
  selector, coordinate, cached-live-read and input-offset controls are detected.
- The complete aligned ROM scan finds two direct JAL sites, no direct jumps
  and no literal pointers: `0x1507CB80` in `func_1507C8FC` and `0x15124E94` in
  `func_15124C38`. **2,048 cases / 8,192 executions** run both original windows
  with actual argument setup, branch gates and output consumers. All27 window
  words execute. Four return poisons confirm that the root result is ignored;
  the recovered interface is void. The large parent functions are not fully
  emulated by these bounded windows.

## Production and complete-image evidence

All **15 raw and padded owner neighbors**, normalized pools and zero-warning
diagnostics remain unchanged. The actual five-command Make recipe, including
the owner's existing `jtbl_8009B884_game` binding, reproduces the qualified
object. Six focused tests and the shared tools check pass in both checkouts
before and after production installation. Runtime reuse is bound to the
complete oracle bytes, selected C, raw hash, frozen input index, raw/padded
objects and first linked ELF. A26-artifact canonical manifest pins preparation.

The independent complete-image predictor changes only the target's224-byte
slot and its ELF symbol extent12->212. The ELF length stays fixed. All6,053
executable addresses and6,052 other bodies are unchanged. No overflow body is
removed or moved. Guard CSV and linker map are unchanged. The private map
comparison normalizes nine shadow-object paths and one output path; the
production comparison requires literal equality to the unchanged map.

Protected Game data remains **189,088 bytes / 720 owners**, exact. Complete
sealed-input review before documentation finds only the target source, owner
object and ELF changed, with zero unplanned dependent objects or exclusions.
An independent recount reads the adopted Windows-checkout ELF. New ELF SHA-256:

`2b585aabd9bfae2d0851db1f9c8b140dd3a31f08622da19c055216fc3244b0bb`.

Evidence: `conker/build/game-actor-transform-position-1507E1D0-match/`, including
`profile7-results.json`, `shape9-results.json`, `preparation.json`,
`runtime-qualification.json`, `caller-runtime.json`, `public-preinstall.json`,
`production.json`, `installed-audit.json` and `native-install.json`.

## Continuation

Continue the remaining Game queue toward75%. `func_150174C0` remains private
with the declaration/loop/return-interface gaps recorded in [Note1965](1965-private-codegen-audit-and-spherical-vector-preparation-20261101.md).
Do not credit it or the other parked candidates before their complete gates.
All older private experiments, original assembly, dirty tools-mirror work,
archives and the host-port Release checkpoint are preserved. No push is
requested or performed.
