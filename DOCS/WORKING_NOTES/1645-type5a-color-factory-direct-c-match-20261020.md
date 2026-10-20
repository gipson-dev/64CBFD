# Type-0x5A Color Factory Direct C Match

Date: 2026-10-20. Consumer predecessor: `3fad1811`; tools predecessor:
`41229dd`. Qualified tools committed first as `da87893`; the consumer
source/docs/pin checkpoint follows. The **75% total C-matching objective
remains active**, not complete. No push.

## Recovered Routine

Target `func_151A4FD0` in
[generated_1D0840.c](../../conker/src/game/generated_1D0840.c).
VA **151A4FD0..151A5070**, ROM **1D2480..1D2520**,
**40 words / 160 bytes**, **32-byte frame**, one call binding,
normal **IDO O2/g3**. Preserve the address-based name and add a purpose comment.

Use a private 0x20-byte `Type5AColorRecord` prefix:

| Offset | Field |
| --- | --- |
| 0x00..0x0F | Opaque allocator/linkage header |
| 0x10 | Complete 32-bit value, not assumed to be an owner pointer |
| 0x14 | Selector |
| 0x15..0x17 | Red, green and blue bytes |
| 0x18 | State, initialized to zero |
| 0x19 | Callback byte |
| 0x1A | View byte |
| 0x1B..0x1F | Reserved bytes, preserved |
| 0x20 onward | Optional trailing payload, not initialized here |

The existing renderer `func_151A5170` packs the three RGB bytes into its
color command and uses the view byte for its per-view data offset. Keep its
existing GLOBAL_ASM body unchanged. Do not infer additional effect semantics.

Call `func_15167A68(0x5A, 0, size, 0, 0xFF, 1)`, where `size` is the
**unsigned 32-bit wrapping sum** of the eighth input and 0x20. Preserve the
word at the existing signed-word API boundary using the pinned 32-bit
compilers; do not assume defined signed C overflow or clamp the request.
Return NULL on failure. Otherwise initialize only the documented fields
and return the allocation's original pointer.

The first, third, fourth, fifth and sixth inputs retain word-width incoming
homes despite their byte-sized output fields. The second input is a word:
the large caller supplies an actual wrapping SUBU address difference.
The seventh input is an unsigned byte read from SP+0x3B.

## Direct Compiler Fit

The first complete C probe already had the correct extent, frame, binding,
register allocation and all but three independent scheduling words.
Placing the C callback assignment before the state clear recovers the exact
retail load/store schedule. The compiler emits the zero store between the
callback load and store. No instruction normalization is needed.

A state-clear-last variant, a word-wide callback parameter, and a swapped
color-store order do not match. Select the direct ANSI C form, not a new
profile or physical-register workaround. **No new guards**; the entire
existing manifest remains byte-identical, SHA-256:
`016466c90030bca35c3b27892833265d62314b8b8156145fd9c2eae7c3e37623`.

## Actual Callers And Helpers

The pristine complete-function JAL scan finds all three direct sites, with
no aligned literal target pointer elsewhere in ROM:

- `func_1502460C` at **15025AF0**. Execute its actual **14-word** window
  **15025AC8..15025B00**, ROM **52F78..52FB0**, through the child and the
  branch-delay return-one update, stopping on the real **150265B4** join.
  This is not execution of the complete **2,032-word** parent.
- Execute the complete **41-word func_150B6C90**, including optional old
  record removal, current-view reload, pointer publication and all clear-loop
  stores. Removal remains a bounded provider.
- Execute the complete **29-word func_151CCE94**, including its enable-byte
  gate, actor view-byte load, NULL path and four-byte trailing actor-pointer
  copy. The unchanged memcpy remains a bounded four-byte provider.

The model preflight passes **64 full-caller phases**, plus **32 large-window
phases / 64 fired join boundaries**. In this window, the parent replaces the
factory result with one in its branch delay slot. Do not generalize this
bounded result to unexecuted parts of the full parent.

Execute the complete **28-word original allocation wrapper** and **20-word
original list initializer** in **64 phases**. Check all heap argument words,
NULL/success paths, empty/nonempty list heads, next/previous links, header
bytes and the returned pointer. All 48 helper words execute. The unchanged
**258-word lower heap routine** remains a bounded provider; these tests do
not establish allocation success or safe heap sizes for every wrapped request.

## Qualification

[The module](../../tools/experiments/game_type5a_factory.py) freezes 21
source/header/assembly/helper/caller/image/build inputs.
[The focused suite](../../tools/tests/test_game_type5a_factory.py) covers
672 cases: 640 native-valid cases and 32 guest-only stack-alias cases.
Across both stack phases this gives **1,344 modeled phases**, including
**64 guest-only alias phases**. All 40 target words execute.

