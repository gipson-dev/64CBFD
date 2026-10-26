# 1735 - Environment Color Command Scan Match - 2026-10-26

The adopted Native ELF measures **3,812/5,506 exact C functions (69.23%)**,
Game **3,139/4,833 (64.95%)**, zero address drift and 1,694 different.
Only `func_15012ED8` gains credit. Inventory and converted-byte totals stay
fixed; 318 more matches reach the present 4,130-function 75% threshold.

## Complete semantic C and return contract

`func_15012ED8`, owner `generated_3FC60`, occupies VA
`0x15012ED8`..`0x15012F90`, ROM `0x40388`..`0x40440`: 46 words,
frame zero and no separate alignment words. The complete
`s32 func_15012ED8(u32 *displayList)` replaces the zero-return placeholder.
Keep the retail symbol; the local RGB type and comment describe observed
command processing without inventing a gameplay name or changing shared headers.
The u32 pointer admits the observed four-byte command alignment.

Walk eight-byte command pairs until signed opcode -33 (SDK G_ENDDL, DF).
On signed opcode -5 (G_SETENVCOLOR, FB), snapshot the unsigned counter
`D_800BE564`, save the current command index as a halfword to `D_800BE550`,
and store the RGB bytes in three-byte records at `D_800BE530`. Alpha is ignored.
Preserve three separate payload reads: after the index store, after red, and
after green. Capture blue before storing capturedSlot+1 to the counter; then
store blue. Fetch the next opcode after these stores. Return the scanned count
in V0. No reset, clamp, or invented capacity check is added.

The fixed guest globals overlap: RGB slot 10 reaches the index table, and
slot 17's green byte reaches the counter. Input commands can alias these same
bytes. Do not infer disjoint storage from the local unsized C declarations.
The native fixtures use independent, in-bounds logical arrays; actual fixed
overlap, missing-end boundaries and emitted faults are qualified separately
in the big-endian guest model. They are not portable C fault guarantees.

## Actual compiler profile and guarded fit

The owner already has a target-specific -O2 profile. The generic O2/g3 helper
initially produced 12-byte placeholders and a 47-word candidate, whereas actual
Make's placeholders are eight bytes. That private fit is not installed or
credited. New, separately named O2 before/after objects reproduce the actual
baseline and preserve every neighbor. Failed/profile-discovery receipts and
original raw executions remain intact.

The actual complete C emits 46 words, frame zero, with six HI16/LO16 bindings;
raw body SHA b8aa821e21f3b64eea16d2ea78a1f88e939d649686f932447b42a9ab6214ee4f.
Forty expected-word/relocation rows derive closed register lifetimes, independent
opening/address scheduling and the captured-slot increment schedule. Allocate
the complete count lifetime to V0 and opcode/slot to V1. The now-redundant
return copy in JR's delay slot becomes NOP. No instruction is inserted or omitted,
no memory access is reordered, and no profile override or volatile is added.
This is **guarded semantic C**, not a compiler-only match or a retail-word C array.
Every previous guard byte is retained as an exact prefix.

The original assembly, fitted body, and six complete bindings agree. Preserve
all three raw/padded owner neighbors, their pools and addresses. Actual shadow
Make runs its three compiler/padder/assembler commands; all four compact
functions agree and its whole padded object equals independent qualification.

## Behavior, caller and negative controls

Both canonical tools copies pass six fresh checks and shared tools checks.
Installed copies each run two fresh input/image checks and reuse four unchanged
semantic checks only under the sealed module/input/artifact fingerprint.

- 7,936 guest cases cover all 256 opcodes and unsigned counter values, two stack
  phases, the fixed global overlap and 18 four-byte input/global aliases.
  Raw C agrees with an independent memory/access-order/count reference;
  fitted/original complete states agree. All 46 retail words are visited.
  307 alias cases deliberately reach a mapped-boundary failure after losing
  their end command; they are bounded prefixes, not successful list scans.
