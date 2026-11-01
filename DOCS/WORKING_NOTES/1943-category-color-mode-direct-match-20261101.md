# Category color-mode dispatcher restored directly from C

`func_151645C4` now emits all **108 retail body words and 27 bindings directly
from semantic C**, with its original 24-byte frame and three zero alignment
words. The complete 111-word slot is byte-exact, without guards, insertion,
omission or a compiler-profile change.

Production and the live Windows-checkout recount agree on **4,016/5,506
(72.94%)** total, Game **3,343/4,833 (69.17%)**, Init 492/492 and Debugger
181/181, zero drift and 1,490 different. **114 more matches** are needed for
the active 4,130/5,506 threshold. Tools are committed first at `236e090`.

## Recovered operation and ABI

Owner `game_18D770`; VA **151645C4..15164780**; ROM **191A74..191C30**.
The body ends at 15164774, followed by three alignment words. Its input is an
unsigned byte. It stores that raw byte to `D_800DCDD0` before loading the signed
32-bit category `D_800BE9F0`; nonzero values select the enabled branch.
The input is not normalized before the global byte store.

| Category | Nonzero input | Zero input |
| --- | --- | --- |
| 6 | Enable category 10, submit mode 4, restore enabled colors | Disable category 10, submit mode 6, restore disabled colors |
| 7 / 12 | No further action | Submit mode 6 and restore disabled colors |
| 11 | Submit mode 4 | Submit mode 6 |
| 41 | No further action | Submit mode 1 |
| 57 | Restore enabled colors | Submit mode 6 and restore disabled colors |
| Other values | No further action | No further action |

Enabled colors copy the three tint bytes from `D_800886F0`, then write object
components from `D_800886F4`. Disabled colors copy tint from `D_800886F8` and
write 255 to all three object components. The tint destination is the inline
RGB slot at `D_800DCD20`; a local typed view documents the shared header's
legacy pointer declaration without changing shared headers.

The source uses explicit byte fields to preserve retail's three input reads
before the tint stores. The object pointer and later source components are
reloaded for each object write. Moving category 11 before the enabled
fall-through cases recovers retail's block order and the complete direct match.
Ordinary structure assignment has a different partial-overlap access order;
it is not substituted for the recovered byte operation.

## Caller and semantic qualification

A ROM-wide census finds **three direct JAL instructions** and no aligned target
pointer literal. Each instruction is verified against its containing assembly:

| Caller | Call PC | Argument setup |
| --- | --- | --- |
| func_1500E470 | 1500E5A8 | Inverse of bit 0x80 in a pointed-to flag byte |
| func_1502460C | 15025290 | Unsigned script operand byte |
| func_1509D8FC | 1509D9AC | Full-word state equality with 6, then a byte argument |

The first site is in an ignored assembly directory and was found by the
ROM-wide scan after the initial ordinary source search. All three bounded
original windows execute: **588 cases / 2,352 executions** across retail,
raw C, padded owner and actual Make forms. The script caller replaces the
result with one; the other two restore their return address without consuming
the target's result. The recovered interface is `void (u8 enabled)`.
Whole-caller reachability and complete caller restoration are not claimed.

**4,502 guest cases / 18,008 executions** cover all 256 low-byte values,
representative full-word category boundaries, high input bits, both branch
families, three root/global rebases, two stack phases and helper mutations.
Both callees are explicit providers which record arguments, clobber caller-saved
state and can change category, mode, palette bytes and the object pointer.
Their implementations and natural gameplay are not newly qualified here.

Every body instruction is reached. Complete machine state and ordered traces
agree between all four code forms; public bytes, canaries and saved state agree
with the independent reference. Guest-only byte aliases cover overlapping tint
input/output, source components overwritten by earlier object stores, mode
overlapping the category low byte, and the first object write changing the
pointer used by subsequent writes. Native tests use separate ordinary objects.

Two effective compiled guest controls reject the structure-copy ordering and
a cached object pointer. Native32 O0/O2/O3 each pass **5,720 cases under UBSan**
and reject six compiled controls: a full-word mode parameter, missing mode
store, wrong enabled helper mode, missing category-toggle call, wrong white
component and wrong disabled tint component.

Six focused tests pass in each tools copy before installation and again after
production installation. Both shared tools checks pass. The older tools mirror
receives only the three owned modules; its unrelated edits and history remain
untouched.

## Build and image audit

The complete owner preserves **77 other raw/padded functions** and its pools,
including the preceding matrix-position recovery. All 45 existing owner
warnings are unchanged by code, message and source statement; the isolated
selected function has no diagnostics. The actual five-command Make recipe
reproduces the qualified padded object byte for byte under normal O2/g3.

The independent ELF prediction changes the complete retail slot, the existing
function-size field from 12 to 432 bytes, and one closed BFD metadata collision:
`D_800886F4` / `D_800AB494`. Both named symbol records and their consecutive
strings are reversed while every name, value and other field is preserved.
This accounts for 14 metadata bytes. First link and production reproduce the
complete prediction: **342 changed bytes and zero exclusions**.

All **6,056 function addresses and 6,055 other linked bodies** remain fixed.
All **189,088 protected Game-data bytes / 720 owners** stay exact. The guard
manifest, map and conversion inventory remain unchanged. The native checkout
receives only the qualified source, object and ELF, and its independent recount
confirms the totals above.

Raw C SHA-256:
`e14dca38ada0746ef210213b37e52f0c0a9844ab64e86b450791d02735e625b4`.
Production ELF SHA-256:
`be164b26d56a087c8d3bf4b58048def90a9040ff95f60ecadd8baaa7f16ead2f`.

```sh
python3 -m unittest tools.tests.test_game_category_color_mode_match -v
```

Evidence lives in `conker/build/game-category-color-mode-151645C4-match/`:
the 1,002-input snapshot, canonical fingerprints, caller census, original/raw/
padded/Make objects, literal first link, runtime/native receipts and installed
audits. The fresh compiled control uses a separate object and checks its code
and bindings against the pinned control, keeping preparation evidence immutable.
Failed setup runs remain separate from passing receipts; the native recount
runner's stale remaining-count expectation was corrected to 1,490 before banking.

Root README changes only its two aggregate matching rows. Documentation indexes
and the roadmap record completion. The scoped graph retains all prior nodes and
valid relationship occurrences, archiving the old integer-return references.
No Claude call, host/editor/Release change or push is made.

Next ordinary C placeholder: **func_15072208**, owner `game_981E0`, VA15072208,
ROM9F6B8, 58-word slot. It currently returns a null `struct127 *`; its original
leaf derives an actor index and scans related records. Its pointer-return
definition needs a suitable scoped source parser. Keep the parked scalar and
reference-event work private and uncredited. The wider 75% goal remains active.
