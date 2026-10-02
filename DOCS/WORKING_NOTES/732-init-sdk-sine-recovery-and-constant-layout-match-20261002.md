# Init SDK sine recovery and constant layout match

Date: 2026-10-02

## Recovery

Init `__sinf` at `0x10026540..0x10026700` now emits its complete 112-word /
448-byte body from semantic C in `conker/src/game/generated_sinf.c`. The
generated-slice directory is an existing build convention, not its execution
section: the replacement is linked in Init. Game's existing `sinf` source
and retail slot remain untouched.

The local SDK reference in `tools/ultralib/src/gu/sinf.c` supplies the original
exponent classification, double-precision polynomial, nearest-integer pi
reduction, odd-quadrant sign handling, and NaN/large-input exits. Constants
are external references to the existing retail data owners. The ordinary
`-O2 -g3` profile reproduces every word directly; no expected-word guards,
insertions, omissions, or alternate compiler profile are needed.

The layout row now names `generated_sinf` as the source owner. Existing slice
discovery, object padding, and generated linker replacement handle the new
object without changing the YAML or repurposing Game's source path.

## Constant ownership repair

The first linked comparison found one address difference at body offset
`0x1B0`: `D_8002C920` resolved to `0x8002C8F0`. The original math rodata owner
at `2C850` had likewise been placed at `0x8002C820`, 48 bytes early. Absolute
assignments masked the other constant-address differences without restoring
the actual data bytes to those addresses.

`anchor_init_math_rodata` in `tools/patch_generated_slice_ld.py` now anchors
the existing `2C850.rodata` object at `0x8002C850`. Its existing contiguous
layout places the following `2C920` NaN owner at `0x8002C920`. No constant data
is duplicated and no hardcoded code-pointer workaround is used. The generated
linker's US-only path applies the anchor; other versions are unchanged.
Two focused tests check insertion before the original owner and preservation
of unrelated linker text.

## Verification

The explicit `make -C conker NON_MATCHING=1 all -j4` code build and binary
regeneration pass. Use the explicit `all` target: a bare make currently selects
an earlier object dependency target and is not evidence of a full code build.

Direct linked-byte comparison with `conker/conker.us.bin` confirms:

| Span | Bytes | Result |
| --- | ---: | --- |
| Init `__sinf` | 448 | Exact |
| Neighboring `sqrtf` | 16 | Exact, unchanged address |
| `__n_CSPHandleNextSeqEvent` | 276 | Exact, unchanged address |
| `__n_CSPHandleMetaMsg` | 716 | Exact, unchanged address |
| Math/NaN data at `0x8002C850..0x8002C930` | 224 | Exact |

```text
__sinf SHA-256
d7840ece4eac7dccb91884b9b448cae90a18cfe285443df35d7bbffc85bcf25b
Math/NaN data SHA-256
46fdb19fe4681fbbeb69f6b26d094c940633fa6e2486940edd051f4c3d5dca19
```

Fresh conversion and linked matcher results:

- Total: 5,459 / 6,042 C rows; 3,238 byte-exact, zero drift, 2,221 different.
- Init: 490 / 539 C rows; all 490 exact; 147,944 / 164,048 C bytes.
- Game: 4,788 / 5,321 C rows; 2,567 exact; unchanged.
- Debugger: 181 / 182 C rows; all 181 exact; unchanged.

All 13 tool unit tests pass, including the two linker-anchor tests, five
word-patch tests, and one matcher test. Project tool checks and whitespace
checks also pass. Existing audio pointer-type warnings
remain outside this change. No gameplay launch or full compressed-ROM build
was performed; this is linked guest-code/data verification. The sibling host
port and its frozen Release artifacts are unchanged.

## Resume

Continue with `__n_CSPHandleMIDIMsg`, whose complete 954-word retail boundary
and custom behavior are recorded in Note 731. The other 48 Init assembly rows
retain original handwritten/shared-register ownership. Do not reintroduce the
earlier blanket handwritten classification of `__sinf`.
