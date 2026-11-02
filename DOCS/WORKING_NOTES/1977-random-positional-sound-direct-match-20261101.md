# 1977 - Random positional sound selection recovered directly from C

`func_151618BC` now emits all **57 retail words**, its natural **96-byte frame**
and all four relocations **directly from semantic C, with no guards**.
Actual production Make and the independent Native ELF recount confirm
**4,044/5,507 (73.43%)**, Game **3,371/4,834 (69.74%)**, zero drift and
1,463 different. Exactly one match is added. The 75% threshold is 4,131:
**87 more** matches are needed; the wider goal remains active.

## Behavior and recovered interface

Owner `game_18D770`, source `conker/src/game_18D770.c`, VA
`0x151618BC..0x151619A0`, ROM `0x18ED6C..0x18EE50`.
The recovered interface is `void(u16 volume, s16 pitch, u8 flags, s32 channel,
struct17 *position, s16 minimum, s16 maximum)`. Repair the owner-local forward
prototype, including its fifth pointer argument. Shared headers stay unchanged.
The existing audio helper prototype already has the correct narrow types.

Copy all ten signed sound IDs from `D_800A66E4` into a local 40-byte aggregate
**before** calling `func_150ADA20`. Interpret its full result as unsigned and
select the copied ID at remainder ten. Read the position live after that call,
truncate its X/Y/Z floats to signed32, then pass them through the signed16 audio
boundary along with volume, pitch, flags, fullword channel and distance limits.
The original `func_10010F88` wrapper consumes the low signed halfwords and
forwards eleven arguments to `func_10010E78`. No new null gate is added.

## Why explicit sequencing matters

The first isolated C expression was word-exact under IDO, but placed RNG inside
the first argument of the final audio call. GCC may evaluate the coordinate
arguments first. Native mutation tests exposed the difference: at one witness,
old code forwarded X=1 while retail required X=-321 after the RNG mutation.
That candidate was rejected despite its exact guest instructions.

The final C declares `SoundIds sounds` followed by `s32 selected`, copies the
table, assigns `selected = sounds.ids[(u32)func_150ADA20() % 10U]` in a separate
statement, then calls audio. This enforces the required timing in native C and
still emits the same 57 IDO words. Reversing those two declarations changes two
allocation words; both explicit index and selected-ID screens confirm the
ordering result. A memcpy-based screen instead emits 48 words/51 differences.
No shared tool, profile, Makefile, register binding or inline assembly is added.

Raw payload SHA-256:
`e8b39d79ee227ec99370a1ced79b6f0375a9ddc45cb44c031d7ee49cad0dad39`.

## Qualification evidence and bounds

- Fresh GNU links at three code/table layouts check all 57 words and four
  relocations, including HI/LO carries with table bases `0x80107FFC` and
  `0x8020FFFC`. **2,496 guest cases / 4,992 original/C executions** cover all
  ten remainders, full random-word boundaries, signed and narrow arguments,
  live pointer/home rewrites, stack phases and table/position aliasing. All
  57 words execute. Complete bounded GPR/FPR/HI/LO, memory, calls and access
  traces agree. **129 access-prefix pairs** also agree. Float inputs are finite
  with representable signed32 truncations; no portable fault, NaN, out-of-range
  conversion or hardware claim is made.
- The original **29-word `func_10010F88`** equals its retained production slot.
  **278 cases / 556 connected executions** visit every wrapper word and check
  signed-halfword coordinate consumption. Lower `func_10010E78` stays an opaque
  provider with argument/return and caller-saved effects modeled.
- A complete aligned ROM census finds **two direct JALs** and no direct J or
  pointer literal: ROM **0x18DA44 / VA 0x15160594** in `func_151604A0`, and ROM
  **0x18DEF0 / VA 0x15160A40** in `func_15160954`. J-format comparison includes
  the encoded low28 bits; an initial missing-high-nibble census was corrected.
  The original nine-word and five-word windows each pass **76 cases / 152
  executions**, covering all words and the actual outgoing stack stores and
  delay slots. The first route submits volume16000/min500/max1000; the second
  volume25000/min500/max1500. The result is not consumed in these windows;
  complete parent functions and upstream dispatch are not claimed qualified.
