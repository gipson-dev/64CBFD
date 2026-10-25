# View-Plane Query Direct C Match

2026-10-25. Production-qualified, adopted and freshly recounted.

## Recovered Routine

`func_150A2FA4` now replaces its zero-return placeholder in
`conker/src/game/generated_CDE80.c` with a complete semantic query. All 45
body words / 180 bytes emit directly from normal IDO O2/g3, with frame 0x18,
seven original bindings, no alignment tail and **zero new guards**.

- Body VA: `0x150A2FA4..0x150A3058`; VROM: `0xD0454..0xD0508`.
- Interface: `s32 func_150A2FA4(s32 viewIndex, s32 selector)`.
- Use canonical `struct108`, size 0x9A0, and its float fields +0x2F8/+0x2FC/+0x300.
- Mask the full incoming selector to twelve bits. Interpret `D_800D3094` as
  unsigned for the strict `count < selector` rejection; equality, including
  zero/zero, still accesses the selected record. Out-of-range returns one.
- Read the count and view pointer before the bounds branch. Load the record
  table pointer only after that branch, then use the 0x34-byte record stride.
- If the unsigned flag byte at +0x15 has both low bits set, pass the record and
  all three float bit patterns to `func_150A2E4C`. Otherwise return zero.
- Preserve the complete helper result, RA save/restore, branch-likely zero,
  and the unreachable duplicate zero-result word at `0x150A3044`.

Direct table indexing recovers retail's repeated selected-record address
calculation naturally. The first cached selected-pointer form has only 44
words. Two base-pointer forms have 45 words but two scheduling differences;
two direct-index forms match exactly. No rejected form is installed or counted.
Raw direct-C SHA-256:
`260215a1c6f61fc64c84cf88317f2dd59f68379662791ae6f20cdf810c875649`.

The bindings are count HI/LO at +0x14/+0x18, view pointer HI/LO at +0x24/+0x28,
record pointer HI/LO at +0x58/+0x5C and helper R_MIPS_26 at +0x90.

## Types And Callers

The two existing private record/plane views are unified into one compatible
0x34-byte type. The three signed origin halfwords, flag byte, existing +0x17
byte and +0x18/+0x1C/+0x20 words, and four +0x24..+0x30 float fields retain their
offsets. The existing setter receives only three corresponding field renames;
`GeneratedCDE80Plane` remains an alias for the shared private type. All 27
neighbors, including the two `GLOBAL_ASM` bodies and guarded plane helper,
retain their raw and padded code, bindings, pools, extents and addresses.
No shared header or compiler profile changes.

The table symbol stores a pointer. The owner preserves its correct private
pointer declaration rather than importing the legacy inline-array declaration
from `variables.h`. The count retains its canonical signed declaration and an
explicit unsigned comparison. The view uses the existing canonical type.

The aligned whole-ROM scan finds one static JAL at VROM `0xCDC20`, and no
aligned literal target pointer. This does not rule out arbitrary computed calls.
The real 317-word dispatcher `func_150A04D8` reaches this query through command
13 and the `0x9000` reference kind. Its current C source and object remain
unchanged zero-return placeholders; testing the original route does not restore
or credit that caller or qualify the other dispatcher commands.

The existing 38-word plane helper is already guarded-exact. Its unusual use of
the adjusted Y value for the third origin subtraction is preserved, not changed
to the incoming Z argument. Guest tests execute all 38 helper words. Native
tests use a correctly typed opaque provider to check pointer/float arguments
and full return bits. They do not establish portable native execution of the
older helper's signed-halfword origin view, hardware FCSR behavior or gameplay.

## Qualification

Both tools copies pass six fresh pre-install checks, with zero errors,
failures, skips or reuses: primary 34.280 seconds; older mirror 31.360 seconds.
Both shared tool checks pass, in 0.294 and 0.323 seconds respectively.

- 1,756 guest phases cover full-word view/selector values, unsigned count
  boundaries, every flag byte and mixed O32 GPR/float bit passage. All 44
  reachable target words execute; the unreachable 45th word remains literal.
