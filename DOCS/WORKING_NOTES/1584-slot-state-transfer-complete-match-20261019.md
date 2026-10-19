# Slot-State Transfer Complete Match

Verified: 2026-10-19. **Installed complete C recovery: all 189 words / 756 bytes
match retail, with the original 0x50-byte frame.**

Finish `func_1508E89C`, generated_B3020, VA `1508E89C..1508EB90`, ROM
`BBD4C..BC040`, after [Note 1583](1583-slot-state-transfer-recovery-and-matching-boundary-20261019.md).
Consumer predecessor `1df34adb`; tools predecessor `a53e876`. Bank the explicit
layout/integration tools **49a11c6**, then the normalized caller check
**63f4733**, before the consumer source/guards/docs/pin. No push.

## Source And Matching Boundary

Install the complete body already recovered in Note1583, with full-word source
and destination slots, signed-halfword score-helper views, ordered mask writes,
fresh table/state reads, actor transfer, optional script updates, two-argument
final helper and signed-byte counter. Every return remains zero. Preserve the
address name and one concise purpose comment; working field/type names do not
establish original source naming or complete shared structure definitions.

The selected semantic C is unchanged from that recovery. **Raw compiler output
still has100 real word differences**; this is not a direct unguarded C match.
Both full-owner profiles produce the same189-word/frame80 body and26 relocation
positions. Twelve additional meaningful-value screens preserve their tested
public algorithm but regress or fail to improve the fit. Do not add a dummy
padding local, volatile or physical-register binding to force a stack layout.

`game_slot_state_transfer_layout.py` specifies instruction-field transformations
and an origin permutation, not a retail body copied wholesale into the padder:

- Rename the closed temporary register roles using an opcode-aware field map;
  reject unsupported instructions or an unexpected source register.
- Restore ten source-cache/mask/destination-pointer stack references. The
  first-helper homes become SP+0x1C/+0x20/+0x24 and the destination-pointer home
  becomes +0x2C. Already-correct halfword+0x48 and linked-byte+0x3F stay fixed.
- Restore the independent opening OR/store schedule, script address/multiply
  schedule and actor+0x125 store/state-pointer-load schedule. The latter fields
  are disjoint even when their actor base wraps in guest address arithmetic.
- Convert four negative-base equality checks into ADDIU-computed-address plus
  BEQZ checks. Modular addition is zero exactly when the original base equals
  the negative offset. Move the first hoisted materialization after the flag
  block and retarget its zero-flags edge to execute that materialization.
- Move only the script branch's actor-base HI/LO bindings, from source word
  indices143/145 to output141/142. Preserve all26 bindings and all189 source
  words exactly once: **no inserted or omitted words**.

The raw SHA256, exact binding dictionary and normalized SHA256 gate the recipe.
The100 generated manifest rows each check their actual old word and relocation
ownership. Generation preserves the complete historical manifest prefix, and
requires the exact manually installed C owner and retained first-image proof.
No shared padder, Makefile, compiler profile, original assembly or data change.

```text
raw:        6614844cb6c0714ad69f73adab4fa0214a709c66aeefac7aea114d0fcdc127fe
normalized: 70b4fa7e70377c696f09b510e462abaae7a665dd7615a95db41bb585ab9f9c05
```

## Fresh Qualification

All **10 pre-install tests pass in66.757 seconds**. All **11 final installed
tests pass in69.858 seconds**, including the additional normalized caller
window. No skips. Test setup recompiles the semantic body and owns its artifacts;
the integration test generates qualification, shadow Make and first-link inputs.

- **950 fixtures/two stack phases:1,900 paired executions** compare complete
  modeled GP/FP/LO state, private/public RAM, ordered events and helper calls.
  Independently compare public effects against the bounded algorithm reference.
  Literal private homes now match, rather than merely recording Note1583's
  effective raw-source nonmatch. Complete static comparison covers all189 words;
  the fixture corpus visits185, not all189.
- **844 fired access-fault pairs** across gate, transfer, zero flags, lookup,
  same-slot and helper-mutation paths agree in complete modeled state. Every
  requested cut actually fires; this is not a hardware exception guarantee.
- Native32 **O0, O2 and O2+UBSan** each pass950 cases with71 named observations.
  Three executed source negatives exit21; positives exit0. Keep the existing
  stack-realignment/no-strict-aliasing harness policy and256-actor fixture backing.
