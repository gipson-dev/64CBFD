# 2633 - Randomized map particle emitter guarded byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_150EC6B0` replaces its zero-return placeholder with a complete semantic
particle emitter. Its **237 C words normalize to all 238 retail words** in
frame **0x110 / 272 bytes**. **19 guards** cover independent setup scheduling,
closed caller-volatile register choices and the affected forward branch; one
coprocessor hazard `nop` is inserted. No semantic instruction is omitted.
This is a guarded match; the raw compiler stream is not byte-exact.

Production is **4,615 / 5,528 (83.48%) total**, **3,942 / 4,855 (81.19%) Game**,
zero address drift and 913 different. Init492/492 and Debugger181/181 remain
exact. **84 more matches** reach85%. Conversion rows are unchanged. Source is
`conker/src/game/generated_1199D0.c`; original `conker/asm/1199D0.s`,
VA150EC6B0..150ECA68, ROM119B60..119F18, 952 bytes.

## Recovered source and normalization

The registered callback accepts the actual SDK `struct260 *` common header.
Its enclosing56-byte record contains the three position floats at0x28 and
the accumulator at0x34. An explicit float RNG draw precedes late timestep
and accumulator reads. The update is
`accumulator += (1352 + draw*1698)*0.0001*timestep` with retail single-precision
operation order. Emission starts and repeats strictly while accumulator>1.

A112-byte effect definition and16-byte extra packet live at SP+0x9C and
SP+0x8C. Fixed fields, the copied position and zero velocity/acceleration
initialize once before the loop. Each iteration randomizes dimensions,
offsets, a parameter, two flag bits, alpha, lifetime and paired extents.
The kind0 factory receives16 extra bytes and the record's current byte-wide
priority/context. Successful allocation receives the extra packet at+0xA8.
The accumulator reloads after external calls and subtracts1.0f. Mutable
escaped packets retain the retail lifetime across successive iterations.

The compiler's24-byte six-float pool exactly matches existing D800A1578..158C:
44D44000,38D1B717,3F7870B9,3F82B114,3DC8B43A,3E3020C5. A single target-specific
`RETAIL_RODATA_SYMBOL := D_800A1578` Make binding reuses that data without
duplicating it. Existing owner functions, diagnostics and old guard rows are
preserved. The new raw function SHA256 is
`74539b4f1c7cf3d1a9aa4af97ddd5b15bf3c7aeb2385d87295c4b26c88175bed`.

The private schedule analysis explicitly preserves every one of the237 raw
instruction origins exactly once. It moves the independent definition-pointer
setup and floating-zero setup, inserts one hazard nop, adjusts one forward
branch, and closes two GPR and eight FPR temporary words. Nineteen guarded
rows implement the complete normalization with expected words and relocations.
Both padders agree, and eight GNU links across four rebases match the complete
original target. Six other owner functions remain identical.

## Semantic, caller and helper qualification

- Guest979 cases per raw/original stream cover all four rounding modes,
  signed zeros, threshold boundaries, repeated emissions, null/successful
  allocation and valid escaped packet/provider effects. Raw233/237 and
  original234/238 words execute; four constant-divisor `break7` words remain
  unreachable. The IEEE model is bounded and finite, not full VR4300 NaN,
  denormal, exception or hardware acceptance.
- Every access cut in four discriminating cases gives424 matching public
  memory/call/FCSR fault prefixes. Raw PCs and volatile registers have
  different layouts and are not claimed identical. Saved GPRs and F20..F31
  retain their entry values.
- SDK32 at O0/O2/O3 passes133 cases each with the actual common-header,
  record and packet sizes, strict aliasing and UBSan. Only defined packet
  fields are inspected. Eight effective source controls reject inclusive
  threshold, wrong dimensions/lifetime/extra destination/size/flag/position
  and wrongly reset escaped-extra state. Eight instruction-level controls
  independently reject corresponding semantic corruptions.
- Actual table D8008A4E8 registers callback90 of98 at8008A650. The complete
  original/current45-word dispatcher15149264 passes192 cases per stream
  covering common-header argument, TTL flags, callback skip, death/revival,
  conditional release and an effective missing-record control. Callback V0
  is overwritten by the lifetime reload. Death/release internals are modeled.
- Connected1728 cases per stream execute original float RNG25words,
  integer RNG18, factory38/61 and memcpy11, with an independent64-bit seed
  model and four rounding modes. Factory coverage is the actual kind0/null
  auxiliary-pointer path used here; other factory modes remain unqualified.
  The six allocator arguments,184-byte allocation,112-byte definition copy,
  cleared auxiliary state byte and16-byte extra copy agree. Allocation-leaf
  internals remain contracted.

## Whole-image and adoption evidence

Actual Make reproduces the proposed object through the existing O2/g3 recipe
with the declared retail-pool binding. Production equals the complete
independent ELF prediction: **721 changed bytes, zero exclusions**. One
explicit adjacent symbol/string permutation exchanges D80099F38 and D800E0E08
using two symbol records and22 string bytes. Other loaded bodies/addresses,
189088 protected GameData bytes /720 owners and conversion rows agree.
ELF SHA256 `45f369bca4cd8faf0805f5c8e80044c852fc6507492c5949d42a1fa114bea6c1`.

Both tools configurations pass all seven checks before and after installation,
with matching Python/data fingerprints within each pair. The preinstall pair
qualified an earlier CSV serialization of the same guard values. An append-only
writer then preserved all5,734,359 baseline CSV bytes; parsed guard values,
the qualified object and complete predicted ELF remained unchanged. The final
installed pair executes that final packet freshly. Shared tools-check passes.
The real sibling's existing edits and dependency hashes remain unchanged. Existing
duplicate generated_12D630 Make warnings remain unchanged. A fresh-directory
screen exposed and removed a setup dependency on a prior guest receipt;
every credited suite executes its own guest test.

Baseline consumer `3a8d4fca68874f740153ddf2b59ffb8c9eef1621`; tools `b8f0ed451e570a757733b8d812e3f72905e4e3df`.
Tools commit `23d455b17a69f729a41adc0010a1e91d7eaf4cd4` precedes the
consumer source/build/guard/docs commit. No push. Available host applicability
is recorded separately; no host/Release changes or gameplay claim. Zero
Claude calls. ECc70 remains pending. Finish graph retention and immutable
banking before the next recovery; keep the total85% goal active.

Graph maintenance: the native update exited 1 with all
70,901 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,963 nodes / 168,497 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
