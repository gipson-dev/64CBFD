# Identity-change dispatch private code-generation screen

`func_15163FEC` remains an unmodified zero-return C placeholder. No function,
matching byte, guard or production change is credited for this investigation.
Baseline at screening: consumer121abdf2/tools888a895, 4,023/5,507 exact C.
The private stage is `conker/build/game-identity-change-dispatch-15163FEC-match/`.

## Retail contract inspected

Owner `game_18D770`, VA15163FEC..151640C0, ROM19149C..191570,
53 words/frame24. A0 owner, A1 event, A2 narrowed to an unsigned byte and
stored in its incoming home. The entry is an indirect callback in
`D_8008B150[16]`, ROM22FC50 / VA8008B190, not the neighboring update table.
This table identification is from the original data assembly; full caller
execution and a complete ROM reference census are not qualified here.

Event zero compares owner identity word+18 to event word+0, then compares
owner byte+1C to event byte+4 if needed; either equality releases the owner
through func1516972C. Event2D swaps the matching owner identity between event
words+0/+4 and takes the corresponding event identity byte+9/+8. Other events
load owner subtype byte+2D, select D8008B374[subtype], and call the nonnull
callback with the original owner/event/byte arguments. The table holds NULL
and func151640C0. Its shared legacy declaration has only an s32 argument;
the private screen uses an isolated proper three-argument callback type.
No shared declaration or production caller was changed.

The adjacent func15164134 retail body has the same structure with owner
subtype+3D and D8008B37C. It was recognized from complete original assembly,
but no separate candidate compile, ABI qualification or matching claim was made.

## Measured compiler boundary

Sources use typed identity and replacement views without volatile/filler.
Four initial control forms, 24 named-local/comparison forms, 24 switch/exit
forms, nine valid flattened-exit forms and sixteen profile/type forms are
retained with complete receipts. The first exit screen rejected a void-return
expression unsupported by this IDO C dialect; it is not a passing screen.

Best normal candidate: `switch-0-1-0.c`, 52 words /21 word-position differences
including the one-word length discrepancy. Raw SHA:
`1ab6583bd89581552261d54197fa0496c2c13bd673810aef668f3e17a64f7642`.
Named locals recover the opening read order and most register roles. The
remaining boundary includes a commutative branch operand order and retail's
return-address reload/branch-delay scheduling. This is not a closed temporary
register cycle, so no word guard or inserted reload was published.

Normal O2/g3 and supported no-unroll each remain52/21. O2 without g3 is51/50;
O1 is73/72. Alternate callback return/prototype and pointer-key views do not
resolve the boundary. Source-only speculation about further epilogue recovery
is not a match or semantic proof.

No full owner/padder, actual Make, guest/native, fault-prefix, connected caller,
strict image, production or recount gates were run for this candidate. Do not
install it or credit it from the isolated source screens. Future work should
inspect the compiler's epilogue/branch scheduling, not repeat the same local
return/switch/profile matrix. All artifacts remain private and uncredited.

## Queue hygiene and continuation

Fresh actual-ELF differences were intersected with the real C definition parser,
excluding conditional definitions and existing semantic routines. A trivial C
body alone does not prove compiler-generated retail code: func151F8870 is
explicitly handwritten and uses T0/S5/S0 and multiple register results in its
bitstream contract. It remains separate assembly work, as does func150A76F0.
Do not reclassify these entries to improve the goal percentage.

The next independently qualified recovery is
[Note1954](1954-node-chain-release-guarded-match-20261101.md), func151D3130.
This private identity screen adds no matching credit. No Claude calls.
