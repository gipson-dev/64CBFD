# Game event-record link update match - 2026-09-26

## Result

`func_151419D0` is byte-exact across all 43 words, or 172 bytes, at
`0x151419D0..0x15141A7C`. The fresh linked matcher reports 2,661 / 5,483 exact
C functions overall and 2,093 / 4,794 in Game.

## Recovered behavior

The function operates on fields at owner offsets `0x2C` and `0x30` using a
record with endpoint identifiers at offsets `0x0` and `0x4` and selector
bytes at offsets `0x8` and `0x9`.

For event zero, matching either the first endpoint identifier or its adjacent
selector destroys the owner through `func_1516972C`. For event `0x2D`, if the
owner currently references either endpoint, the function replaces that
identifier and selector with the record's opposite endpoint pair.

The previous C expressed the two source endpoint loads independently. A
function-scope `source` lifetime shared by both event paths gives IDO retail's
`v1` allocation. Reversing the commutative byte comparison to destination
then source recovers retail's load order. Together these source changes recover
fifteen mismatched words and all later temporary-register colors.

IDO canonicalizes the final equality to `bnel a0,t2` regardless of its C
operand order, while retail uses the equivalent `bnel t2,a0`. One guarded row
at function offset `0x88` preserves that instruction. The shared patch table
now has 1,060 rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x16EE50` and pristine retail
span `conker.us.bin+0x16EE80` are both 172 bytes and compare equal. Both hash
to:

`23565b1986f5d0cdc768681a8e31d9b1cfdb6d1f9fc76330ea2eaa2a60523b68`

Changing the shared patch table triggered and passed the required
all-consumer rebuild. The focused object disassembly, linked ELF, objcopy
binary, fresh matcher, and exact span comparison pass. The outer nonmatching
build, `make tools-check`, all project-tool unit tests, and `git diff --check`
also pass.

## Sibling audit

`64CBFDOGL` contains `func_151419D0` only in generated recompilation,
configuration, and symbol artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Keep probable handwritten `func_15125628` out of the ordinary C
matching queue; raw-assembly ownership remains a separate workstream.

Continue with 25-word `func_15143874`, the next ordinary Game C row with
sixteen real differences. Establish its source, callers, and retail behavior
before changing compiler shape or adding guarded rows.
