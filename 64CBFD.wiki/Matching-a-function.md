This page will contain some common differences and how to get functions to match.

**`lbu` vs `lw` or `sh` vs `sw`**
- change type from s32 to u8 (etc)

**`lw` vs `addiu`**

- `&VARIABLE` / `VARIABLE`; dereference the variable

**`andi 0xff` or `andi 0xffff`**

- `&& 0xff`; and with `0xff`
- `(u8)`; cast to `u8`

