# Working Note 1911: Ordered script-list insertion

Date: 2026-10-31. `func_1509B810`, ordinary owner `game_C8950`.
ROM `0xC8CC0..0xC8DAC`; VA `0x1509B810..0x1509B8FC`.
Tools: `646f4fd7724794ac55207b99a474d7249add2117`.

## Recovered behavior and interface

The zero-return placeholder becomes
`void func_1509B810(ScriptNodeC8950 *node)`. It inserts a script node into
`D_800D2F48`'s ordered doubly linked list. The existing local node/list types
and alias macro are reused; no shared declarations change. The list header
is 12 bytes, the node is 32 bytes, and next/previous links are at 24/28.

The key is the unsigned kind halfword masked with `0xFFFF03FF`, effectively
its low ten bits. Starting at the tail, the routine scans backward over the
cached unsigned halfword count. It inserts after the first strictly smaller
key, or at the head when none is smaller. Equal keys are passed while scanning,
so a new equal key precedes existing equal keys. Empty lists set both ends
and clear both node links. Tail, middle and head insertion each preserve the
original store order and increment the live halfword count with 16-bit wrap.

The final unsuccessful scan iteration still loads the previous pointer.
That read is preserved even though the fallback then reloads the head.
Link reads also remain repeated where earlier stores can alias them.
Guest tests include insertion aliases to existing nodes; these preserve
retail behavior without promising a valid list after reinserting a member.

The original 86-word `func_1509B5AC` is the only aligned JAL caller in the
complete frozen decompressed input, at ROM `0xC8AE4`; no literal target
pointers are found. Its call delay slot forwards the created node. It reloads
the node kind after insertion and eventually returns its saved S0 node pointer,
independently of insertion's V0, proving the recovered void result contract.
Its existing source placeholder remains unchanged. This is not a census of
all possible indirect runtime calls.

## Matching and qualification

Ordinary O2/g3 emits all 59 body/slot words with no frame or alignment padding.
All two HI16/LO16 bindings to `D_800D2F48` are preserved. There are 57 reachable
words; offsets `0x90` and `0xB8` are unreachable retail duplicates.
Eight expected-word guards at word indices 5, 7, 25, 46, 47, 54, 55 and 56
normalize the closed tail snapshot, loop predicate and final increment register
choices. There are zero insertions or omissions. All sixteen actual padder
stale-word/binding controls reject. This is a guarded C recovery.

An ordinary do-while form caused IDO to unroll to 114 words. The explicit
boolean loop condition and `next_node` label retain the original access order
and 59-word shape without changing the Makefile or compiler profile. Other
55/58/60/114-word exploratory forms are retained privately as rejected evidence.
Raw C memory, preserved registers, ordered calls and memory access traces
agree with retail; caller-saved temporary registers need not be equal.

Guest qualification passes 2,433 cases: 9,732 normalized and 2,433 raw runs,
three independent rebases, 324 alias cases, 73 access-prefix cuts and 16
branch-delay cuts. Every reachable word is covered, including count-65535
wrap and the final predecessor read. All normalized architectural state and
prefix traces agree across the original, normalized C, padded and Make objects.

Native32 O0/O2/O3 each pass 589,825 cases with trapping UBSan: every 16-bit
new kind value across nine list sizes, upper kind flags, equal keys, list ends,
middle links and a count-wrap case. Expected list ordering is checked against
a mathematical insertion position; node kind/padding and header padding remain
unchanged. Eight wrong semantic controls exit 1. Native tests cover ordinary
nonmember insertion; full guest fixture comparisons provide alias evidence.

The complete original caller passes 160 cases, 640 normalized and 160 raw
runs. Its lookup, creator and event helpers are opaque providers, with volatile
registers and argument homes clobbered. Both the early bitset gate that bypasses
insertion and the post-insertion flag paths are included. The early gate indexes
the full 16-bit input; the later gate masks to ten bits. The fixture therefore
uses the full 8,192-byte bitset. This proves the bounded caller interface and
continuation, not a full original creator or gameplay path.

Both tools copies pass all eight fresh canonical methods with no skips,
plus shared tool checks. After installation each passes two fresh installed
checks and reuses six semantic checks only after complete input/module/artifact
fingerprint equality. All sixteen owner neighbors and pools remain identical.
The three inherited C warnings are unchanged. Actual Make executes five owner
commands: preprocessing, compilation, postprocessing, padding and assembly.
Its pre-existing duplicate-rule warnings are retained.

## Production and handoff

The independent complete image prediction agrees with the production link:
171 changed bytes, comprising 170 target code bytes and one target extent byte.
There are zero metadata changes and zero excluded ranges. All other 6,055
linked bodies and all 6,056 function addresses remain fixed. All 189,088 bytes
across 720 Game data owners remain exact. Existing guard rows and conversion
CSV bytes are preserved. All 17,269 sealed inputs are checked before adoption.

Production ELF SHA-256:
`eee144eb2ebf4e7589f3823a47f31889c93002b2d3951887598bee6d7fb3e2e6`.
Map SHA-256:
`19139e6eb3cb32838dba4e8909f0275dc9bc2b9ce99a8efd030e800380070e85`.

Captured installed-ELF recount: Total **3,988/5,506 (72.43%)**;
Game **3,315/4,833 (68.59%)**; Init 492/492; Debugger 181/181; zero drift.
The 75% threshold remains 4,130, with **142** more exact functions needed.
Tools are committed first; the root README changes only two aggregate rows.
The eleven-file scoped AST refresh retains old nodes and valid directed
relationships, retiring only the obsolete s32 placeholder return relationship.
It does not claim full-corpus extraction or fresh global clustering.

Next screen: `func_150E1060`, uncredited until its complete gates pass.
Evidence is under `conker/build/game-script-sorted-insert-1509B810-match/`,
including canonical and installed receipts, private caller/native/guest checks,
strict production proof, captured recount, function views and final banked seal.
Private candidates, old tools mirror work and sibling host/Release outputs
are preserved. No push is performed.
