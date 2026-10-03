# Init MMIO: Partial-Volatility Compiler Trials

Date: 2026-10-03. Baseline: `90c2f9f`.

## Result

Twenty new distinct isolated compilations do not produce an eleven-word retail
match for `func_100038E0`. Production assembly, compiler profiles, word guards,
and aggregate coverage are unchanged. This is a bounded negative result, not
proof that matching C is impossible.

The new hypothesis was that qualifying only one global publication volatile
could preserve retail's separate value materializations/address lifetime
without the extra instructions seen when both publications were volatile.
The `-O1 -g3` profile was also tested, separately from earlier `-O1` trials.

## Source Shapes

Each fixture declares `u32 D_80038070` and `u16 D_80038074`, has a void
no-argument function, and retains three separate statements:

1. Address publication volatile; value publication ordinary:

```c
*(volatile u32 *)&D_80038070 = 0xBC000C02;
D_80038074 = 0x4040;
*(volatile u16 *)0xBC000C02 = 0x4040;
```

2. Address publication ordinary; value publication volatile:

```c
D_80038070 = 0xBC000C02;
*(volatile u16 *)&D_80038074 = 0x4040;
*(volatile u16 *)0xBC000C02 = 0x4040;
```

3. Shape 1 with `register volatile u16 *address = (volatile u16 *)0xBC000C02`,
   publishing `(u32)address` and writing `*address`.
4. Shape 2 with the same register-pointer local.

These are compiler-shape probes. Their emitted order was checked; source
statement separation alone is not a language-level ordering proof for all
ordinary versus volatile accesses. No new return value or hardware identity
was invented.

## Measurements

Cells are **body words / differing aligned word positions**; retail is eleven
words. Include the actual return delay slot, excluding alignment padding.

| Shape | `-O2 -g3` | `-O2` | `-O1` | `-O1 -g3` | `-O0` |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 12 / 12 | 11 / 10 | 12 / 12 | 13 / 13 | 15 / 15 |
| 2 | 12 / 12 | 11 / 9 | 12 / 11 | 13 / 12 | 15 / 14 |
| 3 | 12 / 12 | 11 / 10 | 13 / 13 | 13 / 13 | 16 / 16 |
| 4 | 12 / 12 | 11 / 9 | 13 / 12 | 13 / 13 | 16 / 15 |

The eleven-word variants still rematerialize the MMIO base and put the hardware
store in the return delay slot; they do not reduce to a closed register rename
or independent scheduling adjustment. The partial volatile store requires
explicit address materialization. No normalization batch is justified.

All twenty emitted bodies were decoded in an isolated instruction trace:
exactly a word store `0xBC000C02` to `0x80038070`, a halfword `0x4040`
to `0x80038074`, then a halfword `0x4040` to `0xBC000C02`, with the initial
stack pointer restored. This confirms the checked emitted store trace, not
hardware behavior, original source provenance, or byte-exactness.
The final matrix was rerun after extending the narrow trace to recognize the
unoptimized branch over its nop; twenty distinct variants, forty compilations.

## Reproduction

Ignored fixtures and output remain under `conker/build/`:
`init-mmio-partial-volatile.c`, `init-mmio-partial-volatile.py`,
`init-mmio-partial-results.json`, and twenty linked/disassembled objects.

From `conker/`:

```sh
python3 build/init-mmio-partial-volatile.py
../ido/ido5.3_recomp/cc -c -32 -G 0 -Xfullwarn -Xcpluscomm \
  -signed -nostdinc -non_shared -Wab,-r4300_mul -mips2 -o32 \
  -DSHAPE=2 -O2 -o build/init-mmio-partial-2-o2.o \
  build/init-mmio-partial-volatile.c
mips-linux-gnu-ld -m elf32btsmip -Ttext=0x100038E0 \
  -e func_100038E0 --defsym=D_80038070=0x80038070 \
  --defsym=D_80038074=0x80038074 \
  -o build/init-mmio-partial-2-o2.o.elf build/init-mmio-partial-2-o2.o
mips-linux-gnu-objdump -d -z build/init-mmio-partial-2-o2.o.elf
```

## Regression / Baseline Checks

Three tracked tests in `tools/tests/test_init_mmio_assembly.py` now check:

- The original contiguous eleven-word slot, nop return delay, and retained
  assembly ownership. Retail SHA-256:
  `2afa60e885db40dd282ff0cf18ffe43a5716521c18c5c235975bcf8cb84d97f4`.
- The three-store sequence from two distinct initial register patterns,
  with preserved general callee-saved registers, stack/frame pointers, and ra.
- Independently assembled and linked reference bytes at retail addresses.

All 170 tool tests and project checks pass. Both existing complete Init ELF
sections still match retail, with the hashes from Note 761. No full project
rebuild was necessary or performed: no production build input changed.
No hardware write, guest execution, host-port build, or gameplay test occurred.

## Next Action

Keep both small Init leaves deferred. This adds to the prior five plus twenty
MMIO trials without establishing a production conversion. Do not repeat the
completed matrices or replace the body merely because it fits the slot.

Resume ordinary Game semantic recovery at `func_15045384`, following the
already recovered highest-height query. Reopen Init only with new source
provenance/dataflow evidence or an explicitly scoped whole-contract rewrite.
