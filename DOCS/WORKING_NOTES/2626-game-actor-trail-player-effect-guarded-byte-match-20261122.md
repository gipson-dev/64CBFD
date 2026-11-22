# 2626 - Actor trail and player effect guarded byte match

Date: 2026-11-22. The total 85% matching goal remains active.

`func_15194810` replaces its zero-return placeholder with complete semantic C.
Its **116-word retail slot matches through seven expected-word guards**.
Raw C has **six linked-word differences**; it is not raw byte-exact C.
Fresh production is **4,608 / 5,528 (83.36%) total**, **3,935 / 4,855
(81.05%) Game**, zero address drift and 920 different converted functions.
Init remains 492/492 and Debugger 181/181. **91 more matches** reach 85%.

## Recovered source and ABI

Source `conker/src/game/generated_1C1150.c`; preserved original
`conker/asm/1C1150.s:797`. VA `0x15194810..0x151949E0`, ROM
`0x1C1CC0..0x1C1E90`, 464 bytes. Frame 168 (0xA8), RA at SP+0x1C,
no saved S0. The three-pointer ABI has unused source and byte-context pointers;
the actor is live only through the surface service. Caller continuations
discard or overwrite the callback return. This is recovered as `void`.

Actor kinds 0..4 use the five-entry jump table; kind 0x53 uses the separate
branch-likely path, including its X-load delay slot. Other byte values return.
The XYZ snapshot precedes the surface helper. Y adds single-precision 95.
Snapshot12@SP+0x9C, trail68@SP+0x58, angles8@SP+0x50 and surface36@SP+0x2C
retain the original storage and lifetimes. The trail uses time10/5,
scale D_800A82E4/E8, radius5/D_800A82EC, counts15/10, selectors3/2,
durations70/22, modes155/100, selector0, chance0.5 and values16/15/request0.
Angles are 0/255/-63/57. No private bytes are filled artificially.

The eight-byte `PlayerEffect15194810` at SP+0x24 has flags1, duration
`(u32)RNG % 11 + 20`, level8, playerMask1 and callback-1. Private byte1 and
tail byte7 retain uninitialized/private contents. The original registration
provider copies eight bytes. An initial seven-byte array draft failed native
alignment sanitization; recovering the typed halfword field gives natural
alignment and emits identical MIPS bytes. This record is named for the
observed player-registration interface; audio or hardware behavior is not
claimed from the opaque provider model.

## Guards, tables and owner

Raw target SHA256 `b0eeb280856642706f7cc9dd3b95a77a1256ce9bb50c009eb521bbfc81209ba8`.
The full owner contains 29 functions; all 28 other raw and padded functions
are identical. Existing O2/g3 and mixed GLOBAL_ASM ownership are retained.

Two relocation-aware guards retarget the new packed table at offset80 to
the retained retail `jtbl_800A82D0`. Its five entries all point to target+0x50.
The old 80-byte pool prefix and its 20 owner/offset bindings remain unchanged;
the new entries occupy bytes80..99, followed by 12 compiler alignment zeros.
The table's packed address is not inferred to equal its interleaved retail
address. Both HI16 and LO16 bindings are guarded, even where bound HI matches.

Five other guards rotate only independent `A0=SP+0x2C` from word25 to the
surface JAL's delay word30. JAL word29, float arithmetic, and ordered memory
instructions are unchanged. There are zero insertions/omissions. Every prior
guard byte is preserved as a 5,731,319-byte prefix; no neighbor guard changes.
Raw private fault PCs are not claimed equal. Normalized/original words and
complete access-fault states agree.

## Fresh qualification and production

- Guest: 3,280 cases per raw/normalized/original stream, all256 actor kinds,
  all116 words, special/reject paths, unsigned RNG boundaries, nonfinite Y,
  two stack phases, alias inputs, mutable provider inputs and incoming homes.
  Complete raw end states agree; trace comparison explicitly rebases only
  the packed table read.154 normalized/original access-fault pairs pass.
- Actual callbacks: D_80086694 index11, pointer800866C0/ROM22B180; both
  original/current JALR windows1505BD78 and1505C6DC,160 cases/stream and
  all17 caller words. Two missing-delay controls fail effectively.
  Full parent functions are not executed. Surface89, trail-submit168 and
  registration111-word provider extents are statically retail-exact.
- Connected RNG: all18 original 64-bit instructions,480 cases/stream,
  independently checked seed transitions, signed64 return followed by
  unsigned32 remainder. Remaining providers are contracted.
- SDK32: O0/O2/O3 each4,288 valid typed-object cases, strict aliasing,
  UBSan and natural packet-layout assertions. Nine effective source controls
  reject missing special kind, wrong range/height/scale/radius, signed RNG
  remainder, wrong span/player-effect level and late position capture.
- Both padders reproduce original target payload/relocations.16 GNU links
  cover all12 target binding sites including HI16 carry boundaries. Five
  controls reject stale words/relocations, duplicate guards and wrong output.
- The natural mixed Make route executes five commands and reproduces the
  qualified owner. Production `make -C conker -j4 build/conker.us.elf
  progress.csv` passes; known duplicate generated_12D630 recipe warnings
  remain. Fresh linked recount supplies the totals above.
- Complete ELF prediction is literal with **464 changed bytes / zero
  exclusions**. Target body and12-to464 symbol-size update plus four closed
  GNU metadata permutations account for every changed byte. All19 named
  definitions/attributes and209 string bytes are explicitly reconstructed.
  All189,088 GameData bytes and720 owners remain exact; conversion rows,
  other bodies and addresses are preserved.
- Both primary and isolated sibling-overlay copies pass all five focused
  checks before and after installation. Shared tools-check passes. Inputs,
  imported Python/non-Python dependencies, real sibling dirty status and
  sibling dependency hashes are checked. Prior neighbor suites are reused
  only for unchanged source/profile/bindings; they are not called fresh runs.

Production ELF SHA256 `2cd8cb2aca5b65bc71d65e3eeb9a37bd638fe2e6e6cff8213dc9bac6ed5135a4`.
Baseline consumer `e33a4207ca2f5a2eb32914b0fb70e5b0c773ee6e`, baseline tools `13fe746e4103a8525fc3c20e3b0beebbb8e197d4`.
Qualified tools are committed first as `12b7ec9fdaba9912f0d3af478a514cca20f54bac`;
the consumer checkpoint records that pin. No push or real sibling overwrite.

## Limits and continuation

Zero Claude calls: local instruction, ABI, compiler and execution evidence
resolve this routine. The available host scene configuration consumes binary
code rather than this C source, and its input does not share this target's
retail mapping. No host/Release build or gameplay acceptance is claimed.
Continue the remaining Game function census toward85%; older uncredited
private camera/position/history candidates remain outside accepted totals.

Graph maintenance: the native update exited 1 with all
70,436 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,488 nodes / 164,533 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
