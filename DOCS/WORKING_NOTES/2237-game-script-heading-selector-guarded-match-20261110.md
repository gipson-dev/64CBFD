# Game script heading selector guarded match - 2026-11-10

`func_1507AA48` now matches its complete **154-word / 616-byte** retail slot,
VA **1507AA48..1507ACB0**, ROM **A7EF8..A8160**. Its sequenced semantic C
emits153 words with the natural **0x18 frame**. **62 checked guard rows**
close register allocation and the unsigned-conversion schedule, including
one unreachable duplicate MFC1 insertion. No source instruction is omitted.
This is a guarded match; it is not direct byte-exact compiler output.

Production recount: **4,307 / 5,513 (78.12%)** total; Game **3,634 / 4,840
(75.08%)**; Init492/492 and Debugger181/181. Zero address drift,1,206 still
different; **104** further matches reach4,411/5,513 and the active80% goal.
Conversion rows/counts remain fixed. README contains aggregate rows only.

## Recovered source and ABI

Owner `conker/src/game_A28B0.c`; object `conker/build/src/game_A28B0.c.o`.
The original154-word assembly in `asm/nonmatchings/game_A28B0/` is retained.
Public ABI remains `void(void)`. Read bytes D_800D1890/1 into one unsigned
16-bit value before dispatching on D_800D1892. Selectors0..8 operate on the
current actor through D_800D154C:

| Selector | Behavior |
| --- | --- |
| 0 | heading+0x78 = base+0x76 plus packed value, narrowed to16 bits |
| 1 | heading = base minus packed value |
| 2 | heading = packed value |
| 3 | copy heading into base, then reload current actor/heading into saved+0x7A |
| 4 | path-node direction helper, late scale, unsigned conversion and heading offset |
| 5 | RNG result's low16 bits into the current actor reloaded after the call |
| 6 | heading = base |
| 7 | base = selected actor's saved heading plus packed value |
| 8 | base = this actor's saved heading |

All other byte selectors leave actor storage untouched, including when the
current actor is NULL. Halfword wrap, unsigned fields and the original
actor-pointer reloads are preserved. Selector7 uses D_800CC34A as the existing
u16 view of D_800CC2D0+0x7A: index*0x196 halfwords equals the812-byte actor
stride. Canonical actor layout is checked at118/120/122, group319 and index546.
Native fixtures use the real26-actor array and an assembler alias for that
u16 view; they do not replace it with unrelated storage.

Selector4 selects a path row through D_800D2104 using the current actor's
group byte at0x13F. The existing PathNode8 has8-byte stride. Both indices address the following
record: signed x/z halfwords are loaded at indexed-pointer+8/+12. Subtract
first from second, convert tofloat and call150484A0(dx,dz). Read D_8009A20C
after the helper, multiply in float32, convert to **u32**, then read the live
third byte D_800D1893 and current actor. Add (third<<8) +0x4000 to the
converted value and store its low16 bits. Protected scale bits remain4622F983.

The predecessor used a135-word if-chain and signed conversion. The recovered
nine-case switch restores the compiler table and unsigned conversion. The
helper, conversion and publication are separate full expressions. A native
control demonstrated that the compact combined expression allows GCC to read
the third byte before the helper; the separate statements preserve the late
read across all three native optimization profiles. The scale and current
actor also remain live after helper side effects. Source probes stay private.

## Closed normalization and table ownership

Raw SHA256:
`3af4566311faf666718a8eca674d3b6f054f2ae4720ccd905357b7cb4e51b4f0`.
All612 source bytes,38 binding sites, owner and function are pinned. Explicit
instruction origins retain every source word, with source104 represented
twice. Move the2^31 constant before conversion control, use retail's successful
BEQL delay-slot MFC1, and keep the second MFC1 unreachable after the failure
branch. Recompute every affected branch displacement and use44 closed
register-operand edits. No frame, private-home or compiler-profile change.
An insertion-corruption control checks even the unreachable word's bytes.

The generated .rodata is48 bytes: nine R_MIPS_32 case targets plus12 alignment
bytes. Raw target offsets80/108/136/156/192/464/488/508/580 map to retail
80/108/136/156/192/468/492/512/584. Every entry is qualified against the
original36-byte table at **jtbl_8009A1E8_game**. The target-specific Make row
sets RETAIL_RODATA_SYMBOL for game_A28B0.c.o. The generic padder binds code
references to the protected retail table and drops the generated pool. No
protected data/table bytes move or change. Both independent target padders
and the complete owner produce the same154 words and binding identities.

