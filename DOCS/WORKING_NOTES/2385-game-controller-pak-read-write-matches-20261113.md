# Game controller-pak read and write matches

Date: 2026-11-13. The Game copies of four libultra controller-pak routines now
replace their C placeholders with the corresponding recovered Init logic:

| Function | Retail address | Words |
| --- | --- | ---: |
| `__osContRamRead2` | `0x151F2080` | 145 |
| `__osPackRamReadData2` | `0x151F22C4` | 90 |
| `__osContRamWrite2` | `0x151F2430` | 140 |
| `__osPackRamWriteData2` | `0x151F2660` | 95 |

All four compile to the retail instructions directly, without word guards. The
Game and Init packet builders are retail-identical; each Game transaction only
differs from its Init counterpart in the builder called. The two Game owners
now use the same `-O1` profile as their Init counterparts. The read transaction
handles channel errors, data CRC, retries and output copying; the write also
honors the protected-address/force check. The packet builders prepare the PIF
request, including the original copied structure padding byte.

The status word is explicitly named `D_80042A0C`, the existing alias at
`__osPfsPifRam + 0x3C`. This matters beyond the retail link: when both fields
were referenced through `__osPfsPifRam`, the padded assembly reordered
interleaved MIPS HI16/LO16 relocations and could bind one high half incorrectly
at an alternate address with a low-half carry. The explicit status alias avoids
that ambiguity. This finding does not establish that the general padding tool
has been repaired for other inputs.

Tools commit `4899020` provides the reproducible tests:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_controller_pak2_match -v
```

Both the mounted tools and an isolated sibling overlay passed. The latter is a
hybrid with mounted fallback modules; the sibling's 2,434 existing dirty paths
were preserved. The tests cover 98 packet cases, 659 packet access-fault prefixes,
216 connected transaction cases, native 32-bit O0/O2/O3 with trapping UBSan,
and four GNU-link address layouts. The SI, DMA, message, status, and CRC
providers are modeled; native checks use an aligned channel. These checks are
not a physical controller-pak test. An aligned direct-call and literal-pointer
scan finds only each wrapper's call to its own builder; indirect or dynamic
uses are not ruled out.

The actual Make build and independent whole-image audit pass: four changed
function bodies among 6,051, all function addresses fixed, 189,088 protected
data bytes unchanged, and zero image exclusions. The one symbol-metadata
reordering is explicitly accounted for. Only the two intended objects changed
among 698 fingerprinted linked objects; the conversion and guard CSV files are
unchanged. A scoped Graphify refresh retained all 60,048 prior nodes; it was
not a full-corpus extraction.

Fresh production recount: Game **3,772 / 4,843 (77.89%)**, total
**4,445 / 5,516 (80.58%)**, zero address drift. **103** further Game matches
are required for 80% at the current denominator.

The next private candidate remains `func_15016850`. A 36-shape screen reached
the correct 84-word length, but its best recorded form has 79 same-position
differences and an extra saved register. Its persistent helper output and live
count reload must be preserved; the candidate is not installed or credited.
