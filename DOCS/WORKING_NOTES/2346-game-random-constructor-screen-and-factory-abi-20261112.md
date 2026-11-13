# Random constructor screens and effect-factory return ABI

**Follow-up:** [Note 2347](2347-game-paired-randomized-constructor-match-20261112.md) resolves the candidate frame differences and records their installation.

Date: 2026-11-12. `func_151303BC` in `generated_15D730` forwards the pointer
returned by `func_15130374` in retail. Its old C definition declared `void`
and discarded that result. The definition now returns `void *` and explicitly
returns the helper's result. The wrapper was already byte-exact, so this
corrects its C contract without adding a match.

Tools commit `7d9d0a5` tests the corrected ABI:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_effect_factory_return_151303bc -v
```

Both tests pass with mounted and staged sibling tools, before and after
installation. The guest test covers 128 argument/return combinations in the
old, corrected, retail and both padded bodies. Native 32-bit tests cover 64
cases at each of `-O0`, `-O2` and `-O3`, with UBSan and an effective
return-discarding negative control. All 31 functions and their relocation
bindings in the owner remained identical; its compiler object differed only
in `.mdebug`. The Make-planned shadow and real production build produced
**identical ELF and binary bytes** to the prior build. The other 1,453 linked
objects, protected Game data, guards and conversion rows were unchanged.

The next two candidates, `func_150C60D8` and `func_150C6A08`, are 197-word
randomized effect constructors. Their pointers occupy slots 4 and 5 of the
`0x80089A70` table. Retail `func_151342BC` indexes that table and calls the
selected function indirectly, passing its owner in the seventh argument.
The constructors initialize a descriptor, make eight integer and six float
random draws, invoke `func_151303BC`, and on success copy a 40-byte payload.
The underlying factory copies **112 bytes** from the descriptor, including
uninitialized tail and gap bytes. The available alternative draft omits an
unused argument slot and misinterprets the owner's `0x60` floating-point field;
it was not adopted.

Private semantic candidates compile to 197 words with 104 positions directly
identical and preserve the incoming-stack-relative descriptor and payload
addresses. They use a `0xC0` frame while retail uses `0xB8`. Tools commit
`66841d5` preserves the candidates and the following screen:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_random_paired_constructor_screen -v
```

Three checks pass in mounted and staged sibling tools. Twenty modeled ordinary
cases per candidate agree with retail, including all 112 factory-input bytes
and the copied payload. With the owner deliberately placed over the stack,
148 of 226 cases per candidate agree when the owner's 128-byte region is also
observed; **78 differ**. In two successful cases at owner offsets `-0x10C`
and `-0x104` from incoming SP, the saved return-address placement changes two
bytes of the copied owner-height field. These constructed aliases do not prove
that a real owner occupies the callee frame. The caller path is identified,
but its storage provenance and all possible inputs have not been established.
The candidates are **not installed or counted**; match the frame or establish
the actual non-overlap contract and complete the full qualification before
adoption.

The fresh linked recount remains Game **3,734 / 4,842 (77.12%)**, total
**4,407 / 5,515 (79.91%)**, zero drift; **140** additional Game matches are
needed for 80%.

The scoped Graphify refresh retained or relocated all 59,953 previous nodes,
with 59,955 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
