# Game particle state dispatcher guarded match

Date: 2026-11-14. `func_15176B84` is recovered in
`conker/src/game/generated_1A20A0.c`. Its complete **155 words / 620 bytes**
match retail after **32 checked guard rows**, with **no inserted or omitted
instructions**. Semantic C already emits 155 words and the original
**0x20-byte frame**, saved S0/RA homes and epilogue. Owner **7 / 9 C-exact**.

VA **0x15176B84..0x15176DF0**, ROM **0x1A4034..0x1A42A0**.
Derivation: `tools/experiments/game_particle_state_15176b84_match.py`.
Raw text SHA-256:
`48c966ca7c378cbbf975486add81e1d23296ca84f1f8c61ddc80f00edfc35be8`.
Baseline consumer `03cea508`, mounted tools
`e65d090dfc65ae6d2656ab31735319f5cf07b26b`.

## Contract and recovered behavior

The callback takes one pointer to the **248-byte** particle view and returns
void. Its four authentic registry slots are **0x8008B8EC**, **0x8008B920**,
**0x8008B954** and **0x8008B988**, ROM
0x2303AC/0x2303E0/0x230414/0x230448. No direct JAL names the target.
The generic update dispatcher supplies the pointer through its real five-word
window at **0x15167164..0x15167178**. The larger delegated
`func_15175958` remains an opaque, uncredited provider boundary.

The opening short-circuit model/control gate retires absent or disabled
variants. Model rows are five pointers wide; the explicit row view recovers
the original 20-byte indexing without changing other routines' flat views.
The record slot's live flag starts fading by setting F1; that transition
does not also change alpha during the same call. Otherwise alpha rises toward
255 or falls toward zero, retaining unsigned 32-bit wrap before the original
signed clamp comparisons. An already empty fading particle retires early.

The active marker is stored through the current variant before reading state
91. State zero truncates actor/particle X/Z into the actual four-word distance
packet. A signed result below **200** sets state 2 before calling the RNG.
The signed-halfword divisor and base height are read after providers, and the
near model uses the late live variant at `D_800DDE88`. Far results use the
second model field at `D_800DDE84`. State 4 retires only for the ordered
below-ground comparison; other states delegate to the larger updater.
The E4 record field is now named **`targetHeight`**. No shared header changes.

## Why the private direct-match draft was superseded

The private draft in [Note 2448](2448-game-model-vertex-wave-guarded-match-20261114.md)
matched all 155 words directly under IDO, but its ordinary unsigned-to-float
cast did not preserve retail rounding under the native compiler for every
full-width remainder. For example, before adding the base height:

```text
unsigned remainder 0x80000081
retail signed float32 conversion, then float32 +2^32: 2147483648
ordinary native unsigned float32 cast:                2147483904
```

The full signed 32-bit RNG return and negative signed-halfword divisor
transport are retained. Those cases are not removed from the corpus. Source
now makes the two stages explicit: convert the signed interpretation, then add
**4294967296.0f** when its sign bit is set. A native negative control restoring
the old implicit cast fails at **O0, O2 and O3**. The earlier draft was never
installed or credited. This note supersedes that private direct-match handoff.

The explicit source still emits 155 words, but changes a seven-word conversion
join and caller-temporary allocation. The normalizer pins all **155 raw words**
and **24 named binding sites**, rejecting **179 altered-word/binding controls**.
It reads no retail words while transforming a candidate. Six changed words
restore the conversion join; 26 instruction words restore only caller GPR/FPR
roles. Saved registers, frame, constants, named bindings and all other memory
offsets stay fixed. Exactly **32 rows** append to the existing manifest.

`tools/tests/game_particle_state_15176b84_proof.py` symbolically executes both
sign paths from conversion through the height store. It proves one signed
base-height read, one variant read, the same finite height expression and
store, the same live model address, and unchanged saved roles. The source's
phi move and retail's duplicated branch-delay load implement the same public
events. The final commutative add has finite operands derived from signed
integers, the exact 2^32 correction and a signed halfword; NaN equivalence is
not assumed. The small static guard ledger restores the actual retail stream.

## Completed qualification

- [x] **841 independent guest cases** compare full public memory, all provider
  packets and **248-byte record snapshots at every call**, across retail,
  explicit raw C and the actual guarded object. They cover gates, alpha
  boundaries and wrapping steps, all 256 state bytes, ordered ground cases
  including NaNs/infinities, provider mutations and sparse byte indices.
- [x] **16 zero-divisor cases** stop at the actual pre-division boundary.
  They verify the preceding state store and RNG packet without claiming C
  modulo-by-zero semantics or executing a hardware division fault. Signed
  divisor extremes and high unsigned remainder rounding remain covered.
