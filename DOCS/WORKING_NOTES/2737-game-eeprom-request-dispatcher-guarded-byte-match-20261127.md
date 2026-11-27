# EEPROM request dispatcher guarded byte match - 2026-11-27

`func_1501C57C` replaces its zero-return placeholder with the complete
**106-word / 424-byte** EEPROM request dispatcher in
`conker/src/game/generated_48FD0.c`. Its body is at VA
`0x1501C57C..0x1501C724`, ROM `0x49A2C..0x49BD4`. The original slot is
109 words through `0x1501C730`, including three trailing zero words.
The unchanged O2/g3 profile emits 106 words and the original 24-byte frame.

Actual production recount: **4,716 / 5,528 (85.31%) total**,
**4,043 / 4,855 (83.27%) Game**, Init 492/492 and Debugger 181/181.
There is zero drift and 812 still different. This adds one accepted match;
conversion rows and denominators remain unchanged. The **90% goal stays
active: 260 more matches** reach the required 4,976 / 5,528.

## Recovered interface and behavior

The public interface is `void (void)`. The sole aligned direct JAL is at
ROM `0x490C0` in `func_1501BBB8`. Its complete 278-word original body is
pinned against ASM and ROM. The actual five-word call window, starting at
VA `0x1501BC10`, overwrites V0 before use and supplies no argument words.
No aligned target pointer literal or interior entry is found. Historical
C return spelling remains unproven. The complete child and this call window
are executed by the caller fixture; the complete controller loop is not.

The dispatcher always polls `func_151DCFD8(0)`. It then examines signed
pending byte `D_80082BB4`. If work is pending and the cached type is not
`EEPROM_TYPE_16K`, it probes through `func_151DD460(&D_800BE900)`, stores
the low byte in `D_80084068` and re-reads the pending request. Probe/poll
providers may change pending work, slot, type or staging-buffer state.

For unsupported types, the source preserves the original seven-case no-op
table and bounded countdown from 19, then handles request 1 with
`func_150064E0` or request 4 with `func_15007168` and clears pending work.
The no-op switch and countdown have no additional C-visible side effect;
their unusual source shape recovers existing retail instructions and data.

For type 2, requests 1..7 call their corresponding helpers. The first
three pass signed slot byte `D_800BE3EC`; the remaining four take no
arguments. Pending work is cleared before checking `D_800BE3F0` again.
A non-NULL staging pointer is released through `func_10004074(pointer-8)`
and then cleared. A free provider may publish new pending work, which must
survive because the pending clear precedes the free. A provider's temporary
replacement of the staging pointer is cleared after the call.

The probe and poll contracts are checked against their concrete source
providers. The first two request handlers still have production placeholder
bodies; their one-word argument transport is qualified here, with no helper
body credit. All services are opaque in the native/guest dispatch fixtures.
EEPROM hardware behavior and gameplay acceptance are not claimed.

## Closed control-flow normalization and table bindings

The selected semantic C emits the exact 106 words, 24-byte frame and RA
save at SP+20 before guards. Forty-two external relocation positions are
accounted for. The original object additionally has one resolved internal
PC16 branch, canonicalized to its literal word for comparison.

Twelve expected-word guards cover differing positions within the closed
15-word fallback region at `0xA0..0xDC`. They normalize two equivalent
request==1/request==4/default predicate graphs. The same calls, pending
clear and cleanup occur on every path. Retail statically clones an RA
reload; each runtime path loads RA once. One retail word (index 46,
`LI AT,4`) is unreachable and remains preserved in the normalized object.
This is control-flow normalization, not only independent scheduling.

An exhaustive 9,216-case changed-region interpreter covers every request
byte, three register seeds, three helper-return poisons, two mutation modes
and two saved RA values. Complete registers, memory, formal calls and
access order agree at the join. Raw literal PC/trace/fault-prefix parity
is not claimed. Full normalized fault-state comparisons are checked
separately. No instruction insertion/omission, artificial padding/storage,
frame rewrite or floating-point rewrite is introduced.

Four further HI16/LO16 guards bind the compiler's two switch tables to
retained `jtbl_80096964` and `jtbl_80096980`. The second low addend changes
from 0x1C to zero against the second symbol. Both seven-entry tables are
owned, pinned against ELF/ROM and independently rebased. Their complete
56-byte payload and eight compiler alignment bytes are checked; nonzero
alignment is rejected. The disposable compiler pool is replaced by the
already retained GameData tables. Table payload SHA256:
`74e99b8dcd5f5fb03044a827ec971cdfc86f2d47812c347fdfec2c6ba50417dc`.

