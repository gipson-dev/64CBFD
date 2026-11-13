# Game wrapped-angle velocity smoother match

Date: 2026-11-12. `func_15049688` in `generated_76A60.c` replaces a
zero-return placeholder with semantic C. The retail body is VA
`0x15049688..0x150497DC`, ROM `0x76B38..0x76C8C`: all **85 instruction
words** match, followed by one slot-alignment word. The 80-word compiler body
uses 39 checked relocation-aware guards, including five inserted instructions,
to reproduce retail scheduling and control flow. Both independent padders
produce the exact retail body and bindings.

The routine obtains the wrapped target difference from `func_15048A70`,
damps and integrates velocity, checks for overshoot when the absolute
difference is below 10 degrees, and normalizes the result through
`func_15048758`. The original `func_15121C00` caller supplies the six O32
arguments and consumes the updated angle. Position and velocity can alias;
the retained C stores the target before clearing velocity on a snap.

An alternative 83-word candidate matched the ordinary cases but changed public
memory at an interrupted access when the two pointers alias. The retained
80-word candidate preserved retail's public state for all modeled cuts below.
These tests model access boundaries; they do not establish portable C fault
semantics or gameplay acceptance.

Tools commit `ce85a13` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_angular_smoother_15049688_match -v
```

All seven checks passed before and after installation using mounted tools and
staged sibling dependencies. Coverage includes 1,072 finite cases against an
independent floating-point model with both original angle helpers connected,
56 cases through the original caller, 112 completed pointer/stack overlaps,
192 special floating-point bit-pattern cases, and 796 modeled access cuts.
Four further deliberate overlaps hit the emulator instruction limit in every
version and are incomplete. Native 32-bit builds at `-O0`, `-O2`, and `-O3`
each pass 536 cases with UBSan and ten effective negative controls. Twelve GNU
links cover three symbol bases. The modeled NaN and subnormal checks are not
hardware FCSR, exception-mode, or gameplay validation.

The actual Make build matches the independently audited shadow ELF, binary
and owner object. The strict image audit accounts for **232** changed bytes
with zero exclusions; only the target function changed, all **6,050**
function addresses stayed fixed, and all **189,088** protected Game-data
bytes were unchanged. The other 1,453 linked objects and conversion rows were
preserved. A fresh linked recount reports Game **3,740 / 4,842 (77.24%)**,
total **4,413 / 5,515 (80.02%)**, zero drift, and **134** more Game matches
needed to reach 80%.

The `func_150B9D8C` screen in [Note 2343](2343-game-effect-descriptor-alias-screen-20261112.md)
remains private. This turn tested 54 small-local declaration arrangements and
18 aligned work-area forms; none reproduced the two retail RNG spill slots,
descriptor address, and `0x88` frame together. Its caller and overlap contract
remain unresolved, and it receives no match credit.

Next screen `func_15072F10` in `game_981E0.c`, a remaining 81-word
placeholder; its state accesses, call contract, and callers need qualification.

The scoped Graphify refresh retained or relocated all 59,963 previous nodes,
with 59,965 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
