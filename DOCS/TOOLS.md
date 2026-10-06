# Project Tools

This page documents repository-local tooling, especially scripts that are not
upstream submodules. Run commands from the repository root unless a section
says otherwise.

## Effect-configuration packet compiler controls

[Driver](../tools/experiments/game_effect_configuration_packet_candidates.py)
screens eight forms under four profiles: 32 controls with real SDK types and
fixed anchors. A separate captured float local under O2/g3 emits all 69 words
directly. The tool installs no source/guards/profile. IDO, retail ROM and MIPS
tools required; ignored receipts under
`conker/build/game-effect-configuration-packet/`.
[Six tests](../tools/tests/test_game_effect_configuration_packet_match.py)
check the complete 60-byte packet, scalar narrowing, call-entry snapshots,
source/global aliases, post-capture mutations, saved registers and typed
32-bit native layout. Guest bit transport includes signaling NaNs without
FP arithmetic; native cases deliberately use finite/quiet-NaN patterns.
`func_15152190` is an opaque callback and remains a C placeholder in production.
No full effect-path/hardware/FCSR/gameplay/host claim. See
[Note 1043](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md).

## Address-record allocator compiler controls

[Driver](../tools/experiments/game_address_record_allocator_candidates.py)
screens 12 forms under four profiles: 48 controls with real SDK types and
fixed retail anchors. Owner-before-flags O2/g3 emits all 37 words directly;
the tool installs no source, guards or profile. Retail ROM, IDO and MIPS tools
required; ignored receipts under `conker/build/game-address-record-allocator/`.
[Six tests](../tools/tests/test_game_address_record_allocator_match.py) bind
the direct wrapper and unchanged 28-word allocator/20-word list inserter.
Guest traces cover all halfwords and mode/channel pairs with high incoming
bits; native actual C verifies both allocator outcomes and all record/list
footprints. The native fixture uses one explicit 32-bit heap-address cast.
Heap remains opaque; sparse high context rows/self-head states are diagnostics,
not full caller/hardware/FCSR/gameplay or host adoption claims. See
[Note 1042](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md).

## Conditional packet allocator compiler controls

[Driver](../tools/experiments/game_conditional_packet_allocator_candidates.py)
screens six forms under four profiles: 24 controls with real SDK/struct headers
and fixed retail anchors. Reserved-first O2/g3 emits all 38 words directly;
the tool installs no source, guards or profile. Retail ROM, IDO and MIPS tools
required; ignored receipts under `conker/build/game-conditional-packet-allocator/`.
[Six tests](../tools/tests/test_game_conditional_packet_allocator_match.py)
bind the direct wrapper and unchanged cleanup/allocator chains. Guest checks
include ordered calls/reads/stores, callback snapshots, allocation failure,
global/source aliases and copied untouched padding. Native actual wrapper/
cleanup C uses an opaque typed allocator and checks initialized fields without
inventing padding values. SDK/backend callbacks remain bounded models, not
hardware/gameplay/host adoption. See
[Note 1041](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md).

## Random selector/output compiler controls

[Driver](../tools/experiments/game_random_selector_outputs_candidates.py)
screens six forms under four profiles: 24 controls. A 32-bit selector under
O2/g3 emits all 37 words directly, retaining the callee's byte narrowing.
The tool installs no source, guards or profile; retail ROM, IDO and MIPS tools
required. Ignored receipts under `conker/build/game-random-selector-outputs/`.
[Six tests](../tools/tests/test_game_random_selector_outputs_match.py) bind the
direct wrapper, unchanged 31-word selector/18-word handwritten RNG and palette.
Ordered external traces, output aliases and call-entry snapshots are checked;
a local 64-bit guest extension executes the RNG without changing shared runners.
Native fixtures use the actual wrapper/selector C plus an independent RNG-state
model, not native execution of MIPS assembly. No hardware/FCSR/gameplay or host
adoption claim. See [Note 1040](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md).

## Actor position-queue wrapper compiler controls

