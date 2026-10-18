# Route Record Setup Semantic Recovery And Private Order Boundary

Date: 2026-10-18. **Recovery checkpoint, not an installed byte match.**

## Scope And Baseline

Recover `func_150870D0`, owner `generated_B3020`, VA
`150870D0..15087350`, ROM `B4580..B4800`, 160 words / 640 bytes,
retail frame `0x60`. Consumer baseline is `2d4acf9`; tools predecessor is
`a48f19d`. Tools **483ddb2** is committed before this consumer checkpoint.

Production remains the original three-word zero-return placeholder. The
complete C body is in the experiment only; no new guards, Make changes,
production build or matching credit. The installed vector, spline payload,
projection and dispatcher baseline from Note 1565 stays fixed.

The 23 frozen live inputs and their immutable snapshots remain unchanged,
including the complete owner, retail assembly, caller assembly, compiler
profile, manifests, ROM and ELF. The production SHA-256 values remain:

| Input | SHA-256 |
| --- | --- |
| Whole ELF | `e55a6d218b40d9216dbe690c058132eacbae0e57d009c0f2670501ff46aa65b3` |
| B3020 source | `53bab1289ba22cce5a94208fa441fb9b349cb825185748af3096e293937b685b` |
| Guard manifest | `0d6c65a40cc623678449ea344d3fcb1b4a119f33f619e6964164c4c25b46558e` |

## Recovered Contract

The proper interface is **three full-width arguments**,
`void func_150870D0(s32 key, s32 playerCount, s32 extraCount)`.
The first argument goes unchanged to the real lookup. The alternate source's
two-argument body, hard-coded lookup key zero, signed-byte loop counters and
word casts over byte fields are not transplanted.

The retail routine clears the output pointer before lookup, truncates only
the resulting route index to a byte, then scans all five neighbor entries.
Its signed mode selects a minimum/maximum unsigned class, retaining the last
tie. Both initial neighbor calls execute even if the first result is FF.
Failure gates preserve the existing count/mask/ready globals.

The closed-route walk retains byte indices but a full-width length. It stops
after the call whose old previous index is the start; no timeout or synthetic
route cap is added. The recovered source uses the original six accessed byte
homes inside a 0x20-byte scratch workspace. The reserved struct view recovers
their ABI locations; it is **not a claim about the original C type**.

Only the count stores truncate to bytes. The total uses modular 32-bit
addition; allocation requests total * 0x84 modulo 32 bits with `(1,0,0)`.
Allocation still executes for nonpositive totals, and its returned pointer is
published before the signed positive-count gate. Retail has no positive-count
null check, so none is invented.

Each positive-count iteration reloads the published table pointer, calls the
real 33-word constructor, preserves the original record-field store order,
reloads the signed player and human limits, and reads the human limit before
storing the route-length byte. The ready flag is set after the loop, including
the zero/negative-total path. Allocation providers may mutate globals.

## Source And ABI Fit

The bounded source screen contains **34 measured forms**, with no new compiler
diagnostics and all **72 owner neighbors / normalized pools unchanged**.
The selected full body emits **160 words / frame 0x60 / 43 raw differences**,
with 26 exact relative relocation bindings. Raw text SHA-256:
`af81faf7636c002ae13313f4948e2ebb51de922efc04d205b12d84346f3b67a6`.

Input-count home reuse and pointer iteration recover the frame. Reusing the
full-width loop index for the explicitly byte-masked neighbor result restores
the walk's `S0=start / S1=next` roles. This matters because the real selector
spills S0 below the parent's frame. The earlier 54-difference form fails final
private memory there; it is not the accepted ordinary-state model. A full-width
candidate local then reduces 50 to 43 differences without losing those roles.

Lower-count public-order regressions and the 161-word delayed-seed forms are
retained as rejected screens. No complete normalizer, padding qualification,
independent rebases or installation prediction has been claimed for this target.

## Fresh Qualification

**All six focused tests pass in 38.164 seconds, no skips.** This includes a test
which positively requires and records the remaining matching rejection.

- **530 paired guest cases**, comparing an independent public reference,
  ordered calls/accesses, complete ordinary memory and saved ABI. Cover early
  gates, both stack phases, full-width key/count edges, high lookup indices,
  128/254/255-node routes, signed-byte globals and allocator effects.
