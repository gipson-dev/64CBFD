# Init Core Limit Predicate And Local Lifetime Trials

Date: 2026-10-04. Qualified baseline: `acf0ed8c` (Notes 879-881).

## Hypothesis

The core starts its output limit at 0x70000000 and replaces it with the
signed input-output distance only when that distance is positive. Therefore
the limit is in 1..0x7FFFFFFF before the workspace-distance check.
For any 32-bit signed workspace distance, `distance >= 0 && distance < limit`
has the same truth value as `(uint32_t)distance < (uint32_t)limit`: a negative
distance converts to at least 0x80000000, which cannot pass the unsigned test.
The hypothesis was that eliminating the explicit sign gate would save text.

A second form kept the limit in a local, initialized using a conditional
expression, applied the unsigned workspace comparison, then stored it once.
This changes intermediate state-store timing; no asynchronous or guest
semantic qualification is assigned to the discarded local form.

## Measurement

Both IDO profiles use the complete retained packed-remaining option set,
including first-refill lookup and table-derived builder allocation. Each
trial freshly compiles both profiles and emits normal measurement receipts.

| Form | O2 core text | O2 entry body/slot words | O2 core bound | O1 core text | O1 entry body/slot words | O1 core bound |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Qualified baseline | 4,384 | 52/52 | 392 | 5,824 | 86/86 | 352 |
| Unsigned workspace predicate | 4,384 | 50/52 | 392 | 5,824 | 85/86 | 352 |
| Local limit plus unsigned predicate | 4,384 | 50/52 | 392 | 5,824 | 85/86 | 360 |

The predicate saves two raw O2 body words and one O1 body word, but trailing
padding absorbs both savings. The local form does not improve text and
increases the O1 direct-call frame bound by eight bytes. Neither form is
retained. No new CLI option or source branch remains.

Ignored receipts and disassemblies:

- `conker/build/init-limit-baseline-20261004/`
- `conker/build/init-limit-unsigned-trial-20261004/`
- `conker/build/init-limit-local-unsigned-trial-20261004/`

All six compiler logs are empty. These are size/code-generation measurements,
not execution qualification of either discarded form.

## Restoration And Checks

The semantic source is restored exactly to Git blob
`bdc96bf5835c86bdd67a495e60f8a5b63cbe9071`; its scoped diff is empty.
Twelve focused tests pass in 6.421 seconds, no skips: slot ledger, corpus
selection, FR=1 word loads, packed-profile size and the executed callee-clobber
negative guard. The last two checks freshly compile/link all six retained
shapes. Project tool and whitespace checks pass.

Notes 880/881's 1,014 paired pages still qualify the unchanged retained
configuration; they are not reassigned to either discarded trial. No full
bounded or corpus rerun is claimed here. Linked O2 remains 4,576 bytes,
592 over the 3,984-byte retail group, with packed core bound 392 and total
descent bound 3,240. Production remains 492 C / 47 assembly rows.

## Next Work

Continue fitting using complete linked size and stack bounds, not raw body
word counts alone. Do not repeat these forms unchanged. Entry/frame ownership,
full reservation and hardware/context gates remain open. No production ROM
build, sibling-port test or conversion is claimed; README totals and defaults
stay unchanged. Unrelated Game source/tests remain preserved and unstaged.