[Driver](../tools/experiments/game_actor_position_queue_wrapper_candidates.py)
screens eight forms under four profiles: 32 controls with real SDK/actor
headers and fixed retail anchors. Plain typed O2/g3 emits all 37 words
directly. No source, guards or profile installed by the tool; retail ROM,
IDO and MIPS tools required. Receipts ignored under
`conker/build/game-actor-position-queue-wrapper/`.
[Seven tests](../tools/tests/test_game_actor_position_queue_wrapper_match.py)
bind the direct wrapper and unchanged helper, complete external guest traces,
signed argument homes, callback capture/mutations and connected queue stores.
Native cases use the actual complete actor and queue-record layouts plus
the retained writer C body. Raw float-bit transport is qualified, not FP
arithmetic/FCSR or gameplay. See
[Note 1039](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md).

## Alternate actor-dimension compiler controls

[Driver](../tools/experiments/game_actor_alternate_dimensions_candidates.py)
screens four forms under four profiles: 16 controls with real SDK/actor/point
headers. Six O2 forms match 41 body words plus two retail padding words; the
tool installs no source, guards or profile. Requires retail ROM, IDO and MIPS
tools; ignored receipts under `conker/build/game-actor-alternate-dimensions/`.
[Five tests](../tools/tests/test_game_actor_alternate_dimensions_match.py)
bind the complete slot/padding, local signed cast and unsigned shared field,
ordered guest traces/full footprints and actual C/real actor-prefix native
cases. Negative controls detect premature cached fields and unsigned +0xE8,
plus wrong threshold/dimension and stub. The preceding query's optional
offset/entry test helpers retain their old defaults. See
[Note 1038](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md).

## Actor-dimension query compiler controls

[Driver](../tools/experiments/game_actor_dimensions_candidates.py) uses real
SDK/actor/point headers for four forms under four profiles: 16 controls.
Direct fields/cached ID/early return match under both O2 profiles; no source,
guard or profile is installed by the tool. Requires retail ROM, IDO and MIPS
tools; ignored `conker/build/game-actor-dimensions/` receipts.
[Five tests](../tools/tests/test_game_actor_dimensions_match.py) bind the
direct linked slot, sequential guest traces/complete footprints and the
actual C/real actor prefix in native cases. Negative controls detect wrong
ID threshold, unsigned fields, missing offset and the stub. Forty reachable
words execute; the impossible likely-branch delay word is structurally bound.
See [Note 1037](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md).

## Projection-wrapper compiler audit

[Driver](../tools/experiments/game_projection_wrapper_candidates.py) runs
20 O2/g3 pointer-home/W/index-lifetime controls using real SDK/structure
headers. None matches; it installs no source, profile or guards. Requires
retail ROM, IDO and MIPS tools; ignored receipts under
`conker/build/game-projection-wrapper/`.
[Three tests](../tools/tests/test_game_projection_wrapper_audit.py) reproduce
all measurements and bind the retained 58-word synthetic-return helper chain
and production placeholder. These are compiler/identity checks, not connected
execution or native/alias qualification. See
[Note 1036](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md).

## Descriptor shape-measure compiler controls

[Measure driver](../tools/experiments/game_shape_volume_candidates.py)
uses the real SDK/descriptor headers for six box operand orders crossed with
two cylinder operand orders under four profiles: 48 controls. Only one O2/g3
form emits all 56 words directly. It installs no source, guards or profile;
requires retail ROM, IDO and MIPS tools. Receipts are ignored under
`conker/build/game-shape-volume/`.
[Six tests](../tools/tests/test_game_shape_volume_match.py) bind the complete
direct slot, corrected prototype/externs, actual descriptor layout and retail
coefficient words. Independent guest traces/native references preserve
wrapped box multiplication and per-operation float rounding; negative tests
detect the stub, unsigned halfwords, unmasked flags and premature float box
multiplication. Shared guest runners are unchanged. No caller-domain/gameplay
or complete FCSR qualification. See
[Note 1035](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md).

## Integer pair-clamp access controls

