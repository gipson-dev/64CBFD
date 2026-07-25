# Contributor and Byte-Matching Guide

This guide covers the normal workflow for converting and matching functions in
the `conker/` code project. Read the [project overview](PROJECT.md) first if the
repository has not built successfully on your machine.

## Before editing

Confirm that the ROM has been extracted and the current tree builds:

```sh
make -C conker --jobs NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
```

`NON_MATCHING=1` allows development builds while functions still differ from
retail. It does not make a function count as byte-exact.

Keep unrelated user changes out of the patch. Generated build output under
`conker/build/` and local ROM material must not be committed.

## Pick useful work

List every non-exact C function from the smallest real diff upward:

```sh
make -C conker match-progress NON_MATCHING=1 LIST=1
```

Fast candidates are usually:

- short constant-return, accessor, setter, and predicate functions;
- thin wrappers that forward arguments to one or two callees;
- repeated function families with the same instruction shape;
- functions with only a few real instruction differences;
- generated-slice placeholders whose retail body is compact and regular.

Prioritize repeated families when one recovered source shape can solve several
functions. Do not assume two functions match merely because they have the same
length; compare their retail instructions and constants.

## Understand the two progress measurements

```sh
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
```

- `progress` counts functions represented in C instead of raw assembly.
- `match-progress` compares each linked function against pristine retail bytes
  at the address implied by its symbol name.
- `exact` means every compared instruction matches.
- `blocked` means only a relocatable address differs. These functions normally
  heal when the referenced code or data placement is fixed.
- `diff` means the function still has real instruction differences or an
  incompatible length.

The symbol-based matcher is the authoritative project-wide measurement. A
whole-binary diff can become misleading when an earlier layout difference
shifts later code.

## Normal edit and test loop

1. Find the function in `conker/src/` and its retail span in
   `conker/retail_layout.us.txt`.
2. Inspect the retail instructions at the function's name-implied address.
3. Reconstruct the smallest plausible C body.
4. Build the containing object or the full code project.
5. Compare the compiled instructions and adjust one source property at a time.
6. Run the full matcher before counting the function as a win.

For a generated slice, a focused object build is faster than relinking the
whole project:

```sh
make -C conker build/src/game/generated_NAME.c.o NON_MATCHING=1
```

Use the real generated filename in place of `generated_NAME.c`. After the
object matches, run the full build and matcher because relocations are only
final after linking.

## Retail spans and generated slices

Generated source files preserve the original retail layout. The object-padding
tools keep each function in its assigned span so one non-matching body cannot
shift later functions.

If a compiled body is larger than its retail span, the build fails with a
message similar to:

```text
compiled func_XXXXXXXX is 0xNN bytes but its retail span is only 0xMM
```

That is a source-shape failure, not a reason to enlarge the span. Revert the
experiment or find a smaller expression, type, or control-flow shape.

## Compiler-sensitive patterns

The project uses IDO 5.3, so semantically equivalent C can produce different
register allocation and scheduling. The following patterns have repeatedly
resolved compact game functions:

### Argument widths and home slots

Use the width shown by retail loads and stores. `u8`, `s8`, `u16`, and `s16`
parameters can change sign extension, stack homing, and which byte of a saved
argument is reloaded on big-endian MIPS.

Empty callbacks may still need typed parameters because retail stores incoming
arguments even when the function performs no other work.

### Explicit temporaries

An explicit local can keep an intermediate in `v0`, preserve a pointer across
a call, or produce the retail load order. Add temporaries only when the retail
instructions show that lifetime; unnecessary locals often create extra moves
or stack traffic.

### Repeated volatile reads

Use a `volatile` cast when retail deliberately reloads the same field, such as
a null check followed by a second load in a `jal` delay slot. Do not apply
`volatile` broadly: it can bloat a function or prevent useful coalescing.

### Expression and call order

Commutative arithmetic and boolean expressions are not interchangeable for
byte matching. Operand order can change floating-point registers, delay slots,
and final instruction operands. Multi-argument calls may also require a named
temporary so IDO assigns the retail register before the call.

### Physical source-line layout

