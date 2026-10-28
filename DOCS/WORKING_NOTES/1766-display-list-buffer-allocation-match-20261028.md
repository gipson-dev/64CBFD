# 1766 - Display-list buffer allocation direct C match

Verified: 2026-10-28. Target func_15015E80, sole compact function in generated_43330.
VA0x15015E80..0x15015F3C /ROM0x43330..0x433EC: 47 body words, 188 bytes,
frame24 and twelve external bindings. One existing zero alignment word extends
the slot through VA0x15015F40 /ROM0x433F0. No guards or profile overrides.

## Recovered behavior and declarations

Replace the zero-return placeholder with void func_15015E80(void). Keep the
address-based symbol and a short allocation comment; do not infer a public name
for the unidentified configuration field. The source retains canonical
struct104 *D_800B0DF0, existing s32 slot storage D_800BE9C8[], and the actual
four-argument s32 allocate_memory ABI from init_3C40.c. No shared header changes.
The configuration halfword at+0x1C is currently padding in struct104, so access
it through a private u16 view without rewriting the shared structure.

1. If the live unsigned halfword is zero, store8000. Then reload the global
   configuration pointer and add400 with u16 narrowing. The zero case stores
   both8000 and8400; an initial0xFE70 wraps tozero without another default.
2. Allocate the first buffer with (liveCount<<3,255,2,0), then publish its
   returned32-bit address in slot0. Reload the configuration pointer/count for
   the second identical allocation and publish slot1. A provider may change
   the count or redirect the pointer between calls; do not cache the size.
3. Read the live slot addresses after the second provider, subtract in unsigned
   32-bit arithmetic, interpret the wrapped difference as signed32, shift right
   three arithmetically and subtract400 for D_800BEBA4. The provider may overwrite
   slot0 during the second call. Preserve negative, unaligned and wrapped gaps
   and nullable results; add no error branch or clamp.

Unsigned subtraction avoids undefined subtraction of pointers from different
allocations. Signed reinterpretation/right shift retain the measured N64/IDO
operations. The native32 harness uses integer address bit patterns and never
dereferences allocator results. It does not claim portable behavior for guest
pointer/halfword aliases or qualify the entire heap service.

## Literal body, bindings and actual call chain

Normal O2/g3 IDO emits all47 original instructions directly. The actual Make
route has three compiler/padder/assembler commands and reproduces the entire
qualified padded object. Twelve relocations comprise five HI16/LO16 pairs and
two J26 calls at body offsets80 and128. Owner pools and the alignment word are
unchanged. There are no neighbors or GLOBAL_ASM routines in this owner.

Raw original/selected body SHA256:
~~~text
fe10bd7c57a957a1ef3d7457edc21b452c0ffd3812a4d61d75be40f3557f3f62
~~~
Full original192-byte slot SHA256:
~~~text
b3e9c0160c5af5ce7b72b7b7d1667dbf53623369c38549996ca41b2942f3a155
~~~

The aligned ROM census finds one direct JAL at ROM0x3521C /VA0x15007D6C in
func_15007B3C, no tailJ and no target pointer literal. Frozen original ASM and
ROM agree on the four-word call window: target JAL/nop, then func_150162B0
JAL/nop. No V0 use occurs between calls, supporting the no-parameter void
initializer contract. Connect the first call and return and stop immediately
before the following JAL. The current parent remains its three-word stub;
this bounded window does not restore the whole parent or the next service.

The retained allocate_memory wrapper is eleven original words at10003C40,
identical in the current ELF. Its32-byte frame saves the return address at+28
and the original fourth argument in incoming home+12. It calls func_10003C6C
with positional arguments (arg0,arg1,arg2,0,arg3), placing arg3 in its outgoing
fifth-argument home+16. The target's24-byte frame plus this wrapper is56 bytes.
Do not label the original fourth argument as a pool selector: the wrapper
supplies zero in the inner service's fourth position. Keep the original s32
return and four-argument declarations. The inner heap remains an opaque bounded
provider in these tests, with caller-saved state and outgoing homes clobbered.

## Focused qualification and effective controls

Both canonical tools copies independently pass eight fresh methods and their
project-tool checks. Both installed copies then pass two fresh owner/image
methods and reuse six semantic methods only under exact module, snapshot,
sealed-input and qualified-artifact identity.

