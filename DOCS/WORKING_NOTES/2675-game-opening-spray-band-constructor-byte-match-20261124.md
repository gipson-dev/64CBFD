# Opening spray and band constructor byte match - 2026-11-24

`func_150C1F60` replaces its zero-return placeholder with the complete
**204-word function and 240-byte stack frame**. Production increases from
4,654 to **4,655 / 5,528 (84.21%)**; Game **3,982 / 4,855 (82.02%)**.
Init 492/492 and Debugger 181/181 stay fixed. Zero address drift, 873 still
different, **44 more matches reach 85%**. Only this constructor gets credit.

Owner `conker/src/game_EF410.c`; original
`conker/asm/nonmatchings/game_EF410/func_150C1F60.s`. VA
`150C1F60..150C2290`, ROM `EF410..EF740`, 816 bytes. The recovered interface
is `void func_150C1F60(u8 channel)`; its single original direct caller ignores
the return register. A complete aligned pristine-ROM census finds one JAL
at ROM56A88 / VA150295D8 in `func_150265CC`, and no entry pointers.

## Packet ownership and lifetime

`OpeningLocalsEF410` contains an eight-byte angle header, a 64-byte band and
a 136-byte spray, totaling 208 bytes. A named three-float position structure
allows the final live position copy without union punning or pointer casts.
Saved RA is at new SP+28; locals are at +32, +40 and +104. The one-byte channel
is reloaded from its incoming home before each submission; the fifth band
argument is stacked at +16. Both older spray functions and their shared
`FixedSpray150C2290` layout remain unchanged.

1. Initialize the spray and submit it to `func_15151A38`, with channel and
   context 1, at 150C20E0. Initial XYZ uses D800A0230,40,D800A0234.
2. Update only the selected halfwords and float fields of the same packet,
   then submit it again at 150C2184. Preserve provider changes to every
   untouched byte, including XYZ, flags, reserved bytes and retained84.
3. Copy the packet's **live XYZ after the second provider** to the band;
   initialize angles (-159,68,-52,38), counts 25/18, speed 40/35, life 25/25,
   opacity 155/100, extent 1152/848, kind 6 and the remaining observed fields.
   Read D800A0250/0254 after that provider, then call `func_15150178` at 150C2278
   with `(header, band, 0, channel, 1)`.

Names describe independently observed layout and known parameters. Unknown
spray members keep offset-based names. Retail leaves reserved bytes and the
word at +0x84 unwritten. Guest fixtures seed and compare all bytes; native
fixtures read only initialized fields. This does not promise a deterministic
portable C value for unwritten storage. The target contains no FP arithmetic:
its float values are copied or loaded as words.

## ABI-only helper repair

`func_15150178` in `game/generated_17CAF0.c` now uses its existing callers'
canonical `void(void*, void*, s32, u8, s32)` interface. Its empty placeholder
emits six words: four incoming argument homes, JR RA and NOP. The fifth
argument already resides at incoming SP+16. Its **original 162-word / frame 184
implementation remains unrecovered and receives zero credit**. The comment
in source explicitly records that limitation. The previously repaired
five-word `func_15151A38` placeholder also remains unrecovered/uncredited.

The complete original helper and seven caller continuations were inspected.
There are no aligned entry pointers or unidentified callers. Call sites are
150C2278,150C27E8,150FA770,151D6BE0,151DC46C,151DC684 and151DC830. These
continuations do not consume a promised helper result; original paths can
retain incidental provider V0 values. Tests qualify the six-word ABI stub,
its four homes, untouched fifth stacked word, descriptor storage, SP/RA and
saved registers. They do not claim execution of the original 162-word helper.

## Scheduling proof and focused qualification

The semantic C emits the correct 204 words and frame 240 with 45 word
differences. Forty-six relocation-aware guards include one identity-word
binding guard. They normalize two closed blocks, words 40..47 and 139..197.
No instruction insertion, omission or arithmetic patch is used. All other
words and bindings are identical.

