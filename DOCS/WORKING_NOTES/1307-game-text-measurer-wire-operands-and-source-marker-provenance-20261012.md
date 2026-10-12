# Game Text Measurer Wire Operands And Source Marker Provenance - 2026-10-12

## Scope

Continue `func_150428D4` from consumer `b8ac2952` / tools `e7ebb38` and
[Note 1306](1306-game-text-measurer-carrier-layout-and-register-role-qualification-20261012.md).
Retail remains 219 words / frame 0x80; production remains the 199-difference
placeholder. Preferred `flag-branches-captured` remains 222 / 0x80 / 146 and
rejected. Latest actual match remains `func_15042C40`, Note 1292. No installed
source, guards, profile change, matching credit, totals or root README edit.

## Descriptor-Defined Operands

The first early-flag capture fails the old decoder at CFE byte 2808:
opcode 81 `loc`, header type/storage byte 0xFF. This is not a compiler
failure or a trusted positive receipt. The prepared UGEN's captured descriptor
declares operand tags 2,14,22 for LOC, not datatype/memory-class operands.
Read-only `f_uini` source at `ido/ido5.3_recomp/ugen_c.c:115164` confirms
those three tags; `f_readuinstr` consumes raw words using the descriptor's
record size and constant-prefix flags. No prepared source/binary edit.

The decoder now follows the descriptor operand program through terminator
22. Tags 0/1 define datatype/memory class; 2 defines the header level;
3/4/5 define the block/label field; 10 and 13 define length and offset.
Undefined interpreted fields become None. Raw words, constants and the
type/storage byte remain intact; the descriptor operand list is retained.
No stream bytes are normalized or skipped to obtain acceptance.

Typed records still reject unknown datatype 31 and padding datatype 18.
Controls reject unterminated/unknown operand programs and reserved EOF/FOO
table slots when encountered as records. The unused descriptor definitions
remain in the captured 154-entry table. Existing stream/table hash, complete
producer/consumer/driver, fired-probe, object/pool and fingerprint gates are
unchanged. The initial over-strict global terminator check exposed those
four unused table slots; handle their definitions without accepting them
as stream instructions. Scope remains the prepared compiler, not arbitrary
compiler-version portability or a full semantic Ucode interpreter.

## Source Marker Boundary

Fresh complete captures now cover the actual earlier named-flag bodies:

| Body | CFE Bytes / Records | UOPT Bytes / Records | CFE VREGs | UOPT Save Pairs |
| --- | --- | --- | ---: | ---: |
| Early captured218 | 18,672 / 859 | 18,304 / 834 | 0 | 0 |
| Late captured222 | 18,888 / 874 | 18,528 / 850 | 0 | 0 |
| Inline void-address222 | 18,840 / 867 | 18,256 / 831 | 0 | 0 |
| Named compound226 | 18,960 / 861 | 18,456 / 825 | 5 | 0 |
| Anonymous carrier216 | 18,632 / 839 | 18,048 / 799 | 4 | 1 |

The early/late source flag uses direct CFE M-48 stores/loads. The void-address
form instead has five CFE M-48 LDA records; its UOPT output retains three
M-48 stores and a load. Early/late UOPT outputs have no remaining M-48
accesses. All three have no literal CFE VREG opcode and no UOPT rstr/rlod.
Thus the earlier UOPT variable-table `vreg` suffix is not interchangeable
with a literal CFE VREG record. This does not identify the exact eligibility
or coloring pass, or prove the front end supplies no other relevant metadata.

The anonymous carrier's four explicit CFE temporary homes and actual
register-8 call-save remain a fired positive control. Five explicit VREGs
alone in the compound form are not enough: its source flag M-44 is stored
at CFE byte 1576, but its first load is byte 4760, after the metrics CUP at
2816. It does not create a pre-call snapshot of that named flag. Do not
attribute the missing save to a specific UOPT deletion pass without evidence.
This absence check uses completed full streams, not an unfired handler probe.

Every diagnostic completes the normal compiler driver with exit 0 and
preserves its own normal text/functions/relocations and the union of every
pool family. Actual owned-child argv/producers, initialized-table probe,
marker order and hashes are checked. cc/uopt/ugen/cfe fingerprints remain
exact; no existing debugger attach, native-memory write, runtime call,
compiler rebuild, package installation or diagnostic compiler flags.

## Default-Zero Source Screens

`compound_candidates()` adds three non-installable real flag initializations
and bitwise compound updates, retaining five metric fields and the owner
profile. CLI `--compound` is exclusive with `--carriers` / `--layouts`;
default/original generators remain unchanged.

| Form | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Named compound | 226 | 0x90 | 197 |
| Inline void-address compound | 230 | 0x90 | 222 |
| Scoped compound initializer | 227 | 0x90 | 222 |
| Ignored shared-default named predicate | 217 | 0x90 | 180 |
| Ignored shared-default direct predicate | 219 | 0x90 | 134 |

None of the three compound forms emits the required T0 zero. The two
additional ignored predicates initialize one real default before effectful
branches, but still emit a space-only T0 reset at word 45 after the width
read. Their call-save is SP+0x54. The 219/134 form swaps width/cursor S1/S2
roles and retains the wrong 0x90 frame. It is not preferred over the old
222/0x80 seed merely for length or a lower difference count. These five
forms are shape screens only, not new public/private/native/owner evidence.

## Qualification And Bank

Nine frontend tests pass in 32.481 seconds, no skips: existing 3,020 public
comparisons plus new descriptor controls, three source-marker captures,
compound shape rejections and the completed compound input/output capture.
Fresh isolated original-predicate regression: seven tests in 34.274 seconds,
6,795 comparisons. Fresh isolated carrier-layout regression: six tests in
35.249 seconds, 7,550 comparisons. All 22 tests pass; no new full private/
fired-fault/native/owner/padder/rebase qualification or matching credit.
Earlier full-20 receipts apply only to unchanged old bodies.

Tools b3d042d7de76eb984c7ec221486aeafb095d0b49 is committed first; consumer
note, concise indexes/workflow and exact gitlink follow. Consumer/mounted/
older tools checks, Windows py_compile and diff checks pass. All nine frozen
inputs and protected 189,088 bytes / 720 owners remain unchanged, with
effective corruption controls. Production hashes, Game 2,813 / 4,823
(58.32%), total 3,486 / 5,496 (63.43%), zero drift and root README stay
unchanged. No OGL/Release/ROM/save/config/editor/guest-debugger change,
additional Claude call or push.

Older HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a` / dirty366 is preserved.
All 89 task fingerprints were checked before synchronizing exactly three
known existing files; the other 86 fingerprints stay unchanged. No new
older paths, older commit/reset/history rewrite. Final bank requires checked
links, fresh post-documentation immutable controls, clean active repos and
the post-consumer Graphify hook's fresh terminal Rebuilt receipt with advanced
log bytes/UTC and zero workers. Preserve graph warnings; no force or purge.
All 4,524 relative links across eight checked documents resolve. Fresh
post-documentation immutable/corruption tests 05/06 pass in 1.686 seconds.

## Next

Keep the same target and full Game goal active. Use operand-aware CFE/UOPT
records to track the actual anonymous predicate value and its default-zero
merge, distinguishing it from source-variable eligibility and post-call
compound loads. Recover the shared early T0 zero, seven saved roles and
complete 219 / 0x80 / SP+0x68 lifetime. Do not repeat these five source screens
or infer all C is exhausted. All final private/fired-fault/native/owner/
neighbors/pools/both-padders/independent-links/rebases/literal whole-ELF/data/
guard-prefix gates still precede installation/totals. `func_150417AC` follows
only after a real match here.
