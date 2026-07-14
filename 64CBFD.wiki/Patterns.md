### extra b/nop
```
348:    bne     t8,at,380 ~>                      i 348:    bne     t8,at,378 ~>
34c:    nop                                         34c:    nop
350:    b       358 ~>                            <
354:    nop                                       <
358: ~> li      t9,0x20                             350:    li      t9,0x20
35c:    sh      t9,0x1c(sp)                         354:    sh      t9,0x1c(sp)
360:    lw      t0,0x2c(sp)                         358:    lw      t0,0x2c(sp)
```

This occurs when there is an `if(0) {}` statement with `-g`.

### 'arg0 + 0x10' when arg0 is a struct

```c
func_8001C770(arg0 + 0x10);
```
becomes
```c
func_8001C770(&arg0->unk10);
```

### padded stacks
```c
    u32 pad0;
    u8  pad1;
    u8  sp22;
    s8  sp21;
    s8  sp20;
    s32 sp1C;
    u16 pad2;
    s16 sp18;

    sp18 = 2;
    sp1C = 0;
    sp20 = arg1 | 0xB0;
    sp21 = 0xA;
    sp22 = arg2;
```
becomes (be aware of reversed ordering!)
```c
typedef struct {
    s16 unk0;
    u16 unk2;
    s32 unk4;
    u8  unk8;
    u8  unk9;
    u8  unkA;
    u8  unkB;
    u32 unkC;
} struct33;

// <snip>
void func() {
    struct33 tmp;

    tmp.unk0 = 2;
    tmp.unk4 = 0;
    tmp.unk8 = arg1 | 0xB0;
    tmp.unk9 = 0xA;
    tmp.unkA = arg2;

// <snip>
```


### missing arg0

```c
void func_80009600(? arg1) {
    func_85161334(0xFF, 1);
}
```
becomes
```c
void func_80009600(s32 arg0, s32 arg1) {
    func_85161334(arg0, 0xFF, 1);
}
```


### crazy struct offset

```c
    temp_a0 = ((D_800BE9F0 * 4) + 0x80090000)->unk1C04;
```
becomes
```c
    temp_a0 = D_80091C04[D_800BE9F0]
```

### crazy unrolling
```c
s32 func_85004E00(void) {
    void *temp_v1;
    void *phi_v1;

    *(void *)0x800C6660 = 0;
    *(void *)0x800C6664 = 0;
    *(void *)0x800C6668 = 0;
    *(void *)0x800C666F = (u8)0;
    phi_v1 = (void *)0x800C6670;
loop_1:
    temp_v1 = phi_v1 + 0x40;
    temp_v1->unk-30 = 0;
    temp_v1->unk-2C = 0;
    temp_v1->unk-28 = 0;
    temp_v1->unk-21 = (u8)0;
    temp_v1->unk-20 = 0;
    temp_v1->unk-1C = 0;
    temp_v1->unk-18 = 0;
    temp_v1->unk-11 = (u8)0;
    temp_v1->unk-10 = 0;
    temp_v1->unk-C = 0;
    temp_v1->unk-8 = 0;
    temp_v1->unk-1 = (u8)0;
    temp_v1->unk-40 = 0;
    temp_v1->unk-3C = 0;
    temp_v1->unk-38 = 0;
    temp_v1->unk-31 = (u8)0;
    phi_v1 = temp_v1;
    if (temp_v1 != 0x800C67F0) {
        goto loop_1;
    }
    return 0x800C67F0;
}
```
becomes
```
void func_85004E00(void) {
    u32 i;

    for (i = 0; i < 25; i++)
    {
        D_800C6660[i].unk0 = 0;
        D_800C6660[i].unk4 = 0;
        D_800C6660[i].unk8 = 0;
        D_800C6660[i].unkF = 0;
    }
}
```

### loops are bastards (1)

```c
s32 func_86001B00(void *arg0) {
    s32 temp_v1;
    void *phi_v0;
    s32 phi_v1;
    s32 phi_v1_2;

    phi_v0 = arg0;
    phi_v1 = 0;
    phi_v1_2 = 0;
    if (*arg0 != 0) {
loop_1:
        temp_v1 = phi_v1_2 + 1;
        phi_v0 = phi_v0 + 1;
        phi_v1 = temp_v1;
        phi_v1_2 = temp_v1;
        if (phi_v0->unk1 != 0) {
            goto loop_1;
        }
    }
    return phi_v1;
}
```
becomes
```c
u32 func_86001B00(u8 *arg0) {
    u32 i = 0;
    while (arg0[i]) {
        i++;
    };
    return i;
}
```
### loops are bastards (2)
```c
void *func_86001AD0(void *arg0, void *arg1, s32 arg2) {
    s32 temp_a2;
    void *temp_v0;
    void *phi_v1;
    void *phi_v0;
    s32 phi_a2;

    phi_v1 = arg1;
    phi_v0 = arg0;
    phi_a2 = arg2;
    if (arg2 != 0) {
loop_1:
        temp_a2 = phi_a2 - 1;
        temp_v0 = phi_v0 + 1;
        temp_v0->unk-1 = (u8) *phi_v1;
        phi_v1 = phi_v1 + 1;
        phi_v0 = temp_v0;
        phi_a2 = temp_a2;
        if (temp_a2 != 0) {
            goto loop_1;
        }
    }
    return arg0;
}
```
becomes
```c
u8* func_86001AD0(u8 *arg0, u8 *arg1, u32 arg2) {
    u8 *tmp0 = arg0;
    u8 *tmp1 = arg1;

    while (arg2 > 0)
    {
        *tmp0++ = *tmp1++;
        arg2 -= 1;
    }

    return arg0;
}
```
### loops can look worse than they are
When the condition is checking for an address, often subtracting the start from the end and dividing by the size of the array type gets you to a more sane place:
```c
    phi_v1 = (void *)0x800DF7C8;
loop_1:
    temp_v1 = phi_v1 + 4;
    temp_v1->unk-4 = 0;
    phi_v1 = temp_v1;
    if (temp_v1 != 0x800DF7D0) {
        goto loop_1;
    }
```
becomes
```c
    for (i = 0; i < 2; i++)
    {
        D_800DF7C8[i] = 0;
    }
```

### temp_f6 + 4294967296.0f;

```c
    if ((s32) temp_t8 < 0) {
        phi_f6 = temp_f6 + 4294967296.0f;
    }
```
just remove these statements

### 2D arrays

```c
temp_v0 = (arg8 * 0x348) + (arg7 * 0x54) + 0x803F6720;
```
becomes
```c
struct048 *temp_v0 = &D_803F6720[arg8][arg7];
```
where struct048 is size 0x54 and `D_803F6720` is defined as `extern struct048 D_803F6720[][10]`