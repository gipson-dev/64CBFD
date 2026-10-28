# 1747 - Bound-object reference event pair guarded C match

Verified: 2026-10-27. Owner `generated_1C2C60`.

| Function | VA span | Retail ROM span | Retirement command | Helper |
| --- | --- | --- | --- | --- |
| `func_15198054` | `15198054..15198110` | `1C5504..1C55C0` | 8 | `func_151993B4` |
| `func_1519986C` | `1519986C..15199928` | `1C6D1C..1C6DD8` | 0x26 | `func_1516972C` |

## Recovery and interface

Replace both zero-return placeholders with complete 47-word /188-byte semantic
callbacks. Each retains frame 0x18 and one R_MIPS_26 binding at byte +84. The
ordinary O2/g3 profile emits 46 words directly. One expected-word guard per
routine swaps the read operands of its symmetric BNEL at byte +0x98; these are
guarded C matches, with two new guard rows total.

The measured interface is `void(u8 *owner, s32 eventAddress, u8 command)`.
The real dispatcher passes three arguments and consumes no return value.
Incidental V0 results remain checked in the guest model; they are not a C return
contract. Cast the 32-bit event address to a byte pointer locally, preserving
the existing dispatcher declaration and a correctly typed Native32 call chain.

`BoundObjectReference` names the object pointer and unsigned identifier at +0/+4
of the state pointed to by owner+0x98. Commands zero, two and the specific
retirement command call the respective helper if either the object pointer or
the identifier matches. The object comparison short-circuits the ID read.
Other commands retain the state without reading the event or state contents.

Command 0x2D replaces a reference in either direction: the first matching object
becomes the second with event byte +9; otherwise a match to the second becomes
the captured first object with event byte +8. The first match has priority when
both tokens agree. Normal retirement payloads use their ID at event+4; the
replacement payload interprets that location as its second pointer. Preserve
these command-dependent layouts and the ID reads after pointer stores when
payload and reference overlap.

Ordered predicates recover the original dispatch shape. An explicit local
captures the first replacement object before reading the current reference,
recovering the retail independent-load order. The remaining branch has raw
`0x544B0005` and normalized `0x55620005`: exchange only GPR V0/T3 as BNEL's two
read operands. Inequality is symmetric for every 32-bit pair. Opcode, likely
behavior, branch offset, delay slot, writes and call binding are unchanged.
Expected raw body hashes and bindings fail closed before normalization.

## Actual caller and helper boundaries

Both callbacks are registered once, in the 20-entry `D_8008A390` table: slot 3
at VA `8008A39C` /ROM `22EE5C` and slot 14 at `8008A3C8` /`22EE88`. The aligned
retail census finds no direct JAL/J instructions to either target.

The complete 18-word `func_15147D1C` dispatcher reads owner+0x20, selects this
actual table entry, skips null entries and calls the three-argument callback.
Its original and retained bodies agree. It uses a full-word index without
clamping. Native tests restrict indices to 0..19; four sparse wrapped-index
cases are guest-machine evidence, not portable out-of-bounds C claims.

The first callback's original and retained 12-word `func_151993B4` helper are
executed completely; its recovered C body is used natively. The second helper
and unrelated registry callbacks use bounded provider contracts. This recovery
does not establish complete teardown behavior for those providers.

## Qualification and retained experiments

Both tools copies pass eight fresh canonical methods, with zero errors,
failures or skips. The primary takes 16.496s; exact mirror timing is retained.
Both shared tools checks pass. The checks include:

- 19,332 guest cases covering all 256 command/identifier bytes, three incoming
  upper-word patterns, ten overlap layouts, two stack phases, both replacement
  directions, first-match priority and complete original/raw/normalized state.
- Each target reaches 45 words publicly; the retained duplicate words 25/37 are
  unreachable from normal entry. All 47 literal words remain exact.
- 2,404 dispatcher cases cover all 20 real registry entries, both original and
  retained dispatchers, null callbacks and four full-word sparse wrap cases.
- Native32 O0/O2/O3 each pass 10,340 positive cases per target, typed indirect
  callbacks, the actual dispatcher C, the first helper C, trapping UBSan and
  eight effective functional negative controls per target.
