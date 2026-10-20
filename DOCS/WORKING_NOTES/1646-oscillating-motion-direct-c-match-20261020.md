# Oscillating Motion Direct C Match

Date: 2026-10-20. Consumer predecessor: `d07df1e7`; tools predecessor:
`da87893`. Qualified tools committed first as `f81540b`.
The **75% total C-matching objective remains active**.

## Target And Layout

`func_151B8B40` in
[generated_1E5FF0.c](../../conker/src/game/generated_1E5FF0.c):
VA **151B8B40..151B8BE0**, ROM **1E5FF0..1E6090**,
**40 words / 160 bytes**, **24-byte frame**, six relocations.
The first complete semantic probe matches directly under normal IDO O2/g3,
with no diagnostics, guards, profile changes or scheduling workarounds.

Use a private `OscillatingMotionRecord` prefix. Keep the address-based
function name and a purpose comment; do not invent a more specific visual
effect or actor identity without additional evidence.

| Offset | Field |
| --- | --- |
| 0x00..0x1F | Opaque header |
| 0x20 | First planar coordinate |
| 0x24..0x27 | Reserved |
| 0x28 | Second planar coordinate |
| 0x2C..0x3B | Reserved |
| 0x3C | Sine-driven output |
| 0x40..0x43 | Reserved |
| 0x44 | Phase in radians |
| 0x48 | Oscillation base |
| 0x4C | Phase rate |
| 0x50 | First coordinate velocity |
| 0x54..0x57 | Reserved |
| 0x58 | Second coordinate velocity |
| 0x5C | Oscillation amplitude |

Evaluate sine at the incoming phase; load amplitude/base after its return.
Store the oscillation, advance phase using the live timestep, normalize the
advanced phase through `func_15144B68`, then integrate the two coordinates
in order. Preserve each separate float32 multiplication/addition, the
post-helper timestep reload, the second timestep reload after the first
coordinate store, and the exact integer return of one.

## Actual Dispatch And Math

The complete pristine-function JAL scan finds **no direct call**. The only
aligned literal pointer in ROM is at **22E3A8**, VA **800898E8**, in the
unchanged `22E370.rodata.s` owner. It is **slot 14** of the table based at
**800898B0**, not a timer table or a new synthetic direct caller.

`func_151321D0` selects the slot using the unsigned record byte at **0x71**.
The qualification window is its actual **13 words** at
**15132244..15132278**, ROM **15F6F4..15F728**. It includes slot-zero bypass,
the indirect call, the branch-delay reload and the zero-result gate. Stop
on the actual **15132278** join. The full 119-word parent is not executed or claimed
by this window. The actual compiled zero-return predecessor sets the wrong
gate and is rejected by an effective negative control.

Connect the original **104-word sinf** at **15047D60**, ROM **75210**,
and **24-word angle normalizer** at **15144B68**, ROM **172018**.
The normalizer retains its strict greater-than upper bound and repeated
single-precision subtraction/addition; do not substitute fmod or clamp.
Finite bounded angles and NaN are qualification inputs. Completion for
infinite or extremely large wrapping inputs and MIPS FCSR/hardware parity
are not claimed.

## Focused Qualification

[The module](../../tools/experiments/game_oscillating_motion.py) freezes the
source, original owner, math sources/assembly, real dispatcher/table owner,
shared headers, ROM, ELF, layout symbols, complete guard manifest, Makefile
and progress CSV. [The tests](../../tools/tests/test_game_oscillating_motion.py)
compare original retail instructions, fresh C, the independent memory
reference and actual helper execution as appropriate.

Model cases vary signed zeros, large and subnormal values, NaNs/infinities
in data fields, helper mutations and timestep aliases with seven record
fields. Aliases are guest-only stress evidence, not portable C object-layout
claims. Native32 uses an actual typed record with fences and bytewise
representation initialization/comparison, separate float32 operations,
scripted math providers and the real callback pointer type.

Required gates before installation: all focused tests in both tools copies,
raw/padded owner and actual Make equivalence, independent GNU relocation
rebases, effective semantic/strict-image negatives, untouched opaque bytes,
all target access-fault prefixes and the actual slot-14 dispatch window.
Guest fault-prefix checks do not establish portable C invalid-memory behavior.

## Pre-Install Results