IDO can schedule identical C differently when statements occupy different
physical source lines. In `func_151E50C8`, putting the complete 23-byte copy
loop on one line changed the four-way unrolled body from the helper's
`1, 2, 3, 0` load order to retail's `0, 1, 2, 3` order. An algebraically
neutral expression such as `condition ^ 0` can likewise preserve later
register allocation. Use these only for a measured final scheduling mismatch;
the decomp permuter's same-line and expression passes can search this space.

### Generated-slice BSS ownership

IDO's address coalescing depends on which globals it believes the current
translation unit owns. A correctly-sized definition can therefore be needed
to reproduce retail `%hi` reuse even when the final link already supplies the
symbol. For generated slices, `pad_generated_object.py` emits only compiled
text and text relocations, so the compact object's temporary `.bss` storage is
discarded and the final symbol still resolves through the project's linker
symbols. Always verify this pattern through the production padded-object
recipe and a full link; do not use it for ordinary objects whose `.bss` is
linked normally.

### Reference decomp source and compile profiles

A completed decompilation of another game built with the same SDK can provide
more than semantic reference code. Compare retail instruction bodies with
relocation operands masked, then port both the source shape and the owning
object's compiler profile. The first Banjo-Kazooie cross-port batch showed
valid matches under plain `-O2`, `-O1`, and `-O3`; compiling every copied
function with Conker's default `-O2 -g3` did not reproduce retail.

Headers can also change code generation. For example, Conker's broad graphics
header marks `sqrtf` intrinsic, while the matching `guNormalize` object calls
`sqrtf`; that source therefore includes only the needed math declaration.
Keep such exceptions local to the object and verify all neighboring functions
after changing a shared compiler override.

When a target is a second copy of an SDK routine, check the project's
already-exact primary copy before importing external source. Batch 2's
controller, PFS, timer, SI DMA, and time routines matched by reusing those
local bodies with only duplicate function/helper names changed; Banjo then
confirmed the SDK version and `-O1` profile. This preserves project-local
types and symbol aliases while still using the completed decomp as evidence.

If one function inside a larger translation unit needs a different compiler
profile, isolate it as its own extraction subsegment and object instead of
changing the shared override. Batch 3's `func_151F27E0` requires Banjo's
`-O1` profile while the following audio code requires `-g`; splitting at the
retail boundary preserves both profiles. Record the split in the tracked
version YAML, keep the objects in retail order, then run a fresh extraction,
full rebuild, and neighbor scan so generated linker-script layout and nearby
exact functions are both verified.

### Stack-local records

Small event or command records often appear as a local structure passed to two
helpers. Match the structure's real size and field widths; padding changes the
frame size and local offsets even if only the first fields are written.

### Name-implied globals

Use the correct `D_XXXXXXXX` symbol instead of a literal pointer. The matcher
resolves those names at their retail VRAM addresses and can distinguish a
source mismatch from linked address drift.

### No `switch` in generated-slice files

Do not write a C `switch` statement in any `generated_*.c` file. IDO compiles
a multi-case `switch` to a jump table placed in `.rodata`; these files build
as standalone per-function objects padded to their retail span with no real
rodata segment behind them, so the link fails with `undefined reference to
'.rodata'` (the padding/compile step succeeds - this only surfaces at the full
link, so it's easy to miss until the whole project is relinked). Rewrite as an
if/else-if chain instead.

## Avoid false wins

- A successful compile does not prove a match.
- A lower real-diff count is useful, but it is not byte-exact progress.
- Do not keep an experiment that makes a function exceed its retail span.
- Do not alter matcher rules to hide a genuine instruction difference.
- Do not use a shifted current-build address as retail ground truth; use the
  function's name-implied retail address.
- Recheck repeated-family members individually because constants, offsets, or
  signedness may differ.

## Required validation

Before publishing a matching batch, run:

```sh
make -C conker --jobs NON_MATCHING=1
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
git diff --check
```

Confirm that:

- the full code build succeeds;
- the exact count increases by the expected number;
- no previously exact section regresses;
- raw-conversion totals change only when raw assembly was actually converted;
- address-drift blockers do not unexpectedly increase;
- documentation numbers and progress bars match the verified output;
- only intended tracked files are staged.

Record published milestones in [UPDATE_LOG.md](UPDATE_LOG.md). Put temporary
experiments, rejected source shapes, and crash-recovery details in
[WORKING_NOTES.md](WORKING_NOTES.md), then move durable conclusions back into
this guide or the relevant subject document.
