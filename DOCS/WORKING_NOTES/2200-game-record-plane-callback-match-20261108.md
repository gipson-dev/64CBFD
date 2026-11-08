# Record Plane Callback Match - 2026-11-08

`func_151319C4` now has its semantic **78-word / 312-byte C body**, original
**0x40 frame**, and **eight checked normalization words**. All normalized
instructions match retail. The isolated body, complete owner, both padders
and actual Make agree. The literal full-image prediction changes **236
bytes**, with zero exclusions and no metadata permutations.

Production: Total **4,269 / 5,513 (77.44%)**, Game **3,596 / 4,840 (74.30%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,244**
converted functions remain different; **142** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion denominators and the
progress CSV are unchanged.

## Recovered interface and control flow

Owner `conker/src/game/generated_15D730.c`, original `asm/15D730.s`.
VA **151319C4..15131AFC**, ROM **15EE74..15EFAC**. Interface:

```c
s32 func_151319C4(BounceRecord15D730 *record, void *surface,
                  BounceResponse15D730 *response);
```

Reuse the existing bounce record and response layouts, moving their typedefs
before the recovered prototype. Reuse the measured HeightResult71820 layout
and struct17 three-float packet interface. The three existing callers gain
explicit pointer casts; all their raw/padded instructions stay unchanged.
No shared headers or compiler profiles change.

- Default result is the byte value 1. Disabled response flag bit0, signed
  callback index -1, a null callback, or an unordered/false comparison
  `record->position[1] < ((f32 *)surface)[1]` skips all probing and returns1.
- Build point X/plane-Y/Z at private SP+0x30/+0x34/+0x38. Save response at
  SP+0x48, surface at SP+0x44 and the byte result at SP+0x3F. Call the original
  point validator func_1514672C. A zero result returns0.
- For success, compute current record Y minus current extent times
  D_800A3844, then call func_15046C80(point,0,threshold,record+0x80). Its u16
  selector and mixed pointer/float ABI carry threshold bits in A2. Reload
  the saved result byte after the call; a zero height-query result keeps it.
- On a hit, make the contact X/resolved-height/Z packet at SP+0x24/+0x28/
  +0x2C. Reload the response pointer, signed index and callback table after
  both helpers, then call(record,reloadedSurface,contact,response). Return
  the callback's low byte. Do not cache the initially checked function pointer.

Table **D_80089874**, ROM **22E334**, has one retail entry:
**func_15131B7C**. Its owner is `asm/data/22E220.rodata.s`. Scale D_800A3844
has bits **3D75C290**, value0.06000000238418579, ROM **248304**, owned by
`asm/data/2482B0.rodata.s`. The point validator's original bounds are19500
and -9500, in the protected249F40 data asset. All values are pinned to the
pristine ROM and current byte-exact helper slots.

## Closed callback setup normalization

The first typed draft has79 words/frame0x40. Moving the byte result before
the two packet declarations recovers all private homes; an explicit failed
validator return recovers the78-word control-flow shape. A bounded screen
of all six contact assignment orders with array/struct packet forms reduces
the remaining differences from14 to8. Selected source stores contact X/Z/Y.

All differences lie in words54..62: a closed F4/F18 scratch-role swap and
six dependency-checked adjacent instruction exchanges. They move the response
home load, table HI16 preparation, and independent packet setup. Relocations
move with their instructions. Frame size, saved S0/RA, packet/home addresses,
public memory-access order, all branches/calls and argument values stay fixed.
No insertion/omission guards or retail-body copying are used.

The schedule certificate checks GPR/FPR dependencies and stack offsets.
Its one private-store/public-read crossing requires a valid incoming record
disjoint from the newly allocated private frame. The contact packet has not
escaped before this block. F4/F18 are caller-clobbered scratch, not FP argument
or saved-register lanes. Raw public semantics use that valid-object domain;
raw private fault addresses and scratch-register identity are not claimed.
Normalized/original literal execution is checked separately. Raw SHA256:
`742a850fc7258921e26896504b66064cedf427e6717dba1e1b5036d70b6e4469`.

The inherited guard prefix, including the prior color jump-table bindings,
is preserved byte for byte before appending the eight checked rows.

## Qualification and boundaries

Six focused checks pass sequentially before and after installation against
mounted and sibling tools, with exact source/dependency fingerprints.

- **2,124 guest cases**, **27 alias cases** and
  **138 interrupted-access cuts** compare independent complete
  memory, packet/call arguments and returns. All78 target words execute.
  Original/normalized literal states agree. Controlled providers mutate live
  record/point/descriptor/table data, incoming pointer homes and the saved
  byte result to check late reloads. Private-home probes remain guest-only.
- **237 connected cases** run the original30-word
  point validator,32-word height wrapper and44-word bounce callback. They
  cover inclusive point limits, float threshold/damping and settled/moving
  response branches. Under valid classifier outcomes0/1/2, height-wrapper
  offsets0x44/0x48/0x6C are not reached; all other helper words are reached.
  The classifier/delegate terrain queries remain bounded providers.
- **288 cases** execute all three complete original callers:
  func_151319A4 (8 words), func_15131AFC and func_15131B3C (16 words each).
  Their optional velocity scalers are bounded providers. Check the proper
  +0xA8/+0xB0 descriptor, parameter homes, calls and incidental V0. The source
  wrappers ignore the result; this does not erase the target's low-byte ABI.
- **1,340 native32 cases per O0/O2/O3 profile**, trapping UBSan,
  use the reused typed record/response/height layouts, independent packet
  values and complete object/plane/response/marker canaries. All
  **14 semantic controls** are effective, including stale callback,
  wrong gates/point/threshold/contact, missing return truncation and the stub.
- Three independent GNU links and12 rebased executions qualify all eight
  binding sites. All78 word, eight binding,72 register-metadata and four
  whole-image corruption controls reject changes.

Native descriptor indices are the -1 sentinel or0..127 inside an explicitly
synthetic128-entry provider table. Other signed byte indices are guest address
probes; the real retail table still has one entry. Native helpers exercise
defined pointed-object/global mutations, while arbitrary private-home changes
stay in the guest model. Native expected byte images account separately for
little-endian numeric fields. An initial fixture plane accidentally overlapped
the emulated stack; moving it to separate storage and using typed native
float backing resolved the fixture mismatch without changing the C candidate.

Models do not establish complete hardware FCSR/exception behavior, terrain,
gameplay, or that the real pure point validator mutates globals. Fault-prefix
checks qualify emitted MIPS accesses, not portable C fault semantics.

## Literal image, production and preservation

Actual Make retains O2/g3/MIPS2/O32 and all five commands: assembly prepass,
IDO compile, assembly postpass, production padder and GNU as. Both padders
preserve all **31 functions / 30 neighbors**, existing pools, the exact
register-mask union and **14 exported interior labels**. Diagnostics are zero.

Independent full-ELF prediction replaces only the312-byte target body and its
12-to312-byte extent: **236 changed bytes, zero exclusions**, no metadata
permutations. All **6,052** disassembled entries keep their addresses; every
other body, extent and metadata byte stays fixed. Protected data is exact
across **720 owners / 189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals that complete prediction.
Makefile, protected data and progress CSV stay unchanged. The pre-existing
full-ROM checksum mismatch (make all exit2) and duplicate generated_12D630
recipe warning remain separate from the successful target build and recount.
Shared smoke checks are fresh in both tools copies; three unchanged helper
regressions per copy are reused by exact fingerprints. All **2,434** inherited
sibling dirty paths are preserved. **111 frozen inputs** pin source, helper
and table owners, headers, layouts, private ROM/data and IDO compiler.
Baseline consumer719f93c8a479b9e4c5e44f8ae212ad040e0ac73f, tools
073765a9cdfac4e3ceb636dbe084cecb6d65c9ae. Claude calls: zero.

ELF SHA256: `8e23ae459604f5a28b69df91a1c409b53e2a9f4d8f3c913bdec84341ba8b65d0`.
Binary SHA256: `98c78dd0daec143ab08a62c168d9da4aefda2747278c558ff4e7f55a90a4c8c7`.
Owner SHA256: `b1d87df23a5d17e179391a298040670bd879609fd7407e91d13e9857138321b4`.
Guards SHA256: `e114c4f489dbfd2fafbad000982b4f5ba4e21702070234f75e2013e80afc8cc4`.

## Resume boundary

Next: **func_151794C8**, an uncredited78-word camera-output routine in
`conker/src/game/generated_1A6360.c`, original1A6360.s. VA151794C8..15179600 /
ROM1A6978..1A6AB0, frame0x40, saved F20/F21 pair. Its instruction shape mirrors
the qualified func_150E41C0 (Note2197): reuse that semantic body, oracles and
bounded FP domain. Audit actual callers and wrappers func_150AD78C/150AD780;
use the live camera pointer D_800DBFF0 and output D_800DD438. Preserve integer
coordinate snapshots, cached angle arguments, later camera reload, explicit
zero arithmetic and halfword store order0/4/2. Complete all gates before credit.

Receipts: `conker/build/game-record-plane-callback-151319C4-match/`.
Tools commit before the consumer pin. Scoped Graphify refresh retains existing
unscanned nodes with explicit evidence; it is not full-corpus extraction.
Host Release stays frozen. The80% goal remains active.
