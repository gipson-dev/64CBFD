# Trail record updater match - 2026-11-25

`func_151B77F4` replaces the zero-return placeholder in
`conker/src/game/generated_1E37D0.c`. All **105 words / 420 bytes** and the
**72-byte frame** match retail after **11 checked independent scheduling
guards**; **94 words emit directly**. All five relocation positions match.
No insertions, omissions, padding, frame translation or profile changes.
VA `0x151B77F4..0x151B7998`; ROM `0x1E4CA4..0x1E4E48`.

Production: **4,687 / 5,528 (84.79%) total**, **4,014 / 4,855 (82.68%) Game**,
Init 492/492, Debugger 181/181, zero drift and 841 still different. One new
match; no additional matching credit for the already exact callbacks,
parent, producer or length helper. **12 more verified matches reach 85%.**
Conversion rows and denominators remain unchanged.

The signed32 status callback captures owner+0x94's record table and
owner+0x98's auxiliary data before the signed global tick gate. Inactive
updates return1. Active updates save the original position and call
`D_8008FB90[aux->callback](owner, &owner->position)`. Failure returns0.
Success copies the updated position to the captured auxiliary object's
post-callback attachment, computes three ordered coordinate differences,
and calls the existing length helper. It then reloads the position and
signed head and writes one 20-byte trail record through the captured table:
position, returned float distance, and opacity 255. Three retained bytes
remain untouched. Head/count/tail use signed byte reloads and narrow stores;
capacity is unsigned. A head/tail collision advances tail and removes the
extra count. Names describe observed fields, not a complete original type.

The callback table's two actual entries are 151B7678 and 151B76CC. Their
originals, ROM and frozen/live linked bodies agree (21 and74 words).
Both now declare the same compatible `s32(void *, void *)` function type
and access shared typed owner/auxiliary views. Entry0 validates its linked
actor and identity and writes three coordinates. Entry1 transforms the
linked source through its scaled matrix. Their emitted code, bindings,
existing qualification and matching credit are unchanged. Residual A2 in
the target is not a third formal argument. No function-pointer casts are
used to manufacture compatibility.

Producer 151B7328 narrows the callback selector to one byte and copies the
12-byte auxiliary payload. The two original direct producers 1506AC0C and
150B0094 supply selectors 0 and 1. Complete originals and provider/table
bindings are pinned. Length helper 15143E64's 12 words agree with ROM and
the linked ELF: three squared components, two additions andsqrt.s, returning
F0. Its standalone ASM file is absent; literal bytes and disassembly are
retained rather than claiming a nonexistent source. These producer/helper
checks are not new conversions or full gameplay acceptance.

An aligned whole-ROM census finds one target literal at ROM 22ED34,
VA 8008A274, and no direct J/JAL patterns. The already exact original parent
15147740 (100 words/frame32) reads unsigned actor.byte30, uses selector 14
in the 18-entry 8008A23C table, and calls at 15147820. Its zero-result test
marks expiration. This is a measured census, not proof of every possible
computed indirect call.

The complete original parent executes **2304 cases per stream** through
original/raw child streams, including **480 connected children per stream**.
Each child is checked against the independent full-memory/frame72/ordered
FP/provider/status model. Lifetime, invalid unsigned selector, skip and
success/failure expiration paths agree. First dispatch is zero-skipped;
third dispatch is disabled or uses the signed -1 skip. The expiration helper
remains opaque. Three supported controls complete and change the expiration
decision. No complete semantic recovery of unrelated dispatches is claimed.

The first semantic candidate used 105 words but an 80-byte frame. One bounded
Claude Pro packet review was attempted and completed, with tools=[] and
MCP=[], zero tool uses. Packet SHA256 `b043e3dcc8a997045fadd8a6b9691e76e0e4fed4f7bcf06ac65c62baf848e43b`.
Pointer declaration order partly improved bindings/scheduling; reversing
vector declarations did not improve the match. The accepted diagnostic
direction used the repository's existing mdebug parser, without unverified
suggested compiler flags. It exposed a reserved named-position local apart
from the compiler's real spill. Removing that redundant local recovers the
authentic72-byte frame. Original integer equality operand order removes one
remaining branch-word difference. No dummy storage, volatile qualifiers,
arithmetic reassociation or extra review call was needed.

