# Note 2476: Vertex transform/clip custom-register restoration

Date: 2026-11-15. Consumer baseline `777822ad54e1533d89bb8ee427dbe4013a2be004`,
tools baseline `074dfa4925bfed6c4235eef835fff95104c73122`.
Continues [Note 2475](2475-game-actor-effect-binding-register-roles-and-byte-match-20261115.md).

`func_150A613C` is restored from its false zero-return C placeholder to the
original assembly in `conker/asm/D3040.s`. Its complete **53-word / 212-byte**
body matches retail, with no alignment tail, guards, relocations, profile
changes or shared-header edits. This is **assembly restoration with zero
new C matching credit**. The source comment records its actual interface.

## Ownership and register protocol

The source owner is `conker/src/game/generated_D3040.c`; VA
`0x150A613C..0x150A6210`, ROM `0xD35EC..0xD36C0`. The included fragment is
`conker/asm/nonmatchings/generated_D3040/func_150A613C.s`, extracted verbatim
from its glabel through endlabel in the retained original file.

- T4 points to three signed XYZ halfwords. F20..F31 carry a 3x3 transform
  and translation; F16/F17 are the projection scales and F18/F19 the depth
  limits. These are actual input registers, not an ordinary o32 C signature.
- The transformed/projected coordinates return in F13/F14/F15, and T3
  carries the clipping flags. The return delay slot intersects the caller's
  running S2 mask with T3. The routine has no frame, stores or external calls.
- The depth checks use ordered comparisons and branch-likely delay slots.
  The X-side test consumes the sign of the unscaled transformed X value;
  the Y-side test consumes the sign of the scaled Y value. Negative scale
  cases distinguish those contracts.

The full aligned retail Game-code census finds six direct JALs at ROM
`0xD31C0`, `0xD31D8`, `0xD31F0`, `0xD34A8`, `0xD34C4`, `0xD34E0`.
The first parent loads T4 in the call delay slots; the second adds GP to
the loaded vertex offsets there. The surrounding instructions consume
T3 and F13..F15 directly. The aligned full-input pointer-literal census
finds no copies of this entry address. These measured inputs/outputs,
together with the parent save/restore and mask lifetimes, establish assembly
ownership independently of spimdisasm's handwritten comments.

The other placeholders in this geometry owner remain separate audit work.
`func_150AE280`, also near the top of the mismatch list, begins with a stack
swap and branch into its parent and contains a later unlabeled conventional
routine; it is not selected as a standalone C conversion from that list.

## Fresh qualification

The pre-install suite passes in **35.151 s**, the sibling overlay suite in
**44.242 s**, and the installed suite in **48.539 s**. Fresh `make tools-check`
passes. The focused command is:

```sh
python3 -m unittest tools.tests.test_game_vertex_clip_150a613c_restoration -v
```

The independent binary32 transform/clip model passes **2,205 cases through
three streams**: original assembly, postprocessed owner and padded owner.
Cases cover signed-halfword extrema, three matrices, negative projection
scales, depth/side boundaries, mask intersections and wrapped guest addresses.
All **53 original instructions** execute. The checks compare modeled output
bits/flags, preserved registers and FPRs, stack-pointer identity and read-only
memory. Nine fired prefixes cover each of the three halfword reads across
three fixtures, comparing complete modeled GPR/FPR/memory/condition/read-trace
and instruction/delay state between streams.

**102 connected cases at all six authentic two-word JAL/delay windows** execute
the complete helper. They compare returned coordinate/flag/mask outputs and
complete modeled states across streams. These bounded windows do not execute
the full parent routines. Five effective instruction controls reject an
unsigned X load, a wrong depth bit, an omitted S2 update, the wrong X scale
and a wrong positive-X clipping bit. All mutated instructions are supported
by the executor, so rejection requires a behavioral mismatch.

Both padders preserve the complete **17-entry owner / 16 non-target neighbors**,
all existing guards and normalized pools. **12 GNU links across four code
regions** preserve the complete target slot. Native C qualification does not
apply to this assembly protocol. The model uses lower-32-bit GPR and binary32
state; full hardware register state, FCSR, exceptional FP, whole parents and
gameplay acceptance remain uncredited.

