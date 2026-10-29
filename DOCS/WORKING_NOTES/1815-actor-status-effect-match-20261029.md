# 1815 - Actor status effect callback - 2026-10-29

`func_151AB854` now emits all 51 retail words / 204 bytes directly from
semantic C in `conker/src/game/generated_1D6E80.c`. It retains the original
48-byte frame and one helper binding, with no guards or custom profile.
The zero-return placeholder becomes `void func_151AB854(u8 *record)`.
The existing `struct185` supplies the packet layout; the original function
name is retained and the source comment describes the operation.

## Recovered behavior and interface

The callback reads an actor pointer from record+0x18. Only unsigned actor
types 0, 1, 2, 3, 4 and 150 enter the effect path. It captures the actor pointer
and identity at +0x3B, sets lifetime 300, clears two flag bytes, and sets mode
3 for type 150 or 0 for the other supported types. Type is reloaded after
packet stores, matching the original access order even when fields alias.

If actor+0x127 is not 255, the halfword at the linked pointer
(actor+0x31C)+0x66 is set to 500. The record pointer is then reloaded from its
incoming argument home, and its unsigned group/context bytes at +0xC and +1
are passed to `func_15190770`, together with the packet and a zero size
extension. The helper result is ignored. The original helper returns the
created pointer or NULL, supporting the local typed declaration.

The 12-byte `struct185` packet begins at frame+0x20 / incoming SP-16.
Offsets 5 and 11 are not written by this callback. Guest checks retain and
compare all 12 bytes; portable native checks inspect only the ten defined
bytes/fields. This change does not zero or otherwise invent padding contents.

The first switch source emitted 53 words and a jump table. An explicit
six-way predicate recovers the original branch chain. Declaring the actor
pointer before the packet recovers its original stack position naturally.
Two of twelve flow/declaration variants match directly. No artificial
padding, instruction replacement or compiler-profile change is used.

## Original routes and scope

The only aligned original pointer is ROM 0x22FAE4 / VA 0x8008B024: slot 21
of the 23-entry `D_8008AFD0` table. There are no aligned direct JAL/J callers.
The original `func_15158D2C` window at 0x15158F40 contains eleven words that
check the second eligibility mask, dispatch the indexed callback with S1 in
A0, ignore its result, and advance S0. All eleven words are exercised,
including the skipped-dispatch route. The wider caller remains a C stub;
this evidence qualifies the window, not the complete parent routine.

The complete original 52-word `func_15190770` helper is exercised with
successful/failed allocation and provider mutation. It captures the actor
and identity, calls preparation service 14, requests a type-32 / 0x300-byte
effect, copies the complete packet, initializes its fields and workspace,
and stores a random byte. All 52 words are visited. Its current C placeholder
is unchanged and receives no recovery credit. Preparation, allocation,
memcpy, bzero and randomness are bounded providers; full provider, hardware
and live gameplay acceptance are outside this qualification.

## Qualification and production

Eight target methods and shared project-tool checks passed freshly in both
tools copies. After installation, two owner/image checks ran freshly per
copy; six semantic checks were reused only after complete input, module,
compiler-adapter and artifact fingerprint identity.

| Evidence | Result |
| --- | --- |
| Retail/compiled guest comparison | 5,472 cases; all 50 reachable words; complete state/access traces |
| Unreachable retail instruction | Duplicate zero-mode store at offset 0x84 retained in the full 51-word slot |
| Types and aliases | All 256 actor types and byte arguments; four actor layouts and six timer destinations |
| Alias-sensitive behavior | Late actor-type read, packet/timer overlap, group/context writes, incoming-home record redirect |
| Original caller window | 216 cases; eleven words; slot 21, mask skip, forwarded record, ignored result and loop increment |
| Original effect helper | 144 cases; all 52 words; allocation failure/success and provider effects |
| Native SDK / 32-bit execution | 262,144 cases each at O0/O2/O3, trapping UBSan, typed packet and complete record/actor/timer fences |
| Effective bad-body controls | Ten native controls and ten independently IDO-compiled controls fail observably |
| Fault prefixes | 144 fired prefixes, including 17 delay-slot cuts; unsupported types and selector 255 skip unused fields |
| GNU links and rebases | Three layouts, 18 cases; original and compiled objects equal |
| Corruption controls | Three raw body/binding mutations and six complete-image mutations rejected |
| Full owner / actual Make | 41 compact functions, 40 unchanged neighbors, 17 retained assembly routines, five Make commands, no owner diagnostics |

Native checks use valid disjoint objects, preserve packet padding freedom,
and do not claim portable C behavior for guest stack aliases or faults.
Routine work used zero Claude calls. All private and canonical runs passed
without source or fixture revisions after the selected matching shape.

The actual production Make build reproduces the independent complete-image
prediction: exactly 155 changed bytes, comprising 154 code bytes and one
symbol-size byte. There are no other metadata changes or image exclusions.
All 6,056 addresses and the other 6,055 bodies remain fixed, together with
189,088 protected Game bytes across 720 owners. Guard CSV, shared headers,
conversion inventory and linker map are unchanged.

- Before: total 3,892/5,506 (70.69%); Game 3,219/4,833 (66.60%).
- After: total **3,893/5,506 (70.70%)**; Game **3,220/4,833 (66.63%)**.
- Init 492/492 and Debugger 181/181 remain exact; address drift is zero.
- The 75% threshold is 4,130 exact C functions: **237 more** are needed.

Tools were committed first as `7d79ac622a71ef6772ff49524ddfa10d613b847f`.
The consumer carries this note, source, tools pin and aggregate README rows.
Prior consumer/tools were `61fc05be` / `5f774aa`. The older tools mirror
retains its 1,886 inherited dirty paths plus three new qualification modules.
No push or host-port/Release change is part of this recovery.

Evidence is retained in `conker/build/game-actor-status-effect-match/`:
611 focused inputs, a 16,603-file active seal, private/canonical receipts,
full-image prediction, production proof, actual-ELF recount and scoped
Graphify retention evidence. No full-corpus extraction or recomputed global
analytics is claimed.

Next inspect `func_151AC550` in `generated_1D92F0.c`, the next unparked
51-word placeholder in the refreshed queue. It has no matching credit yet.
`func_1514E920` and `func_151D7000` remain parked and uncredited.
