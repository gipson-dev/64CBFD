# 1984 - Gated sparse effect payload recovered directly from C

Verified 2026-11-02. Actual production is **4,051/5,507 (73.56%)**; Game is
**3,378/4,834 (69.88%)**, Init492/492 and Debugger181/181. Zero address drift,
1,456 different; **80 more** exact C functions reach4,131/5,507 and75%.
One installed match, unchanged C inventory. The wider goal remains active.

## Recovered body and ABI

`func_151937F4` in `conker/src/game/generated_1C0B10.c` replaces a zero-return
placeholder with `void func_151937F4(u8 *owner, s32 unused1, s32 unused2)`.
Its original slot is VA151937F4..151938E4, ROM1C0CA4..1C0D94:60words/frame88.
The two trailing arguments retain their full-width o32 homes and are unused.
All60 words, all three relocations and the complete frame emit directly from C.
**No guards**, raw assembly substitutions, inserted instructions or padding
compensation are used. The inherited guard CSV remains byte-for-byte unchanged.

The owner pointer and its first32-bit word gate the whole operation. Capture
owner byte+3B and owner pointer into a local60-byte effect payload. Initialize
six floats to -28,6,1,-58,-3,-31; kind2; halfwords30,25,750; byte fields3,3,-1,
4,-1; one zero byte; and the coefficient loaded from `D_800A81E4`. Submit to
`func_15134DAC(&payload,0)`. Offset-based field names remain explicit where
semantic meanings are not yet established; do not invent gameplay labels.

The payload contains **46 initialized bytes and14 untouched bytes** at offsets
1,2,3,9,A,B,25,2C,2D,31,32,33,3A,3B. Explicit padding arrays preserve this
layout. Do not insert aggregate initialization or zero-fill. The original
factory copies all60 bytes into its allocated object's+18 payload, then reads
the live signed halfword at source+28, negates it into child+54, sets child
flags+10/+14 and clears floats+70/+74/+78. Allocation failure returns early.
The complete original39-word factory and11-word memcpy match retained ELF.
Only its allocator is opaque in the connected guest check.

Raw code SHA256:
`40f1b0223a127988851906e120fff416c934d42696efb791aa0a0fa673385b40`.
Bindings: HI16 D_800A81E4 at64hex, LO16 at6C, JAL func_15134DAC atD8.
Independent GNU links cover three code/global/helper layouts, including
signed-low-half boundaries at7FFC andFFFC; every linked root equals its
independently assembled original, and layout0 equals the complete retail slot.

## Qualification and limits

- Guest root:914 corpus cases across three layouts,2,742 cases/5,484 executions.
  All60 instructions and256 owner tags execute. Full60-byte packets, complete
  GPR/FP/memory/call/access traces, HI/LO and PC/delay state agree.65 access-prefix
  pairs agree. Gate failures work with later reads deliberately unmapped;
  full-width nonzero gates include256,80000000 andFFFFFFFF. Guest constant
  words include zero, signed zero, subnormal, max finite and NaN payload patterns.
- Connected factory and copy:672 cases/1,344 executions, all50 helper words,
  both allocation outcomes, caller phases and seeded/mutated padding. The
  source halfword read is observed after the last copied byte. Bounded allocator
  probes may mutate captured payload, owner/global state and incoming homes;
  inaccessible argument-home/private-payload probes are guest-only claims.
- Effective guest zero-padding negative control leaves all46 defined payload
  bytes equal but changes copied padding and observable output memory. This
  rejects a tempting cleanup that would silently change retail behavior.
- Native32:262 cases at each O0/O2/O3, typed owner/payload layout and surrounding
  fences, UBSan, finite coefficient patterns, full-width ignored arguments,
  provider mutation and both helper return outcomes. Nine effective controls
  per profile reject missing null gate, byte-width gate, wrong owner-tag offset,
  missing owner pointer, wrong float parameter, duration, sentinel, coefficient
  and helper extra argument. The native harness validates all defined fields;
  it never reads uninitialized payload padding. Guest NaN bit-copy and private
  stack probes are not portable native/FCSR claims.
- Complete aligned-ROM census finds **three**, not two, JAL sites:150254C0,
  1507012C and150997D8; no literal target pointers. Original bounded windows
 8words@150254B0 and4words@150997D0 plus the complete12-word wrapper
  func_15070114 each cover144 cases/288 executions (432cases/864exec total).
  The wrapper loads owner from D_800D154C and has its original24-byte frame;
  all callers passFF/1. First parent window has a null-owner gate; the second
  proceeds to the next effect without consuming the result. The recovered
  wrapper is void. Large parent functions and gameplay are not executed here.

An initial helper reference invented a mutation between real memcpy and the
factory's next load. That failed private fixture was corrected to observe the
actual instruction/access order. The call census also exposed the wrapper
omitted by a textual search of the two large assembly owners. Neither harness
issue was treated as a production defect; failed receipts remain available.

## Owner and complete-image proof

All three raw and padded neighbors and owner pools remain identical, with zero
old/new compiler diagnostics. This ordinary generated slice uses **three**
actual Make commands (compile, generated padder, assembler), not the five-command
profile of the preceding target. The exact Make-produced object equals the
qualified padded object.

The independent complete-image prediction replaces the target240bytes, expands
its symbol extent12->240 and applies two closed linker metadata permutations:

- Symbol rows at2751800: (func_15155FD4,D_800AA9BC,D_8009E63C) -> (2,0,1).
- Symbol rows at3009480: (D_800A81E4,D_8009FB44,D_8009F674,D_80096274) -> (1,2,3,0).

Each transformation checks the original contiguous name strings, rewrites the
complete symbol/name blocks, and preserves every named definition. There are
**zero excluded bytes**. Arbitrary code, metadata and final-byte negative
controls are rejected. All6,052 function addresses,6,051 other bodies,189,088
protected bytes and720 data owners remain fixed. The map is fully reproduced.

Production ELF SHA256:
`ca4d0c821f391a246d79dd62c5f32c3ec98d094feb4b48678a568a3a4696d673`.
Actual production Make and Native-mounted ELF recount agree. Before documentation,
all17,790 prior sealed files were audited: only target source, target object and
ELF changed. No dependent-object exclusions or guard-history changes.

Both tools copies pass five fresh focused methods and the shared project-tools
check. After installation each passes the two compile/image methods; unchanged
semantic checks are reused under their source, code and24 preparation pins.
The source and tool names/comments describe the recovered payload rather than
retaining unrelated oscillator/position terminology.

## Bank and continuation

Canonical evidence: `conker/build/game-gated-effect-payload-151937F4-match/`,
with1,116 frozen focused inputs and24 pinned preparation artifacts. Final Git
heads, current Native/cache seal, scoped graph-retention evidence and detailed
resume instructions are in `BANKED_STATUS.json`, `FINAL_AUDIT.json` and `HANDOFF.md`.
Tools are committed before the consumer pin; no push. Older tools-mirror dirty
work, private experiments, cleanup archives, WSL runtime and frozen host Release
are preserved. README receives aggregate rows only.

Next ordinary unmatched candidate: **func_15193660**, the preceding101-word
routine in the same owner. It gates owner/owner-word/attached pointer, resolves
point10 through func_15142314 and submits a larger sparse local payload to
func_15152520. Its two trailing arguments are consumed (low byte/full word),
unlike this routine. It remains a stub and receives no matching credit here.
