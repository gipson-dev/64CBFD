# Route Actor Event Direct C Conversion

Date: 2026-10-18. **Installed direct C match: all 51 words / 204 bytes exact.**

Convert `func_1508802C`, generated_B3020, VA `1508802C..150880F8`, ROM
`B54DC..B55A8`, after [Note 1576](1576-route-actor-update-complete-match-and-installation-20261018.md).
Consumer predecessor `595893aa`; tools predecessor `6327a76`. Bank tools
**eabe57c** first, then the consumer source/docs/pin. No push.

## Recovered Interface And Body

The complete routine is `s32 func_1508802C(u8 *record, u8 *actor, s32 reason)`.
It rejects nonzero state+0x120 or a masked actor slot, otherwise sets the actor
and current-actor context, submits `func_1507BB28(0, reason)`, stores its full
32-bit result, clears the halfword timer, writes the byte sentinel, and marks
record+0x30 as state 2. Rejection returns 1; successful submission returns 0.
Keep the address name, meaningful locals and one concise purpose comment.

The actual next-routine caller consumes V0. Correct the older route-update
caller's local `void` declaration to `s32`; its emitted instructions remain
unchanged. Preserve the full-width reason passed to the helper independently
of its low-byte actor store. Preserve the record-index read after earlier stores
and the post-call actor/record reloads. Original assembly remains as a reference.

`variables.h:1074` declares 26 actors; `structs.h:1394` records their 0x32C-byte
size. The native C corpus uses these valid slots, where `1U << slot` is defined.
The explicit masked-shift screen emits 52 words and 36 differences because of
an extra ANDI and changed temporary allocation. It is not selected. The signed
pointer-difference division and original unmasked shift emit all 51 words
directly: frame 0x18, nine bindings, no new guards, volatile or compiler flags.
All 256 signed caller-slot bytes are separately exercised in the guest artifact;
out-of-table cases do not establish portable C behavior or valid gameplay inputs.

Raw unlinked code SHA:
`fd2091bf2ad369fea38cc4cf25a6cec536659ccb69a8c121e0ea51a9aff98acd`.
Isolated, full no-unroll owner and full normal-profile output agree exactly.

## Fresh Qualification

All **11 pre-install tests pass in 38.539 seconds**, and all **11 post-install
tests pass in 32.916 seconds**, with no skips. Do not add overlapping corpora.

- 1,112 cases cover all 26 valid slots, all 256 state-flag bytes, all 256 index
  bytes, all 256 reason low bytes with nonzero high bits, full-width extremes,
  low/high mask bits and three provider-result words. Compare independent
  reference outcomes, public RAM and pre-call snapshots; retail/source runs
  additionally compare modeled GP/FP/LO registers, complete RAM and ordered
  access traces in both stack phases. Every one of the 51 words is visited.
- The same 1,112 cases pass freestanding native32 O0, O2 and O2+UBSan using the
  existing native_command helper. Observe pre-call state and model provider
  mutations to the actor, record and current globals. The native check compares
  14 scalar/call observations, not every native padding/private byte. A wrong
  success return exits 21; a separate outside-shift-domain control traps under
  UBSan. That trap is not counted as an ordinary semantic negative.
- Four ordinary executed guest negatives change the public result: wrong
  success return, narrowed reason, signed mask, and prematurely captured index.
  No crash, timeout or instruction-budget failure is credited as a negative.
- 310 fired own-access fault pairs cover five alias arrangements, three gate
  paths and both phases, including one valid private-home alias. Public aliases
  also pass the independent reference. A rejected initial private fixture
  corrupted the saved pointer/return state; move the witness to a valid home
  and suppress provider mutation there rather than accepting an unmapped fault.
- 72 actual parent-caller cases cover record states 0/1/2, enabled/blocked
  children and both stack phases, including V0 consumption and counter wrap.
  The event helper remains an explicitly bounded provider, not a reimplementation
  or gameplay acceptance claim.
- Independently assemble the preserved retail source. Its raw words and all
  nine bindings equal C. Three GNU maps exercise independent data/call rebases
  and HI/LO carries; six paired code-rebased executions pass. Changed-data-map
  execution is not claimed.

The initial local oracle lacked LB; implement signed-byte loads only in this
target's subclass. Native libc multilib headers are absent, so reuse the existing
freestanding native32 path without installing dependencies. These were fixture
issues, not production changes. No debugger, compiler capture or Claude call.

## Installation And Image Audit

Both full owner profiles preserve all 72 neighbors and pools. The actual mixed
padder preserves all 73 owner functions, including the normal-profile projection
override and remaining GLOBAL_ASM bodies. The first private whole-ELF link is
literally identical to its predecessor, including metadata; no serialization
allowance, symbol-size edit, guard or Makefile change is required.

The real `make -C conker -j4 build/conker.us.elf progress.csv` succeeds. The
installed audit verifies all 6,057 function bodies/addresses unchanged and all
189,088 protected Game-data bytes / 720 owners exact. Whole-ELF SHA remains
`44ecb171bef3c1e2c5f3afb2345953cf70d15224a51db37a1d4fc62c60105e0c`.
All frozen inputs except the declared owner-source change remain fixed. The
existing duplicate generated_12D630 recipe warnings remain; not a warning-free
build. Old receipts retain their original frozen source stage; use this event
audit for the current checkout rather than weakening a predecessor's pins.

## Progress And Handoff

This converts already-exact assembly into exact C; executable bytes do not
improve or change. C coverage increases by one function / 204 bytes. The fresh
matcher reports total **3666/5502 (66.63%)**, Game **2993/4829 (61.98%)**,
Init **492/492**, Debugger **181/181**, with **1,836 different / zero drift**.
Conversion is total **5502/6044 (91.03%), 86.05% bytes**; Game
**4829/5323 (90.72%), 85.42% bytes**. Filter repeated CSV header rows before
aggregating; they are not functions. README receives aggregate rows only.

Both tools copies pass three repository-setup tests and the tool smoke check;
consumer `make tools-check` passes. Three owned files are identical ASCII and
AST-valid. Preserve all 1,298 pre-existing mirror hashes and its ddbdd16 HEAD;
add only these three files, leaving 1,301 dirty paths. No mirror commit/reset.
Post-commit graph preservation is a separate final gate in `graph-audit.json`.

```sh
python3 -m unittest tools.tests.test_game_route_actor_event_match -v
python3 -m tools.experiments.game_route_actor_event_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

This routine is finished. Next audit retained `func_150880F8`, VA
`150880F8..150881CC`, 53 words: the caller already exercised here. Recover its
complete C, including the null-table path and signed byte/counter behavior,
before claiming conversion. Broader Game work stays active. No sibling host
changes, Release actions, hardware/FCSR or whole-game acceptance claim.
