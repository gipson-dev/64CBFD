# Attached cash-label callback restored with closed clamp guards

`func_151D7000` now has a complete semantic C body in
`conker/src/game/generated_203E20.c`. Its linked 51-word, 204-byte slot matches
retail, including all six relocation bindings. The raw compiler body needs
ten checked word guards. These normalize a closed signed-low16 clamp,
control flow and private halfword spill layout; they are not merely ten
independent scheduling changes.

The normal production build and an independent recount of the Windows
consumer ELF establish **4,001 / 5,506 (72.67%)** exact C functions, Game
**3,328 / 4,833 (68.86%)**, zero address drift and 1,505 still different.
Init remains 492/492 and Debugger 181/181. The 75% objective is still active:
4,130 exact functions are required, so **129 more** remain. The conversion
inventory CSV is byte-identical to its predecessor.

## Recovered behavior and ABI

The callback receives one owner pointer. Owner+0x48 points to a label record;
the record starts with its actor pointer and contains an identity byte at+4,
signed cash amount at+8, signed fade threshold at+0xC and signed rate at+0xE.
An inactive actor or a mismatched actor identity byte at+0x3B returns zero
without touching the later lifetime/fade fields or submitting text.

The signed owner lifetime at+0xE selects either opacity255 or the product of
two signed16 values. The low16 product is interpreted as signed and clamped
to zero if negative. The color helper takes its low byte. The actor is
attached with flags 0x109, color is (50,125,28), command is 0x81 and the original
format at `D_800AB254` is `$ %d`.

The label pointer is retained across the three setup calls, while its cash
amount is read live immediately before formatting. Native helper mutations
explicitly distinguish these two lifetimes. The signed16 product fits in
signed32; the low16 conversion is deliberate.

Physical Game-data mapping is ROM 0x2275E0 -> VA 0x80082B20. The sole aligned
callback pointer is at ROM 0x22D36C -> VA 0x800888AC, namely `D_800888A0[3]`.
The complete 35-word parent `func_150D0034` consumes the callback result:
zero expires the owner by storing -1 at+0xE; nonzero clears flag bit 0 at+0x30.
The selector -1 path also clears that flag without making a callback.

For this nonempty format, the original text emitter returns the final packet
address on success and zero on allocation failure. The original printf
wrapper and this callback forward that word. The local prototype records
this measured retail ABI. The separately recovered helper in `game_70200.c`
still has a stale void declaration/body interface; this change does not
claim its native C implementation is qualified or alter that helper.

## Closed normalization and source evidence

The compiler emits all 51 words with a 40-byte frame. The ten guarded offsets
are 0x4C,0x50,0x58,0x60,0x64,0x68,0x6C,0x70,0x7C and0x88. There are no inserted
or omitted instructions, added helpers, FP operations or changed bindings.

The branch region reaches the same helper boundary on both routes. The
multiply inputs commute. Both clamp implementations first discard arbitrary
upper product bits; all 65,536 low16 patterns were executed independently for
both instruction windows, totaling 131,072 executions. Another 60 branch cases
and all 32,768 legal retained reload values pass. Live boundary arguments,
ordered memory accesses and the multiply HI/LO result agree.

The private halfword moves from raw SP+0x1C to retail SP+0x1A. The retained
label pointer stays at SP+0x20, saved RA at+0x14 and outgoing argument homes
at+0..0xF. The retail signed reload and raw unsigned reload produce the same
word because the retained result lies in 0..32767. Both additionally feed a
helper that masks the low byte. The original variadic wrapper copies surplus
guest stack words; `$ %d` consumes only the supplied amount. This is bounded
guest evidence, not a portable C claim about surplus varargs accesses.

Fresh qualification in each tools checkout includes:

- 1,080 raw-C/retail cases, 2,160 root executions, using329 original helper
  words: attachment 12, color 22, command 7, printf wrapper 36 and emitter 252.
  Only allocation and decimal `sprintf` are bounded ABI services. Actual
  packet text, fields, list links, opacity and zero/allocation paths agree.
- 38 parent cases, 75 executions, covering all 35 original parent words.
  Root coverage is 50/51; the remaining word is a duplicate unreachable load.
  Emitter coverage is 178/252 for the fixed cash-label format. Other formats
  and full allocator, `sprintf` or rendering hardware are not qualified.