[Pair-clamp driver](../tools/experiments/game_integer_pair_clamp_candidates.py)
screens 23 forms under O2/g3, O2, O1/g3 and O1: 92 controls, empty compiler
diagnostics, no direct exact form. It installs no source, guards or profile.
Requires retail ROM, IDO and MIPS tools; receipts are ignored under
`conker/build/game-integer-pair-clamp/`.
`--register-lifetimes` separately screens 16 parameter-hint masks times
four local-hint groups under O2/g3 and O1/g3: 128 controls, receipts in
`conker/build/game-integer-pair-clamp-register-lifetimes/`. It does not
change the default 92-control inventory. See
[Note 1033](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md).
`--saved-registers` screens nine locally evidenced `-Wo` uopt options against
the recovered O2/g3 body; modes are mutually exclusive. Flags are passed only
to disposable candidate builds, not production. Receipts:
`conker/build/game-integer-pair-clamp-saved-registers/`. See
[Note 1034](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md).
[Nine recovery tests](../tools/tests/test_game_integer_pair_clamp_recovery.py)
bind the non-matching source/slot, compare complete guest access traces and
native footprints, and detect wrong clamp/swap controls. A local oracle adds
only XOR; shared runners remain unchanged. Explicit register-field renaming
proves correspondence of the 24-word operation core, not an installed
normalizer or whole-function match. The saved-pointer frame and return tail
remain open. See [Note 1032](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md).
The additional register-lifetime test compiles all 128 forms, binds complete
word equality by profile/local group, and runs 1536 bounded corner traces.
The backend test checks all nine accepted controls and 108 corner traces;
`nordstore` changes only one closed temporary lifetime, while `noprecolor`
adds caller-home copies but no saved-pointer frame. No new match is inferred.

## Indexed state-save compiler controls

[State-save driver](../tools/experiments/game_indexed_state_save_candidates.py)
uses real actor/header definitions for eight forms under four profiles:
32 controls, ignored `conker/build/game-indexed-state-save/` receipts. It
installs no source, guards or profile. Requires retail ROM, IDO and MIPS tools.
[Eight state-save tests](../tools/tests/test_game_indexed_state_save_match.py)
bind the direct slot and unchanged exact callback, sequential byte traces,
opaque mutation, connected bit selection, zero-mask non-returning prefixes
and native footprints. Shared guest runners are unchanged; bounded diagnostic
indexes do not establish valid gameplay slots or portable out-of-bounds C.
See [Note 1031](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md).

## Random-reload timer compiler controls

[Timer driver](../tools/experiments/game_random_reload_timer_candidates.py)
screens 19 forms under O2/g3, O2, O1/g3 and O1: 76 controls, ignored
`conker/build/game-random-reload-timer/` receipts. It installs no source,
guards or profile. Requires the retail ROM, IDO and MIPS binutils.
[Eight timer tests](../tools/tests/test_game_random_reload_timer_match.py)
bind the typed record/direct slot and compare three guest instruction bodies
with independent memory/call ordering, native footprints and break-7 cases.
The local oracle subclass adds only DIVU/MFHI/the exact trap; shared runners
are unchanged. No full dispatcher/RNG/gameplay or hardware trap claim.
See [Note 1030](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md).

## Float-reference packet compiler controls

[Packet driver](../tools/experiments/game_effect_packet_wrapper_candidates.py)
screens six source forms under O2/g3, O2, O1/g3 and O1: 24 bounded controls,
empty diagnostics, ignored `conker/build/game-effect-packet-wrapper/` receipts.
It installs no source or profile. Requires the retail ROM, IDO and MIPS
binutils. [Eight packet tests](../tools/tests/test_game_effect_packet_wrapper_match.py)
bind source/production words/no guards, all 28 packet bytes and padding,
narrowing, native layout and connected original-retail-callee behavior.
Production checks also bind the unchanged callee to all 50 retail words.
Full wrapper/callee coverage does not qualify the complete allocator or
gameplay. See [Note 1029](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md).

## Zone selection compiler controls

