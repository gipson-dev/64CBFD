# 1764 - Actor slot refill guarded C match

Verified: 2026-10-28. Target `func_1512B53C`, owner `generated_157840`.
VA `0x1512B53C..0x1512B5FC`, ROM `0x1589EC..0x158AAC`:
48 words, 192 bytes, no frame, two HI16/LO16 bindings.

## Recovered source and original ABI

Replace the zero-return placeholder with `s32 func_1512B53C(u8 *actor)`.
Keep the canonical `s32 D_800BE628` declaration from variables.h: it holds a
32-bit guest table address. Read it as unsigned address arithmetic before
casting the selected count cell to `f32 *`. Shared headers remain unchanged.
The function and global retain their address-based names; local actor, index
and offset names describe the recovered operations without guessing a game role.

1. Read signed counter halfword actor+0x5FC. Zero returns zero before any table
   or destination-pointer dereference. Negative counters are active too.
2. Store state halfword actor+0x5F8 =1. Start index and byte offset at zero.
   While float(index) is less than the count float at the live table address
   plus unsigned selector actor+0x23D times 0x180 plus four, store marker
   0xFFFC through the live pointer actor+0x8BC plus byte offset. Increment index
   with explicit modulo32 arithmetic and unsigned byte offset by two.
3. Reread the selector, global table address, floating count and destination
   pointer for subsequent passes. Fractional positive counts round the number
   of iterations upward through the comparison; nonpositive and unordered
   counts make no marker stores. No count clamp or new bounds check is added.
4. Reread signed counter+0x5FC after the loop, clear float timer+0x60C to +0,
   decrement the counter with halfword narrowing, and return one. The counter
   store occupies the return delay slot. Writes may alias these live inputs.

The raw compiler C already preserves these semantics. An explicit inactive
label recovers the original early-exit block arrangement, reducing the first
44 linked-word differences to 21. The final source uses unsigned address,
index-update and byte-offset arithmetic to avoid signed arithmetic overflow.
All 48 retail words are retained; 47 are reachable. The redundant return-zero
move at +180 remains unreachable and intact.

## Register and scheduling normalization

This is a guarded match. Twenty-seven linked words need no changes; 21
expected-word guards normalize the compiler's address setup, independent
opening schedule, GPR value lifetimes and commutative add operand order.
There are no inserted or omitted words and no change to the normal O2/g3 profile.

A symbolic block proof covers the inactive gate, active prefix, empty-loop
exit, one loop step with arbitrary index/offset/destination, the taken backedge
and the untaken exit. Its expressions carry the complete prior write history
for every memory read. This prevents a cached value from masquerading as a
live read when storage aliases. The global-address/stride register swap and
temporary lifetimes close at the loop boundary; the return value, stack,
callee-saved GPRs and FPRs agree. Four changed-index, marker, bound-address and
reload-address controls are rejected by this proof.

The two global relocations move from compiler offsets +20/+32 to retail +4/+8.
The guards check both old words and old bindings, supply the exact replacement
bindings at their new sites, and remove bindings from the moved-from sites.
The inactive path only gains a caller-saved address calculation, with no new
memory access. Every other guard is checked against the frozen raw body.

Compiler raw SHA256:
~~~text
c45e1ddc7099ee0da0ded42e4fadcf94560a5d86ed7f8dd20ee80c6ea1003a34
~~~
Original/normalized raw SHA256:
~~~text
4b373b113fbb96a2431777810e14e0e12093004dd21ef16ab4ff9f726b498df6
~~~
Retail linked slot SHA256:
~~~text
d13b2f6391829834b46bf37cccae2e791cf709d1c59ca19a03339aefb957d19a
~~~

## Actual caller and fresh qualification

The aligned ROM census finds one direct JAL, at ROM0x15821C /VA0x1512AD6C
inside func_1512AD54, and no tail J or pointer literal. Its original 11-word
prologue/call/branch window supplies the actor in A0, preserves the caller's
float argument across the call, and branches to VA0x1512B0EC when this routine
returns nonzero. Fifteen connected cases verify both skip and fallthrough,
the saved actor register and the 0x70-byte caller frame. The current parent
remains its unchanged three-word C stub; this is original-window evidence,
not full parent recovery or gameplay acceptance.

Both tools copies pass eight fresh canonical methods and project-tool checks.
Installed copies each pass two fresh owner/image methods; the other six are
reused only after exact module, snapshot, seal and artifact identity checks.

- 576 raw-C/retail guest cases cover signed counter boundaries, every selector
  byte, integer/fractional/nonpositive bounds, negative infinity, signed zero,
  NaNs, and output aliases of the count, counter, selector, global pointer and
  destination pointer. Compare public memory, result, callee-saved registers
  and exact memory-access trace. Positive infinity is not a terminal fixture;
  no bound or termination guarantee is inferred for it.
