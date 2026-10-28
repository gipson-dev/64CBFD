# 1761 - EEPROM block reader direct C match

Verified: 2026-10-28. Target func_151DD3A0, sole compact function in generated_20A850.
VA151DD3A0..151DD454 is 45 words /180 bytes. The slot ends at 151DD460:
retail ROM20A850..20A910 is 48 words /192 bytes, including three alignment nops.

## Recovered source and ABI

Replace the zero-return placeholder with
s32 func_151DD3A0(OSMesgQueue *queue, u8 address, u8 *buffer, s32 remaining).
Keep the address name, meaningful comments, and existing address-based symbol
for compatibility with all bindings. Remove the obsolete placeholder banner.
The local SDK osEepromLongRead declaration and original helper/caller assembly
corroborate the interface. Two local typed provider declarations suffice;
no shared-header or other production function changes are needed.

1. Capture all four arguments, narrowing address to one byte. Initialize status
   to zero. Always call func_151DCFD8(1), including empty or negative requests;
   keep polling while it returns nonzero.
2. While signed remaining is positive, call func_151DD140(queue,address,buffer).
   Return its exact nonzero status immediately. On success subtract eight,
   increment the byte address with wrapping, and advance the buffer by eight.
3. Return zero after all reads succeed. A positive partial final length still
   reads a complete eight-byte block. Caller storage must cover those blocks.

The original frame is 48 bytes: S0 remaining, S1 address, S2 buffer, S3 status,
S4 queue; RA at +44. The full original A1 is stored at entered SP+4, after
capturing its low byte. Preserve saved-register lifetime across volatile GPR,
FPR, HI/LO and outgoing-home provider clobbers. The raw three call bindings are
+52 and +68 to func_151DCFD8; +96 to func_151DD140.

The initial break-on-error source emitted 43 words by sharing the epilogue.
Early return restores 45, then remaining/address/buffer source update order
recovers the exact independent AND/decrement scheduling. All 45 body words
emit directly under the existing O2/g3 profile; zero guards or inserted words.
Raw selected/original body SHA256:
~~~text
c5cdafd5c29304ef8a69524df3cb3a62bbb8622ae3a416fb5972fbd7b876b192
~~~

## Provider and original caller boundaries

Original func_151DCFD8 takes the blocking flag, services pending EEPROM writes,
and returns busy/completed status. Its current production definition remains
an unchanged placeholder. The block reader func_151DD140 has the recovered
OSMesgQueue/u8/u8-pointer interface and validates the EEPROM command/DMA path.
This wrapper qualification uses bounded providers; it does not complete the
pending-write helper or claim EEPROM hardware or real-save acceptance.

The aligned ROM census finds exactly three JALs and no pointer literal:

| Original caller | Call VA /ROM | Address | Buffer | Length |
| --- | --- | ---: | --- | ---: |
| func_15006590 | 15006654 /33B04 | (slot*16+4)&255 | D_800BE358 | 128 |
| func_1500727C | 15007298 /34748 | 0x44 | D_800BE2F0 | 112 |
| func_15007440 | 1500745C /3490C | 0 | D_800BE358 | 32 |

Map actual original windows of12,11,12 words, validate each against frozen ASM
and retail, and connect the selected target. Eighteen cases check queue
D_800BE900, captured arguments, successful/error partial provider writes,
and subsequent replacement of the return status. The three current C/ELF
callers remain unchanged zero-return placeholders. No complete checksum,
caller restoration or additional matching credit is claimed.

## Fresh qualification and failures preserved

Both canonical tools copies pass eight fresh canonical_v4 methods and shared
project-tool checks. Installed copies each pass two fresh owner/image checks;
six semantic methods are reused only by exact seal/module/artifact identity.

- 4,705 guest cases cover every byte address, wrap beyond 256 blocks, signed
  negative/zero/positive lengths, INT_MIN, bounded INT_MAX error, positive
  partial blocks, busy sequences and exact nonzero errors. Provider mutations
  and volatile/home clobbers check argument capture and saved-register lifetime.
  Guest stack/queue aliases compare private state and traces; the independent
  disjoint-data reference also checks effects and call sequence. All 45 root
  words are visited. Native storage cases are valid disjoint backing arrays.
