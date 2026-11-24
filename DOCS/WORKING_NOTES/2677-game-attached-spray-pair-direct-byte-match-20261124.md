# Attached spray pair direct byte match - 2026-11-24

`func_150C7020` replaces its zero-return placeholder with complete semantic C.
All **104 instruction words emit directly**, with the original **88-byte frame**,
**nine relocation sites**, and **zero guards, insertions or omissions**.
Production advances from 4,656 to **4,657 / 5,528 (84.24%)**; Game advances
to **3,984 / 4,855 (82.06%)**. Init remains 492/492 and Debugger 181/181.
Zero address drift; 871 still different; **42 more matches reach 85%**.
Conversion rows stay fixed because this replaces an existing C stub.

Source: `conker/src/game/generated_F44D0.c`; original: `conker/asm/F44D0.s:11`.
VA 150C7020..150C71C0, ROM F44D0..F4670, 416-byte body and slot.
Both functions in this owner now match: the neighboring point-spray callback
`func_150C71C0` remains byte-exact and receives no duplicate credit.

## Source and ABI recovery

The recovered interface is `void(u8 *owner, s16 lifetime, u8 unusedOpacity,
s32 unusedMode)`. Null owners skip all providers and packet accesses. For a
present owner, first call `func_1516962C(0x29, owner, 0x12)`, then capture the
owner tag at byte 3B, owner pointer, and a sparse 60-byte packet at incoming
SP-60. The packet has 46 initialized bytes and 14 padding bytes; it is not
blanket-zeroed. A nonzero signed lifetime sets mode 2; zero selects lifetime
300 and mode 0. Sentinel fields retain their original signed byte widths.

The first submission uses event 13 and float fields [2,0,34,-15,0,34]. The
second uses event 12 and [-2,0,34,15,0,34]. Each submission gets two ordered
integer RNG draws: unsigned %66+35 and unsigned %26+25. The source explicitly
sequences these statements. After the first submission, overwrite only the
fields overwritten by retail; retain all other provider changes to the packet.
The helper returns are ignored, and the target returns void.

The first complete C draft matches all 104 words with either an external
coefficient or a literal. The accepted source uses external **D_800A0490**,
whose retained bits are **3EF1A9FD** (0.4720000327f). This avoids adding a
second literal-pool user. The existing Makefile and fail-closed point-spray
pool checker are unchanged. They still pin the neighbor's 99 raw words,
16 bindings and 16-byte pool (3ED0624E followed by twelve alignment zeros).
Both raw and padded neighbor bodies/bindings remain fixed, as do all data.

## Qualification evidence and limits

* Guest: 552 cases in each of four streams (raw C, both padded C objects,
  original ASM), all 104 instructions executed, and 85 access-fault quads.
  Complete 60-byte packet snapshots include seeded padding. Check signed
  lifetime boundaries, zero/absent owners, all 66/26 RNG residues, u32 high
  values, both stack phases, provider changes, and guest-only incoming-home
  mutations. Full registers, calls, memory and instruction-access traces agree.
* Native SDK32: 383 cases per O0/O2/O3 profile, strict aliasing and UBSan,
  actual 60-byte type and field-offset assertions. Compare initialized fields
  with explicit guest/native endian conversion. No claim is made for native
  uninitialized padding or guest stack-home mutations. Ten deliberate source
  errors produce comparison exit 42; no signal or sanitizer trap counts.
* Full aligned pristine-ROM census finds exactly two JAL sites (ROM 5587C
  and 1C1A58), no entry pointers, and no unknown additional entry callers.
  Execute both actual caller routes through all four target streams: 256
  cases. The original 17-word wrapper supplies lifetime 500; the eight-word
  dispatch window sign-extends a computed lifetime and forces its own return
  value after the call. Both ignore target V0. A wrong-A0 control is effective.
* The original 18-word integer RNG executes 288 cases per four streams,
  checking four 64-bit seed transitions against an independent seed formula.
  A wrong return-shift control is effective. This does not model a float RNG.
* Both independent padders expose all 104 single-word corruptions (208 visible
  differences) and reject or visibly mark an oversized body. Sixteen separate
  GNU links and 32 rebased guest runs check HI carry, negative LO and JAL regions.
* The actual four-command Make route reproduces the qualified owner exactly,
  including the unchanged neighbor pool check. The frozen before-C owner plus
  original target ASM independently predicts the complete linked ELF: **325
  changed bytes, zero exclusions**. Every other function body/address/extent,
  all guard rows, conversion rows, protected sections, and all **189,088 Game
  data bytes / 720 data owners** stay fixed. Production equals that prediction.

The original 15-word preparation helper and 39-word submission helper are
already retail-exact. Their complete symbol extents and current bytes are
verified. The preparation interface narrows its third argument to a byte;
the submission helper returns a pointer. Both internals are contracted in target tests;
neither receives added matching credit. Caller windows qualify the target ABI,
not complete current-parent execution, effect-system or gameplay acceptance.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 3.506s | 1 fresh / 4 fingerprinted reuse |
| preinstall-sibling | 6.239s | 1 fresh / 4 fingerprinted reuse |
| installed-primary | 345.702s | 5 fresh / 0 fingerprinted reuse |
| installed-sibling | 234.950s | 5 fresh / 0 fingerprinted reuse |

The initial complete preinstall suites passed all five gates. A helper-window
off-by-one correction then refreshed only caller/RNG gate 4, with the other
four gates explicitly reused under unchanged source/object/data/tool hashes.
Both final installed suites rerun all five gates fresh with the corrected extent
and the local preparation declaration aligned to the existing void*/u8 ABI.
The first declaration recheck correctly stopped credit at the frozen-document
input gate; six owned documentation edits were parked and restored exactly.
Function bodies, padded owner and complete production image are unchanged
by this declaration-only cleanup.
Shared `make tools-check` passes. The second-copy run uses an isolated overlay
of the separately audited tools checkout, preserving its existing edits. The
neighbor's prior semantic receipts are reused only with its exact raw/padded
body, relative relocations, source body, globals, helper and guard inputs fixed;
they are not described as fresh neighbor-suite runs.

Consumer baseline: `01c627047aa473b47bc4c30c99bf9c17f2799365`.
Tools baseline: `73aa2e866a488b07b4235f9b711d9d4c44d2c4f4`.
Tools qualification commit: `80fab1afb75905514af137359e46e04eeab215fc`.
Final ABI declaration qualification: `421a1cdef6778e8a5905ac666447caab1064483b`.
ELF SHA256: `77859cc775aed6a5a59852662fdaf3557066b6db567012ef4eac702cf77f9c31`.
Padded owner SHA256: `1a491d5a113daa58b93268051281d7c1e269e2d0bed019445b2318bb1a961e3c`.

Codex owns all writes and validation; routine direct recovery uses zero Claude
calls. Graphify was queried first; after code edits run native update and a
scoped AST merge retaining every old ID and prior qualification. Record actual
hook producers as terminal before that final merge and bank the committed
inputs. No full-corpus re-extraction, host/Release change or push is claimed.

Next screened candidate: the 104-word `func_150C8730` matrix/effect constructor
in generated_F5800. It gates on an attached actor/type, derives matrix values,
constructs an effect, and writes transformed coordinates and signed angles.
The private dimensions and renderer candidates remain uncredited. Goal stays
85% of total C functions; this checkpoint does not complete it.
