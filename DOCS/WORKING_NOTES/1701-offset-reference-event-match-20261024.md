# Computed-Tail Reference Event Match

Date: 2026-10-24. Consumer predecessor `b968db0f`; tools predecessor
`b844373a`. Qualification tools committed first as
`27b4a9756a4865bae5f4feb4d6c4fa4f4143c964`. No push requested/performed.
Routine work, zero Claude calls; no provider/dependency/host changes.

## Recovered Routine

`func_151BA468`, `conker/src/game/generated_1E73B0.c`, replaces a three-word
zero-return placeholder with the complete computed-tail reference event.
VA `0x151BA468..0x151BA518`, ROM `0x1E7918..0x1E79C8`, exclusive ends:
176 bytes / 44 words / frame 24 / one binding, no alignment tail.

Recover `void(struct132 *owner,s32 pairAddress,u8 command)` from the actual
caller. Retain the existing header type and canonical release prototype;
use a local `OffsetReference1E73B0` word/tag view. The signed offset word at
owner+0x50 selects a tail at owner+offset+0xF8, with reference at +0 and
stored tag at +4. Do not extend shared struct132 from this one local view.

1. Always read the owner offset and capture the tail reference, even for
   otherwise ignored commands. Preserve the full incoming A2 word home
   before byte narrowing, including guest private-home overlap.
2. Command zero releases the owner if pair word zero equals that reference,
   or the referenced object's unsigned byte +0x3B equals packet byte four.
   This is not a comparison with the stored tail tag. Keep short-circuiting
   and release the owner, not the referenced object or packet.
3. Command 0x2D exchanges a matching reference with the other pair word,
   then assigns the corresponding tag byte nine/eight. First match wins;
   read each tag after the word store because the packet and tail may overlap.
4. Other byte commands ignore the packet but still require a readable
   owner and computed tail. Do not copy an earlier handler's NULL-owner gate.

The first source shape emitted 43 words. Capturing the pointer view and
word value separately recovers the full 44-word schedule under normal O2/g3.
Bounded source/declaration/type screens retain register-allocation and
commutative-operand differences. No new profile, volatile barrier, inline
assembly, inserted instruction, omitted instruction or assembly-body replacement.

## Derived Lifetime Guards

Validate the complete 44-word raw hash and sole JAL binding before deriving
the normalization. Eighteen expected-word rows encode the following roles:

| Role | Raw Register | Retail Register |
| --- | --- | --- |
| Computed tail address | V1 | V0 |
| Captured reference value | T0 | V1 |
| Byte command copy | T1 | T0 |
| Early removal comparison word | V0 | T8 |
| Late replacement comparison word | V0 | A0 |
| Referenced-object tag | T8 | T9 |
| Removal packet tag | T9 | T1 |

The two first-word lifetimes are disjoint. Owner A0 remains intact through
the removal path; reuse A0 for the pair word only in the replacement arm.
The early T8 comparison value is dead before the tag load. There are no
new spills or saved-register changes. Raw helper calls retain the same
owner and complete public memory/call trace under the ordinary volatile ABI.

Exchange operands only in unsigned ADDU at +0x20, BEQ at +0x38 and BNE-likely
at +0x8C. Unsigned addition and equality/inequality are commutative. Keep
every opcode, constant, address offset, displacement, delay slot, instruction
count and the JAL relocation at +0x50 unchanged. No guard overlaps that binding.

The duplicate load at +0x88 is unreachable but retained in the full match;
43 executable words are visited. Raw C and original agree on public results,
all memory/access traces, saved state and calls. Do not equate their different
volatile GPR allocations. Fitted and original complete private states do agree.
This is guarded semantic C, not compiler-only matching.

Raw payload SHA-256:
`e409cb01828b32a1b4fca0b2427c86d8722dc32e6dcd43f6e65470a417eb8c97`.
Resolved retail body SHA-256:
`aaeeacb762424d7fe17b0117ac5ae4e099e07d8100537e1ec1e1d49f09519852`.

## Caller And Release Chain

An aligned full-ROM scan finds no literal target pointer and exactly one
direct JAL site, at ROM `0x168F6C`, in `func_1513BA78`. Its complete 23-word
body is already byte-exact and unchanged. It narrows the command, reads
owner byte +0x48 and routes kind one to `func_15109064`, kind two to the
recovered routine, and other kinds to return. Execute every kind byte and
all 23 words in 3,072 phases. The kind-one handler remains bounded.

Correct its local target declaration from obsolete s32 to void in
`conker/src/game_168A90.c`. All 13 caller-owner functions/pools remain fixed;
the complete actual padded caller object is byte-identical. Compile the
actual caller C with the recovered routine for native interface checks.