Both copies pass all eight tests with zero failures/errors/skips: primary
**228.837s**, older mirror **248.602s**. Both shared tools checks pass.
The suite has **443 cases / 886 modeled phases**, including **112 guest-only
timestep-alias phases**, and **366 native32 cases** at O0/O2/O3 with trap
UBSan and eleven effective compiled semantic negatives.

The real math chain passes **72 phases**, visiting **124/128 helper words**,
including all 24 normalizer words; full sine-path/FCSR coverage is not
claimed. The dispatch window passes **16 phases / 32 fired joins**,
including slot-zero bypass and the actual old-stub gate negative. Nine
independent GNU links pass **72 rebase phases**, including signed-low carry.
All **184 target access-fault prefixes** and seven strict-image negatives pass.

Preserve three raw/padded owner neighbors and all pools/bindings. All three
productive actual Make commands reproduce the qualified object and normal
O2/g3 profile. The existing duplicate generated_12D630 recipe warning is
inherited; isolated and owner compiler diagnostics are empty.

Raw body SHA-256:
`d0de507f5f03ba05813e8555cf48941296a28ffa3a4c560d69738377f28bb21b`.
The independent first link exactly matches the declared body/extent change:
**132 changed bytes = 131 code bytes + one symbol-size byte**, extent
**12 -> 160**, **zero metadata exclusions**. ELF SHA-256:
`da4591cc23d4cbd8c1bdc20ce7ee2035e6f60dd87133e32222e0d695186c9ec4`.

Two preflight fixture corrections preserve the unchanged C candidate:
keep relocated targets separate from the oracle's internal symbol map,
and apply the parent's frame after selecting a supported entry-stack phase.

## Installed Checkpoint

Install the independently qualified owner source byte-for-byte. The normal
production build passes in **122.466s**:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The complete guard manifest is pinned and unchanged, so the documented
`-o` reuse of unaffected objects is valid. The changed owner and full link
still run. The duplicate generated_12D630 Make warning is inherited; no
compiler diagnostics are emitted. No Makefile, compiler profile, dependency
timestamp, shared header, original assembly, ROM or guard manifest changes.

Production reproduces the independent image exactly. All **6,055 other
bodies**, all **6,056 function addresses**, and **189,088 protected Game-data
bytes / 720 owners** remain fixed. Protected data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All four focused suites pass eight tests, zero failures/errors/skips:

| Run | Seconds |
| --- | --- |
| Primary, pre-install | 228.837 |
| Older mirror, pre-install | 248.602 |
| Primary, installed | 125.308 |
| Older mirror, installed | 145.013 |

Run the two copies sequentially because scratch outputs are shared. After
the fresh build/audit, invoke the literal standard Make matcher recipe from
`conker/`, avoiding a redundant dependency scan:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh matching: **3,711/5,505 total (67.41%)**, **3,038/4,832 Game (62.87%)**,
**492/492 Init**, **181/181 Debugger**, **zero drift / 1,794 different**.
The current 75% threshold is **4,129**, leaving **418**. The ELF-pinned queue
has **1,660 placeholders, 125 semantic/other bodies and nine unlocated
entries**; source-shape screens are not qualification. README edits are
only its two aggregate rows; the roadmap checks off this completed target.

The older mirror remains at `ddbdd16`. Preserve all **1,504 pre-existing
dirty statuses/hashes** and add only the two task files, bringing it to
**1,506**. Both task copies are byte-identical and all four files AST-valid.
Never commit/reset/stash/clean that mirror. Active tools are committed as
`f81540b`; the consumer source/docs/pin checkpoint follows. No push. Host
source, saves/configuration and frozen Release stay untouched. Zero Claude calls.

## Next Function

Next is the existing semantic `func_15002754` in `game_2DF70.c`:
VA **15002754..150027F8**, ROM **2FC04..2FCA8**, **41 words/frame24**,
currently **38 differences**. Recover unsigned wrapping alignment and
12/8/4-byte partition arithmetic, exact post-alignment count/index reads,
the `func_1510F800` call and the post-call count clear. Do not replace this
semantic body with a placeholder. No new draft, recovery or matching credit
is claimed. Keep `func_1508CAD8` queued.

Receipts: ignored `conker/build/game-oscillating-motion/qualified/`.
Before committing, retain the old graph and rebuild-log offset; afterward,
wait for both owned workers and audit the commit stamp and retention of old
and excluded nodes. The complete 75% goal stays active.
