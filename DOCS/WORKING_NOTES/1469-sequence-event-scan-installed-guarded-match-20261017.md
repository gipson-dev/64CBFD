# Sequence Event Scan Installed Guarded Match

Date: 2026-10-17. Continues the actual final provider from
[Note 1468](1468-sequence-record-setup-installed-guarded-match-20261017.md).

## Installed Contract

`func_1501DAAC` in `conker/src/game/generated_49D30.c` now has its complete
semantic C body and correct `void(s32 slot)` interface instead of a zero-return
placeholder. All **219 words / 876 bytes** are retail-exact after guarded
normalization. VA **0x1501DAAC..0x1501DE18**, ROM **0x4AF5C..0x4B2C8**,
frame **0x80**. This is **guarded matching, not direct compiler matching**.

The routine clears four shared flags and a halfword, scans the selected slot's
live record count, and queries each non-NULL record six times. Commands are
cached at record + 0x18 across the queries. Keys **30, 14, 104, 68** publish
the flags; key **119** publishes a result halfword. Key **1**, with its extra
filter set, may submit a three-byte color selection according to the signed
query value, the -1 sentinel, and event mode. The final indexed output reads
the current shared result as **unsigned 16-bit**, including provider changes.

Do not import the donor body mechanically. Its narrow value/best declarations,
word-sized event-field reads and typed pointer increments do not represent
retail. The recovered source keeps query values/best as **signed 32-bit**,
the table index as **signed byte at +5**, and mode as **signed halfword at +6**.
The query has **11 arguments**; the color submission has six. Each query's
output cell is cleared immediately before the call.

## Matching Proof

The initial complete recovery already had 219 words but frame 0x88 and 97
differences. Inline color operands and recovered local ordering produce all
219 raw words with frame **0x80**, event home **SP+0x74**, count-pointer home
**SP+0x68**, and the original nonvolatile allocation. There are **77 raw linked
word differences**. Keep the existing O2/g3/no-unroll owner profile unchanged.

**77 expected-word, relocation-aware guards** normalize the remaining opening
schedule and closed scratch roles, with **no insertions or omissions**. Preserve
every previous guard byte, including **298 CRLF lines**. No frame size or home
offset is changed and no saved-register role is remapped.

The opening certificate covers two independent register swaps, the disjoint
private count-pointer store/public byte load, and initialization before the
opening branch. Moving the existing nontrapping shift into the empty-path
delay slot is valid because its scratch result is dead there. Valid slots
are **0/1**, with the private stack disjoint from public global objects.
Raw C is **not claimed fault-prefix equivalent** across these reordered accesses.

The relational fixed point reaches **219 words / 197 CFG nodes**, with **645
transfer steps**, eight calls and one return. It checks ordered operands,
addresses, stores, branch decisions, ABI inputs and nonvolatile roles on every
loop edge. Multiply/LO provenance is explicit and invalidated across calls;
an unrelated MFLO is rejected. No commutative operand rewrite is used.

Raw text SHA-256:
**887e373590a5a49348a3264073762e84372b897230e37fd67ca26f240683e8c0**.
Raw/original words, all 38 bindings per body, private pools, and the exact
guard suffix are fingerprint-gated in `game_sequence_event_scan_matching.py`.

## Qualification

All **14 pre-install recovery/matching tests pass in 148.713s**. The final
installed run broadens this to **29 tests, all passing in 327.067s**:

- **2,568 three-way original/raw/guarded cases**, both stack phases, execute
  every word. Compare full memory including private stack, saved roles and
  both homes at every call, all physical query arguments, and independent
  public state/call expectations. Original/guarded additionally compare literal
  GPR/FPR/LO, PC/delay, provider and ordered event state.
- All five positive provider gates fire: live count, cached current commands,
  future record reload, late shared state and color-time state changes.
- **96 native32 cases per O2/O0 profile with UBSan**, separate full C and
  caller/provider units, no fwrapv. Validate typed pointer/halfword lanes, all
  bank fields, event padding, payload, canaries and compile-time ABI offsets.
  Seven effective native controls fail with **21/22**, not sanitizer traps.
- **Eight compiled guest controls** reject narrow best/value, stale count or
  commands, wrong flag/filter, unsigned color index and signed final output.
  Signed table-index boundary tests use an explicitly extended diagnostic bank;
  native uses a valid biased array. This does not establish arbitrary retail
  resource indices as valid. The unsigned-index control is guest-only.
- Opening, live store/load/backedge, unrelated LO and unknown call controls
  execute the proof beyond hashes. Corrupt **438 words**, **78 binding cases**,
  both private pools and all **847 guard fields**; reject every unknown.
- Three independent original and guarded links each compare all 219 words
  across HI16/LO16 carry boundaries.
