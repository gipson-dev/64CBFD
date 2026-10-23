# Payload Link Event Trio Guarded C Match

Date: 2026-10-23. Predecessor consumer `80e7df26`, tools `b792eeb`.
Qualification tools committed first as `31e7a37`.

## Recovered Batch

Recover three complete callbacks, each 43 words / 172 bytes, frame 24 and
one R_MIPS_26 release binding at +0x44:

| Function | Source Owner | VA Span | ROM Span | Table Slot |
| --- | --- | --- | --- | ---: |
| `func_1519E570` | `generated_1CA420.c` | `1519E570..1519E61C` | `1CBA20..1CBACC` | 2 |
| `func_151A4D88` | `generated_1D0840.c` | `151A4D88..151A4E34` | `1D2238..1D22E4` | 1 |
| `func_151ABD54` | `generated_1D6E80.c` | `151ABD54..151ABE00` | `1D9204..1D92B0` | 9 |

Keep address-based names, add purpose comments and retain original assembly.
The original routines have identical retail text, SHA-256
`aeb5314c6b97401a68a8b3dfe749b93b1dda04a7658f99595ba20314ba170b61`.
Identical bytes alone were a batch-selection screen, not acceptance evidence.
Qualify every owner, registration, call, relocation and final linked slot.

## Semantics And Interface

Use the actual callback interface `void (struct260 *owner, s32 eventAddress,
u8 command)`. Convert the word address to a private twelve-byte packet view;
the owner's private eight-byte link begins at +0x28, with identity +0x2C.
Preserve opaque bytes and the existing global actor/header definitions.

These routines select command zero first and load the owner's pointer before
the packet pointer. Release the owner when those pointers match, or when
its identity equals raw packet byte +4. That command-specific byte is not
the retarget packet's identity at +8/+9. For command 0x2D, capture the current
link once, prefer the first matching packet pointer, store the opposite
pointer and only then read/store its late identity at +9 or +8. Ignore other
commands without dereferencing their payloads. Keep the full incoming
command word in its original argument home before narrowing to a byte.

The zero-first, owner-before-event load order differs from Note 1681's
retarget-first callback. Preserve it in guest traces and fault prefixes.
Keep the naturally unreachable duplicate load at word 33 / +0x84 in all
three routines. Visit the other 42 words naturally; do not force entry.

Add local payload types and the existing release-helper declaration to
the three owners only. Explicit `(struct102 *)` argument casts are needed
at the existing byte-pointer calls in `func_1519E61C` and `func_151A4F7C`.
They remove the new typed-prototype warnings while preserving both complete
function bodies and relocations. The third owner needs no such cast.
Do not change shared headers, compiler profiles or the original assembly.

## Two Closed Allocation Cycles

This is guarded semantic C, not compiler-only output. All three raw C bodies
have SHA-256:
`72b888b69c2117b33fe0d428342e9482944c06cd2b6fd7dc0b406bf7d2b07334`.

The release block's words 9..11 exchange T7/T8, commuting equality word 11.
The retarget block's words 24..38 exchange V1/A0, commuting equality words
26/34. Symmetric words 11 and 26 remain unchanged. Exactly six words per
routine require guards, eighteen rows total:

| Offset | Expected Raw C | Retail |
| --- | --- | --- |
| `024` | `8C580000` | `8C4F0000` |
| `028` | `8CAF0000` | `8CB80000` |
| `060` | `8C430000` | `8C440000` |
| `064` | `8CA40000` | `8CA30000` |
| `088` | `546B0005` | `55640005` |
| `090` | `AC440000` | `AC430000` |

Verify the whole raw hash and sole binding before deriving either cycle.
Only register fields and commutative equality operand order change; keep
opcodes, immediates, calls, branches, frame, saved-register lifetime and
extent. No inserted or omitted words. Preserve the entire old CSV prefix.
Qualified guard CSV SHA-256:
`fb52b3db3529db91f553ee7746a5c68adf7968ccbd085bd4e571e0a821fb0585`.

## Actual Registration And Callers

Each callback has exactly one literal ROM pointer and no direct JAL. All
three are in the same 74-entry `D_8008A8D8` table, VA `8008A8D8`, ROM
`22F398`, in `22EF80.rodata.s`. Their pointer words are at ROM `22F3A0`,
`22F39C` and `22F3BC` respectively. Verify all table words in ROM and ELF.

The shared caller `func_15149434` remains byte-exact across all 23 words,
frame 24. Qualify every unsigned selector byte at owner +0x13: values
74..255 select slot zero, and NULL callbacks bypass the call. Retain the
original redundant BLTZ and branch-likely behavior. All caller words are
naturally visited across 61,440 phases. Compile its actual existing C body
in native fixtures; other table callbacks remain bounded providers.

Preserve its complete twelve-function object, SHA-256
`e25e23423217e12289d36ef8ddd82eb68ba757c7b708340995f7a7d8a987aabf`.
Qualify all 56 original/current release, cached scan and default-release
words in `func_1516972C`, `func_151696DC` and `func_15169804` over 360
phases. Cover signed count bytes 128/255, owner-slot replacement, type gates
and optional type/default dispatch. Lower release and other callback
providers remain bounded; full heap, broadcast and gameplay are unclaimed.

## Qualification

