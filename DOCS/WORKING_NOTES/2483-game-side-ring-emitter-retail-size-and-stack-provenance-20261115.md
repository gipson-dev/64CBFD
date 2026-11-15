# 2483 - Retail-sized emitter and exposed stack provenance

The private `func_1519F7F0` candidate now emits **415 words / frame 0x118**,
matching the retail extent and frame. Both exposed buffers occupy the retail
incoming-SP addresses, and all eight transition bytes now agree in the guest
screen. **240 real instruction-word differences remain. No normalization,
installation, or new C matching credit is claimed.** Continue this function.

Fresh production recount remains total **4,511 / 5,514 (81.81%)**, Game
**3,838 / 4,841 (79.28%)**, Init **492/492**, Debugger **181/181**, zero
address drift and **1,003** different. **176** more matches are needed for 85%.

Consumer baseline `3a668afaa50562c3bb25ec0c8caf278459ea470a`, tools baseline
`27df32c3b5ceead58f10455497f745ee76750e9b`; new tools commit `5de6c957db19c12c6dcae52e8cf184ec8ed7f8ec`.
The original **880-input production freeze** remains unchanged. See
[Note 2482](2482-game-side-ring-emitter-private-recovery-and-cleanup-domain-20261115.md)
for the complete interface, emitter algorithm and cleanup/state-domain audit.

## Recovered storage and lifetimes

Use the existing `struct127` actor type and its named state, identity and
position fields. Preserve the actor captured before either query. Keep the
first previous-entry cursor and the tail-minus-two smoothing cursor separate.
Keep the unscaled weight difference and its later scaled step as two real
semantic values. Explicitly reload the owner into the existing state local
after cleanup; it can be null. No local is added solely as padding, no inline
assembly or profile override is introduced, and no shared header changes.

IDO's existing ECOFF debug reader now pins the actual local homes, independently
of the executed provider arguments:

| Local | Incoming-SP offset |
| --- | --- |
| Inverse length | -0x24 |
| Eight-byte transition | -0x2C |
| Twelve-byte interpolated position | -0x50 |
| Two-word transverse velocity | -0x70 |
| Twelve-byte floor-query point | -0x8C |

The new raw SHA-256 is
`b3fefd28d39d0309b9d5b69ddf3e31c6eb1838097d31db6957600ef0bb74178e`.
The old 416-word / 0x110 candidate is retained in the committed manifest and
compiled independently as `previous.o`; its pinned SHA/bindings, all 38
neighbors and normalized owner data pools are still checked. Its earlier
receipts are retained in `screen-2482/` under the ignored working directory.

The three-stream guest screen covers **568 cases per stream**, with all
public memory, complete provider argument tuples and copied transition bytes
compared between retail and the refined candidate. It observes **zero** new
transition-packet disagreements; the prior candidate still exposes **27**,
so the original byte-provenance defect remains an effective control. Six
corrupted retail instruction controls are rejected. Root visitation is
**407/415** words for retail/new C and **408/416** for the previous candidate.
This finite screen is not a whole-CFG proof.

## Fresh caller and native checks

Each stream passes **2,048 connected real-query cases** and **32 original
dispatcher cases**. All original query/heading/sample/dispatcher windows are
checked against the live ELF before use. The actual cleanup remains connected
in a separate forced-miss audit: **12 observations** across three streams,
two modes and both allocation outcomes stop at unmapped stores 0x5C/0x64.
No hardware fault equivalence or portable C null-pointer behavior is claimed.

The new native32 harness executes the **exact refined C body** over **392
defined-domain cases per profile** at O0/O2/O3, with and without strict
aliasing, using SSE2 binary32 operations and UBSan traps. It constructs real
typed effect, payload, entries, state and SDK actor objects; verifies ABI
sizes/offsets, provider arguments, full endian-normalized snapshots of these
objects and relevant globals. Twelve effective source controls cover the
smoothing cursor, duration field, query span and signed/unsigned RNG remainder.

Native cases exclude opaque query misses, nonfinite FP operands, arbitrary
object aliases and the invalid retained-progress/no-motion state. A separate
negative test rejects that last state in the independent model rather than
assigning an invented inverse length.

At O2/O3 GCC diagnoses that `inverseLength` may be uninitialized. Retail leaves
that local untouched on the excluded path. The harness preserves the exact
source, makes **only this specific warning nonfatal**, rejects other warnings,
and retains its diagnostic files. UBSan does not validate uninitialized float
reads. The six native profiles establish evidence over the stated input
contract; the complete caller-state invariant and hardware FCSR behavior
remain unproved. This is an explicit qualification limit, not a warning-free
native or whole-program acceptance claim.

Both the primary tools checkout and an isolated overlay of the sibling tools
checkout pass the focused suite with exact before/after task fingerprints.
The sibling HEAD/status and all **2,434 existing dirty paths** remain unchanged.
No host-port source/build applies here; frozen Release artifacts and saves
are untouched.

## Remaining matching work

The **240 raw word differences** include closed register-allocation changes,
private spill schedules, transition-base addressing and floating instruction
ordering. The screen records concrete FP-order counterexamples: retail computes
another delta before the first ABS/compare, while raw C schedules that ABS and
compare earlier. Value agreement does not prove ordered FP exception/trap
behavior. Do not claim exactness from the matching length/frame or replace all
differences with unproved expected-word guards.

Next recover closer source scheduling or establish checked local transformations
and a whole-CFG relation, with the stated state/alias/FCSR contract. Preserve
the now-correct exposed stack homes and all three untouched transition bytes.
Then qualify both padders, independent symbol rebases, actual Make, strict
whole-image and production gates before installation and a matching recount.

Reproduce with the prepared original production freeze:

```sh
python3 -m unittest tools.tests.test_game_side_ring_emitter_1519f7f0_recovery -v
```

Current receipts are in
`conker/build/game-side-ring-emitter-1519f7f0-private/refinement-2483/`;
canonical compiler/guest/native artifacts are in its parent working directory.
Production ELF SHA-256 remains
`29d206f55163699565107bebaf610b9c9a383ddef1ca7292fd6370400e6fcd60`.
Production source, guards, objects, code image, conversion rows and root README
remain unchanged. Detailed updates stay in working notes and DOCS indexes.
