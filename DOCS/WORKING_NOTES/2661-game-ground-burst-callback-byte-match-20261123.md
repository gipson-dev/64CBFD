# Ground-burst destruction callback byte match - 2026-11-23

`func_150DF334` replaces its zero-return placeholder with its complete semantic
ground-contact and effect-submission routine. The retail **97 words / frame 152**
and **five relocation sites** are byte-exact after a pinned, independently
qualified normalization of **98 raw C words**. There are **98 expected-word
guards, two inserted words and three omitted source words**. This is a guarded
match; it does not emit directly from C without normalization.

Total rises from **4,640 to 4,641 / 5,528 (83.95%)**; Game becomes
**3,968 / 4,855 (81.73%)**. Init remains 492/492 and Debugger 181/181.
There is **zero address drift**, 887 different functions and **58 more to 85%**.

## Recovered behavior and actual interfaces

The complete original is `conker/asm/10C170.s:435`, VA
`150DF334..150DF4B8`, ROM `10C7E4..10C968`. The actual death table
`D_8008A4C0` has this callback at slot 8 (`8008A4E0`), in
`conker/asm/data/22EF80.rodata.s:16`. The recovered `void(struct260 *)`
interface agrees with the full 45-word `func_15149264` dispatcher.

1. Copy owner coordinates at +0x28/+0x2C/+0x30 into a private probe, raising
   Y by 500. Query `func_1504697C(probe,0,probe.y-1000,&ground)` using its
   actual `s32(f32 *,u16,f32,HeightResult71820 *)` interface. The 36-byte
   result preserves its original fields and arbitrary initial/padding bytes.
2. On success, capture the owner's live post-query X/Z and returned height.
   Otherwise select the owner's live coordinate vector. Retain that selected
   pointer across the first random call, then submit the timed effect with
   unsigned `random%62+120`, narrowed to s16, and live channel/context bytes.
3. After the timed submitter returns, re-select contact versus owner and copy
   all three words into a separate burst vector. Raise its Y by 500 and call
   random again. Submit all nine original `func_151A9834` arguments: the burst,
   its live Y-1000 threshold, radius 250, the same ground result, unsigned
   `random%3+3`, selector 1, NULL tag and live channel/context bytes.

The random provider remains the actual handwritten `func_150ADA20` in
`game_DAE50.c`; its low 32 return bits are interpreted unsigned by this caller.
The 49-word timed submitter `func_150E83AC` remains original active assembly;
its disabled C equivalent is not substituted as evidence. Its
real interface is `void(struct17 *,s16,u8,s32)`. The ground and burst helper
bodies use supplied positions/result data; no numeric private-address identity
is introduced by this recovery. Their transitive implementations and gameplay
acceptance are outside this callback's qualification.

## Source fit, normalization and independent proof

Default existing O2/g3/MIPS2 is retained. The initial draft compiled 99/frame 144;
the first ternary fit compiled 98/frame 152. Native checking exposed unspecified
C argument evaluation order when a random call and owner-byte reads occupied
the same argument list. The selected source now explicitly captures
`firstPosition`, calls random, and only then evaluates the submission arguments.
It separately sequences the second random call. This retains 98/frame 152,
changing only an independent pointer reload versus lifetime-narrowing schedule.
No volatile declaration, compiler change or synthetic semantic helper is used.

The normalizer derives output from pinned raw instructions and bindings. It
shifts the complete escaped 76-byte vector/result block down four bytes; frame,
callee saves, outgoing homes and selected-pointer home remain fixed. It removes
an unescaped cached owner-base home and rematerializes owner+0x28, converts the
branch-likely position selection to the retail ordinary-branch/delay-slot
shape, and normalizes two independent local instruction schedules. It does not
copy a retail body into the production source or import the retail words.

A separate finite-path interpreter imports neither the projection nor its
instruction map. It proves both zero/nonzero ground-result paths with symbolic
owner words, arbitrary initial private bytes, unsigned random results, ordered
floating operations and compatible opaque o32 calls. Every call may change
public state and every previously escaped bounded private buffer. It checks
ordered public reads/calls, pointer-role-related arguments and escaped-buffer
contents, and restored o32 saved registers. Eight semantic mutations must fail
by observation mismatch; harmless T6/T7 register renaming must pass.

