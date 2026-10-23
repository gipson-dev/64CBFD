# Recursive Node Identifier Search Direct C Match

Date: 2026-10-23. Predecessor consumer `1501f2e7`, tools `0723f62`.
Qualification tools committed first as `24b7f918`.

## Recovery And Interface

Recover `func_1514D4B8` in `conker/src/game/generated_179F30.c`:
VA `1514D4B8..1514D564`, ROM `17A968..17AA14`, 43 words / 172 bytes,
frame 32 and four bindings. Keep the address-based name, add a purpose
comment and preserve original `conker/asm/179F30.s`.

The actual interface is `s32 (s16 index, s16 wanted)`. Test signed -1 before
equality, return one for an equal non-sentinel identifier, recursively search
node halfword 3 before halfword 2, and short-circuit on success. Reload the
table entry after the first recursion; caching its pointer changes observable
guest behavior under the qualified stack/table alias. Retain the existing
`extern s16 *D_8008ABE8[]` declaration. No header, caller, global type or
compiler-profile change is needed.

All 43 words emit directly under normal O2/g3, without word guards, folds or
insertions. Retain the naturally unreachable duplicate zero at `1514D550`
(word 38 / +0x98); the other 42 target words are naturally visited.
Bindings are HI16/LO16 `D_8008ABE8` at +0x48/+0x4C and self-calls at
+0x60/+0x80. Raw C text SHA-256:
`e34ed1995b70eb6a629ab804178b12d730e7267a9c0d02fcb324ef1ca8d411be`.

## Actual Data And Recursion Limits

`D_8008ABE8` is VA `8008ABE8`, ROM `22F6A8`, in `22F650.rodata.s`.
Verify all 28 non-NULL pointers, the two trailing zero words and all 28
eight-byte node prefixes against both original ROM and current ELF. Node
prefixes live in `24A920.rodata.s`; their first two halfwords are opaque
metadata, and links are signed halfwords at +4/+6. Do not invent domain
names such as child/sibling or treat the trailing NULL words as valid roots.

The original data contains a real self-link: node 10, `D_800A5F3C`, has
prefix words `00010000 FFFF000A`. Of 957 ordered query screens, 925 terminate
and 32 enter a cycle before matching; finite depth reaches 11 / 47 calls.
Do not add a cycle guard. Qualify cyclic executions with fired bounded guest
prefixes, exact 32-byte per-level stack growth and branch-delay PC identity,
not a termination claim. Both observed callers initially pass node[root][2];
none of the original 28 link-2 fields points to 10. This is a fact about the
original fixtures and valid roots, not proof for all runtime mutations.

## Original Caller Prefixes

The aligned ROM scan finds exactly four JAL sites: ROM `55A08`, `17A8D8`,
`17A9C8` and `17A9E8`; the last two are self-recursion. No literal target
function pointer is present. Both larger current C callers remain untouched
zero-return placeholders, with no new conversion or actual-C-caller credit.

- Same-owner `func_1514D3B0`: qualify its original 36-word entry prefix
  `1514D3B0..1514D440`, original frame 56 and naturally reached continuations.
  Preserve the full incoming argument home, signed root narrowing, S4/S5,
  owner +0x2F4 record, signed record +0x1C, root-equality bypass, JAL delay
  loading link +4, false BEQL list advance and success's late wanted reload.
- `func_150265CC`: qualify its original 22-word prefix
  `15028510..15028568` within the original 0x750-byte frame. Preserve the
  branch-likely owner load/selector-byte store, unsigned selector cache,
  NULL-list branch, root-equality bypass, JAL-delay full record-pointer home
  at SP+0x544 and unconditional return reload. Preserve its complete current
  eleven-function object in `generated_50D80.c.o`.

All 58 prefix words are visited across 5,568 caller phases. These are bounded
original-machine caller connections, not full-parent C or gameplay acceptance.

## Qualification

Both tools copies pass eight fresh pre-install tests, then two fresh installed
checks, with zero errors/failures/skips. Explicitly reuse six unchanged
behavioral checks only under strict source, raw/padded object, caller,
table/node data, guard and complete-image identity. Both shared tools checks
pass. Reuse existing MIPS oracles, IDO compiler, native32 and GNU-link helpers;
do not install dependencies or edit shared oracles for this target.

