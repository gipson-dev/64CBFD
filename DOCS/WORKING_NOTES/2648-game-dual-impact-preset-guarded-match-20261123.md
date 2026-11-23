# 2648 - Dual impact preset guarded match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_150C01DC` replaces its zero-return placeholder in
`conker/src/game/generated_EC420.c` with the complete dual impact preset
callback. Its semantic C emits **185 words in the original 240-byte frame**.
The raw compiler result has **63 scheduling word differences**. A strict
63-row relocation-aware expected-word suffix restores all 185 retail words.
This is a **guarded C match**, not a direct compiler match. No instructions
are inserted or omitted, and no shared padding code or profile changes.

Production: **4,629 / 5,528 (83.74%) total**, **3,956 / 4,855 (81.48%) Game**,
zero drift, **899 different**, **70 more matches to 85%**. Init stays 492/492
and Debugger 181/181. Conversion rows and converted-byte counts stay fixed.

Original: `conker/asm/EC420.s:1277`, VA `150C01DC..150C04C0`, ROM
`ED68C..ED970`, 740 bytes. Both complete-owner padders and the actual Make
recipe preserve the other nine functions, pools and diagnostic set.

## Interface and recovered behavior

The measured callback interface is
`s32 func_150C01DC(u8 *owner, f32 x, f32 y, f32 z, f32 height, void *contact)`.
The first three float inputs and contact pointer are unused by this preset;
the original still homes the three register float words. The height arrives
as the fifth o32 argument. Every successful execution returns integer zero.

The literal census finds no direct JAL edge and one aligned pointer:
`D_80089934[13]` at VA `80089968`, ROM `22E428`. Both original dispatch sites
load that table through the owner's selector byte at +0x73. The real windows
at `15132FDC` and `1513397C` establish all six arguments and return handling.
Computed/materialized references are not ruled out by this literal census.

Before either effect submission, the callback captures owner X at +0x38,
supplied height plus 20 with single-precision rounding, and owner Z at +0x40.
It copies a one-entry resource/scale table from `D_800A0100/0104` and fills
the 60-byte burst configuration: counts 5/4, captured position, angles,
speeds, five global floats and lifetimes 30/15. The complete 228-word original
`func_15152190` confirms the configuration layout and interface: configuration
pointer, resource pointer, scale pointer, word count, float radius, byte mode,
byte channel and word context. This caller supplies count 1, radius 0, mode 1,
then unsigned owner bytes +0xC and +1. Its return value is unused.

The later 108-byte emission descriptor uses counts 5/8, kind 108, field 0x5103,
header 0x200005, the captured position, fixed parameter/color fields, flags
0x840E07 and the global floating payload at +0x68. Its +0x54 and +0x58 floats
share a named `sharedScale` local loaded from `D_800A0160` after the first
helper. Opaque fields retain offset names. Padding +5 and +0x65..+0x67 remains
untouched. The full 224-word `func_15153634` confirms pointer/byte/byte/word
arguments. This caller passes mode 255 and **reloads** owner channel/context
after the first helper; those values cannot be cached across that boundary.

## Scheduling boundary and focused gates

The chosen raw C and original ASM have exactly the same instruction words
and relocation-binding multiset, without erasing register fields. Only
instruction ordering differs. Every one of the 63 rows checks its exact
input word and bindings. The old guard file remains an identical prefix.
There are no body substitutions, missing operations, invented constants,
register directives, volatile scheduling tricks or frame padding. Initial
107-difference source screens were reduced using clear source ordering and
a local scalar; unsuccessful alternatives remain private and uncredited.

Five focused gates pass freshly in each tools setup before installation.
Installed runs freshly repeat source/object/Make/full-image qualification;
four semantic gates are reused only with exact source, raw object, guard,
binding, original ASM, manifest, native artifact and import fingerprints.

- **128 cases per raw/padded/original stream** check every initialized field
  of both packets, resource and scale copies, untouched padding, call order,
  public effects, final memory and GPR/FPR/HI/LO state. All 185 target words
  execute. Coverage includes boundary finite heights, signed zero/subnormals,
  NaN payload copies, both stack phases, ordinary/caller-stack owner buffers,
  and first-helper mutations of owner bytes, coordinates and globals.
