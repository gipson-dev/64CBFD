# Game Actor Burst Consumer Semantic Recovery

Verified locally: 2026-10-14, including a fresh session-restart check. This is
an uninstalled research checkpoint, not an exact match or host-gameplay claim.
Keep the wider Game goal active and continue with the same function.

## Target And Baseline

- `func_151A6F00`, owner `conker/src/game/generated_1D43B0.c:7`.
- VA `0x151A6F00..0x151A73EC`, ROM `0x1D43B0..0x1D489C`.
- Complete retail routine: 315 words / 1,260 bytes, frame `0x168`.
- Consumer baseline `3fa3e6e8141e36f2c061e48f1809dbd2f83dcaeb`;
  previous tools `23e45f5ece7ad270f6753dfbc5291f90704009d3`.
- New tools `ce205ae04bb97d1cdee5a30af8098f800df83ef8`, banked first.
- Production owner, caller, whole ELF, guards, conversion rows, Makefile and
  original assembly remain byte-for-byte unchanged. The consumer's production
  body still returns zero; the recovered candidate is not installed.

Ignored before snapshots and pinned SHA-256 manifest are in
`conker/build/game-actor-burst-consumer-recovery-test/`. The whole ELF remains
`50b064c6d7af59a7a78eeece1a2b3c8e32b2886b1695097fd6b43044f2b092ee`.
Do not advance frozen production fixtures for this research-only checkpoint.

## Recovered Semantics

The candidate covers the complete routine, not just the previously qualified
kind-1 caller. Recover byte-sized kind/slot arguments, signed count and range
fields, descriptor initialization, four velocity branches, allocation failure
paths, payload copy, animation submission and retained-scale copy.

The count branch tests the old value and decrements the signed short:

```c
s16 remaining = params->count;
while (remaining--) {
    /* Complete recovered body. */
}
```

Count 3 produces three objects. The m2c initial `count - 1` interpretation
produces two and is an effective negative control. Callbacks changing the input
count do not change the snapshot. Signed negative counts are qualified only
through a bounded three-iteration factory prefix, not a full 65,535-iteration run.

| Kind | Velocity Path |
| --- | --- |
| 0 | Separate randomized planar and vertical speeds; two random-float calls |
| 1 | Randomized spherical velocity; one random-float call |
| 2 | Raw three-word direction aggregate copy; no velocity random-float call |
| 3 | Supplied direction multiplied by randomized speed; one random-float call |
| Other | No velocity assignment; preserve unwritten bytes |

All paths retain two unsigned remainder-based angles, four trig calls,
randomized spherical position, scale, extra coefficient and two independent
acceleration samples. The object factory takes six arguments, including the
16-byte payload size. On success, copy the payload to object+0x170 and construct
the 28-byte animation packet. Reload descriptor+0x0C after factory/copy for the
15x animation rate; keep the earlier retained scale for the final four-byte
copy. Animation failure still writes a null attachment.

## Private Layout And Word Boundary

Natural reordering of existing used variables recovers all four retail homes.
Move the real `horizontalSpeed` declaration before the extra payload and move
the real created/attached pointers before the animation aggregate. No dummy
padding, unused declaration or larger invented animation structure is added.

| Local | Retail | Selected Candidate |
| --- | --- | --- |
| Creation descriptor, size 0x78 | SP+0xE8 | SP+0xE8 |
| Extra payload, size 16 | SP+0xD4 | SP+0xD4 |
| Retained scale, size 4 | SP+0xD0 | SP+0xD0 |
| Animation packet, size 28 | SP+0x8C | SP+0x8C |

Selected `private-float1-pointers1` remains **311 words / frame0x168 / 274 raw
positional differences**. The matching frame, homes, semantics and seeded
packet bytes do not establish instruction or complete machine-state identity.
These are not 274 independent scheduling fixes: the four-word length difference
also shifts later instructions. Do not pad or add broad instruction guards.

Four declaration controls distinguish the payload/scale and animation homes
independently. Their byte comparisons are effective even when raw difference
counts stay equal. A 315-word double-literal control introduces double-precision
COP1 operations absent from retail and is rejected. Three used local-constant
controls remain 311 words, enlarge the frame to0x170 and give280 differences;
they do not fix retail's cached float-constant lifetimes.

Archived screen receipts live in `conker/build/game-actor-burst-consumer/`:
separate locals, reused locals, byte arguments, structured forms, literal forms,
private layouts and the latest constant-local measurements. They are experiments,
not matching credit or committed game artifacts.

