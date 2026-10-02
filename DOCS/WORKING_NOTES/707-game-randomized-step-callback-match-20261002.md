# Game randomized-step callback match

Date: 2026-10-02

Game `func_1518F7C4` occupies the 37-word slot at
`0x1518F7C4..0x1518F858`. It samples `func_150ADA68`, combines that sample
with the base and scale floats at object offsets `0x34` and `0x38`, scales the
result by `D_800BE9A4`, and accumulates it into the float at offset `0x30`.
After `func_1518F8E0` updates the object, signed selector `-1` at offset
`0x88` returns one; any other selector dispatches the object through
`D_8008D67C` and returns that callback's result.

The prior zero-return placeholder omitted the complete randomized update and
callback path. A typed record rooted at object offset `0x30` recovers the
three float fields and signed callback selector. Typing `D_8008D67C` as an
array of one-argument integer-returning callbacks preserves the retail return
contract; its retail entry `func_151905BC` returns one.

IDO emits the arithmetic core and indirect call directly but collapses the
record base into the object pointer, uses a smaller frame, fills the first
call delay slot, and reverses the callback branch layout. Twenty-two
stale-guarded rows normalize that closed compiler layout. Seven checked
insertions and two checked omissions expand the 32-word compact routine to
the retail 37-word slot while preserving the call and global-data
relocations. No compiler-profile override is used.

The focused object and complete repository rebuild passed. The linked bytes
at `build/conker.us.bin+0x1BCC44` and retail bytes at
`conker.us.bin+0x1BCC74` share SHA-256
`ff6f5421d43c98c6c930c115fbe72cb1abbf44859b61fa882d5458cd38a4afb0`.
The guard table contains 10,283 rows with no duplicate keys. The linked
matcher reports zero address drift and advances Game to
`2,546 / 4,788 (53.17%)`, with 2,242 different C rows; overall byte-exact C
progress is `3,214 / 5,456 (58.91%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.

No fresh gameplay run was performed. This checkpoint is semantic recovery,
focused-object disassembly, exhaustive build, and linked-byte comparison
evidence.

Resume the ordinary small-Game queue with 62-word `func_1507A528`, currently
at 34 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
