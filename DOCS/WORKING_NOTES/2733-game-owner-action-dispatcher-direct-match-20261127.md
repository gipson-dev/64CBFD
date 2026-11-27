# Owner action dispatcher direct C match - 2026-11-27

`func_1514D15C` replaces its zero-return placeholder in
`conker/src/game/generated_179F30.c`. All **109 words / 436 bytes**, all
**22 relocation positions** and the original **72-byte frame** emit directly
from semantic C. Zero guards, inserted/omitted words, alignment tail or
compiler-profile changes. VA `0x1514D15C..0x1514D310`; ROM
`0x17A60C..0x17A7C0`. The entire guard CSV stays unchanged.

Fresh production count: **4,712 / 5,528 (85.24%) total**, **4,039 / 4,855
(83.19%) Game**, Init 492/492, Debugger 181/181, zero address drift and 816
different. One target matching credit. No classifier, parent or host matching
credit; conversion rows and denominators stay fixed. The active **90% goal
requires 4,976 accepted matches: 264 more** at this denominator.

The entry is `s32 func_1514D15C(u8 *owner)`. Three signed 32-bit classifier outputs
start at -1. A nonnull head at owner+0x2F4 rejects before services. Compute the
low 32-bit address difference from D_800CC2D0, cast signed 32-bit and divide by 0x32C,
truncating toward zero. Repeatedly call func_15155FD4(index) and free each
nonnull result with func_1516972C; preserve the result across that free call.
For index 0 with clear D_800BE616, call func_15155780(index,0xFF). Then invoke
D_8008AACC(owner) and classify through
func_1514CA80(owner,&first,&second,&third). Zero returns 0; otherwise return 1
after these conditional routes:

| Classification bits | Lookup and call |
| --- | --- |
| bit 2 (`4`) | nonzero D_800A5ED8[third] indexes D_8008AA70 |
| bit 1 (`2`) | nonzero D_800A5EC0[second] indexes D_8008AA70 |
| bits 1+0 (`3`) | D_8008AB90[second][first] indexes D_8008AA70; call a nonnull pointer |

The first two routes require nonnull entries for nonzero selectors; only the
last route checks the function pointer. Do not add protective null gates or
cache later outputs/table contents across callbacks. Returned callback values
are ignored. D_8008AACC is the actual **slot 23 alias** inside the complete
58-entry D_8008AA70 table, not a separate callback object. Names first/second/
third describe observed outputs; more precise gameplay roles remain open.

The native fixture uses actual 812-byte records with pointer fields at 0x2F0
and 0x2F4, typed pointer tables, byte rows, output cells and complete fences.
A base alias into six records permits defined 32-bit negative/zero/positive
logical-index tests. Escaped classifier output pointers remain live during
callbacks and can be mutated by the stronger opaque provider contract.
Incoming-owner-home and private flag-byte mutations are guest-only probes.

Initial source emitted 109 words/frame 72 with 30 differences. Using the byte flags in
the first route reduced that to 9; changing the selector to signed 32-bit worsened
its frame. The verified unsigned-byte classifier result plus a byte local
recovered 109 words/frame 72/all 22 aligned bindings with only SB/LBU home differences:
raw SP+0x33 versus retail SP+0x3B. Scope, inline-call and register-hint screens did
not resolve those words. Declaring the meaningful byte flags before index
recovers the original home directly. No dummy local, padding, gratuitous
volatile or private-home word normalization is used. All 77 other raw/padded
function bodies, bindings and pools remain fixed in this 78-function owner.
Its existing `jtbl_800A5E20` pool binding is preserved by both full padders.

The classifier placeholder's return type changes `s32` to `u8`; its same
three zero-return words and empty bindings remain fixed. Its 439-word semantic
body is still unrecovered and uncredited. Giving that placeholder four formal
arguments adds argument-home stores and fails neighbor identity, so that
formal-argument repair is deferred until a complete body is qualified. The
standalone native service has the real four-argument interface.

The unsigned-byte return is qualified against the original 439-word helper,
not merely inferred from the fit. All four original jump tables, 187/54/19/10
entries, match retail and the frozen ELF. Conservative bit-mask propagation
starts with unknown incoming registers, overapproximates every frozen table
target at each indirect JR, and models branch delays/likely annulment. It
covers 439 words / 716 abstract states and proves all normal returns are in
the low three bits (return masks 0/3/7). Two corrupted valid instruction forms
fail the range comparison. All 81 original store forms are word stores through
A1/A2/A3 at offset0. Direct raw-object checks prove the retained stub stays
12 bytes with no relocation in its body.

Fresh qualification:

