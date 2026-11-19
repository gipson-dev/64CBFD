# Attachment surface effect guarded byte match

Date: 2026-11-18. `func_150BABE0` replaces the zero-return placeholder in
`conker/src/game/generated_E8090.c`. The complete **259-word / 1,036-byte**
slot, VA `150BABE0..150BAFEC`, ROM `E8090..E849C`, is now byte-exact. The
original **208-byte frame** and **27 relocation sites** remain intact. Four
expected-word guards recover two private cached-angle homes; there are no
inserted or omitted instructions, changed profiles, or new assembly bodies.

Fresh production totals: **4,555 / 5,514 (82.61%)** overall,
**3,882 / 4,841 (80.19%)** Game, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and959 still different. **132 more** matches reach85%.
Conversion remains5,514/6,048(91.17%),86.19% of bytes. The85% goal stays active.

## Recovered behavior and interface

The interface is `void(actor, u8 selector, u8 context)`. The global
`0x9A0`-stride record field at `0x380`, scaled by `D_8009FE70`, is read and
truncated **before** the actor-null, inactive/type8, and missing-model gates.
Preserve that early global access. Selector0 chooses matrix attachment17;
selector1 chooses26. The extracted point's Y is replaced by actor+`0x180`
before gated command5/`0x4022` and the truncated coordinate event at Y+6.

The first angular effect uses sample*50+40, signed16 angle+60/angle-60,
unsigned RNG%11+30, kind5 and the context byte. A36-byte surface result and
Y+100/Y-100 probe gate the optional child. Its descriptor carries flags
`0x7340`, duration300, kind42, unsigned RNG%2001+2000, byte/color fields,
mode13 and flags`0x170002`. Three independent random words select its byte
and two-bit variant. Successful creation is appended to `D_80088750`; a
failed append deletes the returned record. A second angular effect always
follows, using sample*40+60, unsigned RNG%7+6 and kind6.

The original allocator's `memcpy` JAL has `addiu a2,zero,0x28` in its delay
slot at allocator+`0x94`; the descriptor really occupies **40 bytes**.
Only its first33 bytes are initialized here. The seven untouched tail bytes
are deliberately retained. The surface's vertices begin at+4. Helper calls
may mutate retained point/surface objects and globals; cached angles and
the REAL sample survive the relevant calls, while later point reads stay late.
The gated command's frozen provider returns a byte, deliberately ignored here.

An aligned full-retail census finds two direct JALs, ROM`9C5E4`/`9C614`, and
no aligned pointer literal for this target. Complete12-word callers
`func_1506F11C`/`func_1506F14C` read `D_800D154C`, pass selectors0/1 and
context255, and ignore the target return. Both caller bodies are literal in
production. Their higher-level parents remain outside this qualification.

Only selector low bytes0/1 have a defined recovered attachment index.
The two default-selector instructions at target+`0xA4`/`0xA8` read an
uninitialized retail home. They have static instruction/binding identity;
native tests make no semantic promise for those other selector values and
do not invent an initializer or default attachment.

## Four-word private-cache derivation

All source instructions except these four already match retail. The compiler
uses private low/high cache cells at SP+`0x40`/`0x44`; retail uses
SP+`0x44`/`0x48`. The frame, saved registers, exposed objects and all27
bindings are identical. The derivation changes only these displacements:

| Offset | Instruction role | Source slot | Retail slot |
| --- | --- | --- | --- |
| `0x1AC` | Store cached lower angle from A0 | `0x40` | `0x44` |
| `0x1B4` | Store cached upper angle from V1 | `0x44` | `0x48` |
| `0x3A4` | Reload upper angle into T1 | `0x44` | `0x48` |
| `0x3A8` | Reload lower angle into T2 | `0x40` | `0x44` |

The proof checks the closed set of accesses, no escaped pointer into either
private backing range, unchanged opcodes/registers, complete equality of the
derived259-word payload and relocations, and ordered guest memory traces with
these two cells identified by role. Both cells are inside a valid ABI frame;
outgoing helper arguments end below them and exposed objects start above them.
This is a qualified private-layout relation, not literal raw stack-byte
identity, a blanket address exclusion, or a hardware fault-semantics claim.

Raw source SHA-256:
`8749fb22399b3c202d4b778dd1bd4749a93068441fcd6b10134470a259e96367`.
The old guard CSV bytes are an unchanged prefix; exactly four rows are added.

