# View-aligned billboard quad recovered and byte matched

Date: 2026-11-07. Continues [Note 2166](2166-game-combiner-state-emitter-match-20261107.md)
from consumer `2b32c052a1775d5ddcb3b290b8809a17f8c8fd56` and tools
`30ce1a5289091193b2a1b17e27d8b6188fc51ceb`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered routine and wrapper contract

`Vtx *func_1513EAD8(u8 *actor, u8 rotated, s16 view)` replaces the false
s32 zero-return placeholder in `conker/src/game_169510.c`. Its complete
**183 words / 732 bytes**, **104-byte frame**, private homes, saved S0/RA
lifetimes and branches match retail after **three expected-word guards**
commute the operands of independent single-precision multiplies. VA:
0x1513EAD8..0x1513EDB4; ROM: 0x16BF88..0x16C264. The existing O2/g3,
MIPS2/O32 compiler profile is unchanged.

1. Query `func_151D5D60(actor + 0x100, view, 0x40, &cursor, &fresh)`.
   Capture the first cursor separately and return null if no buffer exists.
2. If fresh, copy the 64-byte template at actor+0xC0 to both halves of the
   view's buffer. Capture the slot address/template across the calls, but
   reload the slot's pointer for the second copy.
3. Form forward/side offsets from D_800DD1D8[view], D_800DD1E8[view] and
   actor width +0x2C. Set lower = scaleY(+0x50) * height(+0x30), and
   upper = height - lower. Clear all four Vtx flags before reading centers.
4. Build signed 16-bit corner components from centers +0x34/+0x38/+0x3C,
   using float32 operations followed by truncation to s32 then narrowing.
   The normal order is P0,P1,P2,P3; a nonzero rotated byte cycles it to
   P1,P2,P3,P0. This preserves winding. Reload the escaped output cursor
   between stores and return the separately captured first pointer.

The source keeps a separately named `upper` and inline memcpy inputs.
Together with the local declaration order, these recover the original
frame, private spill layout, FPR roles and scheduling. Earlier 183-word
screens had different homes or FPR roles despite equal mismatch counts;
those remain uncredited. No frame/padding/NOP or register-cycle guards are
needed. Raw target SHA-256:
`9a30934a81979a84cdb56c30eaa78e260c8831859e96830ddc3583daef3f1b49`.

The three guards are at byte offsets 0x0CC, 0x0D8 and 0x0E4. Each swaps
only fs/ft fields of `mul.s`; the full raw hash and all seven bindings must
match first. Bindings are byte 44 (backend JAL), 100/124 (memcpy JALs),
136/168 (forward-array HI/LO), and 172/184 (side-array HI/LO).

Both `func_1513EDB4` and `func_1513EDE4` now explicitly return
`Vtx *` from `(u8 *actor, s16 view)` in their definitions and the shared
functions.h. They pass rotated 0 and 1 respectively. Each wrapper retains
all **12 original words** directly; both were already exact, so neither
earns new credit. The old void declarations described a machine V0
pass-through without a valid native C pointer-return contract.

## Original calls, helpers and renderer connection

The complete aligned-ROM census finds exactly two direct leaf JALs, ROM
0x16C27C/0x16C2AC, both in these wrappers; no entry/interior pointers name
the leaf. The wrapper pointers are renderer table slots **34/35** at ROM
0x22E964/0x22E968. Only the 39-entry renderer prefix is a function table;
following graphics words are excluded from that classification.
The second wrapper also has a direct retail JAL at ROM 0x12B064; the
focused execution connection below uses the full table consumer.

The full **295-word func_1513DB00** calls the selected wrapper with actor
A0 and signed view A1 at 0x1513DC24. It consumes V0 as the returned vertex
pointer at 0x1513DC30, including the null gate, and saves it for subsequent
graphics commands. **That renderer remains a production stub.** Its
original execution is compared with a counterpart using the independent
billboard provider through both original wrappers. Other renderer services
remain bounded; no renderer restoration or live rendering claim is made.

The complete original **52-word buffer backend** and **11-word memcpy**
are compared with ROM and the production predecessor, where both are
already exact. Both execute in selected connected cases. Allocation stays
bounded; the only unexecuted backend word supplies a fallback fresh-byte
pointer, while this caller always provides its real nonzero byte address.

## Focused validation

Seven checks pass before and after installation in both tools configurations:

* **931 guest cases per body** compare retail, raw compiler and
  normalized output against an independent ordered float/copy/coordinate
  model. All 183 target words execute. Cover null and reused/fresh buffers,
  signed views and upper argument bits, both vertex orders, pivot values,
  copied-slot and escaped-cursor mutations, captured-return home mutation,
  explicit actor/template/private-points aliases and exceptional casts.
  A null-buffer fixture leaves all actor/output/direction memory unmapped.
* **292 original renderer cases per body**, with
  **128 actual leaf calls per body**, exercise both original wrappers
  against an independent leaf provider. All 24 wrapper words and 293 of
  295 renderer words execute. Words 115/146 are duplicate default slots
  skipped by the preceding explicit branches; their opcodes/offsets are
  checked. Extra hidden-buffer cases cover renderer words 24..34.
