# Fixed descriptor constructor matched with one commutative-add guard

Date: 2026-11-07. Continues [Note 2155](2155-game-record-state-service-dispatch-match-20261107.md)
from consumer `9113f552c7b7256e82577d7999a7e88bec981e34` and tools
`bbac1f13ef9bbe01a18993fd0e6d3729bc48561b`. One additional qualified Game
function advances the active 80% total goal.

## Recovered descriptor, live payload and returned handle

`func_1513BAE8(void)` in `conker/src/game_168A90.c` replaces its zero-return
placeholder with **69 words / 276 bytes**, VA 0x1513BAE8..0x1513BBFC,
ROM 0x168F98..0x1690AC. Ordinary O2/g3, MIPS2/O32 gives the original
120-byte frame, RA at SP+0x1C, descriptor at SP+0x38, five-float payload at
SP+0x24 and saved handle home SP+0x74. All three JAL relocations stay fixed.

The 60-byte descriptor initializes 44 bytes; its 16 padding bytes remain
unspecified C padding. Offset names retain uncertainty about resource semantics.
The fixed fields are recorded directly in the candidate and independent model:
bytes 0/1/2 = 0/2/5, halfword 4 = 300; words 8/C/10/14/18/1C/20 =
1/0x220205/0x40600/1/54/128/32; bytes 24/25 = 0/0; words 30/34 =
9/430; byte 38 = 3. All five payload floats begin as positive zero.

Call `func_1513B5E0(&descriptor,1,20,255,1)`. A zero handle skips both
release and copy. A nonzero handle whose word +0x50 differs from 0x1180
is released through `func_1516972C`. Otherwise reload word +0x50 and copy
the live 20-byte payload to handle+word50+0xF8. Return the original handle
word even on the release path. It is held as `u32` so address arithmetic
wraps in the established 32-bit ABI without signed-add overflow; the
existing `s32` return transports the same bits. No C pointer is retained
and read after deallocation.

Descriptor assignment order matters: placing words 30/34 before the
middle fields reproduces retail's constant-register lifetime and the
independent outgoing fifth-argument constant. The first draft was68 words;
the recovered order gives69. Changing commutative source spelling does
not change the final add's operand preference.

The complete raw body hash is
`a138487343daddcd2774f576d10fe102b8d64856d52e107747272d567226c6cc`.
One expected-word guard at body offset0xF0 changes `0x01272021` to
`0x00E92021`, swapping the two sources of an integer `addu` into A0.
It changes no opcode, destination, immediate, relocation, instruction
position, branch delay or frame. Raw, guarded and retail bodies have
identical tested full machine states, including fault prefixes.

All **12 raw and padded neighbors** are literal. Four existing pointer
diagnostics remain identical; no new warnings occur. The factory dependency
remains its preexisting production placeholder. A typed five-argument
definition screen added four incoming-home stores to that unrelated stub,
so it was rejected rather than changing its bytes. The original creator's
complete 110 words validate this call boundary in connected tests; its
own C restoration remains a separate task with no new credit here.

## Register metadata and complete-image accounting

The new target genuinely uses additional GPRs and F0. Raw `.reginfo` moves
GPR mask0xA300C77E -> 0xA300FFFE and FPR mask0 -> 1. The verifier decodes
the target's actual register operands and requires exactly their union
with the predecessor masks. All other mask words, GP value, section
geometry, data and relocations remain fixed. The 32-byte `.options` record
must retain its eight-byte header and contain exactly the same derived
24-byte register-info change. There is no broad metadata exclusion.

The real plain-owner `pad_c_object` path emits instructions as words;
both padded owners' register masks remain literal 24 zero bytes, with
unchanged ABI flags and other allocatable pools. The final linked ELF
needs no register-metadata allowance or symbol/string permutation.

Actual Make recompiles only this owner and equals the independent complete
ELF prediction: **212 changed bytes, zero exclusions**, solely the target
slot and symbol extent12 ->276. All 6,052 function addresses stay fixed;
only this body changes. All 189,088 protected Game bytes across 720 owners
remain exact. Conversion CSV and Makefile are unchanged. Compile/link pass;
`make all` reaches the expected nonmatching whole-image checksum, exit 2.
The preexisting duplicate generated_12D630 recipe warning remains.

## Focused validation and its bounds

Seven checks pass before and after installation in both tools configurations.
The 136 frozen inputs include target/all-owner original assembly, creator,
caller source/assembly, SDK/compiler inputs, old ELF, linker/layout/registries,
conversion CSV, guards and graph. Imported helpers and new modules are
fingerprinted, including the actual plain-owner padder. The sibling uses
its available helpers through a disposable new-module overlay, with its
missing `alloc_pools` recorded as a hashed, read-only mounted fallback.
All 2,434 inherited dirty sibling paths remain fingerprinted and unchanged.

* **436 guest cases per body** compare retail, raw and guarded code
  with an independent byte model: all 69 target words, all 60 seeded descriptor
  bytes, live 20-byte payload, allocation failure, exact/mismatched/extreme
  header words, retained release handles, three stack-copy aliases and
  argument/private-home mutations. Sparse guest handles cover the signed
  address boundary and32-bit wrap. Those address and private-frame cases
  are guest-only, not portable native pointer claims.
