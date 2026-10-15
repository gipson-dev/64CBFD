# Packed Fade/Scale Callback And Renderer Deferral

Date: 2026-10-15. Continue the whole additional-source / Game matching goal.
Predecessor consumer c43adf8c, tools 6ee5fbe; both active trees initially clean.
Keep the archive read-only, independently dirty tools mirror intact and host
Release frozen. No push, host build/launch or Claude invocation is authorized
or performed by this checkpoint. Standing user authorization: keep committed.

## Renderer Audit Before Adoption

The previous handoff selected func_1516D738: VA 0x1516D738, ROM 0x19ABE8,
153 words / 612 bytes, frame 0x98, owner generated_19A8B0. Inspect all retail
instructions, the archive body, the texture cache/provider/packet writer and
the final projection helper before compiling an archive replacement.

Measured retail control flow:

- Instruction 0x1516D740 copies the second argument to S0; the first remains
  the incoming display-list cursor. The prologue homes the third argument.
  The archive's two-argument void declaration is not an established ABI.
- Texture mode 5 selects mode 2, all other tested modes select mode 1. If
  D_800DD1BC already equals that mode, branch 0x1516D7EC jumps to 0x1516D86C.
- Only the mode-miss branches write sp+0x5C: zero at 0x1516D818, or 0x100000
  at 0x1516D848. The shared instruction 0x1516D874 reads this word before
  calling func_15142FBC. The cache-hit path has no dominating local write.
- The actual texture chain is func_15142E24 -> func_15094FE8 ->
  func_15095060. The last routine's attachment write is at attachment+0x10:
  the packet begins at sp+0x84, so that write is sp+0x94, not sp+0x5C.
- The final func_15095760 reads the supplied coordinate packet and returns
  a display-list cursor; it cannot initialize an earlier mode argument.

Execute 24 bounded original-code cases through the actual 102-word cache,
30-word wrapper and 29-word packet writer. Vary both texture kinds, both mode
cache states, both texture-cache states and three private word seeds. Every
mode hit forwards the inherited sp+0x5C bits into the render-mode argument;
mode misses overwrite them. Check the actual packet write at sp+0x94.
Image selection, low-level texture submission and final render/projection
providers remain opaque. This is positive bounded evidence, not an assertion
about every possible provider, stack history or complete gameplay outcome.

The archive also leaves its sp5C C local uninitialized. Do not initialize it
to zero, infer the mode from a cache, or adopt an undefined C read to obtain
matching credit. Leave func_1516D738's current placeholder unchanged and its
C recovery open. A future original-assembly preservation step would be a
separate, honestly assembly-classified change, not a C match.

## Callback Recovery

Recover func_1516ECAC instead: VA 0x1516ECAC, ROM 0x19C15C, 47 words / 188
bytes, a leaf with no frame, same owner. It is entry 1 of the real nine-entry
D_8008CBA0 callback table used by the already recovered func_1516D678.
Keep the address-based symbol name and add comments describing measured work.

The archive is a behavioral lead, not usable byte-exact C: word operations at
byte offsets and an unsigned-byte accumulator lose the retail live 32-bit
arithmetic. Recover byte fields and a signed word accumulator:

- A nonzero record[0x24] raises intensity by delta*128 unless already 255;
  wrap as a word, then apply the signed upper clamp. Store only the low byte.
- A zero countdown lowers a nonzero intensity by delta*record[0x26]; wrap
  before the signed lower clamp. Retain the full live value after the store.
- Return exactly 1 only when the freshly read countdown and live value are
  both zero. This selects the updater's binding clear and removal path.
- Otherwise combine bytes 0x2C/0x2D as an unsigned 16-bit scale, multiply
  modulo 2^32, shift the signed product by 7 and write both halfword extents
  at 0x16 and 0x14. Return zero. Explicit unsigned intermediates avoid signed
  overflow and negative left-shift undefined behavior.

The initial complete semantic body emits 47 words / 14 differences. A bounded
20-shape expression/local screen reduces that to three. Raw C remains three
words different, not a direct compiler match. The production guard append is
limited to offsets 0x48/0x4C/0x50: exchange T8/T9's independent delta/byte loads
before the unchanged commutative MULTU. Move the actual LO16 relocation from
0x50 to 0x4C; retain the HI16 relocation. The entire raw text hash and all four
relocations are pinned. No fake volatility, profile change or semantic guard.

## Focused Qualification

The first eight checks pass in 13.596 seconds before the full linked rebuild:

- 6,144 guest cases cover every intensity byte, word wrap and signed clamps,
  zero/255 bypasses, stack-backed records and a delta/intensity storage alias.
  Compare guarded code to every retail word/register/access event; raw C to
  the independent memory/return/write model. Raw operand read order differs,
  so do not claim raw retail guest-fault order.
- 130 paired, actually fired access-fault prefixes compare guarded and retail
  state at both stack phases. This qualifies emitted guest order only.
- Native32 invokes the actual selected C at O2 and O0, 8,192 cases each,
  comparing complete canary-backed storage and return values. Six compiled
  negative controls must fail both guest and native public-state checks.
- A proposed logical-vs-arithmetic final-shift negative is correctly rejected
  as ineffective: the difference lies above the stored halfword. Replace it
  with a wrong shift count. No production behavior or acceptance is relaxed.
