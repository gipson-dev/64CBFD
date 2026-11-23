# Resource cache sweep guarded byte match - 2026-11-23

`func_15114A1C` replaces its zero-return placeholder with the complete resource
cache cleanup loop. Its **94 retail words / frame 64** are byte-exact through
qualified guarded C. Total rises from **4,637 to 4,638 / 5,528 (83.90%)**;
Game is **3,965 / 4,855 (81.67%)**, Init 492/492 and Debugger 181/181.
There is zero address drift, 890 different functions, and **61 more matches
are needed for 85%**. This counts one complete function.

## Retail behavior and caller

The complete original is `conker/asm/13D350.s:5223`, VA
`15114A1C..15114B94`, ROM `141ECC..142044`. It scans signed live count
`D_800DBEF0` with 0xA0-byte records from `D_800DBEF4`, resource pointers from
`D_800DBEF8`, and byte ages from `D_800DBEFC`. Nonpositive counts do no work.

- Record flag 0x70 bit zero controls the two cleanup branches. The set branch
  clears its resource slot without release when 0x6F bit 0x80 is clear.
- In the clear branch, null resource slots are skipped. Type byte 0x4E equal
  to three, or flag 0x6F bit 0x80, selects the retained-resource age path.
  A nonzero age decrements; age zero releases the resource. Other nonnull
  resources release immediately.
- The pointer table is reloaded after the opaque release call before clearing
  its slot. Records, ages and count preserve their retail reload lifetimes;
  provider mutations can rebind each table, grow the bounded count, or end
  the scan. Capturing these globals once would be incorrect.

The actual caller is in `conker/src/game_45B80.c`. Its incorrect `s32(void)`
prototype is now `void(void)`, matching the original routine's unused return
register. All 16 complete caller functions, bindings and literal pools remain
identical; both before/after production padded caller objects are literally
equal to the frozen baseline. Only raw compiler debug type information differs.
The literal JAL/delay window at `15018CCC` reaches the next original call to
`func_1517CFC4` in 48 connected cases per stream. This is a bounded call-window
check, not a claim about the complete graphics loop or release-helper internals.

## Closed transform and focused checks

The complete semantic C body emits **92 words / frame 56** under the existing
O2/g3/o32 profile. All 33 owner neighbors, their bindings, literal pools and
diagnostics stay fixed. The transform pins every source word and all 18 binding
sites. It allocates the same live roles, restores the original 64-byte frame,
orders the corresponding saved-register operations, and uses the two call
delay NOPs for the required A1-to-A0 argument moves. The unused retail S3 save
and restore add two words. There are **92 strict guards, two insertions, zero
omissions**; the entire existing guard CSV remains an unchanged prefix.

An independent instruction interpreter does not consume this projection. It
checks both entry paths and all **16 inductive loop/exit paths** from arbitrary
related loop states. Ordered public reads, writes, opaque call arguments,
loop-carried roles and all o32 saved-register lifetimes agree. Fresh symbolic
reads conservatively cover aliases and arbitrary public effects at each call.
Fifteen semantic mutations fail; an independent temporary-register allocation
passes. This is a normal-execution proof with mapped ordinary public RAM
outside the private frame and a returning o32 provider. Native C additionally
requires valid typed, bounded arrays. MMIO, races and raw C trap/private-state
identity are outside this contract.

- **576 cases per raw/generic-padded/generated-padded/retail stream** agree with
  an independent public-memory and ordered-call model. Both normalized streams
  match retail's complete register, private-memory and trace states. The two
  unexecuted original words, 51 and 68, are unreachable duplicate loads retained
  literally. The raw C private bytes are not claimed identical.
- **292 fired access-prefix triples** check the two padded streams against retail;
  this does not claim raw C fault-prefix equality.
- Actual SDK32 native C at O0/O2/O3 passes all 576 cases/profile with strict
  aliasing and UBSan. Typed pointer/resource arrays, complete byte backing,
  guard regions and ordered release arguments are compared. All seven source
  mutation controls fail by result comparison.
- Both real padders reject every changed source word and binding: **220
  effective rejections**, plus both oversized-body controls. Twelve independent
  GNU links across four code/global arrangements match original ASM; 64 guest
  rebase runs check public state and call order.

Both full-owner padders agree on all text, function definitions, relocation
bindings and literal pools. Their object symbol/relocation-table metadata
differs; the production generated-padder object is the accepted artifact.
Actual Make replay reproduces that entire object exactly.

The preinstall receipts precede a caller-pin metadata correction: the hash
initially described CRLF text while the tested/materialized caller used LF.
Only `selected_caller_sha256` changed in the manifest; C bodies, interfaces,
objects, guards and the full-image prediction stayed fixed. An early canonical
source/pin consistency assertion and an effective wrong-pin control now cover
both phases. Both installed checkouts ran all five gates fresh against that
correction. The original preinstall receipts and one-field correction
certificate are preserved in the ignored target directory.

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 112.450s | 5 fresh / 0 reused |
| preinstall-sibling | 109.784s | 5 fresh / 0 reused |
| installed-primary | 124.163s | 5 fresh / 0 reused |
| installed-sibling | 116.470s | 5 fresh / 0 reused |

## Production, preservation and resume

The independent predictor recompiles frozen old C with old guards and replaces
only the target with original ASM. It reconstructs the target's declared size
and every ELF byte without source guards or exclusions. Actual production equals
this prediction: **291 changed bytes, zero exclusions**. All
189,088 protected Game data bytes and all 720 data owners remain exact.

```text
before ELF: 47817ce9cabf98e1ecc9fb9281bdd90e24bd3096ae21b3f6849326a5289ecd54
after ELF:  9999cd2e749bcb56978dbd18e9e09485cfd4819bfc5cbd653a3b7fd2d192421b
owner:      017d98fff58a1287caf5a26efe1aeb252b77a9a2843c5574661b868ddf94d0a8
```

Production uses the real Make recipes for the changed owner and caller. The
shared CSV's timestamp is held old with `-o retail_word_patches.us.csv` after
verifying that its appended rows belong only to this target; the unchanged
history and every other frozen object are audited by hash. This avoids rebuilding
unaffected owners. Conversion rows, layouts, shared headers and the complete
debugger object remain frozen. Shared `make tools-check` passes.

The real dirty sibling tools checkout is preserved; its qualification overlay
records task, sibling and primary-fallback origins. The two inspected host
scene configurations still consume binary artifacts; the selected scene also
lists this target as a stub. No host C consumer or complete host build root is
present at that path. This decomp match does not enable that host path; no host
build or frozen Release artifact is used.

Tools qualification commit `31f4ab706671983cf899a41a1ed48e18213edf73`
and caller-pin fix `259c3a8e51cd1a3ba5e092811ac4f12e41e3748e` precede the consumer
source/guards/pin/docs commit. Nothing is pushed. Graphify refresh and scoped
AST qualification retain every prior ID after observed hook producers finish;
this is not full-corpus re-extraction. README receives aggregate status rows only.

The larger `func_15197148` ribbon-renderer recovery remains private and uncredited
in `conker/build/game-effect-ring-ribbon-15197148-private/HANDOFF_CURRENT.md`.
Its original baseline and completed compiler screens are intact. Resume the
ordinary Game C queue at `func_151D1448` using the new committed baseline;
its complete 98-word boundary and original `func_151D1138` caller are screened
in `NEXT_TARGET_SCREEN.md`. Shared handwritten
entrypoints need separate boundary/ABI audits. The 85% total goal remains open.
