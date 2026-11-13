# Game script-node acquisition match

Date: 2026-11-13. `func_1509B5AC` replaces the placeholder in
`conker/src/game_C8950.c`. Its 86-word retail slot spans VA
`0x1509B5AC..0x1509B704`, ROM `0xC8A5C..0xC8BB4`.

The recovered routine looks up a signed-halfword script ID, optionally rejects
the full signed 32-bit ID through the state bitmap, and acquires and inserts a
node if none exists. A newly acquired node may run the script interpreter
under color `0x06000000`, then receives the original `0x4000` flag according
to the force argument and node flags. An existing forced node with flag
`0x1000` and without `0x0800` has its recorded tail zeroed. The bitmap and
node flags are read again where the retail helper calls permit mutation.

The previously `void` creator `func_1509B8FC` now returns the node pointer
from `func_1509B950`. This corrects a C interface: the retail acquisition
routine immediately consumes the creator's V0 result. The creator's complete
21-word compiled body and all 16 other owner functions remain unchanged.
Note 1952's statement that the creator's outgoing V0 was unconstrained was
limited to its then-tested callee boundary; the newly examined upstream caller
demonstrates that the pointer return matters. The handwritten interpreter
`func_150ADAF0` remains a bounded provider in these tests, not a recovered C
implementation or a gameplay claim.

The compiler emits the retail frame and 86-word extent. Six relocation-aware
expected-word guards restore two closed bitmap-address register allocations;
four retain HI16/LO16 bindings. No words are inserted or omitted. The real
generic padder reproduces every retail word and binding, and rejects 12
individually corrupted instruction or relocation preimages. Eight GNU links
verify the original and padded bodies across four independent symbol layouts.

Tools commit `09ddc76` supplies the reproducible suite:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_script_node_acquire_1509b5ac_match -v
```

The suite runs 2,240 guest cases per raw/retail body, covering all 86 words,
and 128 node or bitmap stack-alias cases. It compares 88 retail/padded guest
access-fault prefixes, including eight delay-slot cuts. The complete original
table caller `func_1509B4A0` executes 96 cases per retail, raw, and padded
body; ROM census finds a second direct call in `func_1509F850`. Native 32-bit
O0/O2/O3 each pass 2,240 cases with trapping UBSan, and six semantic mutations
are rejected. Provider effects and fault models are bounded; these checks do
not establish live gameplay behavior.

All eight checks passed in the mounted tools checkout and in an isolated
sibling overlay. The latter uses mounted fallbacks and is therefore a hybrid,
not a complete independent checkout run. The sibling's 2,434 pre-existing
dirty paths remain unchanged. The shared project tool checks also pass.

The production Make build and independent image audit pass. Exactly 256 ELF
bytes change with zero exclusions; only this function changes among 6,051
linked bodies, every address remains fixed, and all 189,088 protected Game
data bytes remain identical. Of 698 fingerprinted linked source objects,
only `game_C8950.c.o` changes; the debugger object remains identical. Existing
guard rows and conversion CSV bytes are preserved. The scoped Graphify refresh
retains all 60,040 previous node IDs and does not claim full-corpus extraction.

Fresh production recount: Game **3,766 / 4,843 (77.76%)**, total
**4,439 / 5,516 (80.47%)**, zero address drift. **109** further Game matches
are required to reach 80% at the current denominator. Continue the Game goal.
