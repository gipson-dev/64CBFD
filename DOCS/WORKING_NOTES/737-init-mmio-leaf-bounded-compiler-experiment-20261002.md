# Init MMIO Leaf Bounded Compiler Experiment

Date: 2026-10-02

## Outcome

`func_100038E0` remains assembly. Five isolated IDO compilations establish
the behavior and current compiler differences, but do not produce a direct
eleven-word match. No production source, compiler profile, layout, guards,
or progress totals changed. This is an experiment result, not a proof that
the routine can never be converted.

The prior turn completed `func_10001420`; this follow-up advances the next
Init candidate from an untested proposal to bounded compiler evidence.
The next Init experiment is `func_10005BE0`. The normal Game target remains
`func_15157FE8`.

## Retail Contract

The routine occupies `0x100038E0..0x1000390C`, 44 bytes / eleven words.
Its body in `conker/asm/nonmatchings/init_38E0/func_100038E0.s`:

1. Materializes `0xBC000C02` in `$v0`.
2. Stores that address as a word to `D_80038070`.
3. Stores `0x4040` as a halfword to `D_80038074`.
4. Stores another materialized `0x4040` halfword through `$v0`.
5. Returns with a nop delay slot.

Shared declarations confirm `D_80038070` is `u32` and `D_80038074` is
`u16`. The commented historical prototype is void. A bounded search of
current C sources and generated assembly found no named caller or direct
`jal` word `0C000E38`. This is not proof that indirect callers are absent.
The leftover `$v0` value alone does not establish a return contract.

The specific purpose of the hardware address is not established here.
Do not label it as a particular device without additional evidence.

## Reproducible Candidate

The initial fixture under ignored `conker/build/` contains:

```c
typedef unsigned int u32;
typedef unsigned short u16;
extern u32 D_80038070;
extern u16 D_80038074;

void func_100038E0(void) {
    D_80038070 = 0xBC000C02;
    D_80038074 = 0x4040;
    *(volatile u16 *)0xBC000C02 = 0x4040;
}
```

From `conker/`, the isolated compilation uses the repository's compiler:

```sh
../ido/ido5.3_recomp/cc -c -32 -G 0 -Xfullwarn -Xcpluscomm \
  -signed -nostdinc -non_shared -Wab,-r4300_mul -O2 -g3 \
  -mips2 -o32 -o build/init-mmio-experiment.o build/init-mmio-experiment.c
mips-linux-gnu-objdump -dr -z build/init-mmio-experiment.o
```

The final local fixture has the volatile-publication variant described below;
use the code above to reproduce the initial three profile trials. All object
files are ignored diagnostic artifacts and are not production build inputs.

## Measured Variants

| Candidate | Profile | Meaningful words | Main difference |
| --- | --- | ---: | --- |
| Initial void body | `-O2 -g3` | 11 | Hoists/reuses value `0x4040`, rematerializes the MMIO base |
| Initial void body | `-O1` | 11 | Different temporaries/address use; MMIO store in return delay slot |
| Initial void body | `-O0` | 14 | Extra MMIO base materialization and duplicate return |
| Local address plus explicit address return | `-O2 -g3` | 12 | Extra return move; return contract not established |
| All three stores explicitly volatile | `-O2 -g3` | 13 | Separate address registers and address materialization |

Counts exclude trailing object-alignment nops; disassembly used `-z` so
meaningful nops and the unoptimized duplicate return are not hidden.

The `-O1` body has the closest store ordering and count. Its first store
uses `$t6` instead of `$v0`; the value temporaries shift from `$t6/$t7`
to `$t7/$t8`. It also emits `lui $t9,0xBC00` and stores at `0xC02($t9)`
in the return delay slot instead of reusing the full retained address with
a pre-return store. This is more than the closed register-only change in
the preceding clear-loop conversion. No word-normalization batch was added.
The delay-slot store itself is not a demonstrated semantic error; it simply
does not match retail's instruction sequence.

The explicit-volatile variant casts the addresses of both published globals
to volatile pointers and leaves the hardware dereference volatile as well.
Its emitted stores retain the observed word/halfword/halfword order, but
the resulting thirteen-word body exceeds the original slot. The explicit
return experiment was rejected rather than inventing a signature to encourage
compiler register allocation.

## Baseline Recheck

The tree began clean at `e249ec4`; origin had caught up with the local branch.
A fresh read-only matcher reports total 3,241 / 5,461 exact C rows, Init
492 / 492 exact, Game 2,568 / 4,788 exact, and Debugger 181 / 181 exact.
There are zero address-drift rows and 2,220 different Game C rows.

Structured extraction of the existing linked ELF independently reconfirms
all 164,048 Init code bytes and all 17,376 initialized-data bytes exact,
with the unchanged hashes from Notes 735 and 736. No full build or runtime
test was needed or claimed: only ignored standalone fixtures were compiled.
The sibling host port and frozen Release artifacts remain untouched.

## Resume

1. Keep `func_100038E0` in a deferred matching-experiment queue. Additional
   source shaping is possible, but none of these five trials establishes a
   direct match or original compiler-generated provenance.
2. Inspect `func_10005BE0`'s inclusive bitmap endpoints and final-bit mask.
   Establish its caller/data contracts before extracting it from `init_5AB0`.
3. Require a complete linked-function match and full Init code/data comparison
   before reporting another converted row. Leave aggregate README tables
   unchanged until a production conversion is verified.
