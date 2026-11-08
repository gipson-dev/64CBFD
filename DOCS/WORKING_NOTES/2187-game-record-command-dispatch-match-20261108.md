# Record Command Dispatcher Direct C Match - 2026-11-08

`func_150A03B0` now emits all **74 retail words / 296 bytes directly from C**,
with its original **0x28-byte frame**, **zero instruction guards** and no
compiler-profile change. One Makefile row binds its compiler-generated
switch-table reference to the existing `jtbl_8009F550`; the protected table
and its six case pointers remain unchanged.

Production recount: Total **4,256 / 5,513 (77.20%)**, Game **3,583 / 4,840
(74.03%)**, Init **492 / 492**, Debugger **181 / 181**, zero address drift.
There are **1,257** different converted functions and **155** additional
exact functions needed for 4,411 / 5,513 and the active 80% goal. Conversion
rows and denominators are unchanged.

## Interface and recovered behavior

Owner: `conker/src/game/generated_CD860.c`. VA 0x150A03B0..0x150A04D8;
ROM 0xCD860..0xCD988. Three incoming O32 words:

```c
s32 func_150A03B0(u32 identity, u32 command, u32 *record);
```

The unsigned command selects exactly six cases. Negative/high full words
follow the default path; narrowing the selector would be incorrect.

| Command | Helper packet | Return |
| --- | --- | --- |
| 0 | `func_150A2864(identity, 0)` | 1 |
| 1 | `func_150A2864(identity, 1)` | 1 |
| 2 | `func_150A2940(identity, record[2], record[3])` | 1 |
| 3 | `func_150A3444(identity, (s16)record[2], (s16)record[3], (s16)record[4])` | 0 |
| 4 | `func_150A3398(identity, (u16)record[2], record[3], record[4], record[5], record[6])` | 0 |
| 5 | `func_151C970C(status, address)` as described below | 0 |
| Other | No helper or record-field read | 0 |

Cases 0 and 1 do not read the record and permit an ignored null record
pointer. Case 3 reads signed low halfwords at +0xA/+0xE/+0x12, while case 4
reads an unsigned low halfword at +0xA. Case 4 writes outgoing words five
and six at SP+0x10/+0x14; word six is stored in the original JAL delay slot.
No helper result determines this routine's return value.

Case 5 maps `record[2] == 999` to status 2, other nonzero values to 0,
and zero to 1. It sends the full address of record `identity` in the
0x34-byte `D_800D3098` table. A local opaque 0x34-byte record type preserves
that proven stride without inventing undocumented fields. The provider's
existing `(s32 mode, s32 recordAddress)` interface is retained. Native
cases use valid in-array identities; guest execution separately qualifies
full-word identity bits and the original wrapped address arithmetic.

The explicit nested `nonzero ? 0 : 1` expression preserves IDO's original
branch sequence, including its one unreachable literal instruction.
Replacing that expression with the shorter equality expression emits a
69-word alternative and does not match retail.

## Original registration and caller

The pristine aligned census finds no direct J/JAL entry. The entry pointer
is ROM **0x22CFA0**, `D_800884D4[3]` at VA 0x800884E0. Six interior case
pointers are ROM **0x244010..0x244024**, `jtbl_8009F550` at VA 0x8009F550.
They target relative offsets 56, 76, 96, 120, 148 and 192.

The original **26-word** window at VA **0x150AE12C**, ROM 0xDB5DC,
loads the full command from record+4, selects the registered callback from
the header's type nibble, clears only bits 12..15 of the identity, allocates
16 outgoing-home bytes, and invokes the original JALR. High identity bits
remain intact. Its handwritten wrapper preserves RA in S7 and returns the
callback result while restoring SP. **288 connected cases** compare that
full window, call packets, public effects, result, saved registers, SP and
RA. The surrounding parent and helper bodies are not fully emulated.
Graphify was queried for both this target and the next candidate.

## Owner, switch table and metadata

The complete two-function owner has zero compiler diagnostics. Its one
neighbor, `func_150A04D8`, remains unchanged in raw, padded and linked form;
it is still a separate unqualified placeholder. All **18** exported labels
in the full slice are preserved, including the target's six switch labels.

