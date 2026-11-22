# 2620 - Owner mask effect guarded byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_151B9F00` now has a complete semantic C implementation. Production
recount measures **4,603 / 5,528 (83.27%) total** and **3,930 / 4,855
(80.95%) Game**, zero address drift and 925 different converted functions.
Init remains 492/492 and Debugger 181/181. **96 further matches** are needed
to reach 85% at the current denominator.

## Recovery and exactness boundary

The source is `conker/src/game/generated_1E73B0.c`; the preserved original
starts at `conker/asm/1E73B0.s:11`, VA `0x151B9F00..0x151BA084`,
ROM `0x1E73B0..0x1E7534`. The complete routine is 97 words / 388 bytes, frame
0x78, RA at SP+0x1C and eight relocation sites. Existing O2/g3 and mixed C/GLOBAL_ASM
membership are retained. All 56 neighboring functions, constant pools and
compiler diagnostic rows are preserved.

The null owner returns null. Otherwise the routine snapshots the owner pointer
and identity byte at 0x3B into an eight-byte header, fills a 60-byte effect
descriptor, and selects its mask at 0x39 using signed mode/player flag bytes.
Owner stride is 812 bytes. For indices below 2 with a nonzero flag, mode 2 uses
mask 253; mode 4 uses 251 for index 0 and 247 otherwise. Other modes retain 255.
The descriptor preserves lifetime 300, resource 429, field30=9, field8=1,
fieldC=0x200205, field10=0x60600 and the remaining retail fields.

The factory `func_1513B5E0` receives descriptor, 1, 8, byte priority and full-word
context. Its signed 32-bit return transports the created pointer. On success,
`memcpy` copies the saved eight-byte owner/identity header to
`created + *(s32 *)(created+0x50) + 0xF8`; the original created pointer is
returned. Helper mutation cannot replace the cached identity with a later read.
The local descriptor view exposes byte 0x39 within the factory's full 60-byte
copied representation. Parent padding remains object representation rather
than a portable C value guarantee.

**This is a guarded match, not a raw compiler byte match.** The complete C
emits 97 words / frame 0x78 with 25 positional differences. Twenty-four changed
words lie inside one closed 25-instruction window at indices 9..33, moving
independent owner-index division/address work relative to descriptor stores.
The instruction-plus-relocation multiset is identical and the branch at 32
is unchanged. The remaining word 87 commutes the two destination-address
addition operands. Exactly 25 expected-word/relocation guards restore retail
order; no words are inserted or omitted. All other words and bindings match.
Raw SHA256 is `c123e9e98248d2332ae83bfdf51cd7cfa66a1220402856638d10165c0a125948`.
The prior CSV is retained byte for byte as a prefix, with only these 25 rows
appended. Controls reject stale words, stale relocations, wrong functions,
wrong owners through the exact-output gate, and duplicate offsets.

## Fresh qualification

Run `python3 -m unittest tools.tests.test_game_owner_mask_effect_151b9f00_match -v`.
All five checks pass before and after installation in primary tools and the
isolated sibling overlay. Imports and non-Python inputs are fingerprinted.
The actual dirty sibling and all inspected dependency bytes are preserved.
Shared `make tools-check` passes. Prior unchanged neighbor-suite receipts are
reused explicitly; they are not described as fresh full-project tests.

1. The normal mixed Make recipe executes five commands, with no membership
   override. Normalized padded instructions and relocation bindings equal
   all 97 retail words. Independent whole-ELF prediction equals the link,
   **299 changed bytes, zero exclusions**, solely the target slot and symbol
   size 12->388. There are no metadata permutations. GameData remains exact
   across 189,088 bytes / 720 owners. Production Make also rebuilds every affected
   dependency after the guard CSV changes; its actual full image must equal
   the same independent prediction. Conversion rows remain unchanged.
2. Guest execution checks 3,331 cases per retail/raw/normalized stream,
   all 96 reachable words. Word 47 is statically unreachable. All 256 mode bytes,
   signed index division boundaries including negative/misaligned guest
   addresses, flag/priority boundaries, allocation outcomes, helper mutations,
   dynamic offsets and null owners are covered. Complete final memory,
   private stack, GPR/FPR/HI/LO state, return, calls and ordered accesses agree.
   All 97 sampled access-fault prefixes agree for retail and normalized code.
   Raw arithmetic intermediate states intentionally differ; no raw fault-state
   equivalence is claimed.
3. SDK32 native qualification checks 3,840 cases at each of O0/O2/O3 with strict
   aliasing and UBSan. Valid owner indices 0..3 use actual array objects and
   checked descriptor/header offsets. Six source controls detect wrong masks,
   player gate, resource, copy length and returned pointer. Negative and
   misaligned pointer-index probes are guest-only, outside portable C objects.
4. The complete 93-word original `func_1514F194` caller is current/retail exact
   and executes together with each target stream for 384 cases. Its real JAL
   at 0x1514F204 forwards owner/255/1, including the context in the delay slot.
   All 93 caller words execute; three controls detect a missing call, incorrect
   owner and wrong delay-slot context. This is the sole direct ROM call in
   the census, with no aligned loaded target-pointer literals. Computed
   references are not excluded by that census.
5. Six GNU links independently bind raw/retail/padded objects at two code/data
   bases. R_MIPS_26, HI16 and LO16 sites agree with independent predictions,
   including signed-low carry. Raw is compared to its own scheduling stream;
   normalized output is compared to retail.

The existing 110-word factory slot is retail-exact. The existing 11-word memcpy
slot is not exact. Tests use explicit factory/copy and other caller-helper
contracts with aggressive ABI clobbers; this work claims neither full
allocator/helper execution nor hardware/gameplay acceptance. Existing duplicate
generated_12D630 recipe warnings and unrelated owner diagnostics are retained.

## Production, applicability and continuation

Production ELF SHA256: `b4a55aaa617066ee5da6b02e9c2fe4aef173d233e3d8f266cf6dd5e5243b9abf`. Prior consumer
`71c67fd784466dcdc087e69169c8c07f3476a89c`, prior tools `97e4c021cb195c3138e876759c56be0414304279`. Tools are committed first.
Codex performs implementation/validation; zero advisory/model calls. The prior
Claude authentication failure was not retried. The root README receives
only its Total and Game aggregate row changes; this detailed update is separate.

Sibling host applicability was inspected read-only using its actual saved
scene-recompile configuration/input. That binary/symbol workflow provides no
direct C-source import for this restoration. No host source/build changes or
Release changes were made; no host gameplay parity is inferred.

`func_151BE850` remains private and uncredited. Its best current source is
181 words / frame 200 versus 180 retail, 147 differences. The recovered 108-byte
contiguous scratch layout resolves the 24-byte payload/descriptor overlap, but
typed fallback 151BEEE0 changes a neighboring placeholder and needs its own audit.
See that private CURRENT_HANDOFF.md before resuming; do not normalize a broad
unresolved schedule just to obtain a count. Other private candidates remain
separate. Continue the remaining Game census toward the full 85% goal.

Graph maintenance: the native update exited 1 with all
70,162 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,204 nodes / 161,861 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
