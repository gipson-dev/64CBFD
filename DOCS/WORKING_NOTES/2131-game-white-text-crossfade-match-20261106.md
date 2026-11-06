# White text crossfade match

Date: 2026-11-06. Continue the active 80% goal from consumer
`62440e34d314e42d9275e0b08fb4024b05cea192` and mounted tools
`9a33c7db280faeb9ce323b963547a75b9f586c11`, following
[Note 2130](2130-game-actor-spatial-query-match-and-dependent-abi-20261106.md).

## Recovered callback

`func_150D0534` in `conker/src/game/generated_FC5F0.c` now matches its
complete **71-word slot**, VA `0x150D0534..0x150D0650`, ROM
`0xFD9E4..0xFDB00`. Its executable body is **70 words / 280 bytes**,
ending at `0x150D064C`; the original final zero alignment word is preserved.
The retail frame is `0x30`, including S0, RA and the incoming owner home.

The unary `s32(u8 *)` callback resets the signed payload countdown to 20
when owner byte `+0x30` has bit 0 set. A positive count yields byte opacity
`count * 12`, complementary opacity `255 - opacity`, and a truncated byte
update `count - D_800BE9E4`. Unsigned subtraction preserves the target's
word wrapping for extreme ticks. A nonpositive signed count draws only
the current text at full opacity. The routine always returns one.

Both passes use white RGBA and position/format arguments `(20, 20, 128)`.
The first selects the current buffer through descriptor index `+0x15`;
the second selects `index ^ 1`. The payload pointer is owner `+0x48`,
buffer pointers are owner `+0x40/+0x44`, and the descriptor starts at `+0x28`.
The descriptor's existing typed layout and the helpers' existing prototypes
are reused. No helper definition, shared header or compiler profile changes.

Opaque providers may change the index, buffer pointers and timer. The first
descriptor is reloaded after its color call; the second descriptor is captured
before its color call and retained in SP+0x20. Addressing the parameter home
preserves these retail reloads. The simpler direct-owner control loses that
home and emits only 64 words/frame0x20, so it is rejected.

The current qualified colored fade `func_150D01A0` supplied the useful source
shape. The older white-fade probe remains a rejected historical candidate:
its 69-word/no-S0 body and 62 differences are not reused as matching proof.

## Closed scheduling guards and owner audit

The existing O2/g3/MIPS2/O32 profile emits all 70 semantic words, including
the retail saved-S0 lifetime. Only six words differ, at offsets B8..CC:

| Offset | Compiler | Retail |
| --- | --- | --- |
| B8 | load owner from SP+0x30 | set A0 to 255 |
| BC | add descriptor offset 0x28 | load owner from SP+0x30 |
| C0 | save descriptor at SP+0x20 | set A1 to 255 |
| C4 | set A0 to 255 | set A2 to 255 |
| C8 | set A1 to 255 | add descriptor offset 0x28 |
| CC | set A2 to 255 | save descriptor at SP+0x20 |

Six expected-word guards close this permutation. Every retail instruction
has a compiler origin, with no omission, insertion, call substitution,
branch retarget or frame change. None of the six moved words has a relocation.
The counter HI/LO pair and four renderer calls retain all six bindings at
identical offsets. Original CSV bytes remain an exact prefix of the new file.

The complete owner has 25 functions. All **24 raw and padded neighbors**,
all raw/padded allocatable pools and register metadata remain identical.
The existing `RETAIL_RODATA_SYMBOL := D_800A0860` binding is preserved.
The copied padded predecessor equals the actual pre-install object; actual
Make later equals the predicted padded replacement and complete linked ELF.
All **107 frozen inputs** are audited; protected inputs remain unchanged.

## Qualification

Eight focused tests pass before and after installation in both actual tools
configurations. The sibling uses only an ignored overlay for the five new
modules, with its real shared helpers imported and fingerprinted. Its six
tracked edits and 2,428 untracked files are preserved. Both tools smokes are
fresh; three shared regression suites per copy are exact-fingerprint reuses
from Note 2124, separately recorded. Routine work used zero Claude calls.

- **4,600 guest cases per body** compare retail, raw C and normalized C with
  an independent external-state reference. All 256 counter bytes, flag and
  index cases, extreme tick words and mutable opaque providers are covered.
  Normalized C additionally matches complete RAM, registers, events and
  access order. All 70 body words are visited; this does not claim every
  branch direction, since inverse zero is unreachable with scale 12.
