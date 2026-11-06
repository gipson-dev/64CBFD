# Text-buffer fade semantic recovery and private-home boundary

Date: 2026-11-06. Continue the 80% goal from consumer
`0b4642f6d3460f6751cddf366091ef91a4cfa298` and mounted tools
`e9aebb8eb91dc330fd162c21f47ca2f738c70f3f`.
[Note 2116](2116-game-oriented-effect-parameter-constructor-direct-match-20261106.md)
remains the latest adopted exact function. This note adds qualification
evidence and no matching credit.

## Target and recovered contract

`func_150D01A0` belongs to `generated_FC5F0`:
VA `0x150D01A0..0x150D02B4`, ROM `0xFD650..0xFD764`,
69 words / 276 bytes, frame0x30. Its table is `D_800888A0[0]`, with the
sole aligned literal at ROM0x22D360. There are no direct JALs. The original
parent `func_150D0034` calls it at0x150D0078 and consumes its return value
at0x150D0084: zero expires the record; this routine must return1. The
existing table declaration confirms `s32(u8 *)` compatibility. This is
static caller analysis, not a claim that the complete caller was executed.

The owner's existing `TextDescriptorFC5F0` begins at0x28: active byte0x30,
index0x3D, buffer pointers0x40/0x44, payload pointer0x48. Active mask1
resets the signed payload byte to8. A positive countdown gives
`opacity = (count * 31) & 255`, inverse255-opacity, then stores
`count - ticks` modulo256. Nonpositive values use opacity0/inverse255.
The inverse pass submits the indexed text buffer; the opacity pass uses
index XOR1. Each pass sets color206/196/97, then text coordinates146/190
and mode129. The owner is reloaded after the first color provider, and the
second descriptor pointer survives its color provider in a private home.

The retained private source uses typed payload access through the existing
descriptor. Tick subtraction is explicitly unsigned before byte truncation,
avoiding signed-overflow assumptions for extreme tick words. The formal
address expression remains an experiment, not original-source provenance.
No volatile qualifier, frame patch, guard, or production source is installed.

## Reproducible semantic qualification

Run from the prepared consumer root:

```sh
python3 -m unittest tools.tests.test_game_text_buffer_fade_recovery -v
```

Five checks pass in the mounted checkout. The same new modules also pass
through an ignored overlay using the dirty sibling's actual complete-owner
compiler helper, object parser, MIPS oracle and native32 command builder.
The overlay supplies the new files and uses the pinned mounted relocation
decoder where that newer module is absent from the sibling. Nothing is
written to the sibling. Both tools smoke checks pass. This does not claim
the older standalone checkout already contains every new module.

- **4,600 cases per guest body** compare retail and raw C against an
  independent external-state/call-order reference. They cover all256 signed
  countdown byte encodings, both active states, both valid buffer indices,
  two stack phases, extreme tick words, and mutable index/buffer/countdown
  effects at opaque calls. All69 retail instructions execute across the
  corpus; preserved ABI registers and return1 are checked. Complete private
  stack equality is explicitly not claimed.
- **61,440 native32 executions**, SDK layout checks and O0/O2/O3 with UBSan,
  check all defined external state and calls. The callback is invoked through
  the compatible `s32 (*)(u8 *)` type. Seven controls fail: unsigned count,
  omitted reset, added ticks, multiplier32, added inverse, same-buffer second
  pass, and false return0. Only buffer indices0/1 are native-qualified.
- **Eight frozen production inputs** remain byte-identical: source, owner,
  original ASM, Makefile, guards, ELF, ROM and progress CSV. Their snapshot
  and all screen/native/private receipts are retained under
  `conker/build/game-text-buffer-fade-150D01A0-match/`.

The first guest fixture accidentally placed its payload at the emulated
stack base. That fixture collision is corrected and guarded by an explicit
disjointness assertion. Native comparisons verify each state's own payload
pointer before normalizing the different fixture addresses for comparison.

## Measured private-home failure

The best candidate still emits69 words/frame0x30 with **34 literal word
differences** and all six bindings. It writes an opacity copy to **SP+0x20**,
reloads a T8 value for the second-pass gate, and places the descriptor pointer
at SP+0x24. Retail gates directly on S0 and uses SP+0x20 only as the second
descriptor pointer home. Retail also retains the positive-count exit branch
with the byte store in its delay slot; the candidate falls through.

The regression witness is concrete: use countdown0, flags0, tick7, and bind
the tick word to SP+0x20. Retail leaves the tick word7; raw C overwrites it0
with the extra spill. Their ordinary provider calls agree, but memory-access
traces and the named tick state differ. This guest-only stack alias is not
a portable native-C test. It disproves a scheduling-only or dead-register
explanation; no normalization rows are justified by current evidence.

The wider production gates remain pending: whole owner/padder/pools, complete
caller execution, original helper integration, fault-prefix equivalence,
independent GNU links, strict image prediction, actual Make/recount, and any
adoption. Passing the semantic tests is not exact-match evidence.

## Source screens and bounded advisory

The first plain-pointer body emits64 words/frame0x30. The indexed formal
address view recovers69/frame0x30; a named home pointer gives frame0x38, and
simple `*(&owner)` folds back to64. Register hints and explicit byte casts
leave the34 differences unchanged. Widened/signed opacity variants, split
gates, declaration changes, else branches, goto exits and O1/O2-without-g3
profiles either change the frame/length or fail to improve the fit.

One packet-only Claude analysis used no tools or repository access. Its
packet SHA-256 is
`ff53e7dd8de53ebbfae88d090a99b260223627a31369efe757d9a8b1521b0f6a`.
The proposed cached count/value-reuse hypothesis was independently tested:
both signed-byte and signed-word temporaries emit65 words/frame0x28,
including explicit-cast forms. Explicit casts alone remain69/0x30/34.
The proposed second-pass statement order was already present. These results
reject the advisory's expected branch/spill recovery; no suggestion is
adopted on authority and no additional advisory is needed for this packet.

The adjacent auto-decompiled source has wider flag/index loads that disagree
with retail and signed subtraction assumptions. It is not imported or counted.

## Progress and next action

Production remains **4,186/5,512 (75.94%)**, Game **3,513/4,839 (72.60%)**,
Init492/492, Debugger181/181, zero drift. **224 more** exact functions are
needed for the4,410 threshold. README aggregates remain unchanged.

Stop broad syntax screens for this target. The next focused investigation is
the CFE/UOPT transition that creates the opacity spill and splits the gate's
value from the retained S0 color argument. Compare the formal-home/address
flags and lifetime records with the decoded SP+0x20/SP+0x24 stores before
trying another source form. Preserve the passing semantic oracle and its
negative private-home witness. Keep this target uncredited until all gates
pass; other Game recoveries may advance the80% total meanwhile.

The graph update is scoped with old-node retention. The prior ordinary CLI
refusal of a smaller graph is reused as the known corpus boundary; this is
not a new full-corpus re-extraction. Preserve the eight separate boundaries
from Note2116, unrelated sibling edits, private inputs, real saves and frozen
host Release. No host-port acceptance is added.
