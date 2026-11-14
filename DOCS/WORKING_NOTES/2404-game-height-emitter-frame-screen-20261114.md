# Game height emitter frame and padder screen

Date: 2026-11-14. This extends [Note 2403](2403-game-height-emitter-qualified-screen-20261114.md).
`func_150E971C` remains a production placeholder; no match is credited yet.
Tools commit `f6bf7fc` adds the checks below and formats the private C
candidate with one descriptor assignment per line. The reformatted candidate
still emits 91 words with 67 in retail positions; the same 24 guard positions
restore the complete retail stream.

Both padding implementations agree with the retail function and preserve all
28 neighboring production functions with their relocations. Across four
rebased layouts, 12 independent GNU links agree on the complete target body.
Five guest paths cover 142 modeled access-fault prefixes, with retail and
guarded streams agreeing on machine state, memory and traces.

An additional 195-case screen deliberately overlaps the actor with the
callback's private stack. The guarded stream agrees with retail in every
case, including the modeled exceptions; the unguarded C stream differs in
all cases because its compiler-generated frame and stack writes differ. Two
cases caused modeled assertion exceptions in at least one stream. These
overlap experiments are not a claim that such aliases are valid portable C or
occur in normal gameplay; they show why the frame normalization matters.

The complete private suite passed in the mounted tools checkout and in an
isolated sibling-tools overlay with mounted fallbacks. `make tools-check`
passed; the sibling checkout's 2,434 existing dirty paths were preserved.
The screen is still bound to the pre-install source, object, ROM and ELF.
Production adoption, build, independent post-build audit, recount and
documentation remain outstanding. The last verified Game count remains
**3,784 / 4,843 (78.13%)**, with **91** more matches needed for 80%.
