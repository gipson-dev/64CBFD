# Note 2478: Selector-mask defined shifts and guarded match

Date: 2026-11-15. Consumer baseline `ff93fee34718b0bd470642fb62f8c1c579d65781`,
tools baseline `5c1750ac08d9ce07c1e0f81b632997e0410c6fbc`.
Tools implementation and qualification: `836b220ac68153663cd41c869425e3007949e4d7`.
Continues [Note 2415](2415-game-selector-mask-private-screen-20261114.md).

`func_1515942C` is adopted and **byte-exact across all 90 words / 360 bytes**,
with its original **0x40-byte frame**. The complete C preserves defined
five-bit shifts for all signed selector and byte-field values. **62 checked
guard rows** normalize ten redundant masks and the closed scratch-register /
independent scheduling changes: **ten omissions, 52 replacements**, no inserted
instructions and no compiler-profile changes. This earns **one C match**.

## Source and ABI

Owner `conker/src/game/generated_185560.c`; VA `0x1515942C..0x15159594`,
ROM `0x1868DC..0x186A44`. The actor is valid. Five signed halfword arguments
select fields at bit offsets 0, 3, 6, 9 and 13; -1 allows the entire field,
using masks 0x7, 0x38, 0x1C0, 0x1E00 and 0x3E000. A key-0x13 lookup on the
actor's list at +0x2F4 supplies a node; its data pointer at +0x10 supplies five
bytes at +0x2C..+0x30. Missing lookup returns zero. Otherwise the result is one
exactly when the requested mask contains every generated field bit.

The C uses unsigned shifts with explicit `& 31`, including out-of-range signed
arguments and byte values. It does not import the alternate source's full-word
data reads or undefined shifts. Descriptive names/comments are retained. The
local output pointer is SP+0x38 and the initial result byte SP+0x37. Incoming
arguments reload after the lookup, preserving possible callback home changes.

The earlier 95-word candidate retained correct accesses but had a different
failure shape. Explicit early failure and a single OR expression recover a
**100-word** body. The expression is arranged so IDO emits the retail public
byte-read order **2D, 2C, 2E, 2F, 30**. A separate unsafe-shift diagnostic emits
90 words with 68 at retail positions; it is only compiler evidence and is not
the installed source. Installed C keeps all ten defined masks. The retained
manifest pins its full source, raw body hash and sole helper relocation.

## Independent normalization proof

The proof executes the actual 100-word compiler stream and the 90-word retail
stream, without using the guard mapping as a transfer template. MIPS variable
shift semantics reduce a shift count to five bits. Canonical symbolic ORs
establish the same final containment predicate across register and expression
trees. All **65 symbolic paths** agree in ordered public access/call traces,
all modeled private homes, return value, saved registers, FP state and FCSR.
Lookup return and post-callback incoming selector words are symbolic.

Four effective controls reject a changed field address, field mask, shift
register and C-side count mask. Another **101 raw-word/binding corruption
controls** reject changes to each compiled word and the helper relocation.
The two padder APIs produce the same exact body and retain all **36 owner
neighbors** and normalized pools. Two independent symbol rebases also agree.

This proof assumes valid mapped stack/storage and no public alias of private
stack. It proves normal instruction behavior; it does not claim identical
scratch registers at asynchronous faults. Finite overlap and fired-prefix
checks extend that boundary as described below.

## Fresh qualification

- **4,128 cases per stream / three streams** compare retail, raw C and guarded
  instructions. Every word is visited: 90 / 100 / 90. Complete memory, access
  traces, calls and return values agree. Cases include lookup absence/presence,
  signed selector boundaries, all-sentinel branch combinations, byte extrema
  and callback mutations. **57 fired memory-prefix cuts** agree on memory,
  prior calls and accesses; each cut dispatches a real memory instruction.
- **512 cases** connect the original **23-word** `func_1514ECE0` lookup;
  **512 more** run the original **seven-word** caller window at 0x1507F128.
  That window supplies `(actor, 0, 0, -1, -1, -1)`. The immediately following
  original BEQZ consumes this result. Full parent/hardware execution remains
  outside this bounded caller check.
