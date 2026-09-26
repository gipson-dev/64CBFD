# Game fixed-matrix identity match - 2026-09-26

## Result

`func_150A7B80` is byte-exact across all sixteen words at
`0x150A7B80..0x150A7BC0`. The linked matcher reports
`2626 / 5483 (47.89%)` overall and `2058 / 4794 (42.93%)` game, with one
address-drift blocker and 2,856 total differing C functions. Debugger remains
complete at `181 / 181`.

## Source and compiler boundary

The function clears all eight 64-bit words in a fixed matrix, then writes one
to halfword offsets `0x00`, `0x0A`, `0x14`, and `0x1E`. Retail emits eight
unrolled `sd` instructions followed by the four diagonal `sh` instructions,
with the last diagonal write in the return delay slot.

The source now expresses those eight clears explicitly instead of using a
loop. IDO 5.3 nevertheless lowers every `u64` assignment to two 32-bit stores,
so the compact body is 34 words and cannot fit the 16-word retail slot. The
normal padding path therefore redirects the oversized body to
`.game_overflow`.

`pad_c_object.py` now emits overflow slots as guarded words with the jump's
`R_MIPS_26` relocation made explicit. Normal non-inserting word patches can
replace those slots after checking the original word and relocation state;
attempted insertion is rejected. Fourteen guarded rows replace the trampoline
and zero fill with the retail instruction stream. The new unit test assembles
an oversized fixture, replaces its trampoline, and verifies both the final
words and removal of the original jump relocation.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0xD5000`
- retail `conker/conker.us.bin+0xD5030`
- SHA-256 `108873d13a1c690c87868608bf80cf08d8f25d68c2effd60fe2268c9253dde17`

The patch table contains 858 rows with no duplicate
`(filename, function, offset)` keys. The focused three-test padding suite, full
nonmatching build and link, fresh direct matcher, outer build, and project tool
checks passed.

The `64CBFDOGL` sibling contains generated recompilation output and historical
backup artifacts for this address but no separately maintained C/C++ host
implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 16-word `func_1516A770`, now the smallest ordinary-C game row
among the fourteen-difference candidates. Retail scans a zero-terminated byte
string, replaces each `0xBD` byte with zero, and returns the traversed byte
count including the terminator. The current generated C body is only a
zero-return placeholder.
