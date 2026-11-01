# Packed scale command recovered as byte-exact guarded C

Verified 2026-11-01. `func_15076D3C` now matches its complete **46-word**
retail body with the natural **24-byte frame** and 25 checked scheduling guards.
Its existing nonmatching C decoded Y before X and reloaded the scale coefficient;
the recovered C captures the coefficient once and decodes both signed X/Y
values before writing the actor. The interface remains `void(void)`.

Production Make and an independent Windows actual-ELF recount report
**4,032/5,507 (73.22%)** total, **3,359/4,834 (69.49%)** Game, zero canonical
address drift and 1,475 different. Init remains 492/492; Debugger 181/181.
The converted inventory stays 5,507/6,045, Game 4,834/5,324. The threshold is
4,131: **99 additional exact C functions are needed**. The wider goal stays active.

## Source, interface and schedule

- Owner/source: `game_A28B0`, `conker/src/game_A28B0.c`.
- Original assembly remains at
  `conker/asm/nonmatchings/game_A28B0/func_15076D3C.s`.
- VA `0x15076D3C..0x15076DF4`, ROM `0xA41EC..0xA42A4`, 184 bytes.
- No shared header, compiler profile, layout or historical guard row is edited.

The routine captures `D_8009A144` (retail bits `3C23D70A`), assembles signed
little-endian 16-bit X/Y values from `D_800D1890..D_800D1893`, multiplies them
by the captured coefficient, writes the current actor's XZ/Y scales, copies
them to fields `unk154/unk158`, and invokes `func_15062BDC` with the live actor
and reloaded scales. Current actor-pointer reloads are retained. Aliases can
change that pointer after a store, so caching the actor is not equivalent.

Eight initial source forms and sixteen subsequent variants were screened.
The selected form naturally emits 46 words and frame24, with 25 differences.
Forms storing X before capturing Y are rejected for alias behavior even where
their code appears similar. No inserted words, omitted words or volatile filler
are used. The independent permutation is:

    [0, 1, 23, 24, 2..22, 26, 25, 27..45]

It moves the independent coefficient LUI/load pair earlier and exchanges an
independent integer-to-float conversion with the actor-pointer load. Every raw
instruction is retained once, and all 13 relocation bindings move with their
instructions. Guards derive from that permutation, not replacement retail
words. Complete normalized bytes and bindings equal original assembled ASM.
Corrupt raw bytes, missing bindings, stale expected words and repeated guard
installation reject. The 25 relocation-aware CSV rows append to all existing bytes.

Raw SHA-256:
`998d83eecf7cdddabd3edf636d0ad3c3b9303129e3e887598c72dcd9525be6de`.

## Behavioral and caller qualification

- **10,752 guest cases / 53,760 executions**, three rebases, seven alias
  layouts, two stack phases and all 256 values of each packed byte. All 46
  words execute. ASM, padded owner, actual Make object and normalized isolated
  C agree in complete modeled state and traces; raw C agrees in public memory
  and preserved ABI. Pointer aliases after each output store, coefficient
  aliasing and command/output aliasing are exercised.
- **60 fault prefixes / 240 executions** agree across the four exact programs.
  This qualifies guest order, without claiming raw-C fault-order equivalence.
- **1,024 connected cases / 5,120 executions** run all 77 words of original
  `func_15062BDC` at `0x15062BDC`, ROM `0x9008C`, pinned against retail and the
  baseline ELF. ID255 skips descriptor work; 512 nested paths validate signed
  descriptor dimensions and truncation using an independent reference.
  `func_15062AC4` and `func_15062B84` remain bounded providers.
- **480 caller cases / 2,400 executions** run the original 29-word window
  `0x1507BD00..0x1507BD74` in `func_1507BC14`. All 28 reachable words execute;
  duplicate LBU at window+0x20 is unreachable. Opcode86 copies four bytes and
  calls table `D_80086730[86]`, then advances the packet cursor five bytes;
  opcodes247/255 skip and advance one. Four ignored-return poisons pass. The
  sole aligned root pointer is ROM `0x22B348`; no aligned direct JAL/J exists.
  This is a bounded caller window, not full dispatcher emulation.
