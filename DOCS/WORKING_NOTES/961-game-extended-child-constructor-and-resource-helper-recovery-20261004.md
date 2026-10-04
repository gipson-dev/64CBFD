# Game Extended Child Constructor And Resource Helper Recovery

Date: 2026-10-04

## Scope And Result

Replace two zero-return placeholders in `conker/src/game/generated_15F680.c`:
extended child constructor `func_1513264C` and resource helper `func_151336A8`.
Retain `func_15132A4C`'s exact pointer-return wrapper. No instruction guards,
data changes, compiler-profile overrides or retained-assembly conversions.

| Function | Retail Slot | C Body | C Frame | Raw Word Differences |
| --- | ---: | ---: | ---: | ---: |
| `func_1513264C` | 256 words / 1024 bytes | 255 words | 0x50 | 184 |
| `func_151336A8` | 46 words / 184 bytes | 45 words | 0x30 | 9 |
| `func_15132A4C` | 15 words / 60 bytes | 15 words | 0x28 | 0 |

Constructor retail frame is 0x48; resource helper retail frame is 0x30.
Constructor extent is `0x1513264C..0x15132A4C`, ROM
`0x15FAFC..0x15FEFC`; helper extent is `0x151336A8..0x15133760`, ROM
`0x160B58..0x160C10`. Each recovered body has one trailing zero padding word
in its complete retail slot. Both remain non-matching.

Complete production-slot SHA-256:

- Constructor: `8b6d14c3eb1958344cb8b6b07419aa58f7f376269bb1717182d3f8f879ee046a`.
- Resource helper: `b9bf8563bcb9f3774bccf5094ff9f8f46b47cc2de1d93c7b05e35831022fe287`.
- Exact wrapper: `ffae9cfd67fff9633201e9af3484a65b32dbb9f1c3222dd9170fe0fc8d43ceeb`.

## Constructor Contract

Seven arguments are descriptor, resource/view count, stored value, optional
36-byte state, extra byte count, unsigned slot byte and signed context.

The signed `D_800DC63C > 300` cap precedes descriptor reads and all callbacks.
Count 300 is allowed and becomes 301 on success. Descriptor flag 0x4000
selects record kind 0x48 instead of 0x19; flag 0x400000 selects pool 2 instead
of 1. Call `func_15167A68(kind, context, extra + 0x170, 1, slot, pool)`.
Record allocation failure returns NULL without cleanup callbacks.

Reload the descriptor's unsigned resource halfword at +0x56 after allocation.
A zero signed halfword reference count selects new-resource creation:

1. Reload the pool flag and call `allocate_memory(16, 1, 2, pool)`.
2. Node failure unlinks the record with `func_15168A9C`, frees it with
   `func_10004074`, and returns NULL.
3. Reload the resource ID and invoke actual `func_151336A8(id, node, record)`.
   Failure unlinks/frees the record, then frees the node, in that order.
4. Prepend the successful node to `D_800DC460`, update the old head's back
   link, or initialize `D_800DC464` for an empty list. Set new back link NULL.
5. Reload descriptor ID/flags after helper callbacks. Set node retention byte
   only for flag 0x100000, categories other than 0x3B/6/0x13/2, and zero
   `D_800BE616`. Leave the node's final reserved byte untouched.

A nonzero signed reference count selects existing-node reuse. Search starts
at the head with counter 100. A mismatching step decrements the counter and
follows the next pointer even when the counter reaches zero; the endpoint
then fails without inspecting its ID. Matches at positions 0..99 succeed;
position 100 fails. No invented NULL-list guard or larger search is added.
Malformed missing/null chains remain outside the qualified domain.

After either successful path, increment the freshly selected signed halfword
reference count, save the node at result+0x8C, and copy all 124 descriptor
bytes to result+0x10. Initialize result+0x134/+0x138/+0x13C to float zero,
+0x144 to one, and +0x148/+0x149 to byte zero. Compute +0x140 as the square
root of the sum of squares of the descriptor's fresh +0x34/+0x38/+0x3C reads
after the copy callback.

Copy optional state as nine words to result+0x110. Without it, initialize
only +0x110 from retail `D_800A3868` (-10000), word +0x128/+0x130 to zero
and byte +0x12C/+0x12D to zero. Preserve all other default-state bytes.
Reload/increment the global count, store arguments at +0x14C/+0x168, clear
byte +0x150 and pointers +0x154/+0x158/+0x15C/+0x160/+0x164.

A nonzero resource/view count calls `func_1515D480(resource)` for indices
zero through signed `D_80082FA0`, reloading the bound after every callback,
then calls `func_1515D440` for +0x164 even if the initial bound was negative.
Zero resource skips both view helpers. Finally clear flag 0x200000 from the
fresh result+0x60 flags and return the record. No new bound clamp is added.

## Resource Helper Contract

