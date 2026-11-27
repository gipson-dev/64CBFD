# Owner packet-pair callback guarded byte match - 2026-11-27

`func_1514D64C` replaces its zero-return placeholder with the complete
**200-word / 800-byte** owner callback in
`conker/src/game/generated_179F30.c`. VA `0x1514D64C..0x1514D96C`;
ROM `0x17AAFC..0x17AE1C`. All **13 relocation positions** are preserved.
The normalized frame is the original **296 bytes**. The complete function
is emitted from semantic C, with 44 checked compiler normalizations; there
are no inserted/omitted instructions, dummy locals or compiler-profile changes.

The actual production recount is **4,714 / 5,528 (85.27%) total** and
**4,041 / 4,855 (83.23%) Game**, Init 492/492, Debugger 181/181, zero drift,
814 different. The target adds one match after the complete acceptance gates.
All denominators and conversion rows stay fixed. The **90% goal remains
active: 262 more** matches reach 4,976 / 5,528.

## Recovered interface and behavior

The callback receives one `u8 *owner`. The 58-entry retail callback table is
pinned against ELF and ROM; its slot 12 is the sole aligned pointer literal
to this routine, at ROM `0x22F560`. No aligned direct J/JAL pattern or interior
entry was found. The complete original 109-word `func_1514D15C` dispatcher
ignores the callback return, supporting a `void (u8 *)` callback interface.
An original historical C return spelling is not proven. The retail and
normalized machine code leave the final spawn result in V0.

The recovered C builds two packets with the existing local packet types:

| Object | Extent | Retail SP offset | Important contract |
| --- | ---: | ---: | --- |
| Runtime | 32 bytes | `0x54` | Six float words, owner pointer, kind, live identity and mode |
| Descriptor | 88 bytes | `0x74` | Type 3, flags `0x401`/`0x12012`, red/opaque color, zero vector |
| Source | 92 bytes | `0xCC` | Sizes, live coefficients, scale and tail bytes; helper writes byte `0x58` |

The first source sizes are `(28, 28, 4, 17)`; its runtime vector is
`(0, 0, 25, 0, 0, 75)`, kind 43 and mode 1. The second source sizes are
`(30, 30, 10, 16)`; its runtime vector is
`(0, 10, -70, 0, 20, -140)`, kind 5 and mode 0.
Each factory result is attached unconditionally, including NULL, under keys
9 and 10. The last call submits kind 5 with the current runtime vector and
the full original 16-argument interface.

The identity byte at owner+`0x3B` and coefficient globals are read again after
opaque calls. Unwritten packet bytes are preserved. Existing shared field
names `zero10`/`zero14` are historical names; this callback supplies nonzero
coefficient values to those fields. The existing types were moved unchanged
before the callback, rather than duplicating or shrinking their storage.

`func_15189FF0` is the already restored 41-word helper. It writes source
byte `0x58 = 0x0B`, calls the factory, then copies the 32-byte runtime block
on success. This requires the full 92-byte source extent; an 88-byte source
would be unsafe. The helper C was frozen before candidate generation, and
its original machine code is independently pinned against ELF and ROM.

## Compiler normalization and its limits

The selected raw C has 200 words, a 304-byte frame and 44 positional word
differences. A meaningful shared packet-size scalar recovers all three
retail buffer offsets. All 77 other raw functions, their bindings and pools
remain unchanged; the existing four diagnostics are unchanged.

| Normalization | Words | Closed proof |
| --- | ---: | --- |
| Frame tail | 2 | Remove eight unused high bytes; every emitted SP access, all saved roles and every escaping packet extent remain inside 296 bytes |
| COP1 roles | 12 | One phase-two FPR bijection across MTC1/LWC1/SWC1 bit transfers; no arithmetic, comparison, conversion or FCSR instruction |
| Independent stores | 30 | Ten closed permutations of nonoverlapping SP-relative stores, with no intervening call or source/base mutation |

All 200 words are accounted for structurally, and all 13 bindings are
unchanged. The guards check both expected input words and expected
relocations. This is not a literal raw private-state or raw fault-prefix
parity claim. Raw packet/public effects are qualified through the stated
private-frame correspondence; literal complete fault states are checked
for the normalized streams against retail.

Both complete padders reproduce the same final owner object. Their before
objects also reproduce the frozen accepted owner. All 77 normalized neighbors
and pools remain unchanged. The existing classifier jump tables and neighbor
pool guard are retained, with no new table or pool payload.

## Fresh qualification