- 90 access-fault prefixes compare original/raw/normalized states. Sparse unknown
  commands need only owner+0x98 and stack mapped; an object match bypasses both
  optional ID bytes. Eighty integrations execute the original/retained first
  helper with expected owner/reference effects.
- All 94 raw-word corruptions, two wrong bindings and both actual padder guard
  corruptions are rejected. Twelve GNU links across three layouts per target,
  including another JAL region, pass with 24 rebased guest cases.
- Ten full-image corruptions and two wrong predecessors fail closed.

The first canonical guest fixture accidentally placed its reference at the
shared oracle's stack address. The second stack phase overwrote its ID with
saved RA, and the real helper could then change that saved return address.
The corrected fixture separates normal state/event storage; intentional home
aliases remain separate cases. Candidate C, code and guards are unchanged.
Failed v1 receipts remain in `failed-canonical-v1/`; accepted suites are v2.

Earlier private preparation also exposed source-newline serialization, a Python
fingerprint-map merge error and an existing scratch-directory precondition.
Those driver issues were corrected and the full actual Make/image preparation
rerun as v3. The initial pointer-typed event API is archived under
`pointer-api-preparation/`; the selected API matches the actual s32 dispatcher.
Its instruction payloads remain identical.

## Production, whole-image audit and recount

All 67 neighboring owner functions and pools remain fixed. The actual
three-command Make recipe reproduces all 69 compact functions and the entire
padded object. Production passes, retaining the inherited duplicate
`generated_12D630` recipe warning. Each tools copy then runs two fresh installed
owner/image checks and reuses six semantic methods only after module, snapshot,
prepared-artifact and sealed-input fingerprints agree. Broad unchanged suites
are retained evidence, not freshly rerun tests.

The production ELF equals the independent prediction: 254 target code bytes and
two target symbol-size bytes change, 256 total, zero exclusions or serialization
allowance. All 6,056 function addresses and 6,054 other bodies remain fixed.
Protected Game data stays exact across 720 owners /189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

All 120 focused inputs and 16,162 sealed Native/cache files are checked with five
declared source/guard/object/ELF/map adoption paths. Conversion inventory is
unchanged; every old guard byte is preserved and exactly two rows are appended.
No hardware, emulator, FCSR, rendering or gameplay acceptance is claimed.

The captured adopted Native ELF recount is 3,825/5,506 exact (69.47%):
Game 3,152/4,833 (65.22%), Init 492/492 and Debugger 181/181; zero address drift,
1,681 still different. The 75% threshold is 4,130, requiring 305 more matches.
Remaining triage is 1,552 placeholders, 120 semantic/other and nine unlocated
entries. Source shape alone does not earn matching credit.

## Checkpoint and continuation

Baseline consumer `c8d5a18208ea30f553aa01de5c44eb8f9985e5e7` and tools
`e1008a10162e36b51f34e1feca4d6a778026d1f8`. Tools are banked first in
`7a27c64df6ea03dc507fdd6ef7931a45969d1698` and then pinned by the consumer.
Preserve the old mirror's 1,704 inherited dirty paths plus two new files. No push.

- Snapshot SHA: `eb2226dbaa3914d54a9f10dba76bab4c394d2d2ed7e50c59fe75f6b8373c1f33`.
- Padded object SHA: `c25d7b55b5d03fc503a99a3285dbbec343c9b75f9c5d5c890dbb89f9547c43d5`.
- Adopted ELF SHA: `200faa361e36be0a7d13249ae6437bc0a40508a89fa1f1e0af7eeb1654beef4c`.
- Reproduce: `python3 -m unittest tools.tests.test_game_reference_event_pair_match -v`
  in the prepared consumer/cache. Ignored evidence remains in
  `conker/build/game-reference-event-pair-match/` with fresh PID directories.

The earlier `func_1514E920` screen remains private/uncredited in
`conker/build/game-owner-bit0-attachment-match/`. Its ordinary reconstruction
emits 44 rather than 47 words; alternative state lifetimes still fail full
identity. No owner/header/guard changes from that screen are installed.
Next screened placeholder: `func_15097910` in `generated_C4DC0`,47words.
Codex owns implementation/validation; routine Claude calls zero. Keep the 75%
goal active and refresh changed-source Graphify with old-node/link retention.
