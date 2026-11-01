# Lifetime, callback and fade dispatcher restored

`func_15154C90` now has a complete semantic C implementation in
`conker/src/game/generated_17CAF0.c`. All 60 linked words and five relocation
bindings match retail after seven checked private-byte-spill/register-role
guards. There are no inserted or omitted instructions. Its actual interface
is `void func_15154C90(u8 *owner)`; the former zero-return placeholder gave
the wrong return contract.

The normal production build and an independent Windows-consumer ELF recount
establish **4,002 / 5,506 (72.68%)** exact C functions, Game
**3,329 / 4,833 (68.88%)**, zero address drift and 1,504 still different.
Init remains 492/492 and Debugger 181/181. The conversion inventory CSV is
unchanged. The 75% goal remains active: **128 more** exact functions are
needed to reach 4,130/5,506.

## Recovered behavior

The owner supplies signed lifetime at+0x22, unsigned flags at+0x24, signed
fade threshold/rate at+0x26/+0x28, current byte at+0x2E and method byte at+0x68.
Flag `0x1` enables timer subtraction by signed32 `D_800BE9E4`. The subtraction
is explicitly unsigned32 before retaining low16, avoiding signed32 overflow
at extreme deltas. A negative retained lifetime marks the owner expired.

The method is masked to its low nibble. A nonzero method is called through
`D_8008ACC8` only while not expired; its zero word result requests expiry.
The callback can mutate the owner. Flags, lifetime, threshold, rate and byte
are consequently read live afterward, rather than cached before the call.

Flag `0x8` enables the fade comparison. If lifetime is below threshold, its
signed16 product with rate is retained as signed16 and compared with the
unsigned current byte. A smaller value is stored as low8, including negative
products; adding a zero clamp would change retail behavior. Finally, expiry
calls `func_1516972C(owner)`. The two signed16 multiplicands fit signed32.

## Actual callback registration and void return

Physical Game-data mapping is ROM 0x2275E0 -> VA 0x80082B20. The only aligned
function pointers occur at ROM 0x231114 -> VA 0x8008C654 and
ROM 0x23124C -> VA 0x8008C78C. These are the column 0 callbacks of
`D_8008B4A8[87]` and `[93]`, using the existing 0x34-byte `struct115` stride.
Its callback field already has a void interface. There are no aligned direct
JAL references to this routine in the supplied input.

The complete original 74-word `func_151670C0` parent calls column 0, saves the
next list cursor before the callback and reloads that live cursor afterward.
It does not consume the callback's V0. Both category slots and both rows are
exercised with four separately forced return words: 0,1,0x80000000,0xFFFFFFFF.
The single-node cases cover 73 parent words; two-node traversal reaches the
remaining branch-delay word, establishing all 74. The callback's V0/V1 are
therefore dead at the parent continuation. Complete cleanup and gameplay are
not inferred from these tests: callback methods and release remain explicit
bounded ABI services.

## Closed guards and guest qualification

The compiler emits all 60 words with the original 32-byte frame and saved RA
at SP+0x14. The seven guards affect offsets 0x68,0x7C,0x94,0x9C,0xB0,0xB4,0xB8.
The first pair maps a private expired-byte spill/reload from raw SP+0x1F to
retail SP+0x1B. Outgoing argument homes stay at+0..0xF; the retained owner
home remains at+0x20. The other five form a closed V0/V1 duration/product
role exchange, including commutative unsigned multiplication. There is no
arithmetic algorithm or branch-control normalization.

Both fade instruction windows pass all 65,536 low16 patterns, totaling 131,072
executions, with identical ordered accesses, public memory, HI/LO and live
registers. The complete normalized unrelocated payload equals retail and
retains all five bindings. Another 101 fired access prefixes pass with the
explicit private-byte mapping. These qualify emitted guest order, not
portable C fault semantics.

The full raw-C/retail suite exercises 1,200 cases/2,400 executions and reaches
all 60 root words. It includes signed timer boundary classes, wrapping deltas,
method and expiry gates, signed byte limiting, zero/nonzero callback words
and live callback mutations. The complete parent adds 16 cases/128 executions,
plus eight two-node executions. Sparse paths have six executions; two guest
global-overlap cases retain ordered behavior. The overlap cases make no
portable native C aliasing claim.

Eight earlier scalar-type/timer-expression screens all emitted the same
60-word/seven-difference shape. Repeating that matrix is unnecessary. The
selected source uses signed expired/opacity locals and explicit wrapping
timer subtraction. A first native negative control was rejected under
`-Werror` because an unsigned comparison with literal zero is constant;
the corrected, independently compiled control uses a volatile zero provider.
No positive source change was needed.

## Native, owner, build and image gates

Typed native32 owner objects assert every used member offset and size.
Canaries, all object bytes, exact callback selection, argument pointers and
cleanup order are compared with an independent typed reference. Four live
callback mutations distinguish cached and current fields.

O0/O2/O3 each pass 91,136 positive cases under UBSan, plus 25,600 cases for each
of ten effective compiled controls: unsigned expiry, calling an expired
method, wrong method mask, cached flags, cached lifetime, unsigned opacity,
wrong fade flag, an added negative clamp, missing cleanup and early expiry.
Each executable therefore completes 347,136 cases.

The complete before/after owner has no diagnostics, preserves all 40 neighbors
and pools, and agrees with the isolated compiler body. The actual five-command
O2/g3 Make recipe, including asm processing, compilation and padding, produces
the independently qualified object. All 14 expected-word/binding guard
preimage controls fail closed.

The independent linked image prediction changes only the target's retail
instruction bytes and symbol extent 12->240. There is no BFD metadata pair
permutation, image mask or exclusion. Production reproduces that complete
ELF exactly. All 6,055 other function bodies and all function addresses are
fixed. Protected Game data is byte-exact across 189,088 bytes and 720 owners.
Review of the entire 17,365-file predecessor seal finds only the intended
source, guard CSV, target object and ELF changes; no extra dependent object
metadata change is accepted or hidden.

Production ELF SHA-256:
`a0da86a005be514b9ea4c80fdbcd6c80e506804436f61f85566499c59ae0f9cc`.
Tools commit `b23f346` precedes the consumer pin. Seven target tests pass in
both local tools checkouts, with both shared tool checks; the installed
production target suite passes again. The older tools mirror's inherited
work is preserved and it is not committed. Nothing is pushed. The scoped graph refresh retires the obsolete placeholder
`s32` return-type edge into its provenance archive and retains every prior
valid node and edge occurrence.

## Reproduction and continuation

With the prepared target stage and consumer inputs:

```sh
python3 -m unittest tools.tests.test_game_lifetime_callback_fade_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The retained stage is `conker/build/game-lifetime-callback-fade-15154C90-match`.
`preparation.json` records the actual private Make/link;
`production-v14.json`, `production-seal-changes-v14.json`,
`installed-audit.json` and `native-production-recount.txt` record acceptance.
The canonical tools retain exact source, owner, artifact and service boundaries.

Next screen: the 60-word leaf `func_15004BF0`, which searches record byte IDs
in either direction. Its current placeholder remains unmatched. Other private
motion, path-height, gate and deferred candidates remain uncredited.