- SDK/native32 O0/O2/O3 each execute 65,537 cases with trap UBSan, all opcode/counter
  combinations, byte counter wrap, full logical-array canaries, ignored alpha,
  count return and halfword index truncation after 65,536 commands. Eight compiled
  controls for opcode, stop, RGB channels, index, increment and return all fail.
- 888 fired access faults preserve raw memory/access prefixes and fitted/original
  complete states. Unmapped and misaligned input reads are also checked. Forty-six
  raw-word and six binding corruptions reject changed compiler inputs; all 80
  stale expected-word/relocation controls fire in the real padder.
- Nine GNU links exercise original, raw and fitted code across three HI/LO-carry
  layouts. Seven complete-image corruption controls are effective. All 6,056
  function addresses, 6,055 other bodies and protected Game data remain fixed.

The aligned census scans the whole 2,467,288-byte reference image. The scanner
has one direct JAL at ROM `0x400FC`, VA `0x15012C4C`, and no aligned literal-address
registration. Parent `func_150127B0` receives its sole direct call at VA `0x1500E514`.
The latter is raw-word restored assembly, so a named-ASM search alone misses it.
Graphify supplies source/owner navigation; retail bytes establish the ABI.

Execute the original 15-word parent tail `0x15012C48`..`0x15012C84` in 12 cases.
Its JAL delay slot loads the input pointer from `D_800B0E00`. Preserve S0..S7,
FP, RA, the 64-byte parent frame and the forwarded V0 count. The upstream
`func_1500E470` calls another helper immediately without reading that result.
The complete larger parent, upstream function and gameplay remain outside this
credited conversion. The first test-link fixture omitted an unrelated neighbor's
global definition; resolving that existing symbol fixed the fixture without
changing the recovered C or raw compiler objects.

## Production, banked inputs and measured continuation

Production Make exits zero in 5.525s and reproduces independent
ELF 59d3bd429e7ccdbb3b4be813f439298240f4e5f2bda288c5d6bd931d7af8ca5a. The complete delta is **187 bytes: 135 code bytes and 52 metadata
bytes, zero exclusions**. Target size changes from eight to 184 bytes.
Two closed linker symbol/string swaps explain the other metadata bytes:
(`func_150BABE0`, `D_8009EF78`) and (`D_800991CC`, `D_8009E6DC`). Named definitions
are unchanged apart from the target extent. Protected Game data remains exact:
720 owners / 189,088 bytes, SHA
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
The inherited `generated_12D630` duplicate-recipe warning is unchanged.

Source SHA: 363e866a0c24e87b5f7630f2284b32a5aa90d622d6c325fe98fe53a763992271.
Padded object SHA: 6e0f9a57f8c90fbeb0ec86d0994d78420f21c599ff1846ee4832dd2c826a5f0e.
Baseline consumer b5265e4c, tools b94c8d58, ELF becd3288.
Tools 6b2f3e80e54cabc9c15eba2df7d2948f1ffd46d6 are committed first; the consumer pins that commit.
The seal covers 16,107 Native files and exactly five qualified adoption outputs.
Preserve all 1,680 pre-existing dirty paths and the older tools mirror's history;
only the new pair is added there. No push or host-port work is performed.

The scoped native no-cluster graph refresh updates eight changed C/Markdown
sources and must retain or uniquely relocate all 44,304 previous nodes.
Manifest freshness outside that scope and historical community labels are
preserved. Global clustering/centrality is not recomputed, and no full-corpus
extraction is claimed. Tools AST extraction is separate from the parent graph.

The actual Native ELF-pinned queue contains 1,565 placeholders, 120 semantic/other
definitions and nine unlocated screens. Next screened placeholder is `func_1503B708`
(`generated_64120`), uncredited until its source/ABI, guest/native, owner/Make and
production gates pass. The unresolved pointer/NULL factory remains a placeholder.
Keep the 75% goal active. Routine Claude calls: zero.

Prepared-checkout focused command:

```sh
python3 -m unittest tools.tests.test_game_environment_color_scan_match -v
```

Keep frozen raw objects intact; a new compilation needs new fingerprints.
