# Game particle rise and idle callback guarded match

Date: 2026-11-14. `func_1517685C` is recovered in
`conker/src/game/generated_1A20A0.c`. Its complete **202 words / 808 bytes**
match retail with **123 checked guard rows**, with no inserted or omitted
instructions. Semantic C emits 202 words and the original **0x20-byte frame**,
saved S0/RA homes and final epilogue. Owner **8 / 9 C-exact**.

VA **0x1517685C..0x15176B84**, ROM **0x1A3D0C..0x1A4034**.
Baseline consumer `bf2fc489aefa846d93d00ba3e459ab22f24050cc`, mounted tools
`b0d17ba555f62e5a36a090c8b23ea967d8b017a0`.
Derivation: `tools/experiments/game_particle_rise_1517685c_match.py`.
Raw text SHA-256:
`f9a0b87ff7817b19e5d206ff37c857e7357ea789ebc2c0271a55095464467660`.

## Contract and recovered behavior

The callback takes one pointer to the **248-byte** particle view and returns
void. Its only registry pointer is at ROM **0x230344**, VA **0x8008B884**,
descriptor index 19. There are no direct JAL callers. The authentic generic
update window at **0x15167164..0x15167178** transports the pointer and updates
the bookkeeping value. The delegated **961-word `func_15175958`** remains an
opaque, uncredited provider for this qualification.

A cleared live-slot byte retires the particle. Otherwise the callback writes
the active marker through the current variant before reading state 91.
State zero submits four truncated signed X/Z coordinates to the distance
helper. A signed result below **400** sets state 1 before RNG, then writes
B4 to -1 minus the low two random bits and tilt to **-8.0f**. That call returns
without running the common updater.

For a distant particle, a nonzero tilt step advances tilt. A negative step
also advances heading by angular rate. Tilt above **45** reverses the step to
**-5**; otherwise a negative step above **25** can reverse to **+5** when the
low random byte is below **51**. The final live tilt read at or below **10**
stops the step, including after an RNG provider changes the record. A zero
step uses a random-byte threshold of **25** to restart at +5; the subset below
**13** chooses angular rate using **unsigned remainder modulo 6, followed by
signed subtraction of 3**, giving -3 through 2. The other restart path clears
angular rate. The recovered CC member is named `tiltStep`; this member rename
does not change any neighboring emitted function.

State 1 reaches its transition at Y >= **300.0f + groundHeight**. It writes
state 2 and performs the two original flag updates, clearing bit 0 and then
setting bit 2, before RNG. The target height uses low seven random bits plus
a **fresh** 300-plus-ground-height expression after RNG. The common helper
runs on both sides of this comparison. Other states steer B4 toward the
target height with -1.5 or +1.5, retaining B4 on the remaining path, then
delegate. B4 retains its generic field name until the common updater is
recovered; a physical role is not inferred from this callback alone.

## Closed normalization and return proof

An initial early-return shape emitted 201 words. The live outer gate and a
bounded 128-candidate zero-literal/marker-type screen recover 202 words and
the original frame. The selected shape has **123 raw word differences**.
All eight neighboring raw functions and owner pools remain unchanged.

The source-pinned normalizer reads no retail words to transform a candidate.
It validates the complete raw digest and **15 named binding sites**, rejecting
**217 altered-word/binding controls**. Its order ledger uses all **202 source
words exactly once**; 104 positions move. Field edits affect **43 instruction
words**, only caller GPR/FPR roles. Saved roles and frame remain fixed.

The active marker's literal one is reused by the first switch comparison.
The redundant raw `LI AT,1` at **0x40** and the raw NOP at **0x1C4** become
the original two `LW RA,0x1C(SP)` return loads. The original common restore
remains. One false FP branch becomes false-likely so the added return load
executes only on that return edge; the other return moves its store before
the unconditional branch and restores RA in the delay slot.

Five pinned edge-entry adjustments accompany the permutation:

| Raw branch offset | Raw destination | Normalized destination |
| --- | --- | --- |
| 0xB0 | 0xE8 | 0xE4 |
| 0x140 | 0x158 | 0x150 |
| 0x1C0 | 0x314 | 0x318 |
| 0x1F0 | 0x224 | 0x224 |
| 0x228 | 0x314 | 0x318 |

The proof checks the closed non-return operation inventory after the two
redundant preparations become restore loads, the complete named binding
multiset, and named call order. A bounded epilogue proof checks the three
return paths, the FP branch's two outcomes, SP/S0/RA restoration and final
memory/store transport. The guarded stream matches all 202 literal retail
words. Each CSV row checks its raw word and relocation provenance; none
inserts or omits an instruction.

## Completed qualification