- **156 private clock/stack alias cases per body** and **51 fired access-cut
  prefixes** compare literal retail/normalized state. Incoming-home redirects
  distinguish the late first descriptor from the captured second descriptor.
  The raw body has external-state equivalence, without a raw fault-order or
  portable-C stack-alias/fault claim.
- **168 original-caller cases per body** exercise all 35 dispatcher words
  across successful/skipped callbacks and the false-return expiry control.
  Positive paths cover 31 words; the old stub reaches the four expiry words.
  The callback is registered at **D_800888A0[2]**, ROM `0x22D368`, with no
  direct JAL or tail call in the aligned ROM census. The current C caller
  binds to the identical original 35 words, so this also covers its body.
- **1,024 cases per body** connect the complete original 22-word color helper
  and cover every helper word. Its four byte stores and exact text-call
  arguments agree. The text renderer remains an opaque provider; its full
  rendering, variadic overreads and gameplay are not acceptance claims here.
- **Nine independent GNU links**, three entry/global-address layouts and
  **111 cases per normalized body** verify all six bindings, including the
  counter HI/LO carry boundary. Raw linker binding is checked separately.
- **61,440 SDK native32 executions** pass O0/O2/O3 with UBSan and the proper
  callback pointer. Native indices are valid 0/1; sparse full-byte guest
  indices are a separate instruction test. Seven wrong controls each fail
  with checked exit 1: unsigned counter, missing reset, wrong ticks, wrong
  scale, wrong inverse, same buffer and false return. A sanitizer trap does
  not satisfy the negative-control gate.
- All **280 raw-byte corruptions**, six binding corruptions, six stale guard
  expectations and five whole-image corruptions are rejected. The old zero
  stub is explicitly rejected by its result and absent draw calls.

The first new image assertion mistakenly compared a 70-word body with the
parser's 71-word slot. It was corrected to require the complete body plus
its one literal zero alignment word; the strict ELF predictor never excludes
that tail. This fixture correction changes no recovered C or guard words.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Actual Make compiles only generated_FC5F0 once with its unchanged profile,
introducing no C diagnostics. Keep both old-dependency flags until a deliberate
broader rebuild; unrelated object timestamps are untouched. The full ELF
matches the independent **209-byte prediction**, with **zero exclusions or
metadata permutations**. Only this body and its symbol size (12 to 280 bytes)
change. All **6,052 addresses**, conversion rows, progress.csv, Make rules and
**189,088 protected data bytes in 720 owners** are fixed. The unfinished
whole image retains its expected checksum failure and the existing duplicate
generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,200 / 5,512 (76.20%) | 0 | 1,312 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,527 / 4,839 (72.89%) | 0 | 1,312 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**210 more** matches reach the current 4,410 threshold for 80%.

- ELF: `00e9bcfb500382daa9eb5e83eefade3abebbaaf4ba16bf05c27ab70ac249e5db`.
- Owner: `1a02662264f8613a187743b1438bcfc476aac683d90fb5aa6e113fa4647e4cd8`.
- Code binary: `5db57ebb654ef592db5f9417d086c585bda57e515e60efcd5ce3373a1b4cb9d2`.
- Guard CSV: `915496ebc88595fb6fa685dd89a03b174c869de5d070398620cd74f07086abd9`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence is retained in `conker/build/game-text-crossfade-150D0534-match/`.
Graphify receives a scoped AST refresh with old-node retention evidence;
no full-corpus extraction is claimed. Tools are committed before the consumer
source, guards, documents and pin. Root README changes aggregate rows only.

Next static target: **func_1515A11C**, generated_185560, VA
`0x1515A11C..0x1515A238`, ROM `0x1875CC..0x1876E8`: 71 words/frame0x28.
The complete retail window advances two byte phases using signed velocities,
computes two coordinates through func_151423D8, advances/wraps a floating
phase through func_15144B68, then applies one sine to three output scales.
Inspect the helper return ABIs, mutable-provider reloads and callback caller
before compiling a private candidate. It remains uninstalled and uncredited.
Preserve private inputs/saves, unrelated work, handwritten func_150A76F0 and
the frozen host Release. The full 80% goal remains active.
