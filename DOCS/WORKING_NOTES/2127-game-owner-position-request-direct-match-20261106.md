# Owner-position request direct match

Date: 2026-11-06. Continue the 80% goal from consumer
`943ee0830e37ab3a312d7380af2222ddf15d08d5` and mounted tools
`3c4d5c22f525c4e79ff2235b79f7a1b8f8cbc921`, following
[Note 2126](2126-game-five-source-effect-constructor-direct-match-20261106.md).

## Recovered body and interface

`func_151A3504` in `generated_1D0840` now emits all **70 words** directly
from semantic C: VA `0x151A3504..0x151A361C`, ROM `0x1D09B4..0x1D0ACC`,
280 bytes, frame `0xA8`, saved RA at SP+`0x34`. The existing O2/g3 profile
and all four R_MIPS_26 bindings are preserved, with **zero guards**.
All **22 raw and padded neighbors** remain unchanged, including the recovered
C caller `func_151A4ECC`, query `func_151A4E34` and assembly-backed
`func_151A5170`. The old static shortlist counted prototypes and reported
27 functions; the assembly, layout and compact object establish 23 slots.
All compact/padded pools and register metadata remain unchanged.

The supported interface is `u8 *(void *input, u8 channel)`. Input points to
a valid owner-link snapshot; its first word is the owner pointer. A zero
owner returns NULL. The routine dereferences input before this test, so no
input-pointer null guard is invented. The channel retains the retail low-byte
incoming home, read after the position query. Both known callers ignore the
result, but the function returns the created pointer or NULL and that contract
is retained. No caller casts or existing matched caller code are changed.

The routine copies **0x30 bytes** into a local **0x50-byte payload**, then
sets kind6, two float zeros and two flag bytes. It constructs a separate
**0x1C-byte request**: signed lifetime1000 at +0xC, flags2 at +0xE, step8
at +0x10 and count50 at +0x15. The query writes a position into the request;
on success its three words are copied to payload+0x34 and flags are ORed
with4. Query mutations of the live payload/request remain observable.
There are 59/71 defined payload bytes and 9/21 defined request bytes on
query failure/success. Reserved bytes retain stack contents. Native tests
score defined fields; guest tests preserve and compare every seeded byte.

The factory call is
`func_15147A80(&request,0x50,0x18,6,6,6,0,0,NULL,channel,0)`.
On success, payload destination is loaded from result+0x98 and all80 bytes
are copied there. The copy return is ignored; the created pointer is restored
from its saved SP+0x38 home. Guest aliases retain forward-copy effects,
including output that overwrites that home. Portable native tests use valid,
disjoint objects and do not claim overlapping memcpy behavior.

The typed initial source already had70 words/frame0xA8 but17 differences.
Declaring the request first recovered local placement; keeping the two zero
float assignments separate recovered the final two stores. Complete direct
identity required no profile change, normalization or Claude advisory call.

## Qualification

All eight checks pass before installation in both tools configurations and
again after installation against both actual helper copies. The sibling
overlay stays in the ignored target directory; its six tracked edits and
2,428 untracked files remain unchanged. Both tool smokes are fresh. Three
unchanged shared suites per copy are explicit exact-hash reuses from Note2124
(match-progress, word patches, PC16 padding), not fresh regression executions.

- **716 cases per body**, original/raw/padded, reach all70 words and cover
  owner rejection, query/factory outcomes, all256 channels, complete guest
  records/memory, raw point patterns, live argument homes, provider clobbers,
  partial initialization, snapshot mutations, forward aliases and saved return.
- **185 own-access fault prefixes** compare complete machine states across
  all three bodies, including first-word access, saved RA/result, request
  fields, query output and the delayed incoming-channel read. These qualify
  guest instruction order, not portable C fault semantics.
