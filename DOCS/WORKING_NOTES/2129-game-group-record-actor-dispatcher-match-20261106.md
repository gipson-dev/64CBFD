# Group-record actor dispatcher match

Date: 2026-11-06. Continue the active 80% goal from consumer
`d3cd56b836a4cae2d1b2c3de7f0242661047e4b0` and mounted tools
`3ec88e1a58b6f8d2c811fc1ad645d1c13d5745a7`, following
[Note 2128](2128-game-event-height-threshold-dispatcher-match-20261106.md).

## Recovery and compiler evidence

`func_15022528` in `conker/src/game/generated_49D30.c` now matches its entire
**70-word / 280-byte** retail slot, VA `0x15022528..0x15022640`,
ROM `0x4F9D8..0x4FAF0`, frame `0x40`. The supported interface is
`void(s32 group)`. Its sole direct caller is **func_1501D348**, at
JAL VA `0x1501DA64` / ROM `0x4AF14`, with S5 copied to A0 in the delay slot
and continuation at `0x1501DA6C`. No tail calls or literal pointers were found
in the ROM census. The earlier private guess naming func_1501DAAC as parent
was wrong; that is the next function after the actual parent.

The routine walks a byte-sized count at D_800C363A[group]. Both unsigned
halfword masks, D_800C35D0[group][index] and D_800C35C8[group][index], must be
nonzero before the eight-byte descriptor is read. Only its exact unsigned
halfword kind 2 triggers lookup of byte 2 through func_15083E90. A nonnull
result is dispatched to func_1502178C(actor, group, index). Pointer-table
entries are reloaded on each active iteration; callbacks may replace them.
The count is retained across mask-rejected iterations and refreshed after
descriptor processing, including a wrong kind or null actor result. Explicit
count storage recovers this retail behavior and the exact branch-delay index
and halfword-offset updates. No range clamp, narrowed group or scalar return
contract is invented. Native backing uses valid groups 0..2; full-word sparse
group probes describe emitted guest arithmetic, not out-of-array native C.

The local forward declaration changes from an old-style s32 placeholder to
void(s32). The existing old-style func_1502178C declaration and unrecovered
zero-return body remain unchanged; its original 395-word assembly consumes
the three arguments. This match does not recover that helper. The existing
typed u8 actor lookup declaration is retained. Its complete 72-word linked
body and the original two-word caller window independently equal the ROM.

The owner already uses **O2/g3/-Wo,-loopunroll,0/MIPS2/O32** at Makefile:175.
No compiler profile, Make rule, layout or shared-header change is made.
The initial ordinary-loop screen gave 71 words/58 differences. Recovering
the cached count gives 70/frame0x40/21 differences. All 24 local declaration
permutations and seven explicit address/control shapes converge on that
same result. The first screen used default O2/g3; copied-owner qualification
was corrected to use the existing owner profile without weakening the audit.

The remaining differences form one closed six-register allocation cycle:
raw S6->S3, S7->S4, FP->S5, S3->S6, S5->S7, S4->FP. Saved accesses are
reordered into their original physical-register homes. **21 expected-word,
relocation-aware guards** produce every retail word, with **zero omissions,
insertions, frame changes, branch retargets or changed calls**. Every output
instruction has one compiler origin; the origin list is a permutation of all
70 words. All ten bindings stay at the same offsets with the same symbols.
The complete semantic C remains visible; it is a guarded match, not a claim
that the unnormalized compiler stream is directly byte-exact.

All **56 raw and padded neighbors**, including the actual caller and helper
placeholder, remain fixed, as do all compact/padded pools and register
metadata. The owner has57 actual function slots; prototype counts are not
function counts. The old guard-file byte prefix is preserved, followed only
by these 21 rows. No diagnostics are introduced. No Claude call was used.

## Focused qualification

Seven checks pass before installation in both tools configurations and again
after installation against both actual helper copies. The sibling overlay is
confined to ignored build storage. Its six tracked edits and 2,428 untracked
files remain unchanged. Both tools smokes are fresh. Three shared suites per
copy (match-progress, word patches, PC16 padding) are exact-hash reuses from
Note 2124, explicitly recorded separately from fresh tests.

