# Record byte-ID search restored directly from C

`func_15004BF0` now has a complete semantic C body in `conker/src/game_30E90.c`.
The normal O2/g3 compiler emits all **60 words and twelve relocation bindings
directly**, with **zero guards, insertions or omissions**. Its signature is
`s32 func_15004BF0(s32 descending)`. The stale placeholder comment is removed
and the forward declaration now describes the actual argument.

The production build and an independent Windows-consumer ELF recount establish
**4,003 / 5,506 (72.70%)** exact C functions, Game **3,330 / 4,833 (68.90%)**,
zero address drift and 1,503 still different. Init remains 492/492 and Debugger
181/181. The conversion inventory CSV and entire guard CSV are byte-identical
to their predecessor. The 75% goal remains active: **127 more** exact functions
are needed to reach 4,130/5,506.

## Behavior and data view

VA 0x15004BF0..0x15004CE0; ROM 0x320A0..0x32190. It is a leaf with no frame.
`D_800DBEF0` is the signed record count, `D_800DBEF4` the record base, and
`D_800DBF00` a captured byte boundary. Records have stride 0xA0 and the searched
ID byte is at+0x72. A private `ByteIdRecordView` names that byte without changing
the shared `struct131` layout or any shared header.

For a zero mode, the candidate begins at 1 and the scan begins at the captured
boundary index. A matching ID increments the candidate and restarts the scan
at that first index. Reaching 256 returns 255. A nonzero mode instead starts at
255-boundary and scans from index 0; collisions decrement the candidate and
restart, and reaching zero returns the original upper limit.

Those saturation fallbacks can already be in use. They are preserved exactly,
with no replacement sentinel or alternative allocation policy. Signed negative
and empty counts, or a forward boundary beyond the count, can skip scanning
without loading an absent record-base global.

## Direct source recovery

The first for-loop draft had 19 word differences. A typed record field reduced
this to 17, but the relocation positions still differed. Reusing the mode
argument as the captured scan boundary after selecting direction recovered the
retail A0/V0 allocation, leaving only two opening global loads reversed.

Putting the boundary assignment in the forward loop initializer,
`index = descending = D_800DBF00`, recovered the load order and all twelve
bindings directly. An explanatory source comment records the parameter reuse.
The exact isolated payload is also emitted in the complete owner; no guarded
normalization is used. Earlier private drafts are retained as experiments,
not installed or credited separately.

Raw/unrelocated compiler payload SHA-256:
`544b07fdb0d4cc0f80f8ac3839d82c217e1ee76ee841f39af95a4d23f9991d91`.

## ABI and guest qualification

The aligned input census finds three direct JALs at ROM 0x31444,0x31654,0x319C8,
corresponding to VA 0x15003F94,0x150041A4,0x15004518 in `func_150039E0`.
There are no aligned literal function pointers. The first two calls pass 1;
the third passes 0 in its delay slot. All three store the returned word's low
byte at record+0x72.

The original caller windows start at 0x15003F90 (five words ), 0x150041A4
(three words), and 0x15004518 (eight words). They pass 27 cases/54 executions,
including the post-call count reload and loop-index advance in the third.
These are bounded caller windows; they do not qualify the complete large
caller or prove every forced window input naturally passes its preceding gate.

An independent used-ID-set reference agrees with the raw C and retail
instruction streams in 604 cases/1,208 executions, reaching all 60 retail words.
The matrix includes both directions, full32-bit mode values, duplicate and
ordered IDs, skipped prefixes, signed count limits and four 256-record
saturation fixtures. Six sparse executions avoid absent memory correctly.
Records are immutable within the independent reference's domain.

Three independently linked code/global-address profiles include distinct
global high halves and signed-low16 carry boundaries. Both complete rebased
payloads remain identical, and nine cases/18 executions agree with the reference.
Forty fired access-prefix cases/80 executions and a guest record/start-byte
alias also agree. The guest alias and fault-prefix tests make no portable C
aliasing or fault claim.

The original 50k-step interpreter limit was too small for a long saturation
fixture. A local clone of the same interpreter loop uses a bounded one-million
limit; no shared interpreter source is modified. One early alias fixture moved
the mapped byte without relinking its symbol, causing an unmapped read. The
corrected test independently links both bodies to the alias address and passes.
Neither fixture failure represents a production-source defect.

## Native, owner and production gates

Native32 asserts the private record ID offset and both private/shared record
sizes. A separate used-ID-set reference checks the result while complete record
bytes, canaries, count, pointer and boundary globals remain unchanged.

O0/O2/O3 each pass 864 positive cases under UBSan and 864 cases for each of nine
effective compiled controls: narrowing the mode, ignoring the forward boundary,
omitting either restart, changing either saturation fallback, using the wrong
ID offset, changing the reverse boundary, and substituting an empty-count result.
Each executable completes 8,640 cases.

Fresh complete-owner compilation has no diagnostics and preserves all eight
neighbors and pools. The actual three-command Make recipe emits exactly the
independently padded object. All 240 payload-byte corruption controls, twelve
binding controls and two owner/function scope controls reject changed input.

The independent prediction and production ELF agree literally in every byte.
Only the target instruction bytes and symbol extent 12->240 change; there is no
metadata permutation, mask or exclusion. All 6,055 other linked bodies and all
addresses remain fixed. Protected Game data matches across 189,088 bytes and 720
owners. Full review of the 17,374-file predecessor seal finds only source, target
object and ELF changes, with no unexpected dependent-object changes.

Production ELF SHA-256:
`8094c1c9a8fdb238b7fa7419e8e4edb53507e81e8e7594d7543953b42642a6ea`.

Seven fresh target tests pass in both tools checkouts, both shared tool checks
pass, and the installed production suite passes again. Tools `db215dc` bank
the qualification; `75baf67` only corrects module/diagnostic naming, verified
with executable-AST equivalence and syntax checks in both copies. Tools are
committed before the consumer pin. The older mirror's inherited work is
preserved and it is not committed. Nothing is pushed.

## Reproduction and continuation

With the prepared consumer inputs and retained target stage:

```sh
python3 -m unittest tools.tests.test_game_record_byte_id_match -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Stage: `conker/build/game-record-byte-id-15004BF0-match`.
`preparation.json` records the actual private Make/link;
`production-v17.json`, `production-seal-changes-v17.json`,
`installed-audit.json` and `native-production-recount.txt` record acceptance.

Next screen: `func_15049350`, a plane-coefficient routine. Start with its caller
ABI: the retail first coordinate words arrive through integer argument
registers despite their later floating-point use. Its slot is 60 words,
including three post-body alignment words. No C from that screen is credited.
Other private candidates remain uncredited.
