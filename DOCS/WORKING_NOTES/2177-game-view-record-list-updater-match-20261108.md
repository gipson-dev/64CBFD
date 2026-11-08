# View Record List Updater Byte Match - 2026-11-08

`func_150A104C` now replaces its zero-return placeholder with the complete
record-list/view-state updater. The semantic C has all **94 words** and the
original **888-byte frame**. Twenty expected-word guards normalize a closed
saved-register role cycle and save schedule; the installed function is
byte-exact. This is a guarded match, with 74 words already literal from C.

Fresh production totals: **4246/5513 = 77.02%**, Game **3573/4840 = 73.82%**,
Init 492/492, Debugger 181/181, zero address drift, 1267 different. **165 more**
exact functions reach 4411/5513 and 80%. Conversion rows remain unchanged.

## Source and recovered interface

Owner `conker/src/game/generated_CDE80.c`; VA 0x150A104C..0x150A11C4,
ROM 0xCE4FC..0xCE674; 376 bytes; normal IDO 5.3 O2/g3/MIPS2/O32 profile.
Interface: `void func_150A104C(struct108 *view,
GeneratedCDE80Record **records, s32 count)`.

The local record type now names its signed halfword at 0x08 `heightOffset`.
The unchanged 52-byte layout retains flags at 0x15 and subtype at 0x17.
The complete typed owner emits exactly the same raw code as the private
byte-cast draft, including all 28 bodies; no shared header changes.
A local forward collision declaration and extern float D_8009F5AC are added.

The routine builds one 812-byte struct127 at SP+0x4C. It copies the view's
current x/y/z at 0x2F8/0x2FC/0x300, duplicates current Y to query+0x180, and copies
old x/y/z at 0x304/0x308/0x30C. All other query bytes retain original stack
contents. It sets view+0x364 from D_8009F5AC and clears view+0x84 bit 0x40000,
including for a zero count.

Each list slot is read once before the null check. Non-null records are
submitted to func_150A1DA0(query,record,0). Only a zero service result
proceeds; the slot is reloaded after that call, so provider redirects are
visible. Accepted records require flags byte 0x15 >> 2 equal to 1. Subtype 2 sets
view+0x364 to signed halfword 0x08 plus signed origin Y at 0x02, converted to float32;
subtype 0 sets bit 0x40000; subtype 6 clears it. Other subtypes do nothing.
Every slot advances the local list and decrements the full count word.
Later accepted records win. Query construction is not repeated after calls.

## Derived allocation normalization

The initial 94-word draft had 39 differences. A named current-record local
recovers A1 and the original slot reload; placing case 2 before 0 recovers
retail's switch body order. This leaves 20 raw differences. Mask/result
locals move the query four bytes and are rejected. Unsigned masks/counts,
register hints and equivalent loop/equality forms do not improve the result.

Raw body SHA256: `51cbc833f40f00db183a7db6a9aa02dc3db4ce1ec15c13227dc3a4c3b649b709`.
Its remaining differences are exactly one closed role cycle:
raw S3->retail S4->S5->S6->S7->FP->S3. Fourteen words change only their
GPR fields. The six stores at words 1,11..15 form a closed permutation of
the same register/stack-slot pairs. Each original callee-saved value is
saved before its new role is initialized; the fixed restore slots remain
unchanged. All opcodes, branch targets, calls and bindings are preserved.

All three bindings remain literal: D_8009F5AC HI16/LO16 and collision JAL.
The guard manifest preserves every inherited byte and appends 20 rows.
All 94 raw-word corruptions, all 3 binding corruptions and a changed inherited
CSV prefix are rejected. The production padder separately rejects a wrong
word and an unexpected relocation at each of the 20 guard positions.

## Complete owner and independent image gates

Predecessor consumer 07e7e90e440fbaab454a9977d06883c73a56565a and tools
397892277a84b39bd0a2f9d91fb3f62ad4fca2a7. Frozen inputs: 99 files, including
the complete owner, original assembly/caller, all headers and compiler stages.

All 27 raw/padded neighbors, allocatable pools and register metadata remain
fixed. Production and strict padders agree on all 28 bodies/pools; all 31
original case-label definitions are accounted for. The actual copied
five-command Make recipe equals the complete qualified object.

