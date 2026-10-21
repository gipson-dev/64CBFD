# Two-Range Position Sampler

Started: 2026-10-20. Checkpoint verified: 2026-10-21.
Consumer predecessor `7e04e480`; active tools predecessor `8310f77`.
The 75% total C-matching goal remains active.

## Target And ABI

`func_150E6E34` in
[generated_113D60.c](../../conker/src/game/generated_113D60.c):
VA **150E6E34..150E6ED8**, ROM **1142E4..114388**,
**41 words / 164 bytes**, **32-byte frame**. The predecessor is a
zero-return placeholder with 38 retail word differences.

The aligned pristine ROM scan finds no direct JAL and one literal,
ROM **22D4E0**, VA **80088A20**, slot **0** of `D_80088A20` in
[22D4E0.rodata.s](../../conker/asm/data/22D4E0.rodata.s).
The actual caller `func_150E68B0` reads a signed descriptor byte at +4,
bypasses -1, selects the callback and passes its three-float local at
parent SP+0x8C. It does not consume the return. Recover
`void func_150E6E34(f32 *output)`, keeping the address-based name and
a purpose comment. Qualify the **17-word window 150E6988..150E69CC**,
not the complete large parent or other callback slots.

## Semantics

Call `func_150ADA68()` first, then read `D_800A130C`
(retail bits **3F102F57**) for a strict less-than comparison. Capture
`D_80088A3C` on true and `D_80088A40` otherwise. The pointer cells
reference the six-float ranges at **800A11D0** and **800A11E8**.
Take a second independent sample and share it across XYZ, computing
base + (end - base) * fraction with separate float32 operations.
Keep sequential output stores interleaved with later range reads.

The selected range pointer is captured before the second RNG call,
while its fields are read after that call. Do not reuse the first sample,
clamp extrapolation samples, snapshot fields early, reload the selected
pointer after the second call, invent NULL handling or return an
incidental cursor/register value. Each six-float range is an XYZ segment,
not a uniformly sampled box.

The unchanged handwritten float RNG is **25 words**, VA
**150ADA68..150ADACC**, ROM **DAF18..DAF7C**. Preserve the full 64-bit
`D_800885B0` seed and exact scale bits **37800080**, not an approximate
reciprocal. The original 26-word fixture accidentally included the next
seed-setter entry's first word; that failure was rejected, its extent
corrected and the complete formal suites rerun. No RNG conversion,
FCSR/hardware or gameplay acceptance is claimed.

## Direct C And Owner Qualification

The base-first expressions emit all **41 words/frame32/eight bindings**
directly from normal O2/g3. No word guards or compiler-profile changes.
The delta-first probe has the same extent/frame but three commutative
float-add operand differences; it is not selected. Raw unrelocated SHA-256:
`5a319d0e37a2ab1f612e09b28dbaeb1902b768816c1b8c2c20529cda78a484da`.

The native snapshot freezes **27** source/header/assembly/data/layout/
image/build inputs and separately pins the old padded owner object:
`1a37dd1e85195d1159cadda6f18551a5e098b412df22f8e9186441be11a71960`.
The predecessor ELF SHA-256 is
`ac46421b428bcc3f4363add6ae33949764979d9d5e82ada2426da8976811e912`.

Whole-owner compilation preserves **28 raw/padded neighbors**, all pools,
addresses and unrelated symbol metadata. The target symbol grows from
**12 to 164 bytes**. Owner diagnostics are unchanged and the isolated
compile has none. Independent GNU assembly of the original has the same
payload and all eight relocations. Actual Make runs **five productive
commands**, including GLOBAL_ASM processing, with the existing
`D_800A1350` rodata anchor. Keep the three retained assembly functions
`func_150E7FEC`, `func_150E83AC` and `func_150E8470`.

## Tests And Boundaries

Each copy passes all eight tests before installation, with zero errors,
failures or skips. Each then freshly passes the two install-sensitive
checks, 01 and 08, in a byte-sealed Linux-local copy of each checkout,
including a fresh isolated compile, full installed audit and all 27 frozen
inputs. These are fresh sealed-copy runs, not fresh Windows-mount runs.
The live consumer is tied to them by full input/object/image byte identity. Reuse the six unchanged model/native/
caller/RNG/rebase/fault checks per copy only under strict source,
raw/padded object, helper, tools and whole-image identity. Do not call
them fresh installed reruns. Copies run sequentially:

| Run | Fresh Tests | Runner Seconds |
| --- | ---: | ---: |
| Primary, pre-install | 8 | 1108.114 |
| Older mirror, pre-install | 8 | 1094.734 |
| Primary, installed (sealed copy) | 2 | 1.845 |
| Older mirror, installed (sealed copy) | 2 | 1.781 |

Runner times exclude module-loading time. Both shared tools checks pass.
The inherited duplicate generated_12D630 Make-recipe warning is not a
new target warning; do not claim a globally warning-free build.

Each complete suite covers **376 cases / 752 modeled phases**,
including **16 guest-only argument-home phases**, and all **41 target
words**. Typed/fenced native32 fixtures cover **368 cases** at O0/O2/O3
with trap UBSan and twelve effective compiled semantic negatives.
Quiet-NaN selection is covered without asserting arithmetic NaN/FCSR
payload behavior. Native pointer identities use real typed arrays;
guest-only stack-home redirects are not portable C claims.

The real **17-word caller window** passes **40 phases / 80 fired joins**,
including table slot 0, the signed -1 bypass and restored descriptor v0.
The complete large parent and other callback slots are not claimed.
All **25 original RNG words** execute over **88 phases**, checking both
range choices, full seed64 and the exact scale. **Six independent GNU
links / 42 rebase phases** cover all eight bindings and signed-low carries.
**68 fired target fault prefixes** and **seven strict-image negatives**
pass. Fault-prefix agreement qualifies guest instruction ordering, not
portable C invalid-memory behavior or hardware fault semantics.

## Installed Checkpoint

Only the qualified source body and two owner-local declarations are
installed. The entire guard manifest is byte-identical, SHA-256:
`704d9da0fe81ea2498078c8b5b2f53994ba05cf8e9e88af2ba0cb5dfd38ce71c`.
No Makefile, shared-header, original-assembly, ROM or conversion-row changes.

The same-source Linux-local actual Make completes in **0.83
seconds**, excluding export/setup. This is not the Windows-mounted build's
elapsed time:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The first production attempt was deliberately stopped: old guard-manifest
timestamps caused unrelated rebuilds even though its bytes were unchanged.
Four unrelated padded objects completed; their unchanged linked effects
are checked by the strict whole-image audit. Four later compiler jobs were
stopped only within the owned Make tree; partial temporaries are not linked.
The retry marks the byte-identical manifest old with `-o`. It produces the
exact live owner object but remains slow while regenerating the linker
script. It is superseded only after the sealed-copy build and checks pass,
all live static inputs are byte-verified and only its owned process tree
is retired. No Makefile/profile or source changes outside the target owner.

## Sealed Build Copy

Native export captures **15,716 files / 167,536,302 uncompressed bytes**,
then **48 additional non-linked Make prerequisite objects / 376,848 bytes**.
The source, SDK, both tools copies, compiler files and all unchanged linker
objects keep their exact bytes and timestamps. The target object is omitted
for a genuine fresh compile. The initial export takes **1,162.484s**; its
**47,677,348-byte** archive SHA-256 is:
`fbd7159f72974051d62945da7f0022902e05f7852abfee03e2bc08515629ae7c`.
Do not present the 0.83s Make time as total setup time.

The first local attempt is rejected for missing unlinked prerequisite
objects/directories, not accepted as C qualification. Adding the 48 sealed
objects completes the same Make recipe and fresh installed checks. All
**1,453 unchanged linker-input objects** and the extra objects remain
byte-identical; the selected owner and complete ELF reproduce the known
qualified hashes. No compiler or SDK replacements or relaxed gates.

The native live-byte check initially finds **15,763 identical static files**
and one generated-output difference: `build/conker.ld` is exactly the owned
Make job's CPP output, before `patch_generated_slice_ld.py` finishes. Its
SHA-256 is `3656193361e0c7964e1914bf85f161035ea965c2b83d89b37c03098ccb9768d4`.
The qualified patched script reproduces the pinned predecessor's
`6479ca7cef48dc77d746c16afcc244de6bfb80c6789ba79a03d6f110e42a98d5`.
This is an owned intermediate output, not an unexplained source difference.

