# Record List Loader and Relocation Match - 2026-11-08

`func_1509CF28` now matches all **75 words / 300 bytes** with the original
**0x50-byte frame** and local count at **SP+0x40**. Its complete semantic C
uses **22 checked guards** for a closed temporary-register mapping and two
independent scheduling swaps. No instruction is inserted or omitted.
The owner keeps its established O2/g3/no-unroll MIPS2/O32 profile; no
Makefile or shared-header change is needed.

Production recount: Total **4,257 / 5,513 (77.22%)**, Game **3,584 / 4,840
(74.05%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,256** different converted functions and **154** additional
exact functions needed to reach 4,411 / 5,513 and the active 80% goal.
Conversion rows and denominators remain unchanged.

## Source, ABI and loader behavior

Owner: `conker/src/game/generated_C9EC0.c`. VA 0x1509CF28..0x1509D054;
ROM 0xCA3D8..0xCA504. The recovered interface is:

```c
s32 func_1509CF28(s32 resource, u32 *lastIndex);
```

The existing loader provider in `game_57FA0.c` has four fixed words and
variable path arguments:

```c
void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...);
```

Initialize the local count to zero, then submit exactly seven physical
words: `(NULL, 0, &count, 3, 8, 0, resource)`. Word seven is stored in the
JAL delay slot. The incoming full resource word survives without narrowing.
The count is held as u32 because the original compares it unsigned; the
provider receives the corresponding signed-word pointer type.

Publish the loader result to `D_800D2FB0` before checking null. Reload the
output pointer from its incoming home after the call. Null clears that
output word and returns zero. Success writes `count - 1` to result+4 and
then the output word, reloading count for each store. Counts zero and one
still return success; zero produces an unsigned 0xFFFFFFFF last index.

## Relocation walk and alias-sensitive lifetimes

For indices 1 through the live count minus one, use an eight-byte table
stride. Fetch the list through the current global table. Process every
pair, including the final flagged pair: add the current entry's base to
word zero, preserve only the low 28 bits of word one, and stop when the
original word one had bit 31 set. Pair advancement occurs in the branch
delay slot.

The inner loop reloads the global table pointer and current table entry.
The post-walk record pointer instead comes through a cursor rooted in the
original loader result. Mask and shift that record's word +0xC right by one,
advance the cursor, and reload count before the next outer iteration.
These are different lifetimes, represented by distinct `loaded`, `cursor`,
`pair` and `record` variables in C.

Guest cases deliberately alias output with the count home, loaded header,
global pointer, table entry and pair fields. Other cases make a pair store
change the global table mid-walk or wrap the live count to a smaller bound.
Controls reject caching the global/count or substituting the global table
for the original post-walk cursor. These synthetic private/global aliases
qualify emitted MIPS behavior and are separate from the native valid-domain
fixtures. Nine malformed/large-count cases execute to an unmapped-read
boundary; no early validation or fabricated success path is added.

## Original callers and cleanup

The pristine aligned census finds two direct JALs and no aligned
entry/interior pointer literals or interior direct entries:

- `func_151DF574`: ROM **0x20CBE4**, VA **0x151DF734**. Its ten-word
  window passes an output home at caller SP+0xB4, reloads that result,
  updates the actor-state flag and consumes the returned success flag.
  The count-dependent delay-slot shift follows the original modulo-32 rule.
- `func_151E30C4`: ROM **0x2105A4**, VA **0x151E30F4**. Its 13-word
  load/query/cleanup window sign-extends the resource byte, reloads the
  resource and subindex after the loader, submits the four-word query,
  then runs the original 14-word `func_1509D054` cleanup routine. That
  routine calls the original release service for a nonnull table and
  clears the global pointer.

**240 connected cases** cover both windows, loader home mutations, the
first result/count branch, second caller's live global reloads, original
cleanup and release packet. The larger parents and loader/query/release
service bodies are not fully emulated; helper effects are bounded and
explicitly modeled.

## Owner, compiler and guards

Initial private screens used the default profile; actual-owner review
identified the existing no-unroll setting. The final qualifier uses that
profile for both predecessor and candidate, and the actual Make recipe
confirms it. The target's raw body is identical across those two screens,
but only the inherited profile preserves the complete compiled owner.

All **18** raw and padded neighbors, pools and **58** original labels are
preserved. The independently compiled isolated target has identical words
and bindings. Its register declaration derives the exact complete-owner
GPR union; CPR masks and GP remain unchanged. All **72** register-metadata
byte-corruption controls fail closed.

The normalization changes only volatile temporaries after the sole loader
call. One swap moves the independent mask ORI and original-result cursor
copy; the other swaps independent cursor/offset increments. Every memory
operation remains in the same order. All 75 raw words and three bindings
are pinned; altered-word and altered-binding controls reject unknown input.
Both padders and the three-command actual Make recipe produce the identical
qualified owner with zero C diagnostics and no profile changes.

## Fresh execution and whole-image evidence

Six focused checks pass before and after installation in both tools copies,
with four sequential runs and exact source/dependency fingerprints:

- **876 guest cases**, with all **75 words** reached. There are 867 normal
  returns and nine unmapped-read prefixes. Original and normalized literal
  register/memory/trace states agree; the raw compiler stream also has the
  same complete memory effects, calls and read order.
- **367 memory-fault cuts** compare exact original/normalized prefixes.
- **736 native32 cases per profile**, at O0/O2/O3 with trapping UBSan,
  exercise actual C variable arguments, complete table/list words, output
  aliases and all **16** effective semantic controls.
- Three independent GNU links and **18** rebased guest executions qualify
  the helper and both halves of the global-pointer binding, including
  signed-low-half carries. Four complete-image corruption controls cover
  headers, function body, symbol extent and protected data.

The independent full-ELF predictor replaces only this function's 300-byte
slot and changes its symbol extent from 12 to 300 bytes. Actual and
predicted files are identical: **224 changed bytes, zero exclusions**.
All **6,052** disassembled entries retain their addresses; every other
function body, extent and metadata byte remains unchanged. Protected data
remains **720 owners / 189,088 bytes**, with no changed byte.

Production Make compiles only this owner under the inherited no-unroll
profile, links the predicted ELF, regenerates an identical progress CSV,
and passes a fresh recount. `make all` retains the existing whole-ROM
checksum failure (exit 2); this function match does not claim the full ROM
is byte-exact. The inherited duplicate-recipe warning for generated_12D630
is unchanged.

Both fresh shared tools smoke checks pass. Three prior shared regression
checks per copy are explicitly reused with identical helper/test hashes.
The sibling's **2,434 pre-existing dirty paths** are fingerprinted and
preserved, with only a private three-file validation overlay.

ELF SHA-256: `0e30fac10f61f81713ed1ad9574f79aafdad34d6b66a37dfc7a651ec69c35579`.
Binary SHA-256: `137dbd4cdf32d494d14996b260e9a2d30b3e7f7e934535efce9fb3bfd6fd0c5e`.
Owner SHA-256: `9529026bbeb0ca151569f31ab9021ffd493aea664ef941bfd5b2df0fd3516aed`.
Guard CSV SHA-256: `ab4a2eb5c63a044bbb705009b55df2cf31a32791f1b99391efa32ab30544426c`.

## Resume boundary

Next candidate: **`func_15063254`** in `game_83300.c`, still an uncredited
zero-return placeholder. Its body is **76 instructions / 304 bytes**,
VA 0x15063254..0x15063384 / ROM 0x90704..0x90834, with frame 0x58. The
progress/retail slot is **316 bytes / 79 words** through VA 0x15063390;
its final three words are padding nops. Keep body and slot sizes separate.

One direct JAL is at ROM **0xC6E10** / VA **0x15099960**, in
`func_15097A8C`; no entry/interior pointer literal was found. Qualify its
four-word pointer/byte-field/FP-bit interface, captured auxiliary pointer,
six saved FP words, facing halfword and saved-owner restoration across
`func_15060F28` and `func_15082A44`. Preserve fresh post-helper reads and
full payload bits. Reconcile its old generated declaration and inspect the
actual owner/compiler profile before screening. Scratch:
`conker/build/game-actor-snapshot-15063254-match/`.

Current receipts: `conker/build/game-record-relocation-1509CF28-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
has changed-path and old-node-retention evidence, retaining existing
unscanned nodes without claiming a new full-corpus extraction. Frozen
host Release artifacts are untouched. The 80% goal remains active.