Execute all 28 unchanged `func_1516972C` release words in 288 connected
phases, including bookkeeping mutation before its late kind read, kind
boundaries and callback/fallback routing. Compile its actual C body in
native checks. Bookkeeping/destructor/fallback and the other kind handler
remain bounded providers, not full engine or gameplay acceptance.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation:
no errors, failures, skips or reused checks. Pre-install primary/mirror:
100.689s / 98.795s; installed: 100.383s / 103.484s. Both shared project-tool
checks exit zero. Reuse existing MIPS, frame/fault, native32, source-span,
relocation, object/pool and ordinary generated/legacy padder helpers.

- 19,440 original/raw/fitted root phases cover all byte commands with upper
  word variants, pointer patterns, first/second/neither matches, referenced
  tags, four signed offsets, seven guest aliases, two stack phases and
  provider mutation. Compare independent public semantics and literal traces.
- Native32 O0/O2/O3 trap UBSan covers 1,572,864 root cases and 131,072
  actual-parent cases per optimization, ten effective defined wrong-C
  controls and full allocated backing. Native-endian packet words and byte
  accesses are checked separately from guest big-endian/private-home aliases.
- Forty fired root-access fault prefixes compare complete fitted/original
  private state, plus raw memory/events/saved state. Five ignored commands
  allow a NULL packet but reject an unreadable owner in the guest model.
  These are instruction-access checks, not portable C fault semantics.
- Forty-six raw-normalizer corruptions reject all changed words, a missing
  binding and a short body. Two real padder corruptions reject an expected
  word mismatch and wrong relocation expectation. Prefix corruption fails
  closed, preserving every historical guard row and byte.
- Nine GNU links independently compare assembled original, qualified padded
  and actual Make objects at three entry/release pairs. Execute 126 rebased
  phases; three independent whole-image corruptions are rejected.

The private CSV writer initially escaped newline literals twice; correct it
before qualification. The caller's actual Make plan has three commands, not
the mixed target's five; bind the checker to the observed recipes. No guard
scope, production semantics or immutable-input requirement was relaxed.

## Production And Preservation

Advance the preceding checkpoint's three qualified overrides, then seal
15,970 initial files. Add the two owned tools modules in both copies:
15,974 files / 42 focused inputs / all 1,454 linker objects. Use the verified
Linux cache and checked native stdin/tar bridges, no DrvFS project reads.
Preserve all 1,614 baseline mirror dirty statuses/hashes/HEAD; add only the
two owned modules, now 1,616 paths. Do not reset or commit that mirror.

Actual Make uses five normal commands for the mixed target and three for
the legacy caller, both O2/g3. Preserve all 56 raw/padded target neighbors
and pools, all 13 caller-owner functions and the unchanged release owner.
Isolated diagnostics are empty; whole-owner diagnostics are unchanged.
Inherited pointer/integer and duplicate generated_12D630 recipe warnings
remain, not a warning-free build claim.

Production Make exits zero in 0.768s. Independent and production complete
ELFs agree on exactly 121 changed bytes: 120 target code plus one target
symbol-size byte, 12 to 176. Zero metadata exclusions or unrelated changes.
Preserve all other 6,054 bodies/all 6,055 addresses and protected Game data:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,974 native files around adoption with exactly five overrides:
target source, caller declaration source, CSV, target object and linked ELF.
The caller object itself stays byte-identical. Re-capture and freshly recount
the actual live adopted ELF, not an inferred +1. Append exactly 18 guard rows
with zero removals; all previous bytes remain an identical prefix.

Installed ELF SHA-256:
`cf1d1caf927af6465ce45f5e95b09fa292b5ddcd454b37207736f309d2011fa7`.
Installed target object SHA-256:
`75638e249a902cf27c97003929eb77977642b5c6d82b76a430e27f565c532c0d`.
New guard CSV SHA-256:
`c29ddb1088d2b844a43b92bae7199d7045f19bab36c29b25798c9b44d4bcc6a5`.
Unchanged old-prefix SHA-256:
`6d19dfd5806dedfc839f6c7e33f8fb2d1123d826021b93505bd7a265e516f427`.

Root README changes only Total/Game aggregate rows. Detailed recovery updates
stay in DOCS. Host Release, saves, configuration and private inputs untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,778 / 5,505 (68.63%) | 0 | 1,727 |
| Game | 3,105 / 4,832 (64.26%) | 0 | 1,727 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_151BA468` from the live-ELF-pinned queue. Remaining source
screens: 1,598 placeholders, 120 semantic/other and nine unlocated entries.
Next real placeholder is `func_1518F058`, `generated_1BA1D0.c`, 44 words,
not qualified here. `func_1510D8C0` already has a Gfx-pointer definition
missed by the parser and stays a separate uncredited matching case. Keep
the 92-word `func_1509E730`, 862-word `func_1508CAD8` and unmatched 121-word
`func_15169070` C separate. Threshold 4,129 exact C functions: 351 more needed;
goal remains active and incomplete.
