# Game linked actor-effect updater match

Date: 2026-11-13. `func_151D2C40` replaces a zero-return placeholder in
`conker/src/game_1FFF60.c`. Its 91-word retail body occupies
`0x151D2C40..0x151D2DAC`, ROM `0x2000F0..0x20025C`.

The updater validates its linked actor's state, identity, matrix pointer and
type, then transforms a point. It may decrement a timer, call a release
callback and destroy the effect, or call an update callback and copy the
resulting point. The timer subtraction models the retail 32-bit wrap and
16-bit truncation. The three output words are copied without altering float
bit patterns; the GNU build uses a may-alias type for that copy. Conversion
to signed 16 bits relies on the tested compiler's narrowing behavior.

Descriptor slot `0x3D` references the function at data address `0x8008C10C`.
The bounded caller window in `func_151670C0` performs the indirect call with
the effect node and saves the next node in the call's delay slot. This is a
bounded call-site qualification, not whole-dispatcher or gameplay testing.

IDO directly emits 89 of 91 retail words. Two expected-word guards restore
the order and register assignment of adjacent identity-byte loads. The raw C
does not establish the retail memory-fault order; the guarded guest stream
does so for the exercised fault prefixes. No instruction is inserted or
omitted.

Tools commit `acbf12e` supplies reproducible checks:

```sh
python3 -m unittest tools.tests.test_game_actor_linked_effect_151d2c40_match -v
```

The guest model checks 2,880 cases for each of retail, unguarded C and the
guarded stream. The native32 test checks 2,880 cases at each of O0, O2 and O3
with trapping UBSan and rejects five deliberately incorrect variants. The
suite also covers 48 bounded caller cases, 61 retail/guarded memory-fault
prefixes, eight GNU links across four layouts, and eight stale word or
relocation rejections across both padders. The stack-overlap sweep has 362 of
390 cases where all streams terminate, and the actor/effect overlap sweep has
750 of 774; these terminating cases agree. The remaining cases are unresolved,
not counted as passing. The transform helper and callbacks are modeled; these
results do not establish hardware or gameplay behavior.

The complete mounted suite initially reported a test-label typo; the corrected
guard test passed separately. The complete mounted suite passed after
installation. The independent sibling overlay passed all ten checks before
and after installation. `make tools-check` passed; the sibling checkout's
2,434 pre-existing dirty paths were preserved.

The production Make build and independent whole-image audit account for
267 changed bytes with zero exclusions. Only this function changes among
6,051; every function address and all 189,088 protected Game-data bytes
remain fixed. Only `game_1FFF60.c.o` changed among 698 fingerprinted linked
objects. The conversion CSV and prior guards are unchanged. The scoped
Graphify refresh retained all 60,066 prior node IDs and was not a full-corpus
extraction.

Fresh production recount: Game **3,776 / 4,843 (77.97%)**, total
**4,449 / 5,516 (80.66%)**, zero address drift. **99** more Game matches are
needed for 80% at the current denominator.
