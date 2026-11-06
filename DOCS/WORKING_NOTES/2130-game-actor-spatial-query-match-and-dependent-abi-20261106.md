# Actor spatial query match and dependent ABI

Date: 2026-11-06. Continue the active 80% goal from consumer
`b3912a20acaca285615c3d6d10826ea9121a71fb` and mounted tools
`68db7dbf183f497db3e0d1d29756c53c85d258f2`, following
[Note 2129](2129-game-group-record-actor-dispatcher-match-20261106.md).

## Recovered query

`func_15081574` in `conker/src/game/generated_AE1D0.c` matches its complete
**71-word slot**, VA `0x15081574..0x15081690`, ROM `0xAEA24..0xAEB40`.
The executable body is **68 words / 272 bytes**, ending at `0x15081684`,
followed by three original zero alignment words. Frame `0x50` retains seven
saved GPRs, RA, F20/F21 and F22/F23. Keep body and slot counts distinct.

The C clears the actor-address output, scans exactly **25 actors** from
D_800CC2D0 up to D_800D121C exclusively at stride0x32C, and checks the live
header word, model pointer+0x1D4 and unsigned type byte+4. The type argument
remains full signed32; a byte with the same low bits is insufficient when
the full argument differs. This scan is not the separate26-actor lookup.

The original part lookup func_1508108C returns an index or -1. Only exact -1
is rejected. Metadata byte D_8009BD30[index*4+2], origin, current actor, two
unchanged float arguments and full query mode are passed to func_15080D20.
The first nonzero result is returned without boolean narrowing, and its
actor address is stored through the reloaded output-argument home. A failed
query advances to the next actor. Exhaustion returns zero.
Providers can mutate the current actor, metadata and argument homes; gates
already tested before lookup are not retested afterward.

The definition agrees with the existing shared functions.h declaration:
`s32(struct127 *, f32, f32, s32 *, s32, s32)`. In particular, the output is
an s32 actor-address word, not a new pointer-to-pointer contract. The source
includes structs.h and casts only the stored address and private byte view.
Correcting the initial opaque pointer hypothesis preserves every emitted
instruction and relocation. Shared headers and the parent object are fixed.

The unchanged O2/g3/MIPS2/O32 profile emits all 68 body words. A do-while scan
recovers the original unconditional first iteration; the ordinary for form
adds a guard and emits 70 words. **11 expected-word relocation-aware guards**
close an S4/S5/S6 role cycle and independent address/argument-load ordering.
All 68 words have one compiler origin; there are no omissions, insertions,
frame changes, branch retargets or substituted calls. All eight bindings are
tracked through the scheduling permutation and independent GNU links.

## Explicit dependent-helper audit

The old zero-return func_15080D20 definition had an unspecified argument list.
Its call now needs six typed arguments to preserve the float ABI. Typing this
still-unrecovered definition makes IDO emit four O32 argument-home stores,
then its original three-word zero return. Its symbol grows **12 to 28 bytes**:

```text
sw a0,0(sp); sw a1,4(sp); sw a2,8(sp); sw a3,12(sp)
move v0,zero; jr ra; nop
```

This helper remains unmatched and receives **zero new matching credit**.
The complete original 219-word geometry routine was inspected for its ABI;
its geometry is not recovered here. The helper delta is explicitly modeled
in the full-image predictor and tested, with no function or section exclusion.
A late prototype following the old empty definition is rejected by CFE for
its parameter-count mismatch and is not adopted.

The owner has four functions. Both assembly neighbors, the 48-word lookup
and 266-word func_1508114C, keep every raw and padded body word and binding.
The copied padded predecessor equals the actual production object. Raw
allocatable metadata changes only the FPR mask at .reginfo+8, from00350551
to00F50551, adding F22/F23 for the new query body. Every other raw pool byte
and binding stays fixed. All padded allocatable non-text sections, including
register metadata, remain identical. These are explicit owner inventories,
not a blanket exclusion of the changed helper.

## Qualification

All eight focused checks pass before and after installation in both tools
configurations using the actual imported helpers. The sibling overlay stays
in ignored consumer build storage; its six tracked edits and 2,428 untracked
files are preserved. Both tools smokes are fresh. Three shared suites per
copy are exact-fingerprint reuses from Note 2124, recorded separately from
fresh execution. No shared parser/oracle implementation changes, compiler
profile change or Claude call is used for this routine.

