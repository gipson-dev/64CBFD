# Game paired random-effect wrappers converted directly to C

Date: 2026-11-12. `func_150D6388` and `func_150D6434`, owner
`generated_1028F0`, were ordinary assembly-backed wrappers and now have
semantic C bodies. The first spans VA `0x150D6388..0x150D6434` and ROM
`0x103838..0x1038E4` (43 words); the second spans VA
`0x150D6434..0x150D64E8` and ROM `0x1038E4..0x103998` (45 words).
Both emit their complete retail instruction streams and relocation bindings
directly from C, without target word guards. Their original assembly remains
as a reference.

Both accept a position, an eight-bit selector and a context. The first draws
one floating-point and one integer random value and submits a point effect;
its unsigned integer reduction has a 56-value range. The second draws three
floating-point values and passes the resulting parameters to the effect actor
factory. Their live caller `func_150D5A6C` uses consecutive call windows at
`0x150D633C` and `0x150D634C`. All 17 owner functions, normalized constant
pools, compact register metadata and compiler diagnostic categories were
preserved; two independent padders reproduce the retail bindings.

Tools commit `3c54fde` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_random_effect_pair_150d6388 -v
```

Before installation, its seven checks passed both in the mounted tools and
with staged sibling dependencies. The guest model exercises 36,864 cases
across each of three bodies and all selector values, with helper mutations;
192 cases use the original RNG and visit all 43 of its instructions; 96 cases
use the original caller windows. Additional coverage includes 144 modeled
non-finite cases and 348 modeled instruction-access cuts. Native 32-bit UBSan
checks exercise 896 finite cases per `-O0`, `-O2`, and `-O3`, with 13 effective
negative controls. The local model corrects an inherited `MFC1` register-write
issue for this packet. Non-finite model results are not hardware FPU or
gameplay acceptance.

The seven checks also pass after installation in both tools environments. The scoped
Graphify refresh retained every out-of-scope node: 59,939 before and 59,943
after, with three IDs relocated by matching signatures. Its fail-closed path
retained 31,816 existing nodes; this was not a full-corpus extraction.

The actual Make owner build, link and binary extraction match the independently
planned shadow: the entire owner object, ELF and binary are byte-for-byte
identical to the frozen baseline. All 6,050 function bodies and addresses and
189,088 protected Game-data bytes are unchanged. Progress regeneration changes
only the two intended rows from assembly to C, so the matching numerator and
converted denominator both rise by two. A fresh linked-image recount reports
Game **3,730 / 4,842 (77.03%)**, total **4,403 / 5,515 (79.84%)**, zero
address drift and **144** additional Game matches needed for 80%.

Next screen `func_1504A2B0`, an unmatched floating-point routine in
`generated_77760` whose 84-word recorded slot begins with an absolute-value
threshold and contains a convergent series. Its interface, floating-point
edge cases, linked slot and callers still need qualification; this initial
screen is not match credit.
