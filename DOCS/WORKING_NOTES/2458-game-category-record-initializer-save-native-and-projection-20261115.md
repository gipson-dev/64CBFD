# Game category record initializer: original save layout, native and ABI

Date: 2026-11-15. Continue **`func_150169A0`** from
[Note 2457](2457-game-category-record-initializer-private-recovery-20261115.md).
The private source now emits retail's **single S0 save**, **0x58 frame** and
original named stack homes. Fresh guest/native checks pass, and the original
caller's result-use proof closes the recovered void interface. Raw C remains
**481 / 477 words**, with **405 real word differences** including the four-word
overrun. It is **uninstalled and uncredited**.

A separate **private diagnostic projection** agrees with all **477 retail
words / 79 switch-table entries**, but its scheduling/register transformation
still lacks an independent equivalence proof. It emits no production guards
and has no installer. This is not a new accepted C match.

Production remains **4,496 / 5,515 (81.52%)** total, **3,823 / 4,842 (78.95%)**
Game, zero drift and **1,019** different. Init stays **492 / 492**, Debugger
**181 / 181**; **192** more matches reach the active 85% goal. README aggregate
figures remain unchanged. The accepted production baseline is
[Note 2456](2456-game-resource-cache-guarded-match-20261115.md).

## Original single-register lifetime and stack homes

The two loops require distinct source indices. Reusing one index across the
player and identity loops encouraged a saved S1 lifetime; separating them
removes that extra save. A shared unsigned byte-size temporary is reused for
the two allocation stages. Index expressions let the compiler recover the
0x30-byte induction cursors without unnecessary named offset locals. Local
declaration order then recovers the original homes:

| Value | Retail and current private source |
| --- | --- |
| S0 / RA | SP+0x20 / SP+0x24 |
| Incoming category | SP+0x58 |
| Bank start | SP+0x4C |
| Captured allocation count | SP+0x40 |
| Player index / induction cursor | SP+0x3C / SP+0x30 |
| Identity index / induction cursor | SP+0x54 / SP+0x2C |

The append destination uses the complete 0x30-byte record type. This recovers
the original register-divide/multiply/constant-divisor guard shape; its final
register allocation still differs. The resource cases use the original block
order. No dummy local, volatile declaration, frame guard, shared header or
production compiler-profile change is introduced.

Complete-owner O2/g3/mips2/o32 compilation has no diagnostics. Both other raw
functions retain instructions and bindings. The target has **68 binding sites**,
a **336-byte private pool**, and raw text SHA-256:
`0028b0d4e468e23a1d1bd253c8286eca1bb2572ae5a2b659c83f467fdd8eb4ec`.
The prior 476-word draft, reports, object and tools files are preserved under
`conker/build/game-record-initializer-150169a0-private/qualified-476/`.
Source-form experiments remain in `save-lifetime/`; they are diagnostics,
not a broad installed conversion batch.

## Guest execution and the raw-code address boundary

- [x] **686 guest cases / two streams** compare all public memory and helper
  entry snapshots. The original 473 reachable words execute; four bypassed
  retail words retain the structural checks from Note 2457. Three effective
  instruction controls remain rejected. Saved S0..S7, saved FPRs and SP agree.
- [x] The 481-word candidate overruns its original slot and would overlap
  `func_15017114` if executed at the retail parent address. Raw execution is
  therefore independently based at **0x14000000**, including its generated
  table targets; named external providers retain their original addresses.
  No simulator call is allowed to fall into the overlapping raw epilogue.
- [x] The original caller's category-load delay instruction remains literal.
  Its raw-stream JAL uses the corresponding named callee relocation to
  0x14000000. **48 caller cases per stream** compare packets, snapshots, public
  memory and saved state. The retail stream keeps the original JAL unchanged.
  This qualifies the private interface, not production placement of 481 words.

No raw fault-state, full caller, opaque-provider internals, emulator/gameplay
or host-port acceptance is inferred.

## Native32 qualification and reusable receipts

- [x] **639 cases each at O0/O2/O3**, with seven effective C controls per
  profile. Undefined-behavior traps and float-cast-overflow traps are asserted
  in the actual compiler command. Providers use noinline definitions and
  memory barriers so their public effects remain observable.
- [x] Every native helper-entry packet and the final state are compared with
  the independent retail-derived model. SHA-256 covers **29,090 public bytes**:
  **6,144 record bytes**, **21,112 actor bytes**, **1,008 ROM bytes**, **800
  auxiliary-buffer bytes** and **26 global bytes**. Two known SHA-256 vectors
  are checked in each executable.
- [x] Native scalar fields are serialized to the guest byte order; pointer
  fields and helper packets are converted through explicit address maps.
  ROM bounds use GNU linker aliases into one backing object. The address-map
  ranges are half-open, so adjacent arrays cannot be mistaken for each
  other's one-past endpoint. The initial inclusive-range fixture was rejected
  before these results.
