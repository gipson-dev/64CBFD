# Dual Random Point Direct C Match

Date: 2026-10-20. Consumer predecessor: `2cf1656e`; tools predecessor:
`5092f17`. Tools **12b5844** are committed first. No push.
The **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_150F7F8C`'s false zero-return placeholder in
[generated_124920.c](../../conker/src/game/generated_124920.c) with its complete,
purpose-commented dual-submission wrapper. Keep the address-based name and
use the existing `struct17` point type, a byte selector and a full word parameter.
VA **150F7F8C..150F802C**, ROM **12543C..1254DC**.

All **40 executable words / 160 bytes** emit directly from normal **IDO O2/g3**,
with the original **48-byte frame** and **four R_MIPS_26 bindings**. There are
**no new guards or compiler-profile changes**.

The wrapper itself obtains two independent float RNG results. Save the first
across the second RNG call, then submit:

```text
func_151541B8(point, 3*first+9, float_bits(3F030C35),
             70*second+70, 0.0f, selector, parameter);
func_151D3F14(point, selector, parameter);
```

Both expressions retain separate single-precision multiply/add rounding.
The exact constant is **0.5119050145149231f**, not an approximate replacement.
Inspect both complete original helper interfaces before declaring them:
the first returns a pointer or NULL; this wrapper discards that result and
must still call the secondary helper. The inspected direct-call windows
do not consume a wrapper return value.

Reload point/selector/parameter for the second submission after the first
provider returns. Preserve point identity and live point contents, not a copy.
The incoming homes are **SP+0x30 / +0x34 / +0x38**; the big-endian selector
reload is **SP+0x37**.

## First RNG Home

The first straightforward C draft already had 40 words/frame48 and only two
differences: its first float store/load used **SP+0x2C**, not **SP+0x28**.
Declare the used `second` local before the used `first` local, then obtain
the samples in their original order. This recovers the complete retail
instruction stream, including the first-result store in the second RNG call's
delay slot. Neither local is dummy padding, and no physical-register binding
or stack-word normalization is introduced.

The tests verify the first home at entry to the second RNG provider, before
that provider destroys caller-owned GP/FP registers. They also pin the literal
store/load words and preserve the original argument reload schedule.

## Qualification

[The focused helper](../../tools/experiments/game_dual_random_point.py)
freezes 13 source/header/assembly/image/build inputs without advancing any
historical input hashes.
[Eight tests](../../tools/tests/test_game_dual_random_point.py) pass in both
tools copies, with no errors, failures or skips:

| Stage | Primary | Standalone Mirror |
| --- | ---: | ---: |
| Before installation | 31.633s | 28.684s |
| Installed source | 50.067s | 36.243s |

- **515 cases / 1,030 complete original-versus-C modeled phases** compare all
  modeled state and independent seven-/three-argument packets. Execute all
  **40 target words**. Include asymmetric RNG samples, signed zero, subnormal
  and finite larger/negative samples, selector/full-word edges, both stack
  alignments, point changes during providers and NULL/non-NULL first results.
- **512 native32 cases**, O0/O2/O3 with trap UBSan and FP contraction disabled,
  check independently precomputed float32 results, exact constant bits,
  provider order, unchanged point identity, live contents and byte fences.
  Three incoming argument-home redirects are explicitly guest-only probes,
  not portable C alias semantics.
- **Ten compiled semantic negatives** all reach rejection code23: one RNG call,
  mixed-up sample dependencies, wrong offsets, a one-ULP constant change,
  wrong extra float/selector, a narrowed parameter and skipping the second
  call when the first result is NULL.
- Scan every pristine function for direct JALs and the ROM for literal target
  pointers. Both direct sites are in **func_150F78B4**, at **150F7A58** and
  **150F7AF4**. Execute their actual nine-word windows in **88 phases**:
  **44 active and 44 gated off**, with **176 fired join boundaries** across
  original/C runs. Verify the real argument-byte delay loads, branch-likely
  effects, first site's byte clear and second site's AT restoration.
  The full large parent remains unrecovered/unexecuted by this checkpoint.
- Three independent GNU call-symbol rebases pass **54 phases**, preserving
  all four bindings and the complete original/C words and packets.
- Execute the original first helper's duration-reject path in **18 phases**.
  All **18 reachable gate/epilogue words** execute, return actual NULL and
  still reach the second submission. These deliberately chosen finite
  negative/zero durations are not a claim about normal RNG range.
- Execute the complete original **56-word secondary helper** in **78 phases**.
  Check unsigned integer RNG modulo counts **4..6**, modes **20..32**,
  word-before-output coordinate truncation, selector/parameter forwarding
  and its lower emitter's eleven arguments. Compare defined descriptor fields;
  do not claim initialization of its unused padding.
- The complete first **221-word** helper is inspected, but its positive factory
  and FCSR conversion path are **not executed or claimed**. The secondary
  helper's lower emitter remains a bounded provider. Full PRNG-state evolution,
  hardware/FCSR/MMU, malformed memory and gameplay/host acceptance remain open.
- Seven strict-image negatives reject unrelated header/code/data, target size,
  truncation and appended bytes. Both shared tools checks pass.
- The two task files agree across tools copies and all four Python files parse.
  Preserve all **1,492** older mirror dirty paths/statuses/hashes and its
  **ddbdd16** HEAD. Add only these two absent task files, leaving **1,494**
  dirty paths; do not commit/reset that older mirror.

## Production And Progress

Preserve all **16 other raw/padded owner functions**, bindings, pools and
normalized inherited diagnostics, including the existing GLOBAL_ASM routine.
The actual Make path has **five productive commands**, normal O2/g3 and
qualified padded code/metadata identical to the direct helper output.

Production passes in **188.035s**, reproducing the strict independent first-link
prediction exactly: **128 changed bytes**, comprising **127 instruction bytes
plus one symbol-size byte**, target extent **12 -> 160**. There are **zero
metadata exclusions**.

All **6,055 other linked bodies**, **6,056 addresses** and **189,088 protected
Game-data bytes / 720 owners** remain fixed. ROM, original assembly, shared
headers, the entire guard manifest, Makefile and progress CSV stay byte-identical.
The inherited duplicate generated_12D630 Make warning remains.
Unchanged broader suite receipts are reused through this strict source/image
proof, not represented as fresh reruns.

ELF SHA-256:
`1ee5a6a85d7164f5d38185dd99f434d3abb6aafb9ae6da8f4b37aebe78c9292a`.

Fresh full matcher: **3,705/5,505 exact (67.30%)**, Game
**3,032/4,832 (62.75%)**, **1,800 different / zero drift**. Init remains
492/492; Debugger 181/181. Converted counts/bytes are unchanged.
The present 75% threshold is 4,129: **424 more matches**.
Refresh the ELF-pinned remaining queue: **1,666 placeholders,
125 semantic/other definitions and nine unlocated entries**. It remains
triage, not permission to install unqualified source.

Next **func_151220D0**, VA **151220D0..15122170**, ROM **14F580..14F620**:
**40 words / frame40**. Qualify its +0x36C descriptor pointer/halfword mask 0x4
gate, temporary vector and post-helper displacement reads, length and
+0x37C/+0x39C stores, exact D_800A3460 scale, unconditional finalizer, helper/
caller interfaces and full owner/image. Its record extends beyond struct127;
do not assume that partial actor layout. It remains **queued, uninstalled,
without a draft or matching credit**. Keep `func_1508CAD8` queued too.

Root README receives aggregate rows only. Commit tools before the consumer
pin, with no push, then verify the existing graph hook's terminal processes
and old-node retention in the ignored final checkpoint. No host source,
real save/configuration or frozen Release artifact is changed.
