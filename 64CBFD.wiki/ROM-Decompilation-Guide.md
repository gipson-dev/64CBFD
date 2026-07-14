# Introduction

> Please note that this is a (very) work-in-progress document; it is incomplete - feel free to help me improve it!

An N64 ROM is a chunk of data containing everything that makes up the particular game. 

There are two high-level categories, **code** and **assets**:

 - **code**; logic that is executed by the various N64 processors ('os' code (libultra), μcode as well as game logic)
 - **assets**; everything else that makes up the game:
   - models
   - levels
   - textures
   - display lists
   - music
   - sound effects
   - cutscenes
   - more!

As part of the decompilation process, the various sections of the ROM that contain these different formats needs to be identified and likely handled differently.

Decompilation projects may have different goals, from trying to understand a little more about the ROM, to having the complete source code, assets and all.

## Code

The "code" section is made up of MIPS machine code - i.e. the result of taking source code (asm, c or c++) and compiling it for the N64's CPU. The process for decompiling (reversing) this machine code usually has two steps:

1. Converting the machine code into more human-readable assembly language
2. Taking this assembly and writing C code that, when compiled, matches the assembly 1:1.

Converting the machine code into assembly is straightforward using tools like [(n64)splat](https://github.com/ethteck/splat), you simply tell it the start and end of each code section and it does the rest.

Re-writing the assembly in (matching) C is a **significantly** more difficult and time-consuming process.

At a high level the following need to be determined in order to get code that matches (even if the C is perfect!):

1. Compiler used (IDO? gcc? other?)
2. Version of compiler user (IDO 5.3? 7.1? etc)
3. Compiler optimisations used (`-O2`? `-O3`? `-g`? `-O2 -g3`?); can differ on a per-file basis
4. Compiler flags used (mips version 1, 2 or 3? loop unrolling?)

### Variables

The code section of the ROM includes two types of variable data:

- [bss](https://en.wikipedia.org/wiki/.bss); variables used during the running of the game that are *not* constants; they take up no space in the ROM.
- (ro)[data](https://en.wikipedia.org/wiki/Data_segment); constant variables, i.e. setting a variable `const f32 PI = 3.14159265;` will create a 4 byte section hardcoded with the value `0x40490FDB`.

As you start to decompile functions you will start to build a list of `unknown_syms` and all variables will simply be `extern`'d; as the project matures you will be determine where variables are assigned - this is known as 'placing' the variables.

## Assets

There are many different formats used in N64 games. Some of them are well documented (e.g. Super Mario 64), some of them are not.

### Compression

There are a number of compression types used to reduce the overall ROM size (a smaller cartridge is cheaper to make == more profit), and there are open sourced libraries available to both compress and decompress them.

 - [LZ77](https://en.wikipedia.org/wiki/LZ77_and_LZ78) variants
 - [DEFLATE](https://en.wikipedia.org/wiki/DEFLATE) variants
 - [RNC ProPack](https://wiki.multimedia.cx/index.php/RNC_ProPack)

### Textures

The following is a non-exhaustive list of texture formats:
 - RGB(A) variants:
   - RGBA32 - 8 bits for Red, Green, Blue and Alpha; 4 bytes total
   - RGBA16 - 5 bits for Red, Green and Blue, 1 bit for Alpha; 2 bytes total
   - RGB656 -
   - RGB5A3 -
 - CI*; palette based
 - I(A)*; intensity

### Models

### Levels

### Music

M64/Midi

### Sound Effects


# Tooling

This section describes the tooling used within the Conker project.

## (n64)splat

At a high level, splat splits up an input file into smaller segments based on a configuration file you feed to it. Out of the box a decent number of types are supported, and splat is extensible so you can define new types with custom behaviours to meet your needs.

### Sample n64splat configuration file

```yaml
options:
  basename: conker
  target_path: baserom.us.z64
  compiler: IDO
  cpp_args:
  - "-Iinclude"
  - "-Iinclude/2.0L"
  - "-D_LANGUAGE_C"
segments:
  - name:  header
    type:  header
    start: 0x00000000
  - name:  boot
    type:  bin
    start: 0x00000040
  - type:  code
    start: 0x00001000
    vram:  0x80001000
    subsegments:
    - [0x1000, "asm"]
  - [0x20000, "bin"] ### just try to analyse a small chunk to begin with - until you determine where the code ends
  - [0x04000000]
```

## mips to c

The brains behind the scenes. Takes a file in assembly and translates it into C. Depending on the function and compiler options used, the accuracy of the output can differ significantly.

```sh
python3 tools/mips_to_c/mips_to_c.py asm/1234.s
```

## asm-differ

[asm-differ](https://github.com/simonlindholm/asm-differ) is a very useful tool that compares the assembly output of your function to the original. Using `-mwo` flags allows passing a function name and for the file to be automagically recompiled when you save it.

```sh
python3 tools/asm-differ/diff.py -mwo func_00001234
```

You will need to take a copy of your `build` directory from an `OK!` compile, and copy it into a directory named `expected`, e.g.
```sh
mkdir -p expected
cp -r build expected/
```

You will also need to create a file named `diff_settings.py` in the base of your repository, it should look something like this:
```py
import os

def apply(config, args):
    basename = 'conker' # change this to match your basename
    version = 'us'      # remove references to "{version}." if you are not working on different versions

    config['baseimg'] = f'baserom.{version}.z64'
    config['myimg'] = f'build/{basename}.{version}.z64'
    config['mapfile'] = f'build/{basename}.{version}.map'
    config['source_directories'] = ['src', 'include']
```

## asm-processor

As your project progresses you will want find that you are able to generate matching decompilation for certain functions within a given file, but not all (yet!). [asm-processor](https://github.com/simonlindholm/asm-processor) allows you to include assembly files one-by-one, so you can work on each function individually until you have successfully decompiled the entire file.


# Notes from Conker Decompilation

This section is very bare and basic, I made a few notes, they are pasted verbatim below. I will update this page to flesh it out.

## Initialisation of git repo
```
mkdir ~/conker
cd ~/conker
git init
```

## Using splat

Download:
```sh
mkdir tools && cd tools
git submodule add https://github.com/ethteck/n64splat tools/n64splat
```
Create dummy Makefile
```
cp tools/n64splat/makefile_template.txt Makefile
```
Install pre-requisites (note: needs Python 3.7+)

```sh
sudo apt-get install python3-pip
pip3 install capstone pycparser # see Dockerfile for
```
Create example config
```
python3 tools/n64splat/create_config.py baserom.us.z64
```

Edit the file, add option:

```yaml
options:
  - find_file_boundaries: yes
```

## get vram offset

```sh
$ python3 tools/n64splat/util/rominfo.py conker.us.z64
Image name: CONKER BFD
Country code: E - North America
Libultra version: G
CRC1: 30C7AC50
CRC2: 7704072D
CIC: 6105 / 7105
RAM entry point: 0x80001000
```

python3 tools/n64splat/split.py baserom.us.z64 configs/conker.us.yaml .

## Tools

Take the following from an existing project; recomp builds are recommended over the original IDO versions:

- IDO 5.3 Compiler
- IDO 7.1 Compiler

## Makefile

Add `-I include` to `AS_FLAGS` and take `include/macros.inc` from sm64 decomp copy in as `macro.inc`

## First function

Pick a small asm, paste into [https://simonsoftware.se/other/mips_to_c.py](mips_to_c).

Add file as `src/func_name.c` and edit configuration, e.g.

```yaml
- [0x15550, "asm"]
- [0x17870, "asm"]
- [0x17AA0, "c", "code_17AA0"] # new function being added
- [0x17AF0, "asm"]
- [0x17DF0, "asm"]
```

Re-run

```
python3 tools/n64splat/split.py baserom.us.z64 configs/conker.us.yaml .
```

Compile:

```
make
```

It will that the file does not match:

```
build/conker.us.z64: FAILED
sha1sum: WARNING: 1 computed checksum did NOT match
make: *** [Makefile:87: verify] Error 1
```

Use the diff tool to highlight differences:

```
python3 tools/asm-differ/diff.py 0x17AA0

17aa0:    addiu   sp,sp,-0x28                     i 17aa0:    addiu   sp,sp,-0x20
17aa4:    sw      ra,0x14(sp)                       17aa4:    sw      ra,0x14(sp)
17aa8:    sw      a0,0x28(sp)                     s 17aa8:    sw      a0,0x20(sp)
17aac:    li      t6,0xf                            17aac:    li      t6,0xf
17ab0:    sh      t6,0x18(sp)                     s 17ab0:    sh      t6,0x1e(sp)
17ab4:    lw      a0,0x28(sp)                     s 17ab4:    lw      a0,0x20(sp)
17ab8:    addiu   a1,sp,0x18                      i 17ab8:    addiu   a1,sp,0x1e
17abc:    move    a2,zero                           17abc:    move    a2,zero
17ac0:    li      a3,2                              17ac0:    li      a3,2
17ac4:    jal     0x1c224                           17ac4:    jal     0x1c224
17ac8:    addiu   a0,a0,0x48                        17ac8:    addiu   a0,a0,0x48
17acc:    b       0x17ad4 ~>                        17acc:    b       0x17ad4 ~>
17ad0:    nop                                       17ad0:    nop
17ad4:    lw      ra,0x14(sp)                       17ad4:    lw      ra,0x14(sp)
17ad8:    addiu   sp,sp,0x28                      i 17ad8:    addiu   sp,sp,0x20
17adc:    jr      ra                                17adc:    jr      ra
17ae0:    nop                                       17ae0:    nop
17ae4:    nop                                       17ae4:    nop
```

So solve we need to add padding to the stack. This is trial-and-error. Eventually running make will give:

```
build/conker.us.z64: OK
```

## Finding other code sections

## Finding MP3s

## Finding compressed sections
