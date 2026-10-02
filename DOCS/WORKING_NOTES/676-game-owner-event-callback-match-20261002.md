# Game owner-event callback match

Date: 2026-10-02

`func_15100230` occupies 35 words and 140 bytes at
`0x15100230..0x151002BC`. Its former C placeholder returned zero and omitted
the owner-event callback.

For event `0x48`, the recovered routine compares both the owner pointer and
owner ID in the object's embedded record at offset `0x28`. A match releases
the object through `func_1516972C`. Other events are forwarded through
`func_15149514` with the owner record, owner-ID address, and object context.

The callback uses a function-specific `-O1 -g3` compact object while the
neighboring generated slice remains under its established `-O2 -g3` profile.
The semantic body has the exact 35-word extent. Twenty-eight stale-checked
words normalize one closed instruction schedule, including relocation-aware
movement of the release and forwarding calls; no behavior is supplied by an
inserted or omitted instruction.

The linked matcher advances Game to `2,506 / 4,788 (52.34%)`, with 2,282
different C rows. Overall byte-exact C progress is
`3,174 / 5,456 (58.17%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`.

Resume the ordinary small-Game queue with 34-word `func_1510E7A4`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
