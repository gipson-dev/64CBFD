# 2651 - Unmatched layout and pair lookup recovery audit

Date: 2026-11-23. The 85% total matching goal remains active.

This checkpoint banks two **uncredited C candidates**, their source packet
and reproducible screens. **Neither is installed. No new match is counted.**
Production stays **4,631 / 5,528 (83.77%) total**, **3,958 / 4,855 (81.52%)
Game**, zero drift, 897 different, **68 more matches to 85%**. Init remains
492/492 and Debugger 181/181. Root README's existing aggregate rows stay correct
and are unchanged.

| Candidate | Raw C words/frame | Retail words/frame | Raw word differences | Unchanged raw neighbors |
| --- | ---: | ---: | ---: | ---: |
| `func_15195AA8` | 147 / 96 | 150 / 96 | 111 | 68 |
| `func_15022024` | 87 / 8 | 91 / 16 | 90 | 56 |

All before/after owner pools and diagnostic sets remain fixed. Expected raw
instruction and relocation fingerprints are pinned, so the screens do not
accept a different body merely because its word/difference counts agree.

## Reproducible source packet and focused tests

The four task files are
`tools/experiments/game_unmatched_recovery_20261123.py`, its adjacent JSON
packet, `tools/tests/game_unmatched_pair_lookup_20261123_guest.py` and
`tools/tests/test_game_unmatched_recovery_20261123.py`. The packet contains
the selected C bodies/declarations, original source/ASM fingerprints, ROM
spans and exact candidate payload/binding fingerprints.

From the decomp root under WSL:

```sh
python3 -m unittest tools.tests.test_game_unmatched_recovery_20261123 -v
```

These are **private recovery screens, not adoption gates**. Their reports
explicitly keep `source_installed=false` and `matching_credit=0`. The scripts
write only `conker/build/game-unmatched-recovery-20261123/`; they refuse changed
production source, image, guard or ROM inputs. No production C, header, layout,
profile, object, image or conversion row is changed.

| Tools setup | Elapsed | Tests |
| --- | ---: | --- |
| primary | 15.545s | 3 fresh / 0 reused |
| sibling | 17.901s | 3 fresh / 0 reused |

`make tools-check` also passes. The second setup is a disposable overlay:
1,523 files comprising 349 identical sibling files, 1,169 explicit primary
fallbacks, four task files and one bootstrap. The real sibling's HEAD,
existing dirty state and 353 dependency hashes remain unchanged. This is not
a standalone-clean-sibling compatibility claim.

## Pair lookup: selected next normalization target

`func_15022024`, original `conker/asm/49D30.s:6044`, VA
`15022024..15022190`, ROM `4F4D4..4F640`, is a 91-word leaf with a 16-byte
frame. The recovered interface is four full o32 arguments:

```c
s32 func_15022024(f32 *first, f32 *second, s32 actorIndex, s32 group);
```

It requires group gate `D_800C35EA[group] == 1`, scans the unsigned byte count
at `D_800C363A[group]`, skips inactive u16 entries from `D_800C35C8[group]`,
and requires an eight-byte tag's u16 type to equal 2. Its byte at +2 must
match the selected 0x32C-byte actor's `unique_id` at +0x3B.

On the first match it clears the four output floats in retail order, then
reads optional values at +0x3C and +0x40 of a 0x44-byte record selected through
`D_800C3958[group]`. Each non-sentinel value fills its corresponding output
pair. Sentinel bits are **C61C3C00** from `D_80096A14`, captured **before**
the output clears. Return is 1 on a matching record, including when both
values are absent, otherwise 0.

Important observed access details are represented in C:

- Clear first[1], second[1], first[0], second[0] in that order.
- Retain the sentinel across output writes; do not reload it afterward.
- Reload the output's first float before duplicating it to the second float.
- Reload the global record pointer only after the first optional value's
  output stores. A narrowly scoped volatile pointer-table read preserves
  this measured retail reload; no shared global declaration is changed.

**680 cases per raw/original stream** agree with an independent reference on
public RAM and the complete result. **Ordered public read/write traces also
agree in all 680 cases**, excluding only incoming SP-16 through SP-1, the
union of the actual private frames. Full traces differ in every case because
the raw/private layouts differ; full GPR/FPR/private-state parity is not claimed.

Coverage includes groups, gates, zero/positive counts, first/later/no matches,
record/tag/actor filtering, sentinel/finite/zero/NaN/infinity bit patterns,
same/partially overlapping output pairs, record-float aliases, guest-only
sentinel-region aliases and the actual caller's positive stack offsets.
The fixture's tag table is separate from the target's private frame.