- **1,157 cases per body**, original/raw/normalized, compare complete RAM,
  call arguments, return values and external access order. All 68 executable
  words are reached. Cases cover all 256 type bytes, full-word type/return
  values, first/last/no actor, header/model gates, signed rejection, two stack
  phases, exact float bits, and guest-only argument-home mutations/aliases.
  Original/normalized complete machine states agree. No full raw fault
  parity or portable native claim about overwriting caller homes is made.
- **381 own-access fault prefixes** compare literal original/normalized
  complete states. Disabled actors also succeed with model-pointer and
  metadata storage unmapped. These are emitted-instruction checks, not
  hardware exception or FCSR acceptance.
- **256 cases per body** connect the complete original 48-word part lookup;
  **44 of 48 helper words** execute. Independent results and memory agree.
  **72 cases per literal body** execute both nine-word caller windows from
  the same parent, func_1505528C. The retail window starts150553B4, calls at
  150553D0 and uses SP+0x64; the current C window starts150553D0, calls at
  150553EC and uses SP+0x7C. S0 origin is an explicit precondition. Both pass
  40.0f,10.0f,mode15,type0x53 with correct O32 homes. Full parent execution
  and the geometry provider remain outside this bounded qualification.
- **Nine independent GNU links**, three data/helper layouts and 36 cases
  per body verify all eight relocations, signed-low16 carry boundaries and
  the 25-actor end address. The standalone function symbol is272 bytes;
  production's three alignment words are checked separately.
- **9,216 native32 SDK/UBSan calls** at O0/O2/O3 use complete typed actor,
  origin and integer-output backing, callback-compatible declarations,
  output canaries and complete actor/metadata/call-log comparisons. Nine
  wrong variants fail with checked42: signed kind, narrowed type, absent
  model gate, wrong part rejection, wrong metadata byte, swapped floats,
  wrong mode, skipped first actor and narrowed return value.
- **5,120 dependent-stub cases** check all 256 tag bytes, float bit patterns,
  both stack phases, the four precise home stores, preserved SP and zero
  return. This qualifies the changed stub ABI, not retail geometry behavior.
- All 272 raw-byte corruptions, eight binding corruptions, eleven stale
  manifest expectations and five whole-image corruptions are rejected.

Fixture fixes corrected dictionary rebasing, added the null-model delay-slot
coverage case, and replaced a float-returning input constructor with local
union bit initialization. The constructor's x86 return path had quieted a
signaling NaN before it reached the target. A focused GDB witness identified
the differing log byte; corrected O0/O2/O3 runs preserve the requested bits.
Recovered C, guards and predicted production bytes do not change for these
fixture corrections. Final receipts fingerprint all five modules/helpers.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Actual Make preprocesses/compiles only generated_AE1D0 once, applies the
existing assembly processor and padder, and introduces no C diagnostics.
Keep both old-dependency flags until a deliberate broader rebuild; unrelated
object timestamps are untouched. The actual ELF equals the independent
**237-byte** prediction with **zero exclusions or metadata permutations**.
Only the target/helper bodies and their two symbol sizes change. All 6,052
addresses, progress.csv, conversion rows, Make rules and 189,088 protected
data bytes in 720 owners are fixed. The unfinished whole image retains its
expected checksum failure and duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,199 / 5,512 (76.18%) | 0 | 1,313 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,526 / 4,839 (72.87%) | 0 | 1,313 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**211 more** matches reach the current 4,410 threshold for 80%.

- ELF: `f2089f914ce3e8ec73000e208ffd9dfb92f7c0eee263de6aaa5c2fb2373f5a16`.
- Owner: `fab463a931fa494e45d40d7b7d1856a64cece76e99335e76a1c40582d503485b`.
- Code binary: `5895e582263aea6b4bc09541985e9128de7d31be148aec88c839ad54dd9a92a8`.
- Guard CSV: `6f37b42a215f48aa06bf0ea48e3fd0e704d8ea215e3a61daacf05577d290c95a`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence and all 108 frozen inputs are retained in
`conker/build/game-actor-type-query-15081574-match/`. Graphify receives a
scoped refresh with old-node retention evidence; no full-corpus extraction
is claimed. Tools are committed before the consumer source/guards/docs/pin.

Next static target: **func_150D0534**, generated_FC5F0. Its 71-word slot has
a 70-word body and one alignment word, frame0x30. Inspect its signed timer,
byte alpha arithmetic, current/previous text selection and four graphics
calls before qualification. It is uninstalled and has no new matching
credit. Preserve private inputs/saves, unrelated work, handwritten
func_150A76F0 and frozen host Release. The full 80% goal remains active.
