# 1814 - Six-parameter record effect packet - 2026-10-29

`func_151A1EE8` now emits all 51 retail words / 204 bytes directly from
semantic C in `conker/src/game/generated_1CC440.c`, with its original
96-byte frame, two call bindings and no guards. The zero-return placeholder
becomes `void func_151A1EE8(struct260 *record)`, matching the death-callback
table's existing interface. The original function name is retained and a
comment describes the captured 36-byte packet.

## Recovered behavior and interface

The packet contains the position at record+0x28, values at +0x34 and +0x38,
a zero phase, and six signed halfwords at +0x3E through +0x48. All 36 bytes
are initialized before calling the effect factory. The factory receives the
signed lifetime at +0x3C, death selector -1, update selector 4, flags 1,
allocation selector 0, payload size 36, and the unsigned bytes at +0xC and +1.
A successful allocation receives the captured packet at effect+0x28 through
`memcpy`; allocation failure skips the copy but still captures the inputs.
The result is void and the original caller ignores V0.

The local byte pointer provides the record view used by all field reads.
It also recovers IDO's original 96-byte frame naturally. The first shape
without this local emitted 51 words with an 88-byte frame and 13 stack-layout
differences. Thirteen natural declaration/type variants were checked; four
matched directly. The selected shape adds no padding, patches or custom
compiler profile. The packet starts at frame+0x38 / incoming SP-40.

The only aligned original pointer is ROM 0x22EF90 / VA 0x8008A4D0, slot 4 of
`D_8008A4C0`. There are no aligned direct JAL or J callers. The complete
45-word original `func_15149264` dispatcher is already byte-exact in the
current ELF. Its update callback may change the record's lifetime before the
death gate, and lifetime is reloaded again before cleanup. This recovery
preserves that existing dispatcher and the canonical `struct260 *` interface.

## Qualification

Eight fresh target checks and the shared project-tool checks passed in both
local tools copies. After production adoption, two owner/image checks ran
fresh per copy; six unchanged semantic checks were reused only with complete
input, module, adapter and artifact fingerprint identity.

| Evidence | Result |
| --- | --- |
| Retail/compiled guest comparison | 8,848 cases, all 51 target words, complete state and access traces |
| Captured packet and aliases | All slot/context bytes, lifetime boundaries, four source and returned-record layouts, source/provider mutations, forward-copy overlap |
| Complete original dispatcher | 2,304 cases, all 45 words, slot 4, ignored result, lifetime/update/cleanup gates |
| Retained original helper chain | 80 connected cases, 116 literal words across factory, constructor, allocator and memcpy |
| Native SDK / 32-bit execution | 524,288 cases each at O0/O2/O3 with trapping UBSan; all 65,536 halfword values and slot/context pairs |
| Effective bad-body controls | Ten native variants rejected; an independently IDO-compiled late-capture variant also rejected in guest execution |
| Fault prefixes | 272 fired access prefixes, full state/access/PC/delay comparison; null destination needs no child mapping |
| GNU links and rebases | Three layouts, 18 cases, original and compiled objects equal |
| Raw body/binding corruption | Three rejected mutations |
| Complete-image corruption | Six rejected mutations; no excluded image bytes |
| Full owner / actual Make | 39 compact functions, 38 unchanged neighbors, six retained assembly routines, five actual Make commands, no diagnostics |

The real factory/constructor/allocator/memcpy bodies remain exact. Successful
allocation requests 76 bytes, initializes kind 35 and update selector 4, and
copies the complete payload. Coverage reaches 28/28 factory, 47/49 constructor,
28/28 allocator and 11/11 memcpy words. The constructor's alternative kind-95
branch is outside this target's flags-1 route. Heap, registration, zero-fill,
update and cleanup providers are bounded. This evidence does not establish
full provider behavior, hardware or live gameplay acceptance. Native tests
use valid disjoint objects and do not claim portable C behavior for guest
stack overlaps, fault prefixes or FCSR state. Routine work used zero Claude calls.

Git's whitespace check caught an extra final blank line in the new oracle
module. It was removed without changing its AST; the original seal/receipts
remain in `pre-whitespace/`, and both canonical copies were requalified before
commit. The C source and compiled artifacts did not change.

## Production audit and progress

The actual production Make build reproduces the independently predicted ELF.
All 6,056 function addresses and the other 6,055 bodies are fixed, along with
189,088 protected Game bytes across 720 owners. Guards, shared headers,
conversion inventory and linker map are unchanged. The entire ELF changes by
153 bytes: 152 code bytes and one target-size byte. No symbol/string swaps,
other metadata changes or image exclusions are required.

- Before: total 3,891/5,506 (70.67%); Game 3,218/4,833 (66.58%).
- After: total **3,892/5,506 (70.69%)**; Game **3,219/4,833 (66.60%)**.
- Init 492/492 and Debugger 181/181 remain exact; address drift is zero.
- The 75% threshold is 4,130 exact C functions: **238 more** are needed.

Tools were committed first as `5f774aa2ea5ff8b0bb2f16141586db22d042fb5c`.
The consumer commit carries this note, its source, the tools pin and aggregate
README rows. Prior consumer/tools were `997483fa` / `3eda82b`. The older tools
mirror retains its 1,883 inherited dirty paths plus three new qualification
modules. No push or host-port/Release change is part of this recovery.

Evidence is retained in `conker/build/game-record-effect-packet-six-match/`,
including frozen inputs, private and canonical receipts, independent complete
ELF prediction, production proof, actual-ELF recount and scoped Graphify
retention audit. No full-corpus extraction or refreshed global analytics is
claimed. The active input seal contains 16,596 files and 586 focused inputs.

Next inspect `func_151AB854` in `generated_1D6E80.c`, the next unparked 51-word
placeholder in the refreshed queue. It has no matching credit yet.
`func_1514E920` and `func_151D7000` remain parked and uncredited.
