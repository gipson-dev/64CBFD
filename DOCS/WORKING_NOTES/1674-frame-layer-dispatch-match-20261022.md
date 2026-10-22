# Frame-Layer Dispatcher Direct C Match

Date: 2026-10-22

## Result

Recover `func_151749F8` in `conker/src/game/generated_1A1E50.c` from its
twelve-byte zero-return placeholder. Complete semantic C emits all
**43 words / 172 bytes, frame 24 and seventeen bindings** directly under
normal O2/g3. No guards, inserted words or profile changes.

VA 151749F8..15174AA4 / ROM 1A1EA8..1A1F54, ends exclusive.
Preserve `conker/asm/1A1E50.s` and all three owner neighbors, including
the two already-matching SDK matrix wrappers. Keep the address-based name
and add a purpose comment, a private callback typedef and typed local
helper/global declarations. No shared-header or conversion-row changes.

Correct the sole local declaration in `conker/src/game_45B80.c` from
s32 to void. The routine does not define a meaningful integer return;
its sole caller ignores V0. Raw code/pools for all sixteen caller functions
and the entire ordinary-Make caller object must remain identical.

## Recovered Contract

Both incoming words are stored in their homes at current SP+0x18/+0x1C.
The first is unused. The second is forwarded to the selected callback after
the three setup calls, including the late home load present in retail.

1. Call func_15165F70 without arguments.
2. Read both live D_800B0E00 words and pass them to func_15195FF0.
3. Call func_1510C8A8.
4. Read D_800B0DF0 and its selector byte +0x0B. A nonzero selector dispatches
   D_8008CD04[selector] with the second incoming word.
5. Read the late D_800BE616 byte. If zero, call both func_1517DE5C and
   func_151880C0, even if the former changes that byte.
6. Read live D_800BE9E4 and the unsigned D_800CBD4E halfword. Add the clock
   word shifted left six and store the low sixteen bits.

Use an explicit unsigned cast before shifting, preserving all clock-word
bit patterns without signed-shift UB. Do not cache the clock, accumulator,
configuration pointer or disable gate across effectful calls. Do not add
an integer return or suppress the original unused incoming-word home.

The second incoming home's mutation is guest-only evidence of emitted
instruction behavior. Native C tests use ordinary backed globals and valid
callback signatures; they do not claim portable access to another function's
private argument homes.

## Callback Bounds

The retail D_8008CD04 table has 28 entries and null slots 0, 12 and 27.
Only selector zero is gated by this routine. Do not invent a null callback
guard, clamp the selector or claim safe nonzero-null/out-of-range behavior.

Boundary qualification deliberately provides a backed synthetic 256-entry
table with defined callbacks. This covers byte-index arithmetic, not
retail table validity for every possible byte. Original table bytes and
holes are checked separately. Most helpers and callbacks remain bounded
contracts, not recovered complete providers or full gameplay acceptance.

## Exact Emission

Raw unlinked SHA-256:
`7aeac6d5bee38c7fffdc9c2b66901c530c43ef08f846a5dce787fb605b9e9fe6`.

Independent original GNU assembly, isolated C and complete raw owner agree
on all words and seventeen bindings. Actual Make reproduces both owner
recipes: three productive commands each, six total. All three raw/padded
neighbors, pools and addresses remain fixed. The caller's complete object
is unchanged despite the corrected return declaration.

## Link Serialization

The first whole-image check correctly rejected forty otherwise-unaccounted
metadata bytes. GNU ld swaps adjacent symbol/string records for
D_8008CD04 and func_1517A84C. Reuse the existing structured serialization
helper with the exact two names, order (1,0), and full predecessor
value/size/info/other/section definitions. Assert adjacent symbol records,
contiguous original strings and exact spellings.

The absolute symbol remains 8008CD04/size0/info16/other0/SHN_ABS.
The unrelated function remains 1517A84C/size12/info18/other0/section5.
Canonical symbols before and after the permutation must agree.
This is explicit metadata accounting, not an exclusion or code patch.

The strict independent complete-ELF prediction permits exactly
**168 changed bytes = 127 code bytes + 41 metadata bytes**:
one target-size byte plus forty symbol/string serialization bytes.
Zero exclusions. ELF SHA-256:
`d3fc5c860e95112c1395e56c142478ac6081675edcbdfda76874d456332fdca4`.

## Qualification

Task tools, identical in both local copies:
`experiments/game_frame_layer_dispatch.py` and
`tests/test_game_frame_layer_dispatch.py`.
Reuse the ordinary owner/padder, dual-owner Make, MIPS fault-prefix,
native32, independent GNU link and strict serialization helpers.
Routine work uses zero Claude calls.

- 6,144 guest phases cover every selector byte, empty/selected branches,
  disable bytes, full incoming words, halfword/clock boundaries, callee
  side effects and incoming-home mutation. Every target word executes.
