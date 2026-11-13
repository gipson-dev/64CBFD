# Game linked-owner motion callback match

Date: 2026-11-12. `func_150D6F0C`, owner `generated_1028F0`, VA
`0x150D6F0C..0x150D7068`, ROM `0x1043BC..0x104518`, now contains its
semantic C body and matches all **87 retail words**. The prior source was a
zero-return placeholder. The observed caller passes a pointer as its second,
unused argument.

The callback retrieves the linked target at owner offset `0xA8`. It returns
zero when the target's first word is zero or its identity byte at `0x3B`
does not equal the saved identity at owner offset `0xAC`. The target pointer
is dereferenced before that check; null is not an early-return case. Otherwise it invokes
`func_150D6C98` to copy the target position, updates two owner scale fields
using `sqrt(elapsed) * scale`, stores the converted alpha byte, increments
elapsed time by `D_800BE9A4`, and returns zero if the updated value exceeds
its limit. The linked fields are read again after the helper, and the target
pointer used for the helper is retained from before the call.

The compiler emits 87 words. Ten relocation-aware expected-word guards replace
compiler words: eight normalize the frame and saved-local offsets, and two
restore retail's order for the elapsed and decay loads. Both independent
padders produce the exact retail body and relocation bindings. The compact
register metadata differs because of the new floating-point operations; the
assembled padded metadata is unchanged. All 16 other owner functions,
normalized pools and diagnostic categories were preserved.

The qualification packet is in tools commit `4e14c2d`:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_owner_scale_150d6f0c -v
```

Its seven tests pass before and after installation using both the mounted
tools and staged sibling dependencies. Coverage includes 2,304 modeled guest
cases across raw, retail and padded bodies; 192 overlapping owner/target cases;
180 modeled access-fault cuts; 80 cases connected to all 11 instructions of the
byte-exact retail helper; and 32 cases through `D_80089760[31]` and the retail
`func_151303EC` callback window at `0x15130A38`. Native 32-bit tests pass
381 cases at each of `-O0`, `-O2` and `-O3`, with eight effective negative
controls and UBSan.

The unguarded compiler output reads elapsed and decay in the opposite order
from retail in 576 modeled cases. The fault-prefix comparison checks external
writes and helper calls, and the checked retail guards restore the original
read order in the installed body; this does not claim equal read traces for
faulting or memory-mapped source accesses. Native tests restrict square roots
and float-to-unsigned conversions to defined inputs. Guest non-finite cases
and FCSR restoration use an instruction model, not hardware exception proof.
These checks do not establish visual or gameplay acceptance.

The actual Make production build equals the independently planned shadow
image. The strict linked-image audit found 225 changed bytes with **zero
exclusions**; only `func_150D6F0C` changed, all 6,050 function addresses are
unchanged, and all 189,088 protected Game-data bytes remain exact. A fresh
production recount reports **3,727 / 4,840 Game matches (77.00%)**, **4,400 /
5,513 total matches (79.81%)**, zero drift, and **145** more Game matches
needed for 80%.

The scoped Graphify refresh retained all out-of-scope nodes: 59,935 before,
59,937 after, and three relocated IDs matched by signature. Its fail-closed
path retained 31,816 existing nodes; this was not a full-corpus extraction.