[Edge lifetime driver](../tools/experiments/game_graph_edge_crossing_lifetimes.py)
adds 209 existing-profile source controls in eight modes: default layouts,
`--loops`, `--sides`, `--coordinates`, `--registers`, `--declarations`,
`--parameters`, or `--geometry`. Modes are mutually exclusive and each writes
a separate ignored JSON receipt under `conker/build/game-graph-edge-lifetimes/`.
It freezes the preceding 151-difference body; no experiment installs source
or permits oversized code. See
[Note 1026](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md)
for the selected 207-word / 102-difference improvement and qualification limits.

[Linked-record tail driver](../tools/experiments/game_linked_record_tail_candidates.py)
freezes the original 71-word body and measures four store-volatility forms
under four backend profiles (16 controls), with ignored receipts. Its strict
normalizer binds the three compact words of the closed return-tail expansion;
it does not install source or enable oversized bodies. Six tests qualify
3360 three-way guest cases, actual emitter/relocation rejection and production
slot equality. See [Note 1028](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md).

[Scope driver](../tools/experiments/game_graph_edge_crossing_scopes.py) freezes
the 102-difference body and screens 101 named controls across default scopes,
`--planes`, `--aggregates`, `--sums` and `--products`. Each writes a separate
ignored receipt. `--verify-checkpoint` compares all live ELF slots with the
preceding ignored lifetime-test receipt and fails if absent or different.
Three tests bind transformation boundaries and inventory. No source is
installed. See [Note 1027](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md).

[Edge-crossing driver](../tools/experiments/game_graph_edge_crossing_candidates.py)
screens 39 source forms under the existing/default-unroll profiles, writing
78 records to ignored `conker/build/game-graph-edge-crossing/screen.json`.
It preserves the semantic baseline and marks minimum-result/narrowed-band
negative controls. Requires the retail ROM, IDO and MIPS binutils. It does not
install source or permit oversized bodies. See
[Note 1025](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md)
for the original recovery; Note 1026 supersedes its 151-word mismatch with
the current 102-difference form. The original 39-form inventory stays frozen.

[Root lookup driver](../tools/experiments/game_root_neighbor_lookup_candidates.py)
measures 35 source forms under both existing/default-unroll profiles and writes
70 records to ignored `conker/build/game-root-neighbor-lookup/screen.json`.
It preserves the pointer-based recovery and old typed placeholder; the
unsigned-index forms are signed-count negative controls. Requires the retail
ROM, IDO and MIPS binutils. See
[Note 1024](WORKING_NOTES/1024-game-root-neighbor-lookup-direct-match-20261006.md)
for the direct match; its geometric-helper placeholder is now superseded by
the non-matching recovery in Note 1025.