- Native32 O0/O2/O3 with trapping UBSan each pass 49,152 positive cases across
  two byte offsets, all 256 addresses, complete storage fences, busy counts,
  first/middle errors and lengths through 2057. Ten wrong C variants fail
  effectively: missing/incorrect/short polling, normalized/ignored error,
  wrong address/buffer/length step, discarded partial block and false return.
- 416 fired root access-prefix pairs preserve full private state, trace,
  fault PC and delay ownership. Empty requests need no buffer or queue mapping
  in the non-mutating provider contract, but still poll. This is not hardware
  EPC, exception or pointer-overflow acceptance.
- Three independent GNU layouts exercise all three J26 bindings in 24 cases.
  The real padder reproduces the object. Three raw/binding and six full-image
  corruptions fail closed. An actually compiled skip-empty-poll variant is
  rejected by call sequence on length zero, without an unmapped-read shortcut.

Preserve failed drafts and receipts. First canonical setup exposed a wrong
unpack count for the established link helper; the next exposed a fixture
counter shadowing the inherited memory-read trace. Correct those fixture
errors before the passing v3 run. Final banner cleanup changes debug-bearing
compact output but not body/bindings/pools or the padded object. Preserve its
initial assertions and old Make shadow, rebuild all final evidence, and pass
v4 against the final source. No weakened compiler flags or functional gates.
Routine Claude calls: zero.

## Actual Make, literal image and measured progress

The sole-owner route is three actual commands: normal IDO, padder, GNU as.
No GLOBAL_ASM preprocessing, profile changes, neighbors or pool changes.
Selected/owner/actual Make diagnostics are empty. Production exits zero and
reproduces the qualified padded object and strict full-image prediction.
The inherited duplicate generated_12D630 Make recipe warning remains.

The full ELF changes exactly 137 bytes: 136 code bytes and one symbol-size byte
12->180. Keep the 180-byte body extent separate from the 192-byte padded slot.
All 6,056 addresses, 6,055 other bodies and all other named definitions stay
fixed, with zero exclusions. All 720 protected Game data owners /189,088 bytes
remain exact. Headers, helper/caller sources and objects, map, inventory CSV,
and the guard manifest remain unchanged. The padder retains all three trailing
alignment words.

ELF SHA256:
~~~text
90784cd8cccfb9b4ada79065984003ebf4fc1ae7ead31cd2b824700665287087
~~~
Native CRLF guard SHA256 (Git-normalized LF unchanged):
~~~text
f867c3817abab6b6ef822343afa48a4b188e7067ce1d4c69a078b54a6f4b4c40
~~~

Seal 16,232 Native/cache inputs and 233 focused inputs. Recount the captured
adopted Native ELF, with no denominator/classification changes:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,839 /5,506 (69.72%) | 1,667 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,166 /4,833 (65.51%) | 1,667 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_151DD3A0 becomes exact. The 4,130 threshold leaves 291 more to 75%.
Remaining source shapes: 1,538 placeholders, 120 semantic/other, nine unlocated.
Typed func_151725FC and NULL func_1518F5D0 remain uncredited.

Predecessor consumer b7cb3203d8bc513e409aeb2993eb42be17fcf354 and tools
4e8fbb1e7c38d582c7e7407db10dac562ee5dea6. Bank the tools first at
9b6dcfaf4390cd65691a77ec5ae382e127f4896c, then the qualified source, consumer
pin and seven measured documents. Preserve the older mirror's 1,732 inherited
dirty paths plus the two new files. No push. Root README changes only its
two aggregate matching rows; detailed recovery updates remain here.

Refresh ten changed C/Markdown/tool sources structurally after committing.
Retain every old node and valid directed confidence/context relationship;
validate the target return, parameter and two distinct helper relationships
against actual source and all three object bindings. Current production
callers remain placeholders, so add no invented caller edges. Outside-scope
freshness and communities remain historical, with no full-corpus extraction
or global clustering/centrality claim. Detailed receipts and independent
final audit live in conker/build/game-eeprom-block-read-match/.

Next inspect func_151152A8 using a fresh predecessor and caller/ABI audit.
Keep func_1514E920 parked and uncredited. The 75% goal remains active.
