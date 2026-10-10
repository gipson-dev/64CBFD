# Object Color-Mode Helper Byte Match

Date: 2026-10-10. Installed and linked byte-exact, not a direct compiler match.
Continue [Note 1207](1207-game-object-color-mode-semantic-recovery-and-table-gates-20261010.md).

## Target And Source

func_1502EC34: VA 0x1502EC34..0x1502EE8C, ROM 0x5C0E4..0x5C33C,
150 words / 600 bytes, frame 0x28. Replace the false zero-return placeholder in
[generated_58F80.c](../../conker/src/game/generated_58F80.c) with complete typed
void C accepting an object and four 32-bit output pointers.

The seven-mode semantics and alias-sensitive reloads qualified in Note 1207
are retained. Mode 0/>7 remains lazy; mode 1 uses direct or scaled/clamped float
opacity; modes 2/3 reload mode after stores; modes 4/5 retain rounded cosine
arithmetic and the post-opacity blend-byte reload; modes 6/7 retain the first
high byte and fresh packed/phase reads. Reserved locals keep the physical
scratch extent and are never accessed. Return-register value is not a contract.

Single Codex writer, zero Claude calls; existing compiler, parsers, interpreter,
native32, copied-owner asm processor, actual padder and ELF audits are reused.
No OGL, Release, save/editor work, memory writes or push.

New tools:

- [Closed matching driver](../../tools/experiments/game_object_color_mode_matching.py).
- [Focused full-match suite](../../tools/tests/test_game_object_color_mode_match.py).

