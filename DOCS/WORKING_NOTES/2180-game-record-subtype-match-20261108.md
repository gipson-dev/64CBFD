# Record Subtype Dispatcher Match - 2026-11-08

`func_150A25D4` is byte-exact across all **110 words / 440 bytes**, with its
original **40-byte frame**. Total **4,249 / 5,513 (77.07%)**, Game
**3,576 / 4,840 (73.88%)**, Init **492 / 492**, Debugger **181 / 181**.
Address drift remains zero; 1,264 converted functions remain different.
Another **162** exact functions reach 4,411 / 5,513 and the active 80% goal.
Conversion totals are unchanged.

## Source and argument layout

Owner: `conker/src/game/generated_CDE80.c`. VA 0x150A25D4..0x150A278C;
ROM 0xCFA84..0xCFC3C. The recovered entry is:

```c
void func_150A25D4(GeneratedCDE80Record *record, struct127 *actor,
                  s32 selector, u64 flags)
```

The original caller passes a 64-bit bitmap. Under O32 its fourth argument
aligns to stack words four and five: high word at caller SP+10, low word at
SP+14. A3 is alignment padding. The callee reads only the low word at its
SP+3C and does not store A3. A provisional six-scalar signature emitted an
extra A3 home store; the four-parameter interface recovers the real layout.
The caller's eight-byte bitmap stride and `__ull_rshift` path independently
support the width. Native checks use actual 32-bit pointers, an 812-byte SDK
actor, a 52-byte record and a 64-bit mask.

The sole aligned direct JAL is at ROM 0xCF0E8 / VA 0x150A1C38 inside
`func_150A11C4`. Connected execution covers its ten original words, including
both stack mask stores, the low-word store in the JAL delay slot, and the
post-call branch to 0x150A1CF8. The selector is the caller's byte-derived
value, 0..255; the return value is ignored. The aligned census also finds
eleven switch-table pointers at ROM 0x244108..0x244130 and no interior direct
J/JAL entries. All 31 existing case labels are retained.

## Recovered behavior

The switch selects record byte 0x17. Cases 0, 4, 5, 7 and values above 10 do
nothing. The other cases preserve the original order of reads and effects:

- Case 1: when selector is not 255, call `func_150E7290` with its low byte,
  255 and zero. The established provider signature remains `void(u8,u8,s32)`.
- Case 2: when selector is not 255, compute `D_800D9EB8 + selector * 3`
  once. Write the low byte of field18, reread field1C and write its low byte,
  then reread field20 and write its low byte. Interleaved aliases remain live.
- Case 3: when selector is not 255, call `func_150E68B0` with actor,
  selector, record and the low byte of field18. Expressing that byte as
  `(u8)record->field18` preserves retail's big-endian LBU at offset 0x1B and
  gives the same logical field value in native little-endian C.
- Case 6: when the low mask word's bit zero is clear, store 30 to
  `D_800D3090`, then call `func_10010344(0x66F, actor, 24000, 400, 500)`.
  Reload the live counter and `D_800BE9E4`, add with unsigned 32-bit
  arithmetic and narrow to a byte. At 31 or more, transform actor's unsigned
  halfword at 0xB2: 1441 or more becomes 1200, 240 or less becomes 90,
  otherwise subtract 240. Write the halfword and clear the counter byte.
  The field's wider game meaning remains unnamed.
- Cases 8, 9 and 10 call `func_151C8674`, `func_1515F270` and
  `func_151CE51C` respectively, in actor/record order and with their existing
  provider types.

The complete 196-word `func_150E7290` home-read census proves that only the
low selector byte is consumed after its argument home store. Its definition
and signature are unchanged. This permits the normalized caller to reuse the
already-homed selector word: upper byte-argument padding has no public effect.
Connected tests execute the full 14-word owner-command wrapper and 18-word
action-table dispatcher. The SDK audio provider is limited to its original
23-word inactive-actor gate; full audio execution is not claimed. Remaining
provider effects use bounded hooks. No provider or caller source is changed.

## Derived normalization and owner protection

Semantic C emits **108 words / 432 bytes** under the unchanged IDO 5.3
O2/g3/MIPS2/O32 profile. **41 fail-closed expected-word/relocation guards**
normalize address rematerialization, register lifetimes, selector padding and
independent load/restore scheduling. Two inserted words supply the original
address/RA-restore schedule, bringing the result to 110 words. The guards do
not supply a copied function body. All semantic state transitions, calls and
conditions originate in C. There are 16 raw bindings and 20 normalized ones.

The compiler creates eleven jump-table entries (44 bytes) plus four zero
alignment bytes. Two guarded table-address relocations bind to the original
`jtbl_8009F648`; the original protected table remains byte-exact. The raw
compact table is discarded only after its entire layout and ownership are
qualified. No linker alias or Makefile change is needed. All other raw pools,
24 register-metadata bytes, 27 raw/padded neighboring functions and all case
labels remain fixed. Production and strict padders agree across all 28
functions and their pools. Every preceding guard CSV byte is unchanged.