The old ASM's D_80004000 annotations identify literal80000000/4000 integer
constants in this routine. Independent assembly qualifies them with
`.equ D_80004000,0x80004000`; they are not runtime memory references.

## Qualification and production

All **210 non-target neighbors** stay identical before/after raw and padded
compilation. The owner contains211 functions, with retained ASM15079B30.
Register usage and owner pools stay fixed after padding. The13 inherited
diagnostics stay13. The actual five-command asm-processor/IDO O2-g3/
postprocess/generic-padder/assembler recipe equals the independently padded
owner, including the single Make table binding. No shared declaration changes.

Strict literal full-ELF prediction accounts for **537 changed bytes** with
zero exclusions: the616-byte target slot, st_size540->616, and a closed swap
of existing func_15148F1C/D_8009D6C0 symbol rows and adjacent names. Both
metadata tables are predicted from the predecessor, without copying result
bytes. Seven corruption controls cover code, inserted word, protected table,
symbol/name metadata and headers. All6,051 function addresses remain fixed.
All189,088 protected bytes across720 owners remain exact, SHA256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Existing duplicate12D630 Make warnings and expected `make all` checksum exit2
remain. The actual production ELF/owner equal the private predicted outputs.

- Guest: **354 cases per body /1,062 executions** across raw, normalized and
  retail, plus36 independently rebased executions. All153 raw words and153
  of154 normalized/retail words are visited; the remaining word is unreachable.
  All256 selectors, signed coordinate extrema, next-node indexing, all public
  bytes, ordered stores, helper snapshots, saved ABI and live callback effects
  pass. A physical global-pointer alias proves selector3's second reload.
- Conversion: guest-only negative/nonfinite/out-of-range cases exercise the
  compiler's unsigned conversion and indefiniteFFFFFFFF result. The bounded
  FCSR model checks conversion mode, exception decision and save/restore,
  including provider control-state seeds. It does not model the full hardware
  floating environment or all multiplication rounding/exception behavior.
- Native SDK32: **347 defined cases at each of O0/O2/O3**, UBSan and12
  effective controls per profile. All retained actor/path/table bytes and
  helper-boundary snapshots pass with explicit endian normalization. Physical
  address aliases and invalid float-to-u32 inputs are excluded. Signed-cast
  discrimination remains guest-only to avoid claiming native undefined cases.
- Compiler/control gates:13 effective IDO controls;153 word plus38 binding
  corruptions rejected;62 stale expected guard rows rejected; wrong switch
  destinations detected. Four independent GNU links and36 executions exercise
  HI/LO carry boundaries. Compiler/interpreter errors never count as witnesses.
- Caller: no direct ROM JAL/J, one entry pointer at ROM22B25C, protected
  VA8008679C =D_80086730[1B]. The complete original1507BC14 dispatcher remains
  byte-exact C:100 body words plus3 alignment words. **258 executions /246
  target invocations** cover all nine selectors, script decode/FF skips,
  advancement, null lookup, countdown/flags and real JALR ABI. It visits99
  body words; word67 is a dead duplicate byte load. Lookup1507BB28 and next
  handler1507735C are bounded providers. Direction/RNG algorithms, complete
  game scripts and visual gameplay/hardware acceptance are not qualified.

Six focused tests pass before and after installation in both tools environments.
The sibling uses a read-only overlay for new modules and preserves its native
Git baseline of2,434 dirty paths. Dependency origins/hashes are recorded. Both
shared smokes are fresh; three unchanged regressions per copy are explicitly
fingerprinted reuses.720 inputs are frozen. Tools commit precedes consumer
source/guards/Make/docs/pin. No push or host-port changes.

Graphify receives a scoped AST refresh for the owner and six new modules.
All210 active C positions, the retained ASM and nodes outside changed files
are audited. New-module node coverage is recorded as observed; this is not
a full-corpus extraction claim. Ignored receipts and exact hashes live in
`conker/build/game-heading-selector-1507AA48-match/`.

Next: **func_150768DC**, same owner,160 retail words /159 screened differences.
Recheck its current source, complete ASM and caller before qualification.
Hard private1510D404 remains uncredited. Keep the80% goal active.
