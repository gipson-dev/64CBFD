# Game positional effect-and-audio handle direct match (2026-11-04)

## Outcome

`func_150E3414` now replaces its zero-return placeholder in
`conker/src/game/generated_1104D0.c` with the semantic positional-effect and
audio-registration wrapper. Its complete 64-word / 256-byte retail body emits
directly from C with the original 72-byte frame and four relocation words. No
word guards, instruction insertions, omissions, alignment changes, compiler
profile changes, or inventory changes are required.

This is a source, ABI/caller, raw and padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and graph
retention result. It is not runtime sound, visual-effect, scene, save-state, or
gameplay acceptance.

## Recovered behavior and ABI

The nine O32 arguments are three signed sound coordinates, three signed effect
coordinates, a full-width context, a full-width effect kind, and a binary32
step value. The wrapper calls `func_150E3020` with the effect position, three
zero target coordinates, kind, step, context, each sound coordinate converted
from signed word to single precision, a final zero, and signed halfword
sentinel `-99`.

Allocation failure returns zero and does not register audio or modify an effect
record. Success calls `func_1000FA64` with sound ID `0x2D0`, the low signed
halfwords of the three sound coordinates, volume `0x5DC0`, radius `0x1770`,
falloff `0x3E8`, callback `func_150E33CC`, null callback data, and three zero
flags. The returned unsigned 16-bit sound handle is stored at effect offset
`0x4A`. The function reads the unsigned slot byte at offset `0x48` and returns
its one-based value, including 256 for slot byte 255.

The existing effect factory still returns an address-valued `s32`; the wrapper
keeps that shared interface instead of inventing a pointer return type. The
audio provider declaration matches its recovered 12-argument ABI. This change
does not claim recovery credit for either provider.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x150E3414..0x150E3514` |
| Retail ROM range | `0x1108C4..0x1109C4` |
| Owner | `generated_1104D0`, 13 compact functions |
| Frame | 72 bytes |
| Relocation at `0x080` | `R_MIPS_26 func_150E3020` |
| Relocations at `0x090`, `0x094` | `R_MIPS_HI16/LO16 func_150E33CC` |
| Relocation at `0x0D0` | `R_MIPS_26 func_1000FA64` |
| Natural object body SHA-256 | `0ab13fb3ed75394d1abee20045a9e3222c6419d1f1d7abc13ce7165efb2b27ee` |
| Linked retail body SHA-256 | `8dc372cb9b7454b5316acbc8f24fcaf95235656415ab68b1e2f13a0221204e99` |

## Caller and callback evidence

The retail ROM has one aligned `jal` to this function, at ROM `0xCAB04` /
VRAM `0x1509D654`, inside `func_1509D180`. Its retained assembly loads the
three sound coordinates, three effect coordinates, kind, and integer source
for the converted step from the current record, supplies `D_800CC2D0` as the
context, and consumes the result as zero or `(handle << 6) | 0xE004`.

The parent remains a zero-return C placeholder. Its retail assembly is used as
caller evidence and a bounded execution window; no current C caller edge or
parent recovery credit is inferred. There are no aligned pointer literals for
`func_150E3414`. The callback address passed to the audio provider is the
existing `func_150E33CC` body in the same owner.

## Qualification

The candidate screen found five sensible integer/pointer/local spellings with
the same exact 64-word body. The adopted integer-handle form matches the
existing factory declaration and makes no unsupported pointer-return claim.
The permanent qualifier and installed-tree suite establish:

- all 64 guest instructions execute across 1,280 cases, two stack phases,
  allocation success/failure, all 256 slot bytes, signed word boundaries,
  signed halfword coordinate truncation, binary32 coordinate conversion, and
  legal volatile GPR/FPR plus outgoing-home clobbers;
- 768 executions of the original 86-word caller window observe all nine
  arguments and both the zero and encoded-success result paths;
- native 32-bit O0, O2, and O3 each pass 4,096 cases, for 12,288 executions,
  with undefined-behavior trapping, valid aligned object backing, all slot
  bytes, and varied unsigned 16-bit sound handles;
- thirteen independently compiled semantic controls are rejected, covering
  effect and sound coordinates, zero targets, kind, step, context, sentinel,
  sound ID/volume/callback, both effect fields, and one-based return;
- all 256 raw-byte mutations and four relocation-binding controls fail closed;
- the twelve neighboring owner functions and normalized data pools remain
  unchanged; and
- the qualified full ELF changes only `func_150E3414`, preserves every
  function address, has zero strict-image exclusions, and retains all 189,088
  protected Game data bytes across 720 owners exactly.

The installed five-test suite passes in 33.163 seconds. The shared
match-progress, guarded-word, generated-PC16, and protected-data suite passes
all 19 tests in 5.159 seconds.

## Production closure

The actual Make rule compiled, padded, assembled, and linked
`generated_1104D0` from the installed source. The production owner and full
ELF equal the independently qualified artifacts. `make -C conker all -j2`
generated the ROM and stopped only at the expected final retail-ROM SHA check;
there was no compile, padding, assembly, link, or image-generation failure.
The inherited duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `5a3181727523cb25926ee7fc331c52e77a4f730c1f61433994de3cdbb1086aeb` |
| Qualified / production linked ELF | `feaa6333d20cea1f98b78faf1094ffe42cfffeb191f0e1cdeb2823138318bacb` |
| Production rebuilt ROM image | `213e968590bde6f4b4f7ec1624325f33d95bbe70662988201aa70f01b7b0c89b` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Guard table | `2c94dfb97dbd6abd4bdab3c379ea92d6131a5a1f70a2d2c04d1608a4d80ab85a` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,137 / 5,512 (75.05%)**, zero address drift, 1,375 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,464 / 4,839 (71.59%)**, zero drift, 1,375 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **273 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,603 nodes against the retained 58,397-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`ae8f43c7eb19aa80c3046ceee0c7e86d2f44166409dc12316c05fc7896d44c96`.
No forced refresh was used.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,407 nodes, 112,267 links, and 5,111 communities. Against the saved
pre-change snapshot, 58,394 / 58,397 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Thirteen IDs were
added: those three relocated headings plus the Note 2066 file node and its
nine indexed headings. The ten-node and ten-link net additions are confined
to the new working note. The explicit-refresh graph SHA-256 is
`af2b9d4267dad72e8286f96fc4737136563358a8ff57f6e4832360021fc699d9`.

A final note-only refresh after recording this section reports no code-graph
topology changes and preserves the same node, link, community, and old-ID
retention counts. Historical global analytics are not represented as fresh
full-corpus extraction.

## Continuation

Continue with ordinary Game candidate `func_150F9AB0`, 64 words with 63 real
differences in the fresh production image. Keep the seven documented
handwritten/custom-ABI/boundary cases separate: `func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC`, and `func_150A6760`.
