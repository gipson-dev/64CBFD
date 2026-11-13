# Game ground-height effect dispatcher match

Date: 2026-11-12. `func_150CDBB0`, owner `generated_FB060`, VA
`0x150CDBB0..0x150CDCF4` and ROM `0xFB060..0xFB1A4`, now has its semantic
C implementation in place of a zero-return placeholder and matches all
**81 retail words**. Its interface takes an actor pointer, an eight-bit effect
flag, and an unused third argument.

For a non-null actor, the routine initializes a height result, builds a query
point from the actor's floating-point position with 1,000 added to its vertical
component, and queries against the actor's current height minus `D_800A07B0`.
If the query succeeds, it uses the returned height and submits two effects.
The first uses a random count in the range 35–50 and type `0x17`; the second
uses a count in the range 30–50 and type `0x18`. The original caller is
`func_15171BF4`. The alternate-source draft was not adopted: it interpreted
the actor's floating-point position fields as integers.

The compiler emits 80 words. **Four relocation-aware expected-word guards**
restore the retail height-store and random-call schedule, including one
inserted delay-slot word and the affected branch distances. Both independent
padders reproduce the complete retail body and its relocation bindings. The
two other owner functions remain unchanged.

Tools commit `a94c732` supplies the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_ground_effects_150cdbb0 -v
```

Before and after installation its seven checks passed with both mounted and
staged sibling tools. The guest model compares the raw C and three retail/padded
bodies over 1,728 cases, including null actors, query outcomes, actor/stack
aliases, flag widths and helper mutations; all 81 retail instructions were
visited. It also covers 96 cases connected to all 18 original RNG instructions,
72 cases through the original caller window, and 165 modeled access-fault cuts.
Twelve GNU links exercise three independent bases. Native 32-bit checks pass
360 finite cases at each of `-O0`, `-O2` and `-O3`, with UBSan and ten
effective negative controls. Guest fault-prefix agreement covers observable
memory and helper calls; the raw C call-delay schedule can differ, and these
models do not establish hardware or gameplay acceptance.

The actual Make build, link and binary extraction match the independently
planned shadow. The strict full-image audit accounts for all **251 changed
bytes with zero exclusions**; only this function's linked body changed, all
6,050 function addresses remain fixed, and all 189,088 protected Game-data
bytes are unchanged. The generator's conversion rows are unchanged because the
old placeholder was already counted as C. A fresh linked-image recount reports
Game **3,732 / 4,842 (77.08%)**, total **4,405 / 5,515 (79.87%)**, zero address
drift and **142** additional Game matches needed for 80%.
The scoped Graphify refresh retained all out-of-scope nodes: 59,945 before,
59,947 after, with three IDs relocated by matching signatures. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.

Next screen `func_150B9D8C` in `generated_E5E90`, an unmatched effect routine;
its payload, random draws, callback ABI and live caller still need full
qualification. This selection is not match credit.