- **932 cases per body**, original/raw/normalized, compare complete RAM,
  helper calls and external access order. Every retail instruction executes.
  All 256 counts and actor IDs, halfword edges, missing/null results, aliased
  masks, count shrink/growth, callback pointer replacement, two stack phases
  and full-word guest groups are covered. Original/normalized complete
  machine states agree; raw stack access order and fault parity are not claimed.
- **287 own-access fault prefixes** compare literal original/normalized
  states. Empty and mask-disabled cases also succeed with unused pointer
  tables absent. These are emitted guest instruction checks, not portable
  C fault semantics or hardware acceptance.
- **256 cases per body** connect the complete original 72-word lookup and
  compare independent results/storage. This fixture reaches 18 lookup words;
  it does not establish full lookup-path coverage. **56 cases per literal
  body** execute the original two-word caller window with S5 group as an
  explicit precondition. Full parent/update execution and gameplay are not
  claimed. The update provider is bounded independently.
- **Nine independent GNU links**, three code/data layouts and 21 cases per
  body check all ten bindings, signed low16 carries, the 280-byte symbol and
  eight zero alignment bytes outside the function.
- **26,880 native32 SDK/UBSan calls**, O0/O2/O3, use complete typed arrays,
  records, actor backing and callback logs. They check all 256 counts/IDs,
  field offsets, exact halfword kinds including0102/8002, aliased masks,
  dynamic counts and replacement tables. Eight wrong variants fail with
  checked exit42 and no diagnostic/trap: kind, narrowed kind, omitted second
  mask, narrowed first mask, selector, group, index and stale count.
- All 280 raw-byte corruptions, ten binding corruptions,21 stale manifest
  expectations and five whole-image corruptions are rejected. The stale
  fixture preserves every existing guard while corrupting each new row.

Initial fixture corrections moved actor storage away from STACK=0x40000,
provided freestanding memcpy for GCC structure copies, strengthened kind
edges and retained the caller's existing guards in negative manifests.
These fixes did not alter recovered C or production guards. Final successful
receipts fingerprint all five new modules and actual imported helpers.

## Actual production

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Actual Make compiles only generated_49D30 once under its preexisting profile,
without diagnostics. Keep both old-dependency flags for scoped builds until
a deliberate broader rebuild; do not touch unrelated object timestamps.
The actual ELF equals the independent **221-byte** prediction with **zero
exclusions or metadata permutations**. Only the target body and symbol size
(12 to 280 bytes) change. All 6,052 addresses, progress.csv, conversion rows
and 189,088 protected data bytes in 720 owners remain fixed. The unfinished
whole image retains the expected checksum failure and the preexisting
duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,198 / 5,512 (76.16%) | 0 | 1,314 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,525 / 4,839 (72.85%) | 0 | 1,314 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**212 more** matches reach the current 4,410 threshold for 80%.

- ELF: `7fed3e3d16adc225ed18fce721a8669903cd4a061c01d6c94d9f1c2558b01ecf`.
- Owner: `0c5039982f76a6224fa8e92ccac19ec4ccaf03cf3a5c90c5c33e9ca68c4b6eb2`.
- Code binary: `7fc7e027a6f443d75d6a21d9ed0c2ec526206231c97c097f1eb1bf4c38f1c6f3`.
- Guard CSV: `35c4628409bcf6ed0c1b776c1f886bc144f19ca23ec7f923a4e2fdb614e9b4fa`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

All 107 frozen inputs and the strict predecessor/prediction are retained in
`conker/build/game-group-record-actor-dispatch-15022528-match/`. Graphify receives
a scoped refresh with old-node retention evidence; no full-corpus extraction
is claimed. Tools are committed before consumer source/guards/docs/pin.

Next static target: **func_15081574**, generated_AE1D0. Its retail slot is 71
words, consisting of a 68-word body and three alignment words. Inspect its
float/integer O32 arguments, output pointer and actor scan before selecting
a compiler candidate. It has zero new matching credit. Preserve unrelated
work, private inputs/saves, handwritten func_150A76F0 and frozen host Release.
The full 80% goal remains active.
