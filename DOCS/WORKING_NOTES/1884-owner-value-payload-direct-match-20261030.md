# 1884 - Owner value payload constructor direct C match - 2026-10-30

`func_15109ED4` replaces its zero-return placeholder in
`conker/src/game/generated_1368C0.c`. All **57 words / 228 bytes**, both call
bindings and the 72-byte frame match directly under the existing O2/g3 profile.
There are **no new guards, insertions, omissions or compiler-profile changes**.

Tools commit: `2fb3f255384c761587d3aa5d0e22843a0e7e1642`. Ignored evidence:
`conker/build/game-owner-value-payload-15109ED4-match/`.

## Recovered behavior and ABI

The eight arguments are an owner byte pointer, signed 16-bit lifetime, two signed
bytes, a float value, unsigned 32-bit extra-byte count, unsigned selector byte and
a final signed word passed to the factory. A null owner returns null without
allocating. Every negative lifetime selects 300 and flag 0; nonnegative lifetimes
pass through with flag 1.

The 16-byte payload stores the owner pointer at 0, positive zero at 4, the supplied
float representation at 8, signed settings at 12/13, and two untouched alignment
bytes at 14/15. The factory request uses selectors `-1, 0x1B, -1`, request byte
`0x1B`, unsigned `extraBytes + 16`, the selector and final word. The original
factory adds its 40-byte header, so the allocator sees `extraBytes + 56`, with
the retail 32-bit wrap. On success, `memcpy` copies all 16 payload bytes to the
created object at `+0x28`. The routine returns the original allocation pointer,
including when the copy service returns its destination pointer instead.

The frame has saved RA at `SP+44`, payload at `SP+52`, untouched padding at
`SP+66/67`, and the saved allocation result at `SP+68` across the copy call.
The source uses a signed duration temporary and byte flag; setting the explicit
flag before assigning the nonnegative duration reproduces the retail schedule.
Several narrow flag types emit the same code; the selected unsigned byte agrees
with the factory argument and only carries values 0/1.

## Allocator declaration repair and preserved neighbor

The owner previously declared `func_15149130` with a generic pointer return and
integer seventh argument. The recovered provider and shared SDK declaration use
`struct260 *` and `struct37 *`. This owner now includes the real SDK typedefs and
uses that compatible declaration. An explicit pointer cast carries the observed
byte-count word; the provider's broader pointer-typed size contract is unchanged.

The already matched neighbor `func_1510A344` gains two explicit SDK32 casts: its
factory result to `u8 *` and its 20-byte size to `struct37 *`. Removing exactly
those two casts reproduces its previous source body. Its complete 50-word raw
and padded body, six bindings and globals remain identical. Fresh native checks
cover its null gate, signed lifetime, priority lane, captured identity, three
float values, allocation failure, complete 20-byte copy and result pointer at
O0/O2/O3. This is a declaration correction with no additional matching credit;
[Note 1802](1802-owner-float-payload-match-20261028.md) records its original match.

## Qualification evidence

- **1,230 guest cases / 3,690 executions** compare original, direct C and padded
  code with the original 49-word factory and 11-word byte-copy loop connected.
  Every target word and 47 reachable factory words execute. The factory's two
  flag-2-arm words remain present but are unreachable from flags 0/1.
- Twelve raw float patterns cover signed zeros, subnormals, finite extrema,
  infinities and quiet/signaling NaNs without arithmetic on their representations.
  Seven extra-size patterns exercise the unsigned wrap. Provider mutations test
  incoming homes and the payload's untouched padding. Returned allocation-pointer
  identity is checked independently from the copy return.
- **83 access cuts**, including five delay-slot cuts, preserve complete guest
  state and actual fault context across all three code versions. Eight rebase
  cases use two independent function/callee layouts across address boundaries.
- The aligned ROM census finds only JALs at **`0x54AD8` and `0x54B14`**, with no
  aligned literal function-pointer words. Their original 15-word windows start
  at VA `0x150275FC` and `0x15027638` inside `func_150265CC`. **192 cases** verify
  both windows, eight arguments, the signed lifetime, two setting variants, float
  loads, null/allocation gates and the original exit `0x15029BA4` with return 1.
  The parent remains a C placeholder; full-parent execution is not claimed.
- Native SDK32 O0/O2/O3 each pass **524,288 target cases** with trapping UBSan,
  all 65,536 duration and signed-byte-pair patterns, 12 float representations,
  seven size patterns, null owners, both allocation outcomes, owner/output aliases,
  complete representation copies and canaries. Padding values are not assumed.
- The declaration-affected neighbor passes **1,024 fresh native cases per profile**.
  All nine owner neighbors and pools are also compared as complete compiled code.
- **14 effective controls** run through IDO/guest and native compilation: zero,
  value, first setting, default lifetime, negative gate, flag, kind, operation byte,
  extra size, copy length/destination, allocation failure, return pointer and null
  gate. Build/interpreter failures do not count as semantic control success.
- Both tools copies pass eight fresh canonical checks and shared checks. Production
  repeats two installed checks per copy, reusing six semantic receipts only after
  full input/module/artifact fingerprint equality.

These are bounded guest and native validations. Emitted fault order, provider
aliases and raw representation checks do not establish portable C fault/overlap
behavior, general FCSR equivalence, real allocation capacity or hardware acceptance.

## Owner, image and measured progress

The actual three-command Make recipe reproduces the qualified object. Selected,
owner and executed-command diagnostics are empty. The existing duplicate
`generated_12D630` warning remains in the Make dry-run plan.

The independent whole-image prediction equals the first link and adopted ELF:
**168 changed bytes = 167 code bytes + 1 symbol-size byte**, metadata 0, exclusions
0. All **6,055 other bodies**, all **6,056 function addresses**, the entire guard
manifest, C inventory CSV and protected Game data (**189,088 bytes / 720 owners**)
remain fixed.

Raw C SHA-256: `6b60a469e17fb4b30a2a8891a0a28681248c8a1dd01f3dfe28537e2b211707d7`.
Owner source SHA-256: `e4c9535fa6fda0cd498850a4492d9195ac82cccd5d7c126546c7f58888d4301d`.
Padded owner SHA-256: `bec3d71c582641a6df6e07e642819c06f60ba2548a3db231b21f47dfbdfb805f`.
Adopted ELF SHA-256: `cf242df79321050b2fe148aa0057602caee2df153e8aa4ef621d0ba2ca284ef3`.

Fresh recount: **3,961 / 5,506 (71.94%)** total exact C; **3,288 / 4,833 (68.03%)**
Game, zero drift. Init stays 492/492 and Debugger 181/181. The 75% goal remains
active with **169 more** matches needed for 4,130 / 5,506. Next screen: `func_151D5714`.
The root README receives only its two aggregate matching-row updates.

All 2,090 inherited mirror dirty paths and its HEAD are preserved; three new
qualification files are added there. Tools are committed before the consumer;
nothing is pushed. The scoped eleven-file Graphify refresh retains prior nodes
and valid relationships, retires both obsolete signed-return relationships and
records the cast-only neighbor correction. Historical communities remain
historical; no full-corpus re-extraction or global clustering is claimed.

Codex performed implementation, review and validation. This routine matching
used zero Claude calls, provider changes or dependency installations.