* **20 cases per body** connect the complete 110-word creator and11-word
  original SDK copy. Every 121 helper word executes. The creator copies
  all 60 descriptor bytes, derives resource sizes and view buffers, copies
  resource data and publishes word50 before this target validates it.
  Resolver, allocator, release, setup and resource-tail services stay bounded.
  The creator's production placeholder remains unchanged.
* **72 cases per body** execute the complete18-word original one-shot caller
  `func_150E0300`. All 18 words execute; it is already exact in production.
  The aligned retained-input census finds the sole target JAL at ROM 0x10D7D4,
  with no entry/interior pointers. Its returned handle is ignored.
* **598 fired access cuts**, including 216 delay-slot cuts, preserve complete
  private memory, GPR/FPR/HI/LO, PC and access prefixes for all three bodies.
  These are emitted guest instruction-order checks, not portable C fault
  semantics or hardware/gameplay acceptance.
* SDK native32 O0/O2/O3 each pass 100 independent little-endian byte fixtures,
  with size/offset assertions and UBSan traps. The defined 44 descriptor
  bytes are checked; 16 padding bytes are explicitly excluded. Seven compiled
  negatives fail with exit 1: old stub, wrong descriptor constant, nonzero
  payload field, wrong size gate, short copy, clearing the released handle,
  and omitting release. The native release provider retains its fixture
  storage; no actual native deallocation or private-frame mutation is claimed.
* Two GNU links/rebases independently validate the three JALs. Four
  whole-ELF header/body/symbol/string corruptions and two object register-
  metadata corruptions are rejected.

Initial fixtures accidentally overlapped the allocation arena with guest
STACK0x40000 and included an oversized resource case beyond the fixture's
arena. Native byte hashes and a guest unmapped-store assertion rejected
those assumptions. The arenas are now disjoint with explicit assertions;
the connected cases fit their mapped storage. Measured creator coverage is
110/110, correcting an initial108-word expectation. No production behavior
or acceptance gate was weakened. The final unsigned-handle source emits
the same raw 69 words and was freshly requalified.

Shared smoke checks pass freshly in both copies. Three unchanged shared
regression receipts per copy are explicitly reused after exact fingerprints
against Note2155. Claude calls for this constructor: zero.

## Separate private func_150A25D4 investigation

The pending adjacent record-mode updater remains uninstalled and uncredited.
Its preferred source emits 108 of 110 words with frame40 and27 unchanged
neighbors. A new independent guest model passes 4,999 finite cases per body,
including all mode/timer bytes, 64-bit flag positions, service mutations,
selector widths, aliases and fieldB2 boundaries. This establishes finite
public behavior, not matching, private/fault equivalence or completion.

Timer expression/storage/actor-field forms and register hints retain the
same mismatch. Actual supported O1/g3 compilation was checked directly,
after the asm processor rejected that flag pair; it gives 134 words and
does not solve the mismatch. Ordinary O1 and non-g3 O2 also reject, with
changed neighbors. No profile change or manufactured liveness was installed.

One packet-only advisory for that distinct private task completed through
the verified existing claude.ai/firstParty Pro route, tools=[],
mcp_servers=[], tool uses0. Packet hash:
`9f93d2b006b2e54ebd6cb033bc5c0e038726ffb7874ca090f3177e8f8aaf2f4a`;
answer hash:
`adc729365f3e487b9ec4fb909fa18ae51618675ab4cc3f8585da27963b45711a`.
Disposition: the O32 u64 alignment interpretation is independently supported;
a proposed extra record use is rejected because no such retail access exists.
Register-pressure causation remains a hypothesis. No further call is needed
for repeated unchanged evidence. Ignored packet, response, probes and semantic
receipt remain in `conker/build/game-record-mode-update-150A25D4-private/`.

## Production progress and continuation

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,226 / 5,512 | 76.67% | 0 | 1286 |
| Game | 3,553 / 4,839 | 73.42% | 0 | 1286 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**184 additional exact functions** remain to 4,410/80%. Root README receives
aggregate rows only, and four current indexes get a concise lead with their
historical text preserved. Graphify refresh retains old nodes outside changed
paths and excluded-but-existing legacy files fail-closed; this is a scoped
refresh, not fresh full-corpus extraction. Commit tools first, then consumer
source/guard/docs and exact pin, followed by fresh hook/preservation audit.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `ee48bfffbe008eacf28903e17c86bd7ce0c3a0db40db31fbcfe40fe24cf45fdd` |
| Production binary | `6cc606add0c09131c7422c5f4358481959b207fac61f4b770aef6627ca8dd133` |
| Padded owner | `26ed73e96dc325ba4834569db439f7cd712ceebfff4e98cb2b8ab5c8a193ad87` |
| Guard manifest | `b6b276d1ee5e6e69bcbd1cc995318ea562379c6716817fabfc1d1b4d3becf3f4` |

Qualification, pre/post suites, shared checks, actual Make, graph retention
and post-commit receipts remain ignored under
`conker/build/game-fixed-effect-factory-1513BAE8-match/`.

Next: **func_1513B5E0**, the 110-word creator dependency in the same owner,
VA 0x1513B5E0..0x1513B798, ROM 0x168A90..0x168C48. Its original instructions
and independent resource/view/copy model are now connected and exercised.
Recover its C body and proper five-argument definition, preserving live
view-count reloads, allocation failure, resource copies, returned handle
and complete owner/image gates. Keep the wider 80% goal active; preserve the
frozen handwritten/hidden-ABI boundaries, private inputs/saves, unrelated
work and frozen host Release.
