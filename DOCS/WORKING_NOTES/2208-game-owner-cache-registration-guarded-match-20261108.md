# Owner Cache Registration Guarded Match - 2026-11-08

`func_15188810` replaces a false zero-return placeholder with the complete
owner-keyed timer update and counted buffer registration. Semantic C emits
all **79 words / 316 bytes** with retail's **0x38-byte frame**. Two checked
word guards move one private size spill from SP+0x24 to SP+0x20. There are
no register renames, instruction insertions/omissions, schedule changes or
compiler-profile changes. The complete fitted routine is byte-exact.

Production: Total **4,277 / 5,513 (77.58%)**, Game **3,604 / 4,840 (74.46%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,236**
converted functions remain different; **134** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion rows remain unchanged.

## Recovered behavior and ABI

Owner `conker/src/game/generated_1B5CC0.c`, original `conker/asm/1B5CC0.s`.
VA **15188810..1518894C**, ROM **1B5CC0..1B5DFC**. Public interface:

```c
void func_15188810(u8 *owner, s32 timer, s32 mode);
```

Walk `D_800DF7C8` through next+0xC. For the first node whose key+0x10 equals
the owner address, compare its **signed 16-bit timer** with the complete
**signed 32-bit incoming timer**. Store the incoming low halfword only when
it is greater, then store the mode low byte. The comparison occurs before
narrowing, so an input above 32767 can produce a negative stored timer.
Duplicate keys after the first match are untouched.

If missing, allocate a **24-byte** header with `(24, 1, 0, 0)`. On success,
read the live owner type byte +4 and call `func_1502DB20(s32)`. Zero count
frees the header. Compute the low 32-bit byte size as `(count * 3) << 7`,
using unsigned count arithmetic, and call `allocate_memory(size, 1, 1, 1)`.
A failed second allocation frees the header. Distinct count and byte-size
locals naturally produce the original frame; a multiplied byte size alone
had incorrectly produced frame 0x28 and a shorter instruction sequence.

Initialize active=0, kind=3, cleared=0, recordSize=20, mode, timer, buffer,
owner key and word+0x14=0, preserving byte +5. Clear the counted buffer with
bzero, then append through `func_15188A58` using the **live global head**.
Initialization, helper effects and incoming timer/mode reload order are
preserved. The count helper's unsigned-halfword table and fourteen
subtract-four types are tested, including zero and negative count outcomes;
size arithmetic retains its low-word result and bzero's signed-length gate.

The existing `ListNode15188A58` is a **20-byte prefix**, used by the exact
neighbor `func_1518894C` in `sizeof(*node)`. It is moved before both users
without enlargement. `OwnerBufferNode15188810` wraps that prefix with the
cleared +0x14 word, making the new allocation 24 bytes while preserving the
neighbor's 20-byte allocation. SDK native32 assertions verify both layouts.
The legacy insertion-helper head interface remains unchanged.

## Closed private spill certificate

All instruction/register/branch/call/field-access words match directly
except word **44** (`sw t0,0x24(sp)`) and word **69** (`lw a1,0x24(sp)`).
Expected-word guards change both offsets to **0x20**, matching retail.
This four-byte value is the allocation/clear byte size, live across the
second allocator call. Neither slot has another emitted access; its address
is not passed to a provider. Frame, saved registers, public argument homes
and the full lifetime remain fixed. A source/profile/word/binding change
rejects the certificate instead of applying an open-ended patch.

Retail and fitted code agree in literal private bytes and fault state.
Raw C comparisons use an explicit initial/final four-byte **slot permutation**
(SP+0x20 exchanged with SP+0x24), including read/write event addresses.
Raw physical private-byte identity and portable C access to private frame
aliases are not claimed. Public heap aliases are checked independently.

## Qualification and bank

- **115 frozen inputs** pin the complete owner, all headers/compiler stages,
  ROM, layout, guards, caller sources and original helper implementations.
- **14 raw and padded neighbors** and pools are unchanged. Both whole-owner
  padders agree across 15 functions. The actual three-command Make recipe
  reproduces the qualified owner under existing O2/g3, with **zero C diagnostics**.
- Independent prediction of the **entire ELF** permits only this function
  body and its size 12 to 316. The CSV appends only two checked guards.
  **237 changed ELF bytes, zero exclusions, no symbol-name reorder**. All
  **6,052 function addresses** and every other body remain fixed. All
  **720 protected owners / 189,088 data bytes** remain exact. Progress CSV,
  Makefile and retail input/binding data remain unchanged.
- The **19-word original packed-state caller** `func_1506EE60` is executed
  completely across 30 cases, including its alternate removal path. Four
  additional original call windows execute 24 cases, qualifying all five
  aligned call sites, timer 100 setup where present, signed mode byte and
  ignored return. Complete execution of those larger parents is not claimed.
- **2,168 cases per body** cover all 256 owner types and mode bytes, signed
  timer boundaries, first duplicate match, empty/existing lists, allocation
  rollback, retained bytes, live head/type mutations and private incoming homes.
  All 79 literal words match; word 24 is a dead duplicate next load, while
  the other 78 words are visited. **16 heap alias cases**, **100 fired fault
  prefix triples** (13 delay cuts) and **six independent GNU links / 51 cases
  per body** qualify the closed slot mapping and exact fitted instruction order.
- **271 connected cases per body** execute original count (25 words), allocator
  wrapper (11), bzero (40-word slot) and append (17), with the exact original
  256-byte count jump table. All five helper baselines, including free's 119
  words, are verified exact. Allocator core and free remain bounded providers.
- Native32 **O0/O2/O3 each pass 1,268 cases**, with actual C count/append helpers,
  SDK types, prefix/wrapper assertions, all node fields and complete 4,096-byte
  buffer checks, and trap UBSan. All **17 compiled incorrect implementations**
  fail observably in every native profile and in the guest tests.

Target compile/link/progress and production recount pass. The existing
whole-ROM checksum mismatch still makes `make all` exit 2. Fresh target-suite
checks run in both tools environments before and after installation. Shared
smoke is fresh in both; three unchanged regressions per copy are reused only
by exact helper/test fingerprints, not reported as fresh executions.

Receipts: `conker/build/game-owner-cache-registration-15188810-match/`.
Sibling tools retain all 2,434 inherited dirty paths; host Release stays frozen.
Tools commit before the consumer pin. Scoped Graphify refresh retains old
unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_15188E48**, the measured 79-word unmatched cache-buffer updater
in the same owner. Audit its captured kind, live owner/count/global page,
copy loop and state-byte advance before adoption or credit. The 80% goal stays active.

Production ELF SHA-256: `26f95da8368e64e5e840f34b3cefab8956683c2fed1ef96e56a57e99cb19d7ce`.

Guard SHA-256: `49031750032f08677fbfd1270972d9e358fc6284dcda9e3fdf72a57b52eb93d7`.
