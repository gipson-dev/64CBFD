# Game effect intensity callback match

Date: 2026-11-12. `func_151C7038`, owner `generated_1F3780`, VA
`0x151C7038..0x151C7194`, ROM `0x1F44E8..0x1F4644`, now contains its
semantic C implementation and matches all **87 retail instruction words**.
The surrounding retail slot has additional alignment bytes. The prior source
was a zero-return placeholder.

The callback reads the owner's effect pointer at `0x7C` and returns zero if
its effect's type at `0x84` is not `0xE9`. Otherwise it calls
`func_15142A5C`, sets or clears owner flag `0x20000`, scales the cached
(effect-before-call) pointer's float at `0x4C` by 35, clamps the result to
`[0, 255]`, stores the converted byte at owner `0x70`, and returns one. The
pointer is retained across the helper call; the flags and scale are read after
that call. These details matter if the helper mutates the owner or effect.

The compiled C emits 85 words. Twenty-one relocation-aware expected-word
guards replace compiler-emitted words to normalize branch displacement,
floating-point register and constant scheduling, and result scheduling; two
rows also insert retail instructions at the corrected positions. The resulting 87-word body and relocation binding
match independently assembled retail through both generated-slice and generic
padders. Seven other compact and padded owner functions, normalized pools and
diagnostic categories were preserved. The compact `.reginfo` changed as a
result of the new float operations; the assembled padded metadata is unchanged.
The guards are pinned to the exact compiler output; the source remains a
semantic C implementation.

Tools commit `29dca9a` contains the reproducible qualification packet. From
the decomp root, run:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_effect_intensity_151c7038 -v
```

The seven tests passed before and after installation with the mounted tools
and separately staged sibling dependencies. They include 1,280 modeled guest
cases across the raw, retail and padded bodies; 256 overlapping owner/effect
cases; 84 modeled access-fault cuts; 400 cases connected to all nine words of
the byte-exact retail helper; and 60 cases through the original
`D_800898B0[23]` table entry and the `func_151321D0` call window at
`0x15132264`. Native 32-bit tests pass at `-O0`, `-O2` and `-O3`, with
192 cases and six effective negative controls each under UBSan. The native
float-to-unsigned cast tests exclude NaN; non-finite guest cases and FCSR
restoration use the existing instruction model and are not hardware exception
proof. These checks are not a visual or gameplay acceptance claim.

The independently planned shadow Make build and the installed production
build produced the same object and linked ELF. The strict full-image audit
found 237 changed bytes and **zero exclusions**; the only changed function
body is `func_151C7038`, and all 6,050 function addresses are unchanged.
All 189,088 protected Game-data bytes match the baseline. A fresh production
ELF recount reports **3,726 / 4,840 Game matches (76.98%)**, **4,399 / 5,513
total matches (79.79%)**, zero drift, and **146** additional Game matches
needed for 80%.

The interpolation draft in [Note 2336](2336-game-sequence-interpolation-layout-screen-20261112.md)
remains private and uncredited. Continue the Game matching queue without
assuming that its unsigned-conversion and floating-point concerns transfer to
this callback or that either has hardware runtime acceptance.

The scoped Graphify refresh retained all out-of-scope nodes: 59,932 before,
59,935 after, and three relocated IDs matched by signature. Its fail-closed
path retained 31,816 existing nodes; this was not a full-corpus extraction.
