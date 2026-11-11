# Scaled vertex-radius initializer byte match

Date: 2026-11-11. `func_15004AAC` replaces the zero-return placeholder in
`conker/src/game_30E90.c`; the retail assembly remains in
`conker/asm/nonmatchings/game_30E90/func_15004AAC.s`. Its 81-word body spans
VA `0x15004AAC..0x15004BF0`, ROM `0x31F5C..0x320A0`.

The recovered C scans signed 16-bit vertex coordinates with a 16-byte stride,
scales each component, takes the largest truncated squared distance and
computes its square root. It initializes the two stored radius fields if the
first is zero, or classifies an existing pair against the calculated radius;
three 16-bit global counters record those outcomes. The unused second argument
is retained for the original calling convention. Twenty-seven expected-word
guards normalize the compiler's different register assignments and instruction
schedule, including the ordering of independent vertex and scale loads.

A bounded guest oracle compared the retail body, compiled C and normalized
body over 240 valid finite non-overlapping cases and visited all 81 words.
The original `func_150039E0` call window passed the same cases; the entire
parent function is not qualified. An aligned ROM census found one direct JAL
at `0x31664` and no aligned entry-address literal. SDK32 native O0/O2/O3 each passed 240 cases
and ten negative controls, with undefined-behavior sanitization. The raw C
and retail perform some loads in different order, so concurrent mutation,
aliasing, faults, exceptional floats and out-of-range conversions are not
covered by this equivalence claim. No claim of hardware qualification is made.

Both object padders match independently assembled retail code and relocation
bindings after the guards. Twelve rebased GNU links, 29 bounded access-cut
triples and 114 raw, binding or guard corruption rejections pass. Actual Make
and strict independent image comparison account for **267 changed
bytes**, without exclusions. Two symbol-order metadata cycles are recorded in
the manifest. All 6,050 function addresses and 189,088 protected data bytes
remain unchanged. Actual ELF SHA-256: `8d3dd93d5fa5e3db17d1e69fe7c86c46b4e7513b15ed6910f24b1872dbb026e3`. The existing
complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,339 / 5,513 (78.70%)** overall and **3,666 /
4,840 (75.74%)** Game, zero drift and 1,174 different. The 80% target needs
72 more exact functions. The tools commit `304233eaa522935693c50dd1059daaccb4dee4a3`
precedes the consumer change. The separately documented declaration issue in
[Note 2268](2268-initializer-declarations-and-startup-audit-20261111.md)
remains open.
