# Note 2602: Actor projection submission guarded byte match

Date: 2026-11-21. Consumer baseline `16c3bd7051abafb88d6a0e87c80537f388bbeaa0`;
tools baseline `9643f3af44e407ffb0b4449ed9b03d8cb23d1280`.
Qualified tools commit: `64aa7580e13b3d78f8495f5a6554075066bcbae3`.
The core qualification is banked in `e951444368df0d1bf1a1a39eaa0df3a9ad356832`;
the follow-up commit couples the historical caller input to its exact snapshot.

`func_15035808` replaces its seven-word zero-return placeholder with complete
semantic C. Its **345 words / 1,380 bytes**, **216-byte frame**, seven saved
GPR homes and all **32 relocation sites** are byte-exact through **316 checked
normalization rows**. No profile change, instruction insertion or omission is
used. Raw C has the correct length and frame; byte identity includes the guards.

Production recount: **4,586 / 5,528 (82.96%)** total, **3,913 / 4,855 (80.60%)**
Game, zero address drift, **942** still different. Init 492/492 and Debugger 181/181
remain exact. **113 more** are needed for 85% at this denominator. Converted
rows are unchanged because the old placeholder already counted as C.

## Behavior and source interface

Owner `conker/src/game/generated_61D10.c`, VA `0x15035808..0x15035D6C`,
ROM `0x62CB8..0x6321C`, no alignment tail. Ten arguments carry mode, actor
index and eight floating-point projection parameters. Known callers ignore
V0; the recovered interface is void. The declaration in generated_CDE80.c
is repaired accordingly. All 28 raw caller functions, pools, both padded forms
and the complete actual-Make caller object remain unchanged.

The routine rejects a full 15-record queue, unsuitable actor state, missing
projection data, excluded low flag nibble and zero opacity. It queries matrix
count, checks unsigned matrix-buffer capacity, computes truncated camera
distance, and applies the retail 1,400/10,000 distance gate and fade. The fade's
unusual denominator is `distanceLimit-200`; it is preserved exactly.

It queues an initial projection, publishes matrix/color/actor fields, submits
all 19 matrix-helper arguments, scales alpha, and rolls the count back on cull
rejection. Successful submissions advance matrix cursor and used count.
It then scans matching linked descriptors, preserving the preloaded next link
across providers. It retains color and primary/secondary output homes, resolves
matrices, allocates missing cache entries, reloads the frame index after the
allocator, publishes the cache, submits the descriptor packet and scales alpha.

The locally recovered descriptor is 92 bytes: `fixedMatrices` at 0x34, `attachment` at 0x48,
two cached matrix pointers at 0x4C/0x50 and links at 0x54/0x58. The existing constructor's
5C-byte allocation supports that extent. Unrelated shared struct126 is not
reused. All nine other owner functions, bindings and the existing 16-byte literal
pool remain identical despite the local type extension.

Actual passed homes are colors at SP+0xC4/0xC8/0xCC, primary at SP+0xC0 and secondary at SP+0xB0.
All 256 private/incoming bytes (-216..39 relative entry SP) are included in
qualification. No dummy arrays, invented volatile declarations or frame-size
guards were introduced. Integer camera components preserve ordered subtraction
and truncation; the earlier vector form failed that stronger FP-order check.

## Closed normalization and independent evidence

Raw payload SHA256:
`0c57b385f9bf139b75ad4e3bd9e1625fcb5a504b90757faecccab200c2de7222`.
The frozen plan hash is
`d5a67b544eac81613a4f8d0bc7194415cf7d3e8cfff632fd8862570022e2ef1c`.
The emitter consumes only fingerprinted compiled C instructions, relocations
and a finite origin/register/CFG plan. It does not read ROM or original assembly
to generate code, and the plan stores no output instruction words.

The derivation normalizes register lifetimes, independent prologue/19 argument
packet schedules, index-home timing, alpha spill from SP+0x88 to SP+0x80, boolean lowering
and loop-header lookahead. It preserves physical saved homes. Redundant actor
pointer/index/boolean temporaries are replaced by equivalent continuations
derived from existing branches, constants and loads; output length stays 345.
GNU original assembly and all 32 bindings independently agree. Two complete links
exercise shifted code/data and HI16/LO16 carry. Mutated payload, binding and
plan controls reject. The normalized unbound SHA256 is
`858f0ab1801f67b0438ec1413e2a45d7f7ba4540276281dfb440e3c018d5b03c`.