Both tools copies pass eight fresh pre-install tests, then two fresh
installed checks, with zero errors/failures/skips. Explicitly reuse six
unchanged behavioral checks after installation only under strict source,
raw/padded object, guard, caller/helper and complete-image identity. Both
shared tools checks pass. Reuse the existing compiler, parser, padder,
MIPS-oracle, native32 and GNU-link helpers; no dependency or oracle edits.

- 16,260 target guest phases and 720 aliases cover all byte commands,
  noncanonical homes, full-word keys, ordered pointer reads, late byte reads,
  duplicate first-match preference and ignored unmapped arguments.
- 7,895,040 native32 cases per O0/O2/O3 build across the three routines,
  2,631,680 each, cover direct calls and the actual dispatcher over every
  selector byte. Trap UBSan and twelve effective wrong-C controls per
  routine pass. Use fresh allocated owner storage, a disjoint typed packet,
  real pointers, explicit opaque bytes and fences, not a declared undersized
  `struct260` object. Keep the global short header unchanged.
- 27 independent GNU links and 360 rebase phases preserve original/raw/
  padded code at alternate entries and release addresses.
- 2,598 fired root-access prefixes compare normalized complete state,
  memory, attempted access and branch-delay PC. Raw C public results and
  traces pass, but raw complete-GPR equality is not claimed.
- 33 raw/binding corruptions and nine distinct strict-image controls are
  rejected. Each old zero-return stub fails effective semantic cases.

Native evidence is bounded to GNU/Linux 32-bit allocated owner storage and
disjoint typed packets. Guest aliases, private homes and invalid addresses
qualify emitted N64 behavior, not portable C fault semantics or native64.
Only guarded output claims literal complete-state equality with retail.
The earlier private probes were screens; both final eight-test suites are
fresh qualification, not those private results relabeled as published tests.

## Make And Preservation

The first run stopped at an inherited three-command Make precondition,
before running tests. Inspect and retain the actual per-owner recipes:
three commands for `1CA420`, five each for `1D0840` and `1D6E80`, thirteen
total, all normal O2/g3. The latter owners retain one and seventeen
`GLOBAL_ASM` neighbors. Pin all eighteen referenced assembly files, expanding
the focused snapshot from 33 to 51 inputs. Preserve the failed zero-test
receipt separately, then rerun all eight tests in both copies.

Actual Make reproduces all three complete qualified padded objects byte
for byte. Preserve 22, 22 and 40 neighbors respectively, 84 total, including
both typed-cast neighbors and every existing assembly routine. Pools,
addresses and non-target extents stay fixed. Padded object SHA-256 values:

- `generated_1CA420`: `1ae2dfe1cb27c83ae7c7b829c411a5d4d32fefa714a658c0ad30aa6d6406cf93`
- `generated_1D0840`: `890b92b4db9715298c0dd431682e9925ab70170a391df7aa538a3279d41cd2e1`
- `generated_1D6E80`: `87dc45dc61c8d8204eca69bf24bcd587460d6d13651f981fa42b0c766240c1a7`

Independent linking and production Make agree on exactly 357 changed ELF
bytes: 354 target-code bytes and three symbol-size bytes, zero exclusions.
ELF SHA-256:
`28e5b2e952e95ae65484b3668a712fadf9e93d046d893ee8f41d5b3f1d1802e2`.

Preserve all other 6,052 bodies, all 6,055 function addresses and all 720
protected Game-data owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal and recheck 15,898 files, every one of 1,454 linker objects and all 51
focused input pins. Advance the preceding checkpoint's four adopted entries;
this checkpoint has eight mutable entries: three sources, three objects,
CSV and ELF. Promote the linker script and progress CSV unchanged. Keeping
the guard CSV old for bounded Make is justified by its intact prefix and
eighteen new rows scoped only to the rebuilt owners, not whole-file identity.

Commit primary tools first; preserve all 1,576 preexisting dirty paths and
the HEAD of the older standalone tools mirror, adding only the two identical
task files. Do not push or touch host Release, saves or configuration.

## Recount And Handoff

Run the standard matcher against the adopted live consumer ELF, not just
the independent prediction. It exits zero in 14.739 seconds:

| Section | Exact C functions | Address drift | Still different |
| --- | --- | --- | --- |
| Total | 3,754 / 5,505 (68.19%) | 0 | 1,751 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,081 / 4,832 (63.76%) | 0 | 1,751 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The converted-C denominator is unchanged. The 75% goal remains active:
4,129 exact functions are required, 375 more than this checkpoint. Remove
only these three newly exact entries from the ELF-pinned queue; it contains
1,620 placeholders, 122 semantic/other definitions and nine unlocated entries.
Next `func_150A00F0` is a 43-word placeholder with 42 differences. It is queued
only, unqualified and uncredited. Keep the 862-word `func_1508CAD8` owner stub
queued separately. Do not equate source-shape triage with recovered behavior.

Primary tools are already committed at
`31e7a37f20ba7e6ce8380fa23cd05625b628f532`. Bank only the twelve scoped consumer
paths after the installed-image, documentation-link and old-mirror audits.
The normal post-commit Graphify refresh must complete before its retention
audit; require all 43,810 old nodes retained or uniquely relocated, changed
C/Markdown extraction current and the graph stamp at the new consumer HEAD.
Excluded-old-corpus warnings do not establish clean full re-extraction.