All 90 reachable retail words execute. Word **81**, VA **15022168**, is a dead
increment from normal function entry: its predecessor is the delay slot of
an unconditional branch, and no direct branch/jump targets it. The static
check records this explicitly instead of weakening the coverage assertion.
It still belongs in an eventual complete byte-exact restoration.

The literal census finds the call at VA **1503B204**, ROM **686B4**.
The actual **15-word caller window `1503B1F0..1503B22C`** passes first output
at caller SP+0xD0, second output at SP+0xC8, actor word from SP+0x40 and group
zero. It can bypass the call, saves/restores T0, and branches on the boolean
result before writing caller flags. **170 cases per raw/original stream**
execute that whole window and check its arguments, public memory and flags.
The complete large caller parent is not qualified.

Five independently compiled output controls fail their comparisons: wrong
gate, wrong tag type, wrong record field, an uncached sentinel and discarded
true return. The sentinel control is effective on the alias-sensitive cases.

### Concrete normalization outline, still unproved

The raw compiler saves only S0 in frame 8; retail uses S0/S1/S2 in frame 16.
Retail has two additional saves, two copies of the output pointers to saved
registers and two additional restores. The current C also has a redundant
two-word zero-count early return relative to retail's common zero exit.

After excluding the actual frame/save blocks and that return pair, and
classifying the inverse positive/negative count guard, both bodies have the
same **79-word core opcode/immediate/zero-role/relocation-binding multiset**.
This is an inventory result, **not a closed register or control-flow proof**:
register names, instruction scheduling, branch targets and exact private
states remain open. No word guards, insertions or omissions are installed.

Continue here rather than repeat the broad source screen. Either recover a
natural direct source shape, or prove a closed normalization that preserves
all 79 operations, six allocation words and the folded count guard. Do not
copy retail words over the body without that mapping. Then run valid SDK32
native cases, exact expected-word/binding and corruption controls, both
padders, independent GNU rebases, full guest/private/fault-prefix checks,
actual Make and an independent complete-image prediction. Only after those
and production recount/documentation gates may this function receive credit.

Guest-only alias cases do not establish portable native C guarantees. Native,
FCSR/hardware, arbitrary-pointer, full-parent and gameplay acceptance remain
unqualified in this checkpoint.

## Layout slot registration: retained separately

`func_15195AA8`, original `conker/asm/1C2C60.s:235`, VA
`15195AA8..15195D00`, ROM `1C2F58..1C31B0`, uses the existing header's canonical
eight-word, pointer-return interface. Its C candidate scans the zero-key list,
uses the scanner/constructor/index helpers, and selects one of two five-slot
halfword-index arrays and their byte tile counts. Full arrays skip the writes.

The original loads incoming argument 4 from SP+0x70 into S6, clears it after
successful binding and writes it back before the epilogue. No value-dependent
use appears in the complete original. The current compiler eliminates this
lifetime from the candidate. Routine profile/source screens did not restore
the complete 150-word body; the selected ordinary O2/g3 candidate remains
147 words with the original 96-byte frame. Do not invent a behavioral flag
test, padding local, register directive or broad volatile qualifier to force it.

The header and 24 literal call sites establish eight arguments and the pointer
result. This candidate has **owner/source/codegen screening only**; the pair
lookup's guest/caller proofs do not apply to it. Native, connected caller,
normalization and linked gates remain outstanding. Its source packet is banked
so this audit need not be reconstructed on the next turn.

The refreshed remaining queue also exposes small entries containing interior
entry labels, unusual register conventions or mixed handwritten/ordinary
code. Those need ownership/boundary audits before treating their word counts
as standalone C conversion targets. No matcher or denominator was changed.

## Production, documentation and commit boundary

The prior accepted complete production image remains byte-identical:

```text
370aca4f81e5197454282894dae2680d22f39bb10b442396fab8277cec9c5927
```

Its existing full-image qualification is reused by exact whole-image equality;
no new production build is claimed for this tools/docs checkpoint. All 3,009
previously frozen inputs are audited. Original sources, actual objects,
progress rows, guards, compiler/layout inputs and root README remain fixed.

Tools are committed first; the consumer commit records the pin and this note
with concise indexes. The graph update retains all prior node IDs and adds
explicit **private/uncredited** candidate nodes; it does not mark the installed
placeholder definitions recovered, or claim a full-corpus extraction. Actual
post-commit graph producers are observed terminal before banking the next
immutable snapshot. Codex is the only writer; Claude calls: zero. Nothing is
pushed and no sibling host/Release work is performed.
