# Color Record And Pointer Table Reset

Date: 2026-10-20. Consumer predecessor `97b6ab57`; active tools
predecessor `ff22329`. The 75% total C-matching goal remains active.

## Target And Ordering

`func_150B6C90` in
[generated_E4070.c](../../conker/src/game/generated_E4070.c):
VA **150B6C90..150B6D34**, ROM **E4140..E41E4**,
**41 words / 164 bytes**, **40-byte frame**. The predecessor C was a
zero-return placeholder, with 38 differences in the old linked image.

Conditionally remove the original `D_800D9894` record through
`func_1516972C`. Only after that call, reload the complete word at
`D_800BE9E8`, not the distinct timestep word at `800BE9E4`.
Call the already recovered type-0x5A color factory with all eight words:
`(0, 0, 255, 0, 0, view, 0, 0)`.

Publish the returned pointer, including NULL, to `D_800D9894`; store
**byte 3** at `D_800D9890`, preserving its three neighboring bytes.
Clear ten pointer slots at **800D9898..800D98C0**. The first two stores
precede the remaining eight-slot, four-at-a-time loop. No early return on
factory failure, premature pointer clear, widened state store or semantic
effect identity is justified.

## Actual Dispatch And ABI

The complete pristine ROM JAL scan finds exactly one direct target call:
**150B6BF8**, ROM **E40A8**, in the **52-word/frame24 func_150B6BC0**.
There is no aligned literal pointer to the target.

That dispatcher has no direct JAL caller. Its sole aligned literal pointer
is **2317D8**, VA **8008CD18**, slot **5** of the table at **8008CD04** in
[231730.rodata.s](../../conker/asm/data/231730.rodata.s).
The outer **43-word func_151749F8** selects this table with its record's
unsigned byte at 0x0B, calls through it and does not consume the result.
The actual window **15174A2C..15174A58** includes the record lookup,
slot-zero bypass, slot-5 indirect call and its delay slot. The complete
outer parent is not claimed by this window.

The return is unused through both caller levels. Recover a
`void func_150B6C90(void)` API, preserving the address-based name and a
purpose comment. Do not invent a meaningful return value from the
incidental loop cursor left in v0.

## Owner Profile And Fitting

The existing Makefile already assigns this owner
`-O2 -g3 -Wo,-loopunroll,0`. Do not change it or use an isolated default
profile as production evidence. The established
`game_view_list_setup.compile_owner(..., no_unroll=True)` wrapper applies
the flag only to the compiler, not to the ASM processor.

Default-profile diagnostics emitted 51 words for the natural loop and
66 for explicit quads. A direct attempt to pass the optimizer flag through
the generic helper was rejected by the ASM processor before compilation.
Neither route is installation evidence.

Under the correct existing owner profile, the natural loop emits 39
words; the selected four-at-a-time form emits 42. The initial 21 words,
both helper calls and frame already match. The raw body is 168 bytes,
not a direct fit to the 164-byte slot. It has 16 relocation bindings.

Seventeen expected-word/relocation guards normalize independent setup
scheduling, the complete v0/v1 loop cursor/end allocation cycle, and one
fixed-layout address fold. The fold removes the materialized address of
the first pointer pair and uses one adjusted-HI16 base with two relocated
stores. Exactly one address instruction is omitted; none is inserted.
The resulting 41 words and 17 bindings equal independent GNU assembly of
the original routine. This is guarded semantic C, not compiler-only C.

The pair at `D_800D9898` and `D_800D989C` must share its adjusted-HI16
page; the layout gate also checks word alignment and all table spacings.
A split pair at `80347FFC` is explicitly unsupported. Other supported
rebases exercise signed-low carry. Do not claim arbitrary placement.
Raw C leaves a different private caller-saved a0; its public effects and
C ABI are compared, while the fitted routine must match full retail state.

## Qualification Boundary

The input snapshot freezes **27** source/header/assembly/data/layout/image/
build files and separately pins the old padded owner object. The predecessor
ELF SHA-256 is
`9c49b22ea18204941236929c1b2b692fde1a23003166cb685ea767423482d44b`.
Old owner-object SHA-256:
`0ea31300ad8af9399f9f78986b405043c1771d4530eb146199b17c6267b05dd5`.

Before installation, require the complete routine, real eight-word factory
packet, release/factory mutation ordering, NULL path, all ten pointer
stores, untouched bytes, typed/fenced native32 fixtures, effective semantic
negatives, actual caller dispatch, independent GNU rebases, unchanged
owner neighbors/pools/metadata and the actual owner Make output.
Execute bounded original callee paths where practical; distinguish
callback/lower-allocator providers from complete heap or gameplay proof.
Guest aliases/fault prefixes are not portable C invalid-memory claims.

Then install only the independently qualified source, rebuild the full
ELF/progress CSV, reproduce a closed whole-image prediction, audit every
other body/address and protected data, and run the literal standard matcher.
Fresh installed-input/compiler/image checks must pass; reuse unchanged
pre-install tests only under explicit input/object/helper/image identity.

## Installed Checkpoint

Each copy passes all eight tests before installation, with zero errors,
failures or skips. Each then freshly passes the two install-sensitive
checks (01 and 08), including a fresh isolated compile, full installed
audit and all 27 frozen inputs. The six unchanged model/native/caller/
guard/rebase checks per copy reuse pre-install receipts only under strict
source, raw/padded object, helper, tools and whole-image identity. They
are not claimed as fresh installed reruns. Copies run sequentially:

