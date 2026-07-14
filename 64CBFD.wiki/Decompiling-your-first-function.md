# Introduction

**NOTE:** 
The following assumes you've already run through the [Quickstart](https://github.com/mkst/conker/wiki/Quickstart) and are able to get `build/chunk0.bin: OK` when compiling `chunk0`. 

We are working with `chunk0` as this is the game logic and is the most accessible place to begin.

# Overview

The general steps are as follows, and these will make up headings for the rest of this section

1. Identify a **file** you wish to work on
2. Identify a **function** within the file to start with (either the first one, or the smallest is a good place to begin)
3. Update `n64splat` configuration and re-extract if required (if the file does not exist in `src/`)
4. Run `mips2c` locally (or [online](https://simonsoftware.se/other/mips_to_c.py)) to generate some `c` code
5. Replace the `GLOBAL_ASM("asm/nonmatching/code_123/func_1234")` with the `c` code
6. Run `asm-differ` to check for differences
7. Modify C code until it matches
8. Update `unknown_syms.txt` with any new variable offsets
9. Run `make` and ensure you get `build/chunk0.bin: OK`

## Identify a file you wish to work on

There are two scenarios:
- You are working on a function in existing C file
- You are working on a function in a file that does not have a C file associated with it

For this example, let's assume we want to work on a file that is yet to be migrated to C  - `asm/code_40D90.s`

## Identify a function within the file to start with

There are three scenarios:
- You are looking at a function in assembly (.s)
- You are looking at a `#pragma GLOBAL_ASM(...` line
- You are looking at a partially-decompiled function

For this example, we are looking at `asm/code_40D90.s`, and we will work with the first function `func_15040D90` which looks like this:

```
glabel func_15040D90
/* 40D90 15040D90 AFA40000 */  sw         $a0, ($sp)
/* 40D94 15040D94 03E00008 */  jr         $ra
/* 40D98 15040D98 00000000 */   nop       
```

**NOTE:** This is almost the simplest function you'll encounter - most function's aren't going to be this easy!

## Update n64splat configuration and re-extract if required

If your function is defined in an existing C file, there's no splat configuration to change and you can skip the next section.

If there is no C file, then you will need to update the splat configuration and re-run the split command.

### Updating n64splat configuration and extracting again

We've decided that we wish to work on `func_15040D90` within `asm/code_40D90.s`.Let's assume a snippet of our `chunk0.us.yaml` looks like 

```yaml
    - [0x40350, "c"]
    - [0x40D90, "asm"] # our function is in this section of the ROM
    - [0x412C0, "asm"]
    - [0x42D50, "c"]
```

We know that there is no C file associated with this function for two reasons:

1. The function was found within `asm/code_40D90.s` (rather than `nonmatching/code_40D90/func_15040D90.s`)
2. The yaml configuration for the parent file, `0x40D90`, has its type set to `"asm"` rather than `"c"`

We need to modify the configuration - simply changing `"asm"` to `"c"`:

```yaml
    - [0x40350, "c"]
    - [0x40D90, "c"] # we changed this line
    - [0x412C0, "asm"]
    - [0x42D50, "c"]
```

Then when we run `make extract` again, it will tell us that it has created a C file for us:

```sh
$ make extract
game.us.bin: OK
python3 ../tools/n64splat/split.py game.us.bin chunk0.us.yaml .
Wrote code_40D90 to ./src/code_40D90.c
....
Split 2 MB (100.00%) in defined segments
                code:     2 MB (100.00%) 2 split, 0 cached
             unknown:      0 B (0.00%) from unknown bin files
```

If we take a look at that file, we can see that it has a number of `GLOBAL_ASM` lines; these are used to include the raw assembly file within the C file.

```c
#include <ultra64.h>
#include "functions.h"
#include "variables.h"


#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040D90.s")

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040D9C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040FCC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_1504129C.s")
```

**NOTE:**
All functions in the original assembly file `asm/code_40D90.s` are now split out into `asm/nonmatchings/code_40D90/`!

We should run `make` here to confirm that we can still build a matching ROM

```sh
$ make
<snip..>

build/chunk0.bin: OK
```

Now that we have confirmed the code matches, we need to take a copy of the build directory to be used as a 'golden source' to compare against as we try to decompile:

```sh
mkdir -p expected
cp -r build expected/
```

We are now ready to start decompiling the function.

## Run mips2c on the assembly file

For simplicity, we will use mips2c [online](https://simonsoftware.se/other/mips_to_c.py). Paste the function into the `MIPS assembly:` section, and click `Decompile`. You should get the following output on screen:

```c
void func_15040D90(s32 arg0) {

}
```

## Replace the GLOBAL_ASM with C code

This is as easy as replacing the `GLOBAL_ASM` line with the code (tip: comment out the `#pragma` in case you cannot get things to match!):

```c
#include <ultra64.h>
#include "functions.h"
#include "variables.h"


// #pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040D90.s")
void func_15040D90(s32 arg0) {

}

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040D9C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_15040FCC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/code_40D90/func_1504129C.s")
```

## Run asm-differ to check for differences

The `asm-differ` tool can take a few different arguments, we will be using `-mwo3` which basically means "watch for changes and automatically recompile, only work on the affected function rather than whole project, and show the previous diff".

in order to run `asm-differ` against `func_15040D90` we run:

```sh
python3 ../tools/asm-differ/diff.py -mwo3 func_15040D90
```

If it complains `Please ensure an OK .o file exists at "expected/build/src/code_40D90.o".` be sure you copied `build` into `expected/`. 

You should be greeted with the following (left is original, right is your code):

```
TARGET                                              CURRENT                                           PREVIOUS
0:    sw      a0,0(sp)                              0:    sw      a0,0(sp)
4:    jr      ra                                    4:    jr      ra
8:    nop                                           8:    nop
c:    addiu   sp,sp,-8                              c:    addiu   sp,sp,-8
10:    lui     t1,0x800c                            10:    lui     t1,0x800c
14:    lui     t2,0x8003                            14:    lui     t2,0x8003
18:    addiu   t2,t2,-0x5518                        18:    addiu   t2,t2,-0x5518
1c:    addiu   t1,t1,-0x1640                        1c:    addiu   t1,t1,-0x1640
20:    sw      s0,4(sp)                             20:    sw      s0,4(sp)
```

There are no differences! 

## Modify C code until it matches

Here we will pick a slightly more complicated function, `func_150792FC`.

Start by feeding this assembly into mips2c online.

```
glabel func_150792FC
/* 792FC 150792FC 3C03800D */  lui        $v1, 0x800d
/* 79300 15079300 2463154C */  addiu      $v1, $v1, 0x154c
/* 79304 15079304 8C620000 */  lw         $v0, ($v1)
/* 79308 15079308 3C19800D */  lui        $t9, 0x800d
/* 7930C 1507930C 944E02F8 */  lhu        $t6, 0x2f8($v0)
/* 79310 15079310 31CFFFF8 */  andi       $t7, $t6, 0xfff8
/* 79314 15079314 A44F02F8 */  sh         $t7, 0x2f8($v0)
/* 79318 15079318 8C620000 */  lw         $v0, ($v1)
/* 7931C 1507931C 93391890 */  lbu        $t9, 0x1890($t9)
/* 79320 15079320 945802F8 */  lhu        $t8, 0x2f8($v0)
/* 79324 15079324 03194025 */  or         $t0, $t8, $t9
/* 79328 15079328 A44802F8 */  sh         $t0, 0x2f8($v0)
/* 7932C 1507932C 03E00008 */  jr         $ra
/* 79330 15079330 00000000 */   nop       
```

We get the following output:

```c
void *func_150792FC(void) {
    void *temp_v0;
    void *temp_v0_2;

    temp_v0_2 = *(void *)0x800D154C;
    temp_v0_2->unk2F8 = (u16) (temp_v0_2->unk2F8 & 0xFFF8);
    temp_v0 = *(void *)0x800D154C;
    temp_v0->unk2F8 = (u16) (temp_v0->unk2F8 | *(void *)0x800D1890);
    return temp_v0;
}
```

We need to fix up syntax, first replace these with variable names (current format is `D_` + address - until we know what the variable is for, and can start naming them). Therefore:

- `*(void *)0x800D154C` -> `D_800D154C`

```c
void *func_150792FC(void) {
    void *temp_v0;
    void *temp_v0_2;

    temp_v0_2 = D_800D154C;
    temp_v0_2->unk2F8 = (u16) (temp_v0_2->unk2F8 & 0xFFF8);
    temp_v0 = D_800D154C;
    temp_v0->unk2F8 = (u16) (temp_v0->unk2F8 | D_800D1890);
    return temp_v0;
}
```

This still won't compile, because we are trying to index into a `void` variable. We need to replace the `void` with the correct struct.

`D_800D154C` is already defined (you can find it in `include/variables.h`) and is a pointer to `struct127`.

- replace `void` with `struct127` 

Now we can save the following and see how close it is to matching:

```c
void *func_150792FC(void) {
    struct127 *temp_v0;
    struct127 *temp_v0_2;

    temp_v0_2 = D_800D154C;
    temp_v0_2->unk2F8 = (u16) (temp_v0_2->unk2F8 & 0xFFF8);
    temp_v0 = D_800D154C;
    temp_v0->unk2F8 = (u16) (temp_v0->unk2F8 | D_800D1890);
    return temp_v0;
}
```

`asm-differ` output looks like this (easier to see in the console with colours):

```
TARGET                                              CURRENT                                           PREVIOUS
3ee0:    lui     t6,0x800d                        i 3ee0:    lui     t6,%hi(D_800D1890)
3ee4:    lui     t7,0x800d                        i 3ee4:    lui     t7,%hi(D_800D154C)
3ee8:    lw      t7,0x154c(t7)                    i 3ee8:    lw      t7,%lo(D_800D154C)(t7)
3eec:    lbu     t6,0x1890(t6)                    i 3eec:    lbu     t6,%lo(D_800D1890)(t6)
3ef0:    sb      t6,0x232(t7)                       3ef0:    sb      t6,0x232(t7)
3ef4:    jr      ra                                 3ef4:    jr      ra
3ef8:    nop                                        3ef8:    nop
3efc:    lui     v1,0x800d                        r 3efc:    lui     a1,%hi(D_800D154C)               3efc:    lui     v1,0x800d
3f00:    addiu   v1,v1,0x154c                     r 3f00:    addiu   a1,a1,%lo(D_800D154C)            3f00:    addiu   v1,v1,0x154c
3f04:    lw      v0,0(v1)                         r 3f04:    lw      v1,0(a1)                         3f04:    lw      v0,0(v1)
3f08:    lui     t9,0x800d                        r 3f08:    lui     t0,%hi(D_800D1890)               3f08:    lui     t9,0x800d
3f0c:    lhu     t6,0x2f8(v0)                     | 3f0c:    lw      t7,0x2f8(v1)                     3f0c:    lhu     t6,0x2f8(v0)
3f10:    andi    t7,t6,0xfff8                     r 3f10:    andi    t8,t7,0xfff8                     3f10:    andi    t7,t6,0xfff8
3f14:    sh      t7,0x2f8(v0)                     | 3f14:    sw      t8,0x2f8(v1)                     3f14:    sh      t7,0x2f8(v0)
3f18:    lw      v0,0(v1)                         r 3f18:    lw      v0,0(a1)                         3f18:    lw      v0,0(v1)
3f1c:    lbu     t9,0x1890(t9)                    r 3f1c:    lbu     t0,%lo(D_800D1890)(t0)           3f1c:    lbu     t9,0x1890(t9)
3f20:    lhu     t8,0x2f8(v0)                     | 3f20:    lw      t9,0x2f8(v0)                     3f20:    lhu     t8,0x2f8(v0)
3f24:    or      t0,t8,t9                         r 3f24:    or      t1,t9,t0                         3f24:    or      t0,t8,t9
                                                  > 3f28:    andi    t2,t1,0xffff                   -
3f28:    sh      t0,0x2f8(v0)                     | 3f2c:    sw      t2,0x2f8(v0)                     3f28:    sh      t0,0x2f8(v0)
3f2c:    jr      ra                                 3f30:    jr      ra
3f30:    nop                                        3f34:    nop
```

First thing to do is to remove the `return`. Generally (always?) returns involve a `mv` to `v0`, we do not have this here, so it's worth seeing whether that brings us closer (be sure to correct the return type in the signature):

```c
void func_150792FC(void) {
    struct127 *temp_v0;
    struct127 *temp_v0_2;

    temp_v0_2 = D_800D154C;
    temp_v0_2->unk2F8 = (u16) (temp_v0_2->unk2F8 & 0xFFF8);
    temp_v0 = D_800D154C;
    temp_v0->unk2F8 = (u16) (temp_v0->unk2F8 | D_800D1890);
}
```

Check the diff:

```
TARGET                                              CURRENT                                           PREVIOUS
3ee0:    lui     t6,0x800d                        i 3ee0:    lui     t6,%hi(D_800D1890)
3ee4:    lui     t7,0x800d                        i 3ee4:    lui     t7,%hi(D_800D154C)
3ee8:    lw      t7,0x154c(t7)                    i 3ee8:    lw      t7,%lo(D_800D154C)(t7)
3eec:    lbu     t6,0x1890(t6)                    i 3eec:    lbu     t6,%lo(D_800D1890)(t6)
3ef0:    sb      t6,0x232(t7)                       3ef0:    sb      t6,0x232(t7)
3ef4:    jr      ra                                 3ef4:    jr      ra
3ef8:    nop                                        3ef8:    nop
3efc:    lui     v1,0x800d                        r 3efc:    lui     a0,%hi(D_800D154C)             r 3efc:    lui     a1,%hi(D_800D154C)
3f00:    addiu   v1,v1,0x154c                     r 3f00:    addiu   a0,a0,%lo(D_800D154C)          r 3f00:    addiu   a1,a1,%lo(D_800D154C)
3f04:    lw      v0,0(v1)                         r 3f04:    lw      v0,0(a0)                       r 3f04:    lw      v1,0(a1)
3f08:    lui     t9,0x800d                        r 3f08:    lui     t0,%hi(D_800D1890)
3f0c:    lhu     t6,0x2f8(v0)                     | 3f0c:    lw      t7,0x2f8(v0)                   | 3f0c:    lw      t7,0x2f8(v1)
3f10:    andi    t7,t6,0xfff8                     r 3f10:    andi    t8,t7,0xfff8
3f14:    sh      t7,0x2f8(v0)                     | 3f14:    sw      t8,0x2f8(v0)                   | 3f14:    sw      t8,0x2f8(v1)
3f18:    lw      v0,0(v1)                         r 3f18:    lw      v1,0(a0)                       r 3f18:    lw      v0,0(a1)
3f1c:    lbu     t9,0x1890(t9)                    r 3f1c:    lbu     t0,%lo(D_800D1890)(t0)
3f20:    lhu     t8,0x2f8(v0)                     | 3f20:    lw      t9,0x2f8(v1)                   | 3f20:    lw      t9,0x2f8(v0)
3f24:    or      t0,t8,t9                         r 3f24:    or      t1,t9,t0
                                                  > 3f28:    andi    t2,t1,0xffff
3f28:    sh      t0,0x2f8(v0)                     | 3f2c:    sw      t2,0x2f8(v1)                   | 3f2c:    sw      t2,0x2f8(v0)
3f2c:    jr      ra                                 3f30:    jr      ra
3f30:    nop                                        3f34:    nop
```

A large part of the matching process is adding or removing temporary variables. In this case, we can try removing the temporary variables, and reference the global `D_800D154C` directly (be sure to remove the temporary variable definitions too):

```c
void func_150792FC(void) {
    D_800D154C->unk2F8 = (u16) (D_800D154C->unk2F8 & 0xFFF8);
    D_800D154C->unk2F8 = (u16) (D_800D154C->unk2F8 | D_800D1890);
}
```

Check diff:

```
TARGET                                              CURRENT                                           PREVIOUS
3ee0:    lui     t6,0x800d                        i 3ee0:    lui     t6,%hi(D_800D1890)
3ee4:    lui     t7,0x800d                        i 3ee4:    lui     t7,%hi(D_800D154C)
3ee8:    lw      t7,0x154c(t7)                    i 3ee8:    lw      t7,%lo(D_800D154C)(t7)
3eec:    lbu     t6,0x1890(t6)                    i 3eec:    lbu     t6,%lo(D_800D1890)(t6)
3ef0:    sb      t6,0x232(t7)                       3ef0:    sb      t6,0x232(t7)
3ef4:    jr      ra                                 3ef4:    jr      ra
3ef8:    nop                                        3ef8:    nop
3efc:    lui     v1,0x800d                        i 3efc:    lui     v1,%hi(D_800D154C)             r 3efc:    lui     a0,%hi(D_800D154C)
3f00:    addiu   v1,v1,0x154c                     i 3f00:    addiu   v1,v1,%lo(D_800D154C)          r 3f00:    addiu   a0,a0,%lo(D_800D154C)
3f04:    lw      v0,0(v1)                           3f04:    lw      v0,0(v1)                       r 3f04:    lw      v0,0(a0)
3f08:    lui     t9,0x800d                        r 3f08:    lui     t0,%hi(D_800D1890)
3f0c:    lhu     t6,0x2f8(v0)                     | 3f0c:    lw      t7,0x2f8(v0)
3f10:    andi    t7,t6,0xfff8                     r 3f10:    andi    t8,t7,0xfff8
3f14:    sh      t7,0x2f8(v0)                     | 3f14:    sw      t8,0x2f8(v0)
3f18:    lw      v0,0(v1)                           3f18:    lw      v0,0(v1)                       r 3f18:    lw      v1,0(a0)
3f1c:    lbu     t9,0x1890(t9)                    r 3f1c:    lbu     t0,%lo(D_800D1890)(t0)
3f20:    lhu     t8,0x2f8(v0)                     | 3f20:    lw      t9,0x2f8(v0)                   | 3f20:    lw      t9,0x2f8(v1)
3f24:    or      t0,t8,t9                         r 3f24:    or      t1,t9,t0
                                                  > 3f28:    andi    t2,t1,0xffff
3f28:    sh      t0,0x2f8(v0)                     | 3f2c:    sw      t2,0x2f8(v0)                   | 3f2c:    sw      t2,0x2f8(v1)
3f2c:    jr      ra                                 3f30:    jr      ra
3f30:    nop                                        3f34:    nop
```

Casts, e.g. `(u16)` can have a large effect on the compiler output (they can also have no effect, depending on what is being cast from what to what!).

In this case we can try removing the u16 (unsigned 16-bit, aka unsigned short) casting.

```c
void func_150792FC(void) {
    D_800D154C->unk2F8 = D_800D154C->unk2F8 & 0xFFF8;
    D_800D154C->unk2F8 = D_800D154C->unk2F8 | D_800D1890;
}
```

Check the diff, it improved things but we're still not there:

```
TARGET                                              CURRENT                                           PREVIOUS
3ee0:    lui     t6,0x800d                        i 3ee0:    lui     t6,%hi(D_800D1890)
3ee4:    lui     t7,0x800d                        i 3ee4:    lui     t7,%hi(D_800D154C)
3ee8:    lw      t7,0x154c(t7)                    i 3ee8:    lw      t7,%lo(D_800D154C)(t7)
3eec:    lbu     t6,0x1890(t6)                    i 3eec:    lbu     t6,%lo(D_800D1890)(t6)
3ef0:    sb      t6,0x232(t7)                       3ef0:    sb      t6,0x232(t7)
3ef4:    jr      ra                                 3ef4:    jr      ra
3ef8:    nop                                        3ef8:    nop
3efc:    lui     v1,0x800d                        i 3efc:    lui     v1,%hi(D_800D154C)
3f00:    addiu   v1,v1,0x154c                     i 3f00:    addiu   v1,v1,%lo(D_800D154C)
3f04:    lw      v0,0(v1)                           3f04:    lw      v0,0(v1)
3f08:    lui     t9,0x800d                        i 3f08:    lui     t9,%hi(D_800D1890)             r 3f08:    lui     t0,%hi(D_800D1890)
3f0c:    lhu     t6,0x2f8(v0)                     | 3f0c:    lw      t6,0x2f8(v0)                   | 3f0c:    lw      t7,0x2f8(v0)
3f10:    andi    t7,t6,0xfff8                       3f10:    andi    t7,t6,0xfff8                   r 3f10:    andi    t8,t7,0xfff8
3f14:    sh      t7,0x2f8(v0)                     | 3f14:    sw      t7,0x2f8(v0)                   | 3f14:    sw      t8,0x2f8(v0)
3f18:    lw      v0,0(v1)                           3f18:    lw      v0,0(v1)
3f1c:    lbu     t9,0x1890(t9)                    i 3f1c:    lbu     t9,%lo(D_800D1890)(t9)         r 3f1c:    lbu     t0,%lo(D_800D1890)(t0)
3f20:    lhu     t8,0x2f8(v0)                     | 3f20:    lw      t8,0x2f8(v0)                   | 3f20:    lw      t9,0x2f8(v0)
3f24:    or      t0,t8,t9                           3f24:    or      t0,t8,t9                       r 3f24:    or      t1,t9,t0
                                                                                                    > 3f28:    andi    t2,t1,0xffff
3f28:    sh      t0,0x2f8(v0)                     | 3f28:    sw      t0,0x2f8(v0)                   | 3f2c:    sw      t2,0x2f8(v0)
3f2c:    jr      ra                                 3f2c:    jr      ra
3f30:    nop                                        3f30:    nop
```

The `lhu` on the left is "load unsigned short", our code is doing `lw` (load word). The struct definition has `unk2F8` as a `s32`, but it appears it should be `u16`. So we can edit the definition in `include/structs.h`, save, and check the diff.

`asm-differ` output shows a match!

```
TARGET                                              CURRENT                                           PREVIOUS
3ee0:    lui     t6,0x800d                        i 3ee0:    lui     t6,%hi(D_800D1890)
3ee4:    lui     t7,0x800d                        i 3ee4:    lui     t7,%hi(D_800D154C)
3ee8:    lw      t7,0x154c(t7)                    i 3ee8:    lw      t7,%lo(D_800D154C)(t7)
3eec:    lbu     t6,0x1890(t6)                    i 3eec:    lbu     t6,%lo(D_800D1890)(t6)
3ef0:    sb      t6,0x232(t7)                       3ef0:    sb      t6,0x232(t7)
3ef4:    jr      ra                                 3ef4:    jr      ra
3ef8:    nop                                        3ef8:    nop
3efc:    lui     v1,0x800d                        i 3efc:    lui     v1,%hi(D_800D154C)
3f00:    addiu   v1,v1,0x154c                     i 3f00:    addiu   v1,v1,%lo(D_800D154C)
3f04:    lw      v0,0(v1)                           3f04:    lw      v0,0(v1)
3f08:    lui     t9,0x800d                        i 3f08:    lui     t9,%hi(D_800D1890)
3f0c:    lhu     t6,0x2f8(v0)                       3f0c:    lhu     t6,0x2f8(v0)                   | 3f0c:    lh      t6,0x2f8(v0)
3f10:    andi    t7,t6,0xfff8                       3f10:    andi    t7,t6,0xfff8
3f14:    sh      t7,0x2f8(v0)                       3f14:    sh      t7,0x2f8(v0)
3f18:    lw      v0,0(v1)                           3f18:    lw      v0,0(v1)
3f1c:    lbu     t9,0x1890(t9)                    i 3f1c:    lbu     t9,%lo(D_800D1890)(t9)
3f20:    lhu     t8,0x2f8(v0)                       3f20:    lhu     t8,0x2f8(v0)                   | 3f20:    lh      t8,0x2f8(v0)
3f24:    or      t0,t8,t9                           3f24:    or      t0,t8,t9
3f28:    sh      t0,0x2f8(v0)                       3f28:    sh      t0,0x2f8(v0)
3f2c:    jr      ra                                 3f2c:    jr      ra
3f30:    nop                                        3f30:    nop
```

We can tidy up the function a little and still have it match:

```
void func_150792FC(void) {
    D_800D154C->unk2F8 &= 0xFFF8;
    D_800D154C->unk2F8 |= D_800D1890;
}
```

Job done.

## Update unknown_syms.txt

When new variables are encountered, they are `extern`'d (which means they are declared but not defined). When the location is understood, we can add the definition to the correct file. In the meantime they are simply added to `include/variables.h`.

Because these variables are only declared, they need an entry in `unknown_syms.txt` with the address, e.g.

```c
D_8002ABE0 = 0x8002ABE0;
```

## Run make to get the OK

If you believe you have gotten everything matching in your C file, run `make` to ensure you didn't break anything else via your changes. you should get an `OK`:

```sh
$ make
build/chunk0.bin: OK
```

And you can move on to the next function (and/or raise a PR to commit your changes to the repo!)


# Appendix

## Using context file

`mips2c` supports a 'context' file which is used to aid with naming of struct elements and other helpful things. As we move to naming structs (e.g. "unk120" becomes "is_on_fire"), we will want to use context files to fill this names in for us as part of the assembly->c translation.

Steps are pretty straightforward:

Generate `ctx.c`
```sh
python3 tools/ctx.py src/game_131F30.c
```

Run mips2c using context file:

```sh
python3 ../tools/mips_to_c/mips_to_c.py --context ctx.c asm/nonmatchings/game_131F30/func_15104FF8.s
```