- **729 additional paired guest cases** cover all 243 five-slot patterns in
  three signed modes, unsigned high-bit classes, disabled types and last ties.
  Complete ordinary memory and public access/call order agree.
- The lookup, selector and constructor execute their **real 19/88/33 linked
  words**, independently checked against retail: 140 real helper words. Only
  the allocator is an opaque, caller-clobbering provider.
- **1,286 native32 cases per O0/O2 build**, both with UBSan. Execute the complete
  C target and all three actual C helper bodies, checking entire output banks,
  untouched route data, globals and ordered helper arguments/snapshots. Sweep
  every mode, player-count and human-limit byte. Five effective controls
  (key zero, truncated total, unsigned human limit, wrong slot limit and
  0x80 stride) exit ordinary wrong-result 23; no crash is counted as success.
- **186 raw-word/binding corruption controls** and **46 live/snapshot input
  corruptions** fail closed. All 23 genuine inputs remain intact.
- Whole-Game retail scanning finds one direct site: `func_1509DFC4` at
  `1509E1B8`. **41 real retail-only caller windows** execute its three argument
  loads, including A2 in the call delay slot, the complete candidate/retail
  target and the caller's zero-result branch. Saved ABI, complete ordinary
  memory and ordered calls/accesses agree. Full dispatcher execution and
  unknown indirect interfaces remain unqualified.

Guest allocator modes 3/5 deliberately map aliases to count globals / the
published table pointer, including a constructor-induced pointer reload.
These are guest instruction probes, not portable native aliases. Native tests
exclude them, positive null allocations and malformed/nonterminating graphs.
The independent reference detects repeated route states; it does not impose
a new production iteration limit. No universal C, hardware-trap or gameplay
proof is claimed.

## Matching Rejection And Next Step

**465 fired paired synthetic memory cuts: 140 equal, 325 rejected.** Full
private access order is not restored. Compare only paired cuts that actually
fire in both bodies; one early-failure fixture has 36 versus 37 accesses,
which is explicitly retained in the receipt, not treated as a fired raw fault.

The first mismatch is **cut 43** in the normal three-node fixture. Candidate
PC is `150871D4`; retail is entering its second selector at `150888AC`.
The candidate has already written value 2 at entry-SP minus 23, the parent's
`SP+0x49` seed byte. Retail still holds that first result in **S7** and writes
the two seed bytes only after the second call. Final memory agreement does
not erase this live scheduling difference. These cuts do not establish
universal GPR/fault-PC or physical hardware exception equivalence.

**Continue the same function.** Recover the first neighbor result's original
S7 lifetime and delayed seed stores without losing the 160-word/frame-0x60
shape, S0/S1 walk roles, signed-limit order or three-argument interface.
Delayed-store screens currently grow to 161 words and change saved roles.
Then finish a source-derived all-word/binding fit, private-prefix and alias
qualification, actual mixed-profile padding/Make path, independent rebases,
first whole-ELF prediction, installation, linked audit and fresh recount.
Do not install a public-output-only model or bypass the recorded rejection.

## Repository And Reproduction

Tools **483ddb2** first; the standalone mirror's older ddbdd16 HEAD is untouched.
Only the two absent task files are copied there, byte-identically, preserving
all **1,270** preexisting dirty hashes. It now has **1,272** dirty leaf paths;
no mirror commit/reset. Three repository-setup tests and tool smoke checks pass
in each copy, and consumer `make tools-check` passes.

Root README is unchanged. The last installed, freshly measured Note 1565
counts remain **Game 2,990/4,828 (61.93%)**, **total 3,663/5,501 (66.59%)**,
**1,838 different / zero drift**. Those are reused installed figures, not a
new recount or credit for this experiment. No unchanged broad neighbor suite
is described as freshly run. No push, Claude call, debugger/emulator session,
host-port edit or frozen Release build/launch/modification.

From the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_route_record_setup -v
python3 -m tools.experiments.game_route_record_setup --qualify
python3 -m tools.experiments.game_route_record_setup --captures
make tools-check
```

Ignored `conker/build/game-route-record-setup/` retains frozen inputs, complete
owner compilations and commands, all source screens, native sources/binaries,
guest/native/caller/corruption receipts and the explicit private-order rejection.
The wider Game matching goal remains active.