- Native32 O0/O2/O3 with trap UBSan cover all 4,096 indices and all 256 flag
  bytes in valid typed arrays. Eight effective bounded argument/bounds/provider
  controls are rejected. These are exhaustive individual axes and bounded
  combinations, not all possible Cartesian inputs or native alias behavior.
- Twelve phases execute the original plane helper; 108 phases connect the
  full original command-13 caller to the target with nested frames and
  caller-saved clobbers. Other original caller routes remain unqualified.
- Nine independent GNU links exercise seven bindings and signed-low HI/LO
  carries in three layouts, with 81 rebased phases and four guest stack aliases.
- Seventy-two fired target-access fault prefixes agree in complete guest
  state, PC, delay-slot context and dispatched instruction. This qualifies
  emitted guest ordering, not portable C fault semantics or an MMU.
- All 45 word corruptions, seven binding corruptions, six strict-image
  corruptions, six frozen-input mutations and the stale target stub are rejected.

Whole-owner compilation and the actual five-command Make shadow retain the
owner's existing assembly preprocessing/postprocessing. A copied three-command
fixture assumption was corrected without changing production Make. The first
rebase fixture passed an empty anchor map to the existing emitter; supplying
the verified symbol map fixes that fixture. Failed receipts are retained.
The source module, 33 frozen inputs and four qualified artifact identities
remain pinned when reusing the unchanged owner/Make qualification.

The independent full image has exactly 148 changed bytes: 147 body bytes and
one symbol-size byte, from 12 to 180, with zero metadata exclusions. SHA-256:
`81efe331ccd0c1502e0f94b33f884a8111dae4a86dd2d59e42d732b2a8aeba96`.
The pre-existing duplicate `generated_12D630` Make recipe warning is retained.

## Production And Progress

Tools `283d45faaac49a6f0777657d8b082cc05686d6d2` are committed first, with only
the two qualified modules. Actual production Make passes in 15.442 seconds and
reproduces the strict 148-byte image, with zero exclusions. All 6,054 other
linked bodies and all addresses remain fixed. Protected Game data is exact
across 720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each copy passes two fresh installed checks, in 0.520 and 0.805 seconds, plus
four explicitly fingerprinted semantic reuses. These are not six fresh
installed tests. Reuse requires the same complete sealed inputs, module hashes
and four qualified artifacts, plus literal installed source, object and ELF
equality. The unchanged owner/Make evidence is reused only after its source
module, 33 frozen inputs and four artifact identities are checked.

The Native source is manually applied and byte-identical to the proposal.
Adoption verifies all 16,054 inputs with exactly three overrides: target source,
target object and ELF. All other inputs and objects remain unchanged. Adoption
takes 56.219 seconds. The actual adopted Native ELF is streamed without DrvFS
to the fresh GNU matcher; the recount passes in 6.457 seconds and equals the
independent image SHA-256 above.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,798 / 5,505 (68.99%) | 0 | 1,707 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,125 / 4,832 (64.67%) | 0 | 1,707 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Only `func_150A2FA4` leaves the remaining queue. Converted totals are unchanged.
The 75% threshold is still 4,129 / 5,505, requiring **331 more exact matches**.
Queue triage has 1,578 placeholders, 120 semantic/other definitions and nine
parser-unlocated entries. These source-shape screens receive no extra credit.

## Handoff

The next ordinary queue entry is `func_150AFDB0`, owner
`generated_DC6B0`, 45-word retail slot. It is only a queue entry, not a qualified
C recovery. Keep existing-C `func_15014094` and parser-missed
`Gfx *func_1510D8C0` separate.

Baseline consumer `58fbb1845042fb6d8afbd2525e84a77042729a1e`, tools
`ab2eb2e8621bca0d94f1ba9f885d3b3c5a385bab`. Fresh capture normalizes the prior
four adoption overrides, then seals 16,054 current inputs and 1,454 link objects.
Preserve the older mirror's 1,654 pre-existing changed paths and HEAD, plus only
the two owned module additions. No mirror commit, reset or stash is authorized.
Ignored receipts: `conker/build/game-view-plane-query-match/`.

Claude calls: zero; the local compiler/oracle evidence resolves the task.
No host/editor/Release, dependency, global configuration or gameplay changes.
Nothing is pushed. The wider 75% goal remains active.
