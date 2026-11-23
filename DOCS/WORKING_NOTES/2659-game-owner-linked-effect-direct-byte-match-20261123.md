# Owner-linked effect direct byte match - 2026-11-23

`func_151D1448` now replaces its zero-return placeholder with the complete
actor-linked effect constructor. All **98 words / frame 144** emit directly
from semantic C, including all four relocation sites. There are **zero guards,
insertions or omissions**. Production total rises from **4,638 to 4,639 / 5,528
(83.92%)**; Game is **3,966 / 4,855 (81.69%)**, Init 492/492 and Debugger 181/181.
There is zero address drift, 889 different functions and **60 more matches to
85%**. This counts one complete function.

## Behavior, interface and boundaries

The complete original is `conker/asm/1FA770.s:4493`, VA
`151D1448..151D15D0`, ROM `1FE8F8..1FEA80`. The recovered interface is
`void func_151D1448(u8 *owner)`. The function captures the actor at owner+0x28,
builds a 28-byte request and a 32-byte configuration, then calls the existing
11-argument factory `func_15147A80`.

- Actor type 0x25 selects configuration values 800, 36, 50 and 200. Other
  actors select 260 when signed `D_80082FA0 > 0`, or 500 otherwise, followed
  by 40, 40 and 180. The final float is captured from actor+0x14C.
- The request captures the owner's three position words and sets lifetime
  300, mode 0x36, active 19, kind 6, count 25 and the final zero word.
  The factory receives payload size 32, entry size 40, channel owner+0x0C
  and unsigned context owner+1, with the remaining retail arguments intact.
- On factory failure there is no copy or attachment. On success, the payload
  pointer is loaded from created+0x98, all 32 configuration bytes are copied,
  and only then is the created object published at owner+0x30. Configuration
  capture precedes provider mutations; the publication address retains its
  original lifetime across both opaque calls.

The request has two untouched padding bytes and the configuration has three.
They remain untouched as in retail. Native checks compare initialized fields
and surrounding storage, without claiming defined C padding bits. Guest-binary
checks compare all packet bytes and distinguish a zero-initialized configuration.
Float edge values are bit transfers; this function performs no float arithmetic.

The actual caller `func_151D1138` still has an unrecovered C placeholder. Its
original six-word call/common-epilogue window at `151D1310` loads the owner in
the JAL delay slot, restores RA and unwinds its 0x38-byte frame. Forty-nine
connected cases per stream verify that window. This does not convert or credit
the complete caller. The existing factory body in `generated_174BF0.c` and its
11-argument declaration are compatible; no helper source repair is needed.
The factory implementation itself is not executed by the opaque-provider model.

## Qualification and production evidence

The selected source preserves all **51 owner neighbors**, their relocation
bindings, literal pools and diagnostics. Both full-owner padding implementations
produce the same object, including metadata, and real Make replay reproduces it.

- All four streams (raw C, both padders and retail) pass **584 cases each**
  against an independent public-memory, ordered-call and packet model. Complete
  guest state and access traces agree because the direct instruction streams
  are identical. Original word 36 is an unreachable duplicate MTC1 retained
  literally. Eight synthetic high return addresses and three public payload
  overlap cases are guest-only checks.
- **213 fired access-prefix quadruples** compare complete guest state, including
  the dispatched word, at each selected access boundary. This is a direct-binary
  check, not a portable C trap-state claim.
- Typed SDK32 C passes **576 cases each at O0/O2/O3**, with strict aliasing and
  UBSan. All eight deliberate actor/view/parameter/request/copy/context/attachment
  errors fail by result comparison. Complete backing and guard regions are
  checked after pointer/endian normalization, with padding values excluded.
- **204 word/binding controls** show that both direct padders preserve detectable
  corruption across all 98 instructions and four relocation sites. They are
  mismatch controls, not guard rejections. Generic overflow remains visibly
  unmatched; generated padding rejects an oversized body.
- **12 independent GNU links** across four code/callee/global arrangements agree
  with original ASM. **96 guest rebase executions** preserve state, packet values
  and call order. A separately compiled zero-padding control changes observable
  retail packet bytes; native padding values are not credited.

Two fixture problems were corrected before the accepted paired runs: a synthetic
actor buffer overlapped the guest stack, and the freestanding i386 entrypoint
lacked alignment for optimized SSE stack stores. The corrected fixture asserts
public/stack disjointness; `_start` realigns its stack. Neither correction changed
the recovered C, direct match or full-image prediction. Earlier diagnostic
artifacts are retained privately and are not accepted qualification receipts.

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 135.593s | 5 fresh / 0 reused |
| preinstall-sibling | 112.127s | 5 fresh / 0 reused |
| installed-primary | 109.499s | 5 fresh / 0 reused |
| installed-sibling | 115.194s | 5 fresh / 0 reused |

The independent complete-image predictor recompiles frozen old C with the
unchanged guard CSV and replaces only this function with original ASM. It
reconstructs the function size and every ELF byte. Actual production matches
the prediction with **297 changed bytes and zero exclusions**. All **189,088
protected Game data bytes / 720 owners** remain exact. Real production Make,
the production recount and shared `make tools-check` pass.

```text
before ELF: 9999cd2e749bcb56978dbd18e9e09485cfd4819bfc5cbd653a3b7fd2d192421b
after ELF:  589d33abd291d98651f557223c00d9a1071c02adf8691dc87975f3d5a255d846
owner:      d1c5ecc65f69a8b6b3225cdb9d41de72c24ad59ea3927d4eb8e1cd5c7919ac5b
```

The shared guard CSV, conversion rows, layouts, headers, complete Debugger
object and every unrelated frozen object remain byte-identical. An initial
production Make inherited the previous task's newer CSV timestamp and began
rebuilding unrelated owners. That owned run was stopped with SIGINT and its
logs retained. The corrected command uses `-o retail_word_patches.us.csv` only
after verifying the entire CSV against the frozen baseline. The interrupted
run logged 178 assembler outputs. All 3,107 frozen inputs were audited: no
unrelated bytes changed and no outputs were missing. The final audit covers
every frozen input and the complete linked image, with no exclusions.

The real dirty sibling tools checkout is preserved through an isolated overlay
with explicit dependency origins. Both inspected host scene configurations
consume binary artifacts, and the selected scene lists this target as a stub.
No direct host C consumer or complete host build root was found there; no host
build, gameplay acceptance or frozen Release update is claimed.

Tools commit `5083b66d7e28e215797e8f811ce75de51a0ad19e` precedes
the consumer source/pin/docs commit. Nothing is pushed. README receives only
its two aggregate status rows; the five documentation indexes receive this
note's short entry while every prior document byte is preserved. Graphify's
scoped AST update and historical-ID retention follow observed hook completion;
this is not full-corpus extraction.

The 85% total goal remains active. Continue with the ordinary unmatched Game
queue from this committed checkpoint. The larger `func_15197148` renderer
remains private and uncredited in its own frozen build directory and handoff.
