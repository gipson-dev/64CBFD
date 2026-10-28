# 1762 - Record value restore guarded C match

Verified: 2026-10-28. Target func_151152A8, owner generated_142560.
VA151152A8..15115368 /ROM142758..142818: 48 words, 192 bytes, no frame.

## Source and original behavior

Replace the zero-return stub with void func_151152A8(u8 *record). Its original
callback caller passes the record in A0 and ignores V0. Keep the existing
address-based symbol and a descriptive comment. Add one local extern f32
D_800A2F8C; reuse the existing signed D_800BE9E4 declaration. Shared headers
and every other production function remain unchanged.

1. Load the signed baseline word at+0x7C. If zero, copy the signed halfword
   at+0x12 into it. Then load the current signed halfword again. Form baseline
   minus current with explicit modulo32 arithmetic.
2. If flags byte+0x4F has bit4, read packed+0x3C. Only when the difference is
   less than its signed low halfword, subtract signed high halfword times the
   signed tick count D_800BE9E4 and store the low16 bits. Preserve strict <,
   the rejected path's absent tick/factor reads, and wrapped multiply/subtract.
3. Otherwise, compute float(current) + ((float(difference)*factor)*float(ticks)),
   rounding each float32 operation in that order. Truncate to signed32 first,
   then narrow to the halfword. D_800A2F8C is bits3D4CCCCD, the retail 0.05f.
   Do not truncate the increment early or regroup the final addition.

The baseline store precedes later tick/factor reads, which matters when those
addresses alias record storage. The float path never reads packed+0x3C.
All 48 words are retained; 47 are dynamically reachable. The redundant delta
word at+108 follows an unconditional return and remains unmodified.

The initial C already emits the full 48-word shape and all six bindings with
empty diagnostics, but 25 words differ only in integer temporary registers.
Source screens for flag widths, casts, capture forms, compound updates and
record views did not solve that allocation. The selected source explicitly
casts the float result to s32 before halfword narrowing, matching trunc.w.s.

## Checked allocation guards

One closed ten-register cycle maps compiler temporaries to retail:
T6->T7->T8->T9->T0->T1->T2->T3->T4->T5->T6.
The 25 expected-word guards change only those GPR operands. COP1 transfers
change their GPR rt; FP loads/stores change only their address register.
FPRs, format fields, shift counts, opcodes, branch offsets and operations
remain intact. Six HI16/LO16 bindings at+4,+52,+76,+116,+120,+128 are preserved,
including the four guarded binding words. There are no inserted/omitted words,
new constants, fake fields, helper substitutes or compiler-profile changes.

Raw compiler body SHA256:
~~~text
5bbf43f04a0ee142a0cfbe8459884080b347ca3d4649f16902babfe706f1409c
~~~
Normalized/original raw body SHA256:
~~~text
293e0f2e158836f267e7414f2acb12a2d55b846ddf57497b2f6b570082fb358a
~~~

This is complete semantic guarded C. Direct compiler-only matching is not
claimed. The unnormalized compiler output also passes independent public
semantics; guarded execution additionally matches literal private state,
instruction traces and fault boundaries.

## Actual callback route and scope

The aligned ROM census finds no direct JAL/tailJ and one pointer at ROM22D798,
VA80088CD8: slot 6 of the 12-byte D_80088C90 records. Its three words are
(target,0,0). Do not infer a full table count from the next symbol address.

The actual 22-word original func_1509E900 window at VA1509EBBC /ROMCC06C
loads the chosen table entry, installs the callback at record+0x38, the second
callback at+0x78 and kind byte at+0x92. The actual five-word original
func_15113E54 window at VA15113EE0 /ROM141390 loads+0x38 and calls it with
A0 record, then advances its own counter without using V0. Five connected
cases cover both arithmetic modes, initialization and extreme ticks.

Both current production definitions remain unchanged zero-return stubs.
Original window evidence does not claim restored full registry/dispatcher
behavior, additional matching credit, live gameplay or hardware acceptance.

## Focused qualification

Both copies pass eight fresh canonical_v3 methods and shared project-tool
checks. Installed copies each pass two fresh owner/image checks; six semantic
checks are reused only after exact sealed input/module/artifact identity.

- 1,593 guest cases cover signed halfword/int32 boundaries, wrapped arithmetic,
  all 256 flag bytes, both modes and every one of 32 aligned tick and factor
  aliases in the record. Compare reference effects, complete normalized private
  RAM/GPR/FPR/HI/LO state and exact access traces. Also execute the actual raw
  compiler C output against the independent public reference.
