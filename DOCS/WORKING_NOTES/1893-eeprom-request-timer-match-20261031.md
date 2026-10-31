# 1893 - EEPROM request setup, timer calculation and signed result

`func_151DCEF0` replaces its zero-return placeholder in
`conker/src/game/generated_20A3A0.c`. Its recovered interface is
`s32 (OSMesgQueue *queue, s32 address, void *buffer, s32 length)`.
All 58 retail words match after three checked guard rows. The existing O2/g3
profile remains unchanged; no words are inserted or omitted.

## Request and return contract

VA `0x151DCEF0..0x151DCFD8`, ROM `0x20A3A0..0x20A488`: 232 bytes,
58 body/slot words and no alignment words. The frame is 40 bytes, RA is saved
at SP+36, and all four incoming argument homes are SP+40/44/48/52.

The function calls `func_151DCFD8(1)` until it returns zero, then publishes:

| Global | Recovered field |
| --- | --- |
| `D_800E0A20` | Request message-queue pointer |
| `D_800E0A24` | Low byte of the address argument |
| `D_800E0A28` | Request buffer pointer |
| `D_800E0A2C` | Signed request length |

It computes `(12000ULL * D_8002BD10) / 1000000ULL`, preserving unsigned
64-bit multiplication wrap before unsigned division. `D_8002BD10` retains
its existing `u64` declaration. The timer call receives `&D_80042A58`, the
computed count, zero interval, `&__osEepromTimerQ`, and `&D_80042A90`.
The signed `osSetTimer` result is returned to the caller.

The actual checksum caller already declares the four-argument signed-return
interface and stores the result in a volatile local. Two further original
call sites also store v0. A provisional void-return draft was rejected before
installation. No caller declarations or shared headers are changed.

The neighboring poller remains an uncredited zero-return placeholder. Giving
that placeholder a full parameter list changed its emitted code, so this
conversion preserves its existing unspecified forward declaration and body.
The signed polling-mode argument is independently checked against the original
callee contract. All neighboring machine code remains unchanged.

## Checked normalization

Three expected-word/binding guards account for two instruction-word changes:

- Offset `0x3C`: replace the compiler's word load from SP+44 with retail's
  byte load from SP+47. Only the low byte feeds the address-byte store before
  provider clobbers. The complete incoming address home remains captured.
- Offsets `0x68/0x6C`: normalize the low clock-word HI/LO bindings from
  `D_8002BD10 + 4` to its existing alias `D_8002BD14`. The LUI word is
  unchanged; the low-word load addend becomes zero. The 64-bit clock is not
  split or retyped to force a match.

Raw payload SHA-256:
`909077782d5b7404e0e012d7a0dbe04922b60491619d8ad2117f79ae7097e969`.
Normalized payload SHA-256:
`16850a0fffd7694ae2d957fb3b1b11fd53c94279de8ba6ff751aea404abdf656`.

Six invalid word/binding preimages are rejected by the actual padder. Two
invalid alias layouts are rejected. A 1,024-case byte-home identity check
supports the narrowing guard. All inherited guard bytes remain a literal
prefix; no existing row changes.

At the clock's low-word signed-carry boundary, literal GNU linking of the raw
object's shared-symbol HI/LO pairs mispairs the high-word load. This is retained
as an effective linker negative control. Raw rebase checks isolate that high
register pair under a symbol with exactly the same base address, without
changing raw instruction words. Original and normalized rebase checks retain
literal bindings. Universal literal raw-linker equivalence is not claimed.

## Qualification evidence

Receipts and artifacts are retained in
`conker/build/game-eeprom-request-timer-151DCEF0-match/`.

- Complete-owner, normalized-pool and actual Make checks pass with zero
  diagnostics. The one neighboring poller is unchanged. Three Make commands
  reproduce the qualified padded object.
- 1,296 guest cases / 3,888 executions cover all 58 original instructions,
  zero and repeated/noncanonical busy results, captured argument homes, high
  address bits, signed lengths, unsigned 64-bit wrap and timer-result forwarding.
  Original and normalized streams agree on complete modeled state, traces and
  fault context. Raw C agrees on public memory, calls and result; raw fault
  scheduling is not equated.
- 60 access-prefix cuts, including five branch-delay cuts, and nine independent
  rebases pass. Deliberately aliased clock/request linker symbols are guest
  machine extensions, not a portable-C aliasing claim.
- The complete original 56-word checksum caller passes 160 cases and stores
  the signed result at its SP+24. The other two original windows, 13 and 12
  words, pass 2,112 cases, including byte-address construction and result
  stores at SP+76/SP+24. All three aligned ROM JALs are accounted for:
  `0x344F0`, `0x348D4`, `0x34AD8`; no aligned literal function pointer occurs.
  The other two enclosing parent routines remain placeholders; their full
  execution is not claimed.
- Native SDK32 checks pass 65,536 cases per profile at O0/O2/O3 with UBSan,
  using disjoint typed globals and a four-argument signed-return function
  pointer. Independent shift/add multiplication and bitwise division provide
  expected results. Timer, queue and message canaries remain unchanged.
- The prepared 32-bit shared libgcc and loader are fingerprinted and reused;
  no runtime is installed. Native ABI validation is distinct from guest o32
  alignment validation. Twelve separate semantic mutations are effective in
  both IDO guest and native checks. Fixture/linker/compiler failures do not
  count as effective semantic controls.
- Eight fresh canonical checks and shared tools checks pass in both tools
  copies. Two installed checks rerun in each copy; six semantic checks are
  reused only under exact input/module/artifact and runtime fingerprints.

Polling, integer helpers and timer services are bounded providers. Synthetic
nonzero timer statuses qualify forwarding; EEPROM hardware acceptance and full
lower-provider execution are not claimed.

## Literal image and banking

The independent prediction accounts for exactly **411 changed bytes**:
188 target-code bytes, one function-extent byte, and 222 metadata bytes.
Seven closed permutations of named ELF symbol records and their strings are
explicitly predicted; all named values, sizes and attributes remain fixed
except the restored target extent. No image byte is excluded. Production
reproduces the first predicted ELF:
`53557b80979cc40da3e39ad2db57fe828903306b255bbad53e4986d0c8974364`.

All 6,055 other disassembled function bodies and all function addresses remain
fixed. Protected Game data remains byte-exact across 189,088 bytes and 720
owners. Inventory CSV is unchanged.

Tools commit `583732fd7631b8d484810b47cb6b368118c969e8` precedes the consumer commit. The old tools mirror's
inherited changes remain intact; no push occurs. Actual adopted-ELF recount:
**3,970 / 5,506 exact C (72.10%)**, Game **3,297 / 4,833 (68.22%)**,
Init 492/492 and Debugger 181/181, zero address drift and 1,536 still different.
The 75% target remains 4,130 exact functions, leaving **160** more.

The root README changes only its two aggregate rows. Graphify receives an
eleven-file structural refresh with all prior nodes and valid relationships
retained. The return type remains s32, so its prior return relationship stays
valid. No full-corpus extraction, global clustering or centrality claim is made.

Next screening candidate: `func_1514D564`. Private candidates remain uncredited.
