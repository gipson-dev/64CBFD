# Game paired object-state transition match

Date: 2026-10-02

`func_150CF0A0` replaces its zero-return placeholder with the 40-word retail
routine at `0x150CF0A0..0x150CF140`. It selects between handling an existing
state-two caller and placing two referenced objects into that state.

The function first tests the low two bits of caller byte field `0x73`. When
they already equal two, it forwards the caller to `func_15117798`. Otherwise,
the update path requires bit two of caller field `0x4F` and nonzero byte field
`0x57` in the object referenced by `D_800CC5EC`.

When both gates pass, `func_151149AC` resolves object IDs `0xFE` and `0xFD` in
sequence. Each returned object's byte field `0x73` is updated with separate
`&= ~3` and `|= 2` operations. Those distinct compound assignments preserve
retail's intermediate clear store and final state-two store; combining them
into one assignment omits two words per object. Keeping the existing-state
handler in the final `else` block also reproduces retail's branch placement.

The complete routine emits directly from semantic C with no expected-word
guards, checked insertions or omissions, relocations, or compiler-profile
override. The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with
zero address drift. The linked and retail 160-byte spans are identical, with
SHA-256:

```text
490810107b5323085833837e355928cb311f43f6cb2855ac0740251592146f7c
```

Game advances to `2,551 / 4,788 (53.28%)`, with 2,237 different C rows;
overall byte-exact C progress is `3,219 / 5,456 (59.00%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 37-word `func_1500F378`, currently
at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