An independent byte-memory symbolic evaluator proves complete GPR/FPR/private
memory joins from arbitrary entry register and private byte values. The
second block has 30 matching accesses and only five inverted pairs, each
disjoint private storage: stores at SP+92/+100 commute past SP+96, outgoing
SP+16 and the incoming byte at SP+243. Global loads remain correctly bound.
Normal mapped/aligned stack, enabled FPU and stable disjoint globals within
provider-free blocks are explicit assumptions. With no FP arithmetic, FCSR
is unchanged compositionally. Raw fault/interrupt prefix identity inside
the reordered blocks is excluded.

* 1,024 cases per four guest streams cover all 204 instructions, all 256
  channels, high argument bits, two stack phases, arbitrary float words,
  retained bytes, changing globals and mutations after both spray calls.
  Compare complete registers/memory/provider observations. Canonicalize only
  the independently proved five private inversions in traces and events.
* 208 normalized/retail fault-prefix triples compare literally. These are
  emitted-instruction checks, not portable C fault semantics.
* The original three-word caller window 150295D4..150295E0 loads the channel
  byte and stores it in the parent frame in its JAL delay slot. Three cases
  per stream verify the child frame, all submissions and correct return.
* Native SDK32 at O0/O2/O3, strict aliasing and UBSan: 1,024 cases per profile.
  Eight effective source controls fail with comparison exit 42, covering
  partial update, untouched bytes, stale position, angles, life range,
  channel/context and late global loads. No signal/trap counts as success.
  Signaling NaNs and unwritten bytes are guest-only coverage.
* 227 raw-word/binding pins, 100 guard corruption rejections, 354 visible
  unguarded corruptions, two oversize rejections, 16 actual GNU links and 32
  rebased guest runs cover adjusted HI, negative LO and distinct JAL regions.

Both complete-owner padders retain all 17+40 raw/padded neighbors, pools and
diagnostics. The ordinary owner's second-padder geometry uses the same
frozen layout, not an independent original layout. Actual Make replays six
owner and five helper commands, including the unchanged motion-pool check.

## Independent image and committed bank

A separate reference compiles frozen before-C and substitutes the original
target ASM and explicit six-word ABI stub. It reconstructs every named ELF
definition and string from the frozen baseline. The C link and production
ELF equal that independent prediction: **892 changed bytes, zero exclusions**.
All 189,088 protected Game bytes across 720 owners, other function bodies,
addresses/extents, conversion CSV, old guards and unrelated objects remain
fixed. Exactly 46 target guard rows are appended.

ELF SHA256: `a6acba02c7756ba1cf983d71d59c43b3839e0a9b05ac46f68913cf718b5adacd`.
Padded owner: `2ce2a57146de54c94848a32901cc7a7460888660664aa943f0660d3e256e480b`.
Padded helper: `241b562b3488e1b1a5f81166daaded6b348e288ee4d7782b8c4b96c4be04fb6d`.

| Phase | Time | Gates |
| --- | --- | --- |
| preinstall-primary | 105.841s | 5 fresh / 0 reused |
| preinstall-sibling | 95.063s | 5 fresh / 0 reused |
| installed-primary | 80.434s | 5 fresh / 0 reused |
| installed-sibling | 77.620s | 5 fresh / 0 reused |

Shared tools-check passes. Tools commit
`fba9b0dad1428e287b62050f7503bf5e9ebf93cc` precedes the consumer commit.
Exploratory receipts are excluded from final qualification. All frozen live
inputs and snapshot hashes are audited, preserving the dirty real sibling.
Root README changes only aggregate rows; old DOCS index bytes are retained.
Normal Graphify update, actual hook completion and scoped AST refresh have
separate receipts with full old-ID/current-definition/qualification retention;
this is not full-corpus re-extraction. Host applicability is inspected, with
no direct C consumer or complete host build root found. No host/Release
edit/build, push, WSL restart or Claude model request. The 85% goal remains
active; dimensions 15015FBC and renderer 15197148 stay private/uncredited.
