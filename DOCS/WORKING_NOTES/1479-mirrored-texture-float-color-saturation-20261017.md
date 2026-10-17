# Mirrored Texture Float Color Saturation

Date: 2026-10-17

Continue [Note 1478](1478-mirrored-texture-upstream-home-provenance-20261017.md)
from clean consumer **819f51b4**, tools **b44bad7**. Same uninstalled
**func_1517FB9C**, 633 retail words/frame 0xD8. This investigation preceded
the independent reset installation in [Note 1480](1480-overlay-mode-defaults-direct-match-20261017.md).
It does not add renderer matching credit or qualify an alternative for installation.

## Actual Allocation Constraints

Two target-specific adapters reuse the existing owned mode5 UOPT diagnostic,
normal compiler profile, exact isolated/full-owner target hashes and qualified
completion/object checks. The cc/cfe/uopt/ugen fingerprints remain unchanged.
The diagnostic allocates a debug-stream buffer and suppresses real-number
printing only inside its newly owned UOPT child. It is not a wholly read-only
process observation. No compiler file or configuration is changed.

Both captures complete with normal/traced code, functions, bindings and pools
identical. Installation/removal gates and child/driver exit0 are checked.
**Debug real-number costs/timings are invalid; use only integer identities,
colors, forbidden sets and interference.**

The original 626-word candidate yields **35 variable records / 110 allocation
records**. The following association is corroborated by that candidate's
emitted instructions, not claimed as a general color mapping for all targets:

| Value / Expression | Mode5 Color | Emitted Role |
| --- | ---: | --- |
| Float size / 41 | 24 | F0 |
| centerX / 8 | 25 | F2 |
| centerY / 16 | 26 | F12 |
| offsetX / 24 | 27 | F14 |
| positiveX add / 26 | 28 | F16 |
| offsetY / 30 | 29 | F18 |
| positiveY add / 32 | 0 | Uncolored, M-120 / SP+0x60 |

The positiveY record has forbidden colors **[24,25,26,27,28,29]**.
Its source variable M-20 is expression28, while its surviving addition is
expression32. Do not mistake the eliminated variable entry for the allocated
expression. The allocation evidence narrows the first spill issue to actual
float-color saturation and input/expression lifetimes, not a late UGEN guess.

## Changed Spill, Still Not A Match

A targeted source form snapshots offsetX after the centers, computes
positiveY before positiveX, and uses that saved X offset for both X sums.
It produces **624 words / frame 0xD8 / 543 ordinal differences**.
PositiveX now spills and offsetY/positiveY use F16/F18, but the spill is
**SP+0x5C**, not retail's +0x54. OffsetX is F12 and centerY is F14, the
opposite of retail's F14/F12. The length deficit is nine words, not a
nine-word scheduling certificate.

Its allocation trace yields **36 variables / 110 records**: offsetX gets
color26 with an empty forbidden set, centerY gets color27, offsetY28,
positiveY29, and positiveX's expression35 is uncolored with all six colors
forbidden. This is partial residency progress, not full register/home recovery.

Raw candidate SHA-256:
`be79ea5c922c834aa00875e23e5e46e8f6167f3fb867766bad4f0f17bd412d22`.
Both global binding pairs are unchanged. The two allocation text hashes are:

- Record candidate: `9d9a2ed62a3ff6ce0339ba78e3e7b52b061aa1536ee4513770e40cd987ab459c`.
- Ordered X snapshot: `c70a5ab7219d15154b54c72a680ddb55d733bdda9b5699feadaf229ce1e6bde9`.

Thirteen bounded complete-source forms were measured, not installed:
early X/XY snapshots, late ordered snapshots, inline positive-coordinate
expressions, a separate word-sized negative rate, and late u16 rate narrowing.
Inline coordinate forms produce 618..622 words and smaller frames. Late rate
narrowing emits exactly the prior candidate in both tested bases. A named
negative rate does not recover the original two-home/register lifetime.
None closes the full 633-word or private/fault contract. The earlier public/
native qualification is evidence for the original 626-word candidate only,
not qualification of these changed forms.

## Retained Local Evidence

The prepared checkout retains these ignored, transient investigation artifacts
under `conker/build/game-mirrored-texture-rectangles/`:

- `lifetimes.py`, full source/object/JSON files for all thirteen forms.
- `allocation.py`, `allocation-record-mode5/`, `allocation-late-x-y-first-mode5/`.
- Each allocation directory's script, baseline/traced objects, uoptlist,
  parsed integer records, debugger log and completed trace.json.

These adapters are local investigation artifacts, not a newly published CLI.
They refuse an existing allocation output directory. Do not restart a compiler
on an observation timeout or run the old text-measurer/rectangle target
unmodified and report it as mirrored-texture evidence.

**Next: retain this open renderer target.** Recover the remaining centerY/
offsetX lifetime ordering without an artificial storage/volatile effect, the
positiveX +0x54 home, and shared rate residency at +0x34/+0x30 with T4.
Preserve full-word Y sign tests and unsigned conversion paths. Require all
633 words and private/fault gates before installation. Broader Game work may
bank independent qualified functions without assigning this renderer credit.
