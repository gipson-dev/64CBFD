# Game trajectory actor scan byte match

Date: 2026-11-13. `func_150E1570` in `generated_10EA20.c` replaces a
zero-return placeholder with a semantic actor scan. The full 161-word retail
body at VA `0x150E1570..0x150E17F4` / ROM `0x10EA20..0x10ECA4` is now
byte-exact. The following three alignment words are unchanged. The 160-word
IDO source uses 21 relocation-aware checked guards, including one inserted
branch; these normalize the saved-register allocation, independent schedule,
and the original conditional source-index path. Both object padders reproduce
all retail body words and relocation bindings.

The function builds a look-at matrix and segment length, scans 25 actor records
with a `0x32C` stride, filters active, health, immunity, self and excluded
indices, and chooses the first smallest nonzero signed geometry result. It
submits the selected actor through `func_1505D1C4`, copies the source `+0x76`
halfword after that call, and returns the initializer's result. Note 2352
corrected that initializer's return ABI before this installation. Retail
uses byte and signed-halfword field loads; the alternate auto-decompiler output
misstates several widths. The null-source/no-selection path returns zero; the
selected path still dereferences the source, as in retail.

Tools commit `31f5269` provides the reproducible qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_trajectory_actor_150e1570_match -v
```

Retail, raw candidate, and both padded streams passed 1,500 finite modeled
guest cases with independent eligibility and signed-score checks, and two
null-source outcomes. The 136 source-pointer alias cases had no public, call or
outcome differences; 12 reached matching modeled stop conditions. Four cases
covered 1,339 memory-access cuts; padded streams agreed throughout and the raw
candidate had no observed private-memory differences. Eighty helper mutations
exercised incoming source and coordinate homes. The original callback passed
120 connected cases, and the second original call window passed 80, including
the null-source/no-eligible-actor case. The native 32-bit source passed 1,000
cases at each of `-O0`, `-O2` and `-O3` with UBSan and ten effective negative
controls. Twelve GNU links used three independent address layouts.

The pre-install packet passed with both the mounted tools and staged sibling
dependencies. Three sibling dependency files differ from the mounted versions;
the tests exercised both rather than assuming identical fingerprints. The
post-install production image and owner object match the independently audited
shadow byte-for-byte; the 1,453 other linked objects are unchanged. The strict
image audit accounts for 521 changed bytes with no exclusions. All 6,050
function addresses remain fixed, only this function body changes, and all
189,088 protected Game-data bytes remain unchanged. No hardware, complete
geometry-provider behavior, floating-point exception, or gameplay acceptance
is claimed by these bounded models. The existing duplicate `generated_12D630`
Make recipe warning remains.

A fresh recount reports Game **3,742 / 4,842 (77.28%)**, total **4,415 /
5,515 (80.05%)**, zero address drift, and **132** more Game matches required
for 80%. Continue with the remaining unmatched Game functions; the larger
matching goal is still open.