## Independent Make and production audit

The actual five-command Make shadow and ordinary production build select the
existing GLOBAL_ASM owner recipe. Production command:

```sh
make -C conker -j4 -o Makefile -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

Production equals the independently predicted complete ELF: **185 changed
bytes, zero exclusions, no metadata permutations**. All **6,051 addresses**
stay fixed; only this helper's body and expected size change, from the
12-byte placeholder to 212 bytes. Only `generated_D3040.c.o` changes among
**698 objects**, in `.text` and `.symtab`. All 16 neighbors remain fixed.
All **189,088 protected data bytes / 720 owners** agree, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The frozen record has **862 production inputs**, with **858 non-adoption
inputs unchanged**, including all 80 headers, original assembly and guard CSV.
The inherited snapshot initially omitted this new owner source; the install
guard stopped before writing production, and that source was frozen only
after byte-normalized comparison with the recorded clean baseline commit.
The conversion CSV changes exactly one field, this helper's `c -> asm`.
No other conversion row changes.

GNU as reports odd-numbered floating-register warnings while postprocessing
the original instructions. Their final encodings are checked literally against
retail. The existing duplicate generated_12D630 recipe warning also remains;
no warning-free build is claimed.

Production ELF SHA-256:
`f9648bd31a9604b17b2753451395c9b9f7e54e01392ade3683ad55a4ca512349`.
Helper body SHA-256:
`a377334400eefe1c1ef1ec0e8199667b6b559aa9403f7c286d81b41a5d00aeeb`.
Included assembly SHA-256:
`12956de8441d5254408d38e46be509c3ccdaa02ec2cd05e7d709f85093578a6f`.

## Recount, checkpoint and next target

Fresh actual recount: **4,507 / 5,514 total exact C (81.74%)**, Game
**3,834 / 4,841 (79.20%)**, Init **492 / 492**, Debugger **181 / 181**;
zero drift and **1,007 different C functions**. Converted totals are
**5,514 / 6,048 (91.17%) / 86.19% bytes**; Game **4,841 / 5,327 (90.88%) /
85.57% bytes**. The exact-C numerator is unchanged. The percentage increase
comes solely from correcting a false C classification. At this denominator,
**180 additional C matches** reach 85%; that goal remains active.

Tools commit `66547a36b1fbdf2e7d90f9541fb6234b89053b1b` precedes the consumer source/assembly/docs/tools-pin
commit. Five owned files were tested through an ignored sibling overlay.
Sibling HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,434 dirty paths**
and Windows-Git status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9` remain
unchanged. Scoped AST extraction covers six files plus the explicit assembly
glabel/pragma relationship. All **61,997 prior IDs** remain; the helper concept
moves from C to assembly. Snapshot: **62,030 nodes / 116,198 links**, no lost
IDs. This is not full-corpus extraction. Hook heading aliases preserve old
document IDs after the commit refresh.

Five DOCS indexes gain one concise entry while retaining their old bytes.
The root README changes only four aggregate rows. Claude calls: **zero**.
No host-port source/build applies; frozen Release, saves and private inputs
are untouched. Nothing is pushed. Evidence and archived pre-install receipts
remain under `conker/build/game-vertex-clip-150a613c-restoration/`.

Next: **`func_150F97EC`** in `conker/src/game/generated_124920.c`, VA
`0x150F97EC..0x150F9950`, ROM `0x126C9C..0x126E00`, **89 words / frame 0x70**.
Its ordinary C interface is suitable for further recovery. A private typed
profile screen uses a real 12-byte transformed vector and eight-byte spread
record, replacing the alternate source's undersized pointer locals. Current
isolated results: **O2 86 words / frame 0x68 / 85 differences; O1 92 / 0x70 /
88 differences; O0 107 / 0x70 / 102 differences**. No profile is installed or
credited. The complete production owner, ABI/callers, guest/native, padding,
image and production gates remain open. Resume the source/profile work in
`conker/build/game-actor-joint-effect-150f97ec-private/`; keep the spread/vector
types correct and preserve all production neighbors when integrating a profile.
