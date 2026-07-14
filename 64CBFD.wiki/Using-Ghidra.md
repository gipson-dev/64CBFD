Ghidra gets a lot of flak in N64 Decomp circles; it was not designed to create matching MIPS code (in the way that [mips2c](https://github.com/matt-kempster/mips_to_c) was), but it can still be useful to get an idea of what is going on in a function - especially when loops are involved.

**NOTE:** This page will not cover installing/setting up Ghidra - Google is your friend.

Install the [N64 ROM Loader](https://github.com/zeroKilo/N64LoaderWV) Extension (File -> Install Extension...)

In order to reverse engineer `game` code, you want to load in the extracted code:

```sh
make decompress
cd game/rzip/code
cat 0*.bin > game.decompressed.bin
```

N64 ROMs are loaded in with `MIPS:BE:64:64-32addr:default`, when loading in this file pick the following language: `MIPS | 64-32addr | 32 | big | o32`






