The [decomp-permuster](https://github.com/simonlindholm/decomp-permuter) is normally pulled out when all efforts to manually fix register matching have failed.

**NOTE:**
It does not come with any guarantee that it will be able to generate a closer match.

**Clone into tools**
```sh
cd tools
git clone https://github.com/simonlindholm/decomp-permuter
```

**Import function:**
```sh
cd chunk0
python3 ../tools/decomp-permuter/import.py src/code_75400.c asm/nonmatchings/code_75400/func_15079A58.s
```

**Run permuter:**
```sh
python3 ../tools/decomp-permuter/permuter.py nonmatchings/func_15079A58 --best-only -j3
```