# Note 2601: Filtered projection draw guarded byte match

Date: 2026-11-20. Consumer baseline `e7b0f03548747d0dfc774e032f6949d0cba06daf`;
tools baseline `8ea137f65b2ecd63facfbeb9ff0197c144ddcf12`.
Qualified tools commit: `9643f3af44e407ffb0b4449ed9b03d8cb23d1280`.

`func_15035D6C` replaces its zero-return placeholder with complete semantic C.
All **159 words / 636 bytes**, with no alignment tail and a **32-byte frame**,
are byte-exact through **29 expected-word rows**, including one redundant
shift-mask omission. There are no inserted instructions or profile changes.
The existing O2/g3 Make recipe remains authoritative.

Fresh production recount is **4,585 / 5,528 (82.94%)** total and
**3,912 / 4,855 (80.58%)** Game, with zero drift and **943** still different.
Init 492/492 and Debugger 181/181 remain exact. **114 more** are needed for
85% at this denominator. Conversion rows are unchanged because the former
placeholder already counted as C. The wider matching goal remains active.

## Recovered behavior and interface

Owner `conker/src/game/generated_61D10.c`, VA `0x15035D6C..0x15035FE8`,
ROM `0x6321C..0x63498`. The recovered interface returns a `Gfx *` and accepts
a command cursor, typed display descriptor and three 32-bit color values.
The fifth argument, blue, is read at incoming SP+0x10 / new SP+0x30.

The routine gates on the projection-record count, enables front-face culling,
and scans 12-byte records. It selects renderMode 1, matching descriptor ID and
variant, then emits pipe sync, matrix segment 3, environment color, segment 8
render state and enabled descriptor display lists. Record alpha and descriptor
alpha are unsigned bytes; their product shifted by eight ranges from 0 to 254.
The original opaque-state branch is therefore unreachable for those byte inputs.
It remains present in the source and exact output.

Count and descriptor reloads preserve retail alias-sensitive store order.
Rejected records reuse the last loaded global count; successfully drawn records
reload it after command stores. Enabled lists reload their count after stores.
`1u << (list & 31)` stays defined for every byte list count, including counts
above 32. Only the redundant emitted ANDI is removed: MIPS SLLV already masks
its shift count to five bits. Front-face culling is cleared before return.

The new descriptor is 40 bytes on SDK32, with ID/alpha/variant at offsets
0/3/6, disabled-list mask at 19, byte list count at 20 and list pointer at 36.
Existing record bytes 9/10/11 gain the names descriptorId, descriptorVariant
and renderMode. The previous `func_15035FE8` access changes its field name only.
All nine raw/padded neighbors, their bindings and the existing literal pool
remain identical. `func_15035808` stays its unchanged seven-word typed
placeholder and receives no credit.

The sole aligned direct JAL is ROM `0x5ED64` / VA `0x150318B4`, in
`func_150311C4` (`asm/5D2C0.s`). Its original call window passes cursor and
descriptor in A0/A1, loads red/green into A2/A3 and writes blue into outgoing
SP+0x10 in the JAL delay slot. The next original word consumes V0 into S0.
There are no aligned direct J or literal function pointers; computed callers
remain unexcluded. The caller's C body is still unrecovered and unchanged.

## Closed derivation and independent checks

Raw C emits 160 words with the correct frame and all seven saved-register
physical homes. Raw payload SHA-256:
`c46837ea7e3435857bd1362a9c9418a22f7d68c3ee9c76c88d554a33830c254a`.
The normalizer applies a closed S0/S1/S2 body-role cycle while preserving the
physical saved homes, reorders independent prologue stores, removes raw word
114's redundant mask, adjusts its scratch roles and branches, and changes the
final geometry scratch register. It consumes fingerprinted C output/bindings;
ROM and original assembly are independent verification inputs, not generators.

Independent GNU assembly matches the complete normalized payload and all 18
HI16/LO16 bindings. Two links include shifted entry/data addresses and carry
handling. Changed payloads and binding maps are rejected.