- Independently assemble the complete original function for three text/delta
  rebases, including signed-low carry boundaries, then execute the result.
- Execute 256 real updater/callback/cleanup cases, using real table entry 1.
  Compare complete record/binding storage and call order: 2 removals and 254
  active records. The callback is real code; lower unlink/destructor providers
  remain bounded opaque hooks. Full gameplay/host acceptance is not claimed.
- Retain all 29 other owner's raw bodies, extents, relative relocations and
  normalized pools. Exercise the actual production generated-owner padder.
  Reuse unchanged earlier broad-suite receipts explicitly, not as fresh runs.

Tool entry points: tools.experiments.game_packed_record_scale,
tools.tests.test_game_packed_record_scale, its ROM-free _candidates suite and
its independent _installed suite. Ignored fixtures/receipts are under
conker/build/game-packed-record-scale/. Pin all 49 scoped inputs before edits.

## Complete Linked Image And Progress

The normal ELF/progress build succeeds after the guard dependency's broader
generated-owner/SDK rebuild. Known duplicate generated_12D630 recipe warnings
remain. Independently construct the expected complete ELF from the pinned
predecessor, the 188 retail bytes and symbol extent 12 -> 188, with zero
metadata allowances. The installed 3,257,636-byte ELF equals that image:
exactly 135 changed bytes, target slot/extent only. Every other ELF byte and
all 189,088 protected bytes / 720 owners remain fixed.

| Input | SHA-256 |
| --- | --- |
| ELF | 3cda1ab024db3e37886dd08677ad6adfca63b2bdcee416a41de4f794f3e87615 |
| Owner | e36a92072fa2bbbfde29af0110c8bc2206848dc803569e40927656ac49a98eb1 |
| Guards | e48ca462691e03b724b1dfae8542e4a592826157a755bd4dcc62851a00830491 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Compare all 49 scoped inputs: three changed, 46 fixed. Retain every byte of
the prior guard prefix, appending only the three relocation-aware rows.
The independent installed-image check uses no checkpoint inverse.

Fresh matcher: Game **2,894/4,828 (59.94%)**, total **3,567/5,501 (64.84%)**,
different **1,934**, zero address drift. Init stays 492/492 and Debugger 181/181
exact. Conversion counts/bytes remain total **5,501/6,044 (91.02%), 86.04%**,
Game **4,828/5,323 (90.70%), 85.41%**. This was an already-C-classified stub:
one more exact body, not another converted function. Keep the ignored progress
CSV untracked. Root README changes only its two affected aggregate rows.

## Next Work

Continue at **func_1516E778**, the still-stubbed 85-word preset wrapper at
ROM 0x19BC28 in this owner. Its archive body provides five inputs and a call
to the now-recovered 49-argument func_1516D99C. Re-establish the true argument
widths, packed coordinate extraction, call packet, stack frame and active
compiler shape; do not repeat the archive's unjustified arg1 narrowing.
The wrapper has not been compiled or qualified by this checkpoint.

Keep func_1516D738's C recovery, the wider additional-source/Game queue,
handwritten Init hardware routines and func_1510BF60 open. A narrower callback
match does not complete the whole goal or establish full-game/host parity.

## Banking Gates

Bank tools **94c4245** before the consumer pin/source/guards/docs. All 14
installed checks pass in **123.060 seconds**, including complete image/input
corruption checks and all **801 original archive fingerprints**. The added
checkpoint/capture integrity check passes separately in **0.765 seconds**;
unknown/corrupt paths and each before/after capture are rejected. Current
image and real lifecycle acceptance do not use the exact-input inverse.
Shared tools checks and native Windows syntax for all five new files pass.

Preserve sibling tools mirror **ddbdd16** and all **638 initial dirty
fingerprints**; copy only five absent owned paths after checking that complete
dirty set and HEAD, then verify all **643 final fingerprints**. Standalone
five-file syntax and all three ROM-free candidate checks pass. Do not commit,
reset or copy history into this older mirror. No push or host/Release action.

The full Graphify update refuses **19,341 nodes against 41,115 existing**,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve that
fail-closed result and await the incremental commit worker rather than force
the smaller scan. The tools checkpoint is complete; consumer/post-bank
verification is recorded below when finished.

## Post-Bank Verification

Consumer **c899b74f** banks the semantic callback, three guards, tools 94c4245
pin, README aggregate rows and working documentation. All **15 post-bank
checks pass in 45.794 seconds**, including the independent complete current
image, all 49 input states/corruption controls, exact-input checkpoint gates
and fresh hashes for all 801 archive files. Normal ELF/progress build is up
to date. The raw three-word mismatch is still explicit; only the guarded
47-word linked slot is retail-exact.

Both active checkouts are clean before this receipt. The older mirror's
independent ddbdd16 HEAD and all **643 final dirty fingerprints** remain fixed,
including every one of the 638 initial paths. Seven documents / **4,960
relative Markdown links** validate with zero broken. The source commit's
incremental graph worker finishes at **41,125 nodes / 81,222 edges / 3,803
communities**, preserving the refused smaller full scan without forcing it.
No push or host/Release action. Continue the whole additional-C / Game goal
at func_1516E778, keeping the renderer's inherited-stack C deferral open.