- **64 cases per stream** execute both original indirect callback windows,
  checking table index 13, all six arguments and zero-result handling.
  These are measured 19-word/17-word windows; the first visits 17 words on
  this selected callback path. Complete dispatcher parents are not claimed.
- **306 fired access-cut prefix pairs** compare normalized/original memory,
  registers, ordered traces, calls and packet observations. The raw C differs
  in **144** private prefixes and all 128 complete access traces; its access
  schedule is not described as retail exact. Final state/effects agree.
- Actual SDK32 raw C passes **8,192 cases each at O0/O2/O3**, with UBSan,
  strict aliasing and explicit single-precision height rounding. Typed
  boundaries check all named fields, resource/scale values, snapshot timing,
  reloaded bytes and owner canaries. Eight source controls fail comparison:
  late position snapshot, wrong height/kind/color/resource count/shared
  scale/flags/return. Native code does not read uninitialized padding.
- Both isolated and complete-owner padders produce exact bytes. **12 GNU
  links and 96 guest rebase runs** cover four independent code/two-callee/data
  arrangements, signed-low-half carry and another J26 region. Four wrong
  instruction/binding outputs fail comparison; four stale expected inputs
  fail closed. Both padders reject the oversized control.
- `make tools-check` passes. The disposable sibling overlay explicitly uses
  required primary fallbacks. The actual sibling tools HEAD, dirty state
  and 353 retained dependency hashes are preserved. Routine Claude calls: 0.

The first late-snapshot negative fixture left the first burst position
uninitialized and was rejected by the host compiler. It was corrected to
preserve the first snapshot and wrongly resnapshot only for the second
packet, then all five gates were rerun freshly. No production fix was needed.
Consumer internals are bounded providers. Hardware/gameplay acceptance is
outside these tests. A read-only sibling audit rechecks both scene TOML
hashes and their binary inputs. The selected-scene configuration still lists
this callback as a stub; neither configuration imports this C owner. The
inspected host path contains artifact directories, with no Git/CMake root.
No direct host change is applicable here; no host build or Release change
or host runtime qualification is claimed.

## Independent full-image and production audit

The private and production full images equal an independent literal
prediction: **766 changed bytes, zero exclusions**. Only the target slot and
its symbol size 12->740 change, plus **15 closed metadata record permutations**
whose complete list is pinned. ELF geometry, every other named definition
and the reconstructed full string pool are checked, without excluding any
symbol/string section. All **189,088 protected Game data bytes across 720
owners** remain fixed, along with other loaded bytes, profiles and inputs.

The independent reference recompiles the frozen OLD owner with OLD guards,
requires its full padded object to equal the frozen production object, and
replaces only this slot with independently assembled original ASM. The new
C and guards do not construct that reference. A fresh production Make,
dependent-object input audit and live recount establish the totals above.

Raw target SHA256: `9daf2bf33c9c874322a6da1d7e1f1103cefae62b1a181036b11640628dc11014`.
Normalized full-owner SHA256: `1d9f631be05bea733ba563259753cbd7f352f0a1a3592816a256c21bf0eb674c`.
Production ELF SHA256: `a7ac1c4b47c59a9a68430020c94f3691bd33ebfc84ed4b84136a773c7bea5834`.

```sh
python3 -m unittest tools.tests.test_game_dual_emission_preset_150c01dc_match -v
```

Retained evidence: `conker/build/game-dual-emission-preset-150c01dc-private/`.
Tools are committed before the consumer pin. Graph refresh retains all old
node IDs and qualification metadata; the scoped update is not a full-corpus
re-extraction. No push. Codex owns implementation and validation.

## Next work

[Note 2647](2647-game-actor-emission-preset-guarded-match-20261123.md) preserves
the preceding actor preset. `func_150BF760` is the next shorter unfinished
same-owner candidate: 199 words, VA `150BF760..150BFA7C`. Inspect its complete
original body, bindings and callers before source fitting. The separate
`func_150A6760` decoder remains private and uncredited. The original final
null-object branch in `func_150BF760` needs an explicit fault/ABI audit before
portable source or any repair is proposed. Continue the full 85%
goal with 70 further qualified matches required.
