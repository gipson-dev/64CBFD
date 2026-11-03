# 2018 - Camera mode dispatcher matched as guarded C

Verified 2026-11-02. Production is **4,088/5,511 (74.18%)**; Game is
**3,415/4,838 (70.59%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,423 functions remain different. The active 80% target is
**4,409/5,511**, requiring **321 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_151283B8` replaces its zero-return placeholder in
`conker/src/game_14FF90.c`. It is the sparse camera-mode dispatcher at
`0x151283B8`, ROM `0x155868..0x155974`, owned by `game_14FF90`. Its recovered
interface is `void (struct108 *camera)` and the selected mode is the word at
camera offset `0x2C`.

The semantic switch preserves the retail source order and routes modes `0x80`,
`0x40`, `1`, `8`, `2`, `0x400`, `0x800`, `0x100` and `0x800000` to their
respective camera update helpers. Mode `0x2000` and the default path return
without a call. Mode 8 alone supplies a second argument, and that argument is
zero. The two modes that share `func_15122980` remain separate cases so the C
tracks the retail decision tree rather than concealing it behind a synthetic
condition.

Four aligned retail `JAL` sites target this dispatcher at ROM offsets
`0x150408`, `0x15042C`, `0x150434` and `0x156810`. The recovered `void`
interface reflects that every caller ignores the result.

## Guarded compiler closure

Natural IDO C emits the correct **67 words/frame24** and all nine original
`R_MIPS_26` helper bindings. It differs from retail at only offset `0x0A8`:
IDO chooses `move a1,zero` (`0x00002825`) while retail uses
`addiu a1,zero,0` (`0x24050000`) for mode 8's second argument. One checked,
relocation-free row records that independent instruction-selection difference.
Changing its expected candidate word makes the padder fail closed.

The guarded owner matches all 67 retail words. All 44 owner neighbors and
normalized pools remain fixed. A literal full-image prediction changes only
`func_151283B8`, expands its symbol extent from the old 16-byte placeholder to
268 bytes, preserves all 6,051 function addresses and uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 67-word candidate payload | `77549146a4d8ecae3430bed0d9a184a571fffcf850a1245c17de7decf8714fcb` |
| Retail/guarded 67-word payload | `89c4bd3301bca8b8117089b8d330743444933b89c339b91d3a96473673b83fbf` |
| Qualified/production owner | `a1b234d08243ed5e4f8e64918dfa3980c84251650463dadabb78b89945680637` |
| Predecessor linked ELF | `461d741a53e52ce70ec2163e1a71eff75c0ac788b254a3a8e23f15f5e4ddaa8c` |
| Qualified/production linked ELF | `7ef404e2d38e1367e12689ad0cce2caac0b47c3f913638506eeb840230db08c6` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `d85664dba787bdf08e001177b60099083a6c065e4c7d7253a22aa2a33f943aed` |

## Semantic and production qualification

The guest oracle executes 31 selected and boundary mode words at two incoming
stack phases against both the retail and natural instruction streams: 124
executions total. It verifies the selected helper, the mode-8 zero argument,
stack restoration and equivalence of all observable state. Every one of the
67 words is visited. Native 32-bit O0/O2/O3 profiles pass, while four effective
controls covering the zero argument, two routes and a missing route fail.

The permanent five-test suite also checks the stale guard, all four retail
callers, 44 unchanged owner neighbors, normalized pools, literal full-image
prediction, protected data and installed source/object/image coherence. All
five tests pass in 25.379 seconds. Nineteen shared layout, progress and padder
tests pass independently.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the generated, converted and libultra corpus,
linked `conker.us.elf` and produced `conker.us.bin`; it stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function.

The qualification module and tests were committed first in the tools
submodule as `8c20092`; installed-state verification was tightened in
`14312a6`. Retained stage:
`conker/build/game-camera-mode-dispatch-151283B8-guard-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact rows.
No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,182 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from a fresh ordinary Game ranking. Keep handwritten/custom-entry
`func_150A76F0`, `func_150A613C`, `func_151F8870` and stack-resume
`func_150AE280` outside ordinary C screens. `func_15115F68` and
`func_151AE2BC` remain private and uncredited until their compiler and ABI
boundaries are closed. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount and documentation gates before credit.