Raw body SHA256:
`b970ba7d39ee5dd68138189376daddd712080f84d170a7e216ef8e8393af9784`.
Normalized relocatable body SHA256:
`325dcce1e0e49ea59a07cdd0c6e4acc4b58cdcfdf506a7acb2cc17eebc0cf28b`.

The frozen baseline contains 107 inputs. The actual five-command owner Make
recipe reproduces the qualified object. Two independent GNU links exercise
original and rebased symbols, including signed LO16 carries. Every one of
108 raw-word mutations, 16 binding mutations, 41 stale guarded words,
41 guarded-relocation mutations, 24 register-metadata mutations and eleven
table-target mutations is rejected. Insertions, labels and the inherited
guard prefix are also checked.

## Literal full-image check

The complete ELF changes by exactly **424 bytes**, with **zero exclusions**:
353 function-body bytes, two target-size bytes, and 69 bytes from three
closed symbol/string order permutations. Named definitions, values and types
remain fixed except for the restored function's size (12 to 440 bytes).

The predictor reconstructs the complete affected symbol rows, their string
groups and their `st_name` offsets from frozen predecessor bytes. It accounts
for these observed linker order changes explicitly:

- `D_800CC2D0`, `D_8009D2B0` reverse order.
- `.L1509E5F0_game_data`, `D_8009D8F0` reverse order.
- `D_800D3090`, `D_8008B440`, `D_8008B090` become
  `D_8008B440`, `D_8008B090`, `D_800D3090`.

No candidate metadata is copied into the prediction. Six independent
corruption controls cover code, headers, target size, symbol rows, strings
and protected data. All 6,053 function addresses, all other function bodies,
720 protected data owners and 189,088 protected data bytes stay fixed.

## Execution and production evidence

Both mounted and independent sibling tools configurations pass six focused
checks before and after installation. All four runs are sequential; their
source/helper fingerprints and terminal receipts are retained. The sibling
configuration uses a scratch overlay for these new modules and two explicitly
identified mounted read-only helper fallbacks. Its HEAD and 2,434 inherited
dirty paths remain unchanged. Both configurations also pass a fresh shared
smoke check. Three unchanged synthetic shared regressions per configuration
are explicitly reused by exact hashes, rather than reported as fresh runs.

- **727 guest cases** run retail, normalized and raw C bodies. All 109
  reachable words execute. The remaining word at 0x150A2718 is a redundant
  comparison after an unconditional branch with no incoming branch target.
  Alias, home, mask, callback reload and saved-register behavior are covered.
- **504 original-caller cases per body variant** (1,512 executions), plus
  28 connected owner-command, 48 action-dispatch and 64 inactive-audio cases
  per variant qualify real argument packets and bounded provider paths.
- **170 executed memory-fault cuts** compare literal retail/normalized
  machine states. Raw C is checked for public semantics; identical raw
  scheduling is not claimed.
- **635 native cases per executable** pass at O0/O2/O3 with trapping UBSan.
  Fourteen effective negative controls reject a stub, wrong switch/sentinel,
  high mask, early update, both threshold errors, wrong subtraction/reset,
  cached delta/counter, wrong byte, reversed pointers and lost delta bits.

Production rebuilds exactly one C owner with no C diagnostics. Its actual
ELF equals the literal prediction. `make all` retains the expected checksum
exit 2 while other functions remain unmatched; that is separate from the
successful compile/link, image check and fresh matching recount.
`progress.csv`, Makefile and compiler profiles remain unchanged. README
changes contain only aggregate status rows; this note holds the recovery detail.

Production ELF:
`fdefbfd8e8452a02d60e5f55e18d30354c7e78ba7c861ae513f20d671fb36985`.
Binary:
`7691c8452dc19e4a6330bf033a6e70cdb9f34bd13d4e873167da1cee71ff08ed`.
Owner:
`3e5b30dfa9374742146cf9b2f3cebb68a92ed68c89faed0beed64e6d313d33a4`.
Guard CSV:
`2f6c2bf883add5b0f40483c282970b38ebf30463f7d7e5a7b39abfbd36941d0c`.

## Resume boundary

Next ordinary C candidate: `func_15115F68`, a 60-word leaf in
`generated_142560.c`, pending full caller/field qualification. It remains
uncredited. The smaller remaining `func_150A76F0`, `func_151F8870` and
`func_150A613C` expose handwritten nonstandard register interfaces;
`func_150AE280` switches stacks and has a mixed boundary. They are not
ordinary C leaf conversions despite their current placeholder owners.

Scratch receipts are under `conker/build/game-record-subtype-150A25D4-match/`.
Tools are committed before the consumer pin. The scoped Graphify refresh
preserves old unscanned nodes and audits changed-path relocations; it is not
a full-corpus code extraction. Frozen host Release artifacts are untouched.
