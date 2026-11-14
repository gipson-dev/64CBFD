# Game height emitter private screen

Date: 2026-11-13. `func_150E971C` remains a production placeholder in
`conker/src/game/generated_113D60.c`; neither screened candidate is credited
as a match. Its retail body has 91 instructions at `0x150E971C..0x150E9888`,
followed by two alignment words.

The callback first invokes `func_151337C0`, then compares the actor height at
offset `0x3C` with a threshold at `0x170`. It returns 1 when the less-than
comparison is false, including unordered inputs; otherwise it returns 0. When
the low five bits of the following word equal 10, it draws two random values
and passes a locally assembled descriptor and actor data to `func_1513C73C`.
The second random helper runs before the final position and actor-byte reads.

The constructor copies 40 descriptor bytes. Retail does not initialize eight
of those bytes: offsets `0x1C..0x21` and `0x26..0x27`. This is observable in
the finite guest screen, not merely a difference in dead stack storage. With
the same seeded incoming stack, the straightforward C candidate places the
descriptor at incoming SP minus 40 rather than retail's minus 44. All 32
emitting cases in the screen consequently pass different descriptor bytes.

A private storage-shape experiment adds four trailing bytes to the local C
object. It places the descriptor at the same incoming-stack address and
agrees with retail in all 72 finite guest cases, including 32 emitting cases,
stubbed helper clobbers, actor mutations and all 40 copied bytes. This is a
bounded comparison against retail instructions with mocked helpers, not a
proof of C semantics, unrestricted aliasing, exceptional floating point, the
real helper's behavior, or whole-image identity. The extra storage is an
experiment, not a claim about the original declaration.

Both versions emit 91 words. The straightforward version has 71
same-position retail words; the padded version has 67. All 28 other compiled
owner functions, normalized pools and compiler diagnostics remain unchanged
in this screen. The padded variant also changes the compiler-generated frame
from retail's `0x80` to `0x88`, so its frame, stack-access scheduling, helper
behavior and possible guard normalization still require qualification.

Tools commit `756ca2b` contains the screen. Reproduce with the mounted tools
checkout and the fingerprinted ROM, ELF,
source and compiler inputs:

```sh
PYTHONPATH=. python3 -m tools.experiments.game_height_emitter_150e971c_screen
```

The screen fails closed if those inputs change and writes its temporary
objects and reports under `conker/build/game-height-emitter-150e971c-durable`.
`make tools-check` also passed, and the sibling tools checkout's existing
dirty paths were preserved.
Before installation, qualify the original caller and real update helper,
complete independent guest and native C coverage, audit padding and guarded
instructions, and pass actual Make and strict whole-image checks. Production
source and progress remain unchanged: Game **3,784 / 4,843 (78.13%)**, with
**91** further Game matches needed for 80%.
