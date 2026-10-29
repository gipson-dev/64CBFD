# 1835: Descriptor subtype appearance callback match

Date: 2026-10-29. `func_1518A214`, owner `generated_1B74A0`.
VA `0x1518A214..0x1518A2E8`; ROM `0x1B76C4..0x1B7798`.

Replace the false zero-return placeholder with a complete `s32` routine taking
an object pointer and a byte-output pointer. The object descriptor pointer is
at offset `0x188`, and descriptor subtype is its unsigned byte at `0x68`.
Subtype 15 clears object flag bit1 and returns output0. Subtype16 writes the
`D_800A73C4` scale (retail float32 0.3) to `0x128/0x12C` and RGB128/0/0.
Subtype17 uses the distinct `D_800A73C8` scale (0.6), RGB255/0/0; all other
subtypes use `D_800A73C0` (0.6), RGB255/0/0. Those paths write output1.
Every path returns1. Preserve the three distinct global bindings.

The retained indirect caller `func_1518A094` passes the object and its SP+0x4B
byte, then tests the result and byte to decide whether to continue processing.
Registration is `D_8008D5A0[0]`, ROM `0x232060`, VA `0x8008D5A0`.
The aligned ROM scan finds that pointer and no direct JAL words; it does not
exclude encoded/computed callers. The parent remains a C placeholder and gets
no new conversion credit.

The semantic source emits50 words, frame0, six HI/LO bindings. Twenty natural
pointer/structure/declaration forms all emit the same50-word body. Non-g3 O2
emits52; O1 emits68. Volatile controls do not recover the original shape and
are rejected; no volatile declarations or compiler-profile changes are adopted.

The closed normalization recipe uses every compiled input operation exactly
once, reorders independent setup/color/scale operations, retargets branches,
and expands three folded object-relative float-address pairs. Each added
`object+0x110` address feeds the original `+0x18/+0x1C` stores instead of folded
`object+0x128/+0x12C` stores. Fifty expected-word/binding guards cover the full
raw body, with three explicit `insert_after` address calculations and zero
omissions. Replacement code derives from compiled operations, not a copied ROM
body. Original assembly remains intact. This is guarded byte-exact matching.

Validation:

- 61,440 guest cases /184,320 executions: all256 subtypes, output aliases,
  flag patterns, float bit patterns and both O32 stack phases. Additional240
  cases alias the scale globals with object fields. Raw public memory/result
  agrees; normalized full tested machine state and access traces agree.
- 52 of53 retail words are reachable. The preserved duplicate flag load at
  `0x1518A270` is unreachable through the public entry; it is not omitted.
- The original18-word caller window `0x1518A0F8..0x1518A140` passes1,024 cases,
  including selector-1 skip and callback index0. Earlier descriptor/record gates
  are explicit preconditions; complete-parent/gameplay behavior is not claimed.
- Thirty-two dispatched access-fault prefixes match original/normalized code;
  subtype15 works with all three scale globals unmapped. Three independent
  GNU relocation layouts pass336 cases, including signed LO16 carry boundaries.
- Native32 O0/O2/O3 each pass92,160 cases with UBSan and reject eight effective
  source controls. Output/object and constant/object aliases are included.
  Numeric native float payload storage is separate from big-endian guest proof;
  no hardware FCSR or floating exception acceptance is claimed.
- All200 raw-byte and six binding mutations reject; all50 guard preimage
  mutations reject. Source-color and unexpected-diagnostic controls reject.
- Copied complete owner preserves five neighbors and normalized pools. Actual
  three-command Make output reproduces the qualified padded object. Selected
  and complete owner compilation produce zero diagnostics. The existing
  duplicate-recipe Make warning is inherited and unchanged.
- Eight fresh canonical methods run independently from both tools copies,
  plus each shared tools check. After installation, two checks per copy run
  fresh and six semantic checks reuse only exact input/module/artifact identity.
- Production ELF equals the independent full-file prediction:223 changed bytes
  =162 target code +1 target extent +60 symbol/string metadata. Three fixed
  name-order groups account for every metadata byte: a two-name swap at
  `0x29CA24`, three-name rotation at `0x29D514`, and four-name rotation at
  `0x2DCBF4`. Every named value/type/section is preserved apart from target size;
  zero exclusions. Other6,055 linked bodies and all addresses remain fixed;
  189,088 protected Game data bytes /720 owners remain exact.

Measured from the adopted ELF: **3,912/5,506 (71.05%)** total,
**3,239/4,833 (67.02%)** Game, Init492/492, Debugger181/181, zero drift.
The C inventory is unchanged; **218** more matches reach the4,130 threshold.

Tools commit first: `4f766bbd1b04c0fb077630431452c7b1e37d2bd4`. Consumer pins it; no push. The older tools
mirror retains all1,943 inherited dirty paths and three new tool files.
No host-port, frozen Release, save/editor or memory changes. Zero Claude calls:
the local compiler, retained caller, closed transformation and oracles resolve
the target. Harness syntax/packaging failures are retained as diagnostics and
are not counted as passing qualification.

Graphify receives a scoped native structural refresh. All49,364 prior nodes
and102,411 prior valid relationships must be retained or uniquely relocated.
Signature, constant bindings and original caller registration are source-
validated. No direct caller edge, provider conversion credit or full-corpus
extraction is invented; outside-scope manifest/communities remain historical.

Artifacts: `conker/build/game-subtype-appearance-match/`. Next screened target:
`func_15195D00`; screening is not source/ABI/matching qualification. Previously
parked candidates, including `func_15030310`, remain private and uncredited.
