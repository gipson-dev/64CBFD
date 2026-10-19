# Packed-Entry Peer Lookup Complete Match

Verified: 2026-10-19. **Installed complete C recovery: all 63 words / 252 bytes
match retail, including the original frame8 and saved-S0 lifetime.**

Finish `func_1508ECC0`, generated_B3020, VA `1508ECC0..1508EDBC`, ROM
`BC170..BC26C`, after [Note1584](1584-slot-state-transfer-complete-match-20261019.md).
Consumer predecessor `dbe59bf9`; tools predecessor `63f4733`. Bank tools
**825aaa5** before the consumer source/guards/docs/pin. No push.

## Complete Source And Interface

Replace the zero-return placeholder with a returning lookup. Search the
unsigned global row count D_80087380 through D_800D23C0, using24-byte rows,
the unsigned halfword count+2 and packed halfword entries+8. Construct the
key by truncating `(group <<12) + value` to16 bits. This is addition, not OR;
large values can carry into the group nibble or wrap the complete key.

Find the **first row containing that key**, using its first matching entry
index. Return the low12 bits of the first entry whose high nibble equals the
requested peerGroup and whose index differs from the key's index. A peer can
have the same group as the key; only its index must differ. If that first row
has no peer, return -1 immediately, without trying later rows. Also return -1
when no row contains the key. Do not restrict the source group to0..15 or mask
peerGroup to four bits: the former participates in truncated arithmetic and
the latter is a complete unsigned-halfword comparison.

Use `s32 func_1508ECC0(u32 group, u32 value, u16 peerGroup)`, with explicit
u16 views of the first two parameters. The original entry code consumes low16
bits but writes **all three full incoming words** into argument homes. Keep
the address name and concise purpose comment. PackedPeerRow is a local layout
view, with unknown+0/+4 fields left named unk0/unk4, not authenticated source
names. Native fixtures use the eight entries fitting a24-byte row. Wider
guest count probes do not establish a universal portable C array domain.

There is no named direct caller in the retained assembly/source search. The
original code image also has no aligned1508ECC0 address word or0D423B30 JAL
word. This does **not** prove the function unused: indirect/computed callers
remain possible. The entry ABI is derived from the complete routine and
qualified with synthetic call windows, not invented retail caller receipts.

## Explicit Layout

The chosen ordinary C emits **60 words/frame8**, with four bindings, in both
owner profiles. It is not a direct unguarded match. The source screens compare
row cursors, indexed/typed fields, parameter widths/reuse, declaration order,
register hints and old-style definitions. They do not justify dummy padding,
volatile or physical-register bindings. The selected body needs no such hint.

The layout recipe in `game_packed_peer_lookup_layout.py`:

- Restores full-word A0/A1 home stores at SP+8/+12. The existing full-word A2
  home store at+16 and saved S0 at+4 are retained.
- Moves the initial low-halfword views, zero index and table-address prefix
  into the original independent schedule. Restore the empty-count BEQL edge
  directly to the epilogue, with a new -1 delay-slot update. Nonempty paths
  retain V0=0; an empty count never reads the table pointer.
- Restores the row-address/key schedule and13 opcode-aware register recipes.
  Preserve every one of the60 source origins exactly once. Add only the two
  argument stores and early -1 operation; omit no source word.
- Moves all four existing HI/LO bindings to their original output positions.
  The normalized code and bindings match independently assembled retail code.

The manifest encodes the derived63-word stream with **60 expected-word and
expected-relocation rows plus three insert_after fields**. Manifest stream
association is separate from instruction-origin numbering. Gate the recipe on
the complete raw SHA256, exact bindings and normalized SHA256. Generation also
requires the exact installed C owner and first-image proof, and preserves the
entire historical CSV prefix. No shared padder, Makefile, compiler option,
original assembly or retained data change.

```text
raw:        24b2c822fdd4365a8bf9df44f1614b83ca16b08e2c19babd04e0059a9b3d02ca
normalized: 750aa7902c6654ecbdb453d806b36ffa26da8ad81feb3ba8bfdaeaa17c9bf444
```

## Fresh Qualification

All **10 pre-install tests pass in22.064 seconds**. All **10 installed tests
pass in25.016 seconds**, without skips. Setup recompiles the complete C body;
the suite creates its own owner, padder, GNU-map and image artifacts.

- **1,828 fixtures/two phases:3,656 paired literal executions** agree in full
  GP/FP/LO state, private/public memory, ordered events and returns. The same
  corpus checks raw C's public result against an independent numeric reference;
  this is reused coverage, not3,656 additional independent inputs. Public data
  stays unchanged. Dynamically visit61 words; statically compare all63,
  including the two unreachable loop increments.
