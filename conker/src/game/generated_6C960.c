#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6C960.s. */

s32 func_1505E0C4(s32 arg0, s32 arg1, u8 *arg2, s32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, f32 arg7, f32 arg8, f32 arg9,
                  f32 arg10, s32 arg11);

s32 func_1503F4B0() {
    return 0;
}

s32 func_1503F5B8(u8 *arg0, s32 arg1, s32 arg2, f32 arg3, f32 arg4,
                  s32 arg5) {
    return func_1505E0C4(0, 0, arg0, 0, arg1, arg2, arg0[0x3F5], arg3,
                         arg4, 0.0f, 0.0f, arg5);
}

void *allocate_memory(s32, s32, s32, s32);
s32 func_1502FE10(s32, u8 **, u8 *, u8 **, u8 **, u8 **, u32 *);
void func_10004074(void *);
s32 func_1503F5B8(u8 *, s32, s32, f32, f32, s32);

s32 func_1503F62C(s32 kind, s32 selector, u8 **records, u8 *count,
        u8 **source, u8 **transform, u8 **attached) {
    u32 recordCount;
    u8 *node;

    *attached = allocate_memory(0x3F8, 1, 2, 2);
    if (*attached == 0) {
        return 1;
    }
    bzero(*attached, 0x40);
    (*attached)[0x215] = 1;
    (*attached)[0x45] = 1;
    /* Retail ignores this status, including an unwritten recordCount on failure. */
    func_1502FE10(kind, records, count, source, transform,
        (u8 **)(*attached + 0x3F0), &recordCount);
    (*attached)[0x3F4] = recordCount;
    (*attached)[0x3F5] = selector;
    (*attached)[0x3F6] = 0;
    *(u8 **)(*attached + 0x3E8) = allocate_memory(recordCount << 6, 1, 2, 2);
    *(u8 **)(*attached + 0x3EC) = allocate_memory(recordCount << 6, 1, 2, 2);
    kind = (s32)*attached;
    node = (u8 *)kind;
    /* These inverted NULL-free gates are part of the original routine. */
    if (*(u8 **)(node + 0x3E8) == 0 || *(u8 **)(node + 0x3EC) == 0) {
        if (*(u8 **)(node + 0x3E8) == 0) {
            func_10004074(*(u8 **)(node + 0x3E8));
            kind = (s32)*attached;
            node = (u8 *)kind;
        }
        if (*(u8 **)(node + 0x3EC) == 0) {
            func_10004074(*(u8 **)(node + 0x3EC));
            kind = (s32)*attached;
            node = (u8 *)kind;
        }
        func_10004074(node);
        return 1;
    }
    func_1503F5B8(node, 1, 0, 1.0f, 0.0f, 0);
    return 0;
}

void func_1503F7B8(u8 *arg0) {
    func_100043B4(*(s32 *) (arg0 + 0x3E8), 4);
    func_100043B4(*(s32 *) (arg0 + 0x3EC), 4);
    func_10004074(arg0);
}