- **102 private-stack overlap cases** retain complete access traces and return
  values. Four original instruction mutations are rejected. Unrestricted
  pointer aliases and arbitrary fault-register equivalence remain unclaimed.
- Defined C passes **328,960 native32 cases in each of six configurations**:
  O0/O2/O3, strict and non-strict aliasing, with trapping UBSan. Each signed
  16-bit value is tried independently in each selector, and every byte value
  independently in each data field. This is not an exhaustive cross product.
  A narrowed count mask is rejected in both aliasing modes.

Focused command:

```sh
python3 -m unittest tools.tests.test_game_selector_mask_1515942c_match -v
```

Fresh mounted preinstall and isolated sibling-overlay suites pass in **78.557 s**
and **71.606 s**; the installed suite passes separately. `make tools-check`
passes. The sibling's 2,434 prior dirty paths, HEAD and exact Windows Git-status
digest remain unchanged. Six task files are tested through an ignored overlay.
Prior unchanged neighbor suites are reused through exact source/object/image
identity, not reported as freshly run.

## Actual Make, strict image and progress

The private audit executes the five actual Make recipe commands, then links
the full image with the untouched production objects. Production subsequently
rebuilds through:

```sh
make -C conker -j4 -o Makefile -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

Independent whole-file prediction accounts for exactly **286 changed ELF bytes**
in the target body and its symbol size, with **zero exclusions**. All **6,050
other functions**, all addresses and extents, and **189,088 protected data bytes**
are unchanged. Of **698 objects**, only the target owner changes; all 36
neighbors, existing pools and prior guard rows remain fixed. The production
ELF equals the predicted private ELF, SHA-256:
`98f529aff93f50e86bf69088289f0ea80f86592e9843a8bd32bb6393ee2c644f`.

The **870-input** frozen audit changes exactly source, guards, owner object and
ELF. Conversion CSVs and the compiler/build inputs remain unchanged. Existing
four pointer/integer diagnostics and the duplicate generated_12D630 Make
recipe warning are unchanged baseline diagnostics.

Actual recount: total **4,508 / 5,514 (81.76%)**, Game **3,835 / 4,841 (79.22%)**,
Init **492 / 492**, Debugger **181 / 181**, **zero address drift**, **1,006 still
different**. Converted totals remain **5,514 / 6,048 (91.17%) / 86.19% bytes**.
The 85% total goal remains active: **179** more matches at this denominator.

## Retained attachment-effect boundary and next target

The saved union-factor experiment for `func_150F97EC` completed with two
90-word bodies, neither retaining the literal multiply by one. This phase's
three focused RNG-lifetime controls produce 93 / 93 / 91 words; they do not
improve the correctly conditional 90-word source from
[Note 2477](2477-game-attachment-effect-lifetime-and-false-fit-boundary-20261115.md).
Those rejected sources and receipts remain private. The production placeholder
is unchanged and earns no credit. The earlier consumed Claude review is not
repeated; this selector-mask phase uses **zero Claude calls**.

Next: **`func_1519EF90`**, 94 words / frame 0x40, in
`conker/src/game/generated_1CC440.c`, VA `0x1519EF90..0x1519F108`,
ROM `0x1CC440..0x1CC5B8`. Complete retail assembly and Graphify context are
located. Recover its attachment gate, perpendicular direction/heading fallback,
mode-dependent offset and height selection; qualify literals, FP order, helper
ABI, output aliases and callers before installation. It remains a zero-return
placeholder and is uncredited.

Evidence is retained in `conker/build/game-selector-mask-1515942c-match/`:
frozen inputs, source/profile probes, manifest, proof/guest/native receipts,
both padder outputs/rebases, all three suite logs, actual Make commands,
independent image, production audit, fresh recount, sibling snapshots and graph
receipts. Scoped AST extraction covers six files and retains all **62,090**
prior IDs, with zero lost IDs; this is not a full-corpus extraction. Five DOCS
indexes receive one concise entry. Root README changes aggregate rows only.
The sibling host folder contains only `.codex` and `recomp_scene`, with no Git
checkout or CMake entrypoint; no host build applies. Frozen Release, saves and
private inputs remain untouched. No push.