The new private compiler pool is exactly **32 bytes**: six relocation-owned
case offsets plus eight padding bytes. The qualification derives every
case target and checks the isolated target's identical body and exact
GPR-register union. The old register mask is 0x80000004 and the recovered
mask is 0xA303C1F6; CPR masks and GP remain unchanged. All **72** metadata
byte-corruption controls fail closed.

The padded object references the existing protected table rather than
adding a second data owner. The actual three-command Make recipe, using
the exact proposed one-row binding, produces the same padded object as
both independent padders. No inherited guard byte changes. The existing
O2/g3 MIPS2/O32 compiler flags remain unchanged.

## Execution and full-image qualification

Six focused checks pass before and after installation in both tools copies,
with four sequential runs and exact source/dependency fingerprints:

- **1,204 guest cases** cover every command, invalid full-word selectors,
  signed/unsigned field boundaries, 999/zero/other mapping, full identity
  words, ignored null records, helper mutations and hostile clobbers.
- **73 reachable words** execute; the only unreachable word is the literal
  at **0x150A049C**. Original and compiled execution have identical literal
  register, memory, helper-packet and read-trace states.
- **62 memory-fault cuts** compare identical original/compiled prefixes.
- **364 native32 cases per profile**, at O0/O2/O3 with trapping UBSan, detect
  all **13** effective semantic controls in every executable.
- Three independent GNU links and **21** rebased guest executions qualify
  all **10** bindings, including signed-low-half carries for both data
  symbols and all helper addresses.

The independent literal full-ELF predictor permits only the target body,
its expected size change (12 -> 296 bytes), and one explicit three-row
named-definition permutation. Referencing the table earlier moves the
existing group `(jtbl_8009F550, func_15178750, func_15149838)` to order
`(1, 2, 0)`. The predictor derives symbol fields and name bytes from the
frozen predecessor; it rejects unexpected group/name aliases. It does not
copy metadata from the candidate or exclude any byte.

Actual and predicted ELF are equal across the complete file: **273 changed
bytes, zero exclusions**. All **6,052** disassembled entries keep their
addresses; every other function body/extent and named definition is
preserved. Protected data remains **720 owners / 189,088 bytes**, including
all switch and registration pointers, with no changed byte. Seven image
corruption controls reject altered headers, body, size, metadata and data.

Production compiles only this owner, links the predicted image, preserves
the complete progress CSV and passes a fresh matching recount. `make all`
retains the existing whole-ROM checksum failure (exit 2); this direct C
function match does not claim the complete ROM matches. The inherited
Make warning about generated_12D630's duplicate recipe remains unchanged.

Both fresh shared tools smoke checks pass. Three prior shared regression
checks per copy are explicitly reused with identical helper/test hashes.
The sibling's **2,434 pre-existing dirty paths** remain fingerprinted and
preserved; the three new test files run through an isolated overlay.

ELF SHA-256: `893d4b26ca5699639ac50e69c09aa49fc5e7b3e9893a09cffcc658a750593cfc`.
Binary SHA-256: `3eff2635305f362c01d11738fe03116b86723baafca1228e950e32a0b920fb6a`.
Owner SHA-256: `762eb1c82fea8b4fdee3ce7a1b1a66d96ef89320ddd872ce2784e9601bad61fb`.
Guard CSV SHA-256: `944ed3d5d42a8d537e8730f76afa3da81d6806a5e8fd46391a3edd7cdb747f9b`.

## Resume boundary

Next: **`func_1509CF28`**, 75 words/frame 0x50 in `generated_C9EC0.c`;
VA 0x1509CF28..0x1509D054, ROM 0xCA3D8..0xCA504. The zero-return placeholder
remains installed and uncredited. The aligned census finds two direct JALs
at ROM 0x20CBE4 and 0x2105A4, with no entry/interior pointer literals.

Qualify its seven-word loader call, count out-parameter, global-pointer
publication, null output clear, success count-minus-one stores and nested
flag-terminated relocation walk. Repeated count/base reads, output aliases,
low-28-bit masking, final flagged pair processing and post-walk right shift
need explicit guest/native and bounded malformed-input coverage before
adoption. Scratch: `conker/build/game-record-relocation-1509CF28-match/`.

Current receipts: `conker/build/game-record-dispatch-150A03B0-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
has changed-path and old-node-retention evidence; it retains existing
unscanned nodes rather than claiming a new full-corpus extraction. Frozen
host Release artifacts are untouched. The 80% goal remains active.
