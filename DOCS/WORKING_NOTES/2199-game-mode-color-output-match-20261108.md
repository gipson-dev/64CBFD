# Mode Color Output Match - 2026-11-08

`func_15131514` now emits all **78 instructions / 312 bytes directly from
semantic C**, with its original **8-byte frame**. Two checked relocation
guards bind the compiler's private jump table to the protected retail table;
they change no instruction words. The isolated body, complete owner, both
padders and actual Make agree.

Production: Total **4,268 / 5,513 (77.42%)**, Game **3,595 / 4,840 (74.28%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,245**
converted functions remain different. **143** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion denominators and the
progress CSV are unchanged.

## Recovered interface and ordered channels

Owner `conker/src/game/generated_15D730.c`, original `asm/15D730.s`.
VA **15131514..1513164C**, ROM **15E9C4..15EAFC**. Interface:

```c
void func_15131514(s16 *red, s16 *green, s16 *blue, s16 *alpha,
                  register u8 *record);
```

Four halfword output pointers occupy A0..A3. The record is the fifth
argument at incoming SP+0x10, loaded into S0 after allocating the 8-byte
frame; saved S0 occupies new SP+4. The original wrapper ignores this target's
incidental V0 and forwards the later callee's return, so the recovered C
uses void rather than promising a manufactured return value.

Snapshot the unsigned mode byte at record+0x71. Modes 1..9 use the nine-entry
table; every other byte, including 0 and 128..255, follows the default.

| Modes | RGB source | Alpha source |
| --- | --- | --- |
| 1,5 | Zero through blue, reload blue, then green/red | Zero |
| 2 | One cached byte+0x2C, stored blue/green/red | Zero |
| 3 | Bytes+0x24,+0x25,+0x26, read/store red/green/blue | Zero |
| 4,6 | Bytes+0x28,+0x29,+0x2A, read/store red/green/blue | Late byte+0x2B |
| 7 | One cached byte+0x2C, stored blue/green/red | Late byte+0x2B |
| 8 | Zero through blue, reload blue, then green/red | Late byte+0x2B |
| 9 | Bytes+0x24,+0x25,+0x26, read/store red/green/blue | Late byte+0x2B |
| Default | One cached byte+0x2C, stored blue/green/red | (late byte+0x2B * late byte+0x27) >> 8 |

The individual byte reads and halfword stores are observable under aliases.
Keep their order, the signed halfword reload in zero modes, and the cached
scalar in repeated-channel modes. The default source expression reads +0x2B
before +0x27 to recover the original byte-load/register assignments. All
products are nonnegative and at most 65025. The register hint on the fifth
parameter recovers the original S0 lifetime without changing frame geometry.

## Protected table, labels and complete owner

`jtbl_800A3820` lives at VA **800A3820**, ROM **2482E0**, owned by
`asm/data/2482B0.rodata.s`. Its nine targets, relative to the function entry:

```text
34 4C 80 A0 34 A0 C4 64 E0   (hex byte offsets)
```

The table's repeated entries implement the 1/5 and 4/6 aliases. All seven
target labels are at their original addresses; all **14 exported interior
labels in the complete owner** remain fixed. A pristine aligned census finds
one direct call at ROM **15EB28 / VA15131678** in func_1513164C and exactly
these nine interior pointers, with no entry-point function pointers.

The compiler's new private pool is exactly **48 bytes**: nine R_MIPS_32
entries owned by this function at the offsets above, followed by 12 zero
padding bytes. Its targets are checked independently in owner and isolated
objects. It is consumed by the existing padding mechanism; the linked image
continues using the original protected data table. At instruction offsets
0x20 and 0x28, two expected-relocation guards replace `.rodata` with
`jtbl_800A3820`; expected and replacement instruction words are identical.
The inherited guard prefix is preserved byte for byte. Raw body SHA256:
`1fdf21b79174aee5e5f2984335cd4df64ac9606153b8b79d7495f31b7c3cfa8a`.

Actual Make retains O2/g3/MIPS2/O32 and all five commands: assembly prepass,
IDO compile, assembly postpass, production padder and GNU as. Preserve the
existing GLOBAL_ASM func_15130280 and all **31 functions / 30 neighbors**.
The wrapper's call gains explicit pointer casts for the recovered interface;
its raw and padded instructions remain unchanged. Diagnostics are zero,
register masks equal their exact expected union, and no shared headers or
compiler profiles change.

## Behavior, wrapper and effective controls

Six focused checks pass sequentially before and after installation against
mounted and sibling tools, with exact source/dependency fingerprints.

- **2,560 guest cases**, **5,376 alias cases** and
  **273 interrupted-access cuts** compare independent complete
  memory and literal original/raw-C/normalized states. Every one of the 78
  words executes. Tests include every mode byte, four memory seeds, stack
  phases, three code/data layouts, output overlap, record bytes and incoming
  argument-home aliases.
- **3,584 connected cases** execute the complete
  original **24-word func_1513164C**. Check all nine register/stack arguments,
  saved S0/RA, the ignored target result, late scalar/record home reloads,
  the five followup arguments and forwarded return. func_1513137C is a bounded
  provider with caller-register/home clobbers; its full body is not qualified.
- **5,120 native32 cases per O0/O2/O3 profile**, trapping UBSan,
  use aligned typed halfword backing, byte-record aliases, complete 256-byte
  canvas checks and independently precomputed little-endian expectations.
  All **11 semantic controls** are effective, including wrong modes,
  sources, alpha, shift, table-case aliases, access order, cached alpha and
  the old stub. A signed-selector rewrite is shape-only because it reaches
  the same cases/default for every byte; it is deliberately not credited.
- Three independent GNU links and 12 rebased executions qualify both table
  binding sites and high/low carry handling. All 78 word, two binding, 72
  register-metadata, ten private-pool and 12 whole-image corruption controls
  reject changes.

Guest expectations model big-endian stores; native alias expectations model
the host's little-endian stores separately. They do not assert identical
cross-architecture byte images. Fault-prefix checks qualify emitted MIPS
access order, not portable C fault behavior. Hardware, gameplay and the
complete followup renderer are outside this qualification.

## Literal image, production and preservation

The independent predictor replaces only the target body, its 12-to-312-byte
symbol extent, and two measured closed GNU symbol/string-table permutations:
`jtbl_800A3820` / `func_1513477C`, and `D_800A358C` / `D_8009D7E0`.
Rows are reconstructed from predecessor definitions; equal-length strings
and contiguous extents are checked. No actual metadata is copied or excluded.
The permutations account for 58 bytes across four rows; all definitions,
addresses, extents and bindings remain unchanged by name.

The literal complete-image prediction changes **253 bytes**, with **zero
exclusions**. All **6,052** disassembled entries keep their addresses; every
other body and extent stays fixed. Protected data remains exact across
**720 owners / 189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals that complete prediction.
Makefile, protected data and progress CSV stay unchanged. The pre-existing
full-ROM checksum mismatch (make all exit2) and duplicate generated_12D630
recipe warning remain separate from the successful target compile/link and
recount. Shared smoke checks are fresh in both tools copies; three unchanged
helper regressions per copy are reused by exact fingerprints. All **2,434**
inherited sibling dirty paths are preserved. **105 frozen inputs** pin the
source, original owner, table owner, headers, layouts, ROM and IDO compiler.
Baseline consumer d44eaad60f70e9f3faeb14cb433210f17f52fd33, tools
e0487e773288d0b0aa39db857226304e3f20b4ff. Claude calls: zero.

ELF SHA256: `9a71b3f84b94c16f0f4d2985292e944dc46cbf102b1ce9c4119442ca3ec24712`.
Binary SHA256: `fc28f92e2853fe6b8e35642f057d997a59f9dc3b0a62b28230c1b935a15d9f2b`.
Owner SHA256: `67b7fc5aa47f2222175c8272ba3e0320fc356cc8066bfe1b6e00823b7e5008c4`.
Guards SHA256: `c6df151d01ea4238ab959fea60f128e34533c8ad715b8686b6abe98bc9143179`.

## Resume boundary

Next: **func_151319C4**, an uncredited 78-word collision-response dispatcher
in the same generated_15D730 owner. VA151319C4..15131AFC /
ROM15EE74..15EFAC, frame0x40. Audit its three-pointer ABI, original callers,
signed callback index and D_80089874 before drafting. Flags bit0, signed
index -1, null callback and ordered height comparison return1 without work.
Preserve the two stack point packets, helper mutation boundaries, live
callback-table/index reload, saved byte result and callback low-byte return.
Qualify all helpers/callers, private homes, original table/data bindings and
the full image before any matching credit.

Receipts: `conker/build/game-mode-color-output-15131514-match/`.
Tools commit before the consumer pin. Scoped Graphify refresh retains existing
unscanned nodes with explicit evidence; it is not full-corpus extraction.
Host Release stays frozen. The 80% goal remains active.