## Fresh Qualification

The restored nine-check checkpoint passes in24.454s. The expanded target suite
then passes **10 checks in37.065s**. Two protected-text checks pass in1.478s;
the ROM-free match-progress helper check also passes. Both tools copies pass
`check_project_tools.py` and Windows byte-compilation of the two new modules.

- **960 guest cases:** kinds0/1/2/3/default plus masked upper-byte kinds,
  counts0..4, three allocation outcomes, callback mutations, two SP phases and
  two stack seeds. Independent initialized-field reference and original/candidate
  creation packets, animation packets, actual copied bytes and private homes agree.
- **18 signed-count domains:** actual third-factory stop fires, with two prior
  allocations and the third descriptor observed. Complete long-running negative
  counts and their native narrowing behavior are not claimed.
- **Four zero-divisor guest prefixes:** the real emitted BREAK7 fires after one
  or two RNG calls, before allocation. Empty counts skip division. Native C
  division by zero is explicitly excluded.
- **108 native32 cases per profile, O2 and O0:** independent RNE-reference call
  hashes, count snapshot, every kind path, factory/animation outcomes and rate
  feedback agree. Warning gates, SSE, stack realignment, no-strict-aliasing and
  disabled FP contraction remain enabled. Do not inspect native unwritten bytes.
- **32 raw direction cases:** mode2 copies signed zeros, infinities and NaN
  payload words without arithmetic. A scalar-float-copy control preserves the
  bounded public result but changes emitted words; that is a shape control,
  not an invented semantic failure.
- Effective bad-count and double-instruction controls remain rejected. Complete
  original/candidate machine states remain different despite packet agreement.
- The entire production ELF and the six recorded source/manifest/assembly inputs
  remain unchanged, and the production placeholder is explicitly asserted.

RNG, random float, trig, object factory and animation factory remain bounded
hooks. The original 11-word memcpy executes where reached. Reuse Note1352's
unchanged original-consumer assembly/link/ROM-identity and 18 installed producer
checks explicitly as prior receipts, not fresh full-producer tests.

These domains do not establish full hardware FCSR/rounding behavior, all-input
semantics, public/private alias order, instruction-fault states, owner padding,
independent relocation carries or complete caller/gameplay qualification.

## Banking And Next Work

The old standalone tools mirror stays at ddbdd16; all459 initial dirty-file
fingerprints are preserved. Copy only the two previously absent new modules,
which compare byte-for-byte with the active tools checkout. Its461 dirty paths
are not a request to commit/reset its unrelated work.

Fresh read-only matching measurement remains Game2,832/4,823 (58.72%),
total3,505/5,496 (63.77%), different1,991, drift0. Init492/492 and Debugger181/181
remain exact. No root README change is needed because aggregate status is fixed.
No push, host build/launch, dependency install or frozen Release change occurs.

The full Graphify update safely refuses an18,870-node replacement for the
existing40,638-node graph. A scoped nine-path refresh succeeds with40,648 nodes
and81,130 edges, preserving19,398 nodes from2,972 still-present excluded files.
The new handoff is indexed, but current root filters still exclude the two new
tools modules; a direct graph-file check confirms zero nodes for those paths.
Use their source directly. Do not force a smaller graph or change unrelated
ignore rules to conceal this coverage limit.

1. Continue this same315-word consumer. Compare cached15/30 float lifetimes,
   branch-specific scratch reuse and the initialization/load schedule against
   complete retail instructions. Keep natural complete source forms.
2. Require complete word/state and applicable alias/fault/owner/link gates
   before production promotion. If shared packet ownership is introduced, use
   a narrow header and qualify the unchanged67-word producer as well.
3. Only then install, rebuild and close the whole-image/progress audit. Keep
   current matching totals unchanged until that audit actually passes.

```sh
python3 -m tools.experiments.game_actor_burst_consumer_candidates --filter private-
python3 -m tools.experiments.game_actor_burst_consumer_candidates --filter constant-locals
python3 -m unittest tools.tests.test_game_actor_burst_consumer_recovery -v
```

The restart also confirms the connected REA6.4.0 server,170 tools and available
Ghidra/Java checks without configuration changes. See
[the setup boundary](../REVERSE_ENGINEERING_SETUP.md): provider readiness does
not remove the previously observed Windows adapter MIPS ELF restriction.
