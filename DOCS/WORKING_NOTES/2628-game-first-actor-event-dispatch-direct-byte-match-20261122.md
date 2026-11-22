# 2628 - First-actor event dispatcher direct byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150D0E90` replaces its zero-return placeholder with its complete semantic
C body. All **149 retail words emit directly from C**, frame 72, **zero guards**,
insertions or omissions. Production recount is **4,610 / 5,528 (83.39%) total**,
**3,937 / 4,855 (81.09%) Game**, zero drift, 918 different converted functions.
Init 492/492 and Debugger 181/181 are unchanged. **89 more matches** reach 85%.
Conversion rows are unchanged; the former placeholder already counted as C.

## Behavior and recovered interface

Source `conker/src/game/generated_FDD70.c`; original `conker/asm/FDD70.s:409`.
VA150D0E90..150D10E4, ROMFE340..FE594, 596 bytes, frame0x48. S0..S6 occupy
SP28..40; RA is atSP44. The one-word callback argument is saved at incoming
SP+0 and is unused. The correct interface is `void func_150D0E90(s32 unused)`.

Four counters advance by the signed tick count times 40, -66, -8 and 92 before
the first pool actor's attachment byte120 gates events. Selectors250,249,248
are queried in order, then251. The actual `u8 *(u8)` record lookup returns
160-byte records; an explicit struct131 pointer view recovers signed pointer
subtraction and flag-table indexing. Bit0 selects events. The first three
events invoke the qualified paired-actor initializer and sound0627. The final
event emits that sound, the eight-word effect call, reset and state6 in order.
Provider globals reload after each lookup; the attachment gate is sampled once.
Negative coefficient additions and the narrowed byte selector preserve the
original NEG/addition tree and call-delay schedule. No shared headers or
compiler profiles changed. Raw SHA256:
`338c78d9dd633b6c0a34a71d78d8056da450e0d30383b880ef8744d7b52e6dd9`.

## Current caller and provider evidence

The bounded original text census finds no direct J/JAL references. The loaded
table D8008CD04 has28 entries and registers this callback at index19,
address8008CD50. Both original and current table bytes agree. The current
43-word frame-layer dispatcher `func_151749F8` is retail-exact; all43 words
execute in288 cases per stream with the target connected. Both post gates,
view values, two stack phases, repeated events and phase wrap are checked.
An omitted incoming-view load is an effective negative. The callback return
is ignored. Computed references beyond this bounded census are not excluded.

The current original 28-word lookup executes in96 connected target cases per
stream plus8 standalone cases, covering all28 words including empty, zero and
missing selectors. Four other providers are retail-exact. **func_15136C3C is
still a production zero-return stub**: its eight-word call ABI is observed,
but complete effect behavior and full gameplay are not claimed. The prior
paired-actor initializer qualification is reused under unchanged source/code
and guard fingerprints; this does not claim fresh execution of its internals.

## Fresh qualification and defined domains

- Guest raw/original:788 cases per stream, every256 gate values, all16 event
  masks, flag high bits, mutable base/flag providers, ordered helper mutations,
  two stack phases, saved-register restoration and158 access-fault pairs.
  141/149 target words execute. Unexecuted words72,76,77,78,107,111,112,113 are
  fixed-divisor zero/overflow checks; they are literally exact, not counted as
  executed. Whole guest states and all observed call boundaries agree.
- SDK32 O0/O2/O3:2,564 cases each, actual SDK struct127/struct131 sizes and
  actor attachment offset asserted, strict aliasing and UBSan. Independent
  guest-checked vectors verify every call argument, counter, provider pointer,
  actor/attachment/flag snapshot and final state. Ten effective source controls
cover counter factors, gate, selector count/final selector, flag bit, initializer,
  sound volume, effect stack argument, reset and final state.
- Native pointer differences stay within one allocated record array, including
  negative indices with an interior base. Native signed products and sums stay
  representable. NULL, non-multiple differences and signed overflow are
  guest-only; a missing-record fault witnesses the unguarded retail contract.
  No all-input portable-C or missing-record safety claim is made.

Both padders preserve the complete raw/original payload and all24 relocation
sites.16 independent GNU links include HI16 carry boundaries; twelve possible
alignment bytes are zero and separate from the596-byte body. Four other owner
functions, compact pools, old guards, loaded data and conversion rows agree.
Actual natural Make uses three commands under existing O2/g3. The independently
predicted complete production ELF has **468 changed bytes, zero exclusions**,
with no metadata permutations. All189,088 protected GameData bytes/720 owners
are exact. ELF SHA256 `4e36367aff68160c0c50e6ac4be5f46d90122a1c75aa6851c04fc281ea1909cd`.

Both tools configurations pass all five checks before and after installation,
with Python/data fingerprints verified. The real sibling's edits and352
dependency hashes are preserved. Shared tools-check passes. Existing duplicate
generated_12D630 recipe warnings remain; this is not a warning-free build claim.

The first installed test caught a manifest-only newline hash error: its selected
source hash described the Windows CRLF scratch copy rather than the identical
LF text compiled/installed by WSL. Only that hash field was corrected. Source,
owner object, predicted ELF, test code and all semantic vectors were unchanged.
Preinstall receipts retain that explicit metadata delta; both installed suites
run fresh with the corrected manifest and Python/data fingerprints.

Baseline consumer `85d196732e5b02c6d39d369ecc6b245e31ed9162`, tools `f2e579d8b6fb049b88d58bb4a527cc929fd183ee`.
Tools commit `9928e7b77dca56b0ab50ab60e2879bf4f48c3ec4` is banked before
the consumer. No push. The available host scene input uses different mapping
and consumes binary code; no direct C import, host build, Release change or
gameplay acceptance is claimed. Zero Claude calls.

Continue with the remaining neighboring Game stubs after this immutable bank;
`func_150D1204` is the next 102-word particle-emission candidate to reconstruct.
Earlier private candidates remain uncredited. The 85% goal stays active.

Graph maintenance: the native update exited 1 with all
70,572 prior IDs retained. The subsequent serial scoped extraction
covers 7 C/Python files with no missing AST sources, producing
70,622 nodes / 165,656 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
