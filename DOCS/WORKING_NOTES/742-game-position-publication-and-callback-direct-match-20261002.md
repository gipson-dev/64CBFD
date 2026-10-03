# Game Position Publication and Callback Direct Match

Date: 2026-10-02

## Scope

Recovered `func_15163504` in `conker/src/game_18D770.c`, replacing its
zero-return placeholder and obsolete attempted body. Its complete retail slot
is `0x15163504..0x151635A8`: 41 words / 164 bytes, at ROM
`0x1909B4..0x190A58`. No shared type layout was changed.

## Recovered Contract

- Record offset `0x14` points to the destination.
- Offsets `0x18`, `0x1C`, and `0x20` hold three independent float pointers,
  not one contiguous vector. The adjacent constructor `func_15163414`
  corroborates this pointer payload.
- Each pointed-to float is truncated to a signed word and its low halfword
  is published at destination offsets `0x0E`, `0x10`, and `0x12`.
- The signed selector byte at `0x24` is read after publication. Sentinel
  `-1` skips dispatch and returns one. Otherwise retail reads the selector
  again, calls `D_8008B36C[selector]()` without explicit arguments, and
  returns the callback's actual signed result.
- This routine does not release the record. The preceding timed lifecycle
  routines have a different contract.

The existing heterogeneous `struct225` payload types remain unchanged.
Local pointer overlays recover this routine's guest interpretation without
changing unrelated consumers. Explicit volatile selector reads preserve the
two retail loads.

## Matching Evidence

An initial semantic body retained return-merge and scheduling differences.
Explicit selector reads with assignment of the callback result reduced the
remaining difference to five words. Returning directly from the callback arm
recovered retail's return allocation and cleanup schedule.

The final body matches all 41 words directly from C: no expected-word guards,
instruction insertions, omissions, or compiler override were added. The next
function `func_151635A8` remains at `0x151635A8`.

Independent linked-byte comparison against the pristine ROM confirms the
164-byte span. SHA-256:
`533f7735942b07c385e50a1ff0395c19d9d1fd3dbe13e9883db2a5569c787a6b`.

## Verification

`tools/tests/test_game_position_publication.py` compiles the actual recovered
body with a host-native semantic payload and mock callback table. Six tests
cover separate source pointers and signed truncation, sentinel publication,
publication before dispatch, positive/zero/negative callback results,
callback mutation, and low-halfword narrowing. Destination sentinel bytes
also check that publication does not overwrite neighboring storage.

The host fixture models pointer semantics, not guest byte layout. It does not
establish shared-header host ABI portability, exceptional float conversion,
out-of-range signed-word conversion, or gameplay qualification.

- `make -C conker NON_MATCHING=1 all match-progress -j4`: passed.
- `python3 -m unittest discover -s tools/tests`: all 53 tests passed.
- `make tools-check`: passed.
- Entire linked `.init`: 164,048 bytes, byte-exact against retail.
- Entire linked `.init_data`: 17,376 bytes, byte-exact against retail.

Init code SHA-256:
`34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf`.
Init initialized-data SHA-256:
`a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239`.
These checks concern linked code/data, not BSS, runtime behavior, or a full-ROM match.

## Progress and Resume

Conversion totals are unchanged: 5,461 / 6,042 C rows. Total exact C is now
3,245 / 5,461 (59.42%); Game exact C is 2,572 / 4,788 (53.72%). There are
2,216 different C functions and zero address drifts. Init remains 492 / 492
exact C rows with 47 retained assembly rows.

The supported compiler-generated Init queue is complete. The MMIO and bitmap
leaf experiments remain deferred as documented in Notes 737 and 738; SDK,
hardware, shared-frame, and register-contract assembly remains retained.

Next ordinary Game target: `func_151A4900`, 39 words / 35 real differences.
Keep `func_150A76F0` in its handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue. No sibling host-port
source, build, or runtime artifact was changed.
