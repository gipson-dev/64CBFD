# 2655 - Actor preset constructor guarded byte match

Date: 2026-11-23. The total 85% byte-matching goal remains active.

`func_15196438` replaces a zero-return placeholder with complete semantic C.
Its **196 words / 784 bytes / frame 248** match the original through a
closed, source-derived transform. This is a **guarded C match**, not a
direct compiler match. Original: `conker/asm/1C2C60.s:950`, VA
`15196438..15196748`, ROM `1C38E8..1C3BF8`. The owner remains
`conker/src/game/generated_1C2C60.c`, default O2/g3/mips2/o32.

Fresh production recount: **4,635 / 5,528 (83.85%) total**, Game
**3,962 / 4,855 (81.61%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, **893 different**. **64 more matches** reach 85% at
this denominator. Conversion rows are unchanged: the replaced stub already
counted as C. Exactly one additional match is credited.

## Recovered interface and behavior

```c
u8 *func_15196438(struct127 *actor, s32 presetIndex, s32 channel, s32 context);
```

1. Return null when the actor or its matrix pointer at +0x1D4 is null.
   Capture the owner and unsigned ID at +0x3B into a private 0x90-byte packet.
2. Select one 0x60-byte preset from the seven-record `D_800A87A0` table.
   Copy the recovered lifetime, flags, callback selectors, attachment index,
   vectors, scales and remaining offset-named fields. Initialize only the
   original zero fields. Unknown fields retain offset names; gaps are not
   assigned invented semantics or gratuitously zeroed.
3. If its signed sound selector is not -1, invoke the zero-argument callback
   in `D_8008F890`, retaining the unsigned16 sound handle. Otherwise use zero.
   Reload the owner's matrix pointer after this callback, select index*64,
   then reuse that selected matrix for both point transforms.
4. Form the 28-byte request at SP+0xDC from the transformed first point,
   lifetime, flags, kind 3 and count. Call `func_15147A80` with all eleven
   original arguments, including the unsigned low byte of channel and the
   complete context word.
5. On success, capture the payload pointer at result+0x98 and copy the full
   private packet. Apply the optional `D_8008F870` floating scale callback
   using the payload selector; store through the captured payload even if
   the callback replaces the object's public payload pointer. Invoke the
   optional setup callback through `D_8008F87C` using the private captured
   selector, then return the allocated object.

The point type contains a genuine three-float array. Owner fields use the
existing SDK32 `struct127`; the payload pointer is loaded with its existing
`u8 *` field type before casting. Native checks read only initialized fields.
The guest oracle independently seeds and checks the original uninitialized
packet/request gaps copied by memcpy. Those gap bytes are not portable C
initialization guarantees.

## Sound return-chain repair with zero extra match credit

The sound callback `func_15198C60` already has an s32 callback ABI, but its
source omitted the return of `func_10010F30`. The latter also discarded the
u16 result of `func_10010BE8` and was incorrectly declared void. Restore
explicit forwarding returns, use the canonical u16 audio API in its Init
definition/shared header and three explicit Game declarations, and promote
that unsigned result through the existing s32 callback ABI.

All existing machine code remains identical. Complete old/new padded
objects preserve Init's 54 functions, Game declaration owners' 29, 44 and
4 functions, and all 328 functions in `game_981E0`. Adding the 68 constructor
neighbors protects **527 existing functions**, their relocations, literal
pools and diagnostic sets. The generated_113D60 check uses its actual Make
rodata symbol `D_800A1350`; no metadata/binding exclusion is permitted.

The actual selected C return chain runs at O0/O2/O3 with SDK32, strict
aliasing and UBSan across all 256 channel bytes and 517 sampled unsigned16
handles plus five explicit boundaries (133,632 cases per profile). The
constructor, actual 12-word Game callback and actual 22-word Init wrapper
also execute together in 70 guest cases per stream, with only the final
seven-argument voice allocator bounded by a provider. No audio hardware
acceptance or additional match credit is inferred from the return repair.

## Source-derived instruction and ABI qualification

The selected compiler output is **196 words / frame 248**, with **42 real
word differences**. The normalizer uses all 196 source operations exactly
once, adds/drops none, and consumes pinned words and all twelve relocation
sites. Original ASM is an independent comparison, never the generator.
All 196 expected-word CSV rows protect the complete body; 154 are identity
guards. The old CSV is an unchanged prefix.

The compositional symbolic proof covers every word: 144 literal identities,
a 33-instruction straight-line preset-load/private-store scheduling region,
one byte-argument ABI operation, and an 18-word closed pointer/selector
register allocation region. It compares immutable preset reads, private
writes, live integer/float roles and dead-role lifetimes through later
branches/call clobbers. This is a restricted region proof, not full-path SAT.

Word 134 is explicit ABI restoration: raw LW reads the current full incoming
argument2 word; retail LBU at address+3 zero-extends its low byte into the
complete outgoing o32 word9. The actual allocator's LBU at ROM174F74 proves
its canonical u8 formal consumes only that byte. Raw full outgoing words
are not claimed identical. Normalized execution reproduces the full retail
word, private state and instruction access order.

- 554 independent preset/constructor cases per raw/normalized/padded/retail
  stream cover 512 synthetic cases and 42 cases using real table records.
  Callback mutations exercise owner-ID/matrix changes, payload replacement
  and private versus public setup-selector lifetime. Only raw outgoing-word9
  high bytes differ; normalized complete states equal retail.
- Eight additional guest-only private aliases exercise incoming argument2
  mutations, self-copy and payload destinations overlapping caller homes.
- 1,387 fired own-access fault prefixes compare complete normalized/padded
  versus retail state. These qualify emitted access order, not native C
  exception semantics or hardware behavior.
- 140 caller cases execute both complete original 13-word wrappers
  `func_1506FCC8`/`func_1506FCFC` and two original three-word call windows
  at 150DBA18/150DBC40. Full `func_150DB9E0` remains outside that claim.
- Native SDK32 constructor checks run 554 cases at O0/O2/O3 with strict
  aliasing and UBSan, checking 37 preset, 51 initialized payload and seven
  request fields. Ten effective semantic mutations fail as expected.
- Both complete owner padders reject all 196 changed source words and
  twelve changed binding sites: **416 fired rejections**. Both reject
  oversized bodies. Thirty-two symbolic mutations fail as expected.
- Twelve GNU links over four independent code/global arrangements verify
  HI16/LO16 carries and JAL target-region constraints. Both padded bodies
  and original ASM agree under each arrangement.

Fresh target suites are recorded separately for both tools surfaces before
and after installation; each runs five focused checks without reuse:

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 174.199s | 5 fresh / 0 reused |
| preinstall-sibling | 165.213s | 5 fresh / 0 reused |
| installed-primary | 156.138s | 5 fresh / 0 reused |
| installed-sibling | 149.833s | 5 fresh / 0 reused |


## Production, ownership and checkpoint

Actual Make replay reproduces the full independently padded owner. The
strict image predictor first compiles frozen old C with old guards, then
substitutes only original target ASM. Every production ELF byte equals the
independent prediction: **627 changed bytes, zero
exclusions**. Named definitions, metadata ordering, every string byte,
189,088 protected Game data bytes and 720 data owners are accounted for.
Every frozen input is checked against an explicit six-source/header,
guard, target-object, audited debugger metadata and ELF adoption plan;
no dependent-object exclusion is used. Shared `make tools-check` passes.

The full rebuild exposed one additional object delta in
`conker/build/src/debugger_258ED0.c.o`. Every non-debug section, relocation
and symbol is unchanged. Its complete `.mdebug` delta is reconstructed
from 43 uniform compiler timestamp fields and the `functions.h` recorded
length, 44,179 to 44,258 bytes. Six controlled actual Make commands with
old/new headers independently reproduce that provenance change, and an
unrelated metadata mutation is rejected. The complete production object is
pinned as `e7ee62423430a1ec75906e1a853b0b51d0249003f0db4747a63a650e0f44eac5`.
No metadata bytes are skipped and no extra function is credited.

The two original preinstall suites remain immutable receipts against tools
`718c413`. A focused metadata extension is separately checked through both
tools surfaces and committed afterward; both full postinstall suites run
fresh against that extension. Constructor source, normalizer, guest/native
oracles and their qualification results are unchanged by this extension.

```text
before ELF: 8d4cf1ee357e3d3d6d00af45876b95fb1befc348920c2955d9dfe5258145b88c
after ELF:  e5b2950028dd7a2e711e0500074abbe5790be86c2d390b0ba7eddee9cce9e47d
owner:      934e01b15846655a96c822d509b8f95b69fb2d6b911080e9f102eaa3a062e614
```

The paired sibling overlay explicitly records 1714 files
and its sibling/primary/task origins. The real dirty tools sibling's HEAD,
status and dependency hashes remain untouched. Host scene configuration
applicability was rechecked: there is no direct source consumer requiring
an edit. No host binary, Release artifact or gameplay acceptance is changed.

Tools are committed before consumer source/guards/pin/docs; nothing is
pushed. Graphify is refreshed with old-ID/qualification retention after
observed hook producers finish, recording the actual definition and repaired
return ABI. Scoped AST retention is not full-corpus extraction. Root README
contains only refreshed aggregate rows; this document owns the narrative.

Next audit `func_15196748`, the following unfinished Game routine under the
same owner profile, with fresh ABI/caller/source qualification. The 85%
goal remains open. Codex is the only writer; Claude calls: zero.
