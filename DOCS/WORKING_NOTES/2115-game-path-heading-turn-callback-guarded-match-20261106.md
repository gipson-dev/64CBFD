# Path heading and turning callback recovered and matched

Date: 2026-11-06. Continue the 80% goal from consumer
`004ad45b392a8b5ee2ff7c686137d997b500702d`, tools
`478e79fcd5086a1612045e5b6ce53ce0fe529aad`, and the private boundary in
[Note 2114](2114-game-path-heading-turn-private-fit-and-abi-boundary-20261105.md).

## Installed result and source

`func_15077F64` now matches all **68 words / 272 bytes**, frame **0x28**,
VA `0x15077F64..0x15078074`, ROM `0xA5414..0xA5524`.
The complete `void(void)` C body replaces the false zero-return placeholder
in `conker/src/game_A28B0.c`. Its local forward declaration is repaired and
the superseded commented draft is removed. Shared headers, helper definitions,
Makefile profiles and conversion rows do not change.

The selected source emits67 words. **42 expected-word rows** normalize the
closed register/scheduling differences and restore **one redundant OR copy**
at original offset0x44. No instructions are omitted. The original frame,
saved-RA home0x14 and row-byte home0x1E emit naturally and are not patched.
All **14 bindings** retain their original symbols and relocation kinds;
their moved sites are explicit in the guards. Every prior guard byte remains
an exact prefix of the extended manifest. This is guarded-C matching, not a
claim of a direct unguarded68-word compiler output.

## Semantic interface and portable sequencing

The actor's byte0x13F selects a path, and byte0x21E selects its eight-byte
entry. The next record supplies signed X/Z halfwords. The callback submits
`nodeX - actorX` and `actorZ - nodeZ` to the existing three-argument
`u16 func_1505A630(f32, f32, s32)`, with argument three zero. It saves the
byte value `D_800D1890 - 1` across that call. Mode zero therefore retains
row255 after narrowing; the provider may change the live mode independently.

The query result is assigned to a separate u16 local before storing through
the live actor pointer. The initial single-expression store allowed GCC to
evaluate the destination before a mutating query provider and update the old
actor. The native grid caught that at heading bytes0x78/0x79. Explicit
sequencing fixes the source-level evaluation order and leaves every IDO raw
instruction/binding identical. No normalization row is needed for this fix.

After the angle store, the actor pointer reloads again. The arithmetic-shifted
angle difference is reduced to a byte and folded to circular distance0..128.
The128 tie is retained. Threshold indexing deliberately uses a byte view of
`D_80099A3C`, with ten-byte rows. If the threshold is strictly smaller than
the distance, the callback copies D_800D1891 to actor byte0x250 and submits
the live actor, byte magnitude and saved row to
`void func_15056A00(void *, u8, u8)`.

Both helper types remain consistent with their definitions. The incidental
A3 value at the first call is not a fourth C argument. The bounded original
heading helper never reads A3. The complete caller-window test also proves
that this callback's return register is discarded; no C return is invented.

## Source fit and preserved owner

The bounded symbolic comparison visits **78 original /77 candidate states**
and **four terminal paths**, comparing exact helper arguments, branch
predicates, complete symbolic store histories and stack/return-control
expressions. All ordinary initial reads lie between the RA save and saved-row
write; the comparison treats only that initial read group as commuting.
Later memory and call events remain ordered. Byte-load zero extension and
byte-mask idempotence are explicit simplifications.

After decoded register operands are masked, the complete opcode/immediate
multisets differ only by one OR copy. Every OR in both programs has a zero
operand. The explorer models helper clobbers and memory effects symbolically
and keeps the exact float operand expressions. It is specific to this fixed
window; raw fault order, dead-register/FCSR equality and hardware acceptance
are not inferred from it. Fitted and padded instructions are literal retail
identity and receive separate execution/fault checks.