- [x] The controls cover category-bank choice, original-count capture,
  allocation-length capture across a provider mutation, fresh actor positions,
  live identity-output table selection, scale values and the active marker.
- [x] The native actor/storage contract is **26 actors / 64 records per
  backing table**. The 33-slot guest fixture and full raw fault/alias behavior
  remain separate. These are GNU native32 results, not general C portability.
- [x] Receipts pin candidate, oracle, native fixture, reader/writer and compiler
  fingerprints, all three exact command profiles, generated C and executable
  hashes. The enclosing suite also checks all frozen production inputs,
  including 82 headers. Altered-executable and altered-profile controls reject
  stale evidence without modifying files.

## Original result-use proof

An aligned input census still finds one direct call at ROM **0x35380**, VA
**0x15007ED0**, and no literal function pointer. Starting at the original
continuation **0x15007ED8**, a checked **68-instruction** symbolic traversal
keeps the incoming V0 tainted and the category unknown. It follows:

`func_15005290 -> func_1502B5C8 -> func_1502AC88`

The original code supplies depth 3 and a valid stack output pointer; the loader
stores the initial size value 1 before its first lookup. Every branch before
the cut is resolved from those actual instructions, under the declared aligned,
nonwrapping valid-stack contract. **LUI V0 at 0x1502ACAC** overwrites the parent
result before any read. Two controls reject a forwarded old V0 and a removed
dominating overwrite. No full provider or full caller reconstruction is claimed.

## Private scheduling projection: proof still open

`tools/experiments/game_record_initializer_150169a0_schedule.py` is deliberately
named and documented as an uncredited diagnostic. Its pure projection checks
the exact 481-word source fingerprint and all 68 bindings, consumes the source
instructions through an explicit schedule, changes only checked register
fields/edges/data bindings, and reproduces the original words. The checker also
derives all **79 table targets** through the same inverse map and verifies the
entire original **336-byte pool**, including constants and padding. **549**
source-word/binding corruption controls reject changed inputs.

The proposed transformation has four substantive parts that need independent
validation:

1. Commute the fixed state reset with the independent player-count load and
   restore the original opening branch-delay initialization schedule.
2. Move twelve pure actor-address instructions from before the selector call
   to the coordinate tail; remove the extra private SP+0x28 spill/reload.
   Recover the original duplicated shift across the scene branch and the
   common coordinate load from the two raw load sites.
3. Hoist the constant 3 into the original saved-return-register temporary
   lifetime, removing the second duplicate materialization and checking every
   register role through the cases and both loop joins.
4. Restore the heading-byte store to the unconditional branch delay slot and
   bind the compiler's two tables/two constants to the original data owner.

The schedule omits raw **+0x218, +0x248, +0x57C, +0x628, +0x6B0** and uses
the raw **+0x1E8** shift twice. Register colors are a hypothesis; agreement
with the retail bytes and finite native tests do not prove that hypothesis.
Ordered public effects, valid storage/alias assumptions, helper boundaries,
branch-likely delay behavior and loop induction still need an independent
relational proof. No CSV row or production source is installed from this result.

## Validation, preservation and resume point

The mounted recovery/native/result-use suite passes in **234.244 s**, with
fresh native executions. The separately added private-projection unit passes
in **5.738 s**. Fresh `make tools-check` passes. The seven-file sibling overlay
passes fresh candidate compilation, **64 guest cases / two streams**, **48
caller cases / two streams**, the result-use proof and projection controls in
**45.685 s**. Its native receipts are explicitly reused with exact input,
profile and artifact fingerprints; no fresh sibling native execution is claimed.

All **812 frozen production inputs** remain fixed. The production source still
contains its previous placeholder; headers, 698 objects, original data,
conversion rows, Makefile, guards and ELF remain unchanged. ELF SHA-256:
`668933c3c17e33b1f6d52729397cdfaf7a88690fac78d81bae9cde41c9b80d9c`.
Sibling HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all
**2,439 dirty paths** and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

Graph refresh: scoped AST merge of seven files, **61,193 old IDs retained**, zero loss; **61,208 nodes / 114,956 links**, not a full-corpus re-extraction. Routine Claude calls: zero. Tools
commit `53e78584bf0ee34daae28ea019e8fad1264fe1cb` precedes the consumer documentation/pin commit.
No push; host Release remains frozen.

Next: prove the scheduling projection independently, including register roles
and each permitted memory-order change. Then qualify both actual padders,
independent GNU rebases and original data ownership, actual Make and strict
whole-image prediction, production adoption and actual-ELF recount. Keep the
current snapshot and earlier receipts immutable; no match credit until those
remaining gates pass. The 85% goal remains active.