- 2,756 ordinary guest phases and 40 sparse phases cover signed narrowing,
  sentinel priority, recursion order, early success and full incoming homes.
- 2,111,717 defined native32 cases per O0/O2/O3 build include every 16-bit
  equal-argument pattern and the 925 terminating actual-data queries. Typed
  fenced objects and trap UBSan pass; twelve wrong-C controls fail effectively.
- 1,016 fired regular access prefixes, 1,472 cycle prefixes, twenty NULL-root
  fault cases and forty private stack/table alias prefixes compare literal
  state, attempted access, stack growth and PC/delay identity. NULL roots
  28/29 fault at entry +0x58 when unequal, but equality can return first.
- Eighteen independent GNU links and 126 rebase phases cover original/raw/
  padded code, HI16/LO16 carries, wrong-order and cached-pointer controls.
  Two compiled wrong-order controls fail by non-stack read order; two cached
  pointer controls fail by returning where original code enters a cycle prefix.
- Twelve raw/binding corruptions and eight strict-image controls are rejected.
  The old zero-return stub fails effective semantic cases.

Native evidence is limited to defined typed/disjoint 32-bit objects and
terminating calls. Invalid arrays, NULL dereferences, guest stack aliases and
cycles are guest-only evidence, not portable C fault semantics, native64,
hardware/MMU or host acceptance. Preserve emitted cyclic behavior without
claiming that arbitrary cyclic native execution terminates.

## Production And Preservation

The actual three-command compile/pad/assemble recipe reproduces the qualified
complete owner object byte for byte, including all 77 neighboring functions,
pools and extents. Independent linking and production Make agree on exactly
123 changed ELF bytes: 122 target-code bytes and one symbol-size byte, with
zero exclusions. The original slot and every address remain fixed.

ELF SHA-256:
`29005af947e9be05f68f3d23cd5f1c4a1fee9dbfd41a9e8b6d94af3a0fde28d5`.
Padded owner object SHA-256:
`380203df6b429aeb3bf92095973af7a1b5dee48cf55f63242c59ec84590dabb9`.
The entire guard CSV is unchanged, SHA-256:
`3d9cc32d7a0b09feb9d5ef64850e01f87d22b65d4afe329d201b525158382292`.

Preserve all other 6,054 bodies, all 6,055 function addresses and all 720
protected Game-data owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Seal and recheck 15,890 files, all 1,454 linker objects and thirty focused
input pins. Advance the preceding checkpoint's four adopted inputs; this
checkpoint has only three mutable manifest entries: source, object and ELF.
Promote the linker script and progress CSV unchanged. Keeping the guard CSV
old for bounded Make is justified by whole-file byte identity.

A private pre-install export left a truncated native manifest; its cause
is not established.
Adoption rejected it before any generated output promotion. Recover the
complete manifest from the independently validated sealed production archive,
recheck every live input, and then promote. A premature baseline recount is
not progress credit; rerun the standard matcher against the adopted live ELF.

Commit primary tools first. Preserve all 1,572 preexisting dirty paths and
the HEAD of the older independent tools mirror; add only the two identical
target tool files. No push or host-port changes.

## Handoff

Fresh standard matching against the adopted live ELF reports total
**3,750/5,505 (68.12%)**, Game **3,077/4,832 (63.68%)**, Init 492/492 and
Debugger 181/181 exact. Zero drift; 1,755 different. The 75% threshold stays
4,129 exact, requiring **379 more matches**. The refreshed queue has 1,624
placeholders, 122 semantic/other definitions and nine unlocated entries.

Next `func_15193234` in `generated_1BFDD0.c` is queued only, 43 words / 41
placeholder differences. Establish its interface, complete semantics and
caller behavior before qualification or installation. Retain the 862-word
`func_1508CAD8` stub in the queue. README changes only Total/Game matching
rows and the verification date. Post-commit Graphify completion, fresh-output
provenance and every-old-node retention remain private audited receipts;
do not claim a clean full-corpus extraction. The wider goal remains active.
Host Release, saves and configuration remain frozen and untouched.
