# Actor/List Query Match - 2026-11-08

`func_150229E4` is byte-exact across all **73 words / 292 bytes**, with no
stack frame. Total **4,252 / 5,513 (77.13%)**, Game **3,579 / 4,840 (73.95%)**,
Init **492 / 492**, Debugger **181 / 181**. Address drift remains zero;
1,261 converted functions remain different. Another **159** exact functions
reach 4,411 / 5,513 and the active 80% goal. Conversion totals are unchanged.

## Recovered source and interface

Owner: `conker/src/game/generated_49D30.c`. VA 0x150229E4..0x15022B08;
ROM 0x4FE94..0x4FFB8. The zero-return placeholder becomes:

```c
s32 func_150229E4(struct127 *actor)
```

The existing SDK actor type has an 812-byte stride. Its signed interaction
state is at +0, the opaque unsigned group-selector byte at +5, identity byte
at +3B and linked-slot byte at +65. These fields retain their existing names;
no speculative global actor-base alias or shared structure edit is added.
The local existing `GroupActorRecord15022528` descriptor has an eight-byte
stride, unsigned halfword kind at +0 and identity byte at +2.

Return zero for a null actor, zero interaction state or null global group-zero
enabled-list pointer. That final gate applies even when the actor selects
group one. Select group one only when the actor's +5 byte equals four.
For a nonzero linked slot, read its identity from `D_800CBFDF[slot * 812]`;
otherwise use the actor's own identity. Capture the selected unsigned count.
Only a positive count loads the selected enabled pointer. Scan its halfwords;
only an enabled row reads the live descriptor-table pointer, row kind and,
when kind equals two, row identity. Matching direct actors return one;
matching linked identities return two. Exhaustion returns zero. There are no
stores, calls or floating operations in this function.

The owner forward declaration is typed. `generated_58F80.c` also corrects its
old `u8 *` declaration and computed-slot call cast with an incomplete
`struct struct127` tag, preserving that owner's includes. Its full padded
object remains byte-for-byte unchanged. The already typed declaration in
`generated_A9260.c` is retained.

## Original caller qualification

The aligned pristine-image census finds eleven direct JALs, no entry/interior
pointer literals and no direct interior entries:

| Caller | JAL VA | JAL ROM |
| --- | --- | --- |
| `func_1501DE18` | 0x1501DEB0 | 0x4B360 |
| `func_1501EA18` | 0x1501EBA0 | 0x4C050 |
| `func_1502378C` | 0x15023800 | 0x50CB0 |
| `func_1502C1A4` | 0x1502C270 | 0x59720 |
| `func_1502C974` | 0x1502C9DC | 0x59E8C |
| `func_1502E4C4` | 0x1502E568 | 0x5BA18 |
| `func_15052590` | 0x15052624 | 0x7FAD4 |
| `func_15056B08` | 0x15056B54 | 0x84004 |
| `func_1505E650` | 0x1505E698 | 0x8BB48 |
| `func_150623F4` | 0x150624A4 | 0x8F954 |
| `func_1507C22C` | 0x1507C2BC | 0xA976C |

Sixty-six connected cases execute each original JAL/delay slot and original
return branch for retail, raw C and normalized C, against an independent
reference hook. Ten windows contain four original words; `func_1505E650` uses
seven, including its saved floating argument and stack reloads. Null,
inactive, absent, direct and linked cases qualify the call packet, memory,
saved registers, SP/RA and branch destination. The computed slot pointer and
actual delay-slot stores are exercised. Full parent routines are not claimed.

## Derived normalization

The semantic C emits all 73 words using the owner's existing retail
`-O2 -g3 -Wo,-loopunroll,0` profile. **55 expected-word/relocation guards**
normalize lifetime-specific register cycles and compiler address reuse.
Retail rematerializes the enabled-table address along its two paths, rather
than retaining the compiler's complete address. Eight raw bindings become ten
normalized bindings. The captured count and enabled pointer, linked identity,
kind-two setup and loop temporaries retain their logical lifetimes.

The first state gate changes the raw branch-likely schedule to retail's
ordinary branch/NOP and moves the same executed gate load after the successful
state test. An unreachable duplicate raw gate load supplies the NOP; no
executed load is removed. The cached-address ADDIU becomes a cloned LUI, with
its LO binding replaced by HI and the original loads receiving their LO
bindings. Branch destinations follow the derived origin permutation. No body
is copied into inline assembly, no instruction slot is inserted, and no new
gameplay state transition is supplied by guards. This is a guarded match,
with explicit address-rematerialization normalization, rather than an
unguarded compiler match.