- Native32 **O0/O2/O3 each pass 208 cases**, with UBSan, typed audio calls and
  every public table/position word checked. Eight effective controls reject
  reading the global table live, fixed index, remainder nine, truncating RNG
  to16 bits, caching X before RNG, swapped X/Y, narrowed channel and narrowed
  minimum distance. Native omits deliberate guest-only argument-home writes.
- A native O2 fixture initially faulted at `movaps %xmm2,0x20(%esp)` with
  ESP ending in4. An owned GDB run proved misalignment in the freestanding
  entry wrapper. The local test entry now explicitly realigns its stack; all
  three profiles and all eight controls pass. Production code, shared START
  helpers and sanitizer checks were not changed to bypass this failure.
- Raw and padded full owners preserve **77 neighbors**, both **GLOBAL_ASM**
  routines and normalized pools. Its actual **five-command** Make recipe
  reproduces the qualified padded object literally. The owner has **45 old
  diagnostics and44 afterward**: only warning712 at the existing pointer
  argument in `func_151618BC(25000,0,0,0,&tmp,500,1500)` disappears. Exact warning
  key/message/source-statement accounting preserves every other diagnostic.
  Initial preparation assumptions about equal diagnostic counts and a12-byte
  predecessor were corrected from live evidence, not relaxed silently.
- Both tools copies pass **five target tests plus shared checks before and
  after installation**. Public tests freshly compile the explicitly sequenced
  C, relink all layouts and execute guest/native/helper/caller gates. Routine
  work uses **zero Claude calls**.

## Production preservation and continuation

The independent whole-image prediction starts from ELF
`83088793cafaec148da7082549742f2dd2c964ba2049ca56acb368fc8e01e6d1`.
Only the 228-byte target slot and its symbol extent **28 to228** change.
Actual Make and the private link equal the prediction literally, with **zero
exclusions**. All **6,052 addresses**, **6,051 other bodies**, complete named
symbol definitions except the declared extent, ELF length, map, Makefile and
entire guard CSV remain fixed. All **189,088 protected Game data bytes across
720 owners** stay exact. The actual pre-documentation audit reviews all
**17,723 prior sealed files**; only source, owner object and production ELF change.

Production ELF SHA-256:
`d84330cbf2a3b42de99a5866420c428b00e42a6735f43a6601c76e4235255996`.

Stage `conker/build/game-random-positional-sound-151618BC-match/` retains current
frozen inputs, **32 immutable preparation pins**, rejected source history,
private/public receipts, GDB fixture diagnosis, actual Make object/commands,
whole-image prediction, production/Native recounts, seal and handoff. The earlier
26-artifact unsequenced candidate is preserved in `before-sequencing/`.
Four public modules cover source/image, guest/helper/callers, native controls and
integration tests. A scoped 12-file AST refresh retains prior nodes and valid
edge occurrences, explicitly archiving the obsolete integer return edge.
Zero LLM tokens; no global reclustering or full-corpus extraction. README gets
aggregate rows only. Commit tools first, then consumer; no push. Unrelated mirror
work, archives, private candidates and frozen host Release remain preserved.

Next ordinary unmatched routine: **`func_15003570`**, 62 words/frame48 in
`game_305D0`, already semantically recovered as a resource-header length scan.
Audit buffer/header aliases, byte-combination order, 7,762-entry bound, live
lengths and allocator/read/free ABI before codegen changes. The small
`func_151F8870` inventory entry is handwritten with live T0/S0/S5 and a secondary
return register; it belongs to the custom-ABI assembly workstream, not this C
queue. Parked candidates and historical image fixtures require explicit rebasing.
The full 75% objective stays active.
