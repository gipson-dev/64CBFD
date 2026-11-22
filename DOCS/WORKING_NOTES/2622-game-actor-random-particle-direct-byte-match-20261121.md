# 2622 - Actor random particle direct byte match

Date: 2026-11-21. The total 85% matching goal remains active.

`func_150DE12C` now emits all 94 retail words directly from semantic C, with
**zero guards, insertions or omissions**. The fresh production recount is
**4,605 / 5,528 (83.30%) total** and **3,932 / 4,855 (80.99%) Game**, with
zero address drift and 923 different converted functions. Init remains
492/492 and Debugger 181/181. **94 more matches** reach 85% at this denominator.

## Recovered source and ABI

Source is `conker/src/game/generated_108E90.c`. The preserved original starts
at `conker/asm/108E90.s:2667`, VA `0x150DE12C..0x150DE2A4`, ROM
`0x10B5DC..0x10B754`. Its frame is 144 bytes, S0 at SP+0x40 and RA at
SP+0x44. All six relocation sites are R_MIPS_26 calls. Eleven neighboring
functions, pools and diagnostic rows remain unchanged under existing O2/g3.

The first complete draft matched. It reuses the already recovered descriptor
and ABI of the adjacent, retail-exact `func_150DDFAC`. The smaller variant
changes range multiplier 70->10, kinds 29/30->27/28, and descriptor byte 0x15
255->170. No alternative-source donor was adopted. Raw instruction SHA256 is
`c682d7027264cd522453e00a769fdd0afc579b2b9fa0a1d34643947890cadefd`.

The six arguments are actor, three previous-coordinate floats, height and a
context pointer. The previous-coordinate values are saved to their incoming
homes but not consumed. The current caller confirms their floating bit transport.
Both pointers at actor+0x98 and actor+0x94 are captured before the first random
call. The first selects the payload byte at 0x20, set to 4 after the random-float
call. The second selects 20-byte position records, indexed by signed actor byte
0x2D after all four integer random calls. Later pointer mutations must not
replace these captured bases.

The random float gives `10*x+10`; the first random integer's low bit selects
kind 27/28. Three further integer results supply a masked byte and the sum of
two low bits. The 40-byte descriptor preserves flags 17, lifetime 100, zero
words 8/C, bytes 10/11=255, bytes 12/13/14=0, byte 15=170 and resource 0x30002.
Its padding retains object-representation scope; no new initialization is
invented. `func_1513C73C` receives 14 correctly typed argument words, including
record X/Z, the fifth height argument, both identical range values, and freshly
loaded actor tags. The callback returns 1 regardless of the submitted factory's
modeled result.

## Fresh qualification

Run `python3 -m unittest tools.tests.test_game_actor_random_particle_150de12c_match -v`.
All five checks pass before and after installation in primary tools and the
isolated sibling overlay. Imports and non-Python inputs are fingerprinted.
Shared `make tools-check` passes. The actual dirty sibling and its inspected
dependency bytes are preserved. The sibling callback's existing protocols were
adapted and rerun for this target, not credited from old receipts.

1. Raw C, generic-padded, generated-padded and original instruction/relocation
   payloads agree. The pure-C natural Make recipe uses three commands. The
   independent complete-ELF prediction equals the link: **290 changed bytes,
   zero exclusions**, only the target slot and symbol size 12->376. No metadata
   permutation is needed. GameData stays exact across 189,088 bytes / 720 owners.
   The existing guard CSV and conversion rows remain byte-identical.
2. The mutating guest model runs 1,068 cases, all 256 signed-byte indices,
   pointer capture, tag reloads, both branch choices, all low-bit sum outcomes,
   byte-mask boundaries and height transport including signed zero, infinity,
   NaN payload and subnormal bit patterns. It covers 92 reachable words. The
   two masked-switch fallback words 27/28 are unreachable. Four emitted streams
   agree at all 245 sampled access-fault cuts, including complete private state.
   These cuts qualify emitted instructions rather than portable C fault behavior.
3. The original 19-word dispatcher window at 15148D80..15148DCC executes 72
   cases, using table D_8008A430 index 4, entry 8008A440 / ROM 22EF00. Its real JALR
   at 15148DB0 transports all six arguments; the delay-slot store supplies height.
   Three controls detect wrong context, wrong previous X and an omitted height
   store. Outgoing homes start with different values so the controls must fire.
   The window and full 143-word parent `func_15148BA4` are current/retail exact;
   only the 19-word window is executed by this focused caller test.
4. The original 43-word handwritten integer/float RNG pair executes 12 seed
   cases and five verified 64-bit seed transitions before modeled submission.
   All 43 helper words execute. Current integer 18-word and float 25-word extents
   are original-exact, as are the 50-word factory and adjacent 96-word sibling.
   The integer entry is audited explicitly because it is absent from the C
   retail-layout rows. Factory internals remain modeled. Sixteen independent
   GNU links across four emitted forms verify call relocations at alternate
   aligned helper addresses.
5. Native SDK32 runs 216 valid typed-object cases at each of O0/O2/O3 with
   strict aliasing and UBSan. Owner offsets, 20-byte position stride and 40-byte
   descriptor extent are asserted. Ten source controls detect incorrect range,
   base, payload value, kind, flags, position, byte mask, low-bit sum, return
   value and late payload capture. Incoming argument-home mutations remain
   guest-only; native helpers are explicit service contracts.

## Production, applicability and continuation

Production Make and the fresh recount pass. ELF SHA256 is
`e89ad4c76b89682b8038b662ce7a75d444b2882b2aad66654dc64ec483ccc573`. The prior consumer is `37bded7be1dff43c6e6ab737cf3339a806825781`;
the prior tools baseline is `2aa3e4a09a4ee08304b279d059a07c6dbfdadd20`. Tools are committed first.
There are zero advisory/model calls, and the prior Claude authentication
failure was not retried. Existing unrelated Make warnings remain recorded.
The README gets only its Total and Game aggregate row changes.

The available sibling host scene configuration/input was inspected read-only.
It consumes binary words and symbols, so this C recovery supplies no direct
source import there. No host build or Release changes were made. Full factory,
full parent, hardware and gameplay acceptance are outside these focused checks.

Continue the remaining Game census toward the full 85% objective. The
96-word func_15194408 needs explicit five-entry jump-table/pool ownership audit
and actual HeightResult71820 layout, not an invented float matrix. The private
position/camera/history candidates retain their existing handoffs and receive
no credit from this adoption.

Graph maintenance: the native update exited 1 with all
70,262 prior IDs retained. The subsequent serial scoped extraction
covers 8 C/Python files with no missing AST sources, producing
70,313 nodes / 162,919 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
