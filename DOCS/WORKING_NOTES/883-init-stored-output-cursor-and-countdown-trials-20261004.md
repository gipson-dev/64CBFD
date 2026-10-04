# Init Stored Output Cursor And Countdown Trials

Date: 2026-10-04. Baseline: `29c409f7`, unchanged Notes 879-881 sources.

## Selection

The packed stored loop reloads the output base and adds its produced index
after each `take_bits(s, 8)` call. Two new forms were measured with the
complete retained packed-remaining flag set, including first-refill lookup
and table-derived builder allocation. Both leave generic bit extraction,
length/complement handling, capacity check and final produced commit intact.

The output-cursor form initializes `cursor = s->output + produced` and
`stop = cursor + length` after the capacity check, then stores extracted
bytes with `*cursor++` until the pointers match. It caches the output base
across helper calls and writes; arbitrary state/output alias behavior is not
claimed. The countdown form instead retains indexed output and iterates
`while (length--)`, avoiding a produced/end comparison while retaining end
for the final state commit. Neither discarded form was guest-qualified.

[Note 851](851-init-stored-shared-length-extraction-and-failure-bit-state-20261003.md)
already rejected specialized eight-bit extraction. That form was not repeated.

## Measurements

| Form | O2 core text | O2 stored body/slot | O2 stored frame | O1 core text | O1 stored body/slot | O1 stored frame |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Qualified baseline | 4,384 | 54/54 | 48 | 5,824 | 67/67 | 40 |
| Output pointer cursor | 4,400 | 57/57 | 72 | 5,840 | 69/69 | 48 |
| Length countdown | 4,400 | 57/57 | 56 | 5,840 | 71/71 | 56 |

Both trials increase whole core text sixteen bytes in each profile. Pointer
form enlarges the stored frame 24/O2 and 8/O1 bytes; countdown enlarges it
8/O2 and 16/O1. The maximum core direct-call bound remains 392/O2 and 352/O1,
because another path still dominates. Unchanged maximum does not mean the
stored path's frame cost is unchanged. No linked/guest trial acceptance is
claimed. All four trial compiler logs are empty.

Ignored trial receipts and disassemblies:

- `conker/build/init-stored-output-cursor-trial-20261004/`
- `conker/build/init-stored-length-countdown-trial-20261004/`

Baseline receipts are `conker/build/init-limit-baseline-20261004/` from
Note 882; its two compiler logs are also empty.

## Restoration And Verification

Both edits are removed. The semantic source matches qualified blob
`bdc96bf5835c86bdd67a495e60f8a5b63cbe9071` exactly, with empty scoped diff.
Thirteen focused retained tests pass in 14.635 seconds, no skips: slot ledger,
corpus selection, FR=1 word loads, packed-profile size, executed callee-clobber
guard and stored bad-complement bit-count preservation. Relevant guest tests
freshly compile/link all six retained shapes. Project tool and whitespace
checks pass. No full bounded/corpus rerun is claimed here.

Notes 880/881 continue qualifying 1,014 paired pages for the restored
direct-load baseline, not these discarded alternatives. Linked O2 stays
4,576 bytes / 592 excess; core bound 392, total bound 3,240. Production
remains 492 C / 47 assembly rows. No option, production conversion, ROM build
or sibling-port test is added. Defaults/README stay unchanged; unrelated
Game edits are preserved and unstaged.

## Next Work

Do not repeat these loop forms unchanged. Continue fitting based on complete
text and per-path frame costs, with entry/frame ownership, full reservation
and hardware/context gates still open before production promotion.
