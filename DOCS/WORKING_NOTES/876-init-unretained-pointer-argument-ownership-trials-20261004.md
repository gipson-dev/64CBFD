# Init Unretained Pointer Argument Ownership Trials

Date: 2026-10-04. Baseline: `d44975b9`.

## Result

Three core pointer/address sourcing trials and a matching adapter-store
omission offer no aggregate size improvement. All temporary edits are removed;
both core and adapter source are restored exactly to HEAD. No new option,
default or production conversion survives.

## Ownership Hypotheses

The retained adapter stores input/output/workspace/frame pointers into state,
and forwards numeric input/output/workspace addresses as core arguments.
Six zero/counter initializers were already removed in Note 853; callee reloads
were removed behind Note 875's opt-in symbol. Remaining pointer stores are
not simply redundant zero initializers: the core/header and stream read them.

The direct input trial reads the header from inputAddress and initializes
s->input from that argument plus the two/four-byte opening length. This
could permit omitting the adapter's input state store under its guest pointer
equality contract. The workspace trial instead assigns workspaceAddress from
s->workspace, potentially eliminating the fifth argument store. The combined
trial applies both. No output/frame ownership change is made.

These are guest-only source hypotheses. Native tests intentionally distinguish
host pointers from numeric guest addresses, so the direct pointer casts are
not general native replacements. No native, arbitrary-alias or guest semantic
qualification is claimed for the discarded forms.

## Measurements

Complete retained Note 873 core configuration with the Note 875 adapter:

| Core sourcing | O2 core bytes / core bound | O1 core bytes / core bound |
| --- | ---: | ---: |
| Retained baseline | 4,384 / 392 | 5,824 / 352 |
| Input from argument | 4,384 / 392 | 5,824 / 352 |
| Workspace address from state | 4,384 / 392 | 5,840 / 352 |
| Both | 4,384 / 392 | 5,824 / 352 |

All O2 core public bodies remain 52 words. O1 stays 86 except workspace-only,
which grows to 90. The workspace trial's first compile fails IDO's C89
declaration-order rule because an assignment preceded ABI-seed declarations.
Moving the assignment after those declarations/seed statements resolves the
syntax issue; the table contains only completed corrected compile receipts.
All six final compiler logs are empty.

For the combined trial, the adapter's state input store at SP + 0x20 and
fifth-argument store at SP + 0x10 are removed, retaining all other stores and
Note 875's callee-preserving selection. GNU assembler emits a 248-byte body
(end symbol 0xF8), but object .text remains 256 bytes. Fresh links of the
combined O2/O1 objects emit 4,640/6,080 text bytes: identical to the retained
configuration. No semantic execution of these trial links is claimed.

Ignored receipts:

- `conker/build/init-core-input-argument-direct-20261004`
- `conker/build/init-core-workspace-field-direct-20261004`
- `conker/build/init-core-input-and-workspace-direct-20261004`

The last contains the store-omitted adapter object and both trial linked ELFs.
Unaligned body savings must not be reported as aligned/linked savings.

## Restoration And Next Work

Scoped `git diff --exit-code` passes for both experiment sources after
restoration. Fifteen helper/ledger, retained-size and executed-clobber guard
tests pass in 7.024s, no skips. These freshly compile the restored six-shape
configuration and verify its callee contract; they do not qualify trial code.
Project tool and whitespace checks pass. No whole guest suite, changed full
corpus, production ROM build or hardware run is claimed this turn.

Retained packed O2 remains 4,640 linked bytes / 656 excess. Do not repeat
these ownership forms unchanged as aggregate improvements. Size fitting and
the retained first-refill/callee-adapter combination's full masked CU1-clear
and CU1-set corpus remain open, as do connected ownership/hardware gates.
Production sources, defaults, progress CSV and README counts are unchanged;
unrelated dirty Game source/tests are preserved and excluded from staging.
