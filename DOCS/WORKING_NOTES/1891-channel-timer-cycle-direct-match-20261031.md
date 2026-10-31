# 1891 - Timed actor channel cycle, direct C match

`func_15080348` replaces its zero-return placeholder with a complete semantic
`void func_15080348(u8 *actor)` implementation in
`conker/src/game/generated_AD6B0.c`. All 58 words emit directly from C under
the existing O2/g3 profile. No guards, instruction inserts, omissions, source
header changes, compiler-profile changes or image exclusions are introduced.

## Retail contract and recovered behavior

- VA `0x15080348..0x15080430`; ROM `0xAD7F8..0xAD8E0`: 232 bytes,
  58 body/slot words, no alignment words.
- Frame 32; saved RA at SP+20; captured cycle index at SP+28; actor pointer
  home at SP+32. Input is the optional actor pointer in a0. There is no
  consistent return-value contract in the original branches.
- Zero mode `D_800D1928` or a NULL actor leaves state unchanged, including
  timer `D_800427F0`.
- Mode one writes actor byte `0x1FF`: zero below signed timer 1000, one at
  or above 1000. Other nonzero modes capture `D_800D192C`. A signed timer
  strictly above 1000 enables the countdown test.
- The actor countdown byte at `0x135` minus `D_800BE9E4` uses 32-bit wrapping
  subtraction and a signed negative test. On expiry, increment the captured
  index with 32-bit wrapping; values at least five reset to zero. Load the
  indexed word from `D_8009BD10`, truncate into actor byte `0x134`, call the
  RNG, and store signed remainder seven plus four into byte `0x135`.
  Publish the captured index after the RNG call; clear the timer last.
- Explicit SDK32 unsigned intermediate operations retain the original
  `subu`/`addiu` wrap behavior without native signed overflow. Keeping the
  byte load and subtraction as separate assignments recovers the original
  register allocation directly.

`D_8009BD10` comes from `asm/data/2407D0.rodata.s`: words
`0, 1, 2, 3, 4, 0, 0, 0`. The normal cycle uses entries zero through four;
`func_15080200` initializes the index to zero. Portable successful-access
tests retain valid table indices; they do not claim defined C behavior for
corrupt negative array indices.

## Qualification evidence

Artifacts and receipts are in
`conker/build/game-channel-timer-cycle-15080348-match/`.

- Original, raw C and padded payloads have identical 58-word bodies and all
  17 relocation bindings. Raw payload SHA-256:
  `aa17be61f2765ad3d1b72ae3973bd2a8171c09d5568402511196bad4b49c87bc`.
- The complete owner preserves all three neighbors and normalized pools.
  Actual Make runs three commands; target, owner and Make diagnostics are
  empty. The entire inherited guard CSV remains identical.
- 2,066 guest cases / 6,198 executions exercise all 58 root instructions,
  timer boundaries, NULL/disabled paths, every countdown byte, five cycle
  indices, signed wrapping, actor/global aliases, RNG mutations and captured
  index lifetime. Register state, memory, traces and fault contexts agree.
- 58 access-prefix cuts, including five branch-delay cuts, and nine literal
  independent symbol rebases agree across original/raw/padded streams.
- The original 12-word RNG helper is connected in 128 cases. Eleven helper
  words execute; its final padding nop does not. Its real results are
  nonnegative. Negative scripted RNG returns are explicitly bounded extension
  cases for signed remainder behavior, not real-helper reachability claims.
- Native SDK32 checks pass 35,928 cases per profile at O0/O2/O3 with UBSan,
  complete arena/canary comparison and native-endian actor/global aliases.
  Thirteen separately compiled semantic mutations are effective in both
  IDO guest and native checks. Compile/interpreter failures do not count as
  effective controls. No strict-aliasing suppression is required.
- ROM census finds no aligned direct JAL, direct J, or literal target pointer
  at any byte offset in the 2,467,288-byte input. Two injected encodings verify
  the census detectors. This is an explicit absence of these static-reference
  forms, not proof of unreachability, an invented caller window, or complete
  indirect-call resolution. Entry ABI evidence comes from the original body.
- Eight fresh canonical checks pass independently in both tools copies,
  followed by shared tools checks. After installation, two checks rerun in
  each copy; six unchanged semantic checks are reused only under exact input,
  module and qualified-artifact fingerprints.
- Strict whole-image prediction changes exactly 190 bytes: 189 target code
  bytes plus one function-extent byte. Metadata changes zero bytes. All 6,055
  other disassembled function bodies and all addresses remain fixed. Protected
  Game data remains byte-exact across 189,088 bytes and 720 owners.

Production ELF SHA-256:
`73099a6b504962d5910b421f1ea5d84619973fa462cdd677ce73d0e553224fd7`.
The production build and actual adopted-ELF recount reproduce that image.
The C inventory CSV remains byte-identical.

## Banking and continuation

The tools commit `34d6ee2fbba95cd6dc56031d6dd308817e853285` precedes the consumer commit. Only the three new tool
modules are committed there; all inherited older-mirror changes are preserved.
No publication or host-port/runtime gameplay claim is made.

The actual recount is **3,968 / 5,506 exact C (72.07%)**, with Game
**3,295 / 4,833 (68.18%)**, Init 492/492 and Debugger 181/181. Address drift is
zero; 1,538 C functions remain different. The 75% goal stays active at 4,130
exact functions, requiring **162** additional matches. Root README changes
only its two aggregate status rows; function details remain here.

Graphify receives a scoped structural refresh for the eleven changed files,
retaining prior nodes and valid relationships while retiring the obsolete
placeholder return edge. Historical communities remain historical; no global
clustering, centrality or full-corpus re-extraction is claimed.

Next screening candidate: `func_150D1F6C`. Screening is not installation or matching
credit. Private candidates and frozen sibling Release artifacts remain intact.
