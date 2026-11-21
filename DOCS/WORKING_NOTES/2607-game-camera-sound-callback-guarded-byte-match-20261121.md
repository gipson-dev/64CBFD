# Note 2607: Camera sound callback guarded byte match

Date: 2026-11-21. Consumer baseline `6b3788742f57ac768ab027ccf7c837505b74765e`;
tools baseline `0d9cb61d9f34043f46007d256265371fdca5163f`. Qualified tools commit: `03694d0a53897ad3ab52c6e7cc05fb899ea00a1d`.

`func_151277B0` replaces its zero-return placeholder with the complete camera
sound callback. Its **124 words / 496 bytes**, **48-byte frame**, saved RA,
incoming argument homes and four relocation sites are recovered. **42 checked
word guards** normalize GPR allocation only; there are **zero insertions or
omissions**. All **44 neighboring functions**, pools and five existing warnings
are unchanged. This is a guarded match, not a claim of direct raw-C identity.

Production recount: **4,591 / 5,528 (83.05%)** total, **3,918 / 4,855 (80.70%)**
Game, zero address drift and **937** still different. Init 492/492 and Debugger
181/181 remain exact. **108 more** matches reach 85% at this denominator.
Converted rows are unchanged because the previous placeholder already counted
as C. The root README receives only its two aggregate matching rows.

## Recovered behavior and interface

Owner `game_14FF90`; VA `0x151277B0..0x151279A0`, ROM
`0x154C60..0x154E50`. The callback receives a sound record, five unused pointers
to mix values, and a `u16 *` sound ID. It copies the current primary actor's
truncated coordinates to the sound record. The low 24 bits of the secondary
actor's float product at +0x174/+0x178 are compared with the previous packed
value; its upper byte counts elapsed ticks. The subtraction is unsigned and
the original threshold is strictly greater than 100. Unchanged values reset
the counter. Different values with a prior counter of at least ten select the
stopped transition. The packed count/value is stored before any release call.

Actor state other than 2 returns 1. Active state handles sound IDs 0x622,
0x61C and 0x61D, releases a nonzero handle through `func_100111C8`, clears the
handle and flag 0x80 in the original order, and returns zero. Provider changes
and legal halfword aliases remain visible to subsequent reloads.

Private `CameraSoundRecord14FF90` and `CameraActorScale14FF90` layouts name the
measured record fields and the two floats currently hidden in SDK padding.
The sound record retains its complete 0x30-byte extent. Shared headers and
compiler profiles are unchanged. Native assertions verify private offsets
and extent; a separate SDK32 check verifies camera +0x3D0/+0x3D4 and actor
coordinate offsets. No volatile accesses, explicit register names or assembly
body replace the recovered C algorithm.

## Allocation proof and focused validation

Raw payload SHA256:
`438fb7bad428a7ad6cb61f920bdcddfee64a709246cf3d74fe540b842f930007`.
The initial extra packed snapshot produced 125 words/frame 56. Removing that
redundancy and initializing history before the float product recovered 124
words/frame 48. Further type, mask, union and register-hint screens did not
recover the remaining allocation. The selected source retains defined union
bit inspection; the pointer-pun screen is not adopted.

A decoded symbolic lockstep check covers **all 74 acyclic control-flow paths
and all 124 words**. Each changed bit belongs to a GPR operand field. Branch
predicates, ordered memory reads/writes, helper arguments, stack balance,
return values and preserved registers agree. Memory-prefix tokens preserve
arbitrary alias ordering; the one-argument release call introduces identical
arbitrary memory and caller-clobber effects. Four deliberately broken register
changes are rejected. The proof's float operations are abstract and identical;
independent C/native and provider behavior remain separate gates.

Independent guest execution passes **2,242 cases per stream** for original,
raw and padded bodies, visits all 124 words, and checks complete public RAM,
private bytes, ordered accesses and preserved ABI state. **141 memory-access
fault prefixes per stream** also agree. Four instruction controls fail. Cases
cover all actor-state bytes, count/delta boundaries, tick wrap, signed zero,
coordinate narrowing, provider mutations and sound-ID/handle/coordinate aliases.
Internal caller-saved register identities may differ in raw C; they are not
misreported as literal register equality.

Native checks pass **2,241 cases each at O0/O2/O3**, with strict aliasing, UBSan
traps and seven effective source controls. They use actual SDK camera/primary
actor objects and separately typed private record/secondary objects. State may
legally alias the sound ID, handle or coordinate halfwords. Float-to-short
inputs stay representable; guest-only wider narrowing is separate evidence.
Native tests make no private-frame or unrestricted C alias claim.

## Original registration and dispatch boundaries

A fresh original-ROM census finds one adjacent callback-address construction
at `0x15126B08/0x15126B0C`, no direct JAL/J and no aligned loaded-pointer literal.
The original `func_15126378` passes that pointer to `func_1000FA64`; original
constructor instructions store its callback argument at sound record +0x14.
The **20-word registration window** agrees with the sealed original assembly.
However, **the registration parent remains a C placeholder**. That window is
original reference evidence, not current linked gameplay or a parent recovery.

The Init dispatcher `func_10011624` is literal in the frozen ELF. Its original
**24-word window at 0x10011848** passes **128 cases per stream**, exercising all
seven argument addresses, JALR delay-slot record argument, both callback return
values and the corresponding deletion or handle/flag reload path. The stack
sound ID at caller SP+0xA6 and all five unused mix locals are compared against
the independent model. Missing seventh argument, lost delay argument and
ignored return controls fail. Deletion uses a bounded provider contract; no
complete constructor/outer-dispatcher or hardware acceptance is claimed.

Six GNU links cover original bases and code+0x10010/data+0x18020, including
HI16/LO16 carry. Raw links match independently bound raw instructions; original
and padded links match retail. The isolated raw target has exact payload and
binding identity before linking; unused raw-owner data is outside that scope.

## Production audit and checkpoint

The natural mixed GLOBAL_ASM recipe runs five commands with the existing
O2/g3 profile and reproduces the complete qualified object. The strict image
prediction covers **6,051 slots**, **363 changed bytes**, **zero exclusions**
and no unexplained differences. Only the target body and symbol size, **12 to
496 bytes**, change. All **189,088 protected Game-data bytes / 720 owners**
remain exact. Production ELF SHA256: `502047caaafb0482656ad227fa97397eab9ca44c1e4056e7249c9c70b99e0ae7`.

Every existing guard-file byte is preserved and only 42 owned rows are appended.
The first private CSV rewrite normalized mixed line endings; it was rejected
before adoption. Exact prefix preservation replaced it, and both configurations
were freshly requalified. Public committed modules are authoritative; the
earlier private package generator predates this preservation correction.

Five focused checks pass before and after installation in both configurations;
shared `make tools-check` passes. Eight tools files are committed before source
and guard adoption. The private hybrid has 1174 files; the real
dirty sibling HEAD/status and 351 dependency hashes
remain intact. The production audit checks 2304 frozen inputs.
Earlier unchanged broad suites are reused by fingerprint, not claimed fresh.

Graph updates retain old IDs and qualification metadata. Native smaller-corpus
refusal plus serial scoped extraction is not a full-corpus re-extraction. The
available host scene configuration/input is inspected read-only; no source
import or host parity is inferred. No Make/profile/shared-header, host/Release,
ROM/save changes, push or Claude calls. The 85% goal stays active. Next candidate:
`func_15127520`, the adjacent 164-word/frame-72 sound callback placeholder;
its own ABI, semantics and allocation must be qualified separately.

```sh
python3 -m unittest tools.tests.test_game_camera_sound_callback_151277b0_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```