An independent instruction model proves three prefix, twelve outer-loop and
six inner-loop transfers across two inductive cuts. It compares ordered public
stores, quiet-epoch read multiplicity, saved roles, the fifth argument and all
52 private/incoming bytes. Public stores invalidate the whole epoch, allowing
arbitrary public aliases. FPRs and FCSR remain opaque and unchanged. Every raw
and retail instruction is covered by the stronger abstract transfer proof,
including the unreachable opaque-state branch. Eight deliberate defects fail;
a positive T6/T7 scratch recoloring passes. Exhaustive 65,536 byte-alpha pairs
establish the 0..254 bound separately.

Guest checks pass 592 cases, including 72 public-alias cases and 47,074 ordered
public writes, with equal complete final RAM and returned cursor. Normal
execution reaches 155/160 raw and 154/159 retail words; the same five opaque
branch words, indices 106..110, are unreachable for byte inputs. Native SDK32
checks pass 520 cases each at O0/O2/O3 with strict aliasing and UBSan, complete
255-record and 256-list backing, real graphics macros and six effective source
controls. Aliases that lack a portable C object contract are guest-only cases.

The connected caller check executes 128 cases through eight actual original
words and explicit ten/six-word setup/teardown scaffolding. It verifies all
five arguments, the blue delay-slot store, returned-cursor consumption and
complete RAM equality. This does not claim execution of the full outer caller.

## Production, history and continuation

Both target padders emit the same complete object. The actual natural Make
recipe executes three commands. The linked and production ELF both equal the
independent prediction: **491 declared changed bytes, zero exclusions**, all
6,051 function slots retained, and all 189,088 protected Game-data bytes across
720 owners unchanged. Only this routine and its symbol size change; its nine
neighbors and the known caller remain unchanged. All 2209
frozen inputs pass the explicit task plan. `make tools-check` passes.

Production ELF SHA-256: `03b19221851e515be5260005df27ebc960700e40010bbc84fa35c80bfec097d6`.

Both tools configurations pass **27 focused tests**, six historical-dependency
unit tests and three historical whole-image gates before and after installation.
The focus includes eight new tests, seven actor-projection tests, seven record
draw tests and five actor-effect tests. Twenty unchanged older semantic checks
are explicitly reused by exact fingerprints and AST/provenance, not rerun.
The 17 tools files are committed before the consumer. Historical changes only
append exact coupled snapshots/dependencies and extend the actor-scan snapshot
gate; generation and frozen historical images remain unchanged.

The private sibling overlay has 1108 files, drawn from
{'bootstrap': 1, 'sibling': 347, 'task': 17, 'primary-fallback': 743}. The actual dirty sibling's HEAD, status and all
351 dependency hashes are preserved.
The native Graphify update returned exit 1 and retained all 69,123 existing
IDs: its smaller scan corpus was refused rather than overwriting the graph.
The subsequent scoped AST merge covers 12 files and produces 69,196 nodes /
152,290 links, preserving every old ID and qualification field. The target is
credited once; the seven-word submit placeholder stays uncredited. Commit-hook
retention is checked separately. This is not a full-corpus re-extraction.

Assumptions are quiet mapped/aligned ordinary memory, valid nonwrapping public
backing disjoint from private stack homes, and defined SDK32 C objects for native
checks. Finite execution and symbolic transfer evidence do not establish MMIO,
fault, interrupt, hardware-rendering or gameplay acceptance. No host-port,
frozen Release, ROM or save changes; zero Claude calls and no push.

```sh
python3 -m unittest tools.tests.test_game_projection_filtered_draw_15035d6c_match -v
python3 -m unittest tools.tests.test_game_actor_projection_scan_15036148_match -v
python3 -m unittest tools.tests.test_game_projection_record_draw_15035fe8_match -v
python3 -m unittest tools.tests.test_game_actor_randomized_effect_150f97ec_match -v
python3 -m unittest tools.tests.test_game_list_historical_image -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

Continue with the unfinished 345-word `func_15035808` in the same owner after
freezing the new bank. Its ten-argument interface is measured, but its body
still requires full retail/source/caller qualification and earns no credit.
