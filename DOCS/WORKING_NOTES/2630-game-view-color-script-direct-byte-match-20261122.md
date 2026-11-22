# 2630 - View color script callback direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150D08C0` replaces its zero-return placeholder with complete semantic C.
All **372 words / 1,488 bytes emit directly**, frame40, **zero guards**, inserted
or omitted words and no slot padding. Production is **4,612 / 5,528 (83.43%)
total**, **3,939 / 4,855 (81.13%) Game**, zero drift,916 different. Init492/492
and Debugger181/181 remain exact. **87 more matches** reach85%. This function
already counted as converted; conversion rows remain unchanged.

## Source and recovered behavior

Source `conker/src/game/generated_FDD70.c`; original `conker/asm/FDD70.s:11`.
VA150D08C0..150D0E90, ROMFDD70..FE340. S0 lives atSP20 and RA atSP24.
Raw SHA256 `403f369777e2fab66076ab42a9d46988a82c907553ef46a20933ede4edac006e`.
All five functions in this owner now have semantic C and exact retail bodies.

The existing SDK `struct108` supplies flags at84, timestep at7B4 and size9A0.
Its single structs.h include moves above the first definition. Four other
raw/padded owner functions, diagnostics and pools are unchanged. The file's
stale placeholder heading is corrected; retail function names are retained.

Query func1509BE40(1,403D,6,9000) gates flags80021000. Nested selectors4043,
4044,4045 choose RGB(64,255,255),(255,64,255),(255,255,64); no selection means
white. Disabled mode writes white, clears80021000 and separately sets8.
Three calls to func150495B0 smooth current globals888C0/C4/C8 toward targets
888CC/D0/D4 using velocities888D8/DC/E0, strength4,damping6 and a freshly
loaded view timestep. Six ordered variadic submissions use selectors30F5/F4/
F3 then30FA/F9/F8, key12 and freshly loaded (u8)(u32)current values.

The six unsigned float conversions account for much of the large body. They
save/restore FCSR, attempt truncation, retry above2^31 by subtracting2^31 and
setting the high bit, and useFFFFFFFF for invalid/negative results before the
final byte mask. Query/provider side effects and repeated late RGB/timestep
loads are preserved. Invalid conversions remain guest-only tests.

## Actual dispatcher and helper boundaries

The callback prefix of D80089670 has36 pointer entries before following
graphics words in the same assembly symbol. Index30/address800896E8 holds
this target. The complete original/current dispatcher15130230 has17 body
words plus12zero padding bytes. It reads the scene byteF, skips index0, and
passes incomingA0 unchanged through JALR. The return value is ignored.
Both streams pass80 cases including all query paths, effects, two stack
phases and four rounding modes. Zero-index gating and an effective missing-
view-argument control pass. The complete caller slot and table prefix agree
with the current ELF; no current-parent stub limitation applies here.

Original/current query and submission providers each have92words; the scalar
smoother has54. Connected target execution passes1,440cases per stream with
independent smoothing, overshoot/zero timestep/direction cases, complete
packed leaf arguments and saved global-count restoration. Another36 standalone
wrapper cases cover payload counts0..8 and both stack phases, executing all
92+92 wrapper words. The smoother executes52/54 words; its duplicated words
at150495EC and15049674 are unreachable on the original branch paths.
Selected leaf addresses150A04D8 and1509E900 are read from actual tables.
Those leaf internals remain contracted; no complete script-system or gameplay
acceptance is inferred from these bounded helper tests.

## Qualification, image and adoption

- Guest:696cases per candidate/original stream, all372 target words executed,
  82 access-fault pairs, complete call-boundary snapshots, saved registers,
  mutable providers, flags/palettes and all four rounding modes. FCSR is
  restored after each conversion, including tested NaN, infinity, negative
  and out-of-range fallback paths. This is a bounded instruction oracle,
  not exhaustive VR4300 exception, denormal or hardware emulation.
- Native SDK32 O0/O2/O3:108cases each, actual struct108 layout assertions,
  full unaffected-view canaries, call snapshots and all six submissions.
  Strict aliasing, UBSan and float-cast-overflow sanitizer pass. Native
  colors are finite and -1 < value <2^32. Ten effective controls cover query
  count/selector/truth, flags, palette, timestep, smoothing strength/velocity,
  published width and incorrectly cached repeated red output.
- Both padders emit the identical target payload, no guards or padding.
  Sixteen GNU links independently rebase all69 relocation sites across
  HI16 carry boundaries. Four other owner functions/pools remain exact.
- The natural existing O2/g3 Make route uses three commands. Independent
  complete-image prediction has **1,191 changed bytes, zero exclusions**,
  including five closed metadata permutations/11 symbol records/124 name
  bytes. Symbol identity/attributes are preserved. All189,088 protected
  GameData bytes/720 owners, other bodies/addresses, old guards and conversion
  rows agree. ELF SHA256 `1046bd8fb3ce52487d70150c56a7b6f2336542971e5854eccc1d11bd60057965`.
- Both tools configurations pass all five checks before and after installation,
  with identical Python/data hashes. Shared tools-check passes. The real sibling
  tools checkout's pre-existing edits and dependency hashes remain preserved.
  Existing duplicate generated_12D630 Make warnings remain unchanged.

Baseline consumer `7cdecd34c4f6170616f849c5a37d399569ea26ba`, tools `0b85cce62976a12c338eeef6f63fb5cc0c3e33a8`.
Tools commit `1d5f14abc4a6732dc919e0abce286362ebf8c4af` precedes the
consumer commit. No push. Available host configuration applicability is
recorded separately: it consumes binary words/symbols with a different input
mapping, so no direct C import, host/Release build or gameplay claim is made.
Zero Claude calls. Finish graph retention and the immutable bank before the
next recovery; earlier private candidates remain uncredited.

Graph maintenance: the native update exited 1 with all
70,695 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,754 nodes / 166,781 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
