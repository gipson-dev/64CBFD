# Timed composite-burst constructor recovery and byte match - 2026-11-16

`void func_151A2F0C(u8 *record)` replaces the zero-return placeholder with
the complete constructor. It matches **145 retail words / frame 0x90**,
VA `0x151A2F0C..0x151A3150`, ROM `0x1D03BC..0x1D0600`.

Production now has **4,519 / 5,514 (81.96%)** exact C functions; Game
**3,846 / 4,841 (79.45%)**, Init **492 / 492**, Debugger **181 / 181**.
Zero address drift, 995 different; one new qualified match, **168** more
to the active 85% goal. Conversion stays 5,514 / 6,048 (91.17%), 86.19% of bytes.

## Actual caller and provider

The sole aligned literal reference is `D_8008F8E0[0]`, VA `0x8008F8E0`,
ROM `0x2343A0`. Its second entry is the unchanged `func_151A3150`.
The complete original 45-word/frame 0x20 `func_151A2960` dispatches through
this table at `0x151A29E4`, passing the record in A0 and ignoring the result.
It applies the original timer/fade gates, clears the trigger marker after
the callback, and preserves its second argument for `func_1513170C`.

The constructor passes a **116-byte `CompositeEffectInput`** at incoming
SP-116 to `func_15152B38`, with unsigned mode from record+0xC and the
zero-extended record+1 byte as the full `s32 extra` argument. Its types are
copied from the currently recovered provider, not inferred from a pointer
alone. The provider's original 270-word body and ABI were qualified in
[Note 1988](1988-composite-effect-factory-direct-match-20261102.md); this task
pins the provider source, assembly and the actual callback data file too.

The packet requests a base count 8/range 6 burst, copies the record position,
and optionally adds record+0x4C..0x54 when flags contain 0x1000. It computes
the two scalar ranges from repeated size-field sums, half scaling and the
original `D_800A8D30/34` loads; `D_800A8D38` supplies the other scalar.
All angle/header/byte ranges, flags and two tail sentinel bytes are restored.
Unknown provider field meanings retain their qualified offset-based names.

## Complete C and checked normalization

Raw C already has **145 words / frame 0x90**, SHA256
`abd7629ea2ef251e5294b936f34d3aa4c8a9ac62d8a5d4a30a2fb777ed37b624`.
The typed packet preserves the four untouched bytes at offsets 0x59..0x5B
and 0x6B. Signed-character accesses write the two original -1 sentinel bytes
through the provider's character tail storage without changing its layout.

Exactly **17 expected-word guards** normalize the integer allocation and
packet-store schedule. A bijective opcode/literal/memory-offset/binding
projection conserves all 145 source instructions, all seven bindings and
the branch-likely form. **Zero insertions and zero omissions.** All nine FP
operations preserve ordered operands and FCSR transitions. CSV rows carry
emissions; an independent instruction-driven comparison qualifies the complete
source/retail relation rather than assuming per-row semantic origins.

## Fresh qualification

From the prepared consumer root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tools.tests.test_game_composite_burst_151a2f0c_recovery -v
```

Primary, isolated sibling-tools and installed primary each pass all five
tests, zero failures/errors/skips, at identical task-file hashes. Actual
import origins are sealed. The sibling's 2,434 existing dirty paths and 301
scoped helper fingerprints remain unchanged; the task overlay is separate.

- The independent relation covers **both paths and every 145 instruction**,
  ordered FP/FCSR, arbitrary public aliases within its normal-memory model,
  the complete private frame at the call/return, all return registers and
  opaque packet mutation. No BREAK or other instruction is excluded.
- A separate T0/T1 allocation passes. Wrong flag bit, mode byte, FP operand
  order, tail-byte destination and a private-gap write in the return delay
  are effective semantic failures, not unsupported instructions/timeouts.
- Guest execution passes **1,024 cases per retail/raw/padded stream**, all
  145 words, both offset modes, every mode/extra byte value, full 116-byte
  packet/home and public memory, including opaque packet/record changes.
- Actual C passes **1,024 native32 cases each at O0/O2 with UB traps**.
  Only 112 defined bytes are read or mutated; four indeterminate bytes are
  excluded from native observations. Five source errors exit 3: force/omit
  offset, wrong scale, wrong sentinel and swapped mode/owner arguments.
- The actual parent passes **256 cases per stream**, all 45 words, disabled
  and boundary timers, callback slots 0/1/skipped, post-callback marker clear,
  provider record mutation and second-argument preservation. The unchanged
  slot 1 callback and common tail provider remain opaque; this is not a claim
  that either has been recovered or that gameplay reachability is established.
- Both complete owner padders preserve 38 neighbors and pools. All145 raw-word
  and seven binding corruptions, ten actual stale-CSV cases, and three
  independent provider/data rebases across HI/LO carries are checked.

The first suite passed, but review found its native mutator touched private
padding. That packet and immutable snapshot remain under `adoption/`.
The accepted `adoption-v2/` mutator accesses only defined bytes and has fresh
qualification. Seeded guest/proof observations still cover the whole frame;
no historical snapshot or failed/superseded receipt was weakened or credited.
These are nonfaulting compiled-instruction and finite native checks, not
portable padding contents, hardware fault-state or gameplay acceptance.

## Production and retained evidence

The immutable **1,261-input** baseline begins at consumer `2b581d0f` /
tools `cf5ca381`. Exactly four installed inputs change: owner source, guard
CSV, owner object and ELF; the other 1,257 stay exact. All predecessor freezes
and explicit adoption overlays remain preserved.

The independent five-command actual Make shadow agrees for all 39 raw owner
functions. Production Make builds the source and guards without prebuilt
object copies. Its complete ELF equals the prediction: **515
changed bytes, zero strict exclusions**. Four symbol/string-table permutations
preserve identical named definitions; only this function's size changes from
12 to 580 bytes. A separate canonical-definition and literal-byte audit also
rejects changed symbol values, names, protected data and target instructions.
All other 6,050 linked bodies, every address, 38 owner neighbors and pools
remain exact; only one of 698 production objects changes.

All **189,088 protected bytes / 720 owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA256:
`c3aa38c36a4e4d71eccdf96390a8707640d11aa280fb2090eb5b9ed565019a59`.
Production progress and project-tool checks pass. Older whole-owner receipts
remain historical; only fingerprinted unchanged semantics are reused alongside
the fresh complete owner/image audit. No Claude call was needed.

Receipts: `conker/build/game-next-151a2f0c-private/adoption-v2/`.
The root README changes only Total/Game aggregate rows. Graphify receives a
retained-ID scoped AST refresh, not a full-corpus re-extraction claim.
Tools are committed before consumer source/pin/docs; no push or host
Release/save change is included. Next candidate: `func_151A3150`.
The wider 85% goal remains active.