## Validation and production audit

Both final tools configurations pass **five tests**, with zero failures,
errors or skips: **96.387s primary / 99.673s sibling overlay**,
and **317 imported tool fingerprints each**. The854-file overlay contains339
matching sibling files,507 primary fallbacks,seven task files and one empty
package bootstrap. The real sibling HEAD/status and343 dependency hashes stay
unchanged; conflicting sibling edits were never overwritten or claimed tested.

- Full before/after owner compilation preserves five neighbors and normalized
  pools. Both actual owner padders reproduce the entire slot, with12 GNU
  rebases,286 rejected instruction/binding corruptions and24 guard failures.
- **896 guest cases /1,792 raw-and-retail executions** agree with an independent
  semantic reference and the complete private-cache trace relation. All257
  caller-defined-path words are visited; the two uninitialized-selector words
  retain static-only coverage. Gates, mutable buffers/globals, full-word query
  status, unsigned RNG, creation/append failures and saved ABI are covered.
- **640 cases across both complete callers**, visiting all24 words, preserve
  arguments, ignored return, public memory and saved ABI. The complete50-word
  original constructor wrapper passes128 cases through all14 o32 arguments,
  allocation/initialization failure and deletion paths. Deeper services remain
  opaque. The unchanged26-word effect-helper ABI prefix from Note2554 reuses
  its128-case receipt by exact prefix/declaration/receipt hashes; it is not
  described as a fresh full-callee check.
- **448 SDK32 native cases each at O0/O2/O3**, strict aliasing, no fast math,
  and UBSan, agree with retail-checked transcripts. All12 semantic negative
  controls fail. Initialized integer descriptor fields are compared in guest
  byte order; native uninitialized pre-output bytes and the seven untouched
  descriptor bytes remain unspecified.
- Actual Make and the independent strict full-image predictor agree on
  **805 explained changed bytes**, no metadata alias groups and **zero
  exclusions**. Four image corruptions are rejected. Both configurations
  predict the same ELF; production really recompiles this owner, with no
  prebuilt object copied into production.

All **698 objects** are audited; only this owner changes. All **6,050 other
function bodies, addresses and extents**, five neighbors/pools and **189,088
protected bytes /720 owners** stay unchanged. Only source, guard CSV, owner
object and ELF among1,827 frozen inputs change. Conversion rows, original
assembly, shared headers, compiler inputs and Makefile stay byte-identical.
Production ELF SHA-256:
`41e89549a986711444e293da0b38a2b604dad7bb046ebd84f46a8369298c40ec`.

Two fresh installed checks independently compile all six owner functions/pools,
derive and compare the actual production body, and rerun896 guest and640
caller cases. Unchanged padder/rebase/guard/native/constructor/image receipts
are reused with fingerprints and are not called fresh installed reruns.
Production `match-progress` and `tools-check` pass. The existing duplicate
generated_12D630 Make recipe warning remains.

The first owner gate caught a copied test helper's no-unroll default changing
the existing damping neighbor. The harness now uses the owner's actual normal
O2/g3 compiler helper, and all five neighbors pass; no exclusion was added.
Earlier private native attempts exposed fixture endianness and the deliberate
other-selector compiler warning. The final fixture converts initialized fields
and scopes that warning to the caller-proven selector domain. An early suite
also lacked the report return value; both complete final suites pass after
that harness correction. On2026-11-19 the staged whitespace check removed one
extra EOF newline from the oracle, with identical Python AST. Both complete
final suites were resealed in final-primary-02/final-sibling-02 against the
exact final task fingerprints and installed inputs; source, guards, all compiled
functions and the production image remain identical. Historical outputs are
retained as diagnostics.

Root README changes only two aggregate matching rows. Graphify's native update,
scoped AST extraction, explicit target reference and old-ID retention are
recorded separately, with no forced shrinking replacement or full-corpus claim.
Routine work used zero Claude calls, no REA/WSL reconfiguration and no host,
Release, save or capture changes. Tools are committed before their consumer;
no automatic push or pause.

Next inspect **func_150BAFEC** in this same owner: still a zero-return
placeholder, VA`150BAFEC..150BB260`, **157 words /184-byte frame**.
Freeze its caller/provider evidence against the newly committed baseline before
drafting. No next-target candidate or additional matching credit is claimed.