| Run | Fresh Tests | Runner Seconds |
| --- | ---: | ---: |
| Primary, pre-install | 8 | 579.224 |
| Older mirror, pre-install | 8 | 383.711 |
| Primary, installed | 2 | 433.557 |
| Older mirror, installed | 2 | 43.729 |

Runner times exclude module-loading time; the installed child processes
take 742.470s and 166.464s respectively. Both shared tools checks pass.
The inherited duplicate generated_12D630 Make recipe warning is not a
new target warning; do not claim a globally warning-free build.

Each complete suite covers **472 cases / 944 modeled phases**, including
**48 guest-only phases**, all **41 fitted and 42 raw instruction words**,
and **448 native32 cases** at O0/O2/O3 with trap UBSan. Twelve compiled
semantic negatives are effective. Typed, fenced `void *slots[10]` fixtures
check all bytes without treating arbitrary pointer bits as valid heap
allocations. Raw private caller-saved a0 identity is not claimed.

All **144 original helper words** execute over **128 phases**. The actual
**11-word outer call window** and complete **52-word dispatcher** pass
**64 phases / 192 fired joins**. Test reset/default cases, not the other
dispatcher handlers or the full 43-word outer parent. Callback and lower
heap/removal providers remain bounded; complete heap/free/gameplay
behavior is not claimed.

**21 independent GNU alias/rebase links**, **64 rebase phases**,
**80 target fault prefixes**, **51 guard controls**, **17 raw corruption
controls** and **eleven strict-image negatives** pass. The qualified pair
must share its adjusted-HI16 page; reject the split at 80347FFC and bad
spacing. Guest aliases and fault prefixes do not establish portable C
invalid-memory behavior or hardware fault semantics.

The initial fixture failures were corrected, not accepted as evidence:
publish the bounded factory's v0 result, independently GNU-link alias
layouts instead of moving only data, and implement the connected removal
helper's signed-byte load in the local oracle.

The qualified source and generated 17-row suffix are installed
byte-for-byte, retaining all **3,179,643 old guard-prefix bytes** and
**633 carriage returns**. Production passes in **490.639s**:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The `-o` flag reuses unaffected objects because the complete old manifest
prefix is unchanged and only the rebuilt owner uses the appended rows.
The changed owner, complete link and progress generation actually run.
No Makefile/profile, shared-header, original-assembly, ROM or conversion-row
changes. Preserve **20 raw/padded owner neighbors**, pools and metadata.

The complete **10,188-byte production owner object** equals the qualified
padded object, SHA-256:
`2d30d2ad8af05b3dbb0fbbf76a88ae9b54ba67b9494a41d764fbdc1a7020700a`.
Raw unrelocated 42-word C SHA-256:
`7b497a19b145f7227726bce9a461154ae646dd89bc1c3c7aaa12b3e89750cf01`.

The independent first link and production image agree on every byte:
**209 changed bytes = 134 instruction bytes + 75 metadata bytes**,
extent **12 -> 164 bytes**, **zero exclusions**. Two bounded GNU
symbol/name groups rotate: `(D_800D98A0, D_80088860)` and
`(D_800D989C, func_10004FE0, func_1508BF14)`. Predict those exact
permutations from the pinned predecessor, checking the contiguous name/
symbol groups and unchanged named definitions, not by copying new metadata.
ELF SHA-256:
`ac46421b428bcc3f4363add6ae33949764979d9d5e82ada2426da8976811e912`.

Preserve all **6,055 other linked bodies**, all **6,056 addresses** and
**189,088 protected Game-data bytes / 720 owners**. Protected data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After production/audit, the literal standard Make matcher recipe passes:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh results: **3,713/5,505 total (67.45%)**, **3,040/4,832 Game (62.91%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,792 different**.
The 75% threshold is **4,129**, leaving **416**. The fresh ELF-pinned
queue has **1,659 placeholders, 124 semantic/other bodies and nine unlocated
entries**. These source-shape screens are not C or ABI qualification.
README changes are only its two aggregate rows; the roadmap checks off
this routine and leaves the wider goal open.

All **1,508** pre-existing older-mirror dirty statuses/hashes and its
`ddbdd16` HEAD are preserved. Only the two absent task files are added,
bringing it to **1,510**; copies are byte-identical and all four files are
AST-valid. Never commit/reset/stash/clean that mirror. Active tools are
committed first as **8310f77**; the consumer source/guards/docs/pin checkpoint
follows. No push. Host source, real saves/configuration and frozen Release
remain untouched. Routine task: zero Claude calls.

## Next Function

Next is `func_150E6E34` in
[generated_113D60.c](../../conker/src/game/generated_113D60.c):
VA **150E6E34..150E6ED8**, ROM **1142E4..114388**,
**41 words/frame32**, a zero-return placeholder with **38 differences**.
Screened semantics are two independent random samples, range-pointer
selection/capture and ordered XYZ interpolation stores. Audit the real
callback ABI before choosing the C signature.

The complete aligned ROM scan finds no direct JAL and one literal at
**22D4E0**, VA **80088A20**, slot **0** of `D_80088A20` in
[22D4E0.rodata.s](../../conker/asm/data/22D4E0.rodata.s).
Retail SHA-256:
`534cb5aa04b5b6d9d2209e25cbaebffe359933276a2416d8a6cbaf353526edba`.
These are read-only screen results, not a new draft, installation or
matching credit. Keep the 862-word `func_1508CAD8` stub queued.

Receipts: ignored `conker/build/game-color-table-reset/qualified/`.
Retain the pre-commit graph and rebuild-log offset; after committing,
wait for both owned workers and audit the commit stamp and retention of
old/excluded nodes. The 75% goal remains active.