The remaining closed integer window `[0xEC,0x11C)` has 12 words, 11 guarded.
Structural symbolic expression identity proves equality of all 32 GPRs and
the entire functional byte memory for arbitrary starting registers/memory,
including overlapping position, records and saved pointers. FPR/HI/LO/FCSR
are untouched by its supported integer instructions. Every outside word and
binding is identical. Six supported negative controls produce symbolic
inequality and concrete witnesses. This is a structural expression proof,
not SMT/hardware, and covers **nonfaulting ordinary RAM**. Raw fault-prefix
order equivalence is explicitly not claimed.

Guest execution passes **1928 cases per stream across five streams**,
visits all 105 words, and compares full final machine state and an independent
ordered reference. Coverage includes every signed head/count byte, unsigned
capacity boundaries, callback failure, attachment and record/source overlap,
provider mutations, captured pointer lifetimes, post-provider reloads,
caller-stack storage and all four rounding modes. **192 fault-prefix
quadruples** compare only the four literal-identical normalized streams.
Four complete instruction controls reject. The existing finite FP model
and opaque callbacks/length contract are not hardware or full-provider proof.

Native32 executes the actual selected target and **both actual callback C
bodies**, with the compatible callback table defined across three translation
units. **4096 cases at each of O0/O2/O3** pass strict aliasing, UBSan traps,
LTO type checks and strict FP flags. Valid typed owner, auxiliary, link,
actor, matrix-source, record and attachment arenas retain all bytes/canaries,
pointer fields, provider snapshots, integer return and MXCSR. Arbitrary
addresses and out-of-allocation signed indices are guest-only. **Seven wrong
C variants complete with comparison42**; no signal/trap counts as a control.

Both complete padders retain all 16 raw/padded neighbors, pools and exports
(zero interior retail labels). The three-command actual Make recipe has
zero diagnostics and no GLOBAL_ASM/profile change. The independent image
reference uses frozen old C plus original target ASM. Actual Make, independent
reference/prediction and production ELF agree with **331 changed bytes,
zero exclusions**. All 189088 protected Game data bytes/720 owners, unrelated
bodies/addresses/extents, old guard-prefix bytes and conversion rows remain
fixed. Boundary checks reject 22 guard corruptions and expose 188 unguarded
word and 10 binding corruptions; 20 GNU links/100 guest runs cover high rebases
and low-half carry boundaries. Both oversized probes reject.

Selected owner SHA256 `3532938c989287117e34401674d818e958afee06af435c2c2c80e2790272cdd4`.
Padded owner SHA256 `e9ada42af48179dd999401c58cb796d7d1964cb96bcd7fb49d00407005ac1629`.
Production ELF SHA256 `a132eab9219882f34d4da6c229f6fa15a438effede48bc5c1f3d91f157458451`.

| Tools execution | Seconds | Qualification |
| --- | --- | --- |
| preinstall-primary | 201.252 s | 6 fresh / 0 reused |
| preinstall-sibling | 121.656 s | 6 fresh / 0 reused |
| installed-primary | 96.811 s | 6 fresh / 0 reused |
| installed-sibling | 113.502 s | 6 fresh / 0 reused |

All 24 final tests are fresh. The isolated second copy contains
2183 immutable dependency links and 10
independent task copies. Freeze: 3850 inputs /
2774 copies. Task/import/data/profile/artifact fingerprints
agree across copies; shared tools-check passes. The real dirty tools sibling
is preserved. Initial fixture corrections moved an accidentally overlapping
auxiliary test buffer, made rebased entry selection dynamic and corrected
the caller-table ROM start; final suites cover these corrections. Negative
controls must complete and report a comparison failure, not a compiler
warning or trap.

Baseline consumer `4278eaf28eaf8985a763de2874210d2dec094d42`.
Tools commit `2cf388e9234c60fe0e815e31c569b84ca78419a1`.
Receipts: `conker/build/game-trail-record-update-151b77f4-private`.
The known historical host generated target remains an empty stub; read-only
applicability evidence is separate. No host code transfer, build, launch,
Release change, push, hardware or gameplay acceptance is claimed. Scoped
Graphify refresh retains old IDs and proof metadata, audits all 17 actual
owner definitions including its K&R definition, and observes actual hook
writers terminate before immutable banking. The 85% goal remains active.