After retiring only the owned producer, adopt only verified generated
artifacts and receipts. The original live Make's owner object already has
the exact qualified hash. Recheck all 27 live inputs and rerun the native
content audit: **all 15,764 copied paths now match, zero mismatches**.
The installed audit is reused for the live consumer only under complete
source/header/tool/compiler/object/image identity. The literal standard
matcher then runs against the actual live consumer ELF, not just the copy.

The complete **19,408-byte production owner object** equals the qualified
padded object, SHA-256:
`0baa4f36b471f8f41d5a42389b7b1afbfb9305df9d736aa5910acb822a6404dc`.

The independent first image and production image agree on every byte:
**123 changed bytes = 122 instruction bytes + one symbol-size byte**,
**zero exclusions**, with no symbol/name permutation. ELF SHA-256:
`5920d297b635d80fe5184b6890ca10a1adf32f0e516dfe4a4971e6839923d8a1`.
Preserve all **6,055 other linked bodies**, all **6,056 addresses** and
**189,088 protected Game-data bytes / 720 owners**. Data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

After production and audit, the literal standard Make matcher recipe passes:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh results: **3,714/5,505 total (67.47%)**, **3,041/4,832 Game (62.93%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,791 different**.
The 75% threshold is **4,129**, leaving **415**. The fresh ELF-pinned queue
contains **1,658 placeholders, 124 semantic/other bodies and nine unlocated
entries**. These source-shape screens are not C or ABI qualification.
README changes are aggregate progress rows and the verification date only;
the detailed update belongs here.

All **1,510** pre-existing older-mirror dirty statuses/hashes and its
`ddbdd16` HEAD are preserved. Add only the two absent task files, bringing
it to **1,512**; copies are byte-identical and all four files AST-valid.
Never commit/reset/stash/clean that mirror. Active tools are committed first
as **62ce8ef**; the consumer source/docs/pin checkpoint follows.
No push. Host source, real saves/configuration and frozen Release remain
untouched. Routine task: zero Claude calls.

## Next Function

Next is `func_150A02D0` in
[generated_CD5A0.c](../../conker/src/game/generated_CD5A0.c):
VA **150A02D0..150A0374**, ROM **CD780..CD824**,
**41 words/frame0**, still a zero-return placeholder.

Read-only assembly shows commands 0/1 set/clear bit 0x40 in a 12-byte
indexed record; command 2 copies payload +8 into record +4. Valid commands
return one, all others return zero. The aligned ROM scan finds no direct
JAL and one literal at **22CFBC**, VA **800884FC**, slot **10** of
`D_800884D4` in
[22BEF0.rodata.s](../../conker/asm/data/22BEF0.rodata.s).
Retail SHA-256:
`dd29dea54e9d70d069d2267998d4f3c96628ee68db88663b2b907f860202516c`.

Inspect both actual dispatch paths before choosing the C argument types:
the call at **1509C100** in `func_1509BFB0`, with global payload
`D_800D2F60`, and the **150AE12C..150AE194** script-dispatch window,
which keeps its return link in s7 and passes the original descriptor.
These static observations are not executed ABI qualification, a new
draft, installation or matching credit. Keep the 862-word
`func_1508CAD8` stub queued.

Receipts: ignored `conker/build/game-two-range-position/qualified/`.
The qualified Linux-local workspace is retained at
`/tmp/cbfd-two-range-sealed-my0624sa/64CBFD`, with its sibling tools copy.
Reuse it for the next function only after syncing and verifying the needed
delta; never blindly reuse old source, tool or input fingerprints. The
export archives, manifests, adoption/retirement proof and target-specific
orchestration scripts remain in the ignored receipt directory. The normal
committed qualification helpers still work without this optional copy.
Keep all live-input, actual-Make, object/image and preservation gates intact.

Retain the pre-commit graph and rebuild-log offset. After committing, wait
for both owned workers and audit the commit stamp plus retention of
old/excluded nodes. The 75% goal remains active.