- 1,972 guest cases across five literal streams compare full private RAM,
  GPR/FPR, HI/LO, FCSR, trace, calls and return. Independent ordered target
  reference checks public effects/calls/results. All 109 target words execute.
  Include all 256 classification bytes, signed owner-index cases, gate and
  cleanup paths, actual table 23 alias, late table/output mutations and real
  guest private-home redirects. Six wrong instruction controls are rejected.
- 77 fired access-prefix quintuples retain full private/fault state and
  instruction/delay ownership. Guest fault/private probes are separate from
  portable C or exception-hardware claims.
- Original classifier: 11,106 standalone cases execute **all 439 words**, with
  named-output fences, low3-bit returns and register/FPR preservation. The
  initially missed branch requires owner kinds 156/157; its cases were added.
  Two dynamic controls reject a high return bit and an output-fence store.
  Another 504 cases per stream connect the complete original helper to both
  target streams; 73 helper words execute in this bounded connected matrix.
  The independent target reference reuses the original helper as its service
  model; this is not a separate high-level classifier reconstruction.
- Native32 actual target C in three TUs: 49,152 cases each at O0/O2/O3, typed
  812-byte records and both pointer offsets, strict aliasing, trapping UBSan,
  LTO type checks and complete arenas/pointer tables/call logs/return/MXCSR.
  Eight defined controls exit 42 by comparison, including signed-index
  division, reset channel, both route gates and stale escaped output. No
  compile error, trap or signal is counted as a valid rejection control.
- Both scoped padders expose 218 word and 44 binding corruptions. Twenty GNU
  links / 100 guest rebases move all four helpers and seven global bindings
  through four jump regions and signed HI16/LO16 carries. Preserve the actual
  table 23 alias across carries. Generic oversize stays visible; generated
  oversize rejects.
- The actual three-command owner Make route reproduces the complete qualified
  object. Four existing pointer/integer Warning712 rows remain unchanged
  after source-label/line normalization; no new warning or profile change.
- Independent frozen-before-C plus original-ASM whole-image prediction equals
  private and production ELF byte-for-byte:449 changed bytes, zero exclusions,
  8 fully accounted symbol-record reorderings.
  All other function bodies/addresses, guard history and inventory rows stay
  fixed. Protected 189,088 data bytes across 720 owners remain exact.

The only aligned direct call is ROM B06B8 /VA15083208 in original
func_15082A44. Pin all 538 original parent words against ASM/ROM and its
unchanged 12-byte production placeholder separately. Execute the exact four
words at 15083208..15083218 with each complete child stream and a bounded
next service 150849A0. In 144 cases per stream, S0 reaches A0 in the delay slot,
the target restores its frame/saved roles, and the next service receives the
same owner. Two argument/skip controls reject; two poisoned target return
values leave caller public behavior unchanged because the result is ignored.
This is full-body pinning plus caller-window qualification; **complete parent
execution and parent recovery are not claimed**. Other services remain opaque.

| Phase | Seconds | Coverage |
| --- | ---: | --- |
| preinstall-primary | 273.53 s | 5 fresh / 0 reused |
| preinstall-sibling | 217.472 s | 5 fresh / 0 reused |
| installed-primary | 233.603 s | 5 fresh / 0 reused |
| installed-sibling | 270.225 s | 5 fresh / 0 reused |

All 20 target test methods are fresh. Primary/isolated sibling task/import/
data/artifact fingerprints agree, using each tools copy's own paths. Shared
tools-check passes. No unchanged broad suite is labeled fresh. Freeze:
4176 inputs/3128 copies. Dirty real tools
sibling preserved. Tools commit: `726e51c6c073d443b8961ac31887d00b4c98904b`.
Baseline consumer: `e59eef679aa235d725b8d532eb9d9c54ea155bda`.
Source SHA256: `1b9ec115b87a7d8607b6f64d75e9680b80c3f8632134e78b12b3eddbb2abe7a9`.
Padded owner SHA256: `3df7c27b07d859d5f9d79bb4b5663e33a10ff2da9caca51ab63cbee7de633aa7`.
Production ELF SHA256: `f8b58f179a6b47f48dd53725511fc696591e61340540d9f7c22e8543c2234554`.
Receipts: `conker/build/game-owner-action-dispatch-1514d15c-private`.

Routine Claude calls: zero; no subagents. The host generated target remains an
empty stub with active applicability unqualified; no host transfer/build/launch
or Release change. Scoped Graphify refresh audits 78 current definitions,
marks the classifier as ABI-only/uncredited, retains every old ID and its
qualification records, and observes actual commit-hook producers terminating
before final publication. No full-corpus re-extraction claim. Root README
receives aggregate rows/date only. Continue the active 90% goal from sealed N78.