- 260 fired access-prefix pairs preserve public partial memory and the access
  trace. Inactive counter tests need no mapped global or destination pointer.
  The raw schedules have different scratch registers and fault PCs, so those
  are not falsely claimed identical before normalization.
- Native32 O0/O2/O3 with trapping UBSan each pass 67,584 positive cases,
  including all 65,536 counter encodings and all 256 selector bytes. Storage
  uses typed actor, 0x180-byte setting and slot structures with whole actor and
  output fences. Seven wrong marker, gate, bound, decrement, clear, stride and
  return variants fail effectively. Overlapping float/pointer mutation probes
  are kept in guest memory rather than invalid native type-punning fixtures.
- Three GNU layouts pass 27 guest cases, preserve both moved HI/LO bindings and
  exercise signed low-half carry. The real padder reproduces the full object.
  Raw length/word/binding corruptions, all 21 incorrect guard expectations,
  a missing replacement relocation and an actual bad padder CSV are rejected.
- An actually compiled cached-bound control fails by value on a mapped count
  alias: retail stores one marker, leaving count bits 0xFFFC0000; caching 1.5f
  stores two markers, leaving 0xFFFCFFFC. The rejection does not rely on an
  unmapped access. Six complete-image corruptions are also rejected.

The first canonical run exposed an unqualified test-helper name, corrected
before the final full runs. A later diff check found two whitespace-only lines;
the final normalized tool file was requalified in both copies. Failed receipts
remain retained. All final checks pass with the required flags and gates.
Routine Claude calls: zero.

## Actual Make, strict image and measured progress

The owner has 15 compact functions and no GLOBAL_ASM routines. Preserve all
14 neighbors, their bindings and pools. The actual three-command normal
IDO/padder/GNU Make route and production reproduce the qualified object.
Selected, owner and actual-Make diagnostics are empty; production retains its
inherited duplicate generated_12D630 Make-recipe warning.

The complete adopted ELF equals the independently predicted 147-byte delta:
146 target-code bytes and one target-size byte changing 12 to192. There are
zero exclusions and no extra symbol/string permutation. All 6,056 function
addresses, 6,055 other bodies, named definitions, 720 protected Game-data owners
and 189,088 protected bytes remain unchanged. Map, inventory CSV, shared headers,
current parent and all inherited guard rows remain unchanged. Append only this
target's 21 checked rows.

ELF SHA256:
~~~text
09637b9c03ce34c02c38f08521e35fc9206900f4d25c99448849c87846e6c279
~~~
Native CRLF guard manifest SHA256:
~~~text
a8af4b342808530c29b95255b79b882169fb1f59b94d3365c0e1f0da9cf9a1cf
~~~

Seal 16,247 native/cache files and 245 focused inputs. The actual captured
native ELF recount retains the existing C inventory:

| Section | Exact C functions | Different | Drift |
| --- | ---: | ---: | ---: |
| Total | 3,842 /5,506 (69.78%) | 1,664 | 0 |
| Init | 492 /492 (100.00%) | 0 | 0 |
| Game | 3,169 /4,833 (65.57%) | 1,664 | 0 |
| Debugger | 181 /181 (100.00%) | 0 | 0 |

Only func_1512B53C becomes exact in this bank. The 4,130 threshold leaves
288 more to75%. Remaining shapes: 1,535 placeholders, 120 semantic/other and
nine unlocated. These source-shape screens do not qualify the remaining code.

Predecessor consumer221e0d71b5992fa36f63f9702c4d0ac0ce467a30 and tools
35c985f745fdc603ba3d123016dbb828b61c6729. Bank the tools first at
fbd822387d04651909d49bc63a8b02fda20573cb, then the C, checked guard rows,
tools pin and seven measured documents. Preserve the older mirror's 1,738
inherited dirty paths plus the two new files. No push. The root README changes
only its two aggregate matching rows; detailed function updates stay here.

Refresh ten changed structural C/Markdown/tools sources. Retain every old node
or unique relocation and every still-valid directed confidence/context key.
Validate the s32 return and u8 pointer parameter against the committed signature;
no return relationship is obsolete and no synthetic caller edge is needed.
Outside freshness, communities and global analytics remain historical. This is
a scoped structural refresh, not a full-corpus extraction. Detailed receipts
and the independent audit live under conker/build/game-actor-slot-refill-match/.

Next inspect func_1517B6E8 from a fresh predecessor. func_1514E920 remains
parked and uncredited. The 75% goal stays active.
