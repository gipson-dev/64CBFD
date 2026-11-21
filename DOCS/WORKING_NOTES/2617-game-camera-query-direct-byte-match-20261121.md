# Note 2617: Camera query direct byte match

Date: 2026-11-21. Consumer baseline `69c7685e847b618a7ef7332af9917ff8cb69b4e3`; tools baseline
`b7f85adce6781b59eadbb94784076a6e4cd3494a`. Qualified tools commit: `e818b138365f2866688a1377fc902c666ac6cf8a`.

`func_1509759C` replaces its zero-return placeholder with all five camera
query commands. All **127 words / 508 bytes**, the **0x50-byte frame**, RA
lifetime, private buffers and **17 code relocation sites** emit directly
from C. There are **zero guards, insertions or omissions**. All six owner
neighbors, including the preceding camera-shift restoration, remain identical.
The existing O2/g3 profile is retained; shared headers are unchanged.

Fresh production recount: **4,600 / 5,528 (83.21%)** total, **3,927 / 4,855
(80.89%)** Game, zero drift and **928** still different. Init 492/492 and
Debugger 181/181 remain exact. **99 more matches** reach 85% at this
denominator. The function already counted as C, so conversion rows and the
converted-byte totals are unchanged. README changes only two matching rows.

## Interface and recovered commands

Owner `generated_C3E20`, source `conker/src/game/generated_C3E20.c`, original
`conker/asm/C3E20.s:863`; VA `0x1509759C..0x15097798`, ROM
`0xC4A4C..0xC4C48`. The correct interface is
`s32 func_1509759C(s32 view, s32 command, s32 *parameters)`.
The camera pointer is calculated before the signed `D_80082FA0 < view`
upper-limit rejection. Negative views are not given an invented lower gate.

The original five-entry table at **0x8009DF38** establishes the semantic
command order independently of body order:

| Command | Result |
| --- | --- |
| 29 | Unsigned active byte at `D_800D2DC0 + parameters[2] * 0x24`. |
| 30 | Camera float at 0x37C multiplied by 65536, truncated to s32. |
| 31 | Camera float at 0x390 multiplied by 65536, truncated to s32. |
| 32 | Truncated horizontal distance from target X/Z to signed16 packed point X/Z; point key masked to 12 bits and stride 0x18. |
| 33 | Resolve actor key masked to 12 bits; null returns -1. Build forward vector from heading + retail PI/2, subtract camera target from actor position, clear Y, and return -1 for ordered dot >= 0, otherwise +1. |

Other commands and rejected views return zero. The final ordered comparison
also returns +1 for an unordered dot; replacing it with a reversed less-than
predicate would change NaN behavior. `D_8009DF4C` retains its retail bits
**0x3FC90FDB**. Angle is cached across sin/cos, and the camera pointer stays
cached across helper calls while later heading/target reads remain fresh.

The local camera view gains named 0x37C, 0x390 and heading 0x39C floats while
retaining its 0x9A0 extent and the previously recovered vectors. The point
view has signed16 X/Y/Z and a 0x18 extent. The real SDK `struct127 *`
lookup prototype and position at 0x14 are used. SDK32 asserts camera extent,
query offsets, all three actor coordinates and packed-point size/Z offset.

The recovered single fallback return, declaration lifetime and indexed local
point expression recover the exact code with no compiler guard. Earlier
127-word drafts still had incorrect default scheduling or local homes and
were rejected. Early instruction-only screens also preceded the separate
table-label audit; they are not semantic acceptance receipts. Final raw SHA256:
`58f04919d9f83efa5ab358f35d1e4055b35c16f9a82c9bbc76069aeca9585560`.

## Object, table and complete-image proof

- The original, raw C and padded target payloads/bindings agree. Section-local
  `.rodata` and the original unsuffixed table reference are explicitly bound
  to the existing `jtbl_8009DF38_game` symbol; no instruction is rewritten.
  The raw table has five R_MIPS_32 entries and 12 zero alignment bytes in its
  32-byte pool. Every entry points to the correct original case, including
  the reversed first three body labels. No duplicate retail table is emitted.
- Exactly three obsolete placeholder argument-home omission rows are removed
  from `retail_word_patches.us.csv`, preserving every other byte. The sole
  Makefile binding directs this owner to `jtbl_8009DF38_game`. Before
  installation, the real recipe is exercised using the exact proposed
  Makefile; after installation its natural recipe agrees. Three commands
  produce the independently prepared owner object.