- **192 cases per body** connect the original26-word query,11-word byte-copy
  and115-word factory. An independent public-memory reference checks matrix
  selection, allocation arguments, full descriptor copy, header fields and
  final payload. **121 of152 helper words** execute under root arguments;
  resource and optional paths remain out of scope. Transform, allocator and
  zeroing providers are bounded. Private helper stack, full helper coverage,
  hardware and gameplay are not claimed. The optional-clear byte is +0x7C;
  an initial reference offset error was corrected against original execution.
- **64 cases per body** run both original caller windows (5 and7 words),
  with explicit prior arguments, parent, F8 and stack preconditions. The
  recovered caller restores its owner/flag; the earlier caller's following
  call overwrites the result. Full parent execution is not claimed. ROM
  census finds JALs at0x1D08F0 and0x1D23F0, no tails or literal pointers.
- **Nine independent GNU links**, three layouts and24 cases per body
  qualify all four R26 bindings. Entry,280-byte symbol and eight external
  container-alignment zero bytes are separately pinned with SUBALIGN(4).
- **393,216 native32 SDK/UBSan calls** at O0/O2/O3 assert every used offset,
  all256 channel values, gate/query/allocation outcomes, callback mutations,
  raw point representations, direct calls and compatible callbacks. Output
  guards and defined fields pass; reserved bytes are not scored. Ten incorrect
  variants return checked42 without diagnostics.
- All280 body-byte corruptions, four binding corruptions and five image
  corruptions are rejected. The former stub and wrong chained-zero source
  also fail the literal gate. These negative controls do not alter production.

## Production and progress

Actual Make compiles this owner once with its unchanged default profile:

```sh
make -C conker -o retail_word_patches.us.csv -o Makefile -j4 build/conker.us.elf progress.csv
make -C conker -o retail_word_patches.us.csv -o Makefile all
make -C conker -o retail_word_patches.us.csv -o Makefile match-progress NON_MATCHING=1
```

Keep both old-dependency flags for scoped builds until a deliberate broader
rebuild, as in Note2125; no unaffected object timestamps are changed.
The actual ELF equals the independent **204-byte** prediction with **zero
exclusions or metadata permutations**. Only this body and symbol size
(12 to280 bytes) change. All6,052 addresses, conversion rows, progress.csv
and189,088 protected data bytes in720 owners remain fixed. Make and guard
CSV are unchanged. The unfinished whole image retains its expected checksum
failure and existing duplicate generated_12D630 recipe warning.

| Section | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,196 / 5,512 (76.12%) | 0 | 1,316 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,523 / 4,839 (72.80%) | 0 | 1,316 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

**214 more** matches reach the current4,410 threshold for80%. Fingerprints:

- ELF: `a2f56948a8333d9828998dcfb4a2467ef8afaf32ca7c0bec0a5b259fb30957cd`.
- Owner: `66f326aa7cb1dfb67fa9d3a24b7df25449021ac33fade754e68788c44006c2d9`.
- Code binary: `91d4942e9a1fc47267a84ea191e04364428dbb03b0088e3fd3e03b346072ab1a`.
- Unchanged guard CSV: `7d469fee131d8adbc169fda991046c614fea90f2704bfcd612c41371e6efa1f0`.
- Unchanged Makefile: `509371c33a6266fa242b20212c16cf42d4b61575a8773b053bfad43d0778ae1b`.

Evidence is retained in `conker/build/game-owner-position-request-151A3504-match/`.
Graphify receives a scoped refresh with retention accounting; no full-corpus
extraction is claimed. Commit tools first, then the consumer pin/source/docs.

Next static target: `func_151CE51C`, owner `generated_1FA770`,70 words.
Qualify its event-record lookup, position output range, signed byte indices,
0x1C-byte table stride, floating thresholds and0x60019 dispatch before C
recovery. No matching credit is assigned at discovery. Keep unrelated work,
private inputs/saves, handwritten `func_150A76F0` and frozen host Release
separate. The broader80% goal remains active.
