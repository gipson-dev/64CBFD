# Angular emitter direct byte match

Date: 2026-11-19. `func_150BAFEC` replaces the zero-return placeholder in
`conker/src/game/generated_E8090.c`. The complete **157-word / 628-byte**
slot, VA `150BAFEC..150BB260`, ROM `E849C..E8710`, emits directly from C.
The original **184-byte frame** and **17 relocation sites** match. There are
**zero guards, insertions, omissions or alignment words**. The original ASM
is retained. The normal O2/g3 owner profile is unchanged.

Fresh production totals: **4,556 / 5,514 (82.63%)** overall,
**3,883 / 4,841 (80.21%)** Game, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 958 still different. **131 more** matches reach 85%.
Conversion remains 5,514 / 6,048 (91.17%), 86.19% of bytes. The goal stays active.

## Recovered interface and behavior

The callback retains all fifteen o32 argument words. Coordinates occupy
arguments 2/3/4, heading argument 8 and byte context argument 14. Heading
uses a word formal (`u32`): retail loads the complete incoming word before
narrowing for the byte-angle helper. The shared dispatcher's byte callback
typedef still describes its own zero-extended heading argument; qualification
uses the actual MIPS call, with no native incompatible function-pointer claim.
Unused arguments preserve their ABI positions.

Four `func_151423D8` samples give heading/pitch sine and cosine, using modular
byte angles. Unsigned RNG selects duration `%36+70`, alpha `%52+90`, pitch
`%11-12` and two independent flag bits. REAL samples produce size `*165+800`
and speed `*11+15`. Velocity X/Z use `(speed*pitchSine)` times the heading
sample. Y uses `-speed * pitchCosine`, preserving negation before multiply.
Repeated horizontal expressions recover the original common temporary.

The descriptor occupies **112 bytes**, of which **84 are initialized**.
Ranges `3C..47`, `5C..5F` and `64..6F` are deliberately unspecified. Do not
clear the structure to improve appearance. Signed field `63` is `s8 -1`;
result-pointer declaration order also matters to the original stack layout.
Flags start at `E05`, optionally adding `40` and `80`. Field24 reads
`D_8009FE74` late; `D_8009FE78` is cached before the factory and copied as
four bytes to returned-record +`A8` on success. Factory arguments are
`(&descriptor, 0, 4, context, 1)`. The callback **always returns one**,
including allocation failure.

An aligned retail census finds one function pointer at ROM `22F4D4`,
`D_8008AA00[5]` / VA `8008AA14`, and no aligned direct JALs. The original
dispatcher `func_1514C2F0` call window `1514C3C4..1514C404` forwards all
fifteen words. Its `BEQZL` return-zero path annuls word `1514C400` on the
real return-one path: 15 positive words are visited; two effective zero-return
controls exercise the sixteenth and branch to `1514C42C`. This qualifies the
window, not the entire parent dispatcher.

Connected original helpers are literal in production: all 18 words of
`func_15130374`, 38 of 61 words of `func_15130280` in the actual mode-zero /
null-owner paths, and all 11 words of `memcpy` are visited. The allocation
request uses category `2B`, context 1, size `AC`, flag 1, slot byte, flag 1.
The helper copies 112 descriptor bytes to record+`10` and clears byte `9C`.
The allocator remains an opaque modeled service; no full allocator or hardware
acceptance is claimed. Synthetic factory-time global mutation is tested in
the flat guest/native fixtures, outside the connected allocator contract.

## Validation and image audit

Both final configurations pass **five tests**, no failures/errors/skips:
**95.074s primary / 111.766s sibling overlay**,
**316 imported tool fingerprints each**. The 860-file overlay contains 339
matching sibling files, 514 primary fallbacks, six task files and one bootstrap.
The real sibling dirty HEAD/status and 343 dependency hashes are preserved;
conflicting sibling edits were not overwritten or claimed tested.

- Complete before/after owner compilation preserves all five neighbors and
  pools. Both actual owner padders match, with 12 GNU rebases and 174 rejected
  instruction/binding corruptions. Source and original assembly match all
  157 words and all 17 relocations directly.
- **2,048 guest cases / 4,096 source-and-retail executions** match the independent
  semantic reference, visit all 157 body words and preserve saved ABI.
- **320 dispatcher-window cases** check all fifteen argument words and the
  return branch; **192 connected factory cases** cover success/failure and
  the original descriptor and extra-data copies.
- **1,024 SDK32 native cases each at O0/O2/O3**, strict aliasing, no fast math
  and UBSan pass. All 16 semantic negatives fail as intended. Initialized
  descriptor integer fields are compared in guest byte order; the 28 unspecified
  bytes are excluded from native value assertions, not from the linked image.
- Actual Make and an independent complete-image predictor agree on
  **517 explained changed bytes**, with four image corruptions rejected and
  **zero excluded bytes**. Production really rebuilt the single owner; no
  prebuilt object was copied into production.

Two exact symbol-table record/string permutations are declared and compared:
`[D_8009FE78,D_800A0278] -> [D_800A0278,D_8009FE78]`, and
`[D_8009FE74,D_80091804,D_800A0274] ->
[D_80091804,D_800A0274,D_8009FE74]`. These symbols have distinct addresses;
they are **not same-address aliases**. Complete named symbol definitions are
unchanged except the target's explicit stub-to-body size update. The predictor
reconstructs these specific record/string permutations and compares the entire
ELF; no metadata section or address range is excluded.

Only source, owner object and ELF change among **1,835 frozen inputs**. All
**698 objects** are audited; only this owner changes. All **6,050 other
function bodies, addresses and extents**, five neighbors/pools and **189,088
protected bytes / 720 owners** remain unchanged. Guard CSV, conversion rows,
Makefile, original ASM, compiler inputs and shared headers stay byte-identical.
Production ELF SHA-256:
`c1476b0828dcd37fba1d13b0a8e606dc13d22de9ed168d8aaac23c87a743e1a0`.

Fresh installed checks recompile all six functions/pools, compare all 157
actual production words, rerun 2,048 guest, 320 caller and 192 connected factory
cases. Unchanged padder/rebase/corruption/native/image receipts are fingerprinted
reuses. Required production `match-progress` and `tools-check` pass. The existing
duplicate generated_12D630 recipe warning remains.

Initial private screens and harness failures are retained for diagnosis. The
caller fixture was corrected from actual FPR roles, positive-path branch
annulment and the window interpreter's continuation mechanism. Final suites
ran after these corrections and final tool hashes were sealed.

Root README changes only its snapshot date and two aggregate matching rows;
detailed work remains here and in the five concise documentation indexes.
Graphify uses a native update attempt, scoped AST refresh and explicit target
reference with old-ID retention; this is not a full-corpus extraction claim.
Tools are committed before the consumer pin. Routine work used zero Claude
calls, no REA/WSL reconfiguration and no host, Release, save or capture changes.
The supplied `64CBFDOGL` path currently contains captures, without an identifiable
active host checkout; no current host implementation or adoption is inferred.

Next inspect **func_150BB498**, still a zero-return placeholder in this same
source/ASM owner and the next callback-table entry. Freeze caller/provider
evidence against this committed baseline before drafting. No next-target match
is claimed. No automatic push or pause.
