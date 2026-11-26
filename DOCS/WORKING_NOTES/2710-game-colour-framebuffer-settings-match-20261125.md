# Colour-framebuffer settings match - 2026-11-25

`func_151600D8` replaces its zero-return placeholder in
`conker/src/game/generated_18D250.c`. All **103 words / 412 bytes**, the
**48-byte frame**, and **33 relocation positions emit directly from C**.
There are **zero guards, insertions, omissions, alignment words or compiler
profile changes**. VA `0x151600D8..0x15160274`; ROM `0x18D588..0x18D724`.

Production: **4,689 / 5,528 (84.82%) total**, **4,016 / 4,855 (82.72%) Game**,
Init 492/492 and Debugger 181/181; zero address drift, 839 still different.
One new match, no additional parent/provider matching credit. **10 more
verified matches reach 85%.** Conversion rows and denominators are unchanged.

The routine accepts one owner pointer and returns signed 32-bit status 1. It reads
five settings through the existing seven-argument configuration helper:
`pos s`, `pos t`, `size s`, `size t`, and `pixelation`. These names and the
original file `../Effects/ColourFrameBuffer/colourframebuffer.c` are present
in the retail data, not inferred from generic offsets. The first four
signed results convert to float and multiply by their individually bound
external coefficients before stores at owner+0x18/0x1C/0x20/0x24. The fifth
result is stored as an unscaled integer at owner+0x28.

Indices are 0..4. The first two ranges are -2000..2000 with default 0, the next
two are 0..2000 with default 500, and pixelation is 0..65536 with default 65536.
Original source lines are 452, 457, 462, 467, 473. All five label/file pointer
pairs and four coefficient symbols remain distinct. The four floats at
D800A6674/78/7C/80 are all bits `0x3A83126F` (approximately 0.001), but their
bindings are not merged. The complete 0x150-byte original data region at
ROM 24B000 agrees with the source ASM, ROM and frozen/live linked ELF.

The first complete candidate had 101 words and retained the unadjusted owner
in S1. Capturing the first helper result explicitly produced 102 words.
A genuine named settings pointer recovers all 103 original words, including
the borrowed owner argument home and the post-first-call S1 output-pointer
lifetime. The C counter's increments reproduce indices 0/1 and the saved-S0
2/3/4 sequence. No dummy storage, volatile qualifiers, profile changes or
instruction rewriting were used. Saved S0/S1/RA occupy SP24/SP28/SP2C;
owner uses the incoming home at SP30. The three stack arguments occupy
SP10/SP14/SP18. Five helper calls and the final return remain explicit.

The existing `func_151422DC` is a seven-word, frame-free routine at
ROM 16F78C..16F7A8. It stores four register argument homes and returns the
fifth argument from SP10. Complete literal bytes agree with frozen/live
ELF; source `game_16EE20.c` returns arg4 through seven signed 32-bit parameters.
There is no standalone original ASM file for this helper. Literal bytes,
disassembly, source and argument widths are pinned without inventing one.
The actual seven-word helper is executed in guest tests and its unchanged
C body is compiled in Native32 tests. No new helper matching credit.

An aligned whole-ROM scan finds one target literal at ROM 22FB90 and no direct
J/JAL patterns. The source labels an eight-byte span at 8008B0D0 containing
this target and 150CE200; the following 8008B0D8 has its own three-entry span.
This qualification covers selected index 0 and the signed -1 skip, without
claiming arbitrary computed-call bounds or converting the other entry.

The original status consumer 1515FFEC is 41 words/frame32 and already
byte-exact. It retains the owner in A0 at JALR 15160058 and treats a zero
return as expiration at 15160064..6C. Its current C had omitted the owner
argument in the table call. Passing `arg0` explicitly repairs the selected
C call contract while preserving every parent word and binding. The owner's
named header fields (flags 0xE, signed selector 0xF, signed 16-bit remaining ticks
0x12) come from this consumer and give the native tests real typed objects.
The partial view ends after the 20-byte settings block; it is not asserted
to be the complete original allocation type.

