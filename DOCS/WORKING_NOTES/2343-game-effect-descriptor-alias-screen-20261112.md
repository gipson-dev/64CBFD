# Game effect descriptor: uncredited alias screen

**Follow-up:** [Note 2365](2365-game-effect-descriptor-direct-match-20261113.md) restores the exact frame and installs the direct C match. The observations below describe the earlier candidates.

Date: 2026-11-12. `func_150B9D8C`, owner `generated_E5E90`, has a retail
body at VA `0x150B9D8C..0x150B9EC4` / ROM `0xE723C..0xE7374` (78 words),
followed by three alignment words. The existing C remains a zero-return
placeholder. This note does **not** claim a restoration or a match.

The retail body checks a signed halfword at actor offset `0x98` for `-1`.
On the selected path it initializes a 40-byte descriptor, draws three random
values, converts four signed actor halfwords to floats, and calls
`func_1513C4EC`. The descriptor's 15 unwritten bytes matter: the underlying
factory copies the complete 40-byte object. The available alternate-source
draft misidentifies several of the actor's halfwords and byte fields.

A semantic C candidate has the correct 78-word length and 74 identical words.
Four expected-word guards map the two saved random draws to retail's stack
slots; both independent padders then emit the complete retail body and
bindings. A modified candidate reduces the difference to two words; a packed
work-area candidate preserves the draw/descriptor addresses relative to the
incoming stack pointer but has a larger frame and 19 differing words.

These candidates are **not qualified for installation**. When an actor is
deliberately placed across the callee's stack frame, its fields can alias the
draw slots or saved-register slots. With the four-word candidate at
`actor = incoming_sp - 0xD0`, the raw C sends `0x42C80000` as the first float
argument while retail sends `0x4591A000`; the guarded body matches retail.
A second overlap exposes different factory arguments in both the two-word
candidate and the larger-frame candidate. These are bounded guest tests, not
evidence that a normal actor actually occupies that location.

The literal census of the decompressed code image found no aligned pointer,
direct J or JAL to this entry, and no nearby LUI/address pair in the screened
window. A neighboring function's pointer at ROM offset `0x22E450` is a positive
control. Dynamic, computed or external dispatch remains unresolved; absence
from this census does not prove the function has no callers. Resolve the
actual caller and its actor-storage contract, or recover a source/frame shape
that also preserves the overlapping cases, before awarding match credit.

Tools commit `d78edf5` makes the screen repeatable:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_effect_descriptor_150b9d8c_screen -v
```

All five checks pass with mounted and staged sibling tools. They include 72
ordinary modeled cases, all 40 descriptor bytes including seeded padding, 48
cases connected to all 18 original RNG instructions, the two overlap controls,
both padders, and the bounded direct-reference census. No production source,
guards, image or progress rows were changed by this screen. A fresh recount
remains Game **3,732 / 4,842 (77.08%)**, total **4,405 / 5,515 (79.87%)**,
zero address drift, with **142** additional Game matches needed for 80%.

Next screen the related `func_150C5F94` and `func_150C68C4` routines. They
have closely related retail bodies and known callers in `generated_F3270` and
`generated_F3BA0`; their payloads and alias behavior still need qualification.

The scoped Graphify refresh retained or relocated all 59,947 previous nodes,
with 59,949 nodes afterward and no changes outside the selected files. It
retained 31,816 nodes fail-closed; this was not a full-corpus extraction.