The local node is sixteen bytes: loaded-resource pointer, next pointer,
previous pointer, unsigned ID halfword, retention byte and reserved byte.
The loaded-resource header's first word is its data pointer.

`func_151336A8` selects `D_800A3880[index]`, calls
`func_1502B6BC(&output0, 0, &output1, 2, 9, entry)`, and writes its return
to the node before testing failure. Failure returns zero. Success passes
the resource data to `func_1510CE60(data, 0, 1, 0x3E, &D_800DC640[index])`.
Reload the node's resource/data after that callback, invoke
`func_15168E54(data, resource)`, and return one. The third incoming record
argument is unused by retail. No resource-table bounds check is invented.

## Verification

Fifteen new tests in `tools/tests/test_game_extended_child_constructor.py`
execute the actual constructor, resource helper and wrapper in 32-bit host
fixtures. They cover cap-before-dereference, flag combinations, negative extra
sizes, full-width context/value and unsigned slot arguments, partial default
initialization, optional state, list insertion, retention truth table, exact
reuse boundary, signed reference-count wrap, all allocation/load failures,
fresh descriptor/global reads, post-setup resource reload, changed view bounds,
zero resource, 234 indexed resource-helper cases and fences.

The connected test uses actual `func_150E93DC`, `func_151436B4`, pointer
wrapper, constructor and resource helper. Success follows
`ANLSTCVVVVBE`; record/node/load failure follows `A`, `ANRF` or `ANLRFF`.
It checks eleven float and two integer RNG calls, four spherical math calls,
successful initialized output and failure progress consumption. Retail's
descriptor holes and 28 extra bytes remain unspecified; their initial values
are never asserted or zeroed. As in Note 960, only compilation of the actual
child in the host fixture narrowly suppresses `-Wmaybe-uninitialized`.

Record/node allocation, cleanup, resource loading/setup/attachment, RNG,
view allocation and SDK trigonometry are explicitly opaque fixture boundaries.
Square root uses host SSE. This is not full guest differential execution,
all malformed inputs, arbitrary FPU-mode parity, downstream renderer proof or
natural gameplay acceptance.

Fresh standalone IDO O32 compilation links the real bodies, verifies complete
slot hashes/frames/differences and matches the production slots. Only recorded
internal call relocations are normalized from compact to padded addresses;
no arbitrary instruction replacement is used. Existing child tests retain
their opaque constructor boundary, with the actual constructor now qualified
separately rather than asserted to be a placeholder.

Fresh production compile/padding/relink/progress/matcher succeeds. All
**160 combined tests pass in 35.958 seconds, no skips**. Complete Init code
(164,048 bytes), Init data (17,376 bytes), and Game data (189,088 bytes /
720 owners) remain exact. Prior parent/child/position-writer identities and
exact creators/helpers/wrapper are preserved. Existing duplicate
`generated_12D630` recipe warnings and two unrelated pointer/integer warnings
in resource-owner cleanup remain unchanged.
After fixture cleanup, all 28 constructor/child tests pass again. Project tool
and whitespace checks pass; all 2,725 local links in the touched working docs
resolve. These repeated focused checks are not added to the 160-test total.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_extended_child_constructor tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_child_emission_callback tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_fill_value_mask -q -f
make tools-check
git diff --check
```

## Sibling Boundary And Next

Read-only sibling audit confirms active CMake input `recomp_out/.c` already
has recompiled constructor (line 933252) and resource helper (line 935834)
bodies. Scoped production source search finds no named overrides for them.
Child `func_150E93DC` (line 731447) remains a zero-return stub. No host
transplant, build, binary, save or frozen Release changes.

- [x] Recover the complete extended constructor and resource helper without guards.
- [x] Qualify the actual child-to-constructor/helper source connection.
- [x] Preserve retail partial initialization, failures and resource search boundary.
- [x] Fit complete slots and preserve linked Init/Game-data and prior recovery gates.
- [x] Recover loader `func_1502B6BC` (77 words) and its offset relocation helper;
  subsequently completed in [Note 962](962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md).
- [ ] Recover its lookup `func_1502AC88` (159 words) and block loader `func_1502B350`
  (86 words); unwritten metadata prevents production loading qualification.
- [ ] Recover setup `func_1510CE60` (163 words) and attachment `func_15168E54`
  (45 words), which remain placeholders.
- [ ] Pursue constructor/helper raw byte matching separately.
- [ ] Synchronize the PC child through guest/RDRAM interfaces and qualify natural effects.

Init stays 492 C / 47 assembly. Game stays 2,609 and total 3,282 byte-exact C
functions, zero drift. Both recovered routines were already counted as C
placeholders: README aggregates are unchanged, and recovery updates stay in
dedicated working docs. No complete allocation/resource/rendering pipeline is
claimed while the three deeper resource routines remain placeholders.