Guest execution passes **2304 cases per stream across five identical
instruction streams**, visiting all 103 words. Complete machine/memory,
48-byte frame, borrowed argument home, saved ABI, return, all seven
arguments, label/file/line observations, ordered signed 32-bit conversion/MUL
operands and modeled FCSR agree with an independent reference. It includes
**256 actual-helper connections** and **2048 opaque-contract cases** per
stream, four rounding modes, INT32 boundaries, coefficient/output aliases,
stack owner storage and provider mutations. **89 fault-prefix quintuples**
agree, including actual helper instructions. Five complete instruction
controls reject. The arithmetic model is finite and bounded; this is not
an N64 hardware or portable C fault-semantics claim.

The complete original parent executes **3840 cases per stream**, with
**1600 connected children per stream**, across original/direct leaves.
Child memory/frame/argument/FP/status references agree; lifetime narrowing,
skip and expiration paths agree. The authentic child returns 1, making the
parent's 1516006C word unreachable until two supported controls force the
wrong zero-result decision and reach the opaque expiration helper.
The other callback-table entry remains outside this recovery's execution
claim. Parent source/ABI repair earns no extra function match.

Native32 executes the actual recovered C, repaired original C parent and
original default-provider C body across **three translation units**.
**4096 cases at each of O0/O2/O3** pass strict aliasing, UBSan traps, LTO type
checks and strict FP flags. Real typed headers/settings arenas retain all
bytes/canaries, metadata argument bits, provider snapshots, globals, return
and MXCSR. Actual default behavior and an additional opaque contract cover
integer limits, coefficient/output mutations, four rounding modes and
finite/subnormal coefficients. All **eight wrong variants complete with
comparison 42**, including the parent zero-test and an early cached scale.
Signals/traps do not count. Arbitrary address aliases and private N64
argument homes belong to the guest model, not native allocation claims.

Both complete padders preserve all five raw/padded neighbors, literal pools
and exports (zero interior labels). The entire guard file remains byte for
byte unchanged. Actual Make uses three commands with zero diagnostics and
no GLOBAL_ASM/profile change. An independent reference uses frozen old C
plus original target ASM. Reference, literal prediction, actual Make link
and production ELF agree: **730 changed bytes, zero exclusions**. Closed
symbol/string metadata accounting explains changes outside the target slot.
All 189088 protected Game data bytes/720 owners, unrelated bodies, addresses,
extents and conversion rows remain fixed. Boundary checks expose 206 word
and 66 binding corruptions, with 20 GNU links/100 guest rebases including the
actual default helper and all distinct metadata/coefficient bindings.
Oversized generic output visibly overflows; generated padding rejects it.

Selected source SHA256 `9cc7e20f76d1f1b8eda4d291b732a4b6ecc792a5f2f1967ac98d2d3c512aae06`.
Padded owner SHA256 `0a9f225444ce0b836a15e6b7fe26dd6249dc5806cbca0d0b51d5673b49997622`.
Production ELF SHA256 `9c880ee1c25a9b7eec751296fc67dc6c58ddf7498827be314c3d60312b4da2e4`.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 139.584 s | 5 fresh / 0 reused |
| preinstall-sibling | 94.335 s | 5 fresh / 0 reused |
| installed-primary | 122.927 s | 5 fresh / 0 reused |
| installed-sibling | 116.932 s | 5 fresh / 0 reused |

All 20 final tests are fresh. The isolated second copy has
2202 immutable dependency links and nine
independent task copies; freeze 3875 inputs /
2800 copies. Task/import/data/profile/artifact fingerprints
agree, including the native header/harness/actual provider and derived
helper/parent fixtures. Shared tools-check passes. The real dirty tools
sibling is preserved. The initial private image check was explicitly reused
after naming the genuine header fields only because the actual Make's
entire padded owner remained identical; final suite image checks are fresh.
Helper bytes and parent ASM are regenerated from pinned inputs before tests.

Baseline consumer `ed14e21222e0aaf51e7cfd274fb3520485965c9d`.
Tools commit `9b45dd89760963b0d6815646c9ab11d763fb36ee`.
Receipts: `conker/build/game-colour-framebuffer-settings-151600d8-private`.
Read-only sibling applicability finds the historical generated target is an
empty stub. No active host transfer, build, launch, Release change, push,
hardware or gameplay acceptance. This routine used zero Claude calls and
no subagents. Scoped graph retention audits all six definitions, preserves
the parent's prior qualification while recording explicit owner forwarding,
and retains old IDs/proof metadata after actual hook writers terminate.
Root README receives aggregate/date rows only. The 85% goal remains active.
