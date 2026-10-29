# Live record dispatcher - guarded C match

Verified 2026-10-28. Restore `void func_15183D28(void)` in
`conker/src/game/generated_1B0740.c`: VA 0x15183D28..0x15184118,
ROM 0x1B11D8..0x1B15C8, 252 words / 1,008 bytes, frame 64.
The normal O2/g3 profile emits the complete semantic routine. Its linked
retail match uses 186 direct words and 66 expected-word guards, with 65
external relocation entries. No words are inserted or omitted. Retain the
retail function name and comments describing the recovered behavior.

## Recovered behavior and interface

The dispatcher operates on eleven five-word records at `D_800DDE80`, eleven
signed status bytes at `D_800DDF68`, and eleven view words at `D_800DDF78`.

1. Expire a status of -1 or greater to -2 when its backing record or view is
   missing. Preserve live reads and the signed-byte comparison.
2. Subtract signed `D_800BE9E4` from each of the four timer bytes starting at
   `D_800DDF60`. Preserve the MIPS 32-bit wrapped subtraction, clamp a negative
   result to zero, and store the low byte. Extreme wrapped subtractions are
   guest-only probes; the native corpus stays within the signed subtraction
   range. Portable C behavior outside that range is not qualified.
3. For ready rows 0..6, call `func_15165C80` with all eight geometry arguments,
   including vertices from record word2. Ready rows 2..4 submit a second
   stream using word1 and the secondary geometry table.
4. Dispatch ready row7 to `func_1517725C(7)` and ready rows8/9 to
   `func_15179DB0`. Reread row7 after those helpers before marking row10 ready.
5. Scan all eleven live flags. For -2 with a nonzero backing record, call the
   already recovered `func_15183C28(index)` cleanup.
6. Age positive flags to zero, zero to -1, and -1 to -2. Lower values remain
   unchanged. A separate signed age counter recovers the compiler shape.

The geometry records have stride56: position at0x18, phase at0x24, extent
fields at0x28/0x2C and scale at0x30. `D_8008D318` follows the eleven primary
records at `D_8008D0B0`; the index-pointer table `D_8008D3C0` follows its three
secondary records. Byte counts come from `D_800A72E8`. Tests verify these
offsets, aliases and argument values; wider rendering semantics remain bounded.

The sole direct JAL is ROM0x46814 / VA0x15019364 in `func_15019130`.
`conker/src/game_45B80.c` now declares the dispatcher as `void` with no
arguments, matching its existing ignored-result call under the `D_800BEAC0`
gate. All sixteen caller-owner function bodies and bindings, and the complete
padded caller object, remain byte-identical. Raw caller `.mdebug` changes are
fully predicted from two decimal source-size strings and any compiler timestamp
fields; no metadata section is excluded.

## Guard derivation and relocation carry

The 66 guards come from three explicit transformations:

- Four words replace two finite eleven-row equality comparisons with retail's
  signed less-than comparisons. Both counters start at zero, advance once per
  iteration and reach only comparison values1..11.
- Three words permute independent timer address setup.
- Fifty-nine words recover the final aging loop's independent setup and
  comparisons, with a closed register-role change: pointer v0 to s1, flag v1
  to v0, and end pointer a0 to v1.

The normalizer verifies the entire raw body and bindings before applying these
derived transforms. Independent assembly of the retained retail routine then
matches the normalized body and all relocation entries.

A qualification failure exposed a real carry-boundary hazard in an earlier
scratch plan. Collapsing the delayed end-address HI16 onto `D_800DDF68` let an
intervening LO16 consume it with the wrong carry when base+11 crossed0x8000.
The final plan retains the separate `D_800DDF73` relocation pair at0x2C4/0x2F0,
with a zero low-half addend. An effective negative control recreates the wrong
0x10000 end-address displacement. All three rebased layouts now pass.
The failed v1 normalization is preserved as superseded evidence and is not
installed; authoritative artifacts use the v2 suffix.

## Qualification and installed evidence

Both tools copies pass eight fresh canonical checks and shared tools checks.
Each installed copy then passes two fresh checks and reuses six semantic
checks only with identical module, input and prepared-artifact fingerprints.