The native fixture uses a real typed record object with a trailing byte array
and fences, not a differently typed access through a declared byte buffer.
Native32 checks at O0/O2/O3 use trap UBSan, validate every field offset, all
unwritten bytes, exact NULL/original-pointer returns and all six call words.
The 12 compiled semantic negatives reject wrong sizes/flags/types, truncated
word values, wrong channels/fields/returns and reserved-byte clears.

Guest alias tests model retail's interleaved argument-home reads and stores;
they are not portable C stack-object alias claims. A failed allocation never
reloads the removed argument-home mappings. A separately compiled word-wide
callback parameter fails the physical byte-match gate, not a fabricated
native-semantic claim. The actual old compiled zero-return stub is rejected.
Three GNU call rebases and seven strict-image negatives are part of the suite.

Preserve **22 other raw/padded owner functions**, bindings, pools and inherited
diagnostics. All five productive actual Make commands pass, including the
existing GLOBAL_ASM preprocessing/postprocessing path; their raw and padded
code/metadata equal the independently qualified objects.

The independent first link exactly matches the closed body/size prediction:
**116 changed bytes = 115 code bytes + one symbol-size byte**, target extent
**12 -> 160**, **zero metadata exclusions**. ELF SHA-256:
`93e2e0785b38b376eb6f9715ced30a2ca7d723403fcdda632f90b06818936832`.

All four formal suites pass **eight tests**, with zero failures/errors/skips:

| Run | Seconds |
| --- | --- |
| Primary, pre-install | 22.899 |
| Older mirror, pre-install | 34.898 |
| Primary, installed | 23.019 |
| Older mirror, installed | 27.950 |

Both shared tools checks also pass. Run the copies sequentially because they
share the qualification scratch paths. Hardware/MMU, portable invalid-memory
behavior, full large-parent/heap internals, renderer/gameplay and host
acceptance remain separate. Routine task: zero Claude calls.

The older mirror stays at `ddbdd16`. Preserve all **1,502 pre-existing dirty
statuses/hashes**, add only the two absent task files, verify both copies
byte-identical and all four Python files AST-valid. It now has **1,504**
dirty paths. Never commit/reset/stash/clean that independently dirty mirror.

## Installed Checkpoint

Install only the independently qualified owner source and rebuild with:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The pinned complete manifest is unchanged, so reuse unaffected objects using
the documented `-o` option. The changed owner and complete link still run.
Production passes in **74.545s**, reproducing the independent first link
byte-for-byte. The inherited duplicate-recipe warning for
`generated_12D630.c.o` remains; no new compiler warning is emitted here.
No Makefile, compiler profile, dependency timestamp, original assembly,
shared header, ROM or guard manifest is changed.

The installed audit keeps all **6,055 other bodies** and **6,056 addresses**
fixed. All **189,088 protected Game-data bytes / 720 owners** remain exact,
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
After the fresh build and installed audit, invoke the literal standard
Make matcher recipe from `conker/`, avoiding a redundant dependency scan:

```sh
python3 ../tools/match_progress.py progress.csv build/conker.us.elf conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

Fresh counters are **3,710/5,505 total (67.39%)**, **3,037/4,832 Game
(62.85%)**, **492/492 Init** and **181/181 Debugger**, zero drift and
**1,795 different**. The 75% threshold is still **4,129**, leaving **419**.
The ELF-pinned queue contains 1,661 placeholders, 125 semantic/other bodies
and nine unlocated entries; source shapes are screens, not qualification.
README changes are limited to its two aggregate rows. The focused tools and
consumer changes are committed separately; preserve the dirty older mirror.
Host source, runtime, saves/config and frozen Release remain untouched.

## Next Function

`func_151B8B40` in `generated_1E5FF0.c` is the next queued placeholder:
VA **151B8B40..151B8BE0**, ROM **1E5FF0..1E6090**, **40 words/frame24**.
Its original body computes a sine-based field, advances/wraps the angle,
reloads the global timestep and integrates X/Z in the original order before
returning one. Qualify the real record layout, call/float ABI, aliases and
late reads before installing. No C draft, installation or matching credit
for this next target is claimed. Keep the 862-word `func_1508CAD8` stub queued.

Receipts live under ignored `conker/build/game-type5a-factory/qualified/`.
Before the consumer commit, retain the old graph and rebuild-log offset.
After the commit, wait for both owned graph workers and verify the commit
stamp plus retention of old/excluded nodes. The 75% goal stays active.