[Recovery driver](../tools/experiments/game_zone_neighbor_selection_candidates.py)
retains the original 29-form inventory and previous source checkpoint.
[Lifetime driver](../tools/experiments/game_zone_neighbor_selection_lifetimes.py)
adds 52 lifetime, 16 cursor and 23 register-hint controls without changing the
recovered query layout. Run the latter module normally, with `--cursors`, or
with `--registers`; mode switches are mutually exclusive. Each mode writes a
separate JSON receipt under ignored `conker/build/game-zone-neighbor-lifetimes/`.
Requires the extracted retail ROM, WSL IDO and MIPS binutils. Experiment output
does not install source, enable oversized bodies or count as a byte match.
See [Note 1023](WORKING_NOTES/1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
for measurements and qualification boundaries.

## Toolchain smoke test

Validate the project-native raw-object, minimal-ELF, and standard vertex
conversion helpers without a ROM:

```sh
make tools-check
```

The check creates an isolated seven-byte fixture, wraps it in a 16-byte-aligned
big-endian MIPS object, links it at `0x80000000`, validates both ELF files, and
checks known and malformed standard `Vtx` records. It writes only to the
system temporary directory.

The scripts use `mips-linux-gnu-` by default. Set `CROSS` to another MIPS
binutils prefix, including or omitting its trailing hyphen. `MIPS_AS` and
`MIPS_LD` can override the individual commands.

## Raw binary object wrapper

`tools/mkrawobject` converts an arbitrary file into a big-endian, 32-bit MIPS
relocatable object with a `.data` section:

```sh
tools/mkrawobject INPUT OUTPUT [ALIGNMENT]
```

The default alignment is `0x10`. The input is zero-padded to that boundary.
This is useful when a linker must consume an opaque extracted binary while
preserving an explicit N64 alignment.

Example:

```sh
tools/mkrawobject assets/debugger.us.bin build/debugger.us.o 0x10
```

The normal ROM build already wraps its checked-in binary assets directly with
GNU `ld -r -b binary`; do not replace those established Makefile rules merely
to use this helper. Use `mkrawobject` when section alignment or an independent
diagnostic object is specifically needed.

## Minimal ELF linker

`tools/mksimpleelf` links one MIPS object into a small executable ELF:

```sh
tools/mksimpleelf INPUT_OBJECT OUTPUT_ELF [BASE_ADDRESS]
```

The default base is zero. The linker script is generated in an isolated
temporary directory and retains `.text`, `.rodata`, `.data`, and `.bss`.
This is intended for inspection, conversion, and small tooling fixtures, not
as a replacement for `conker.ld` or the ROM linker scripts.

Example:

```sh
tools/mksimpleelf build/debugger.us.o build/debugger.us.elf 0x16000000
```

## Standard N64 vertex converter

`tools/vertconvert.py` converts packed standard 16-byte SDK `Vtx` records into
C initializers:

```sh
tools/vertconvert.py HEX_DATA
tools/vertconvert.py --file vertices.hex --array-name display_vertices
```

Input can contain whitespace, commas, underscores, and repeated `0x`
prefixes. A file may contain `dlabel` lines, which are ignored. With no
positional input or file, the tool reads standard input. It validates that the
input contains complete 16-byte records instead of silently discarding
malformed data.

The record layout is three signed 16-bit coordinates, a 16-bit flag, two
signed 16-bit texture coordinates, and four color/normal bytes. This helper is
useful for SDK-style display-list data and assembly-to-C work.

It is deliberately not an `assets13` decoder. Conker's verified model records
there contain only three signed 16-bit coordinates per six-byte vertex, with
no inline flag, texture coordinates, color, or normal. Use the decoder in
[Asset formats](ASSET_FORMATS.md#4a-model-geometry-assets13-vertex-arrays-confirmed)
for those records.

## Conker asset tools

Use the following tools for the current Conker formats:

- `tools/asset_dump.py` lists and extracts the master asset-table sections.
- `tools/rareunzip.py` and `tools/rarezip.py` decode and encode Conker's
  four-byte-size-header Rarezip blocks.
- `tools/extract_compressed.py` and `tools/compress_dir.py` implement the
  config-driven compressed-section workflow.
- n64splat's image handling and its `n64img` dependency should be tried first
  for standard N64 texture formats.

See [Asset formats](ASSET_FORMATS.md) and
[Compressed config sections](CONFIG.md) for the verified format details.

## Reference-only imported asset generators

The newly added `tools/assetmgr/` scripts and the top-level
`tools/mktextures` are not Conker asset builders. Their schemas and output
formats describe a different Rare N64 asset pipeline:

- they require a `ROMID`-keyed `src/assets/...` tree that this repository does
  not have;
- their compressor writes a `0x1173` marker and a three-byte size, while
  Conker Rarezip uses a four-byte big-endian size followed by raw DEFLATE;
- their language banks, pad/waypoint records, room tiles, animation tables,
  sequence tables, and texture manifests have no verified mapping to Conker's
  containers.

These entry points therefore stop with an incompatibility message by default.
For controlled cross-game format research only, set:

```sh
ALLOW_PD_ASSET_FORMATS=1
```

That opt-in does not make the formats Conker-compatible, and none of these
generators are part of the build graph. Do not publish generated Conker assets
from them without first documenting and verifying a real format mapping.

## Upstream submodules

`asm-differ`, `asm-processor`, `mips_to_c`, `n64splat`, `texture2c`, and
`ultralib` retain their upstream documentation. Project-specific usage and
format conclusions belong under `DOCS/`.
