# Owner Burst Emitter Restoration And Match

Verified 2026-10-17. Consumer predecessor `4d3f50e4`; tools predecessor
`a825058`. Both active trees began clean. Tools **971eddb** is committed before
the consumer source/docs pin. This completes the same routine investigated in
[Note1508](1508-owner-burst-emitter-recovery-and-private-layout-gap-20261017.md),
[Note1509](1509-owner-burst-frame-trace-and-aligned-packet-qualification-20261017.md)
and [Note1510](1510-owner-burst-uopt-reservations-and-source-controls-20261017.md).

**Installed:** `func_150F2D14`, owner `generated_11FF10`, VA
`150F2D14..150F3194`, ROM `1201C4..120644`, 288 words / 1,152 bytes,
frame `0x150`. The complete semantic C replaces the zero-return placeholder.
All 288 linked words now match retail, with 268 emitted directly and 20
expected-word guards covering two closed compiler differences. This is not an
unguarded C match or a gameplay/hardware acceptance claim.

## Literal And Storage Recovery

The literal `58.14f` emits the real four-byte pool value `42688F5C` at retail
ROM `0x24642C`, runtime `D_800A196C = 0x800A196C`. Qualification checks the
complete 16-byte object pool, its single target HI16/LO16 pair, zero addends,
LUI/LWC1 opcodes, common base register and the existing production anchor.
The isolated linker retains the actual section relocation and pool bytes;
it does not invent an unknown symbol address or rewrite instructions.

The production owner uses the existing `RETAIL_RODATA_SYMBOL` padder binding
to `D_800A196C`. Only four bytes are live: the object's twelve terminal zero
alignment bytes are not installed over neighboring retail data. All other
owner pools and all eleven raw/padded neighbor functions remain unchanged.
The compiler profile is unchanged.

| Complete Source Form | Words | Frame | Unequal Words |
| --- | ---: | ---: | ---: |
| Previous aligned packets / cached scale | 288 | `0x160` | 85 |
| Real literal scale | 288 | `0x160` | 75 |
| Merge duplicate payload pointers | 288 | `0x158` | 75 |
| Put real scalar locals in alignment gaps | 288 | `0x150` | 20 |

The selected declarations place `created` before the aligned descriptor and
`owner` before the aligned input pair. Each occupies an existing four-byte
alignment gap. Swapping the two scalars yields identical instructions. There
are no fabricated parameters, inert padding locals, or frame/address guards.
All caller-relative packet positions and the saved payload pointer remain:

| Storage | Caller-Relative Offset |
| --- | ---: |
| Delta vector | -180 |
| Output pointer pair | -168 |
| Input pointer pair | -160 |
| 52-byte payload | -148 |
| 88-byte descriptor | -96 |
| Saved payload pointer | -4 |

Explicit typed layouts and a short purpose comment are retained in C. The
address-based function name remains stable; the alignment-compatible union
representations are recovered layout choices, not proof of original source
union/u64 declarations.

## Allocation Evidence And Bounded Guards

Five fingerprint-locked UOPT observations extend the prior local trace:
local entry `0x434130`, spill entry `0x450490`, global entry `0x47FE70`,
global return `0x436060`, reemit entry `0x448A80`. These are compiler host PCs,
not Conker guest addresses. For the earlier aligned form, the cursor is
196/196/208/208/208. The selector is `0x08000003`, selecting image bits
4/30/31: actor+0x28, owner-state byte+0x222, and its integer conversion.

Live image/range identities and descriptor attachments agree at every stage.
Colors are 0/0/0 before global coloring and 14/2/1 afterward, corresponding
to emitted GPR16/GPR3/GPR2. The reservations occur before coloring and persist
after values acquire registers; output UCODE and actual machine roles agree.
This does not prove actual spilling or the original compiler implementation.
Owned child completion, fired probes, cleanup and normal-object identity are
required. Sixty-six effective stage controls and eleven pool controls pass.

The final twenty guards are deliberately restricted:

- Eight words close one V0/V1 state-allocation cycle, including one
  commutative BEQ operand-order difference. The next definition closes the
  lifetime; the original unreachable duplicate load at offset `0x8C` remains.
- Twelve words form one closed transform-setup permutation. Its complete
  instruction multiset, arithmetic dependency chain and pointer-store chain
  are preserved. No instruction is inserted or omitted.

No guard changes the frame, packet addresses, branch geometry or logic. None
has a relocation. All twenty expected-word rejection controls and two closed
group/dependency controls are effective. The raw source still differs at a
private access prefix (cut 23); the guarded result matches from cut zero.

## Fresh Qualification

The final installed suite passes **7 tests in 58.929s**. The repaired research
suite passes **7 tests in 91.351s**, and the four affected historical checkpoint
cases pass **4 tests in 85.068s**. Earlier unchanged broad neighbor suites are
prior evidence, not freshly rerun suites.

- 7,800 complete public-memory/call-packet cases and 56 modeled FP edges,
  including both synthetic initial scale `1.25` and real `58.14f`, provider
  mutation and nonuniform copied padding without masks. Retail reachability
  covers 287 words; the original duplicate load is statically unreachable.