The independent whole-ELF predictor equals production with **302 changed
bytes and zero exclusions**: 300 target-body bytes plus 2 symbol-size bytes,
12->376. No metadata permutation. Every other linked body, all 6053
addresses and all other named definitions remain fixed. All 189088 protected
data bytes across 720 owners stay exact. Makefile, shared headers, layout,
absolute rules and progressCSV remain unchanged. The 20 new guard rows apply
only to this function; inherited rows are preserved exactly.

The scoped production build compiles this owner once at O2/g3 with no C
diagnostics. Existing duplicate generated_12D630 recipe warnings and the
normal development-image checksum rejection are recorded separately.

## Focused qualification

Both mounted and sibling configurations pass six fresh tests before and
after installation. Task modules use an ignored consumer-side sibling
overlay, with helper origins/fingerprints and explicit missing-helper
fallbacks recorded. Its 2434 pre-existing dirty paths stay unchanged.
Both shared smoke checks are fresh; three unchanged synthetic shared
regressions per copy are explicitly reused by exact source/helper hashes.

| Check | Evidence |
| --- | --- |
| Ordered guest model | 1027 cases; raw C output and normalized retail output agree with independent public effects and provider observations |
| Query payload | Seven initialized float32 fields; complete 812-byte seeded guest observations; signed zero, infinities, NaN payload and subnormal copies |
| List effects | Null/class/result gates, full count word, current/future slot redirects, first-slot isolation, last accepted record wins |
| Mutations/aliases | Query/view/list/record/constant/incoming-home changes; explicit query/list/view/record overlaps |
| Original caller | 18 original words, 24 connected cases; null-view and zero-count skip gates, list load in JAL delay slot, actor-byte reload |
| Native32 | 517 cases at each of O0/O2/O3; real SDK actor 812/view 2464/record 52/pointer 32 layouts; typed signed field 0x08; trapping UBSan |
| Effective controls | Stub, unsigned height, wrong secondaryY, wrong class, cached record, inverted service truth, skipped empty initialization, query rebuild |
| Fault prefixes | 338 executed access cuts/prefixes, including 3 negative/full-word count probes; literal normalized low-word states |
| Relocation/image | Two independent GNU links with signed LO16 carry; all 3 bindings; four complete-image corruption controls |

Exactly 91 words are reached from the public entry. Original words 64,72,76
are unreachable duplicate loads after unconditional branches. All 94 words
are retained and matched; no artificial interior entry inflates coverage.
Whole-ROM aligned census finds one JAL at ROM 0xCE6DC, no entry/interior
pointers and no direct interior jumps. No active C caller/prototype repair
outside this owner is required.

The caller fixture includes the original LUI/count and null-view setup;
normal arenas are disjoint from its stack. Explicit aliases remain separate.
One-record mutation cases prevent later records from hiding a stale pointer.
Native providers read only the seven initialized fields. Sparse/invalid
pointers, private stack aliases and wrapping count prefixes are bounded
guest probes, not portable native-array claims. Fault equivalence applies
to normalized instructions; the raw save schedule is not claimed identical.
Collision geometry, the complete large caller, full hardware upper-register/
FCSR behavior and gameplay acceptance remain outside this function's proof.
Routine task: zero Claude calls. Host and frozen Release remain untouched.

## Bank and next action

Production ELF SHA256: `af2715001558385cec85d33baac281f90e3a0a4f52397da02ce0afe141748bf4`.
Binary: `6604afd9c2031abbc08000b8c81a523717d2f4f78e968b8a525a72a5b1f58624`.
Owner: `9bcd88dfba5b20e1b123c71b61ffe437d962ff52c06d3cdfc2387767bfac35ef`.
Guard CSV: `8d83b0e799e72ae61f2462c36f033d3d0757427d4839506e9d1bf59f1b319e69`.

Reproduce in prepared WSL from the decomp root:
`python3 -m unittest tools.tests.test_game_view_record_list_150a104c_match -v`.
Canonical receipts: `conker/build/game-view-record-list-150A104C-match/`.
Commit tools first, then source/guards/docs/README aggregate rows/pin locally.
No push. Graphify is refreshed with explicit old-node retention; this is a
scoped update, not a full-corpus extraction.

Next inspect `func_150A0D8C`, the 173-word class-6 record/actor scan, including
the 25-actor traversal, floating state, live record base and four call sites.
The full 80% goal remains active; func_1513FAB4 remains private and uncredited.