Raw C SHA256:
`89aa4cb3ae59362a10d7cca9f45121729f33a1e380fb44c9d31ca51abf6ed045`.
Normalized relocatable body SHA256:
`19a0f87ed1f4f63db473d82fffd057a64f20eff2ded0355455f9de20e3e75f19`.

Every one of 73 raw-word corruptions, eight altered bindings, 55 stale guard
words, 55 stale guard relocations and 96 metadata-byte corruptions is rejected.
The inherited guard CSV is preserved byte-for-byte as a prefix. Three
independent GNU links qualify original and rebased symbols, including signed
low-half carries. No compiler profile or Makefile changes are made.

## Whole-owner and image proof

The 108 frozen inputs cover both C owners, their original assembly, referenced
GLOBAL_ASM files, SDK headers, assembler includes and compiler/link inputs.
All 56 neighboring raw and padded functions, both owners' data pools and full
register metadata remain fixed. All 38 functions in the corrected caller
owner remain fixed. Strict and production padders agree for the complete
57-function target owner. Actual Make reproduces its three-command recipe
and the caller's five-command recipe. The caller recipe retains its existing
`jtbl_80096DF8_game` rodata alias.

The literal full-ELF predictor permits exactly **222 changed bytes**, with
**zero exclusions**, no symbol/string permutations and only the target body
and its restored function-size field. All 6,053 function addresses, other
bodies and all 720 protected-data owners / 189,088 bytes remain fixed. Four
controls reject changes to the header, code, size field and protected data.

## Execution and production evidence

Both tools configurations pass six checks before and after installation in
four sequential fingerprinted runs. The sibling uses a scratch overlay for
these three new modules, with read-only helper fallbacks recorded explicitly.
Its HEAD and all 2,434 inherited dirty paths are preserved. Both configurations
pass fresh shared smoke checks; three unchanged shared synthetic regressions
per configuration are reused only under exact helper/test fingerprints.

- **1,428 guest cases** cover every count byte, both groups, null/state/gate
  paths, unsigned flag and kind boundaries, identity boundaries, linked slots,
  six alias layouts and both stack phases. All three bodies produce identical
  ordered data reads, return values and unchanged input memory.
- All **71 reachable words** execute. Duplicate words at 0x15022A24 and
  0x15022AEC follow terminating paths without incoming branch targets; both
  remain preserved and are not credited as executed.
- **113 executed memory-fault cuts** compare complete literal retail and
  normalized states. Raw C's register/fault schedule is not claimed literal.
- **1,314 native cases per executable** pass O0/O2/O3 with trapping UBSan,
  32-bit pointers, SDK actor/descriptor sizes and full input digests. High
  linked slots and address aliases are guest-only. Thirteen effective
  controls reject a stub, ignored state/group-zero gate, wrong group,
  linked stride/index/identity, ignored or signed flags, byte-sized kind,
  wrong descriptor stride, wrong linked result and signed count. The two
  groups have distinct fixtures, so the wrong-group control is observable.

Production compiles exactly two C owners without C diagnostics, then links
the exact predicted ELF. `make all` retains the expected checksum exit 2
because other functions remain unmatched; compilation/link and the fresh
recount succeed. `progress.csv` is unchanged. README edits contain aggregate
rows only; function detail stays in this note.

Production ELF: `cf8350b1a35a1cca76de197c1f9047b89b0cb0f67e0c13b63be328abfd51a479`.
Binary: `10021ac113bfe164ef319115fb38fd783dfedfafeb6db307d99832144f506e3c`.
Owner: `3e884aaeeb78d69b73cf521e22890b7ee268ed7570395a1720d010a961202847`.
Unchanged caller object: `f95b5939eb7cd5a804bd15d86168bdaee9417ea9891fa569a1cb262aabd1d2d5`.
Guard CSV: `931b6ca3673b8157c374871d9065dffbf39d419211960ab9383c6503808f7f25`.

## Resume boundary

Next ordinary C candidate: `func_15100340`, a 73-word routine with a
0x50-byte frame in `generated_12D7F0.c`. Its five-slot random-toggle/event
loop and all caller/data paths still require complete qualification; it is
uncredited. The smaller handwritten/nonstandard-register cases remain
separate work without false C-match credit.

Scratch receipts: `conker/build/game-actor-list-query-150229E4-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
retains unscanned existing nodes and audits changed-path relocations; it is
not a full-corpus extraction. Frozen host Release artifacts are untouched.
