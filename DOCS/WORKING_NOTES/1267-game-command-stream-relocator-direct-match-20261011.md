# Game Command-Stream Relocator Direct Match

Date: 2026-10-11. Complete func_1503D368, VA 0x1503D368..0x1503D438,
ROM 0x6A818..0x6A8E8, 52 words / 208 bytes. Owner:
conker/src/game/generated_6A3D0.c. All 52 words emit directly from semantic
C, with no new guards, padding substitutions or compiler-profile changes.
The wider Game matching goal remains active.

## Baseline And Recovery

Consumer 556103c5179df47bf1d9baf3c20c511caf6e6a0f, mounted tools
f54c9fbff92e7d7e6c5d81e1ea60bdd968488f37. Both active checkouts were clean.
[Note 1266](1266-game-main-resource-loader-guarded-match-20261011.md)
banked the complete parent loader's 274-word guarded match. Its two actual
calls to this child ignore the result and pass a command address plus an
unsigned relocation base. The child's old zero-return placeholder did not
perform the retail command scan.

Recover the void (Gfx *, u32) contract and use the actual SDK's eight-byte
Gfx records. The opening NULL gate and signed opcode -0x21 / 0xDF terminator
are preserved. Opcode 1 relocates the second word; opcode -0x24 / 0xDC does
so only when unsigned subtype byte +3 is 0x0E. All other opcodes are skipped.
The indexed cursor retains the stable original base, increments by eight
bytes and reloads subsequent opcodes and conditional subtypes live.

The existing nine-word func_1503D438 leaf remains directly byte-exact. It
preserves zero and nonzero-segment values; other words add the unsigned base
with 32-bit wrap. Calling it does not make the command scan return a value.
Type both real callers explicitly without changing their instructions.

The owner's existing retail profile is -O2 -g3 -Wo,-loopunroll,0. A complete
34-form diagnostic sweep succeeds without compiler diagnostics or data pools.
Four vertex-case-first switch forms match all 52 words; some candidates have
identical source bodies, so 34 is not a unique-body claim. Pointer-cursor and
if-chain forms do not match. Only the selected complete switch body is
installed and fully qualified. It naturally restores the original 0x38
frame, saved S0..S6 lifetimes, index updates and branch delays.

The explicit u32 * cast on the SDK unsigned-long word address avoids a
compiler pointer-type diagnostic; both words are 32-bit in this target ABI.
Signed-char byte access is deliberate. This is not a 64-bit host-port claim.

## Qualification

New authored tools are experiments/game_command_stream_relocator_candidates.py
and tests/test_game_command_stream_relocator_match.py. They reuse the existing
IDO compiler, MIPS oracle, native32, owner, pool and padding helpers rather
than introduce another engine. Receipts live under ignored
conker/build/game-command-stream-relocator-match-test/.

- Eleven final pre-install tests pass in 18.838 seconds.
- Original, raw selected and actual-padded forms agree on all 52 words.
  The guest public-memory/access/call reference passes 1,350 cases across
  NULL, immediate terminator, every signed opcode, every unsigned subtype,
  payload/base boundaries and two stack phases. All 51 reachable words are
  exercised. The duplicate subtype load at +0x78 is statically unreachable.
- Ten bounded live-future-record mutation/clobber cases preserve reloads
  and argument/base lifetimes. These hooks are not actual leaf behavior.
- Nine independent links pass 324 cases across three function/leaf rebases;
  actual original, raw and padded forms remain byte-exact.
- Every private-stack/public/actual-leaf access ordinal fires: 214
  original/raw/padded fault triples agree on complete partial memory,
  access/call events and registers. This is a guest fault-model result.
- Six freshly compiled semantic mutations are effective negative controls;
  three stale owner/interface installs are rejected.
- Both complete owner compilations have zero diagnostics. All 14 neighbors,
  including the typed parent, preserve bytes, extents, relocations and pools.
  Both real padders agree and change only the child slot.
- Native32 O2 and O0 execute 65,754 cases each, including all 65,536
  opcode/subtype pairs, payload/base/mutation cases, NULL and immediate DF.
  Every modeled memory byte and call argument agrees with an independent
  reference. An altered vertex opcode fails. The established native fixture
  uses -fno-strict-aliasing and checks Gfx size 8 / second-word offset 4.
- The actual 104/274/52/56/9/194-word parent/main/command/extras/relocator/
  buffer chain passes 768 cases. The new actual command body replaces its
  former helper hook and reaches 49 child words within that chain. Deeper
  allocator/copy/free/auxiliary/hardware calls remain bounded.
