# Descriptor adjustment private semantics and compiler-shape audit

Verified 2026-11-01. **No production function or declaration is installed or
credited by this audit.** Total stays **4,036/5,507 (73.29%)**, Game
**3,363/4,834 (69.57%)**, zero drift and1,471 different. Threshold4,131 still
requires **95 matches**. Production code remains `dab995ed`, tools `7792eb0`.
Only this note, five working indexes and ignored experiment evidence change.
The wider matching goal remains active; no pause or push.

## Descriptor candidate improves to the correct length/frame

`func_150174C0` in `game_447B0`, VA `0x150174C0..0x15017578`,
ROM `0x44970..0x44A28`, has46 words/frame8. It adjusts tag-2 halfwords in
24-byte rows, preserving low16-bit wrapping. Retail uses signed outer bounds,
reloads table base and row count after a matching store, and reloads the outer
bound after a nonempty inner loop. Empty rows retain the captured outer bound.

The previous pointer-header candidate was45/frame8/32 differences. The best
new form is **46 words/frame8/13 differences**: declare a pointer to the
individual halfword inside the inner loop, capture its value, and store through
that same pointer. Unsigned addition preserves wrapping without signed-overflow
UB in the native valid domain. Explicit return of the outer index regresses to
47 words/26 differences for this form; void remains a private ABI hypothesis.

The best source uses the existing packed-peer layout: two halfwords, a reserved
word and eight entry halfwords. `generated_B3020.c` already uses the same24-byte
row layout and an independent byte-pointer table declaration. The production
shared header still declares `D_800D23C0` as `s32`; no public repair is made.

The remaining13 words cover inner-loop entry scheduling, a two-register role
change, entry-address +8 bias versus memory displacement, and branch offsets.
This is **not** a claim that13 independent scheduling guards would be valid.
No word guard, insertion, filler or broad CFG rewrite is proposed or installed.

Fresh source screens:

| Experiment | Words/frame | Differences or result |
| --- | --- | --- |
| Pointer-table typed indexing, void |45/8|32 |
| Same, explicit signed result |46/8|33 |
| Inner-scope halfword pointer, void |46/8|13 |
| Same, explicit signed result |47/8|26 |
| Explicit byte-offset/reload models |46..47/16|44..46 |
| Byte/header and halfword address forms |42/8|33..34 |
| Twelve-halfword row view |45/8|32 |
| Register hints |46/8|13, ineffective |
| Pointer/u32/s32 entry temporaries, pointer header |46/8|13, ineffective |
| Same entry temporaries, existing integer header |44/8|37 |
| Per-iteration cached row pointer, six scope/type forms |42/8|34 |

The first advisory-derived function-scope draft placed a declaration after an
assignment, which IDO rejected. The corrected C89 forms all compile; that failed
draft is historical and not qualification evidence.

## Fresh private semantic qualification

`oracle-draft.py` independently models captured/live bounds and conditional
reloads. **1,014 cases / 2,028 executions**, three independently linked address
layouts, compare the complete original46-word routine with the private compiled
C. Public memory, the full memory-access trace, incidental V0 loop index, saved
registers and SP agree. All46 original words execute. Boundary inputs include
negative outer counts, signed adjustment extremes, empty/full rows, tags,
zero additions and low16-bit wrap.

Two guest-only alias fixtures deliberately alter the table pointer and outer
count through a tag-2 halfword store. Both force the live reloads to matter.
Stale-base and stale-bound reference controls are effective. The initial
stale-base fixture changed the pointer only after its final element, so its
control was ineffective; a third entry in the new row now makes the stale read
produce a different public store. The final positive corpus and both controls
pass. These global-storage aliases do not establish portable C effective-type
or array-bounds equivalence.

**37 access-prefix cuts / 74 executions** compare public memory and access trace.
They do not claim complete fault-register state, identical PCs or hardware
exception equivalence between the still-different instruction streams.