An independent instruction-driven relation compares the intermediate 344-word
stack-normalized C stream with retail: 78 prefix transfers and 31 joint transfers
for each of first/later descriptor iterations. Different boolean branch
partitions are refined with exact bit-vector identities. Every abstract path
and instruction is covered. It checks ordered FP/FCSR effects, public-read
multiplicity, public stores, all 19 helper arguments, saved registers, loop roles
and all 256 private bytes at calls/returns/cuts. Providers may mutate public RAM,
caller state, outgoing homes and retained exposed color/primary/secondary
ranges. Only adjacent stores with proven byte-disjoint addresses commute.
Six semantic instruction defects fail; coherent F6->F14 recoloring passes.

Guest qualification passes 1,084 cases, 6,908 calls and 877 allocations against an
independent public-state reference. All 344 intermediate/345 retail words are
reached, actual pointer arguments agree, and all 256 private bytes agree at every
call and return. Native SDK32 complete-object checks pass 1,084 cases each at
O0/O2/O3 with strict aliasing/UBSan; six selected-source defects reject.

All three original caller windows execute 822 connected cases/12,054 helper calls:
10 words at ROM 0x63744, 21 at 0xCE400 and 11 at 0xCE45C. They preserve all ten arguments,
the original JAL/final FP delay store and following index increment; the record
path also executes its original unconditional continuation. Complete connected
RAM agrees. Each missing-delay control fails. Explicit 5/9-word scaffolding is
separate from the actual windows; no full outer caller claim is made. A complete
original successor-CFG audit finds no V0 use before redefinition/call/void-return;
three injected result reads reject. Computed callers remain unexcluded.

## Production, history and continuation

Both full-owner padders and the natural O2/g3 Make recipe agree. Three actual
Make commands qualify the target and five the mixed-assembly caller. Its two
existing GLOBAL_ASM routines require the assembly padder and retained labels;
the layout padder has identical functions/bindings but different local symbol
tables. The correct natural recipe preserves the complete frozen caller object.
Independent full-ELF prediction includes all 6,051 slots: **1,050 declared changed
bytes, zero exclusions or unexplained bytes**. Only the target slot and its
symbol size 28 to 1,380 change. All 189,088 protected Game-data bytes across 720 owners
remain exact. Production ELF SHA256: `17080b77c6fccf01ed110cf372fa8acd41799dc1ed1be27d8d7ae23b0807e1e1`.
The explicit frozen plan audits 2,222 baseline inputs and two
additional generated caller-assembly fragments, matched to the immutable original
assembly slice in the frozen baseline. Conversion rows remain unchanged and
`make tools-check` passes.

Both primary and private sibling-tools configurations pass **36 focused tests**,
six dependency bridge tests and three historical full-image gates before and
after installation. Nine focused tests are new; 27 existing neighboring-function
checks run fresh. Twenty older semantic checks are explicitly reused by exact
fingerprints and AST/provenance. Historical manifests only append exact
snapshots/dependencies, and the filter recovery gate gains an exact compatible
snapshot branch. Historical fixture bytes and generation are preserved.

After installation, three additional caller-dependency checks pass in each
configuration. They accept the original frozen inputs and the qualified void
declaration only with its complete owner/caller/guard snapshot, and reject
changed caller hashes or any changed snapshot field. The scan recovery change
alters only this input gate; an AST comparison proves its generation unchanged.

The 28 tools files are committed before the consumer, in a core qualification
commit and a focused caller-input follow-up. The private sibling overlay
contains 1,127 files from {'sibling': 347, 'bootstrap': 1, 'primary-fallback': 751, 'task': 28}; the actual dirty sibling's
HEAD/status and all 351 consumed dependency hashes are
protected. Graphify refresh retains existing IDs and qualification metadata;
the scoped merge is not represented as a full-corpus extraction.

Assumptions are mapped/aligned ordinary RAM and o32 providers, public backing
disjoint from private stack, and defined SDK32 native objects/inputs. This does
not establish MMIO/fault/interrupt, full-caller, hardware or gameplay behavior.
No host-port, frozen Release, ROM or save changes. Zero Claude calls and no push.

```sh
python3 -m unittest tools.tests.test_game_projection_submit_15035808_match -v
python3 -m unittest tools.tests.test_game_list_historical_image -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue the 85% matching goal from the new frozen bank. The next function must
receive its own source/ABI/owner, semantic, whole-image and adoption qualification.
