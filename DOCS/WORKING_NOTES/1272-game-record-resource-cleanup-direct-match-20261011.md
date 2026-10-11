# Game Record Resource Cleanup Direct Match

Date: 2026-10-11. Complete func_1503DD1C, owner
conker/src/game/generated_6A3D0.c. Body VA 0x1503DD1C..0x1503DDC8,
ROM 0x6B1CC..0x6B278: 43 words / 172 bytes. The retail-layout slot
extends to VA 0x1503DDD0 / ROM 0x6B280: 45 words / 180 bytes,
including two trailing NOPs. All body words emit directly from semantic C.
No new guards, profile or recipe changes. Wider Game goal active.

## Baseline And Contract

Consumer 8ebaf3b5bb7431a97a7033b00ba9efdd2de2111e and mounted tools
0e3d5204ceb3ad699e182eadc84e14ad6ba592a0 were clean at entry.
[Note 1271](1271-game-group-publication-propagation-direct-match-20261011.md)
banked the 56-word group propagation leaf. Cleanup was the final zero-return
placeholder in this owner and remained a bounded parent-chain hook.

Native Graphify query, complete retail instructions and the direct
func_1503CF20 caller establish void (s32 identity), not zero status.
The failure branch calls cleanup after the optional D_800C6360 free,
then separately reloads/frees/clears D_800C5C08, D_800C6070 and D_800D19A0.
The incidental V0 value is not a C return contract.

Read the initial unsigned halfword D_800C5628[identity]. Zero count
does not read the D_800C5338 slot or any record. Cache both slot addresses,
but reload the live record-table pointer each iteration. Advance by 12 bytes.
Skip a record whose current word is exactly 0x80000000 without reading
its source word. Otherwise skip current==source; call func_1510D7AC with
the source word as a resource identity, not the current word or a heap pointer.
Reload the live count only after a call; skip paths retain the cached count.

Preserve original 0x30 frame, RA at +0x2C and S0..S4 at +0x18..+0x28.
Both branch-likely skip delays increment the record index. The loop-back
delay advances the byte cursor by 12. Do not add bounds, NULL-record,
helper-status or signed-count gates. The caller ignores cleanup's result.

## Direct C Shape

The natural word-index expression emits 44 words with 24 differences:
a multiplication-to-word-offset step leaves an extra shift in the loop.
Casting the table pointer to u8 and adding index*12 emits the complete
43-word body directly under both owner no-unroll and retail profiles.
The compiler preserves the retail count caching, live base reload,
short-circuit skips and call-aware reload. No guard normalization needed.

The final six-source/two-profile sweep completes all 12 measurements:
selected, record-first and separate-current each 44 words / 24 differences;
byte-offset 43 / zero; split-skip 46 / 46 with frame 0x28; signed-word
44 / 25. The direct shape has frame 0x30, zero diagnostics and zero pools.
The experiment defaults to the qualified byte-offset body.
Only the body, forward void/s32 prototype and release declaration change.

## Qualification

New tools: experiments/game_record_resource_cleanup_candidates.py and
tests/test_game_record_resource_cleanup_match.py. Reuse the existing IDO
compiler, guest/native32 oracles, signed-byte CopyOracle, ELF parsers,
owner/pool fingerprints and both padders. Ignored receipts:
conker/build/game-record-resource-cleanup-match-test/.

- Twelve pre-install tests pass in 46.416 seconds. Original, raw C and actual
  padded forms have the full body, original frame/delay updates, 172-byte
  function extent and the 180-byte slot with two NOPs.
- The count/sentinel/equal/full-word identity/phase matrix passes 487 cases
  across three forms and reaches all 43 body words. High unsigned counts
  use a first-callback shrink. Invalid identities use mapped guest fixtures,
  not portable or real-table bounds acceptance.
- Thirteen callback/short-circuit cases preserve count shrink/expansion,
  live table replacement, record changes and the no-source-read sentinel
  path. Helpers clobber caller-saved integer and floating-point registers.
- Nine independently linked rebases pass 108 cases, exercising both global
  HI16/LO16 carries, the release JAL, full-word identity and unused registers.
- All 164 original/raw/padded private/public/callback fault-prefix triples
  actually fire and preserve partial memory, events, calls and registers.
  These are guest instruction-order checks, not portable C fault semantics.
- Five freshly compiled semantic mutations fail effectively, and three stale
  installations reject. Four source/prototype/declaration/newline corruptions
  and five body/padding/extent/symbol-value/name corruptions reject.
  An unrelated ELF byte survives historical projection for later rejection.
- Both complete before/after owner profiles compile without diagnostics.
  Both real padded routes preserve all 14 neighbors, extents, relocations,
  pools, the 274-word caller and existing D804 function-object selector.
- Native32 O2/O0 each pass all 65,536 initial halfword-count cases with early
  shrink, 3,072 identity/count/callback cases, and a separate full 65,535-record
  sentinel scan. Arrays/pointer/call checks and an effective stride mutation
  pass. The high-count matrix is not 65,536 complete maximum scans.
  Existing no-strict-aliasing policy applies; no portable64/hardware claim.
- Actual linked func_1510D7AC equals retail across all 46 words/184-byte extent.
  The actual 43/46-word cleanup/release chain passes 163 cases / 489 executions
  and reaches all 46 release words: signed state byte, unsigned refcount byte,
  conditional inner/outer free calls, live outer pointer reload and real
  pointer/state clears. Heap-free callbacks remain bounded.
