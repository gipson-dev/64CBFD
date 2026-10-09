# Game Record Height Response Match

Verified locally: 2026-10-09. Complete **func_15148BA4** is recovered as
semantic C, **143 words /572 bytes /frame0x58**, linked byte-exact with
**three expected-word guards**. Raw C retains three differences; do not
describe this as direct compiler matching. No filler, inline assembly or
profile override. Existing exact assembly is credited to C without changing
any byte of the guest ELF.

## Baseline And Scope

Parent **8143eb97d322089a5b2e2b9f44efc6e03d6efe75**, mounted tools
**9d3bfa0ac0ccdd351a63584d63914e0f2537dee3**, both clean initially.
Older standalone HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, both
independent dirty-file hashes and **68 pre-existing status lines** are
preserved. One Codex writer, zero Claude calls; local evidence settles the
complete source/ABI/private-lifetime case without a second reviewer.

Owner [generated_175250.c](../../conker/src/game/generated_175250.c),
[complete retail assembly](../../conker/asm/nonmatchings/generated_175250/func_15148BA4.s),
VA **0x15148BA4..0x15148DE0**, ROM **0x176054..0x176290**.
Actual protected **D_8008A3E0[3] at0x8008A3EC** points to this routine.
Direct caller is the banked 97-word payload dispatcher, entered by the
100-word timer through **D_8008A200[1] at0x8008A204**.

Before-source SHA-256:
**0914549204a264e4b3593b5ad5fe3e4dc98d66a94c821ea3891ac5b9ec5f5c7d**.
Before/after ELF **3,261,160 bytes**, SHA-256 unchanged:
**9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e**.
Before guard SHA-256:
**a75754c128d68f1a901860e0f73f6f5ac87545d485f47bac76cedc52c3e0d748**;
after exactly three rows append, SHA-256:
**1d9d7c6c3c0f0905aa40cd9f58c1d39c2aa46ec1aad9c8e7f0d097cdca8fc030**.
No changes to original assembly, layouts, compiler/profiles, shared helpers,
OGL, runtime, saves or editor. Original baseline is captured once, not reset.

## Complete Contract

Capture payload+records from actor+0x98/+0x94 and signed head+0x2E.
When payload+0x18 flags&7, copy the signed start record's XYZ words to
private **SP+0x40..0x4B**. Integrate backwards, always at least one record,
wrapping negative index to live unsigned count-1. Preserve 20-byte records,
live signed start reloads, four time loads and ordered float32 gravity,
updated velocity-Y and XYZ updates. No invented empty exit or loop bound.

After integration, read live flags&0x17. Compare current Y strictly below
private old Y; equality/NaN bypass the query. Form **SP+0x34..0x3F** from
current X, old Y and a fresh current Z/start read. Query func_15046C80 with
selector0, freshly loaded current Y word bits and result at actor+0x60.
Its existing typed HeightResult71820 layout is reused exactly. The query
can mutate result kind, height, selectors/tables and public pointers.

Reload captured payload after the query. Result kind at actor+0x7D selects
payload+0x24 /D_8008A450 for kind3, otherwise payload+0x23 /D_8008A430.
Zero selector returns1. Six arguments are actor, old XYZ float word bits,
fresh result height and actor+0x64; fifth/sixth arguments occupy SP+0x10/14.
Callback zero returns0; any nonzero word, including negative, returns1.
Query failure, no downward movement and unselected response return1.

Flags&7 and flags&0x17 are intentionally distinct: bit0x10 alone can consume
an uninitialized old snapshot. Preserve the emitted retail private lifetime;
do not guess zero coordinates or expand the snapshot gate. Native tests
exclude those uninitialized reads and cyclic ring inputs. Emitted tests
seed prior stack and observe bounded invalid prefixes. These are not
portable-C safety or hardware/gameplay acceptance claims.

## Fitting And Closed Guards