```sh
python3 -m unittest tools.tests.test_game_object_color_mode_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Fresh baseline and receipts: conker/build/game-object-color-mode-match-test/.
Do not overwrite the earlier recovery, adapter or curve historical baselines.

## Closed Recipe And Table

Semantic C emits 148 words / 592 bytes, with the original 0x28 frame. A closed
148-row guard set retains every input word: 71 changed replacements and 77
unchanged dependencies, two insertions, zero omissions. It verifies the entire
expected raw body and relocation map. The recipe never reads or substitutes a
ROM body; it derives from those compiled words with explicit operations:

- 91 register-field renames preserve branch-local producer/use roles, including
  the opacity pointer, packed RGB values, phase, high byte and blend terms.
- Two commutative operand-order changes affect low-32-bit multiply and wrapping
  add only; floating operations and their operand order stay untouched.
- The cosine-path final store moves out of the branch delay slot. Its branch
  moves after the store, and the saved RA reload becomes the branch delay word.
  Retarget only the six branches whose exit displacements change with extent.
- Modes 6/7 reorder the opening opacity-pointer load, constant materialization
  and packed-word load to retail order. A captured-high copy keeps that value
  alive separately from the later phase-byte producer.
- The CSV inserts the relocated exit branch after raw +0x1E4 and the high copy
  after raw +0x21C. The two added operational lifetimes are RA reload/high copy;
  inserted-row placement is not an assertion that both are newly inserted opcodes.

All seven protected case starts now agree: +0x30, +0xD0, +0xD0, +0x108,
+0x108, +0x1F0, +0x1F0. Both compact-owner .rodata relocations change explicitly
to jtbl_80096F1C_game with zero addend, rather than rebasing the compiler's
0x100 addend through the wrong anchor. Independent linker rebases qualify
HI16/signed-LO16 carries. Existing owner tables retain their original anchor.

The new compact switch pool is not emitted into production data. Preserve the
original seven-entry table at ROM 0x23B9DC and adjacent constants
D_80096F38=0x40233333, D_80096F3C=0x3CC90FDB. All 150 linked words are exact;
there is no slot padding or relocated overflow helper.

## Fresh Qualification

Ten tests pass before installation in 11.738s and after installation in 13.546s.
The final strengthened renderer run also passes all ten in 19.044s, executing
helper instructions read from the actual production ELF rather than only an
equal diagnostic link. Prior unchanged broad-suite receipts remain prior, not
fresh reruns. The earlier semantic recovery body is unchanged apart from a
non-executing comment; the complete raw-word guard proves the compiler output.

- 1,697 guest cases / 3,394 executions compare retail and fitted bodies with
  complete private/public memory, ordered accesses and nested calls. Independent
  public reference agrees across all modes, direct values, finite clamp samples,
  output/object aliases, stack phases and bounded cosine responses.
- 210 private/public access fault prefixes / 420 executions verify the fault
  gate fired and exact ordered prefix/partial memory. Three reserved words are
  unmapped across 14 mode/stack cases, proving they are not accessed.
- 12 independent links / four symbol sets / 64 cases compare original, raw C
  and actual padded body across table/constant/cosine rebases and carry boundaries.
- Actual copied-owner preprocess/compile/postprocess is diagnostic-free and
  preserves all 37 neighbor bodies/relative relocations, existing pool prefix
  and every other padded owner byte. The target is exactly 600 bytes.
- The actual padder rejects each of 148 individually stale input words and all
  seven stale relocation specs; the closed recipe also rejects all 148 word
  mutations. Both insertions and protected-table relocation remain guarded.
- Actual full native32 C passes 73,728 finite normal-output cases: all modes,
  phase/high-byte boundaries and three bounded cosine outputs. This does not
  claim native aliases, actual cosf, hardware or FCSR behavior.
- Four fresh complete compiled semantic negatives fail independently: cached
  mode, cached packed value, byte opacity and unsigned blend shift.
- 64 complete banked-renderer cases use the production 475-word caller,
  89-word adapter, 34-word fallback and installed 150-word helper. Custom and
  fallback metadata, signed views, nine-quad strip memory/commands, nested
  helper entry and return agree with the independent renderer reference.

Graphics and cosine callbacks remain bounded; no live rendering, guest hardware
or full-game acceptance is inferred from these static/interpreter receipts.

## Linked Audit And Bank

Fresh build/progress and tools-check pass. Shared guard changes trigger a normal
wider rebuild. Existing duplicate generated_12D630 recipe, legacy pointer/type,
long-double and old compiler warnings remain; target/copy compiles are clean,
not the entire project warning-free.

Whole rebuilt ELF equals the fresh baseline after changing only the 600-byte
target slot and its symbol extent. Decoded ELF metadata agrees after normalizing
symbol/string order. The old guard file remains an exact byte prefix; only the
148 target rows are appended. Conversion CSV and original rodata assembly are
byte-identical. Protected data remains exact: 189,088 bytes / 720 owners,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Current source SHA-256 ceb308b4f004e5ff77c20f453b39bf2c029eb69c65bcc9ff6b76704a73a0d919.
Current ELF SHA-256 8c411142a1836ea9ee4ade35bb323478b8b18ed757cd184740fe46636fc40e19.

Fresh matcher: Game 2,751/4,816 (57.12%), total 3,424/5,489 (62.38%),
Init 492/492 and Debugger 181/181 exact. Zero drift / 2,065 different.
Converted totals/bytes stay unchanged because the placeholder already counted
as C. Root README changes only the two current aggregate rows.

Bank tools 9f71a62b9606e51149c53315bc571074a8c63213 first, then consumer
source/guards/docs/aggregate rows/pin. Mirror only the two absent authored files;
preserve older HEAD ddbdd16 and both independently dirty tracked fingerprints.
No push. Keep the fresh post-commit graph hook receipt separate from prior logs.

Scoped validator passes: 30 documents / 4,118 relative links, zero broken links,
44 authored tools with exact older mirrors and AST parsing in both copies.
Older HEAD and both tracked-dirty fingerprints remain unchanged. Manual
graphify update exits 1, refusing a 39,283 to 17,502-node shrink; retention keeps
19,398 nodes from 2,972 excluded-but-existing files. Existing package/skill
version and zero-node devcontainer.json warnings remain. No force, purge,
install or policy changes; verify the fresh consumer hook separately.

## Next: Phase Updater

func_1502EAFC is still a zero-return placeholder in the same owner. The complete
original is a 78-word / 312-byte leaf, VA 0x1502EAFC..0x1502EC34,
ROM 0x5BFAC..0x5C0E4. It accepts an object pointer; its caller func_1502BD84
ignores return value. Recover a void typed declaration/body together.

Mode +0xA4 dispatches modes 2..7 through six protected entries at
jtbl_80096F04, ROM 0x23B9C4. Mode 0/1/>7 is a no-op. Preserve signed comparisons
of low wrapping products against byte phase values, rather than assuming every
tick is positive. Modes 2/3 decrease phase to zero; mode 4 adds phase with byte
wrapping; mode 5 decays blend by ten ticks or clears mode, then falls through
to a fresh tick read and phase increment; mode 6 saturates phase at 255 and
changes mode to 7; mode 7 decreases phase or clears mode without clearing phase.
Tick is D_800BE9E4. Preserve every observable load/store order and dispatch label.

Take a fresh owner/ELF baseline: this conversion is an authorized neighbor change
and must not invalidate/rewrite historical recovery fingerprints silently.
Changing compact pool offsets must preserve this helper's guarded 0x100 input
addend or explicitly requalify/update the affected recipe, never loosen it.
Qualify a complete updater, table/leaf ABI, tick wrapping, aliases and connected
caller, then linked target-only changes and protected data before banking.

Preserve the separate uninstalled curve handoff in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game matching goal stays active; this one function is not completion.