- The actual sixteen-body parent failure chain passes 1,920 cases / 3,840
  executions with cleanup and release hooks removed, reaching 42 cleanup
  words and all 46 release words. Focused coverage, not this inherited matrix,
  establishes all 43 cleanup words. Source identities in the disposable
  fixture are bounded so the real release tables can be mapped safely.

Initial harness issues were a copied source-hash transcription, treating the
43-word symbol extent as the complete 45-word slot, and a missing signed-byte
dispatch in the focused oracle; use the existing CopyOracle for that opcode.
The first installed audit also exposed the exact linker metadata permutation
below. The parser now accepts bytes/bytearray inputs consistently. These
were harness/audit issues, not production defects. Frozen inputs stay intact.

The final fresh installed/regression selection passes 97 tests in 388.154
seconds: twelve cleanup, twelve propagation, twelve descriptor, twelve pair,
eleven counter, eleven command, fifteen guarded parent, ten earlier shape/audit
checks and two historical status-join checks. No skips/errors/failures.
Earlier complete shapes are recompiled; their old full behavioral matrices
are not rerun. Unchanged prior semantic receipts remain prior evidence.

## Immutable Audits And Actual Delta

Freeze all nine source/ELF/guard/conversion/rodata/symbol/undefined/layout/
Makefile inputs before installation. Require the exact body, typed prototype
and release declaration before reversing to verified prior source SHA-256:
0621f5de4f8c8b3f9c931d07bcf6838566b204eafbbeae45869e54d572d82a3c.
Correct the transcription of that hash in Note 1271, not its frozen evidence.

The literal new audit allows only the 180-byte slot, extent 12 -> 172 and
the measured D_800D35E0/D_8008F8C0 symbol/string-table permutation. Parse ELF
tables and require both exact absolute names, addresses, zero extents,
bindings, section indexes, original adjacent entry/name offsets and complete
entry bytes. Only their four-byte values and eleven-byte names swap.
No blanket symbol-table acceptance or baseline refresh.

Exactly 149 ELF bytes change: 134 target-slot bytes, one extent byte and
14 permutation bytes (six symbol-value/eight string-name bytes).
Headers/sections, semantic symbol set except cleanup extent, other function
bodies/extents/addresses, other metadata and assignment inputs remain exact.
All 189,088 protected data bytes / 720 owners stay exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Historical projections verify the complete retail slot including both NOPs
and extent 172, then reverse only the cleanup slot/extent and exact pair
permutation onto trusted historical evidence. Preserve every other current
byte. Existing propagation/descriptor/pair/counter/command audits remain
frozen; the propagation receipt labels its cleanup-projected view. The new
literal audit does not project its own installation.

Installed source SHA-256:
f580435626504c2fda5ecf8b7fa7a87feaf4d1f2a1332be1118923a6492e5dcb.
Installed ELF SHA-256:
9f2c45ce2994dafadbaa9bce9c640e61852b6f2ebf4d2a34a41d1d1438bbcb25.
Unchanged guard SHA-256:
92679ed3e2a6439969298cd769daf69d41e9619c81360046094cf34f1ec3faf4.
Unchanged Makefile SHA-256:
8493bae49a7d02eac15064df9acd84044095a21ecdd877b11f12b04375943abc.
Unchanged conversion CSV SHA-256:
32045cb144c96ede05faaa343ad9b6bae1c4de6c0d961973cfeda6e16e14bf5c.

Required ELF/progress rebuild and fresh matcher exit zero. Existing duplicate
generated_12D630 recipe warning remains; no new owner diagnostics.

| Section | Byte-Exact | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3,469 / 5,495 (63.13%) | 0 | 2,026 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,796 / 4,822 (57.98%) | 0 | 2,026 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

One matching credit only. Converted-function and converted-byte metrics
stay fixed. README changes only the two affected aggregate matching rows.

## Ownership And Next Work

Single Codex writer, zero Claude calls. Mounted tools 663f63b706836e8064be619136042acd5965c165 is committed
first; consumer banks source, note, concise indexes, prior-hash erratum and
that pin. No push. Consumer/mounted/older WSL tools checks and native
py_compile pass. Copy only two finalized absent paths to the older sibling.
Its HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 35 protected
existing fingerprints stay unchanged. Dirty entries 312 -> 314 are only
those copies. Existing audit files/history are not overwritten, committed
or reset. Copies are not an older-checkout function-suite qualification.

Native Graphify update exits one after protective shrink refusal 39,868 ->
18,087 nodes, retaining 19,398 nodes from 2,972 still-existing excluded files.
Known version/devcontainer warnings remain; no force, purge or install.
Zero native workers verified after the command. Require fresh post-commit
log length/UTC and authoritative completion plus zero workers before reporting
the consumer checkpoint settled; launch receipts alone are insufficient.

Next: investigate raw guard elimination for complete func_1503D774 and
replace its bounded third-loader hook with actual instructions in the
parent chain. It is already linked-exact: VA 0x1503D774..0x1503D804,
ROM 0x6AC24..0x6ACB4, 36 words / 144 bytes. Six normalization guards and
one instruction-drop row remain. Do not award a second matching credit.

Parent/pair guards, deeper lookup/block loaders, real allocator/free/heap,
hardware, renderer/gameplay and portable64 acceptance stay separate/open.
No OGL/Release/save/editor/private-input changes; Release remains frozen.
The wider Game goal remains active.