Initial full source: **141 words /frame0x60 /97 differences**. Indexed
integration, top-of-loop decrement and callback-zero failure with common
fallthrough return recover **143 words /frame0x58 /three differences**.
Ordinary O2/g3 remains selected; O2 has26 differences, O1/g3 and O1 emit
192 words/frame0x48 with188 differences. Typed/byte/integer pointer forms,
selector widths, register hints and query-struct forms do not remove the
remaining three differences. No broader compiler conversion batch.

[Guard manifest](../../conker/retail_word_patches.us.csv) appends only:

| Offset | Raw | Retail | Proof |
| --- | --- | --- | --- |
| 0x48 | 0x016A6021 | 0x014B6021 | Commutative record-position pointer addition |
| 0x170 | 0xAFA80054 | 0xAFA80050 | Save captured payload in query JAL delay slot |
| 0x178 | 0x8FA80054 | 0x8FA80050 | Reload same payload in result branch delay slot |

Both private carry slots lie within the unchanged 88-byte frame and outside
saved registers, snapshot40..4B, query34..3F and argument homes00..1F.
Change store+load together, not their order/value/register/branches. The
routine never otherwise addresses either carry slot. Stale expected-word
tests reject each changed word; unrelated words are untouched. Seven
original relocations remain: time HI/LO, query JAL, two response table HI/LO
pairs. Guards contain no replacement relocation or hard-coded call target.

## Fresh Qualification

[Candidate driver](../../tools/experiments/game_record_height_response_candidates.py)
and [nine-test suite](../../tools/tests/test_game_record_height_response_match.py)
reuse existing compiler/parser, float, MIPS, native32, copied-owner and
padding helpers. No shared helper edits.

- **4,194 cases /12,582 executions**, all byte-wide signed cursors, unsigned
  count, flags, kind and both selectors; zero/nonzero/negative response
  results, query mutations, scratch-register and eight argument-home clobbers.
  All **142 reachable words** exercised; retain natural unreachable index118.
  **732 bounded prefixes** do not add a production limit.
- Raw/normalized/retail agree on public memory, calls, ordered accesses and
  returned state; normalized/retail agree on complete registers/FP/memory/
  events. Raw private memory differs only inside carry slots50/54.
- **144 snapshot cases /432 executions** qualify old-stack finite, signed
  zero, infinity/NaN Y patterns, two stack phases and both table kinds. The
  distinct snapshot and response gates are measured, not assumed.
- **333 missing-public-byte triples**, **37 aliases /111 executions**,
  captured-pointer/live-field order and global-time overlap. Fault prefixes
  qualify emitted order, not portable C or private stack-alias semantics.
- **Eight effective compiled negatives /eight samples**: cursor/count
  signedness, expanded snapshot, wrong response mask/kind/height and negative
  result rejection. An ordinary start255 cyclic sample was ineffective;
  the count0/head0/start255 return witness discriminates it correctly.
- **50,689 actual native32 defined cases**: **49,153 finite head/count pairs**
  plus **1,536 selector/kind/result cases**. Full **256 actor /128 payload /
  11,200 record-byte canaries**, live query-produced kind/height and actual
  six-argument C calls. Local GCC maybe-uninitialized suppression applies
  only to the deliberately retained candidate; IDO owner has no diagnostics.
- Ten asm-postprocessed neighbors, pools and relative relocations unchanged;
  actual padder emits **572 bytes** without filler. Four independent GNU
  links, **96 cases**, rebase entry/time/query/both tables including HI/LO
  carry and JAL-region boundaries.
- **16 connected cases /48 executions** use complete **100+97+143+9 words**
  through actual tables8008A204/8008A3EC/8008A434, including the complete
  banked **func_15148EF8** response body, not a response hook. It naturally
  changes payload selector to4; caller publishes actual record XYZ. Height
  query remains a bounded hook. Other response bodies/failure cleanup open.