Native32 **O0/O2/O3** each pass **168 cases / 1,008 executions**, UBSan and all
descriptor bytes/canaries. Bounded rows contain0..8 entries; guest-only global
aliases are excluded. All five wrong tag, sign, row, shift and adjustment
controls are effective. The signed bound and unsigned addition behave correctly
at the tested integer limits. No native result value is inferred from void C.

## Private whole-owner declaration experiment

`qualify_owner_v19.py` uses a copied `variables-private.h` with only
`D_800D23C0` changed to `u8 *`. The copied owner gets the packed-row type,
candidate void body/prototype, and removes the caller's pointer-to-integer
assignment cast. The isolated and whole-owner candidate payloads/bindings agree.
All **four raw owner neighbors**, normalized pools and zero-warning diagnostics
remain unchanged. In particular, the caller's cast removal emits identical code.

This is **not** a production header/dependent-object audit, actual Make/padder
qualification, complete-image prediction or ABI approval. The header and owner
are copied diagnostic files only. Current sources, headers, objects, ELF, guard
CSV and map remain byte-identical to the banked production checkpoint.

Best raw SHA-256:
`8e57209dd5813886c604aa2b29a938ddc3e8629b4052c3387b7b431d976ecea7`.

## One bounded advisory, independently checked

The difficult source-shape decision used **one attempted/completed Claude call**
under the existing first-party Pro route, without provider/account/model changes.
Safe mode, disabled built-in tools, strict empty MCP configuration and no session
persistence produced effective `tools=[]`, `mcp_servers=[]`; output contains no
tool use. No second call was made. Invocation is evidence for this one
packet-only analysis, not a general filesystem sandbox or model integration.

Question: which minimal source shape might avoid entry-pointer +8 materialization
while preserving the original loop entry and per-iteration row multiply?
Packet revision12 SHA-256:
`d6437fa80ba6095279767582cf8a68d808b66d79d750b53c94f7c3136002f48c`.
The response and provenance receipt are retained beside the ignored packet.

Disposition: the observed pointer-bias/store-displacement distinction is useful
and confirmed in the compiled disassembly. The proposed per-iteration row-pointer
fix and its scope variants were tested and rejected as matching fixes: all six
emit42/frame8/34. The explanation that plain typed double indexing necessarily
adds a second row multiply is contradicted by the retained45-word disassembly,
which already reuses a single computed address. No suggestion is adopted by
agreement, and the advisory did not approve installation.

## Secondary event-handler screen and continuation

An isolated screen recovers a private interpretation of `func_15164134` in
`game_18D770`,53 words/frame24: command0 conditionally deletes an owner,
command45 swaps matching peer keys/tags, and other commands use a type callback.
The best source is54/frame24/48 differences; switch and nested-scope forms are
55/49. Pointer/struct/integer address spellings do not improve it. Its callback
interface and possible extra forwarded arguments remain unqualified. No owner,
runtime, caller or production gates are claimed for this secondary candidate.

Descriptor evidence: `conker/build/game-descriptor-tag-adjust-150174C0-match/`,
including `screen8-results.json` through `screen15-results.json`,
`private-guest-runtime.json`, `private-native-runtime.json`,
`private-owner-qualification.json`, `claude-review-v12.json` and packet/answer.
The corrected advisory experiment is `screen14-results.json`; there is no
successful `screen13-results.json` from its rejected C89 draft.
Secondary evidence: `conker/build/game-owner-peer-event-15164134-match/`.

Next recover the descriptor's remaining loop-entry/address formation in CFE/UOPT
or move to another qualified Game queue candidate; reuse these semantic receipts
only with unchanged source/compiler/input fingerprints. Keep both functions
uncredited until exact words, declarations/ABI/dependencies, owner/padder,
actual Make, entire-image, production/recount and documentation gates pass.
Original ASM, all private work, dirty tools-mirror edits, archives and frozen
host/editor Release artifacts remain preserved.
