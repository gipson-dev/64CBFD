# Endpoint Event Updater Guarded Match - 2026-11-08

`func_150EF910` replaces a false zero-return placeholder with the complete
two-endpoint event callback. Semantic C emits all **79 words / 316 bytes**
with the original **0x18-byte frame**. One checked guard swaps the two
operands of a symmetric integer `bnel` comparison. All other words emit
directly from C, with no schedule changes, insertions or omissions.

Production: Total **4,274 / 5,513 (77.53%)**, Game **3,601 / 4,840 (74.40%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. There are
**1,239** converted functions still different and **137** more exact functions
needed for 4,411 / 5,513 and the active 80% goal. Conversion rows are unchanged.

## Recovered behavior and observed ABI

Owner `conker/src/game/generated_11C2B0.c`, original `conker/asm/11C2B0.s`.
VA **150EF910..150EFA4C**, ROM **11CDC0..11CEFC**. Interface:

```c
void func_150EF910(u8 *owner, s32 eventAddress, u8 command);
```

The existing `EmbeddedOwnerLink` and `OwnerLinkEvent` types describe the
two links beginning at owner+0x110 and the command-0x2D packet. First link:
pointer +0, identity +4; second link: pointer +8, identity +0xC. The extra
discriminator is byte +0xD. Event address is the established O32 word passed
by the real dispatcher, converted to a pointer inside the callback.

1. **Command 0:** capture the first endpoint pointer, event word zero,
   endpoint identity and event byte +4, in that order. Release the owner when
   either the pointer or identity matches. Both identity reads occur before
   the comparison, even when the pointers match.
2. **Command 0x2D:** replace each endpoint matching event `before` with
   `after` and its `after_identity`; an endpoint matching `after` is replaced
   with `before` and `before_identity`. The before test wins when both packet
   pointers are equal. After updating the first endpoint and its identity,
   read the live packet again for the second endpoint. An early message
   snapshot changes behavior when the packet overlaps the endpoint state.
3. **Command 0x43:** require a first-endpoint pointer or identity match,
   then require event byte +5 to match state byte +0xD before releasing.
4. Other command bytes return without endpoint/message payload reads.
   The original masks the incoming third argument to eight bits. The
   callback returns void; the caller does not test its incidental V0.

No extra pointer validity, event bounds or null guards are introduced.
Unknown-command tests with unmapped payload are emitted-code evidence;
portable C execution with invalid objects is not claimed.

## Actual registration, caller and release connection

The sole aligned entry pointer is **D_80089F64[5]**, VA80089F78 / ROM22EA38
in `asm/data/22E730.rodata.s`. The aligned full-ROM entry/interior census
finds no direct J/JAL references.

The actual caller is **func_1513DF9C**, VA1513DF9C / ROM16B44C, the existing
53-word direct-C category dispatcher. Its complete predecessor ELF body is
independently compared with retail. Actor category **7**, with flag
**0x400000** set, selects entry five and forwards `(actor, eventAddress,
command & 255)`. Other categories/flag combinations use their original
table entries. All 52 reachable caller words are visited; word 11 is a dead
duplicate category load skipped by both incoming branch paths and absent
from the switch targets. This coverage distinction retains all 53 literal
words in the byte proof. Nonselected callbacks are bounded providers here.

Connected execution includes the original **28-word func_1516972C** and
**20-word func_151696DC**, both already byte-exact in the predecessor ELF.
All their words are visited. Release repairs older matching cursor slots
before selecting a descriptor destructor or fallback. Cases include types
0, 1, null-destructor type 2 and type 70; signed depths -1, 0, 1 and 3;
and matching/nonmatching cached cursor references. Destructor/fallback
effects are bounded; full allocation cleanup and gameplay are not claimed.

## Compiler, guard and complete-image proof

Capturing the command-0 identity bytes as promoted integers and naming the
first command-0x2D packet pointer recovers the retail register allocation.
Alternative local/caching forms were screened privately and rejected.
The selected O2/g3/mips2/o32 body has raw SHA-256
`3aaba1befaa4a53c5f56773ad17b5a4642db6293894d25fbc50f5113d606cc33`.

The only differing word is **index 37 / +0x94**: raw **54C40007**, retail
**54860007**. Both compare the same A2/A0 values for inequality, branch to
word 45, and retain word 38's `lw A2,8(V0)` delay instruction. The guard
pins the entire raw body and both R_MIPS_26 bindings. No register lifetime,
access order, call, delay slot or branch target changes. Original, raw and
fitted complete machine state agree, including the literal fault prefixes.

The 44-function owner preserves **43 raw and padded neighbors**, pools,
labels and register union. Both padders agree; the actual Make path emits
the predicted padded object in three commands, with no compiler diagnostics.
No GLOBAL_ASM restoration or compiler profile change is used.

Strict whole-ELF prediction accounts for **223 changed bytes, zero exclusions**,
with no metadata-name reordering. Only the target body and symbol extent
change. All 6,052 linked function entries retain their addresses; all other
bodies and protected data are preserved. Protected data remains **720 owners /
189,088 bytes**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Validation and practical limits

Both tools copies pass eight fresh focused checks before installation and
eight after installation, sequentially, with identical detailed receipts:

- **2,240 guest cases per body**, all command bytes/high input bits, exact
  live link/identity behavior, and unmapped ignored payload. All 77 reachable
  target words are visited; words 36 and 58 are dead duplicate instructions.
  The full 79-word body is retained and compared literally.
- **504 message/state alias cases per body**, **1,488 fired fault-prefix
  triples** and **208 delay-slot cuts**. Original/raw/fitted registers,
  memory, call observations, PCs and private accesses agree. Portable C
  fault semantics and guest-private alias behavior are separate claims.
- **2,048 actual-dispatcher cases per body**, including all 256 categories,
  both flag states, four command forms, and the complete connected target.
- **576 connected release/detach cases per body**, with all 28/20 helper
  words visited and their existing exact bytes independently confirmed.
- **Nine independent GNU links in three regions**, **432 cases per body**,
  and both R_MIPS_26 call bindings checked across jump regions.
- **Twelve compiled incorrect implementations** are detected: wrong command
  values, AND in place of the release OR, wrong endpoint pointer/identities,
  missing second endpoint, missing release, wrong/missing discriminator,
  and an early cached packet. The cache counterexample uses command 45 and
  message address owner+0x10C; it fails on observable memory, not stack layout.
- Native32 **O0/O2/O3 each pass 38,912 cases**, trap UBSan, typed 8-byte link /
  12-byte event / 32-bit pointer assertions, original semantic category
  dispatch and whole 640-byte arena canaries. All 11 controls applicable to
  distinct typed packets fail observably in every profile. Overlapping
  packets remain guest tests, rather than portable native alias claims.

The production object/ELF equal the independent prediction and linked recount.
The existing whole-ROM checksum mismatch still makes `make all` exit 2;
target build/link/progress and recount pass. The inherited duplicate
generated_12D630 Make warning remains. Shared tool smoke is fresh in both
copies; three unchanged regressions per copy are reused by exact helper/test
fingerprints, not described as fresh runs.

## Bank and next boundary

Receipts: `conker/build/game-endpoint-event-update-150EF910-match/`.
The 107 frozen source/compiler/header/ROM/layout/caller inputs are audited
through adoption. The sibling tools checkout's 2,434 inherited dirty paths
are preserved, and the host Release stays frozen. Tools commit before the
consumer pin. Scoped Graphify refresh retains existing unscanned nodes
with evidence; it is not full-corpus extraction.

Next: **func_1512623C**, owner `game_14FF90`, the next measured 79-word
unmatched Game routine. Audit its complete retail body, real ABI/callers and
owner/compiler profile before drafting, adoption or credit. The 80% goal
remains active.

Production ELF SHA-256: `1559ab041131bbd04d2dc715f83be5925ebf4662f1e67832c21b24543a351f69`.

Production guard SHA-256: `b6321a2e129ea7f0550984349d4cdab102ff203b44de7fb0ee9bea04ddd89be0`.