- **363 positively fired original/guarded access-fault prefixes** compare
  literal machine/provider state. Bounded hook bulk effects are not claimed
  as instruction-level query-engine emulation.
- All **56 raw and padded owner neighbors** remain unchanged, including the
  newly installed setup caller. No new source/compiler diagnostics or pools.

Connect the original **48-word func_1517EE40** with an independent color-state
reference in **96 three-way cases**, reaching every helper word. Also execute
the complete **473-word setup caller**, six actual setup helpers (**304 words**),
the scan and the color helper together in **18 three-way cases**, with an
independent composed reference. Resource loading, allocation and especially
**func_15023BB0's query engine remain bounded contracts**. The original color
assembly is test evidence; its production C definition is still a stub.
These checks do not establish full sequence-engine, rendering or gameplay parity.

## Complete Image

Before production edits, reproduce the predecessor from captured link inputs,
then independently predict the entire first image/owner/guard successor. Only
the target slot, symbol size **12 -> 876**, and two explicitly pinned symbol
serialization groups change. Group membership, order, definitions and strings
are checked; **zero metadata bytes are excluded**.

The normal development build completes **695 compiler / 687 padder commands**
and regenerates progress. Its ELF equals the first prediction byte for byte:
**4e04f42dd4676fda3fb4296e755a43705c4ee9c0bed6de65b9750dfca3b29ec3**.
Of **755 changed ELF bytes**, **702** are target code, **two** extent, and
**51** exact symbol/string serialization. All other canonical definitions stay
unchanged. Retain the existing duplicate-recipe/compiler warning boundary.

Source owner:
**dd6d6bebb1afad7586f71e5a00a7e057d677aa51864e38ea96291e1b1806c4a7**.
Guard manifest:
**5084330509403cb54c534e06be40b8417b97e95addf3dd362f843e4235b58b35**.
Protect **141 inputs / 138 unchanged inputs**, all three before/after fixture
pairs, and **189,088 data bytes / 720 owners / zero differences**. Prior setup,
reset, maximum and microcode-loader installed checks all pass through the exact
successor adapters. Unknown changes remain rejected.

## Progress And Bank

Fresh official matching: Game **2,941/4,828 (60.92%)**, total **3,614/5,501
(65.70%)**, still different **1,887**, zero address drift. Init stays **492/492**,
Debugger **181/181**. Conversion remains **5,501/6,044 functions / 86.04% bytes**;
the previous C stub already counted. Conversion CSV bytes are unchanged. Root
README updates only its two aggregate matching rows. The wider image remains
non-matching; no full-game or host-port claim is made.

Tools **abf9d17** banks eleven files before the consumer pin. Both copies have
identical pairs and **22 ASCII/AST checks**. Eleven standalone WSL padder tests
pass per copy: active **0.030s + 0.021s**, mirror **0.030s + 0.019s**; tools-check
passes. Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**,
all **969 unrelated initial dirty-file hashes** and its independent history.
Two existing task files are updated and nine added: **980 final dirty paths**.
No mirror commit/reset, push, Claude call, dependency/configuration change,
host-port build/launch or frozen Release action.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_sequence_event_scan_installation
make -C conker -j4 build/conker.us.elf progress.csv NON_MATCHING=1
python3 -m unittest tools.tests.test_game_sequence_event_scan \
  tools.tests.test_game_sequence_event_scan_match \
  tools.tests.test_game_sequence_event_scan_installed \
  tools.tests.test_game_sequence_record_setup_installed \
  tools.tests.test_game_sequence_state_reset_installed \
  tools.tests.test_game_record_maximum_installed \
  tools.tests.test_game_microcode_loader_installed -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Recover complete typed semantics, frame/homes and actual caller/provider interfaces.
- [x] Certify the opening schedule and complete scratch/LO roles; qualify all 219 padded words, native/guest behavior, controls, rebases and faults.
- [x] Execute the actual color helper and full setup/helper/scan chain without claiming the query engine is recovered.
- [x] Freeze the first complete prediction before edits, install, rebuild and pass all 29 tests and exact input/image/data gates.
- [x] Measure fresh progress, update aggregate README rows/indexes/roadmap and bank tools first.

Next: **func_1517EE40**, still a zero-return stub in
`conker/src/game/generated_1AC2F0.c`: **48 words / 192 bytes**, frame **0x8**,
VA **0x1517EE40..0x1517EF00**, ROM **0x1AC2F0..0x1AC3B0**. Recover the actual
color helper's C body next; the assembly exercised above is not an installed
C recovery. Keep the query engine, adjacent func_1501DE18, timing's **141
differences**, wider Game/additional-source matching and full gameplay open.

Subsequent completion: [Note 1470](1470-color-state-submit-direct-match-20261017.md)
restores func_1517EE40 as a complete 48-word direct C match, including precise
signed-byte caller interfaces and exact whole-image/data qualification.
