# Note 2600: Actor projection scan guarded byte match

Date: 2026-11-20. Consumer baseline `3a00cf59b23f24db4df4fe35086bcec227b7753c`;
tools baseline `a0e7ec9cf2bb16436d7f27dedcf802f70576a3d6`.
Qualified tools commit: `8ea137f65b2ecd63facfbeb9ff0197c144ddcf12`.

`func_15036148` replaces its zero-return placeholder with complete typed C.
Its **112-word / 448-byte body**, **two alignment words** and **152-byte frame**
match through eight checked rows: six instruction-scheduling rows and two
verified literal-pool bindings. The existing O2/g3 profile and Makefile remain
unchanged. The known caller uses the correct `void(void)` interface and its
complete padded object remains byte-identical.

Fresh production recount: **4,584 / 5,528 (82.92%)** total,
**3,911 / 4,855 (80.56%)** Game, zero address drift and 944 still different.
Init 492/492 and Debugger 181/181 remain exact. **115 more** are needed for
85% at this denominator; the wider goal remains active. Conversion rows and
the complete progress CSV are unchanged: the former placeholder already counted
as C. Root README changes only its two aggregate match rows.

## Source and interfaces

Owner `conker/src/game/generated_61D10.c`, VA `0x15036148..0x15036308`, ROM
`0x635F8..0x637B8`. Its complete retail slot ends at `0x15036310`, including
two trailing NOPs. The recovered declaration is `void func_15036148(void)`.

The routine checks `D_800DBFF0->unk5F0 & 1` once, then scans 25 actors using
the real `struct127` declaration and its `0x32C` stride. It accepts nonzero
interaction states in category 0 or 1, rejects the -10000 height sentinel,
and applies ordered height, bottom and radius predicates. The extent helper
publishes three unsigned halfwords; this caller interprets its first result
as signed. Height and bottom reload after that helper, then a ten-argument
submission receives mode 1, index, current X/height/Z, two zeros, radii 100/150
and alpha 127. Rechecking or caching the wrong fields changes behavior.

The existing `func_1507C3E0` body in `generated_A9260.c` establishes
`void(struct127 *, u16 *, u16 *, u16 *)`; the first result is cast to `s16`
at the comparison. The three output homes are SP+0x92, SP+0x90 and SP+0x8E.
All GPR/RA and six saved FPR pairs retain their retail homes and lifetimes.

The submit helper's two other aligned direct calls are at ROM `0xCE44C` and
`0xCE480` in `func_150A0D8C`. Its existing `generated_CDE80.c` prototype agrees
on two 32-bit integers followed by eight floats. This recovery gives its local
definition that same interface. **`func_15035808` remains an unrecovered
zero-return placeholder**: IDO adds exactly four incoming argument-home stores,
and its symbol size changes from 12 to 28. That dependent ABI change is declared
in the entire-image prediction and earns **no additional matching credit**.
Its return remains ignored at known call sites. Eight other raw owner functions,
including the previous `func_15035FE8`, remain instruction/binding identical.

The root's sole aligned JAL is ROM `0x46854` / VA `0x150193A4`, in
`func_15019130` in `game_45B80.c`. There are no aligned literal pointers to
either routine; computed callers remain unexcluded. All 16 caller functions,
bindings and pools, and its complete padded object, are unchanged. The caller's
three existing Warning 712 messages remain identical after path normalization.

## Closed schedule and literal binding

Raw C already emits **112 words / frame 152** with exact output/saved homes.
Raw payload SHA-256:
`7d4d50dbd89d5fc69a4c18ef41bb975244be1cfc60b7cc5acf574a2d22d5e513`.
There is no frame guard, synthetic padding, volatile or physical register binding.

Only the packet block changes order: swap source words 84/85 and reverse
86..90. Six positional words differ. These are an independent actor-X load,
an FPR-to-GPR move, and five stores to distinct private outgoing words at
SP+0x14/18/1C/20/24. Every other instruction and branch is identical; no branch
enters the block interior. No floating arithmetic or comparison changes.

The compiler emits a 16-byte pool containing `0xC61C4000` followed by 12 zero
alignment bytes. Fresh source qualification validates that complete pool before
two exact expected-relocation guards bind its HI16/LO16 references to
`D_80097D74`, verified at retail ROM `0x23C834`. No retained data is replaced.
The normalizer consumes only the fingerprinted raw payload/bindings; original
GNU assembly and ROM are independent verification inputs, not byte generators.
Two GNU link contexts include independent entry/code/data rebases and a HI/LO
carry case. Changed payloads and relocation maps are rejected.

An independent symbolic packet decoder preserves complete GPR/FPR/private-byte
state and opaque FCSR for arbitrary incoming bit vectors. All 5,040 instruction
permutations agree; five effective semantic defects are rejected. The separate
adjacent-swap proof checks register hazards, disjoint writes and entry targets.
Together with literal identity outside the block, this closes the loop relation
without changing saved-register roles or arithmetic order.

