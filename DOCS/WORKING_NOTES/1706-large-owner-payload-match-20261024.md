# Owner-Linked Large Payload Match

Verified 2026-10-24. Recover `func_150CE150` in
[generated_FB600.c](../../conker/src/game/generated_FB600.c), replacing its
zero-return placeholder with a complete typed allocation/copy routine.
All 44 retail words match after twelve checked compiler-layout guards.
This is semantic guarded C, not compiler-only matching.

## Layout And Contract

VA `150CE150..150CE200`, ROM `FB600..FB6B0`, 176 bytes. Normal mixed-owner
O2/g3 profile; frame `0x918`, RA at SP+0x14. Four arguments are owner bytes,
signed 16-bit duration, byte selector and full signed category word.
Preserve all four owner neighbors and pools, including the original
handwritten 2,000-byte `func_150CE740`.

Header at SP+0x910, size eight:

| Offset | Initialized Value |
| --- | --- |
| 0, 1, 2 | active 1, callback 1, flags 0 |
| 4 | signed 16-bit duration |
| 6 | category/dispatch byte 2 |

Header bytes 3 and 7 remain untouched. Payload at SP+0x20, size `0x8F0`:

| Offset | Initialized Value |
| --- | --- |
| 0 | owner pointer |
| 4 | owner identity byte at owner+0x3B |
| 8, 0xC | `D_800A07FC`, retail 30000.0f |
| 0x10 | limit 10000 |
| 0x14 | enabled byte 0 |

Do not zero the other 2,270 payload bytes. Guest tests seed every private
byte and compare the complete copied storage. Native tests assert initialized
fields, returns and destination canaries, not portable values for unspecified
header/payload bytes. Copying those bytes is retained in emitted guest code;
no new zero-fill or helper behavior is invented.

Return NULL for NULL owner. Otherwise call
`func_1515FF74(&header, 0x8F0, selector, category)`.
It requests a `0x908`-byte record and copies all eight header bytes to
record+0xE. On allocation failure return NULL; on success copy the complete
payload to record+0x18 and return that payload destination, matching the
observed SDK memcpy result in V0. The original source's spelling is not
known; the recovery deliberately gives every C path an explicit return.

## Caller And Scheduling

The aligned ROM scan finds one direct JAL, at ROM `5490C`, and no literal
target registrations. Inspect the larger VM `func_150265CC`; execute its
actual ten-word window `15027444..1502746C` in 24 phases. It truncates and
sign-extends duration, loads the selector byte, passes category zero, and
overwrites V0 with one after the call. Parent C remains a placeholder and
uncredited; this is not qualification of the full VM or all computed calls.

The complete explicit-return source emits 46 words. A smaller privately
screened candidate fell through its non-NULL C path; do not adopt or credit
it. C's fallthrough rule depends on whether the caller uses the value;
the chosen recovery does not rely on that distinction.
See [WG14 N1570, section 6.9.1 paragraph 12](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf#page=175).

The normalizer derives a closed permutation of independent setup lifetimes
and retains the original relative order of every memory access. Carry HI16
from raw byte 56 to 32 and LO16 from 60 to 56; JAL bindings at 128 and 152
stay unchanged. After the factory, the branch-delay copy establishes V1=V0;
the payload address may use V1 in place of V0. The final copies
`V1=V0; V0=V1` are redundant on the success edge and the zero-result join.
Omit those two words, deriving both return edges to the retained epilogue.

Raw branch indices 12 and 34 originally reach 42 and 41; the latter is the
removed phi copy. Both now reach retained raw index 42 / emitted index 40,
with derived displacements 27 and 5. No inserted words or profile changes.
Twelve appended rows preserve the entire historical guard prefix.
Raw public memory, calls, FPRs, saved state and return match retail;
volatile GPRs and raw fault PCs are not equated. Fitted/original full modeled
private states and emitted access prefixes agree.

## Qualification

[Experiment](../../tools/experiments/game_large_owner_payload.py) and
[focused tests](../../tools/tests/test_game_large_owner_payload.py) reuse
the existing compiler, padder, object/pool parsers, guest oracle and native32
helpers. Both tools copies pass eight fresh pre-install and eight fresh
installed tests, no failures/errors/skips/reuse. Both shared project checks pass.

- 1,020 guest cases: NULL/failure/success, signed duration and category
  boundaries, all selector/identity bytes, provider mutations, owner aliases
  and complete poisoned header/payload storage.
- Native O0/O2/O3 trap UBSan: 3,072 allocated-storage cases per profile and
  ten effective defined wrong-C controls. Explicit returns are checked.
  Unknown header/payload contents are intentionally not asserted.
- 69 fired root-access prefix pairs, emitted guest order only; 50 complete
  raw-word/binding corruptions; one actual padder expectation corruption.
- Six independent GNU links in three layouts, including negative LO16 and
  HI16-carry boundaries. Original assembly and fitted C relocate identically.
- Connect the original 30-word factory and eleven-word forward byte memcpy
  in eight cases, visiting every helper word; only the generic allocator is
  bounded. Verify helper words against the predecessor ELF.
- Independently assemble original code; compare isolated and complete-owner
  C, guarded/padded objects and actual five-command Make. All five compact
  functions and the complete padded object agree. Isolated diagnostics empty;
  owner diagnostics unchanged. Inherited duplicate generated_12D630 Make
  warnings remain.

Raw body SHA256:
`09ad51fae08e63f2c78a773194062540f1b5250c5dba8bacc8897ae0a6d6034c`.
Retail body SHA256:
`6b1e98bf88d1d86811408d002e0323a5ac86ab6427da77651dbb84dd380bce9a`.
Full parent C, portable unspecified-byte values, hardware and gameplay are
not claimed.

## Production And Progress

Tools `455e79a07a213be27a00791a9fdd22a147367b1d` committed first.
Preserve all 1,624 older mirror dirty paths/statuses/hashes and its HEAD;
add only the two owned modules, now 1,626 dirty paths. No push or host changes.

Seal 15,994 files, 35 focused inputs and all 1,454 linker objects in native
and Linux-cache copies, using checked stdin/tar transfer without DrvFS
project reads. Production Make passes. Adopt only source, guards, target
object and ELF as four qualified overrides; linker/progress outputs remain
identical. Strict ELF delta is exactly 149 bytes: 148 target-code bytes plus
one target-size byte (12 to 176), zero exclusions or symbol cycles.
All other 6,054 bodies and all 6,055 addresses remain fixed.

All 720 protected Game-data owners / 189,088 bytes remain exact:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Adopted ELF SHA256:
`42054ab3e2fd8c1a9768693ac80b682908bce356ed2955ca907980a028c7b615`.

Fresh recount of actual adopted native ELF bytes: total **3,783/5,505
(68.72%)**, Game **3,110/4,832 (64.36%)**, Init 492/492, Debugger 181/181,
zero drift, 1,722 different. The 75% threshold remains 4,129, requiring
**346 more** exact functions. Goal remains open.

Remaining source screen: 1,593 placeholders, 120 semantic/other definitions,
nine parser misses. `func_1510D8C0` already has semantic `Gfx *` C;
`func_15014094` stays separate existing-C work. Next audit `func_150E0348`,
44 words/frame 72, including its descriptor constants, copied vector,
helper ABI and callers. Keep larger `func_1509E730`, `func_1508CAD8` and
`func_15169070` separate. Refresh the normal incremental graph after the
consumer commit and explicitly audit old-node retention; not full-corpus
extraction or old-edge preservation.
