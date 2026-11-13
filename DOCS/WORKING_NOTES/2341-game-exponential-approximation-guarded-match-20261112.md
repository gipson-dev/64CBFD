# Game exponential approximation guarded match

Date: 2026-11-12. `func_1504A2B0`, owner `generated_77760`, VA
`0x1504A2B0..0x1504A3F4` and ROM `0x77760..0x778A4`, now has semantic C
in place of its zero-return placeholder and matches all **81 retail words**.
The recorded slot extends to `0x1504A400`; its alignment tail remains intact.
The single floating-point argument and return use the o32 floating-point ABI.

The routine evaluates an exponential approximation. It returns one below the
`2^-23` magnitude threshold, divides the magnitude by the stored ln(2)
constant, and uses a convergent series for the remainder. It repeatedly doubles
the sum for the integral scale and returns its reciprocal for negative input.
For a converted scale of at least 1,025 it returns the stored maximum finite
float for nonnegative input or zero for negative input. The original caller
`func_1504A400` feeds it the product of a logarithm result and an exponent.

The available alternate-source draft was screened independently and emitted
96 words after enabling the compiler's `fabsf` intrinsic; it was not a match.
The recovered simpler source emits 79 words. **29 relocation-aware expected
word guards**, including **two inserted words**, normalize its register
allocation and constant-load schedule into the retail instruction stream.
Three guards move the ln(2) symbol's relocation pair. Both independent padders
produce the complete retail body and relocation bindings.

Tools commit `389f4b4` supplies the seven-check qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_exponential_1504a2b0 -v
```

Before and after installation it passed against both the mounted tools and
staged sibling dependencies. The finite binary32 instruction model compares the raw
C body, retail assembly and both padded bodies across 498 inputs and visits
80 retail words. It also exercises 35 cases through the actual caller window,
seven guest read-access cuts, and 12 actual GNU links across three rebases.
The native 32-bit checks pass 498 finite, defined-conversion cases at each of
`-O0`, `-O2` and `-O3` with UBSan and eight effective negative controls.
Six non-finite or out-of-range cases were compared only as bounded 50,000-step
guest instruction prefixes. Their float-to-signed-integer conversion is
outside the defined C domain; these checks do not establish portable C, FCSR,
hardware-exception or gameplay behavior for those values.

The actual Make build, link and binary extraction match the independently
planned shadow. The strict full-image audit accounts for all **334 changed
bytes with zero exclusions**; only this function's linked body changed, all
6,050 function addresses remain fixed, and all 189,088 protected Game-data
bytes remain exact. The generator's conversion rows remain unchanged because
the old placeholder was already counted as C. A fresh linked-image recount
reports Game **3,731 / 4,842 (77.05%)**, total **4,404 / 5,515 (79.85%)**,
zero address drift and **143** additional Game matches needed for 80%.
Removing the obsolete placeholder comment was followed by a second Make
rebuild; its owner object, linked ELF and binary all remained identical.
The scoped Graphify refresh retained all out-of-scope nodes: 59,943 before,
59,945 after, and three IDs relocated by matching signatures. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.

Next screen `func_150CDBB0` in `generated_FB060`, an 81-word unmatched actor
effect routine called from `generated_19E040`. Its null gate, argument widths,
helper interactions and complete retail slot still need qualification; this
selection is not match credit.
