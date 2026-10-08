# Game Lighting Dispatcher Match

Date: 2026-10-07

## Scope And Baseline

Continue from the matrix-list match `5a764e3a` and separately banked basis
audits `ce7fc332` / `81c5cfb6`. Restore `func_151462C8` in
[game_16EE20.c](../../conker/src/game_16EE20.c), VA `151462C8..151464B8`,
ROM `173778..173968`: **124 words / 496 bytes**. It was a zero-return C
placeholder, so this recovery increases matching, not the converted count.
The original assembly remains the reference, not the implementation.

## Recovered Contract

The [driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_lighting_dispatch_candidates.py)
retains the complete nine-word ABI: command pointer, descriptor pointer,
unsigned-byte mode, actor pointer, unsigned-byte slot, signed-halfword index,
position pointer, unsigned-byte flags and full extra word.

The local 32-byte descriptor has capacity at `+0`, count at `+4`, four light
pointers at `+8..+14`, ambient pointer at `+18` and channels at `+1C`.
These are descriptive field names; the byte offsets and N64 pointer layout
are independently checked. No shared header or callee implementation changes.

- Load the indexed light pointer first. If null, return the incoming command
  pointer without reading the ambient pointer. A null ambient pointer also
  returns immediately, without actor, position or global-state reads.
- Incoming mode 1 uses actor lighting only when the actor exists, its first
  word is nonzero, its slot byte `+3B` matches, its kind `+4` is not 255 and
  its light-count byte `+302` is nonzero. A null actor falls back to position;
  an invalid nonnull actor falls back to global lighting, not position.
- Actor mode passes the indexed word at `+304`, bytes `+301/+302` and pointer
  `+314` to the five-word `func_1515E544` call.
- Global mode passes the indexed `D_800D9E10` word, `D_800D9E20/D_800D9E21`
  bytes and `D_800D9BD0[index][D_800BE9C0]` address to the same helper.
- Mode 0 and other byte modes use `func_1515D914`: signed index, X/Y/Z
  truncated toward zero, unchanged extra/capacity/channel words, both resource
  pointers, the count-byte output address, null history/node pointers and
  `8 | (flags&1 ? 2 : 0) | (flags&2 ? 16 : 0)`.
- Return the helper result exactly, including null. There is no new mode clamp,
  index bounds check or capacity gate.

## Source Fit And Guards

The positive guarded body, late unsigned mode temporary, unsigned `1U`
comparison, explicit zero/default cases and full flag if/else forms recover
**124 words / frame `0x48`**, unchanged O2/g3/MIPS2, no pool or isolated
diagnostic. Actor/global/position calls, all branches and delay slots,
incoming homes, saved-register lifetime and complete epilogue match directly.

Only `+138/+13C` differ: compiler order is `move t0,zero; lh a1,0x5E(sp)`;
retail order is the reverse. These adjacent instructions have independent
destinations and no control-flow or memory dependency. Two expected-word,
no-relocation guards swap only that schedule. All 124 normalized/linked words
match retail, with no insertion, omission, private-offset movement, relocation
replacement or bulk body patch. The padder rejects a stale expected word.

Retain **244 source/profile controls**, none raw exact. They cover mode type
and initialization, actor gate forms, lazy/eager ambient access, direct versus
common returns, explicit zero/default dispatch, index/flag types and constant
sharing. **5,856 bounded candidate executions** qualify their helper calls and
returns on ordinary valid indices. This does not claim every eager or unsigned
index control preserves lazy faults or out-of-range signed-index semantics.
Six compiled semantic negatives have actual call/return counterexamples;
unexpected faults are not accepted as detections.

## Maintained Qualification

[Eight dispatcher tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_lighting_dispatch_match.py)
and the previous matrix-list installed-slot regression bind:

- **30,722 guest fixtures**, all 256 mode/flag bytes, six actor states, four
  ordinary indices, two stack phases, null/non-null helper results and bounded
  callback mutations. Raw C, guarded C and retail instructions preserve full
  memory, public read/write/call traces and saved GP/FP registers while hooks
  clobber caller-saved GP/FP registers. All **122 executable words** are covered;
  unreachable `+A0/+134` remain explicitly excluded, not silently omitted.
