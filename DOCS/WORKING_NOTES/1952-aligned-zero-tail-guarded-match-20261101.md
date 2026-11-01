# Aligned zero-tail block relocation matched from guarded C

`func_1509B950`, owner `game_C8950`, is now byte-exact across all **45 words**.
The zero-return C placeholder is replaced with a semantic pointer-in/pointer-out
routine. Six expected-word guards close two temporary-register lifetimes; 39
words emit directly. No instructions are inserted or omitted and the compiler
profile remains retail O2/g3.

Fresh Native actual-ELF recount: **4,023/5,507 (73.05%)** total, Game
**3,350/4,834 (69.30%)**, Init 492/492, Debugger 181/181; zero address drift,
1,484 still different. This replaces an existing C stub, so the denominator
stays fixed. The 75% threshold is 4,131: **108 more** are required.

## Interface and recovered behavior

Source: `conker/src/game_C8950.c`. VA `1509B950..1509BA04`, ROM
`C8E00..C8EB4`, 180 bytes, frame 32, S0/S1/RA saved at SP+14/+18/+1C.
The interface is `struct248 *func_1509B950(struct248 *block)`; the structure
already describes the six original halfwords. The source header's +4 halfword
is the block size, +6 the zero-tail size, and +A the new tail offset.

1. Capture the tail size before changing the source header. Compute the next
   eight-byte boundary after source+length. An already aligned end advances
   eight bytes, rather than staying at the same address.
2. Retain the intermediate +4 halfword store, write the tail offset to +A, then
   advance the combined tail end to the next eight-byte boundary. Header writes
   truncate to 16 bits exactly as retail does.
3. Call the actual four-s32-argument `allocate_memory(size,255,2,0)` wrapper.
   Its s32 result carries pointer bits; convert it to the allocated block type.
   A null result enters the original nonreturning two-instruction spin.
4. Reload source+4 after allocation for `bcopy`; reload destination+A and +6
   after copying for `bzero`. These live reads matter when providers mutate
   headers. Free the original through `func_10004074`, then return the allocated
   pointer even when the free provider clobbers its return register.

The local forward declaration is corrected from s32 input/result to the proper
pointer types. The existing caller now loses precisely its pointer/integer
argument warning; the other two inherited owner warnings are unchanged.
No shared header declarations are changed.

## Code generation and closed guards

Raw SHA-256:
`6c44e98a6f2f7f773f28487d8263edbd9291a9c75b057d03c359113d7db77f2a`.
All four R_MIPS_26 helper bindings are pinned at +5C/+7C/+8C/+94.

| Offset | Compiler word | Retail word |
| --- | --- | --- |
| +28 | 030F5023 | 030F1823 |
| +2C | 004A4021 | 00434021 |
| +30 | 01091821 | 01091021 |
| +34 | 02035821 | 02025821 |
| +3C | 006C6823 | 004C6823 |
| +40 | A6030004 | A6020004 |

These rename padding T2 to V1 and combined size V1 to V0, including all uses
through the intermediate halfword store. No changed binding or scheduling
insertion is hidden. Each of the six stale-word mutations rejects in the real
padder, using the complete owner object. Raw payload and binding corruption
controls also reject. Naming the padding and retaining the header readback
recovered both the extra arithmetic word and retail's intermediate store
naturally; no volatile cast or filler was added. The separate donor's commented
attempt used a volatile write and was not adopted.

## Qualification and actual production

- Freeze 1,022 focused Native inputs and the previous 17,550-file complete seal.
- Guest: 1,418 cases / 5,672 executions across three entry/helper layouts;
  original, guarded, actual-Make and raw C programs. All 45 words execute.
  The three exact programs agree in complete state and access trace. Raw C
  agrees in public memory, calls and trace. Includes source/destination aliases,
  alignment residues, large halfword boundaries and live provider mutations.
- Allocation failure: six cases / 24 executions. A dedicated witness sees the
  loop PC three times, confirms exactly one allocation call and frame retention;
  a generic instruction-budget exception is not accepted as proof.
- Forty-two access prefixes / 126 executions agree across the three exact
  programs. This qualifies guest instruction order, not portable C fault behavior.
- The complete 21-word original `func_1509B8FC` caller passes 48 cases / 768
  executions, including signed low-halfword arguments and four post-call return
  poisons. Its void caller does not consume the result; its outgoing V0 remains
  unconstrained. ROM census finds one aligned JAL at C8DE8, no aligned tail J
  or literal pointer. The upstream resource loader remains a bounded provider.
- The complete 11-word original allocation wrapper passes 96 cases / 384
  executions. The nested five-argument heap allocator remains a provider.
  Copy, zero and free effects are bounded providers; no full allocator/libc or
  hardware acceptance is claimed.
- Native32 O0/O2/O3 each pass 576 UBSan cases, background canaries and eight
  effective controls: first-boundary rounding, allocation flags, cached copy
  size, cached zero offset/size, missing release, wrong result and wrong offset.
  Native cases use small valid disjoint buffers; large/alias cases are guest-only.
- All 16 raw/padded neighbors and owner pools are unchanged. Actual five-command
  Make produces the qualified object. The independently predicted complete ELF
  differs from baseline in exactly 143 bytes: this slot plus symbol extent
  16 -> 180. No exclusions, metadata exceptions or object reorderings.
- All 6,056 function addresses remain fixed; 6,055 other bodies are unchanged.
  Protected Game data remains 189,088 bytes / 720 owners, exact.
- Six public tests in each tools copy pass before and after installation, with
  shared checks in both copies. Full production Make, complete-seal changed-file
  audit and independent Native actual-ELF recount pass. Only source, guard CSV,
  owner object and ELF change among the previous sealed inputs. C inventory
  CSVs are unchanged; there are no unplanned dependent-object changes.

Production ELF SHA-256:
`0c7cc112eb7b61f6e3322e8d4e84dbdaea048cad244c5aca5f941ac33eec3cbb`.

Retained failed receipts are fixture/predictor corrections, not passing gates:
the old template assumed a 12-byte stub symbol while this actual stub is 16;
the caller poison wrapper needed its explicit empty ends tuple; native helper
definitions were corrected to the SDK's int count prototypes. Candidate C and
six guards did not change during those corrections. Only the corrected complete
runs are credited.

## Queue correction and continuation

The previous Note 1951 handoff's `func_150A76F0` recommendation is superseded.
It is handwritten custom-ABI assembly: T4 input, fixed T9/S7/S6 state, F8 result,
and return via V0, with six continuation jumps. Note 1314 and prior audits
already keep it in a separate register-contract workstream. Do not invent a
normal C ABI or reclassify it to improve this goal's percentage. The adjacent
matrix-pack routines using 64-bit sd instructions likewise need separate review.

Next audit **func_15163FEC**, owner `game_18D770`, a verified zero-return C stub
with a 53-word retail slot at VA15163FEC..151640C0, ROM19149C..191570.
Inspect its complete three-argument ABI, helper and caller contracts before
screening. No source change or match is credited for that next target.
Private relative-direction, motion, owner-gate and other candidates remain
uncredited. The 75% goal remains active. No Claude calls, push, host/editor or
Release changes. Current evidence is in
`conker/build/game-aligned-zero-tail-1509B950-match/`.
