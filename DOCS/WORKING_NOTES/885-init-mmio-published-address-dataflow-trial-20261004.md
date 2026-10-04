# Init MMIO Published Address Dataflow Trial

Date: 2026-10-04. Baseline: `76537bd5`.

## New Hypothesis

Earlier MMIO trials used local address variables, combined expressions,
partial volatility or the published halfword value. This fixture instead
uses the published word address as the final hardware-store destination.
It preserves the existing u32/u16 declarations and void signature:

```c
void func_100038E0(void) {
    D_80038070 = 0xBC000C02;
    D_80038074 = 0x4040;
    *(volatile u16 *)D_80038070 = 0x4040;
}
```

This is an isolated compiler probe, not a replacement contract. The source
introduces an ordinary global read, absent from retail; a matching candidate
would need the compiler to eliminate it. No device identity or return-value
contract is invented. Both prior local-pointer and partial-volatility
matrices remain in Notes 750/762 and are not repeated here.

## Measurements

Five IDO profiles compile and link the standalone fixture at 0x100038E0,
with D_80038070/74 fixed at their retail addresses. Compare all words through
the last JR RA delay instruction, excluding trailing section padding.
Differences are aligned word positions plus excess/missing body words,
not instruction edit distance. The retail body has eleven words.

| Profile | Body words | Different words | Reads published address |
| --- | ---: | ---: | --- |
| O2/g3 | 12 | 12 | Yes |
| O2 | 11 | 10 | Yes |
| O1 | 11 | 8 | No |
| O1/g3 | 12 | 10 | No |
| O0 | 15 | 14 | Yes |

No profile is byte-exact. All compiler logs are empty.

O1 does retain the complete address in T6 rather than rematerialize the
hardware base, but copies it to T9 at 0x100038FC. It materializes the final
value in T8 and performs the hardware store in JR RA's delay slot. Retail
uses V0 throughout, has no address-copy instruction, performs the hardware
store before return and has a nop return delay. This is not only an
independent scheduling or closed register-rename difference; no guards added.
O1/g3 moves the store before return but keeps the extra address copy and
requires twelve words. O2/O0 leave an additional word read at 0x80038070.

## Store Trace And Baseline Checks

A narrow architectural-value decoder checks each linked trial for two
initial register seeds, recognizing emitted loads/stores and supported
straight-line/return forms. All ten traces have exactly the three external
stores in order: word 0xBC000C02 to 0x80038070, halfword 0x4040 to 0x80038074,
then halfword 0x4040 to 0xBC000C02. Stack pointer and callee registers hold.
Extra global reads are reported rather than hidden. Stack traffic is modeled
separately and is not counted as external MMIO stores. This does not qualify
hardware timing, general control flow, source-level ordinary/volatile ordering,
or extra-read equivalence. No host MMIO is executed.

All three existing MMIO assembly tests pass in 0.034 seconds, no skips:
original eleven-word ownership/hash and nop delay, ordered store/callee
contract, and freshly assembled/linked retail bytes. Scoped production/test/
word-patch diffs are empty. Tool and whitespace checks pass.

## Reproduction And Decision

Ignored fixture and driver are
`conker/build/init-mmio-published-address-20261004.c` and `.py`.
The driver emits `init-mmio-published-address-results-20261004.json`, logs,
objects, linked ELFs and disassemblies under `conker/build/`.

```powershell
cd conker
wsl python3 build/init-mmio-published-address-20261004.py
```

Keep production `init_38E0.c` GLOBAL_ASM and the original assembly intact.
Published-address dataflow narrows one O1 difference but does not supply
the complete eleven-word C match. Further MMIO work needs a new justified
source/provenance hypothesis; do not repeat this fixture unchanged.
No production ROM build, conversion, profile change, sibling-port test or
progress update is claimed. README totals and qualified decoder sources
remain unchanged; unrelated Game source/tests are preserved and unstaged.
