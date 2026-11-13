# Game checksum-gated record spawner match

Date: 2026-11-12. `func_150AEB9C` in `game_DBA60.c` replaces a zero-return
placeholder with semantic C. The retail span is VA `0x150AEB9C..0x150AECCC`,
ROM `0xDC04C..0xDC17C`: all **76 words** now match. The raw 73-word compiler
body uses 51 expected-word guards, including three inserted instructions,
to recover retail scheduling, register allocation and relocations. Both
independent padders reproduce the retail words and relocation bindings.

For a non-null owner the routine XORs and shifts 64 words in the code window
`func_15001A08..D_15001B08`, clears two `D_800DCE50` slots if the result is
not `0xB4E42D60`, then iterates the configured records and calls
`func_151491F4`. For each successful allocation it stores the owner, its byte
at `0x3B`, and the current table entry's byte. Allocation failure ends the
loop. The table pointer and count are reread around calls as in retail. The
retail image and the pre-change linked image both produce the expected
checksum. `func_1507D754` calls the routine and discards its return register.

Tools commit `a9c811d` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_checksum_record_spawn_match -v
```

All six checks passed before and after installation with mounted tools and
staged sibling dependencies. They include 384 independent-model cases,
including factory changes to the owner, table and count; 324 completed
owner/stack overlaps; 54 cases connected through all 28 original factory
wrapper instructions with its deeper allocator modeled; native 32-bit builds
at `-O0`, `-O2`, and `-O3`, each with 256 cases, UBSan and six effective
negative controls; and 12 GNU links at three symbol bases. The fixture caches
only the frozen 256-byte checksum window, avoiding repeated reads of the full
image. Seven other owner functions and the constant pools are unchanged.

For 752 modeled memory-access cuts, the raw C output agrees with retail on
public memory and helper calls; retail and padded bodies also agree on full
modeled memory and access traces. Four raw-C cuts differ in private frame
contents due to instruction scheduling. These tests do not establish portable
C fault behavior or runtime gameplay acceptance.

The real Make build matches the independently audited shadow ELF, binary and
owner object. The strict image audit accounts for all **249** changed bytes
with zero exclusions; only the target function changed, all **6,050**
function addresses stayed fixed, and all **189,088** protected Game-data
bytes were unchanged. The other 1,453 linked objects and conversion rows were
preserved. A fresh linked recount reports Game **3,739 / 4,842 (77.22%)**,
total **4,412 / 5,515 (80.00%)**, zero drift and **135** more Game matches
needed to reach 80%.

Next revisit the private `func_150B9D8C` descriptor candidate in
[Note 2343](2343-game-effect-descriptor-alias-screen-20261112.md). Its frame
and overlapping-actor behavior remain unresolved; it is not match credit.

The scoped Graphify refresh retained or relocated all 59,961 previous nodes,
with 59,963 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
