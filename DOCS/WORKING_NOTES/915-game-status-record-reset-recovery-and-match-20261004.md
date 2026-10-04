# Game Status Record Reset Recovery And Match

Date: 2026-10-04. Starting HEAD: `2d008f70`.

## Recovery

Finish the pending `func_151E5034` recovery in
`conker/src/game/generated_20AE20.c`. Replace its false zero-return placeholder
with the retail record reset. A local `StatusReset20AE20` view describes only
the accessed prefix; its rounded size 0x48 is not a claim about the complete
record allocation or all fields used elsewhere. Shared pointer declarations
and neighboring routines remain unchanged.

Retail reloads `D_8008FDD4` before every store. The C body preserves the
repeated pointer accesses rather than snapshotting the record in a local.
The compiled body reproduces all sixteen reload/store pairs in retail order:

| Store type | Record offsets |
| --- | --- |
| Positive-zero float word | 0x00, 0x04, 0x10, 0x14, 0x18, 0x1C, 0x0C, 0x08 |
| Zero halfword | 0x20 |
| Zero byte | 0x2B, 0x3E, 0x3F, 0x41, 0x43, 0x44, 0x2A |

The full interleaved order is asserted by the new test against retail words,
not inferred from the grouped table. No null gate, whole-record memset or
semantic return value is added. Retail leaves `$v0` holding the global cell's
address rather than setting a result; the recovered interface is `void`.
Both current C callers ignore a return value. There is no shared header
declaration to change.

## Exact Match

The complete 37-word / 148-byte slot at `0x151E5034..0x151E50C8` matches
retail directly from C, with no target instruction guards. Next entry
`func_151E50C8` remains at `0x151E50C8`. Production-slot SHA-256:

`845de5f5095fc8fe825cc13824bc15c98e26df9d86161180294a7ca306dc6a21`

The focused test independently extracts the production typedef/body, compiles
with IDO O2/g3, links the global relocation at its retail address and compares
the whole slot against both original assembly and the pristine image.
Its linker script explicitly uses four-byte subalignment: a default linker
otherwise inserts twelve leading bytes to align this isolated input section.
No instruction normalization or production padding tool is used by that test.
Only trailing object alignment bytes may be zero padding after the full slot.

## Fresh Verification

```sh
make -C conker build/src/game/generated_20AE20.c.o
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_status_record_reset tools.tests.test_game_menu_state_reset -v -f
```

Object dependency check and production ELF link/progress refresh succeed.
An independent matcher-parser extraction verifies all 148 linked bytes,
the target and next-entry addresses, and absence of target CSV guards.
The existing duplicate recipe warning remains unchanged.

Nine focused tests pass in 0.429 seconds, no skips. The four new tests cover:

- Original complete slot and all sixteen ordered pointer reload/store pairs.
- Local-view member offsets and 0x48 layout under 32-bit compilation.
- Raw positive-zero bits, untouched bytes and surrounding sentinels for four
  seed patterns, repeated reset after mutation, changing the selected pointer,
  preservation of the previously selected record and of the pointer cell.
- Independent warning-clean IDO compilation and linked byte equality, no guards.

The neighboring menu-reset tests cover the same global pointer's separate
call/mutation behavior. Host fixtures do not qualify deliberate state/global
alias corruption, invalid/null pointers, concurrency, MIPS hardware or gameplay.
Exact guest instructions establish the retained reload schedule; no new guest
interpreter or runtime fallback is introduced. Tool and whitespace checks pass.

## Fresh Aggregate Snapshot

This was already counted as a C placeholder, so conversion totals do not rise.
The fresh current-worktree matcher reports:

| Section | Converted functions | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5463 / 6042 | 3272 / 5463 (59.89%) | 0 | 2191 |
| Init | 492 / 539 | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4790 / 5321 | 2599 / 4790 (54.26%) | 0 | 2191 |
| Debugger | 181 / 182 | 181 / 181 (100.00%) | 0 | 0 |

Game and total exact counts each increase one from the previous README snapshot.
README changes are limited to snapshot date and those aggregate rows. Detailed
recovery updates stay here and in the working documentation.

The fresh ELF represents the current working tree, including the preexisting
uncommitted actor changes; this is not a claim those changes are banked or reviewed.
Only this recovery, its test and documentation are included in the commit.
No ROM build, sibling-port build, Release change or push is performed.

The qualified experimental Init decoder remains unchanged at 4512 linked bytes,
528 above retail, with both full masked-CU1 corpora completed. Its fitting and
reservation/production gates remain open; this Game recovery does not close them.
