# Two-vector effect callback - direct C match

Verified 2026-10-28. Restore func_1514F308 in generated_179F30:
VA 0x1514F308..0x1514F3CC, ROM 0x17C7B8..0x17C87C, 49 words / 196 bytes.
The normal O2/g3 profile emits every original instruction directly, with a
96-byte frame, seven relocations and no word guards. The retail symbol name
is retained and the comment describes its recovered type-five effect behavior.

## Recovered behavior and interface

The interface is void func_1514F308(u8 *owner). Copy the two three-float presets
D_800A5970 and D_800A597C into distinct local vectors, then call func_15160CDC
with the original owner, type 5, both copies, D_800A5E58, kind 2, duration 300,
four 255 color values, flags 1/0/0, slot 255 and context 1. The callback result
is ignored. Null owners still reach the provider, which handles the null case.

The local copies occupy SP+0x54 and SP+0x48; the saved return address is at
SP+0x44. The call at +172 stores the float argument to SP+0x10 in its delay
slot. Retail vectors are (52, 0, 80) and (52, 0, 353); the float parameter has
bits 0x3CC08744. Keep the structures and the 16-argument provider declaration
next to the recovered body to preserve unrelated declaration and diagnostic
ordering. No shared header, Makefile or profile change is required.

All 77 other compact and padded owner functions, their relocations and
constant pools are preserved. The owner contains no GLOBAL_ASM directives.
The actual three-command Make recipe includes the generated padder.
The selected function has no diagnostics. Four pre-existing Warning 712
pointer/integer messages at owner lines 152 and 190 are retained verbatim
apart from the compiler's source filename. The full Make build also retains
the unrelated duplicate generated_12D630 recipe warning.

## Original callback routes and provider

The aligned ROM census finds no direct target calls and one pointer literal:
ROM 0x22F5C0 / VA 0x8008AB00, index 36 of the 58-entry D_8008AA70 table.
The 109-word parent func_1514D15C invokes this table through three routes.
48 connected cases cover all 50 words of the windows 0x1514D230..0x1514D270,
0x1514D270..0x1514D2AC and 0x1514D2AC..0x1514D2F8. They verify selector gates,
owner passing, ignored results, both stack phases and provider mutations.
This qualifies those windows, not every command in the parent. The parent C
placeholder remains uncredited; no source call edge is invented for it.

All 85 original instructions of func_15160CDC execute across 208 cases:
64 connected callback cases and 144 additional provider argument cases.
The provider constructs a 40-byte payload, preserves its padding, handles
null owners and allocation failure, and copies successful payloads to the
returned object. Cases cover signed duration boundaries, byte flags, owner
mutation during allocation and output aliasing the owner. The deeper
func_151602C0 factory and memcpy are explicitly bounded providers.
The provider's C placeholder remains uncredited. These are original-instruction
and interface checks, not an allocator or gameplay completion claim.

## Qualification and production

Both tools copies pass eight fresh canonical methods and shared tools checks.
Each then passes two fresh installed checks, with six semantic methods reused
only after exact frozen-input, module and artifact fingerprints agree.

- 4,228 guest cases visit all 49 target words and compare complete state,
  memory, access traces, both snapshots and all sixteen arguments across
  retail, raw C and padded C. Arbitrary float bits and three stack-alias
  layouts are guest checks; portable C stack aliasing is not asserted.
- 81 fault-prefix triples and 183 integrated-provider prefix pairs preserve
  the executed state and traces, including branch-delay behavior.
- Native32 O0/O2/O3 each pass 65,536 cases with trapping UBSan, finite values,
  quiet NaNs, copied-vector mutation and eighteen effective negative controls.
  Eighteen IDO-compiled controls independently change each argument, pass a
  global vector instead of a copy, or incorrectly skip null-owner calls.
- Three GNU layouts pass 72 guest cases and exercise HI16/LO16 carries.
  Three raw/binding corruptions and 21 full-image corruptions are rejected.
  The actual generated padder reproduces the qualified object exactly.

The qualification seal covers 16,407 paths and 382 focused inputs. Production
reproduces the independently predicted entire ELF: 226 changed bytes,
comprising 149 code bytes, 36 symbol bytes and 41 string bytes, with zero
exclusions. Symbol changes include the target extent 12 -> 196 and four
closed GNU symbol/string ordering permutations. The predictor reconstructs
these groups from frozen predecessor definitions rather than discarding
metadata. Every named value, type, section and extent is preserved except
for the recovered target extent. ELF headers and section geometry are fixed.

All 6,056 function addresses, 6,055 other linked bodies and 720 protected Game
owners / 189,088 bytes remain unchanged. The guard manifest, other objects,
retail layout and conversion inventory are unchanged. No guard is added.

Private fixture fixes preceded the canonical runs: the effect oracle needed
its own symbol dictionary; native negative bodies needed explicit unused-local
casts. GDB traced an O3 harness crash to a misaligned SSE store in the custom
startup path. Applying the existing force_align_arg_pointer startup convention
fixed all three native profiles without changing production C or weakening
checks. The original diagnostic artifacts are retained.

| Artifact | SHA-256 |
| --- | --- |
| Raw C and original relocatable body | 2b6c74eddcd215c26450367f9b19426ca6d2c17e849949875cdf8c5bfa8be3f0 |
| Linked retail slot | 26abbf6a80fe4e65989a2f4b4723ff98645a76423801d553463d5d86daa35724 |
| Adopted owner object | aecc8f7f6f4726eefc755d82b847e26b19fc2c40201b384cfaa8dbc63aaf4306 |
| Adopted ELF | 4f2b9d0c0304fa7e5ce89b9d668179f2c30532a6e406b34d6614a07f729be6af |
| Unchanged guard manifest | 91cfc61697b2f874f74475c5dadac1faec1f2e3c4f2a515d593b62d15b71ba03 |

## Bank and measured progress

Predecessor consumer: edf1b6229a9a57d392bf73341ed7d6d495a0b848.
Tools committed first: a3fb6dab8c63cf0e396763238e0632279ee7c3d2.
The consumer commit records the source, tools pin and measured documentation.
No push is performed. Preserve all 1,802 inherited older-mirror dirty paths
and the three new qualification modules; do not reset or commit that mirror.
Routine Claude budget/calls: zero. No emulator or gameplay claim is made.

| Section | Byte-exact C | Address drift | Different |
| --- | --- | --- | --- |
| Total | 3,865 / 5,506 (70.20%) | 0 | 1,641 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,192 / 4,833 (66.05%) | 0 | 1,641 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

265 more exact functions are needed to reach 4,130 / 75%. Remaining source
shapes: 1,512 placeholders, 120 semantic/other and nine unlocated. Only this
callback receives new credit. Keep func_1514E920 parked and uncredited.
Next inspect func_151838B0; screening alone earns no credit.

Retained evidence: conker/build/game-two-vector-effect-match/ contains the
preparation, canonical and installed receipts, sealed production/adoption
proofs, canonical-function-views.json and 75-percent-queue.json. The final
handoff records the consumer commit, scoped AST refresh and independent audit.
Root README changes only the aggregate status rows.
