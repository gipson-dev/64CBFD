# Game impact-effect dispatcher pair byte match

Date: 2026-09-29

## Scope and behavior

Adjacent `func_15194320` and `func_15194394` in
`conker/src/game/generated_1C1150.c` each occupy 29 words and 116 bytes:

- `func_15194320`: `0x15194320..0x15194394`
- `func_15194394`: `0x15194394..0x15194408`

Both read source byte `0x4` and accept values zero through four through a
grouped switch. Accepted states call `func_1518D1C0` with zero subtype, mode
one, owner `0xFF`, selector one, and a distinct effect definition:

- `func_15194320` uses effect ID `0xA` and `effects_impact_lavaboulder`.
- `func_15194394` uses effect ID `0xC` and `effects_impact_fireimp`.

Values above four return without dispatching an effect.

## Compiler and rodata shape

The grouped switches reproduce retail's unsigned range checks and separate
five-entry jump tables, even though every accepted entry reaches the same
call body. The `generated_1C1150` object maps compact `.rodata` offset zero to
the preserved `jtbl_800A8258_game`; the second table then follows at its
retail offset.

Both complete 40-byte frames, incoming argument homes, switch branches,
jump-table relocations, seven-argument call setups, string relocations, call
delay slots, and epilogues emit directly from semantic C. No expected-word
guards are needed.

## Verification

- The focused `generated_1C1150` object builds with all 29 retail words in
  each function.
- The complete Makefile-driven object rebuild and ELF relink pass with the
  retail rodata anchor.
- Direct linked comparison reports zero differences across both 116-byte
  spans.
- `func_15194320` shares SHA-256
  `8437b4dd34bf84b387ab2bc2a1f2994c271cbfc9db1040a2ea8aea0691302db3`.
- `func_15194394` shares SHA-256
  `94c06f34b68c23f199ab3e8ac64f9c76776135864bfe7f9d9a2819369ffa1deb`.
- The authoritative matcher omits both functions from its non-exact list and
  reports `2,995 / 5,465 (54.80%)` overall and `2,420 / 4,789 (50.53%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next small Game or Init candidate. Preserve the
`generated_1C1150` rodata anchor while recovering later jump-table routines in
the same slice.
