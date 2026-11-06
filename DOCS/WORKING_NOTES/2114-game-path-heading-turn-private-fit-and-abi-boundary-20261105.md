# Path heading/turn private fit and ABI boundary

Date: 2026-11-05. Continue the 80% matching goal from consumer
`e1c0182625c9a902e645abe12fd0bddf7dec99b1`, mounted tools
`478e79fcd5086a1612045e5b6ce53ce0fe529aad`, and
[Note 2113](2113-game-packed-command-coordinates-guarded-match-20261105.md).
Both checkouts started clean. No production C, guard, header, Makefile or
tools files change in this checkpoint. The candidate stays private and
**uninstalled and uncredited**.

## Current result

Target `func_15077F64`, owner `game_A28B0`, source
`conker/src/game_A28B0.c`, original
`conker/asm/nonmatchings/game_A28B0/func_15077F64.s`.
The original is **68 words / 272 bytes**, frame **0x28**,
VA `0x15077F64..0x15078074`, ROM `0xA5414..0xA5524`.

The selected complete C body is `setup-row-last.c` under
`conker/build/game-path-heading-turn-15077F64-match/`. It emits **67 raw
words**, the correct frame0x28 and the correct saved row byte at SP+0x1E.
The declaration and definition remain `void(void)`. It uses the existing
three-argument heading query and the existing typed turning-helper ABI.

A private owner fit emits all **68 original words** using **42 guarded rows**,
one inserted OR register copy and no omissions. No frame, saved-register
home or stack-byte offset is patched. All **14 symbolic bindings** are
retained, with relocation sites explicitly moved by the proposed schedule.
The existing guard CSV is preserved byte for byte as a prefix; the proposed
manifest exists only in the ignored build directory.

The fitted owner SHA-256 is
`02f3cd2b90e6a5e73b4495d1c9fbaa6c162fb3a7f2b4969dc4788f031c2abfe1`;
the proposed manifest is
`31a596ab2aed75f8e41e1119155b7381d597b7ae51ceda71eaa56b9c78854cd8`.
Neither artifact is the installed production owner/manifest.

## Recovered source and helper boundary

The callback selects a path by actor byte0x13F and an eight-byte entry by
byte0x21E. The next record's signed X/Z halfwords are compared with actor
X/Z floats through `func_1505A630(f32, f32, s32)`, with argument three zero.
The returned low16 angle is stored through the reloaded live actor pointer.
The subsequent heading reads reload that pointer again.

The circular distance is the arithmetic-shifted angle difference masked
to a byte, conditionally negated and masked again. The byte threshold is
`((u8 *)D_80099A3C)[savedRow * 10]`. Direct s16-array indexing would double
the intended byte stride. A strictly exceeded threshold copies D_800D1891
to actor byte0x250, then calls `func_15056A00(void *, u8, u8)` with the live
actor, magnitude and saved row. Global mode changes across the first helper
must not replace the saved row. Complete helper/provider behavior remains
to be qualified.

The original heading-query window is independently disassembled from its
50 retail words. It never reads A3. The A3 row temporary seen at the caller
is not evidence for a fourth C parameter. The original helper's FCSR and
conversion instructions are preserved as evidence; no full floating-point
or hardware acceptance is inferred from this static observation.

A diagnostic local s32 magnitude parameter for the turning helper reaches
68 words with17 differences but contradicts its existing u8 definition.
That is not compatible portable C merely because the in-range O32 argument
register agrees. Neither declaration nor definition is changed. Explicit
wide-parameter helper probes also fail raw identity: simple cast64 words,
addressed parameter67, addressed byte local66 with broad differences.

## Source screens and advisory reconciliation

The first typed body emits67/frame0x20/home0x1F. Meaningful float snapshots
declared before the saved row recover frame0x28; a threshold-byte declaration
before the row recovers home0x1E. The selected body reads its row after the
coordinate snapshots. Consequently all ordinary input reads occur before
the saved-byte write, preserving their values even under data/home aliases.
The separate return-address save precedes those reads.

One packet-only Claude advisory runs in safe mode with an empty built-in tool
set, strict empty MCP configuration and no session persistence. It receives
only the bounded packet, completes with exit0, and makes no checkout changes.
Packet SHA-256:
`975ba4c9b20ad6f7f713ef887eb8b4982275f4366144db6d273bae7bdd53ca58`.
Its ABI warning is independently accepted. Its suggestion to combine float
snapshots and the threshold byte is tested: that produces67/frame0x28/home0x1E.
Its claim that this also supplies word68 is rejected by the actual object.
No second advisory is used. Register hints and mode-snapshot reordering do
not supply the missing word. A byte result-angle variant truncates the
heading and is rejected regardless of instruction count.

