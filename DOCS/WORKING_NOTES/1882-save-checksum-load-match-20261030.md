# Note 1882: save checksum reader match

2026-10-30. `func_1500727C`, owner `game_33990`, replaces its zero-return
placeholder and obsolete prototype with `void func_1500727C(void)`. Its complete
**57-word /228-byte body** at VA `0x1500727C..0x15007360`, ROM
`0x3472C..0x34810`, is byte-exact after ten expected-word/relocation guards.
No instructions are inserted or omitted, and there are no alignment words.
The existing O2/g3/mips2/o32 profile and shared headers remain unchanged.
Tools commit: `bf5976204f8586f224c56c9e08baf4b6bc05b90e`.

## Recovered read and validation

Call `func_151DD3A0(&D_800BE900, 0x44, D_800BE2F0.bytes, 0x70)` to request the
112-byte block. Then compute the unsigned 16-bit checksum:

`204 + 4*bytes[2] + 8*bytes[3] + sum(bytes[i] * 2^(i mod 4), i=4..103)`.

Compare it with the block's unsigned 16-bit header. On mismatch, call
`func_15007168()`. The routine ignores the transfer result and validates the
buffer left by that helper, including after a partial read failure. Bytes
104..111 are transferred but excluded from this checksum. The source reuses
the existing `SaveBlock33990` union and its neighboring checksum writer's
field names; the new comment describes the mismatch-handler call.

The frame is 24 bytes with RA at SP+20. There is no result home or defined
return value. The original caller passes no arguments and follows the JAL
with an unconditional branch, corroborating the recovered void interface.
The native tests retain the real SDK queue and block layouts: 24 and112 bytes.

## Guard scope and equivalence

The raw C is already57 words and differs at nine instruction words. A tenth
guard checks a binding-only change. The guards cover these closed groups:

| Byte window | Difference |
| --- | --- |
| `0x48..0x54` | Independent move/address setup and `D_800BE2F0+4` versus `D_800BE2F4` |
| `0x64..0x6C` | Independent next-index and mask scheduling |
| `0x80..0x90` | Independent index-mask and accumulation chains |
| Word49 /`0xC4` | Swapped operands of the same equality branch |

Four GNU-linked layouts prove identical operation multisets and final symbolic
expressions for all32 registers in every register-only window. These windows
contain no memory or control operations. The final branch retains its opcode,
displacement and likely-delay behavior; equality is commutative. Rebases preserve
the required block aliases at base+2/+3/+4/+104, including signed-low-half carries.
Twenty actual padder controls reject altered expected words or bindings.
This is a normalized match, not direct raw-C identity.

## Original helpers and independent qualification

Ignored evidence: `conker/build/game-save-checksum-load-1500727C-match/`.

- **1,698 guest cases /5,094 executions** compare original, raw C and normalized
  code against independent public-memory, protocol and observation expectations.
  Complete cross-image RAM, registers and access traces agree. All57 target
  words, all45 original transfer-helper words and all69 original defaults-helper
  words are exercised.
- The original transfer helper polls `func_151DCFD8(1)`, then calls
  `func_151DD140` in eight-byte chunks at blocks68..81. Bounded providers supply
  busy scripts0/2/3 and failures at chunks0/1/7/13, with both write/no-write
  failure effects and nonzero signed/unsigned error words. The original loop
  controls the requests and stopping behavior; hardware I/O is not performed.
- The original defaults helper uses its verified ten-entry retail jump table.
  It clears exactly104 bytes and updates ten records through `D_80082BBC`.
  Independent reference expectations cover both the save-payload destination
  and a separate allocated record bank, including fields untouched by defaults.
  The transfer helper is already recovered C and remains unchanged; the defaults
  helper remains a placeholder. Neither helper receives additional credit.
- **210 root access cuts**, including one delay-slot cut, preserve exact state
  and actual PC/delay context. **36 rebase cases** use three complete symbol
  layouts and retain the block aliases. These checks qualify emitted instruction
  order, not portable C faults, asynchronous device timing or hardware acceptance.
- The sole aligned JAL is ROM`0x49B64`, VA`0x1501C6B4`; there are no aligned
  literal pointers. Its original four-word window in `func_1501C57C` passes
  **74 cases**, reaching the original exit at`0x1501C6EC`. The parent remains a
  C placeholder; its dispatch logic and complete execution are not claimed.
- Native32 **O0/O2/O3 each pass524,288 cases** with trapping UBSan. All65,536
  seed-byte pairs run through the full-read path with both comparison outcomes.
  Additional modes cover partial reads, helper mutations, separate default
  destinations, complete block bytes and canaries. Helper arguments and call
  counts are checked. All13 compiled controls are effective in both IDO/guest
  and native tests: weights, sign, constant, shift, short/long range, comparison,
  missing defaults, command, transfer length, checksum-before-read and incorrect
  early return on a transfer error. Build/interpreter failures do not count as
  successful semantic controls.
- Both tools copies pass eight fresh canonical checks and shared checks.
  Production repeats two fresh installed checks per copy and reuses six unchanged
  checks only under full input/module/artifact fingerprints. The tools commit
  precedes the consumer commit. All2,084 inherited mirror dirty paths and its
  existing HEAD are preserved; only three qualification files are added there.

The reader declaration is checked against the recovered helper definition:
`s32 func_151DD3A0(OSMesgQueue *, u8, u8 *, s32)`. The buffer argument uses
`D_800BE2F0.bytes`. A final cross-file review caught the earlier broad declaration;
correcting it leaves every raw instruction, binding, padded byte and ELF byte
unchanged. Both tools copies were requalified with the corrected native model.

## Owner, image and progress

All **17 owner neighbors** and pools remain fixed. The actual ordinary-owner
three-command Make recipe reproduces the padded object through `pad_c_object`
and `retail_layout.us.txt`. Target, owner and command diagnostics are empty.
Inherited duplicate-`generated_12D630` warnings remain in the dry-run plan.

An independent literal whole-image prediction equals the private first link
and adopted production ELF: **191 changed bytes =190 code +1 symbol extent**,
metadata0, exclusions0. All **6,055 other bodies** and all **6,056 addresses**
remain fixed. Protected Game data stays exact across **189,088 bytes /720 owners**.
The C inventory CSV and every inherited guard row remain unchanged.

Raw C SHA-256: `14d322a6fac76024c350909f5e26a2b9541220396b973debf8c03b15918f251c`.
Owner source SHA-256: `f52911f4db46b28290bdc3de151cee407689b3a8c11fb1d2c270613ab61c1046`.
Padded owner SHA-256: `3a9368f1300ec6a23a2fcc3cdf2cd7d0bf114cf3ff877ace9379fe3cce1a2d5a`.
Adopted ELF SHA-256: `58a5a898ef75c86e09bd60e0830990f8f99c7d227283784e6edb320cc3fc493b`.

Fresh recount: **3,959/5,506 (71.90%)** total exact C and **3,286/4,833 (67.99%)**
Game, zero drift. Init remains492/492 and Debugger181/181. The75% goal stays
active: **171 more** matches are needed for4,130/5,506. Next private screen:`func_150ECA68`.
The root README changes only its two aggregate matching rows. Graphify uses the
eleven-file scoped AST refresh with old-node and valid-relationship retention,
retiring the obsolete placeholder return-type edge. No full-corpus extraction,
global clustering, whole-game or hardware acceptance is claimed. No push or pause.
