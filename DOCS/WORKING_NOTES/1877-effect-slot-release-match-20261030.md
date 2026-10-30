# Note 1877: effect-slot release and nested iterator matching

2026-10-30. `func_150E35DC`, owner `generated_1104D0`, replaces its zero-return
placeholder with `void func_150E35DC(s32 handle)`. VA
`0x150E35DC..0x150E36BC`, ROM `0x110A8C..0x110B6C`: the complete 56-word,
224-byte slot is byte-exact after five expected-word guards with one scheduling
insertion. The semantic C emits 55 words with the retail 48-byte frame and all
five saved S-register lifetimes. This is a normalized match, not a direct raw-C
word match. Tools commit: `baf53e524513fcc3fbed74b8825c818d998601fb`.

## Recovered behavior and ABI

The handle is decremented with 32-bit wrap: zero selects all records and
positive handles select an unsigned node slot byte at +0x48. The function scans
two 0x1A0-byte rows in `D_800DCE50`; each list head is at row+0x9C. The pool ends
at the physical address of signed byte `D_800DD190`. Its row-end and depth
address roles remain distinct in the emitted code.

Each row reads the depth before its head and increments depth even when empty.
Before calling `func_150E3514(node)`, it stores node+8 in
`D_800DD198[depth]`. After a callback it reloads the live signed depth and saved
successor. On the no-call route it retains the existing cursor. This preserves
callback edits, nested cleanup and a released node whose live next pointer has
changed. It unwinds depth after each row and advances to the second row.

The original call is at `0x1509D844` in `func_1509D780`. Its delay slot computes
the handle with arithmetic `sra a0,a2,6`; the return is ignored. No shared ABI
header or compiler profile changes are needed. RA is saved at SP+44, S0..S4
at SP+24..40. The selected source has no dummy locals or volatile declarations.

## Narrow normalization and source screens

Three guards reorder independent opening low-address materializations for the
pool, depth and end pointer. Two tail guards rotate the existing outer-loop
depth preload into retail's branch-likely schedule, inserting one instruction.
There are no omitted words, frame adjustments or saved-register remappings.
All 11 raw relocation sites and all original output bindings are checked.
Ten padder controls independently reject wrong guard words and bindings.

Plain pointer comparison merges address roles and emits 51 words. Typed rows,
local end pointers, array/struct depth carriers, volatile and register hints,
and computed end addresses do not recover the complete slot. Integer address
comparison recovers 55 words, frame48 and all saved roles. Top-tested while/for
forms produce 56 words with an unwanted entry guard; explicit assignment,
break/continue/goto and loop-step variations do not improve the selected tail.
These alternative shapes remain private and uncredited.

Raw C word SHA-256:
`bed4eb35e3a01869b5dcc886674e2b51af4c8bf582ab8bf91c2d9caedf4f40a7`.
Padded owner SHA-256:
`1e06f4bd9ebd1bdc4dafa420135cdebea0c606ee4a4fd5cb9f342b133657368a`.
Recovered owner source SHA-256:
`b3d954d5ba182eadddee1201116688bef7f87426715ea491a64669e5ec6a5e57`.

## Qualification and boundaries

Ignored evidence: `conker/build/game-effect-slot-release-150E35DC-match/`.
Both tools copies pass eight fresh canonical checks and shared tool checks.
Production repeats two installed checks per copy and reuses six unchanged
semantic checks only through exact input/module/artifact fingerprints.

- Guest: 24,576 cases /73,728 executions, all56 retail words, two row heads,
  empty rows, unsigned slot bytes, wrapped handles, callback mutation and actual
  target re-entry. Raw C, normalized output and retail agree on complete modeled
  final GPR/FPR/RAM, calls, access traces and observations.
- Prefixes: 177 access cuts, including43 delay-slot cuts, match normalized output
  against retail on complete modeled state and the actual PC/delay context.
  These are emitted instruction-order checks, not portable C fault semantics.