- **92 fired access-fault pairs**, two guest-only argument-home/table aliases
  and five unsigned-width probes pass. Every requested cut fires. Large u32
  row-count probes are bounded fault prefixes, not completed enormous scans;
  high u16 entry-count probes return through early, backed entries. This is
  modeled guest access order, not a hardware exception or native-alias claim.
- Native32 **O0, O2 and O2+UBSan** each pass all1,828 fixtures plus **196,608
  extra calls** sweeping all65,536 values of each of three input views against
  literal fixture-specific expectations. Check96 public bytes per fixture and
  final sweep memory/globals. Four executed source controls (OR key, selecting
  self, unmasked result and later-row fallback) exit21; positives exit0. Keep
  the existing stack-realignment/no-strict-aliasing harness policy.
- **46 synthetic full-word ABI pairs** set the third argument in the JAL delay
  slot, preserve saved registers and verify all three full argument-home words.
  These are not actual retail caller windows.
- Nine raw-byte/binding/register corruptions reject their changed inputs.
  Six manifest corruptions fire the actual padder's stale-word/relocation
  checks; three image mutations fire the strict full-image verifier.
- **Three independent GNU maps** agree across all63 instructions and four
  bindings, including HI/LO carries. Execute **486 mapped cases** with rebased
  code, both globals and the current row pointer. They reuse selected fixtures;
  no additional unique-domain or hardware coverage is inferred.
- Both owner profiles preserve72 other routines and normalized pools. The
  actual padder preserves those72 padded bodies/addresses/pools. All seven
  expanded shadow Make commands agree, including the unchanged projection
  override from the normal-profile object.

## Production And Commits

The first private ELF matches the target-only prediction on its first attempt.
Actual Make reproduces that complete3,257,636-byte image: **207 changed bytes,
206 target-code bytes and one target-symbol size byte** (12 ->252). No symbol
order/string permutation or metadata exception. All other6,056 linked bodies,
every address, all189,088 protected Game-data bytes /720 owners, historical
guards and other frozen inputs stay fixed.

The wider manifest-triggered rebuild succeeds with inherited duplicate
generated_12D630 recipes and warnings from untouched C. Both target owner
qualification profiles have empty diagnostics; do not call the whole build
warning-free. The complete build log is retained in ignored
`conker/build/game-packed-peer-lookup/integration/production-build.log`.
Existing mixed CSV endings remain intact; Git's CRLF advisory is not a failure.

```text
owner:  9847b3641891ec5035d87f0bf0c96568bc649abb6ed9911fb3786a584ae959d7
guards: 5c1e9119eed376d6ed986bfbe8c332cec79b259a6cbdbe23db3b1bb4d4517c4c
ELF:    5261c62f0c48dda8fb5a94ab56b8d275bf27ade0a8e1e87bae72010597aa4050
```

Fresh matching: **Game3000/4832 (62.09%)**, **total3673/5505 (66.72%)**,
Init492/492, Debugger181/181, **1,832 different / zero drift**. Conversion counts
and bytes remain5505/6044 (91.08%),86.08% bytes overall and4832/5323 (90.78%),
85.44% bytes for Game. Root README receives aggregate matching rows only.

Both tools copies pass three setup tests and their project smoke checks;
consumer `make tools-check` passes. The five new task files are identical
ASCII/Python-valid in the independently dirty standalone mirror. Preserve its
ddbdd16 HEAD and all1,323 prior leaf hashes; add only five files for1,328 dirty
leaves, without mirror commit/reset. Post-commit graph preservation is a
separate gate in ignored `integration/graph-audit.json` beneath this build.
No compiler capture, Claude call, REA setup, sibling host or Release action.

```sh
python3 -m unittest tools.tests.test_game_packed_peer_lookup_match -v
python3 -m tools.experiments.game_packed_peer_lookup_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

This lookup is finished. The next20-word func_1508EDBC already matches.
Continue with **func_1508EE0C**, VA `1508EE0C..1508EF80`, ROM `BC2BC..BC430`:
**91 instruction words plus two retained alignment NOPs**, a93-word slot,
frame0x30, currently89 slot differences and a false zero-return placeholder.
Recover its first packed-key row search, lower12-bit dispatch to the type2/3
helpers, fresh table/count reload after either helper and final row clear via
the already-exact func_1508EDBC. Derive the actual caller/return interface;
the assembly has no consistent final V0 result, so do not invent a success
flag. Qualify helper mutation, saved roles, argument homes and both tail
alignment words. The broader Game decomp/matching goal remains active.