All **210 compact neighbors and210 padded neighbors** stay identical.
The compact ownership-aware pool check passes. A complete padded inventory
also checks `.MIPS.abiflags`, `.bss`, `.data`, `.game_overflow` and `.reginfo`,
including the inherited executable pool's R_MIPS_26 bindings. No section is
excluded to work around the older R32-only pool parser.

The target owner retains thirteen inherited diagnostics after path/line
normalization: one Warning665, ten Warning712 and two Warning709. This is
not a warning-free owner. The existing duplicate Make recipe warnings also
remain outside the current change.

## Execution and corruption qualification

All **eight focused checks** pass before and after installation. Run:

```sh
python3 -m unittest tools.tests.test_game_path_heading_turn_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- **1,216 guest cases per body**, four bodies, visit all68 target words.
  Both stack phases, all byte mode/index values, signed coordinate extremes,
  exact threshold ties, the128 circular tie and mutable providers are covered.
  Complete memory includes the saved byte and private stack. Raw linked-return
  PCs are accounted for individually; literal dead-register/fault equality
  is asserted only for the retail/fitted/padded programs.
- **272 helper cases per body** execute both complete original helpers:
  the50-word heading query and66-word turning routine. All reachable words
  execute; the heading query's unreachable word at0x1505A6CC is retained.
  Nontrapping FP-control conversions restore the seeded FCSR in the bounded
  model. The lower atan provider remains opaque; this is not full hardware
  FCSR, atan accuracy or gameplay acceptance.
- **72 alias cases**, including actor fields and globals in saved homes,
  plus **86 fired access prefixes** and a sparse case with absent unused
  notice storage. These private-home and pointer/global aliases are guest
  evidence and are not advertised as portable native C inputs.
- **144 original dispatch cases per body**, the complete29-word window,
  both stack phases, callback157 and no-call sentinels, four return poisons,
  and the original five-byte/one-byte script advance. The aligned ROM census
  has no direct JAL/tail jump and one literal at0x22B464 in D_80086730.
  This qualifies the actual window, not the whole enclosing dispatcher.
- **Twelve independent GNU links** cover three code/data layouts, all14
  bindings and signed-low carry boundaries; **48 cases per body** run rebased.
- Native32 O0/O2/O3 with UBSan pass **1,310,720 calls per profile /
  3,932,160 executions**. Every16-bit current and queried heading value appears
  in the pair grid, with four mode bytes and five thresholds. The reference
  uses unsigned circular arithmetic, widened float subtraction and complete
  actor-byte snapshots. This is not an exhaustive four-billion-pair grid.
- All **13 semantic IDO and14 native controls** fail effectively: coordinate
  sign, entry selection, mode, stride, strict threshold, sign/fold, shift,
  state destination, notice, saved row and cached actor. The extra native-only
  control restores the unsequenced query/store and rejects the GCC regression;
  that source difference deliberately has identical IDO words.
- **268 raw-byte,14 binding,84 guard-field and five symbolic corruptions**
  are rejected. Removing the copy fails byte identity. Five whole-image
  corruptions and the old stub are rejected.

The installed target suite, nineteen mounted shared checks and tools smoke
pass. The independent dirty sibling passes its twelve supported shared
checks and smoke without edits. Prior neighbor suites are reused only through
unchanged complete bodies/bindings/pools. The one advisory and its rejected
extra-word claim remain recorded in Note2114; no new Claude call is made.

## Literal production image

The qualification snapshot freezes **135 inputs**, including every header,
owner/caller assembly, the retained helper source/object/assembly, ROM,
manifests, Makefile, linker, owner, ELF, binary, progress and graph. Artifacts
remain in `conker/build/game-path-heading-turn-15077F64-match/`.

The copied owner uses the production basename `game_A28B0.c.o`. A temporary
`owner.o` basename caused GNU to synthesize different STT_FILE/string metadata
for the inherited overflow section. Matching the real basename removes the
entire diagnostic difference; no symbol/string metadata is excluded.

Actual Make equals the independent owner and **entire ELF** prediction.
Exactly **229 bytes** change, confined to the target slot and its symbol
extent from12 to272. There are no metadata permutations or excluded bytes.
All **6,052 executable addresses** stay fixed; only this target body changes.
All **189,088 protected bytes across720 data owners** remain exact. The full
progress CSV, original ASM, Makefile, headers and helper owner remain fixed.

| Artifact | SHA-256 |
| --- | --- |
| Production owner | `02f3cd2b90e6a5e73b4495d1c9fbaa6c162fb3a7f2b4969dc4788f031c2abfe1` |
| Complete ELF | `16169692060a8ca375662bc2f555d3b6352d28fbb6514714aae7102e5ba32c03` |
| Code binary | `e70d6b8c00049c998f014dc17b39fdf737bc745a5bac764a4fceb5c9bd93865a` |
| Extended guard manifest | `31a596ab2aed75f8e41e1119155b7381d597b7ae51ceda71eaa56b9c78854cd8` |

The production rebuild/recount takes **289.010 seconds**.
`make -C conker all` returns2 only at the known incomplete-project retail
checksum mismatch. Source newline styles and historical documentation bytes
are preserved. README changes only aggregate rows and the verification date.

## Progress and continuation

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,185 / 5,512 | 75.93% | 0 | 1,327 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,512 / 4,839 | 72.58% | 0 | 1,327 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The converted inventory stays5,512/6,046. The80% threshold is4,410,
leaving **225 more** exact functions. Next: **func_150DBC60**, the68-word
oriented-effect parameter constructor in `generated_108E90`, frame0x70,
ROM `0x109110..0x109220`. Recover its complete stack descriptor and the
owner byte0x0C submission to func_15152F70, then run every qualification and
production gate. It is not yet converted or credited.

Retain the eight separate boundaries from Note2103: func_150A76F0,
func_151F8870, func_150A613C, func_150AE280, func_15115F68,
func_151AE2BC, func_150A6760 and func_150A70C0. Preserve the sibling dirty
work, private inputs, real saves and frozen host Release. The80% goal stays
active; this decomp checkpoint adds no host-port gameplay acceptance.

Mounted tools are committed first as
`5b305c06ce1d21b91b4e0956c45a5c33e7e18be7`
(`test(game): qualify path heading and turning callback`). The consumer records
that exact pointer with the complete source/interface, 42 guards and notes.
These are local commits; no push is made.

The ordinary Graphify update refuses its smaller25,042-node replacement.
The following refresh is scoped to eight changed consumer paths. It retains
31,816 nodes from3,754 files outside the current scan corpus; this is not a
fresh full extraction or a graph-package/policy change.

The refresh retains58,843 old IDs and relocates three update-log IDs through
unique same-label/same-source replacements. No nodes outside changed paths
are lost. Eleven IDs are added:eight note nodes and the three relocated IDs.
The result is **58,854 nodes /112,627 links /5,110 communities**, SHA-256
`aa60dfd809916d67b820d4581c38d7b7e1d7d9f62c4111ad02c163b5f2e750f5`.

The source file is confirmed in the detected code corpus. Direct AST
extraction of the installed bytes locates the target atL930 with no outgoing
AST edges. The merged graph still retains an older unmarked `return_type`
relationship to `s32`:the current rebuild preserves unmarked relationships
as semantic evidence rather than treating them as AST-owned deletions.
That legacy link is not this callback's current type. Source, the qualified
original dispatcher and emitted words are authoritative; no call edge is
hand-added or inferred from the stale relationship. A following scoped
refresh leaves the topology and graph hash stable.

The final audit verifies the production ELF/binary/owner/guard hashes,
all135 frozen inputs, unchanged progress/Makefile and the complete helper
owner. Historical documentation bytes remain exact; README changes only
two aggregate rows and the verification date. The independent sibling's
six tracked edits and2,428 untracked files and frozen host Release remain
untouched. The wider80% goal stays active.