- 3,332 guest cases visit all252 target words, all256 signed flag-byte values,
  all eleven rows and eight provider-effect modes. Normalized C agrees with
  retail in complete state and access trace; raw C agrees in public memory
  and calls, including all eight geometry arguments and shared aliases.
- 64 cases execute all12 original caller-window words. Another128 cases
  connect all64 original cleanup instructions to the dispatcher.
- Native32 O0/O2/O3 each pass780 cases with trapping UBSan, real pointers,
  1,168 bytes of public state and twelve effective wrong-C controls.
- 375 direct and566 connected-cleanup fault-prefix pairs agree in full state,
  access order, PC and delay-slot state. This qualifies emitted instruction
  order, without claiming portable C fault semantics.
- Three rebased layouts pass72 guest cases. All68 raw/body/binding corruption
  controls and66 incorrect expected-word guards reject; the delayed-HI16
  alias control fails observably.
- Twelve IDO-compiled semantic negatives have actual behavioral witnesses;
  unsupported interpreter instructions or incidental faults do not count.
- Fourteen image corruption controls reject. Production reproduces the
  independently predicted complete ELF exactly.

The actual six-command Make recipes cover both owner and caller. Eight other
owner functions and all pools/bindings remain fixed. The owner has no compiler
diagnostics. The caller retains three preexisting Warning712 diagnostics; the
full build also retains the unrelated duplicate `generated_12D630` warning.

The strict image delta is933 bytes:827 target instruction bytes, two target
extent bytes (12 to1,008), and104 bytes in three closed symbol/string ordering
permutations. Every named definition except target extent is unchanged.
All6,056 function addresses and6,055 other bodies stay fixed, together with
189,088 protected Game bytes across720 owners, the map and conversion inventory.
Exactly66 guard rows are appended; the complete inherited prefix is preserved.
There are zero excluded image bytes. The production seal covers16,442 files
and399 focused inputs; the new working note is added to the closing seal.

The downstream providers remain bounded: `func_15165C80`, `func_1517725C`,
`func_15179DB0`, `func_1510D630`, `func_10004074`, `func_151670C0`, and
`func_15177A94`. The connected cleanup is complete, but these checks do not
claim complete rendering, heap behavior, the full caller, or gameplay acceptance.

| Artifact | SHA-256 |
| --- | --- |
| Raw compiler body | 325597c954cd79c0c4f11956b2dc1c09e3578d30a8b205b529a29311e42a1ff8 |
| Normalized relocatable body | ae19b1edb15ceae8127a019186972affe3f0e22d834c7f44577bac0d25247787 |
| Adopted object | 5ede2c6253fa77257ae7ed64f4ef5f0bb506fdd5ae0ae84248f6ccb71510e1fb |
| Adopted ELF | 088882c693427a28682a2ebb91aef44b98081d212f79b1b2306dce81b607b67c |
| Guard manifest | 9cd65675bf6bfca1ab216bdc540937a1bf50f36f2a112eb0c043605bdc4a85b0 |

## Bank and progress

Predecessor consumer: `e820370819fde1366f7c288bd5b61aaf021bd1bf`.
Tools committed first: `11f9c03e24cd46b4b5e81d3636324995e5ddbc4e`.
Bank owner C, caller prototype, guards, tools pin and measured documentation
together. Preserve1,817 inherited dirty paths plus three new qualification
files in the older tools mirror. No push or mirror commit. Claude calls:zero.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,870 / 5,506 (70.29%) | 0 | 1,636 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,197 / 4,833 (66.15%) | 0 | 1,636 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

260 further matches are needed for4,130 /75%. Remaining shapes are1,507
placeholders,120 semantic/other and nine unlocated. Only `func_15183D28`
gains credit. Next inspect the50-word `func_150C1198` in `generated_EDE60`;
this is a queue candidate, not a qualified recovery. `func_1514E920` stays
parked and uncredited.

Evidence lives under `conker/build/game-record-dispatch-match/`, including
`canonical_v3.py.terminal.json`, canonical and installed receipts, the v2
normalization, actual Make preparation, strict prediction, native adoption
and actual-ELF recount. The closing handoff records the consumer commit,
scoped AST graph refresh with old-node retention, and final audit. Root README
receives aggregate rows only.
