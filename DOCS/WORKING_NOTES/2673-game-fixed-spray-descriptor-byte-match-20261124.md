# Fixed spray descriptor byte match - 2026-11-24

`void func_150C2290(u8 channel)` now replaces its zero-return placeholder
with the complete **101-word / 160-byte-frame** fixed spray constructor.
The recovered 136-byte descriptor has typed float, halfword, byte and word
fields. Eight expected-word guards rotate one constant load through a closed
scheduling block; the other 93 words and all nine relocation sites already
match. No instruction insertion, omission, arithmetic or call-binding patch.

Production rises from **4,652 to 4,653 / 5,528 (84.17%)**. Game is
**3,980 / 4,855 (81.98%)**; Init 492/492 and Debugger 181/181 remain fixed.
There is zero address drift and 875 functions remain different; **46 more
matches reach 85%**. Only the constructor receives additional credit.

## Packet, interface and retained bytes

Owner `conker/src/game_EF410.c`; original
`conker/asm/nonmatchings/game_EF410/func_150C2290.s`. VA
`150C2290..150C2424`, ROM `EF740..EF8D4`, 404 bytes. Incoming A0 is homed
at old SP, masked to eight bits for A1, and passed to
`func_15151A38(&descriptor, channel, 1)`. RA occupies new SP+20; the packet
occupies SP+24 through SP+159. The original caller loads its channel from
SP+0xE0 and narrows S0 in the call delay slot; its result is unused.

Four float words come from `D_800A0258/025C/0260/0264`; fixed float values
are 40, 39, 1, 100 and 57.5. Other offsets retain explicit field names where
their meaning is not established. No floating arithmetic is introduced.

The descriptor is **136**, not 132, bytes, consistent with already recovered
spray callers. Retail leaves offsets 0x3B, 0x57, 0x7E..0x7F and 0x84..0x87
unwritten. The original helper reads the last word at `15151ADC`; preserve
that existing behavior rather than silently zero-initializing it. Guest tests
compare every packet byte under coupled, varying entry-stack contents.
Native tests read only defined fields; native uninitialized-field semantics
and complete original-helper execution are not claimed.

`func_15151A38` in `game/generated_17CAF0.c` is corrected to the observed
`void(void *, u8, s32)` interface, consistent with the existing typed callers.
Its body remains an explicit **ABI-only placeholder**: three incoming word
homes, JR RA and NOP, five words. The original 205-word routine is not
recovered or credited. Guest checks preserve the entire supplied descriptor,
SP, RA and saved registers, permitting only the three incoming homes and
ignoring a void result. Whole pristine aligned-ROM census finds one target
JAL and nine helper JALs, no entry pointers and no unidentified owners.

## Scheduling relation and focused qualification

Raw words 39..46 contain one private byte store, six independent constant
definitions and `LUI AT,0x3F80`. Retail moves the LUI to the opening position.
An independent symbolic evaluator proves the same complete GPR state,
private byte state and memory-access trace for arbitrary initial registers
and private bytes at the block join. The block has no call/branch entry,
relocation or FPU arithmetic; the following MTC1 consumes the same constant.
Normal mapped, aligned execution is assumed. Raw interrupted/fault prefixes
inside the block are not claimed identical.

* 1,024 cases per four guest streams cover all 101 instructions and all 256
  channel values, high argument bits, two stack phases, varying private bytes,
  zero/subnormal/infinite/quiet/signaling-NaN float bits and provider mutations.
  All 136 packet bytes, complete memory traces and final machine state agree.
* 102 normalized/retail fault-prefix triples; raw prefixes excluded. The
  original three-word caller window passes three cases per stream. These
  bounded windows do not claim complete enclosing caller execution.
* Native SDK32 at O0/O2/O3, strict aliasing and UBSan: 1,024 cases per profile.
  Six source controls produce observed comparison exit 42; no crash or
  sanitizer trap counts as a control. Signaling NaNs remain guest-only.
* 110 raw-word/binding pins; both padders reject 16 corrupted guarded words
  and preserve visibility of 204 other word/binding corruptions. Both reject
  the oversized fixture. Sixteen real GNU links and 32 guest rebase runs cover
  HI carry, negative LO and distinct JAL regions.

Both complete padded owners agree across the two padders. All **17+40** raw
and padded neighbors, normalized pools and compiler diagnostics remain fixed.
The ordinary owner has no whole retail ASM slice: its second-padder geometry
is synthesized from the same frozen slot layout, not an independent layout.
Actual Make replays six constructor-owner commands, including its existing
motion-pool checker, and five helper-owner commands. Old unaffected function
suites are not described as fresh regression runs.

## Independent image, receipts and bank

The independent reference recompiles frozen before-C and replaces only the
target with original ASM plus the explicitly derived five-word ABI stub.
It reconstructs every named ELF definition and string from the frozen image;
only the two justified function sizes and bodies change, with permitted
symbol/string ordering reconstructed from the reference. The actual C image
equals that prediction byte for byte: **333 changed bytes, zero exclusions**.
All 189,088 protected Game data bytes across 720 owners, unrelated objects,
function addresses/extents, conversion CSV and the old guard prefix remain
fixed. Exactly eight target guard rows are appended.

ELF SHA256: `cab0d155d9e3c3065451a3b6a3bcf50b4f670637b39d918accff33a9e9e8d4df`.
Padded constructor owner: `bd6d42e71bf0630c46838e8a4b45dff57e61bde078f3b6f8c4306732f9a56e62`.
Padded ABI-helper owner: `e191e25a54c906d53c70a309a2477391ad68b977273a2a9c23ba59f100a8daeb`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 90.113s | 5 fresh / 0 reused |
| preinstall-sibling | 78.441s | 5 fresh / 0 reused |
| installed-primary | 69.474s | 5 fresh / 0 reused |
| installed-sibling | 80.923s | 5 fresh / 0 reused |

Final receipts include the motion-pool checker and manifest, independently
verified against the frozen tools commit before adding them to the input
ledger. Earlier exploratory/overlay-incomplete receipts are archived and not
credited here. Shared tools-check passes. Tools commit
`b1c69f7503757fa2b24ddf39546b52ccbed17090` precedes the consumer commit.
The real dirty sibling tools checkout is preserved. Root README receives only
two aggregate-row edits; all old bytes in the five DOCS indexes are retained.

Normal Graphify update, actual commit-hook completion, scoped AST refresh,
old-ID/qualification retention and current-definition auditing have distinct
receipts. The helper and prototypes receive zero added credit; this is not
full-corpus extraction. Host scene configurations were inspected: no direct
C owner consumer or complete host build root exists there. No host/Release
edit/build, push, WSL restart or Claude model request. The 85% goal stays open;
the dimensions draft 15015FBC and older renderer 15197148 remain private.