- Four changed source/prototype/caller/owner inputs and two changed child
  word/extent inputs are rejected by the historical-audit projection. An
  unrelated ELF byte survives projection so the older whole-ELF audit still
  rejects it. Historical baseline files are not refreshed.

Fixture development corrected an omitted native forward declaration and
included NULL-path visits in the coverage union. An early SDK field argument
needed its explicit u32 * cast. These were isolated fixture/candidate issues,
not production defects. The final selected tests pass before installation.

After installation, 38 fresh tests pass in 122.134 seconds: all eleven child
tests, all fifteen guarded-parent tests, ten shape/whole-ELF checks across
the five earlier loader stages, and two historical status-join shape/audit
tests. Those 31 historical candidates are recompiled, but their full semantic
matrix is not rerun in this checkpoint. Unchanged earlier semantic receipts
from Note 1266 are explicitly reused, not counted as fresh tests.

## Historical Audit Boundary

The shared audit helper accepts only the exact selected child body, typed
prototype and two exact caller casts. Reversing those edits must reproduce
the frozen parent source SHA-256
f43fa661893aadea680107f8ebe446bdad763489b5558996c8a906802beca058.
It independently requires all 52 linked child words to equal retail and the
208-byte symbol extent before projecting only that slot/extent onto each
trusted historical ELF. No other current bytes are discarded or admitted.

Earlier loader audits therefore report on this explicitly projected view,
not a claim that the literal current owner source/ELF is unchanged. Their
immutable baselines, raw candidates, references, controls and guard prefix
remain intact. The new child's whole-ELF audit measures the real delta.
The parent still has 252 direct words plus 22 guards; this child match does
not eliminate those parent guards.

## Whole-ELF Delta And Progress

Installed source SHA-256:
0f8594be47c2082c073901586c8a3a7ee74b6a4b70588de92729e61d3ba0c52d.
Installed ELF SHA-256:
9bc1f33cba446d25b6852a2962cc5ee7f9309f4af1d9ce3b9e957f300a84f561.

Exactly 159 ELF bytes change: 158 in the target slot and one symbol-size byte
as its extent changes from 12 to 208. Every other ELF byte, metadata byte,
symbol name/value/extent and data byte remains identical. All 189,088
protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Layout, rodata source and symbol/auto-assignment inputs retain their hashes.
The guard manifest is byte-identical, SHA-256
aa80c31e9eef9326b6a64100be34df67037a4d3dff3dfb76f89a15d054e0f6eb.
Conversion CSV is byte-identical, SHA-256
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.
The required ELF/progress rebuild exits 0 with the known duplicate
generated_12D630 recipe warning. No new target compiler diagnostics.

Fresh `make -C conker match-progress NON_MATCHING=1` exits 0:

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,464 / 5,495 (63.04%) | 0 | 2,031 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,791 / 4,822 (57.88%) | 0 | 2,031 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Conversion and converted-byte metrics stay fixed.
Root README changes only its two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools
349aa214c1621a556de1d172f2086a51952034d9 is committed first; the consumer
source/docs/aggregate rows pin that exact tools checkpoint. No push.
Consumer/mounted/older WSL project-tools checks pass, as does native py_compile
for all ten changed tools and the two new-file copies.

Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 25
protected existing fingerprints stay unchanged. Its dirty entries 302 -> 304
reflect only two absent-path copies, identical to their mounted counterparts.
Existing older audits are deliberately not overwritten, committed or reset.
Native Graphify refresh exits 1 after refusing shrink 39,821 -> 18,040 nodes;
19,398 nodes from 2,972 still-existing excluded files are retained. The known
skill/package-version and devcontainer zero-node warnings remain. No force,
purge or install. The consumer hook is checked separately: require fresh log
length/UTC, a fresh Rebuilt record and zero actual Graphify/Python workers;
do not mistake the old log for completion.
No OGL/Release/save/editor/private-input changes; Release remains frozen.
Guest models and native32 do not prove real heap/hardware/rendering/gameplay
or portable 64-bit host behavior.

Next connected recovery: complete func_1503D984, VA
0x1503D984..0x1503DA3C, ROM 0x6AE34..0x6AEEC, 46 words / 184 bytes,
same owner, still a zero-return placeholder. Inspect its real void/identity
contract, first command-stream table entry, signed opcode extracted from
32-bit command loads, DF termination, opcode 5/6/high-nibble weights,
eight-byte live cursor and halfword publication to D_800C5918[identity].
Recover and qualify the full body before replacing that loader helper model.
Parent guard elimination and wider runtime acceptance remain separate tasks.
