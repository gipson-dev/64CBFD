# Ring constructor guarded byte match - 2026-11-24

`func_150C88D0` is recovered as semantic C in `conker/src/game/generated_F5800.c`.
The complete linked 102-word / 408-byte slot is byte-exact after 22 expected-word
guards. The C compiler emits the same 102-word length, 56-byte frame, saved
register lifetimes and loop. Eighty raw words already match. This is a guarded
match, not an unmodified compiler byte match.

Production recount: **4,658 / 5,528 (84.26%)** total, Game **3,985 / 4,855
(82.08%)**, Init **492 / 492** and Debugger **181 / 181**, zero drift and 870 different.
**41 more functions are required for 85%**. Only this target earns one match;
no helper, caller or private matrix draft receives additional credit.

Retail VA 150C88D0..150C8A68, ROM F5D80..F5F18, owner F5800. The recovered ABI
returns a pointer and takes a 48-byte descriptor pointer, signed extra bytes,
byte priority and signed allocation group. Existing allocator and SDK helper
declarations were inspected and retain their proper parameter widths.

The routine allocates a type 0x31 record containing the descriptor, five bands
and a sine/cosine lookup table. It preserves the allocator failure exit,
48-byte copy, repeated descriptor-count reads, pointer layout, lifetime and
single-precision angle step. The lookup pointer, count and step remain live
across opaque trig calls. Explicit temporary assignments sequence each call
before the subsequent lookup-pointer read. This removed a native C evaluation
order ambiguity without changing any IDO raw instruction or relocation.
The one-element storage tail documents the variable allocation layout.

The 22 guards retain the entire instruction multiset: header scheduling,
one commutative allocation ADDU and one branch whose absolute destination is
unchanged. One HI16 relocation moves with its instruction; its LO16 remains
bound to the same global. No inserted or omitted instructions, pool changes,
profile changes, copied assembly body or Makefile change is used. The complete
old 6,174,532-byte guard manifest is retained as an exact prefix, followed only
by the 22 new target rows. Both padders reject corrupted guarded words.

All 18 raw and padded owner neighbors retain their bodies, extents and relative
bindings. An actual three-command Make route reproduces the qualified owner.
The independent reference starts with frozen old C and the original target
assembly; its complete predicted ELF equals the actual shadow Make link with
327 changed bytes and zero exclusions. The 189,088-byte protected Game data
section and all 720 data owners remain exact. Production Make reproduces that
same predicted image; conversion rows and all other frozen inputs are audited.

Four independently assembled instruction streams are checked: normalized C,
both padded owners and original assembly. Each agrees with pristine retail.
Guest qualification runs 820 cases per stream, every instruction, all four
rounding modes and 135 access-fault quads with identical complete prefix state.
It covers allocation failures, zero-count division, mutable providers and
guest-only overlap. Boundary checks reject 44 guarded corruptions, expose 160
unguarded corruptions, pin 6 bindings, reject both oversized slots, perform 16
GNU links and 32 guest runs across HI16 carry, LO16 sign and address regions.

A complete aligned pristine-ROM census finds exactly two direct JALs at
ROM F79A0 and F9A00, and no entry pointers. Original descriptor-building argument
windows execute 144 cases across both routes and all four streams, including
the final delay-slot store. Wrong priority is an effective negative control.
This qualifies the call boundaries, not complete parent-function execution.

SDK32 native C passes 376 legal bounded, backed, nonoverlapping cases at each
of O0/O2/O3 with strict aliasing and UBSan. Ordered provider arguments and
canonical dual32 memory digests are compared with the independent reference.
All 256 priority byte values, all four rounding modes and ten effective source
controls are covered. Each control exits 42 from comparison; signals or UBSan
traps are never counted as effective controls. Negative/wide integer and
overlap behavior is qualified in guest instruction tests, not portable C.
Native digests are finite test evidence, not an all-input equivalence proof.
Allocator, memcpy and trig internals are contracted, not executed here.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 90.813s | 5 fresh / 0 reused |
| preinstall-sibling | 89.938s | 5 fresh / 0 reused |
| installed-primary | 85.646s | 5 fresh / 0 reused |
| installed-sibling | 91.874s | 5 fresh / 0 reused |

Shared `make tools-check` passes. The second copy is an isolated dependency-
verified overlay of the separately audited tools checkout; its dirty work
remains untouched. Prior neighbor semantic evidence is reused only under
unchanged body, ABI, relocation, pool and guard inputs; it is not fresh testing.

Consumer baseline: 3e654606aef3971cd40842c6257089c811eb3a73.
Tools qualification commit: `1f6af823fed3906e5d92790aabd62f9c93679f2c`.
ELF SHA256: `c0cbb2f97ee5df1f98b95e2d022d23f47bb7f505549552e4b466dc07af337ac9`.
Padded owner SHA256: `7680b53bda78fd765e823f262afda9c647312332349078af830dfe92d0ca12f5`.
Frozen inputs: 3497; frozen file copies: 2088. Private receipts are under
`conker/build/game-ring-effect-150c88d0-private`.

The preceding `func_150C8730` matrix draft stays private and uncredited:
104 words/frame 184/27 differences versus retail 104/frame 192. Its sole bounded
Claude Pro packet review was advisory, with tools/MCP disabled and no writes;
none of its suggestions resolved the frame. Equal difference counts for grouped
variants did not imply identical words. The ring recovery uses zero Claude calls.
See the private matrix `HANDOFF_CURRENT.md` for the precise rejected screen.

Graphify was queried before recovery. After source changes, run native update
and a scoped AST merge retaining every old ID and qualification; wait for the
actual commit-hook producers to terminate before the final merge and baseline
bank. No full-corpus extraction, host/Release change, gameplay acceptance or
push is claimed. Next: screen the 212-word `func_150C8A68` ring updater. The 85%
goal remains active.
