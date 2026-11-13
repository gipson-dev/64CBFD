# Paired Game ground-height effect descriptor matches

Date: 2026-11-12. `func_150C5F94` (`generated_F3270`) and
`func_150C68C4` (`generated_F3BA0`) replace zero-return placeholders with
semantic C. Each matches all **81 retail words**, including 29 checked,
relocation-aware instruction-scheduling guards per function. Their original
callers are `func_150C5F40` and `func_150C6870`.

Each routine builds a query point from the owner position, asks for ground
height with a lower bound 100 units below the owner, and prepares an attached
effect descriptor. It selects the query result on a hit or an offset from the
owner's current height on a miss. On factory success it copies a 12-byte
context/height payload to the returned record; the original descriptor and
payload padding remains untouched. The two routines use different constants
and variant fields. Factory failure returns zero without the payload copy.

**Correction to Note 2344:** its first screening used `0x40000` for both the
context and the emulated stack pointer. Those 96 cases were overlapping
contexts, not ordinary non-overlapping cases. The corrected fixture places the
context at `0x48000`; the full tests below pass with the correction. The ten
previously incomplete overlap cases per function now compare modeled memory
and helper calls at the point execution stops as well as the exception.

Tools commits `183ca20` and `489834a` provide the qualified packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_paired_height_descriptor_screen -v
```

All seven checks passed with mounted tools and a staged sibling dependency
set, before and after installation. Per function, they cover 96 ordinary
cases with independent descriptor and ABI assertions; 638 completed
stack-overlap cases and ten invalid overlapping cases; 80 cases through the
original caller and 80 through the original factory and copy routines. The
connected tests visit 74 of 76 factory instructions and all 11 copy
instructions. Native 32-bit builds at `-O0`, `-O2` and `-O3` each pass 96
finite cases with UBSan and five effective negative controls. Twelve GNU
links per function exercise three independent symbol bases.

For each function, 288 modeled fault cuts compare public memory and calls;
the retail and both padded programs also agree on the full modeled memory and
access trace. The unguarded compiler output has private frame differences at
64 cuts due to scheduling; fault-prefix tests are guest observations, not a
portable C fault or gameplay claim.

The Make-planned shadow build and production Make build produced identical
ELF, binary and owner objects. The strict image audit accounts for all **589**
changed bytes with no exclusions; only the two selected functions changed,
all **6,050** function addresses remained fixed, and all **189,088** protected
Game-data bytes were unchanged. The other 1,452 linked objects and existing
conversion rows were preserved. A fresh linked recount reports Game **3,734 /
4,842 (77.12%)**, total **4,407 / 5,515 (79.91%)**, zero address drift and
**140** additional Game matches needed for 80%.

Next inspect the related `func_150C60D8` and `func_150C6A08` bodies and their
callers as potential paired candidates; their longer payloads and exact
behavior remain unqualified.

The scoped Graphify refresh retained or relocated all 59,951 previous nodes,
with 59,953 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
