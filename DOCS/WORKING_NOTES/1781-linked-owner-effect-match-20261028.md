# Linked-owner effect - guarded C match

Verified 2026-10-28. Restore func_151918BC in generated_1BA1D0:
VA 0x151918BC..0x15191980, ROM 0x1BED6C..0x1BEE30, 49 words / 196 bytes.
The complete semantic body uses the normal O2/g3 profile. Raw IDO output is
50 words; eleven expected-word guards produce the exact 49-word retail body.
Both forms preserve frame 48 and the saved release flag at incoming SP - 9.

## Recovered behavior and interface

The recovered interface is void func_151918BC(u8 *record). Release the record
when its owner is inactive or its saved owner identity no longer matches.
When the link is valid and the owner capability word is nonzero, prepare the
12-byte payload, submit the effect, and release the record. Otherwise retain it.

| Field | Recovered use |
| --- | --- |
| record +0x01 byte | Effect context argument |
| record +0x0C byte | Effect group argument |
| record +0x0D bit 0 | Copy the remaining lifetime and set payload flag bit 0 |
| record +0x0E signed halfword | Remaining lifetime |
| record +0x28 pointer | Owner pointer and start of the 12-byte payload |
| record +0x2C byte | Saved owner identity |
| record +0x2E signed halfword | Payload lifetime; defaults to 300 |
| record +0x30 byte | Payload flags |
| owner +0x00 word | Live-state gate |
| owner +0x3B byte | Current identity |
| owner +0x1D4 word | Effect capability gate |

The two-word unused local reserves the retail frame and release-byte spill.
The helper may clobber caller-saved registers; the final release decision is
reloaded after it returns. Tests qualify that guest spill explicitly without
claiming that arbitrary writes into a C caller's frame are portable C behavior.
The existing helper placeholder interfaces remain unchanged and receive no
recovery credit. No new translation unit, profile or shared header is added.

## Checked normalization

All prior guard-manifest bytes are retained exactly. Eleven appended entries
check the actual raw words and require no relocation on each edited word:

- Remove the second a0 = record + 0x28 at raw offset 0x70. The earlier
  identical calculation remains live, with no intervening write to a0.
- Retarget the three branches at raw offsets 0x40, 0x50 and 0x68 that cross
  that omitted word. The two call relocations move from 0x98/0xAC to 0x94/0xA8.
- Swap independent address/release initialization at 0x5C/0x60.
- Normalize the flag/lifetime scratch-register schedule at 0x74..0x88.
  The lifetime read at record +0x0E, lifetime store at +0x2E, and flag byte
  at +0x30 are disjoint. Source semantics remain unchanged.

The raw compiler body and retail agree on public memory, calls and payloads
for the qualified cases. Their reordered fault prefixes and temporary
register states are not equated. The normalized body agrees literally with
retail, including complete state, access trace, PC and branch-delay behavior.
Each of the eleven expected words has an effective stale-word rejection test
through the actual production padder. Three independent GNU layouts qualify
both relocated call bindings and all 49 normalized instructions.

## Original dispatcher and helper

The full ROM census finds no direct JAL/J to the target and one address
literal at ROM 0x22EFDC / VA 0x8008A51C: slot 13 of the 98-entry
D_8008A4E8 table. Its adjacent D_8008A4C0 exit table contains ten entries.
Both tables remain fixed and equal retail.

The complete 45-word func_15149264 dispatcher executes in 144 cases,
covering slot 13 and disabled selectors, optional lifetime decrement,
expiry, exit callback and final release. Every dispatcher word is visited;
its current C implementation remains byte-exact and unchanged.

The complete original 52-word func_15190770 helper executes in 72 cases,
covering successful and failed allocation, payload mutation and both stack
phases. It captures the owner pointer/identity, requests a type-32 effect,
copies all 12 payload bytes, initializes pointers/fields, zeroes its working
area and stores a random byte. Every original helper word is visited.
Its current production placeholder remains unchanged and uncredited.
Preparation, allocation, memcpy, bzero, random and release services are
bounded providers. This verifies the instruction interface and selected
integration paths; it does not establish whole-game or hardware acceptance.

## Qualification and strict integration

Both active and older tools copies pass eight fresh canonical methods and
the shared tools checks. After production, each passes two fresh installed
checks; six semantic checks are reused only with exact module, input,
fixture and qualified-artifact fingerprints.

- 1,572 guest cases cover all flag/group/context bytes, signed lifetime
  boundaries, four owner/record alias layouts, helper mutations and saved
  release-byte probes. Public routes visit 48 words; the original unreachable
  duplicate identity load remains present in the complete 49-word match.
- 786 fired access-prefix pairs compare retail and normalized complete
  state/trace/PC/delay. The inactive-owner route skips identity/capability reads.
- Native32 O0/O2/O3 each pass 262,144 cases, including all 65,536 lifetime
  encodings under four gate patterns. Typed records, the one-pointer void
  ABI, whole-record/owner fences and trapping UBSan are checked.
- Nine native semantic mutations and nine separately compiled IDO mutations
  fail observably. A first negative-control fixture had already-set payload
  flag bits; the corrected zero-bit witness rejects the wrong OR operation.
- Three GNU layouts run 48 guest cases with original, raw and actual-Make
  objects. Three raw/binding corruptions, eleven real-padder stale guards and
  six complete-image corruptions are rejected.
- The three-command owner Make recipe reproduces the qualified object.
  All 60 other owner functions, their bindings and constant pools stay fixed.
  The target emits no diagnostics. Four inherited Warning 712 diagnostics
  remain in two unrecovered neighboring helpers. Make retains its unrelated
  duplicate generated_12D630 recipe warning.

The qualification seal covers 16,365 files and 373 focused frozen inputs.
Production permits exactly 136 changed ELF bytes: 135 code bytes and one
symbol-size byte (12 -> 196). There are zero exclusions. All 6,056 function
addresses, the other 6,055 bodies and 720 protected Game owners / 189,088
bytes remain fixed. Progress CSV, shared headers, caller source, Makefile,
layout manifest and inherited guard rows remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Raw 50-word compiler body | cac0c76cac792ddf27064a6fd7c44f1a36b5a6e5f9f73a3f93bda64ecab25205 |
| Linked 49-word retail slot | 5578fde1cc5e213328fe803d0c0e5bc61f0b8341093e819b542f2027b7415d6c |
| Adopted ELF | c7173a57ca1782fd61e4c170a0b9aa6d8429df8bb393b582bfc1cde0c0d08865 |
| Appended guard manifest | 2644438e9057a3ce98cd58c2af11503e38a2cec39164719b1e010ed07dcefd24 |

## Bank and measured progress

Predecessor consumer: e9545765685f7d6c9bedca04bcb08e21fde55a0a.
Tools committed first: 663e4308980fa4fdfc05192edaf07afebad03b80.
Preserve all 1,784 inherited dirty paths in the older tools mirror; add only
these three qualification modules there. No push performed. Routine Claude
calls: zero. Graph refresh is scoped AST work with old-node and relationship
retention; it does not claim full-corpus extraction or global reclustering.
Raw receipts: conker/build/game-linked-owner-effect-match/.

| Section | Byte-exact C | Different | Address drift |
| --- | ---: | ---: | ---: |
| Total | 3,859 / 5,506 (70.09%) | 1,647 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,186 / 4,833 (65.92%) | 1,647 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The adopted native ELF recount leaves 271 more exact C functions to reach
4,130 / 75%. Next inspect func_151A483C; the queue is only a screen.
func_1514E920 remains parked and uncredited.