* **823 fired access cuts**, including **148 delay cuts**, compare full memory,
  GPR/FPR/HI/LO, PC, delay context and access prefixes for normalized versus
  retail words. Cover saved-register lifetimes, original helpers, incoming
  homes, escaped cursor, captured first pointer and stack aliases.
* SDK native32 O0/O2/O3 each pass **1,986 cases** using Vtx16 and pointer32,
  typed direct leaf calls plus typed callbacks at slots 34/35. Check ordered
  effects, helper arguments/call counts, copy-slot changes, cursor redirects
  and pointer returns with trapping UBSan. Ten compiled semantic negatives
  reject with exit 1, including a wrapper that discards the return pointer.
* All 183 raw-word mutations, seven binding mutations, history/pool/options
  corruptions and seven whole-image corruptions reject. Two independent
  GNU links preserve all seven relocations, including signed-LO carry.

Native fixtures use disjoint valid objects, finite values with representable
s32 casts, and round-to-nearest without FTZ/DAZ. Stack aliases/private homes
and exceptional casts are guest-only evidence. The float oracle canonicalizes
NaNs and does not emulate FCSR, NaN payload propagation, hardware exceptions
or gameplay. Raw public-model equivalence and normalized full private-state
identity are recorded separately.

A single bounded, packet-only Claude layout review was used during the
private source search. The suggested declaration order was tested but was
not sufficient; inline memcpy inputs and the separately named upper value
provided the decisive evidence. Its speculative frame/void-wrapper advice
was not adopted. Codex independently implemented and validated the result;
review prose is not matching evidence and no second writer was used.

## Shared-header rebuild, production and aggregate progress

Freeze **571 inputs**, including all 199 direct C consumers of functions.h
and their **200 actual objects**. Ordinary Make header dependencies covered
only 25 compiler commands. Force each source through its existing recipe:
**206 compiler invocations**, preserving the mixed retail profiles. Audit
every resulting object, every named function/body/binding, loaded section,
pool and register/options metadata. The owner changes only this leaf;
all **58 neighbors**, including the typed wrappers, remain exact to the
predecessor in both raw and padded forms.

The other 199 objects preserve all loaded sections/relocations and all
sections except explicitly reported nonloaded ECOFF `.mdebug` changes.
Across all 200 objects, **194 are byte-identical** and
**5 have only such debug changes**; the separate target owner is
qualified against its predicted padded object. The linked ELF has no
`.mdebug`. The audit records each changed debug section's before/after size
and hash, with no linked-image exclusions. Target diagnostics remain 43
inherited warnings, with no new target warning; the full forced build emits
401 C warnings across all profiles. Only the target's
paired diagnostic comparison is claimed as a fresh warning comparison.

Actual Make equals the independently predicted complete ELF byte for byte.
Exactly **537 bytes change**: 535 in the target's 732-byte Game slot and
two bytes changing its symbol size from 24 to 732. All other symbol/string
metadata remains literal, with zero reorderings and **zero exclusions**.
All **6,052 function addresses** and **189,088 protected Game bytes across
720 owners** remain fixed. Guard history is preserved with exactly three
new rows. Makefile and conversion progress CSV remain unchanged.

Compilation/linking pass. `make all` retains expected checksum exit 2 and
the inherited duplicate generated_12D630 recipe warning; this is not a
whole-ROM checksum match. Both tools copies pass fresh shared smoke checks.
Three unchanged shared regressions per copy are explicitly reused only after
exact fingerprints. The new-module overlay and recorded read-only fallback
preserve all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,237 / 5,512 | 76.87% | 0 | 1275 |
| Game | 3,564 / 4,839 | 73.65% | 0 | 1275 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**173 more exact functions** remain to 4,410 / 80%. README gets aggregate
rows only. Four concise index leads preserve history. Refresh Graphify with
scoped, fail-closed legacy-node retention, then commit tools before consumer
source/header/guards/docs/pin. Verify a fresh hook terminal, clean task trees
and stable production artifacts; no fresh full-corpus graph claim is made.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `33974171ba305eb63e384923013b60442a25478f0fcde6a7e6bd709745825108` |
| Production binary | `dd79cfa4cbb5c75681207bca2e6c2134772887ba62435c65857975f25d517652` |
| Padded owner | `8ba57db7ff66d5f8bac54170973f5e884eee5d76a664c673bc7ed45f81d5562c` |
| Shared functions header | `fbdadeaa1fdbded0d554245fd3f20b3fbd9d68e05bccf29e12d5eaefe6e0096a` |
| Guard manifest | `17a99bdbcac743a6a0830994c31ffde2a4c2f5aee472086617feab423a238279` |

Ignored receipts: `conker/build/game-billboard-quad-1513EAD8-match/`;
source/layout screens and advisory packet: adjacent private directory.

Next: **func_1513EE14**, the related 192-word routine at
VA 0x1513EE14..0x1513F114, ROM 0x16C2C4..0x16C5C4. Its retained body
queries the vertex buffer, builds an orientation/translation matrix,
transforms four corners and emits their coordinates/flags. Inspect its
complete caller and source shape independently; this note gives it no
credit. Continue the active 80% goal with all private inputs, saves,
unrelated sibling work and frozen host Release preserved.