## Fresh validation and retained history

Guest checks cover **768 cases / 9,952 helper calls**, visiting all 112 words
on both sides. Full final RAM and all **168 private/incoming bytes** agree at
every helper boundary. Cases include mutable current/future actors, retained
output pointers, post-helper height reloads, signed-halfword boundaries,
quiet NaNs, infinities and signed zeros. The finite engine does not emulate
FCSR; the schedule proof leaves all arithmetic/FCSR instructions unchanged.

Native SDK32 C passes **768 cases each at O0/O2/O3**, strict aliasing and UBSan.
It uses all 26 complete actor objects, verifies the real shared type offsets,
and checks unchanged view padding. Five source controls reject unsigned height,
a shortened scan, inclusive radius, wrong alpha and cached height. An initial
O2 harness failure was diagnosed at an SSE aligned store: the freestanding
Linux entry needed stack realignment. Only that harness entry changed; the
target source did not. The failed binary/GDB record is retained privately.

Connected caller checks cover **96 cases / 1,244 logical helper calls**. Four
original words execute the JAL/delay and following `func_1515D6C8` JAL/delay,
with explicit three-word setup and four-word teardown trampolines. The next
original call runs, the result is ignored and complete RAM agrees. This is a
caller-window check, not complete execution of the outer frame dispatcher.

Both tool configurations pass **19 focused tests**, six historical-dependency
unit tests and three older whole-image gates before and after installation.
The focus comprises seven new tests, seven previous projection-record tests
and five actor-effect tests. Twenty other prior semantic checks are explicitly
reused through exact fingerprints/AST/provenance; they are not fresh tests.

The sibling validation overlay contains 1098 files:
{'primary-fallback': 736, 'task': 14, 'bootstrap': 1, 'sibling': 347}. Its actual checkout's HEAD, dirty status and all
351 dependency fingerprints are preserved. The
previous record-draw recovery gains only an exact source/guard/caller snapshot
gate; AST comparison proves unchanged source generation. Older fixtures retain
their original frozen owner objects and images, using exact live/frozen hashes.
No historical image is advanced, overwritten or partly excluded. Fourteen
task-only tools files are committed before the consumer. `make tools-check`
also passes.

## Production and continuation

Both target padders emit an identical complete object. The caller's
layout-padded object remains identical to its frozen object; no whole caller
assembly file is supplied or claimed. Actual natural Make recipes execute
three commands per target/caller.
The complete production ELF equals the declared prediction: **396 changed
bytes, zero exclusions**, all 6,051 function slots retained and all 189,088
protected Game-data bytes across 720 owners unchanged. The changes comprise
the restored root, typed submit placeholder, two symbol-size updates and two
adjacent symbol/string-table pair rotations. The rotations account for exactly
28 metadata bytes and preserve every named definition. All 2198
frozen inputs pass the explicit task plan. Existing duplicate
`generated_12D630` recipe and caller warnings remain; the target adds none.

Production ELF SHA-256: `54f26fb2e102dd9717fde68acaf821f9ceaf2847a93ded129fe42ccb1aafbf7e`.

Graphify receives a scoped AST merge preserving old IDs and qualification
metadata, with authoritative C definition/prototype classification. The submit
placeholder is explicitly seven raw words with zero matching credit. This is
not a full-corpus extraction. No host-port, frozen Release, ROM or save changes;
zero Claude calls and no push. Assumptions are quiet mapped/aligned ordinary
memory, valid disjoint actor/stack backing and normal o32 providers that do not
inspect unpassed private homes or code PCs. Full rendering, faults, interrupts,
hardware and gameplay acceptance remain outside these checks.

```sh
python3 -m unittest tools.tests.test_game_actor_projection_scan_15036148_match -v
python3 -m unittest tools.tests.test_game_projection_record_draw_15035fe8_match -v
python3 -m unittest tools.tests.test_game_actor_randomized_effect_150f97ec_match -v
python3 -m unittest tools.tests.test_game_list_historical_image -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue with `func_15035D6C` in the same owner: **159 words / frame 32**,
a leaf display-list renderer with a cursor, descriptor and RGB arguments.
The read-only assembly classification identifies record-byte filters and
descriptor-controlled alpha, masks and display lists, including dynamic
count reloads. Its sole aligned JAL is ROM `0x5ED64` in `func_150311C4`
(`asm/5D2C0.s`), whose C body is still a placeholder. The original caller
passes the fifth argument in its delay slot and consumes the returned cursor.
Full caller/SDK-macro/source qualification, including the mask-shift domain,
is still needed after freezing the next bank.
Keep the 345-word `func_15035808` body unfinished until it is actually recovered.
