# Init MMIO Pointer-Lifetime and Profile Trials

Date: 2026-10-02

## Result

`func_100038E0` remains original assembly after twenty additional isolated
compilations: five source shapes across four IDO profiles. None matches its
eleven retail words. This advances the deferred experiment from the prior
five trials in [Note 737](737-init-mmio-leaf-bounded-compiler-experiment-20261002.md);
it does not establish an impossibility result or change conversion totals.

The production source, compiler profiles, word guards, and linked project
artifact are unchanged. No full build, host MMIO execution, or gameplay test
was performed. Diagnostic sources, objects, linked fixtures, and disassemblies
are retained under ignored `conker/build/`.

## Experiment

The source fixture is `conker/build/init-mmio-resume-experiment.c`, driven by
`conker/build/init-mmio-resume-experiment.py`. Shapes use local `u32`/`u16`
typedefs and the two existing global declarations. Shape 1 is:

```c
void func_100038E0(void) {
    volatile u16 *address = (volatile u16 *)0xBC000C02;
    D_80038070 = (u32)address;
    D_80038074 = 0x4040;
    *address = 0x4040;
}
```

Other shapes:

2. A `register volatile u16 *address`, initialized by the expression
   `(volatile u16 *)(D_80038070 = 0xBC000C02)`, then the two halfword stores.
3. A single assignment expression:
   `*(volatile u16 *)(D_80038070 = 0xBC000C02) = (D_80038074 = 0x4040, 0x4040)`.
   The outer assignment operands do not establish the required relative
   ordering of the two global publications in the C language. This is only
   a compiler-shape probe, not an accepted production contract.
4. Shape 1 with both global publications also cast to volatile pointers.
5. A local `u32 address`, followed by the two global publications and
   `*(volatile u16 *)address = D_80038074`. This tests value reuse; it does
   not justify introducing an actual extra global read in a replacement.

Common compiler options from `conker/`:

```sh
../ido/ido5.3_recomp/cc -c -32 -G 0 -Xfullwarn -Xcpluscomm \
  -signed -nostdinc -non_shared -Wab,-r4300_mul -mips2 -o32 \
  -DSHAPE=1 -O2 -g3 -o build/init-mmio-resume-1-o2g3.o \
  build/init-mmio-resume-experiment.c
mips-linux-gnu-ld -m elf32btsmip -Ttext=0x100038E0 \
  -e func_100038E0 --defsym=D_80038070=0x80038070 \
  --defsym=D_80038074=0x80038074 \
  -o build/init-mmio-resume-1-o2g3.o.elf build/init-mmio-resume-1-o2g3.o
mips-linux-gnu-objdump -d -z build/init-mmio-resume-1-o2g3.o.elf
```

Repeat with shapes 1 through 5 and profiles `-O2 -g3`, `-O2`, `-O1`,
and `-g`. Each standalone object was linked with the retail function and
global addresses before comparison against ROM bytes `0x38E0..0x390C`.
Counts include the final `jr ra` delay slot and exclude section alignment
nops. Difference counts compare aligned word positions and count excess or
missing body words as differences; they are not an instruction edit distance.

## Measurements

Each cell is **body words / differing words**. Retail has eleven body words.

| Shape | `-O2 -g3` | `-O2` | `-O1` | `-g` |
| --- | ---: | ---: | ---: | ---: |
| 1: Local pointer | 11 / 9 | 10 / 10 | 15 / 15 | 17 / 17 |
| 2: Register pointer, assignment initializer | 11 / 9 | 10 / 11 | 13 / 11 | 15 / 15 |
| 3: Combined expression probe | 11 / 9 | 10 / 10 | 12 / 9 | 14 / 14 |
| 4: All publications volatile | 13 / 13 | 12 / 12 | 17 / 17 | 19 / 19 |
| 5: Published-value reuse | 12 / 11 | 11 / 10 | 15 / 15 | 18 / 18 |

Shapes 1, 2, and 3 emit identical eleven-word bodies under `-O2 -g3`.
They hoist `0x4040` into `$v0`, publish the address from `$t6`, and
rematerialize a hardware base in `$t7` instead of retaining retail's full
address in `$v0`. Explicit local pointer lifetime does not force the desired
machine-register lifetime under that profile.

Without `-g3`, Shape 1 has ten words and puts the hardware halfword store
in the return delay slot. Counting the last nonzero word plus a presumed
nop would misreport this as eleven; measurements above explicitly include
the actual delay instruction and exclude subsequent padding.

The `-O1` pointer variants retain a live address but introduce an eight-byte
frame with stack adjustment and restoration. The combined-expression probe
retains the address in `$a0`, not `$v0`, and still has the extra frame.
The fully volatile publications add explicit global-address materialization.
No trial reduces the remaining difference to an established register-only
or independent-scheduling normalization.

## Resume Boundary

Keep production `conker/src/init_38E0.c` and its `GLOBAL_ASM` unchanged.
Do not use the combined-expression probe as a semantic replacement or add
a word-patch batch just because one variant fits the slot.

The next bounded Init experiment is `func_10005BE0`: seek a new loop/mask
shape beyond the three trials in
[Note 738](738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md)
before extracting it from `init_5AB0`. The full inventory and acceptance gates
remain in [Note 749](749-init-remaining-assembly-resume-assessment-20261002.md).
Ordinary Game target `func_15040CC8` remains untouched.