- **872 coordinate/slot fixtures**: twelve finite binary32 patterns across
  all three axes, both zero signs, subnormals and signed-int32 boundaries,
  plus all 256 slot bytes. No FCSR exception, invalid conversion or NaN claim.
- **436 lazy-resource/unused-input fixtures**, seven removed required-storage
  faults and four guest-only signed/out-of-range index-address probes. Native
  qualification uses the descriptor's four valid indices only.
- **32,768 freestanding native 32-bit cases**, actual selected dispatcher C,
  static descriptor size/offset checks, all nine inputs, all five/fourteen
  helper arguments, exact pointer/null return, count-byte mutation and command
  fences, warnings-as-errors. Rendering callbacks remain validating hooks.
- Copied production owner: **89 functions / 88 unchanged neighbors**, same
  two warning statements, identical normalized data pools and target bytes/
  relocations equal to the isolated source. The actual padder retains all
  **13 relocations**; each of seven symbols independently rebases through a
  low-half carry while keeping the complete slot correct.

Both renderer callees remain separate recovery work. In particular the
production `func_1515D914` is still a placeholder; these tests do not claim
connected semantic renderer execution, hardware pixels or PC-port acceptance.

```sh
python3 -m tools.experiments.game_lighting_dispatch_candidates --sharing
python3 -m unittest tools.tests.test_game_lighting_dispatch_match tools.tests.test_game_matrix_list_transform_match.GameMatrixListTransformMatchTests.test_installed_complete_slot_and_guard_history -v
make -C conker -j4 build/conker.us.elf
make tools-check
```

All **nine combined tests pass in 324.913 seconds**, zero skips/errors/failures.
Tools, Python syntax and scoped whitespace checks pass. The documentation
checker verifies **84 documents / 3,976 relative links / zero broken links**.

The initial coverage assertion omitted the early-return fixtures; adding both
gates closes their delay-slot coverage. An early installed-slot check also
read the old ELF while the production rebuild was still running. Both are
harness/ordering corrections, not qualified failed runs. The final run is
started only after the complete linked build and audit.

## Linked Audit

The US ELF build succeeds in **339.375 seconds**, with the same two owner
pointer warnings and existing duplicate-recipe warning. The full audit changes
only `func_151462C8` across **6,058 symbols / 6,042 retail slots**. All other
6,041 retail bodies, addresses, extents, 16 overflow symbols, protected Init/
Debugger/data sections and conversion-file hash remain unchanged. All
**720 Game-data owners / 189,088 bytes** stay exact. The prior 11,061 guards
are byte-for-byte intact; the new count is **11,063**.

Matching is total **3,364 / 5,466 (61.54%)**, Game
**2,691 / 4,793 (56.14%)**, **2,102 different**, zero drift. Init 492/492 and
Debugger 181/181 remain exact. Root README changes are aggregate rows only;
detailed recovery history stays in this document and the update log.

## Continue

1. Recover the next zero-return placeholder `func_1514654C`, VA
   `1514654C..1514672C`, ROM `1739FC..173BDC`: **120 words / frame `0xA0`**.
   It chooses attachment/lookup/descriptor/actor matrix routes, then either
   forwards to the matched list wrapper or converts a fixed matrix and
   transforms each source/destination point pair. Audit the lookup-helper
   failures, private matrix `sp+4C`, output locals `sp+90/+8C`, incoming-home
   reloads and positive/nonpositive count returns before matching.
2. Leave already matched neighbors `func_151464B8` and `func_15146508` alone.
3. The basis constructor's 148-word source/layout fit remains open in
   [Note 1101](1101-game-vector-basis-coordinate-and-workspace-controls-20261007.md).
   Translator scheduling and sampler per-path RA/RNG lifetime also remain open.

No sibling port, frozen Release, real-save, runtime, hardware or push action.