## Symbolic and owner evidence

`prove_values.py` explores **78 original / 77 candidate symbolic states**
and **four terminal paths**. It compares branch predicates, complete
symbolic store histories, exact helper arguments and return-control/stack
expressions. Helpers are opaque providers with matching symbolic memory
effects and caller-register clobbers. This does not qualify those providers.

The initial read multiset is compared only after asserting that every input
read lies between the return-address save and saved-byte write. Those reads
commute before that second write. Subsequent memory/call events are compared
in order. Byte-mask idempotence and the zero extension of byte loads are
the explicit value simplifications. Float conversions/subtractions retain
their operand expressions; the explorer does not model IEEE flags/traps.

After masking only decoded operand-register fields, both complete instruction
multisets are identical except for **one OR copy** in retail. Every original
and candidate OR is a copy with a zero operand. No arithmetic, immediate,
frame adjustment, call target, data access or branch instruction is added
or removed by that accounting. The fit restores the copy at original offset
0x44 and applies the declared register/scheduling changes.

Five effective controls reject a frame change, saved-byte home change,
unsigned node-coordinate load, wrong state destination and reversed threshold
comparison. This is a bounded symbolic contract comparison, not a general
MIPS theorem prover. Raw fault order, dead private registers, FCSR state and
hardware equivalence are not claimed. The fitted bytes are literal retail
identity; their complete guest/native/production gates remain pending.

All **210 raw neighbors and210 padded neighbors** are unchanged. Compact
allocatable pools compare through the existing ownership-aware helper.
The padded owner has an inherited executable `.game_overflow` pool with
R_MIPS_26 relocations, which that older R32-only helper cannot parse. A
separate complete section/relocation inventory verifies literal bytes,
section metadata and named binding identities for `.MIPS.abiflags`, `.bss`,
`.data`, `.game_overflow` and `.reginfo`. No dependent section is excluded.
The rebuilt predecessor owner is byte-identical to the live production owner.

## Caller census and remaining gates

A full aligned ROM census finds no direct JAL or tail jump. The sole aligned
pointer literal is ROM `0x22B464`, callback **157** in `D_80086730`.
The retained original dispatch window is29 words at
`0x1507BD00..0x1507BD74`, SHA-256
`05ca508dd6f44cf4acfe0655ba8f037a8985944c4da1d4ed67808f385ecfb2f5`.
Its execution and return-discard behavior are still unqualified for this
target; the prior neighboring callback's evidence is not a fresh test here.

Artifacts include `screen-inputs.json` and eight immutable screen inputs,
the bounded screen scripts/results, `caller-census.json`, helper disassembly,
`symbolic-contract.json`, `proposed-guards.csv` and `private-fit.json`.
These private inputs are not a completed full qualification snapshot.

Next, promote the selected candidate and bounded proof into reusable tools
with a complete frozen-input manifest. Qualify guest/native semantics,
mutable providers, the original dispatch and helper interfaces, aliases,
fault prefixes, effective controls, independent GNU rebases and full owner
padding. Then prove the literal whole-image delta with no exclusions,
run actual production Make/recount, audit all addresses/protected data,
update documentation/Graphify and commit tools before the consumer.
Keep this function uncredited until every gate passes.

Production stays **4,184/5,512 (75.91%)**, Game **3,511/4,839 (72.56%)**,
Init492/492 and Debugger181/181, zero drift. The 80% threshold is4,410,
leaving **226 more** exact functions. README aggregate rows do not change.
Retain the eight existing separate boundaries from Note2103 and the frozen
host Release. The wider goal remains active.

The graph refresh is scoped to the five changed documentation paths. It
retains31,816 nodes from3,754 files outside the current scan corpus, retains
58,836 old IDs, and relocates three update-log IDs through unique same-label/
same-source replacements. No nodes outside changed paths are removed.
Ten IDs are added:seven note headings and the three relocated IDs. The result
is **58,846 nodes /112,607 links /5,254 communities**, SHA-256
`d7f45b9c733076af16f3a88ca1fb592ef635705ba58c0ce895b3debde21f7bbb`. The target's source node remains its unchanged placeholder;
no private fit is represented as an installed C recovery. This is a scoped
refresh, not a fresh full-corpus extraction or graph-policy/package change.

Final scoped audits keep all prior history bytes, README, source, guards,
headers, Makefile, progress and production hashes unchanged. Mounted tools
remain clean at478e79f. The independent sibling's six tracked edits and2,428
untracked files remain untouched. A fresh actual-ELF recount confirms the
unchanged matching totals above. No matching credit is added by this note.