- Native32 O0/O2/O3 each exercise 65,536 selected-body cases with trap
  UBSan. Twelve defined wrong-C controls target call order/omission,
  pair order, callback/view, disable gate, missing optional call, shift,
  reset and prematurely cached clock/accumulator/selector values.
- Nine independent GNU links cover 48 rebase phases and all seventeen
  bindings. Check 76 fired target-access fault prefixes and eleven strict
  image corruptions, including symbol/string serialization sites.
  Guest fault agreement is not portable C/MMU semantics.
- The aligned retail scan finds one direct JAL at ROM46760 and no literal
  target pointers. Execute the original five-word caller window
  150192A4..150192B8 across 32 phases, stopping before the next call.
  Verify the D_800BE9F0 word load and zero second argument in the delay slot.
  Complete parent execution is not claimed.
- The original and current func_15165F70 both contain the same two-word
  no-op return. Connect that actual code across forty phases. Other helper
  bodies and selected callback implementations remain outside this scope.

The initial native O2 fixture crashed at an aligned SSE store with an
unaligned freestanding entry stack. GDB identified MOVAPS at run+51.
Apply the existing force_align_arg_pointer entry convention to the harness,
not production. A negative cached-phase control also required explicit
parentheses under -Werror. Neither failed run counts as passing evidence.

Compile the immutable native runtime once per optimization per tools-copy
run, then compile each selected/control body separately with the same flags
and link it against that runtime. No stale cross-run native object is reused.
This avoids recompiling the 256 callback stubs for every control and keeps
real callee effects across translation-unit boundaries.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 64.221s | 8 tests, 50.919s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 16.691s | 2 tests, 6.588s | 0 / 0 / 0 |
| Final disjoint-rebase rerun | 1 test, 7.955s | 1 test, 10.013s | 0 / 0 / 0 |

Shared tools checks pass in 0.272s / 0.496s. A final fixture review found
that the first relocated global layout used 0x100 spacing around a 1 KiB
synthetic table, accidentally aliasing its gate/counter globals. Change that
spacing to 0x2000 and add explicit disjoint-range assertions. Rerun the
affected relocation/fault-prefix test in both installed copies: all nine
GNU links, 48 rebase phases and 76 fired prefixes pass.

AST comparison proves that only test04 changed: all seven other test
methods and all shared local helpers are identical. Preserve the original
receipts and input manifest as historical evidence. Explicitly reuse five
unchanged pre-install behavioral checks under strict source, raw/padded
owner, complete caller object, guard, helper/input and full-image identity;
test04 is superseded by its fresh installed rerun. Do not call the other
five fresh installed runs. No production source, object or ELF changes are
made for this fixture-only follow-up.

## Production

Commit tools first: `6b78fa71adb01be24ddb1e0d5c770435aec5de0f`. No push.
Bank the fixture-only follow-up as
`14aa3890a98e0aa2d65cee2f946c7a60c74a7d68` before the consumer.
Reverify all 15,866 current files with only the two owned test-file
fingerprints advanced; preserve the pre-correction manifest and receipts.
Preserve all 1,560 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only the two task files, leaving 1,562 dirty paths. Do not reset/commit it.

Seal 15,866 files and all 1,454 linker objects. Normal Make completes in
2.581s in the verified Linux copy. Mark only the verified unchanged guard
manifest old to avoid unrelated historical-object rebuilds. Existing
generated_12D630 duplicate-recipe warnings remain; owner/caller diagnostics
are unchanged and isolated diagnostics are empty.

Preserve all other 6,054 linked bodies, all 6,055 addresses and all 720
protected Game-data owners / 189,088 bytes. Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Padded target owner SHA-256:
`d6f26953bac830554a342a16f33ae4ff5643602f1ac98dc5cf62a767c39423a5`.
Unchanged complete caller object SHA-256:
`6f93d458b6a4991ee00a8d815534c58451aad5b9864fff79c9ceaf0c9533fafc`.

Live adoption audit passes in 23.641s. Verify every static input and
non-target object before and after promoting only the target owner object,
ELF, linker script and progress CSV. Both edited C files must already equal
their qualified proposals. The unchanged caller object needs no promotion;
linker-script and conversion-CSV bytes remain identical. Reproduce the
complete independent 168-byte image prediction with zero exclusions.

## Handoff

The standard matcher against the actual live ELF completes in 6.284s:
total **3,743/5,505 (67.99%)**, Game **3,070/4,832 (63.53%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,762 different.
The 75% threshold remains 4,129 exact, requiring **386 more matches**.
Queue shapes: 1,631 placeholders, 122 semantic/other and nine unlocated.
Next func_1507EEF4 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

The final test-only correction preserves this exact live source/object/ELF
image and refreshes all 15,866 static-input checks; it does not earn another
matching function or change these measured totals.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts. Preserve excluded-corpus/large-HTML caveats without
claiming full re-extraction or a fresh corpus-membership recount.
Host Release remains untouched.