- 36 completed full-private cases and 3,768 memory-fault prefixes, comparing
  registers, stack, memory and calls across two phases and stack patterns.
- Two independent carry rebases and 192 complete protocol cases; both closed
  guard groups remain valid under rebasing.
- Native32 O2/O0, UBSan, 960 typed defined-field cases per profile and eight
  effective controls. Native tests use the real literal; they do not qualify
  arbitrary modified constant pools, guest padding or portable fault behavior.
- Twelve complete research forms, including both equivalent gap placements,
  and seven genuine executable-overflow rejections.
- The dispatch table's `0x8008A658` slot / ROM `0x22F118` remains unchanged.

One earlier research negative incorrectly expected synthetic `1.25` memory
to reject the literal candidate. Both binaries still load the same physical
slot, so both values must agree in the guest model. That expectation was
corrected, not production semantics. Another rejected test-control mask was
corrected to reach the intended closed-cycle gate. Failed runs are not counted.
The new installed packet receipt also removes the older research-only
"private frame still unmatched" label; private state is qualified separately.

## Complete First Image And Checkpoint

The first normal production build exits zero and its **entire ELF equals the
immutable prelink prediction**. No metadata section or byte is excluded:

| Declared Change | ELF Bytes |
| --- | ---: |
| Target code slot | 922 |
| Target symbol extent | 2 |
| Three exactly checked symbol/string serialization pairs | 69 |
| Total | 993 |

All 6,057 function bodies/addresses are audited: only this target body changes,
its slot/address stays fixed, and every other named definition is preserved.
All 189,088 Game-data bytes across 720 owners remain exact. The guard manifest
is a literal twenty-row append; its older mixed-ending byte prefix is intact.
Existing duplicate `generated_12D630` recipe and legacy compiler warnings remain;
this is not a warning-free build.

```text
Before ELF: 5efb8a9f598af0712d97eaf4d0f2ab2df134e349ad16eddfeb0f75e74128b7d4
After ELF:  245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60
Raw target: f5a54eea68420c05735c7f2b3e65f9ddbae01123fa1e9dc9d6275812b9305907
```

Ten before/after checkpoint members are immutable, with twenty corruption
controls. Six small historical adapters reverse only exact known successor
hashes; unknown bytes are not translated. Older first images and fixtures are
preserved. All 271 protected entries / 249 paths are accounted for, with only
the ten declared successor inputs changed.

Ignored receipts are under `conker/build/game-owner-burst-match`,
`game-owner-burst-install`, `game-owner-burst-literal-candidates` and
`game-owner-burst-allocation-stages`. Reproduction from the consumer root:

```sh
python3 -m unittest tools.tests.test_game_owner_burst_match -v
python3 -m unittest tools.tests.test_game_owner_burst_literal_and_allocation -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Fresh totals: Game **2,965 / 4,828 (61.41%)**, total **3,638 / 5,501 (66.13%)**,
1,863 still different and zero drift. Init 492/492 and Debugger 181/181 remain
exact among converted functions. Nominal conversion counts are unchanged;
the old placeholder was already counted as C. Root README changes aggregates
only; function updates remain in these docs.

Both tools copies freshly pass twelve shared tests and smoke checks. Twenty-six
ASCII/AST parses and thirteen identical task pairs pass. Before copying, all six
modified mirror files matched their frozen predecessors and seven destinations
were absent. All 1,133 unrelated hashes and mirror HEAD `ddbdd16b` are preserved;
the mirror now has 1,146 dirty paths. No mirror commit/reset, push, dependency
installation, Claude call, host-port change or frozen Release action.

The native full-corpus `graphify update .` exits one at its shrink guard and
preserves the existing 42,221-node graph; no force override is used. Its
existing incremental rebuild API, supplied the 23 changed file paths,
succeeds with 42,230 nodes / 82,365 edges / 3,918 communities. All unrelated
node identities survive; three replaced IDs belong to the edited update log.
The retained 19,398 nodes from 2,972 still-existing excluded files are not
purged. Existing skill-version, empty devcontainer and HTML-size warnings
are graph-tool limits, not decomp compilation failures.

## Resume Point

- [x] Recover and qualify the actual literal pool and retail frame/packet homes.
- [x] Install complete C with twenty bounded guards and exact first-image proof.
- [x] Preserve historical checkpoints and unrelated mirror work; bank tools first.
- [ ] On resume, recover `func_150F34F4`, the next zero-return placeholder in
  this owner: VA `150F34F4..150F43F0`, 959 retail words. `func_150F34A0` is
  already semantic C; do not replace it with a new stub.
- [ ] Keep the 139-word `func_150F2A60` gate, both fade lifetime gaps and wider
  Game matching open. Opaque providers/full caller behavior, gameplay,
  hardware and general FCSR acceptance remain separate and unclaimed.

The live goal was found paused during final checkpointing. Finish this commit
and leave it paused; no subsequent function is started in this checkpoint.