- **16 paired actual three-word caller windows** pass using the normalized
  complete body. The real full-word argument loads/JAL delay slot are included;
  the stop trampoline is synthetic and the whole dispatcher is not executed.
- Eleven raw-byte/binding/register/schedule corruption controls reject their
  changed input or recipe. Six manifest corruptions fire the actual padder's
  stale-word/stale-relocation checks. Three image mutations fire the strict
  whole-image verifier, including unrelated beginning/end bytes.
- Check1,048,588 modular address predicates, including complete low16 sweeps
  under four high-word prefixes and exact null neighbors. This does not claim
  an exhaustive sweep of all32-bit bases.
- Independently assemble the original routine and derived normalized stream
  under **three GNU maps**, including all global/call bindings and HI/LO carries.
  Their complete code agrees. Execute **24 code-rebased pairs** with original
  global/helper bindings. Differently mapped data/helpers are static link
  checks, not additional rebased-runtime coverage.
- Both owner profiles preserve all72 other routines and normalized pools.
  The actual padder/assembler preserves72 padded neighbors and retained pools.
  All seven expanded shadow Make commands agree with the qualification; the
  existing normal-profile projection override remains unchanged.

Helper providers deliberately mutate table/state/tag/counter values and poison
caller-saved registers/LO. They remain bounded providers, not execution of the
real game helpers. Numerical host memory views, modeled cuts and byte-exact
guest code do not establish arbitrary portable C aliases or whole-game/host
presentation behavior. The prior raw-recovery suite is a predecessor-stage
receipt, not a newly passing installed suite; use the layout suite below now.

## Exact Production Image

The first private ELF equals the target-only prediction on its first attempt.
Actual production Make reproduces that identical3,257,636-byte image. Exactly
**595 bytes change:593 target-code bytes and two target-symbol size bytes**
(12 ->756). No symbol/string permutation or metadata exception is needed.
All other6,056 linked bodies, every function address, all189,088 protected
Game-data bytes across720 owners and every other frozen input remain fixed.

The shared manifest triggers the wider rebuild. It succeeds with the existing
duplicate generated_12D630 recipes and warnings from untouched source; do not
claim a warning-free build. Both target qualification profiles have empty
diagnostics. The existing mixed CSV endings remain intact; Git's CRLF-to-LF
advisory is not a new content change or failed build.

```text
owner:  6fe4d8408e457541217402b980e22d5bec2a543c78159b9257820c3366073008
guards: e0fa6e237c49ab0da592675c5f7ed0ba5151eb440680d7736a152490cae1c49c
ELF:    2de61c0701cc1deb2fe0e0c0334756728c2abbb84525af3d370b531dcb4336d5
```

Fresh matching: **Game2999/4832 (62.07%)**, **total3672/5505 (66.70%)**,
Init492/492, Debugger181/181, **1,833 different / zero drift**. C conversion
counts/bytes stay5505/6044 (91.08%),86.08% bytes overall and4832/5323 (90.78%),
85.44% bytes for Game; exclude repeated CSV header rows. Root README receives
only the verified date and aggregate matching rows, not this narrative.

Both tools copies pass their three repository setup tests and project smoke
checks; consumer `make tools-check` passes. Four new task files are identical
ASCII/Python-valid in the standalone mirror. Preserve its ddbdd16 HEAD and all
1,319 prior leaf hashes, adding only four files for1,323 dirty leaves, without
a mirror commit/reset. Post-commit graph preservation is a separate gate in
ignored `conker/build/game-slot-state-transfer/integration/graph-audit.json`.
No compiler capture, Claude/REA setup, sibling host or frozen Release action.

```sh
python3 -m unittest tools.tests.test_game_slot_state_transfer_layout -v
python3 -m tools.experiments.game_slot_state_transfer_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

This routine is finished. The following func_1508EB90 (26 words), func_1508EBF8
and func_1508EC5C (25 each) already match and are unchanged by the full audit.
Continue with **func_1508ECC0**, VA `1508ECC0..1508EDBC`, ROM `BC170..BC26C`,
**63 words/frame8**, currently63 differences and a zero-return placeholder.
Recover its three unsigned-halfword views, unsigned row/count scans and packed
entry lookup. The key is truncated `(arg0 <<12) + arg1`, not a guessed OR of
masked fields. Exclude the first matching entry when selecting the second;
preserve the early -1 from a matched row with no eligible peer. Qualify S0 and
original argument homes, full-word callers and empty/duplicate/overflow cases.
The broader Game decomp/matching goal stays active.