- [x] Guest aliases include active-marker stores into the record state and
  record/model-table overlap. Provider model writes preserve the real overlap
  of table, live, active and control bytes. All late reads are compared.
- [x] **128 authentic registry-dispatch executions** cover all four entries,
  argument transport, bookkeeping and saved registers. This is the real
  dispatcher window, not a claim of full parent/provider execution.
- [x] **82 target-memory prefixes** compare full guest memory, GPRs, FPRs,
  calls, snapshots, traces, HI/LO and delay-slot state for retail/guarded code.
  The corpus visits **152 / 155 words**. Offsets **0x5C** and **0x228** are
  unreachable duplicate loads; **0x1B0** is the break after the separately
  bounded zero divisor. All 155 words remain literal/corruption-checked.
- [x] Five effective emitted controls reject distance threshold, fade
  direction, active marker, far-model selection and unsigned correction.
- [x] **597 native32 cases per O0/O2/O3 profile**, with undefined-behavior
  traps, compare 248 record bytes, 55 table words and their valid model views,
  11 control words, 12 live bytes, 16 active bytes, step/marker values,
  helper packets and record snapshots. Five effective source controls include
  the old implicit cast, distance boundary, marker, fade and model selection.
- [x] Both complete-owner padders pass **four independent GNU layouts /
  twelve links**, including code/data rebases and low-half carries. All nine
  functions and owner pools agree. The eight other raw and padded functions
  and bindings remain unchanged.
- [x] Actual Make's three recipe commands reproduce the independent owner.
  Strict-image prediction, installation, production rebuild/audit and fresh
  actual-ELF recount pass. Post-install suites pass in mounted tools and the
  isolated sibling overlay; shared `make tools-check` passes.

Native tests use valid variants 0..10 and slots 0..11 with distinct record
storage. Sparse helper table writes are projected into bounded native objects
to reproduce their guest effects on model/live/active/control fields. Guest
pointer aliases and zero-divisor prefixes do not expand that native contract.
Provider behavior is bounded; raw fault-register order, full provider internals,
FCSR exception behavior, hardware and host gameplay are not acceptance claims.
Routine Claude calls: zero.

Reproduce with the prepared consumer and retained ignored baseline:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_state_15176b84_match -v
make tools-check
```

The isolated sibling overlay copies **six byte-identical task files**, using
sibling dependencies and mounted fallback without writing to `64CBFD Tools`.
Its HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439 dirty
paths** and before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are preserved. The Windows Graphify refresh uses Python's safe-path option
because an ignored scratch `select.py` would shadow the standard module.
No dependency installation or graph-tool upgrade is required.

## Linked image and progress

All **803 immutable inputs** in the **807-input** baseline remain fixed,
including 82 headers. Source, guarded owner, guard CSV and ELF are the four
declared changes. Only `generated_1A20A0.c.o` changes among **698 objects**,
in `.text`, `.rel.text`, `.symtab` and `.strtab`. Conversion rows stay exact;
all previous guard bytes remain unchanged.

The production ELF equals the independent prediction. All **6,051 function
addresses** remain fixed; only this body and its 12-to-620-byte symbol extent
change. There are **486 changed image bytes**, **zero exclusions**, and one
fully accounted closed metadata permutation:

```text
D_800DDE84, D_80082E98, D_8008FD38, D_80000008
    -> D_80082E98, D_8008FD38, D_80000008, D_800DDE84
```

All **189,088 protected bytes across 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`aa20f897be4545642a0a8f0c521bf67bcdc65b4183e522ff1a6ccf3c2547e4ac`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,492 / 5,515 (81.45%)** | 0 | 1,023 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,819 / 4,842 (78.87%)** | 0 | 1,023 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted functions remain **5,515 / 6,048 (91.19%)**, converted bytes
**86.17%**. One new match is credited; **196 more matches** reach 85%
at this denominator. The wider goal remains active.

Scoped Graphify AST refresh covers six tools files and the owner, retaining
all **60,898 old IDs**, with zero lost nodes: **60,938 nodes / 114,590 links**.
This is a scoped merge, not full-corpus re-extraction. Tools commit `b0d17ba555f62e5a36a090c8b23ea967d8b017a0`
precedes the consumer commit. Root README receives aggregate rows only; no
push. `64CBFDOGL` has no source checkout here, and Release remains frozen.

Next focused target: **202-word `func_1517685C`**, VA
**0x1517685C..0x15176B84**, ROM **0x1A3D0C..0x1A4034**, frame **0x20**.
Begin with its complete state-machine contract and caller entries, retaining
the 961-word `func_15175958` as an uncredited delegated boundary.
