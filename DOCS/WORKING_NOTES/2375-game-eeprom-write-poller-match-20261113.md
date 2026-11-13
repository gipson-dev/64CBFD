# Game EEPROM write-poller match

Date: 2026-11-13. `func_151DCFD8` in `generated_20A3A0.c` replaces a
zero-return placeholder. Its 87-word body occupies VA `0x151DCFD8..0x151DD134`
and ROM `0x20A488..0x20A5E4`. The recovered `s32 (s32 mode)` interface and
0x28-byte frame match the original. Two relocation-aware guard rows select
retail's low-clock-word symbol alias; both object padders reproduce the retail
body and bindings. The other owner function, normalized constant pools and
compiler diagnostics remain unchanged.

The poller returns zero when there is no pending request or no timer message.
After receiving a message, it clears the pending request and count on completion
or write failure. A successful write advances the address and buffer by one
eight-byte block, subtracts eight from the remaining count, and arms the next
timer using the recovered 64-bit clock calculation. It returns one even if
the modeled timer setup reports an error, as the retail body ignores that
return. A request whose remaining count just reached zero is cleared on a
later received message.

Tools commit `f006687` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_eeprom_poller_151dcfd8_match -v
```

An independent guest model passed 2,880 cases per stream across retail,
raw C and both padded bodies, with every retail instruction visited. It covers
queue results, write results, count boundaries, clock values and provider
mutations. Complete original request and block-read callers passed 16 and 24
cases per stream respectively with the poller connected. Selected access-fault
prefixes agree across retail and both guarded streams. Native 32-bit tests
passed 1,280 cases at each of `-O0`, `-O2` and `-O3`, with UBSan and eight
effective negative controls. Twelve GNU links across three layouts verified
retail, raw and padded target words at the tested clock boundaries; an expected
raw alias carry discrepancy did not reproduce for this function. The mounted
suite and staged sibling dependencies passed; pre-existing sibling changes
were preserved. The project tools check and 11 focused padder tests passed.
All EEPROM, queue and timer providers and buffers in these checks are modeled:
no real save, EEPROM, hardware or gameplay acceptance is claimed.

Production Make and the independently audited shadow have identical owner
objects and linked ELF. The strict full-image comparison accounts for 271
changed bytes with zero exclusions; only this function changes among 6,051
functions. All function addresses and 189,088 protected Game-data bytes are
unchanged, as are the other 1,453 linked objects and conversion rows. Two
checked guard rows were appended; existing guard rows and layouts are intact.

A fresh production recount reports Game **3,760 / 4,843 (77.64%)**, total
**4,433 / 5,516 (80.37%)**, zero drift, and **115** further Game matches
required for 80% at the current denominator.

The scoped graph refresh retained or relocated all 60,012 prior nodes, with
60,014 afterward and no out-of-scope removals or changes. Its fail-closed
path retained 31,816 existing nodes; it was not a full-corpus extraction.