Pre-install **nine tests pass in73.456s**. Fresh normal rebuild succeeds in
**283.986s**, retaining **489 existing CFE warnings and two duplicate recipe
warnings**. No focused candidate/owner diagnostics. Every rebuilt ELF byte
is identical to its original baseline; one asm -> c conversion row and
exactly three appended guard rows. No symbol/metadata audit exception.
Final **nine post-install tests pass in69.618s**, after the build is terminal.
All **6,058 slot bodies/addresses/extents** and protected data/symbol/metadata
bytes remain unchanged, not merely the target or an audit-exception subset.

Fresh **35 shared tests pass in16.902s**, `make tools-check` and mounted
`check_project_tools.py` both pass. Prior unchanged neighbor-suite receipts
are reused explicitly, not fresh reruns; full ELF identity is their basis.
Documentation validation: **144 documents /4,252 relative links /zero broken**.
All **35 mounted/mirrored tool files** parse and have identical bytes.

From the prepared parent root, fresh acceptance commands are:

```sh
wsl --exec make -C conker -j4 build/conker.us.elf progress.csv
wsl --exec python3 -m unittest tools.tests.test_game_record_height_response_match -v
wsl --exec make -C conker match-progress NON_MATCHING=1
wsl --exec make tools-check
```

Run the target suite only after the build has terminated. The mounted tools
check is `wsl --exec python3 check_project_tools.py` from that tools root.

## Progress And Banking

Fresh matcher: **3,406 /5,489 exact (62.05%)**, Game **2,733 /4,816
(56.75%)**; Init492/492 and Debugger181/181 exact. Zero drift, **2,083
different**. Converted Total **5,489 /6,042 (90.85%)**, Game **4,816 /5,321
(90.51%)**. Converted bytes **85.98% /85.33%**, raw CSV totals
**1,940,312 /2,256,728**, Game **1,768,876 /2,072,880**. Gain one C function /
572 bytes; keep README aggregate-only. Preserve all old **11,507 guards**
and their exact byte prefix, append three, total **11,510**.

Per "Keep commited", commit two mounted tool files first, then parent
source/three guards/docs/exact gitlink. Mirror only absent new tool files
into the independently dirty older checkout; preserve its HEAD, two dirty
hashes and all68 initial status lines without replacing/resetting/committing
that checkout. No push, pause or dependency/account/host changes.
Ignored game-record-height-response-test/ retains original before ELF/CSV,
source fingerprint and full slot/guest/snapshot/faults-aliases/negatives/owner/
native/connected/linked/after/build receipts. Commit no ROM/ELF/native binary,
generated probe, progress CSV or save.
Mounted tools **f0818a5c524768cffd883b5e9e3585df1ded20bd** is now banked
with exactly the candidate driver and focused suite. Parent pins that
revision second; the older standalone's two new mirrored paths remain
untracked alongside its untouched independent work.

Graphify query finds no target node. Manual refresh refuses **17,017 nodes**
over retained **38,804**; fail-closed keeps **19,398 nodes from2,972 excluded
files still on disk**. Existing version/zero-node warnings remain. No force
or reinstall. Check the specific parent post-commit hook before clean-state
reporting; reduced-corpus repair remains separate and open.

## Next Work

Recover the owner's last complete GLOBAL_ASM **func_1514803C**:
VA **0x1514803C..0x151488C4**, ROM **0x1754EC..0x175D74**, **546 words /
2,184 bytes /frame0x120**. Actual **D_8008A2A4[1] at0x8008A2A8** is called
by the banked graphics dispatcher func_15147C4C with actor, command pointer
and signed16 index. Entry gates signed active count<2; exit returns a command
pointer. Read all546 instructions and helper interfaces before fitting full
graphics setup/command emission/vertex loops. Preserve S0..S3 and F20..F29
saved lifetimes and SDK graphics macros, not just the gate or a prefix.
Remaining trail constructor func_151DA6F8 still has61 differences. Other
response/cleanup/upstream/hardware/gameplay and graph corpus gates remain
open. This conversion does not complete the wider Game goal.
