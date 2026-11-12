# Effect descriptor candidate: private first compile

Date: 2026-11-12. `func_150C1E34` is a 75-word unmatched C placeholder in
`conker/src/game/generated_EEE70.c`, spanning VA `0x150C1E34..0x150C1F54`
and ROM `0xEF2E4..0xEF404`. Its retail implementation constructs an effect
descriptor, requests two RGB rows, draws a random byte, submits the descriptor
and returns one. The original body is in `conker/asm/EEE70.s`.

The first entry in `D_8008AA00` points to this function. The table is loaded by
`func_1514C2F0`, `func_1514C470`, `func_1514C678` and `func_1514C858`; the
`func_1514C2F0` indirect call window shows fifteen argument words and uses the
return value. Other dispatch windows and indirect or external callers still
need qualification. The descriptor layout resembles the one in
`func_15149EC4`, but each initialized field, helper effect, access order and
floating-point conversion needs independent verification. The double constant
at `D_800A0228` contains `0.1757`.

The ignored private probe
`conker/build/game-next-15015FBC-private/screen_150C1E34.py` compiles a first
semantic reconstruction without modifying production source. IDO emits 71
words, compared with retail's 75; naive positional comparison reports 67
differences. All three other functions in the owner object and compiler
diagnostic rows remain unchanged in this initial probe. These observations are
not a byte match or a semantic qualification.

Next, inspect every dispatch window and the helper contracts; build a retail
guest oracle and native checks for initialized descriptor fields, helper call
ordering and valid floating conversion boundaries. Compare relocation-aware
instruction alignment and both padders; then perform actual Make, strict image,
protected-data, production recount and documentation gates before installing
or claiming the function. Floating values outside the defined C conversion
range, descriptor padding, helper internals and gameplay remain unqualified.
Game progress stays **3,682 / 4,840 (76.07%)**; 190 exact functions remain to
reach 80%.
