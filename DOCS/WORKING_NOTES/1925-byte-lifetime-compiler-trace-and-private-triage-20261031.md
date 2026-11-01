# Byte-lifetime compiler traces and private callback triage

Verified 2026-10-31 against consumer `a84bf5f9` and tools `44366b2`.
This is an investigation checkpoint, with **zero new matching credit**.
Production remains **4,000/5,506 (72.65%)**, Game **3,327/4,833 (68.84%)**;
**130** more exact C functions are needed for **4,130/5,506 (75%)**.
The current ELF identity is
`8c4b9914475e824e2d55b072ba7cba66b551b586d751835dc8dc84903deee91b`.
Source, object, compiler profiles, guard CSV and production image were not changed.

## Packed motion clamp: measured optimizer behavior

`func_15115F68`, owner `generated_142560`, remains private and unmatched.
Its valid 60-word C reconstruction differs in 44 instruction words from retail.
The earlier bounded guest/native/alias evidence establishes behavior on its
checked domains; it does not establish a byte match or authorize those guards.

Fresh `frontend_lifetimes_v18.py` captures compare `clamp-0.c` (59 words) with
`profile-v10-1.c` (60 words). The existing frontend capture adapter was used
without editing its tools. Every compiler executable passed the adapter's exact
fingerprint gate. GDB observed only newly launched compiler children; both CFE
and UOPT producers, UGEN consumers and compiler drivers exited successfully.
The load-node probe fired 27 times per capture and was removed. Each traced
build retained the normal text, function records, relocations and data pools.

| Source shape | CFE records | UOPT records | UGEN load events |
| --- | ---: | ---: | ---: |
| Lazy casts, 59 words | 507 | 506 | 27 |
| Named byte locals, 60 words | 520 | 514 | 27 |

The named source's CFE stream stores divisor, bias, upper and lower in local
memory homes at source lines 21-24. Its UOPT stream removes those named stores;
it retains the packed word and a predicate value in registers, then emits byte
conversions in later blocks. Thus simply moving the C assignments earlier does
not preserve the retail opening. This is an observed transformation, rather
than a hypothesis about the final assembler scheduler. No original source-level
variable types are inferred solely from these optimized registers.

Captured wire streams, descriptor/type tables, decoded records, normal objects,
debugger logs and qualification receipts are retained under:

`conker/build/game-packed-motion-clamp-15115F68-match/frontend-v18-{lazy,named}/`

The earlier semantic receipts are reused unchanged, not reported as fresh here:
4,312 guest cases, 24,064 native32 cases per O0/O2/O3 profile, 108 rebase cases,
180 guest alias cases and 145 fired memory-prefix comparisons. Native NaN
payloads compare by category; modeled guest payloads are separate. Full FCSR,
portable C fault semantics and complete parent routines remain outside those
claims. The full private handoff is `HANDOFF.md` in that build directory.

## Enable-gate screen

`func_1514E920`, owner `generated_179F30`, has a 47-word retail body with a
0x18-byte frame. The private reconstruction toggles/sets/clears flag bit zero,
clears an attached object's byte at +0x30 when disabling it, and delegates other
modes to `func_1514E89C`.

Ordinary reconstructions emit 44 words; explicit early-null returns emit 48.
Typed extension views, integer address views and explicit forwarding of the
retail A3 extension value do not recover the retail structure. These are source
screens, not qualified ABI contracts. In particular, the three-word fallback
argument view and existing two-argument wrapper still need reconciliation.
No extension argument or signature change was installed.

Artifacts are under
`conker/build/game-owner-enable-gate-1514E920-match/`.

## Closer next screen: signed label fade

The same private directory retains a separately named triage screen for
`func_151D7000`, owner `generated_203E20`, VA `151D7000..151D70CC`,
ROM `2044B0..20457C`: 51 words with a 0x28-byte frame.

Retail loads the record at owner+0x48, checks its referenced object's active word
and byte identity, and reads signed halfwords for duration, fade threshold and
rate. Below the threshold it uses the signed low halfword of duration*rate and
clamps negative results to zero; otherwise the fade is 255. It then submits the
font/state, color, command 0x81 and formatted label through four helpers.

The reference draft's word accesses at byte and halfword offsets were incorrect.
Correcting those widths yields a complete 51-word private body. The best current
screen, `text-spills-1.c` (also reproduced by `text-duration-4.c`), differs in
15 words. This is a screening distance only. Differences include branch-likely
control flow, negative-clamp structure, spill locations and argument preparation;
they have **not** been certified as a closed normalization.

Helper ABI is also unresolved. The draft assumes an integer result from
`func_15042E3C`, while the current implementation in `game_70200.c` is declared
`void`. The current font/state setter takes an integer word, whereas the initial
isolated triage declaration used a pointer view of that word. Matching registers
or a native stub would not establish either production contract. The actual
helper chain and the retail caller's return use must be traced before selection.
No helper declaration or callback return type was changed in production.

## Continuation and acceptance boundary

Prioritize `func_151D7000`'s actual helper/caller ABI and its promoted-halfword
source shape. Preserve both private directories and the new compiler captures;
avoid repeating their completed profile/cast matrices. The enable gate and packed
motion clamp remain available for later source-shape recovery.

There is no selected exact C source for any of these screens. Adoption still
requires source and ABI qualification, copied owner/neighbors, the real generated
padder and Make recipe, guest/native evidence with effective controls, independent
strict image prediction, production checks, an actual recount, documentation and
scoped graph retention. Equal body length or semantic agreement alone receives
no exact C credit. The full 75% goal remains active.