- [x] **1,936 independent guest cases** compare full public memory, helper
  packets and complete 248-byte record snapshots across retail, raw semantic
  C and the actual guarded object. Cases include all 256 state bytes,
  thresholds, signed zero, guest NaNs/infinities, unsigned RNG values and
  provider mutations. Providers clobber caller GPRs/FPRs, HI/LO, outgoing
  argument homes and the FP condition boolean.
- [x] Guest aliases cover an active marker into record state and record/model
  table overlap. Sparse provider writes reproduce model/live/active/control
  byte overlap. Late tilt and ground-height reads are independently covered.
- [x] **64 authentic registry-dispatch executions** qualify the one registry
  entry, argument transport, saved state and real bookkeeping. A missing-store
  negative control is rejected from a nontrivial initial bookkeeping value.
- [x] **85 target-memory prefixes** compare full memory/register/call/trace
  state for retail and guarded code, including delay state and the FP
  condition boolean. Public paths visit **200 / 202 words**; 0x14C and 0x2D4
  are unreachable duplicate loads. Both words remain literal/corruption-checked.
- [x] Five effective emitted controls reject distance boundary, idle
  threshold, flag transition, steering sign and tilt clamp changes.
- [x] **1,378 native32 cases at each O0/O2/O3**, with undefined-behavior traps,
  compare all 248 record bytes, 55 model table words, 11 control words, 12
  live bytes, 16 active bytes, step/marker values, packets and snapshots.
  Five effective source controls include signed instead of unsigned modulo.
  The late ground-height provider mutation passes all three profiles.
- [x] Both complete-owner padders pass **four independent GNU layouts /
  twelve links**, including code/data rebases and low-half carries. All nine
  functions and pools agree; the eight other raw and padded bodies stay fixed.
- [x] Actual Make's three recipe commands reproduce the independently compiled
  raw/padded owner. Strict-image prediction, production rebuild/audit and
  fresh actual-ELF recount pass. Mounted post-install qualification and
  shared `make tools-check` pass.
- [x] The isolated sibling overlay passes the same focused suite and preserves
  sibling HEAD and all pre-existing dirty paths. Its terminal result is
  retained separately from the earlier replay whose output was lost.

Native coverage uses finite FP inputs, valid variants 0..10 and slots 0..11,
with distinct record storage. Sparse guest model writes are projected into
bounded native arrays to reproduce their live/active/control effects. Those
projections do not claim native pointer alias or NaN-payload equivalence.
Guest condition-boolean checks do not cover full FCSR exceptions. Raw private
register/fault order, the full parent dispatcher, the common helper, hardware
and host gameplay are not acceptance claims. Routine Claude calls: zero.

Reproduce with the prepared consumer and retained ignored baseline:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_particle_rise_1517685c_match -v
make tools-check
```

The isolated sibling overlay uses **six byte-identical task files** with
sibling dependencies and mounted fallback, without writing into `64CBFD Tools`.
Sibling HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with **2,439
dirty paths** and before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

## Linked image and progress

The **803 immutable inputs** in the **807-input** frozen baseline remain
unchanged, including 82 headers. Only source, guard CSV, owner object and ELF
are declared changes. Only `generated_1A20A0.c.o` changes among **698 objects**,
in `.text`, `.rel.text`, `.symtab` and `.strtab`. Conversion rows and all prior
guard bytes stay fixed. Exactly 123 guard rows append.

Production equals the independent prediction. All **6,051 function addresses**
stay fixed; only this body and its **12-to-808-byte** symbol extent change.
The ELF has **568 changed bytes**, **zero exclusions** and **no metadata
permutation**. All **189,088 protected bytes / 720 owners** stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`73b2aa1dbe44da28872317ece93d57e1b1a1f3a4f321f8d1af67513e8b31fbf6`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | **4,493 / 5,515 (81.47%)** | 0 | 1,022 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | **3,820 / 4,842 (78.89%)** | 0 | 1,022 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted functions remain **5,515 / 6,048 (91.19%)**, converted bytes
**86.17%**. One new match is credited; **195 more matches** reach 85% at this
denominator. The wider goal remains active.

Scoped Graphify AST refresh covers six tools files and the owner, retaining
all **60,944 old IDs**, zero lost nodes: **60,980 nodes / 114,651 links**.
This is a scoped merge, not full-corpus re-extraction. Tools commit
`76987f788cb3c07b715613a9ca599d21ac7b7698` precedes the consumer commit. Root README receives
aggregate rows only; no push. `64CBFDOGL` has no source checkout here, and its
Release remains frozen.

Next focused target: **961-word `func_15175958`**, VA
**0x15175958..0x1517685C**, ROM **0x1A2E08..0x1A3D0C**, frame **0xC8**.
It is the owner's final stub. Freeze the new production baseline, recover its
complete shared particle-update contract and actual callers, then qualify
before installation or credit.