- Native O0/O2/O3 each pass **2,048 cases**, UBSan and complete actor canaries.
  All eight controls are effective: unsigned X/Y, wrong X/Y endian, lost
  coefficient capture, wrong X/Y mirror and missing helper. Coefficient aliasing
  is native-qualified; actor-pointer aliases are guest-qualified.
- **16 cases / 32 executions** exercise both retargeted two-word J/NOP
  trampolines, preserving every register and memory at the new body boundaries.

Full hardware, gameplay, arbitrary NaN/FCSR behavior and unmodeled nested helper
internals are outside this qualification.

## Owner, overflow removal and complete image

All **210 raw and padded neighbors** and normalized pools are unchanged.
The actual five-command Make recipe produces the independently qualified object.
The owner's existing **14 warnings remain 14**, with identical diagnostic kinds
and source expressions; no warning reduction is claimed.

The old canonical entry jumped to a 192-byte private nonmatching body. Restoring
the retail body removes `__retail_overflow_func_15076D3C`. Four subsequent private
bodies move down192 bytes without changing any body bytes:

| Private body suffix | Before | After |
| --- | --- | --- |
| `150781F4` | `0x15F007B4` | `0x15F006F4` |
| `150A7B80` | `0x15F008AC` | `0x15F007EC` |
| `150A7D00` | `0x15F00930` | `0x15F00870` |
| `15125490` | `0x15F009DC` | `0x15F0091C` |

The live entries `func_150781F4` and `func_150A7D00` retarget accordingly. The
other two moved private bodies are unused by their restored public entries.
An exhaustive executable-reference scan, relative branch/absolute call audit,
all named symbol definitions and exact moved-body hashes qualify the closure.
All **6,045 canonical addresses remain fixed**; **6,052 other bodies remain
identical**. The executable inventory changes 6,056->6,055 solely by deleting
the obsolete private body. This is not an all-function-addresses-unchanged claim.

Independent complete-ELF prediction accounts for every byte: the target, two
trampolines, removed overflow payload, symbol deletion/moves, shared string-table
suffix reconstruction, two ROM cursor definitions, headers and alignment.
ELF size falls **224 bytes**, 3,257,124->3,256,900. Independent full linker-map
prediction matches all bytes, including **25 changed lines**. Corruption controls
cover target, moved code, trampolines, symbols, strings, unrelated image and map.
There are **zero exclusions**. All **189,088 protected Game bytes / 720 owners**
remain exact. Installed ELF SHA-256:
`c3712c89cd6c08397b6cc14724a0514ac2264bb7ca8251d6dd2b8df3a7429552`.

Production reviews all 17,614 predecessor sealed files. Exactly source, owner
object, guard CSV, ELF and map change before documentation; there are no unplanned
dependent-object changes. Six focused public tests in each tools copy and both
shared checks pass. Older mirror edits remain preserved; only three identical
owned modules are added. Tools are committed before the consumer; no push.

## Evidence and next work

Self-contained evidence is in
`conker/build/game-packed-scale-command-15076D3C-match/`: 1,055 frozen focused
inputs, 29 canonical artifacts, screens, guard/overflow/map predictions,
runtime qualification, production, independent Windows recount and bank receipts.
Early private preparation records remain historical; final BANKED_STATUS is the
adoption authority. Historical archived checkpoints need explicit restoration.

`func_15117DA4` remains private and uncredited. Sixteen further lifetime forms
do not resolve its two CSE'd output reloads: the baseline stays100 words/frame48/
62 differences; reusing formal parameters yields102/frame56/97, captured final
outputs100/frame56/90, combinations102/frame64/99. No volatile or inserted-word
workaround was adopted. Its production placeholder is unchanged.

Next inspect neighboring command `func_15076DF4`: establish its actual retail
extent, argument/table interface and current source before any matching claim.
Keep the special-position candidate available for a later compiler-lifetime idea.