- 9,072 guest cases compare every private state/trace with literal retail and
  an independent public/call reference. Cover zero and u16 wrap,16 provider
  mutation modes, nullable/negative/unaligned/wrapped address pairs, and nine
  layouts aliasing configuration pointers, halfwords, slots and the limit.
  Reach all47 body instructions and retain the alignment word.
- 1,956 fired access-prefix pairs compare complete registers, private/public
  memory, access trace, PC and branch-delay ownership. Verify zero-default
  store order, live reloads and no default after wrapping tozero. Opaque
  provider controls clobber caller-saved GPR/FPRs, HI/LO and outgoing homes.
- 252 connected cases execute the original caller JAL/return, the initializer
  and all eleven retained allocator-wrapper words. Verify exact five-argument
  forwarding, stack restoration, live provider effects and ignored V0. Full
  parent, following-service, heap, hardware and gameplay acceptance remain open.
- Native32 O0/O2/O3 with trapping UBSan each pass327,680 positive cases: all65,536
  halfword encodings across five provider modes, with typed count records,
  full storage fences and call observations. Fourteen wrong default, increment,
  size, arguments, cached reads, signedness, rounding, margin and null-check
  variants fail by value or arguments. Keep deliberately aliased guest layouts
  separate from the native valid-storage corpus.
- Three independent GNU layouts pass192 guest cases, including signed low-half
  relocation carries, relocated J26 calls, live aliases and negative gaps.
  The actual padder matches the qualified object; three raw/binding corruptions
  and six whole-image corruptions are rejected.
- Three actually IDO-compiled C controls fail in mapped memory. Caching the count
  produces second allocation size67200 where the live reload gives136. Caching
  the first address produces limit130672 where the late read gives65136.
  Replacing arithmetic >>3 with truncating /8 gives-400 instead of-401.

An initial caller-comment parser missed the VA column. Preserve that failed
receipt in canonical-attempt1; the corrected complete eight-method rerun passes
in both copies without weakened semantics or gates. Route metadata now uses
positional allocator arguments. Routine Claude calls:0.

## Production, strict image and progress

The complete adopted ELF equals an independent149-byte prediction:148 target
instruction bytes and one target-size byte12->188. Zero exclusions; no symbol
or string permutation. All6,056 function addresses,6,055 other bodies, named
definitions,720 protected Game-data owners and189,088 protected bytes remain
fixed. Shared headers, current parent, actual allocator source/object, all
inherited guard rows, map and inventory CSV remain unchanged. Selected/owner/
actual-Make diagnostics are empty; production retains the existing duplicate
generated_12D630 Make-recipe warning.

ELF SHA256:
~~~text
9515b096c6de81fdf23abe68a1dd470de2b1280d1d009116fa7540997ad83477
~~~
Unchanged native CRLF guard manifest SHA256:
~~~text
1383ae8599001c8769a2557ce1e4d2791f5f3bb5fcf8b59e822cdbc12e618f85
~~~

Seal16,257 files and255 focused inputs. Recounting the actual captured native
ELF preserves the C inventory and gives:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,844 /5,506 (69.81%) | 1,662 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,171 /4,833 (65.61%) | 1,662 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_15015E80 becomes exact in this bank. The4,130 threshold leaves286 more
to75%. Remaining source screens:1,533 placeholders,120 semantic/other and9
unlocated. These screens do not qualify any pending body or the NULL factory.

Predecessor consumer7163e10a3801016653ac1f435d51a9963b3207b1 and tools
a4d9d22e4ac4634942b1c1594d3f52167bd394e1. Bank tools first at
59b50f29a362d76d1fe606634d8747d42fd487f7, then source, tools pin and seven
measured documents. Preserve1,742 inherited dirty mirror paths plus only the
two new modules. No push. Root README changes only its two aggregate rows.

Refresh ten structural C/Markdown/tools files. Retain old nodes or unique
relocations and all valid confidence/context keys; retire only the target's
false s32 return relation with committed void-signature evidence. Record the
real no-parameter void signature without inventing a void type node. Validate
one allocate_memory call relation against both source calls and the two J26
bindings. Add no production caller edge for the still-stubbed parent. Outside
freshness, communities and global analytics remain historical; this is no
full-corpus extraction. Receipts and independent audit live under
conker/build/game-display-list-buffer-allocation-match/.

Next inspect func_1506FD30 from a fresh predecessor. func_1514E920 stays parked
and uncredited. The75% goal remains active.