The proof covers normal nontrapping executions in mapped ordinary RAM with an
owner disjoint from the private frame, under private-pointer renaming. Numeric
private-address/return-address reflection is outside that contract. Raw versus
retail private/fault-state identity is not claimed. Both padded streams and
retail have literal complete state and fault-prefix identity in the guest tests.

## Fresh qualification and complete linked audit

| Run | Elapsed | Gates |
| --- | ---: | --- |
| preinstall-primary | 148.055s | 5 fresh / 0 reused |
| preinstall-sibling | 263.562s | 5 fresh / 0 reused |
| installed-primary | 142.039s | 5 fresh / 0 reused |
| installed-sibling | 127.964s | 5 fresh / 0 reused |

- 272 guest cases per stream: zero/positive/negative query returns, both unsigned
 random ranges including sign-bit/full-word extremes, live owner changes,
 selected-position writes and retained escaped-buffer writes. All 97 retail
 instructions execute in the cases. Both padded streams and retail agree in
 every private byte and register; raw C agrees under the qualified address relation.
- 157 full dispatched-word/access fault prefixes across the two padded streams
 and retail; no raw/private/portable-C fault claim.
- The complete original 45-word dispatcher executes 15 cases per stream, update
 index -1, death index 8 and 15 final retirements through a compatible opaque
 retirement provider. Full caller return/effects agree; no extra caller credit.
- 272 native32 cases at O0/O2/O3, strict aliasing and UBSan, typed backing and
 exact layout assertions. The 192 guest cases with untouched/partial initial
 ground bytes remain guest-only; native adds 192 corresponding fully initialized
 variants, alongside 80 directly shared initialized cases. Initial/padding-bit
 identity is not claimed for native C. Seven source controls all reach known
 result-comparison failures; signals and sanitizer traps are not counted.
- Both strict padders reject 206 changed-word/binding controls covering all 98
 source words and all five sites. Twelve independent GNU links and 64 guest
 runs qualify four independent code/callee arrangements.
- The real Make owner recipe, both full padded owner objects, two unchanged
 neighboring functions, pools and diagnostics agree. Independent reference
 construction uses frozen old C and original target ASM, then predicts every
 byte of the full ELF. Actual C linking and production Make agree with it:
 **284 changed bytes, zero exclusions**, all 189,088 protected Game data bytes
 and 720 owners exact, no named-definition/metadata changes beyond target size.

```text
before ELF: d22581018f435e71dde2322d1de70655c4ab0ce4193227f0912da30b285ee5db
after ELF:  59ab46e1e44ec85c881dd0129386500be582a270c8fcdcb417593c7f75d2e540
owner:      fbb229762b7f0997264a458b2b0e36f6fdca2bdea7785593efdfd969a18f910d
```

The complete prior guard history is retained byte-for-byte, with only 98 target
rows appended. Actual Make holds the inherited CSV dependency timestamp old
with `-o retail_word_patches.us.csv`; the changed source still rebuilds its owner
and reads the new guards. All unrelated objects, data, addresses, extents,
conversion rows, layouts, headers and Debugger bytes are independently audited
unchanged. Prior unchanged neighbor-suite receipts are reused by frozen hashes;
they are not called fresh tests. Shared `make tools-check` also passes.

Tools commit `c1cffdd94582ffcb8c66bde158e5ebae91a54170` precedes source,
guard CSV, consumer pin and documentation. The dirty real tools sibling is
preserved through a separately pinned overlay. Both inspected host scene configs
consume binary artifacts; one lists this target as a stub. No direct C consumer
or complete host build root was found there, and no host build or Release change
was made. There is no new emulator/gameplay acceptance claim.

Claude preflight found no authenticated route; zero model calls were attempted
or completed, and no account/provider/model setting was changed. Codex resolved
the source-order and private-address questions locally. Graphify receipts
separate normal fail-closed refresh, actual hook completion and a scoped AST
merge that retains old IDs; no full-corpus extraction is claimed. README changes
only aggregate rows; old DOCS bytes are retained by short index insertions.

The 85% goal remains active. Continue ordinary unmatched Game entries from this
committed checkpoint. The larger `func_15197148` renderer remains private and
uncredited on its older frozen baseline.
