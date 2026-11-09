# Game attachment status guarded match - 2026-11-09

`func_1504AF10` now matches its complete **123-word / 492-byte** retail slot
with the original **0x30-byte frame**. Complete semantic C emits 121 words;
**30 expected-word/relocation guards** recover retail register roles and
scheduling, including two additional logical register copies. No compiler
profile, shared declaration, conversion row, data layout or neighbor changes.

Fresh linked total **4,297 / 5,513 (77.94%)**, Game **3,624 / 4,840 (74.88%)**,
Init 492/492 and Debugger 181/181, zero drift, **1,216** different converted
functions. **114** more accepted matches reach 4,411/5,513 and the active 80%
goal. README updates only aggregate rows.

## Source and ordered state

Owner: `conker/src/game_77AD0.c`; VA 1504AF10..1504B0FC,
ROM 783C0..785AC. The frozen US ROM provides the original slot and derived
layout/reference because this converted routine has no standalone retail .s.
The former ECTS/nonmatching comments are replaced with a focused semantic
comment, and local arguments/roles are named actor, force, release, flags,
slot, kind and record. The address-based external function name stays stable.

Snapshot the actor's unsigned halfword at +0x92 into a signed 32-bit local.
Zero flags reject even a forced request. Bit 15 disables ordinary requests;
force overrides that bit. Bits 12..14 select kind and bits 0..11 select slot.
Kind zero calls `func_1504AEF4(flags & 0x7FFF, &slot)` and reloads the actor
halfword afterward. Keep the resolver result full-width and unsigned for its
subsequent shift; do not narrow truth or kind comparisons to one byte.

Kind three uses a 160-byte `struct131` table through **pointer global**
`D_800DBEF4`. Release clears record owner then actor flags. Ordinary update
stores actor-array index plus 100 in record+0x4E; force then clears that owner
and returns. Otherwise mask status with 0x9F, reload the table pointer, OR
0x20, then publish X/Y/Z in order. The unsigned byte view of the signed SDK
status field prevents an arithmetic byte-shift interpretation.

Keep every table access fresh. The SDK actor is 812 bytes and record 160 bytes.
Coordinates truncate to signed 32-bit before halfword narrowing. Y adds the
signed 16-bit view of actor+0x90 using float32 addition. Portable native cases
stay within the actor array and defined signed-conversion range. Sparse
negative/wrapped indices, physical table/actor/stack aliases and overwritten
incoming homes are guest-only instruction tests.

## Guard provenance

All **121 compiler words are used once**. Retail preserves two independent
OR-with-zero copies at output words 16 and 17, while IDO coalesces the category
and masked identifier into A0. The normalization reorders the existing mask,
branch and argument-address setup around those copies; it adds no memory
operation, call, literal, frame adjustment or algorithm.

The two CSV insertion sites are after raw words 13 and 14 (offsets 0x34 and
0x38). Because the existing mask is moved as part of the permutation, the
CSV-inserted words themselves are an existing ANDI and one copy; the other
copy is represented by a replacement. They are **not two NOPs**, and should
not be described as two literal inserted copies in the CSV.

Provenance checks preserve opcode/function/shift, floating operation,
constant/field/address immediate, relocation identity and mapped branch
destination for every retained word. Both ordinary full-owner padding and
independent target-only generated padding produce the same retail payload
and relocations. All 30 stale expected words plus a stale relocation are
rejected by each padder; missing/corrupt insertion shapes fail the exact-body
gate. Every one of 121 raw payload corruptions is rejected.

## Resolver and caller boundaries

The actual seven-word `func_1504AEF4` is **already retail exact**, always returns
zero and does not write the output slot. Its matching zero-return C is not an
unfinished recovery. Tests execute those real words in 36 direct cases,
24 independent rebases and 72 caller-window cases. Scripted nonzero and wide
returns qualify the retained caller interface as **extension cases**, not
observed behavior of this resolver. The post-resolution actor halfword store
is reachable only through those scripted returns; preencoded kind-three
record updates are naturally reachable with the real resolver unchanged.