- Native32 actual C: **229,376 cases at each of O0/O2/O3**, strict aliasing,
  UBSan traps, LTO type checks and opaque noipa providers in a separate
  translation unit. All 256 identities, four NULL/success combinations,
  16 helper-mutation masks and 14 FP bit patterns are exercised. The native
  pointer/field sizes match O32; actual MIPS calling behavior is checked by
  the guest tests. MXCSR is unchanged. Eight controls reject wrong size/flags,
  stale identity/coefficient, wrong key, skipped NULL attach, clearing an
  unwritten byte and the wrong final vector. A signal/trap is not a passing
  negative control.
- Guest: **2,560 cases per stream**, four streams and two helper modes,
  **20,480 runs**. All 200 target words, the actual 41-word wrapper and all
  11 original `memcpy` words execute. Independent byte-offset packet and
  public-effect references agree. **633 normalized fault-prefix triples**
  compare complete private state.
- Caller: **734 cases / 5,872 runs**, two parents, two normalized children
  and two helper modes. All 109 parent words and all 200 child words execute;
  3,840 target callback entries cover the three selected routes. Three child
  return poisons are ignored. Classifier/selector providers are controlled
  interface fixtures; actual gameplay route reachability and the unfinished
  538-word grandparent are not claimed. Two comparison controls are effective.
- Boundaries: **400 word mutations**, **26 binding mutations**, 88 unexpected
  guard-binding rejections and 88 visible missing-guard checks. Twenty GNU
  links cover five construction routes, independent symbol groups and signed
  HI16/LO16 carry boundaries. Both oversized variants are rejected.
- Actual Make: the three-command owner recipe produces the same complete
  padded object as the independent padders, without a profile change.
- Independent full image: frozen before C plus the complete original ASM
  predicts the linked result without candidate bytes or guards in the
  reference. Production equals the entire predicted ELF, **656 changed bytes,
  zero exclusions**. All 189,088 protected data bytes across 720 owners remain
  exact. Conversion rows, unrelated bodies, addresses and extents stay fixed.

The first packaged runner isolated Python's installed user site too strongly,
then a configuration-alias shadowing error was found in its boundary module.
Both failures are retained as rejected receipts. The corrected package uses
an explicit tools root, no inherited PYTHONPATH and a closed import audit.
Only successful complete fresh suites are acceptance evidence.

| Phase | Elapsed | Fresh tests |
| --- | ---: | ---: |
| pre-primary-r3 | 237.592 s | 5 fresh / 0 reused |
| pre-sibling-r3 | 272.188 s | 5 fresh / 0 reused |
| installed-primary-r3 | 232.569 s | 5 fresh / 0 reused |
| installed-sibling-r3 | 280.556 s | 5 fresh / 0 reused |

All four complete suites pass, with 327 primary/328 sibling tools imports
(the extra sibling import is its empty namespace marker), 243 identical tool
data inputs and ten independently copied task files. Reports and dependency
hashes agree. Shared `make tools-check` also passes with the same tools code.

Tools packet commit: `b917b79b2f7904bfd6dfd8355fb8f0244cde53fb`.
Production ELF SHA256: `b7ad27556f67691759b8d0ffaf16b8678b9fc81a8b678e4d8ddb642164ff545f`.
Selected C SHA256: `1a0cdc9c448519996acda7e3f245ebb98ce1c13a689d7d563d66a2ea8a390eaf`.

Graphify receives a scoped AST refresh and retained-ID/qualification audit
before the committed bank is sealed. Full-corpus re-extraction is not claimed.


## Preserved scope and continuation

The dirty real `64CBFD Tools` checkout is preserved; the second suite uses
an isolated dependency snapshot and ten independently copied task files.
The snapshot has 4,199 input fingerprints and 3,763 frozen copies. The
additional 612 copies seal already fingerprinted tool dependencies, rather
than adding matching credit.

One bounded packet-only Claude Pro advisory was used for the frame question,
with tools/MCP disabled and no automatic retry. Its proposed aggregate
alignment explanation was not confirmed; typed/byte views and array controls
did not improve the frame. The adopted source and normalization are supported
by the independent compiler, structural, native, guest, caller and image
evidence above.

The inspected host-port generated file
`64CBFDOGL/recomp_scene/cd64_out/func_1514D64C.c` remains an empty stub.
That is a read-only applicability observation, not qualification of its active
host implementation. No source was transferred, no host build or launch was
performed, and Release remains frozen.

Continue from the sealed accepted baseline with another ordinary unmatched
Game function. Keep custom/shared entries out of ordinary short-function
screens: `func_150AE280`, `func_150183D0`, `func_150A613C`,
`func_150A76F0`, `func_151F8870`; `func_150A6760` also requires its shared
decoder entry `func_150A67D0` ownership audit. No pushes or subagents.