- Native32 O0/O2/O3 with trapping UBSan each pass 393,222 positive cases.
  All 65,536 halfword encodings, both modes, disjoint ticks or valid s32 baseline/
  packed aliases, whole typed-storage fences, and threshold/truncation witnesses
  are covered. Float conversions are explicitly checked to be finite and in
  signed32 range before casting. Eleven wrong C variants fail effectively.
  Guest float/integer address aliases and nonfinite/out-of-range indefinite
  conversion models are separate from this valid native domain. No FCSR,
  exception-hardware, native type-punning or undefined-cast acceptance claim.
- 104 fired root memory-access prefixes preserve complete private state, trace,
  fault PC and delay ownership. Sparse mappings prove rejected integer paths
  need no ticks/factor and float paths need no packed word. Baseline and output
  store order is checked explicitly.
- Three independent GNU layouts pass 18 cases across all six bindings and
  signed low-half carries. The actual padder reproduces the qualified object;
  changed expected words/bindings are rejected. An actually compiled <=
  threshold variant changes 10 to 7 where retail keeps 10; the negative fails
  by value. Eight entire-image corruptions also fail closed.

Keep failed receipts. The initial test fixture assumed only three GLOBAL_ASM
routines; the actual owner has ten. Its rebase emitter needed real symbol
anchors, and the native corpus needed a threshold-equality witness. A signed/
unsigned rate cast is equivalent in the stored low16 result, so replace that
ineffective negative with a wrong rate shift; never count it as a behavioral
rejection. Final v2/v3 suites retain strict compiler flags and every required
image/semantic gate. Routine Claude calls: zero.

## Owner, Make and exact image accounting

The complete owner has 84 compact functions and ten GLOBAL_ASM routines.
Preserve all 83 other bodies, bindings and pools. Its actual five-command
asm-processor/IDO/postprocess/padder/GNU Make route and production reproduce
the qualified object byte-for-byte. Selected/owner/Make diagnostics are empty;
the inherited duplicate generated_12D630 Make recipe warning remains.

The first full-image assertion caught a three-name symbol/string permutation
introduced by the new factor reference. Definitions and addresses were stable.
Keep that failed receipt; the final predictor explicitly reconstructs the
closed reorder D_800A2F8C,D_8009078C,func_151A8A78 ->
D_8009078C,func_151A8A78,D_800A2F8C at the asserted symbol/string positions.
It does not copy metadata from the observed output or exclude sections.

The exact 187-byte ELF delta is 141 target-code bytes, one target-size byte
12->192, and 45 closed symbol/string bytes. All named definitions, 6,056
function addresses, 6,055 other bodies and 720 protected Game data owners /
189,088 bytes remain fixed. Map and inventory CSV are unchanged. The guard
manifest appends only the 25 qualified rows, preserving every inherited byte.

ELF SHA256:
~~~text
6fc32a5f2c15d1e97cc5e7c963f7ff07c47d0c8da90b7dbc93319cba25368f1b
~~~
Native CRLF guard SHA256:
~~~text
7a8a7a39ff6271b22dfb93589c78def9bf0b04d022adb5795ce3afa044c226a6
~~~

Seal 16,237 Native/cache inputs and 236 focused inputs. Recount the actual
captured adopted Native ELF with the same C inventory and classifications:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,840 /5,506 (69.74%) | 1,666 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,167 /4,833 (65.53%) | 1,666 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_151152A8 becomes exact. Threshold 4,130 leaves 290 more matches to 75%.
The queue retains 1,537 placeholders, 120 semantic/other definitions and nine
unlocated entries. Typed func_151725FC and NULL func_1518F5D0 stay uncredited.

Predecessor consumer b2b461cb42d1792f8d58be2302a30bcdbeb98624 and tools
9b6dcfaf4390cd65691a77ec5ae382e127f4896c. Bank tools first at
c57fb83690ae63f4645136eb9c5fec5464f3e3ec, then source, 25 guard rows,
consumer pin and seven measured documents. Preserve the older mirror's 1,734
inherited dirty paths plus two new files. No push. The root README changes
only its two aggregate matching rows; detailed recoveries remain here.

Refresh ten changed structural C/Markdown/tool sources after committing.
Retain all old nodes and source-valid confidence/context relationships.
Retire only the target placeholder's false s32 return relationship after
validating the final void signature; preserve the u8-pointer parameter and
leaf body. Do not add caller edges from current placeholders. Keep outside
freshness and communities historical, with no full-corpus extraction or global
clustering/centrality claim. Receipts and an independent final audit live under
conker/build/game-record-value-restore-match/.

Next inspect func_15169988 from a fresh frozen predecessor and caller/ABI
audit. func_1514E920 remains parked and uncredited. The 75% goal stays active.