In total, **16 guards = 12 closed-CFG words + four table bindings**.
Ninety-four bound words already agree; normalization recovers all 106.
Both complete padders agree. Both before objects reproduce the frozen
production owner. All seven raw and normalized neighbors, their pools,
two handwritten GLOBAL_ASM bodies and prior guards remain unchanged.
No Makefile/compiler-profile change is needed; no new diagnostics occur.

## Fresh qualification and actual production

- Native actual C: **557,056 cases each at O0/O2/O3**, all 256 request,
  type and slot bytes, all 256 probe low bytes, NULL/both buffer banks,
  and poll/probe/handler/free mutations. Providers use separate translation
  units and noipa boundaries. Strict aliasing, UBSan traps and LTO type
  checks are enabled. Eleven effective controls exit with logical
  mismatches; a signal/trap is not accepted as a negative-control success.
- Guest: **10,752 cases per stream, 43,008 runs**, original/raw/both
  normalized streams. All complete post-return states agree, as do the
  independent public-memory and ordered-call references. All 106 raw
  words execute; retail and normalized streams execute 105, with the
  unreachable word statically accounted for. **45 normalized fault
  triples** and four effective controls pass.
- Sole caller window: **2,048 cases, four streams and three return
  poisons = 24,576 connected runs**. All 256 request bytes are covered.
  The complete child and five original caller words execute, and complete
  post-window states agree. Three effective controls reject consuming the
  ignored child return, using the wrong controller byte and skipping the
  dispatcher. The broader controller loop is not executed.
- Boundaries: all **212 word mutations** and **84 binding mutations**
  are visible or rejected; 32 injected guard bindings, 32 guard removals,
  14 table payload corruptions and 14 table binding controls are effective.
  Both overflow controls reject. Twenty GNU links cover four independent
  symbol groups, both tables separately, HI16/LO16 carries and
  raw/manual/retail/both-padder routes.
- The actual **five-command Make owner recipe**, including both
  GLOBAL_ASM preprocessing steps, reproduces the qualified object.
  An independent frozen-before-C plus original-ASM prediction equals
  the entire linked ELF: **353 changed bytes, zero exclusions**.
  All 720 data owners / 189,088 protected bytes, retained tables,
  neighbors, addresses, outside guards and conversion rows remain fixed.
  Actual production Make and the fresh matching recount agree.

The packet runs freshly in the primary tools repository and an isolated
tools twin before and after installation. The real sibling tools HEAD,
353 dependency hashes and all preexisting dirty work remain untouched.

| Phase | Elapsed | Tests |
| --- | ---: | ---: |
| pre-primary | 189.094 s | 5 fresh / 0 reused |
| pre-sibling | 180.021 s | 5 fresh / 0 reused |
| installed-primary | 174.6 s | 5 fresh / 0 reused |
| installed-sibling | 268.12 s | 5 fresh / 0 reused |

Paired reports agree across 325 primary / 326 twin imports and 245 tool data inputs. All eleven task files are independently copied. Shared `make tools-check` passes. The frozen input set contains 4,227 hashes and 3,792 independent snapshot copies. Claude calls for this candidate: **0**; no subagents or pushes.

Tools commit: `6c0c79e52d6fd4e072e0320b3cbf634dc770c696`.
Production ELF SHA256: `3b9ca9a874d1ecaf1f6a2aacd5181b29e4995131062c641c328501968ad49482`.
Complete owner C SHA256: `f981b212c2b1ebc800daafc7a22161af22c15dc1b770a3a5ff32cdd4e1b85d45`.
Padded owner SHA256: `d133eb2304944ada78397be81d36d6fe23f8ea525014088aa5c2d5a910a73cd4`.
Guard manifest SHA256: `1a4ddc2211326411b122610a1a5cf9cfad1bc7125a00a47998811bf457ad023a`.

## Host applicability, graph and next step

The read-only sibling audit finds `64CBFDOGL/recomp_scene/cd64_out/func_1501C57C.c` as generated code only (SHA256 `0d3a11ec86b9a320851cecba170eb65fb6136f02232963a728ad960354a83a3b`). No host implementation transfer, edit, build or launch is made. Release stays frozen.

Graphify receives a scoped AST refresh, auditing every current C definition in this owner while retaining both GLOBAL_ASM bodies, all previous IDs and qualification proofs. Actual Git hook producers must be observed terminal before publication. Full-corpus re-extraction is not claimed. The committed bank retains graph, frozen inputs, suite closures, build/image proofs and commit receipts.

`func_1514EECC` remains private and uncredited: its 145-word source still has a 296-byte frame versus retail 288 and unresolved saved-register placement. Continue with another ordinary unmatched Game routine after sealing this checkpoint; do not install the parked candidate or credit handwritten/internal-entry code as ordinary C. The accepted dispatcher does not complete the 90% goal.
