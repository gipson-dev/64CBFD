# Game fixed-effect packet direct match

Date: 2026-11-13. `func_150AFC68` in `generated_DC6B0.c` replaces its
zero-return placeholder with the recovered six-argument effect-preset wrapper.
Its 82-word body occupies VA `0x150AFC68..0x150AFDB0` and ROM
`0xDD118..0xDD260`. Every instruction and its factory relocation emit directly
from C; both supported padders match retail without added guards.

The wrapper submits a fixed 49-argument preset to `func_1516D99C`, forwarding
four caller words into the appropriate factory slots, the low byte of the
fifth argument, and the sixth argument as a word. The recovered factory
prototype is retained from its own definition. Its narrow parameters consume
the appropriate low bits even when the o32 outgoing stack slots retain the
caller's full word. Two original call windows in `func_15052590` pass the
current identity and fixed preset variants; their bounded windows passed 20
cases per stream. This does not qualify the complete parent.

Tools commit `09cd306` supplies the reproducible checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_fixed_effect_150afc68_match -v
```

An independent model checked the complete 49-word packet in 402 cases per
stream across retail, raw C, and both padded bodies, with outgoing and incoming
home-slot mutations. Retail and the C streams agree at 114 injected
access-boundary prefixes. A connected test runs the original
`func_1516D99C` body and checks its full resulting record in 76 cases per
stream, covering both success and failure from a modeled allocator. Native
32-bit checks passed 2,048 cases at each of `-O0`, `-O2`, and `-O3`, with
UBSan and eight effective negative controls. Twelve GNU links across three
symbol layouts verified every stream against rebased retail. The suite passed
before and after installation with mounted tools and staged sibling
dependencies, and project tool checks passed. The allocator and hardware
runtime are not established by these tests.

The production object and ELF equal the independently audited Make-planned
shadow; the other 1,453 linked objects are unchanged. The strict image
prediction accounts for 245 changed bytes with zero exclusions. Only this
body changes among 6,051 functions; all addresses and all 189,088 protected
Game-data bytes remain fixed. Seventeen other owner functions and constant
pools are unchanged. The two existing owner warnings remain the same after
normalizing their shifted source-line numbers.

The separate preliminary `func_150F1A00` pulse-update screen remains private:
it selects one of three phase increments and scales a 3-by-3 actor matrix, but
the current compiler shapes still differ substantially in loop scheduling and
require an alias-aware qualification. It is not counted.

The production recount reports Game **3,752 / 4,843 (77.47%)**, total
**4,425 / 5,516 (80.22%)**, zero address drift, and **123** further Game
matches required for 80%.
