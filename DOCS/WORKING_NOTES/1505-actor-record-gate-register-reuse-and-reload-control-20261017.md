# Actor Record Gate Register Reuse And Reload Control

Verified 2026-10-17. Consumer predecessoref009915; tools predecessorf983786.
Both active trees began clean. The preceding turn was progress: it established
the shared expression-image association before global passes. This turn
observes the actual lookup/emission path and rejects a reload-only control.
No function is installed and no new matching credit is claimed.

Continue func_150F2A60, generated_11FF10, asm/11FF10.s,
VA150F2A60..150F2C8C /ROM11FF10..12013C,139 words/frame0x40.
The uninstalled baseline stays137 words/120 full-slot differences. Preserve
the separate rejected135-word prolog control from Note1503.

## Common Lookup And Actual Reuse

Reuse the unchanged normal frontend transport, full-owner adapter, image
probe and complete code/function/relocation/pool validator. One new normal
O2/g3 capture adds four read-only native probes in the owned UOPT child:
isearchloop0x455FA0, inreg0x41F0D0, emitter0x438260 and uwrite0x42BC00.
The exact cc/cfe/uopt/ugen fingerprints, procedure760, fired events, all four
child exits/driver exit0 and final null inferior are mandatory.

The live observations connect the opening loads all the way to emitted ucode:

- Both distinct load nodes call isearchloop with hash148, the same address
  operand image269150112 and null second operand. Both return image269150064.
  Return site0x458A05 is inside the observed exprimage routine. These are
  dynamic identities, checked relationally rather than hard-coded as pointers.
- The first node is visited twice by the emitter: first to materialize its
  value, then to evaluate the initial pointer predicate. The second node is
  visited once for the byte-address expression.
- The first visit emits one address-type static load of block747, length4,
  offset0, followed by an address-type register store to hardware GPR2.
- The next two visits each emit a register load from **GPR2**, including the
  second original source-load node. All three relevant inreg calls succeed
  with allocation color1. Color1 and hardware GPR2 are separate observations,
  not interchangeable numbering schemes.

Thus the missing second memory read is observed as actual register reuse, not
inferred solely from a common image or a final instruction count. Normal
frontend/optimized wire loads remain2/1. There is no compiler-decision patch,
diagnostic optimizer option or numeric debug-timing claim.

The public [UOPT image lookup](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptitab.c)
and [emitter](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptemit.c)
were navigation references only. That project targets IDO7.1 according to its
[README](https://github.com/n64decomp/ido/blob/master/README.md); its structure
layouts are not authority for the local5.3 binary. No external code/compiler
was installed or copied into production. The local native observations above
independently establish the conclusions.

## Reload-Only Control Is Not A Restoration

A single scratch control makes only the pointer variable declaration volatile,
preserving the complete semantic body and all other declarations. This is
explicitly a forced-reload diagnostic, **not** a recovered historical qualifier
or an installation candidate. Do not promote it because its length agrees.

It emits139 words/frame0x40 and restores two opening memory reads, but still
has **134 different words**, six saved GPRs instead of retail's five, and a
private-state mismatch at **fault cut0**, before the first memory access.
Its address work is hoisted before the first save. Raw SHA-256:
`714d6725c2f8ba805cf3d1921e8f888ed21affa7b8864a78e6598aa10a14cd99`.

The normal baseline's raw SHA remains
`28c65059860b7a8f40b59166beecbfbe9fecf1c6b7b392a130d9a74d42dcf125`.
All11 copied neighboring routines and normalized owner pools agree between
the normal and control objects. The original source's qualifier/profile and
the independent actor-address rematerialization remain unrecovered. Fixing
the gate read count alone is demonstrably insufficient.

## Qualification And Bank

Four fresh tests pass in20.278s. One normal captured compile preserves all
code, function boundaries, relocations and data/literal pools. Forty-one
effective provenance controls reject wrong identities, lookup operands,
register availability, emitted records, nesting or missing events; five
child/driver exit-code controls reject incomplete lifecycles. All ten native
probes are removed on UOPT exit, with no pending finish probe/active emitter.

The rejected control passes960 public core cases,400 sparse/provider-mutation
cases and12 actual28-word lookup/six-word byte-offset-setter paths. Its initial
read counts are retail/normal/control2/1/2. These checks do not repair the
cut0 counterexample or establish portable fault/concurrency semantics. Earlier
native32 and full recovery receipts are reused, not fresh qualification.

All253 protected entries /233 paths remain unchanged. Production ELF remains
`f56e3591c3c86189f630e4b8d599d8cfd7920165766e0c309a310970cd12ba6a`.
No production source/guard/data/CSV/README change or rebuild is claimed.
Unchanged totals: Game2,962/4,828 (61.35%), total3,635/5,501 (66.08%),
1,866 different and zero address drift.

Tools **8a5bfb6** banks the experiment/test pair before the consumer docs/pin.
Both tools copies pass12 shared tests and smoke checks; four ASCII/AST parses
and two exact task pairs pass. Preserve all1,122 pre-existing mirror hashes,
1,124 dirty paths and mirror HEADddbdd16b. No mirror commit/reset, push,
new Claude call, host operation or frozen Release action. Finish the owned
consumer Graphify rebuild before closing.

- [x] Connect both gate-load nodes through common lookup to actual GPR2 reuse.
- [x] Reject the139-word reload-only control using full words/private state.
- [x] Pass focused/public/provenance controls and preserve production/mirror.
- [ ] Continue this same func_150F2A60 with the independent **block752 actor
  address rematerialization and saved-register pressure**. The prepared
  compiler's opening reuse mechanism is now observed; do not repeat these
  lookup/emission probes or treat volatile forcing as a recovered source fix.
- [ ] Recover all139 words and full private/relocation/linked-image behavior
  before installation. Keep both fade lifetime gaps and wider Game open.

```sh
python3 -m tools.experiments.game_actor_record_gate_expression_reuse
python3 -m unittest tools.tests.test_game_actor_record_gate_expression_reuse -v
make tools-check
```