- The actual dependency rebuild and live recount pass. All 6,051 function
  slots and the complete production ELF agree with an independent declared
  prediction: **509 changed bytes**, **zero exclusions**. Named symbol
  attributes are unchanged except target size 12 -> 508. Three independently
  audited closed metadata permutations cover eight records / 102 string
  bytes: table/func_15071A34, the D_8009DF4C four-name group, and
  func_1511F92C/D_800E0D88. No symbol or string section is omitted.
  Protected Game data, including the dispatch and jump tables, remains
  **189,088 bytes / 720 owners exact**. ELF SHA256:
  `00ae7bf4b95fb7c64359eaf41b2c83cfb8f4fca4090e71704f7a88beced44f99`.

## Execution, caller and relocation checks

- Guest checks pass **3,840 cases per stream**, covering all **127 words**
  in original/raw/padded code and **51 target-access fault prefixes**.
  Complete memory, private stack, GPR/FPR/HI/LO, calls and ordered accesses
  agree. Explicit lookup/sin/cos effects exercise changed globals, argument
  homes, camera values and cached angle/camera lifetime. Four effective
  controls catch a bad limit, key mask, dot order and table permutation.
- **120 connected-helper cases per stream** cover all **26 original
  subtraction and dot-product words**, separately checked against the current
  linked ELF. Lookup and trig routines remain bounded effectful contracts;
  no full helper acceptance is inferred from these interfaces.
- Native SDK32 passes **893 cases each at O0/O2/O3**, strict aliasing and
  UBSan. It uses the recovered subtraction C and real SDK camera/actor
  storage. Eight effective source controls catch the limit boundary, command
  ownership, fixed scale, parameter word, signed point axis, horizontal Y
  clear, ordered dot test and camera reload. Invalid native indices and
  out-of-range/NaN float casts are excluded from native acceptance and tested
  as guest instruction behavior. Single arithmetic/sqrt and indefinite
  truncation results are modeled; FCSR flags, exceptions and hardware are not.
- The fresh census finds no direct original call and one aligned loaded
  function pointer: **0x800884B8**, slot 8 of **D_80088498**. Computed
  references are not excluded. The complete **92-word func_1509BE40** equals
  the current linked caller and passes **1,980 cases per stream**, covering
  all 92 words through its actual indexed JALR. It builds the parameter
  packet, forwards the signed result and restores `D_800D3840`. Three controls
  catch a skipped query, wrong command home and incorrect context restore.
  This does not qualify the complete script engine or gameplay.
- Eight GNU links at two independent code/data bases agree with separate
  binding calculations: six isolated original/raw/padded links, plus two
  whole raw-owner/table links. All five table R_MIPS_32 targets and signed
  HI16/LO16 carry are exercised. SDK extern declarations lacking any
  relocation remain unbound; the audit explicitly verifies no relocation
  references them. Unrelated compact-owner function addresses are outside
  that raw-link scope and remain covered by the production image audit.
- Five focused checks pass freshly before and after installation in both
  primary and isolated sibling configurations, plus shared `make tools-check`.
  Imported source/data fingerprints agree. The actual dirty sibling HEAD,
  status and 352 dependency hashes are preserved. Unchanged historical
  neighbor receipts are reused by fingerprint, not claimed as fresh tests.

Existing duplicate `generated_12D630` recipe warnings and untouched neighbor
diagnostics remain; this is not a warning-free build claim. The available
host scene configuration consumes binary words/symbols and has no identical
saved target window; its configured symbols file is absent. Host mapping,
gameplay and runtime acceptance remain unknown. No host/Release, ROM/save,
model or push action is included. The wider 85% goal remains active.

Continue with fresh caller/profile screening of remaining ordinary Game
routines; this owner's `func_15096A68` and `func_15096D78` are still stubs.
The earlier keyed history callback, sequence query and noncanonical-return
camera transition remain private and uncredited.

Graph maintenance: the native update exited 1 with all
70,008 prior IDs retained. The subsequent serial scoped extraction
covers 6 C/Python files with no missing AST sources, producing
70,052 nodes / 160,284 links and retaining prior qualification
metadata. This is a scoped refresh, not a full-corpus re-extraction. Actual
commit-hook producers must be terminal and their ID/metadata retention audit
must pass before the final immutable bank is accepted.