- 43 fired memory-prefix cases, 86 executions, with the explicit private
  spill mapping; four sparse invalid executions and three connected alias
  cases. Guest fault prefixes do not assert portable C fault semantics.
- Typed native32 object layouts and canaries, complete helper order and
  arguments, live mutations, full32-bit returns and UBSan at O0/O2/O3.
  Each profile runs 76,336 positive cases and 10,800 cases for each of nine
  separately compiled, effective semantic controls.
- Fresh complete owner compilation/padding, all six compact and padded
  neighbors and pools unchanged, no new diagnostics. Every new guard has
  effective expected-word and relocation-preimage controls, 20 total.

## Production image and dependent object audit

The real generated-owner Make recipe executes three normal O2/g3 commands.
Its complete object equals the independently compiled and padded object.
The independent link is compared literally against the entire predecessor
ELF, with the target bytes, its symbol extent 12->204 and one explicitly
predicted adjacent BFD symbol/string pair permutation. There are no image
exclusions. Named definitions remain unchanged except the target extent.
All 6,055 other function bodies and all addresses are fixed. Protected Game
data is byte-exact across 189,088 bytes and 720 owners.

Changing the shared guard CSV caused normal Make to rebuild dependent
objects. The focused fixture caught `sinf.c.o` outside the target. Its previously stale
undefined `D_800BE358` size 8 became 128, matching the already existing
`variables.h` declaration; the debug array upper bound and external size
followed, and debug timestamp/header-size records refreshed. Exactly 210
object bytes differ, confined to `.symtab` and `.mdebug`. A complete-object
constructor predicts every changed byte from the frozen predecessor. All
other sections, its function body and bindings are identical. Its metadata
does not change the literal whole-ELF prediction. This dependency is audited
explicitly rather than excluded from the input or image checks.

The subsequent full 17,365-file baseline audit also found the same stale
EEPROM extern metadata in `debugger_258ED0.c.o`, outside the focused fixture.
Its only changed sections are likewise `.symtab` and `.mdebug`, with the
sole named-symbol delta being the undefined EEPROM size 8->128. Its function
body, all bindings and every other section are identical. The independently
predicted complete ELF remains byte-identical after this full-build audit.
`dependent-full-build-audit-v18.json` records that additional object and
its before/after SHA-256 values; the rebuilt object is preserved in both
Native and WSL current baselines.

Production ELF SHA-256:
`164df1215699e8a1c71efe922af788dbe97ff180ded1ecd2770e73265b09e108`.
Raw callback payload:
`38faafc2a78ea3c2ff911625862fc60a957d684bc23247c69f3cd9f1a573a3a6`.
Normalized unrelocated payload:
`8b6aca29cc7fed0686fade4e290da763f7ab5c65c6177484e715b234f9b27691`.
Linked retail callback:
`185a7d4cc630c3dc6b553bc072b0c5930d72fb8efa9e86fa4ecf11250edf7b7e`.

## Reproduction and continuation

Tools commits `5a57374` and `762ffce` precede the consumer pin. Eight fresh
target tests and the shared checks pass in both local tools copies. The
older mirror's inherited edits are preserved and it is not committed.
Neither repository is pushed.

With the prepared consumer inputs and retained target build directory:

```sh
python3 -m unittest tools.tests.test_game_attached_cash_label_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The retained stage is `conker/build/game-attached-cash-label-151D7000-match`.
`preparation.json` records the independently executed Make/link;
`production-v14.json`, `installed-audit.json` and
`native-production-recount.txt` record production acceptance.
`dependent-object-audit-v10.json` preserves the caught dependency change;
the canonical constructor and corruption controls qualify it exactly.

Earlier fixture failures are retained separately: one missing transferred
proof, a moved local name and an incorrect expectation that selector -1 left
the parent flag unchanged. The corrected suite passes. They are not counted
as compiler or production defects. The preceding private fixture overlap
at guest stack 0x40000 was corrected to a disjoint label at 0x41000.

Next screen: `func_15154C90`, the 60-word lifetime/callback/fade dispatcher
that already supplies useful caller evidence for other adopted callbacks.
Its C reconstruction and full qualification remain to be done. The motion,
path-height, gate and other private candidates remain uncredited.