The whole-ROM census finds exactly two JALs, at ROM 78000 and 8E440, and no
aligned literal entry pointers/direct jumps. Their owners `func_1504A730`
and `func_15060F28` remain production placeholders: symbol sizes 12 and 16
bytes, padded spans 424 and 176 words. The latter's empty typed void body
still stores its two argument homes before returning. Current linked target
JALs are zero. This change preserves those callers and gives them no recovery
credit.

Original 4- and 6-word caller windows pass **3,378 executions** across raw,
normalized and retail bodies, including actor in S0/S1, force zero/one,
release zero, four rejection cases and all ten original static words. The
branch's real delay-slot actor move is checked. Complete parent algorithms,
opaque provider behavior and gameplay/hardware acceptance are not claimed.

## Validation and production

Freeze **669 inputs** from consumer 56cff3b2 and mounted tools 5a4270fd.
Six fresh focused checks pass in each tools environment before and after
installation. The sibling environment uses an ignored read-only overlay for
the six new modules, with actual helper origins/fingerprints recorded; the
sibling checkout's **2,439** preexisting dirty paths stay unchanged.

Guest checks: **551 per body / 1,653 executions**, complete 121/123/123-word
coverage, all 256 status bytes, wide mode/return words, slot boundaries,
callbacks changing actor/table pointer, four physical alias classes and
incoming-home mutations. Native SDK32 checks at O0/O2/O3 cover all 65,536
packed flags in four force/release modes (**262,144 cases per profile**),
all 26 actors, full actor/record canaries and independently generated scripted
callback cases. The flag sweep uses the actual zero-resolver C.

Twelve semantic controls are effective natively and under IDO. Three additional
guest-only controls expose merged status stores, cached table pointers and
reversed coordinate stores. Four independent GNU links test low halves
0000/7FFC/8000/FFFC with 16 executions. Six image corruptions cover header,
target, resolver, retained private overflow, protected data and EOF. No compiler
or interpreter error is counted as a semantic witness.

All **57 owner neighbors**, pools and six register-metadata words stay fixed;
all 6,051 linked function addresses, including 6,047 canonical addresses, stay
fixed. Actual five-command Make reproduces the predicted 58-function owner.
Production rebuild compiles only the intended owner with the existing O2/g3
profile and has no new C diagnostics. Strict whole-image prediction permits
only the 492-byte target slot and symbol-size 484->492 update: **392 changed
bytes, zero exclusions/unexplained bytes**. Protected data is identical:
189,088 bytes across 720 owners. Guard history remains an exact byte prefix.

Shared smoke checks run fresh in both copies; three unchanged regression
receipts per copy are explicitly reused by exact source/helper fingerprints.
Zero legacy actor suites are claimed replayed. The inherited duplicate
generated_12D630 Make warnings and normal all-target checksum exit 2 remain.
The project as a whole still has unmatched routines.

The scoped Graphify AST refresh verifies old-node retention outside changed
paths and all 54 active C labels plus four assembly neighbors. An existing
disabled `func_1504B0FC` draft shares a graph label with its active stub;
source-position ambiguity remains recorded separately. This is not a
full-corpus semantic extraction or evidence of linked caller restoration.
The refresh explicitly retained 31,816 old nodes from 3,754 existing files
outside the current scan corpus. It produced 59,577 nodes and skipped the
HTML visualization because that exceeds the configured 5,000-node limit.

## Reproduce and resume

```sh
python3 -m unittest tools.tests.test_game_attachment_status_1504af10_match -v
```

Private receipts live in `conker/build/game-attachment-status-1504AF10-match/`:
qualification, guest/native/control/caller, both preinstall/installed replays,
production, graph-retention and post-commit JSON, plus `HANDOFF.md`.
The fixture requires the recorded prepared US input/toolchain and frozen
predecessor artifacts; it fails closed on unknown source, scope or bindings.

Next: `func_15169070` in `conker/src/game_1944C0.c`, retail 124 words. It is
semantic C for a column/row node traversal with optional callbacks and a
nested next-node stack. Inspect the original frame, pointer reloads, callback
mutation and traversal order before fitting. No new candidate for it is
installed or credited here. Keep the separate 1510D404 compiler investigation
private and uncredited until its remaining gates pass. Routine Claude calls: 0.