- Rebases: 108 cases in three independently GNU-linked entry/global/helper
  layouts, including low-half carries. The physical pool-end/depth adjacency
  is retained while saved-pointer storage is moved independently.
- Extra signed-depth aliases: 96 guest-only cases. Invalid signed indices and
  byte wrapping are not claimed as portable native C behavior.
- Native32: 9,216 cases per O0/O2/O3 profile with trapping UBSan. Real allocated
  nodes, six saved-pointer slots, physical row-end/depth adjacency, callbacks,
  recursive target entry, node bytes and boundary canaries are checked against
  the guest-validated reference. Twelve compiled semantic controls are effective.
  Defective controls use defined, nonrecursive fixtures to avoid UB witnesses.
- IDO controls: twelve separately compiled wrong decrement/filter/slot/head/row,
  late successor, missing unwind and cached iterator variants produce actual
  semantic mismatches. Compiler errors or oracle failures are not accepted.
- Caller: one aligned direct JAL and zero aligned literal pointers in retail.
  144 cases execute the actual two-word caller window, including signed command
  shifts and the ignored return. Earlier/later parent execution is bounded.
- Connected providers: 720 cases load the original/current50-word
  `func_150E3514` and28-word `func_1516972C`; all78 loaded words are byte-exact
  in the current ELF and48 are visited. Slot-table clearing, saved successor
  mutation and actor kinds0/1/2 are checked. Sound handles are zero;
  unlink/fallback remain explicit bounded hooks. No complete release-chain,
  audio, hardware or full-parent execution claim is made.
- Full owner: all12 neighbors and their pools remain fixed, and the actual
  three-command Make recipe reproduces the complete padded owner. Selected,
  owner and Make diagnostics are empty. A semantically equivalent source that
  merges the depth/end address roles is rejected by the raw payload fingerprint.

Failed fixture receipts remain preserved: the first guest driver had malformed
Python ternary spacing, and the first frame check looked for the RA save at
word1 rather than its actual word3. Both were fixture corrections; production
source and guards did not change to accommodate them.

One focused Claude Code Pro advisory was attempted and completed through the
existing claude.ai/firstParty subscription route. Safe mode, disabled tools,
strict empty MCP and no session persistence produced tools=[]/mcp_servers=[]
and no tool use. The scheduling suggestions were independently screened; none
removed the selected normalization. Packet SHA-256:
`5c21caf9c0fcc8092cb08d3c783afb9af65e37f0733075566a62a72df09333f2`;
answer SHA-256:
`15b553ffb948d6aefe0c6d5e6fad002c8900cce75d74157ae1626e0b35b92644`.
No REA call, dependency install, account or provider change was needed.

## Image, measured progress and banking

Production equals the independently predicted complete ELF:
**176 changed bytes =175 target-code bytes +one extent byte**, metadata0,
with zero exclusions. All6,055 other linked bodies, all6,056 addresses and
189,088 Game-data bytes across720 owners remain fixed. Inventory CSV, linker
script and all inherited guard rows remain fixed; five new rows are appended.
All17,031 current sealed inputs are verified under declared changes. The older
tools mirror retains its2,069 inherited changed paths; only three new modules
are added there and that mirror is not committed.

Adopted ELF SHA-256:
`3644a879a659abc0865a85770d7ab5aad6508a52af60821523bc026d6da0c314`.
Actual Native ELF recount: **3,954/5,506 (71.81%)**, Game
**3,281/4,833 (67.89%)**, Init492/492 and Debugger181/181, zero drift.
The75% threshold remains4,130/5,506, requiring **176** further exact functions.

Tools are committed before the consumer source/guard/docs/pin commit. Root
README changes only its two aggregate status rows. Graphify structurally
refreshes the eleven supported changed source/tools/docs files; the guard CSV
is recorded through its qualified hash. Old nodes and valid relationships are
retained, with obsolete placeholder s32 return edges retired from source proof.
No full-corpus extraction, global clustering or centrality refresh is claimed.

Next private screen: `func_151AE7B0`. Private and parked candidates remain uncredited.
The wider matching goal remains active. No push or pause.
