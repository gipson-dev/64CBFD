# Game eight-record status update match - 2026-11-09

func_150DE32C now queries eight resource records and updates actor/resource
status instead of returning zero. Its complete 75-word, 300-byte slot is exact
after 28 expected-word/relocation normalizations. The semantic C is complete;
this is a guarded match, not a 75-word natural compiler match. The ordinary
O2/g3 profile and frame 0x60 remain unchanged. Source:
conker/src/game/generated_10B7D0.c; original assembly: conker/asm/10B7D0.s.

Production total **4,290 / 5,513 (77.82%)**, Game **3,617 / 4,840 (74.73%)**,
Init 492/492 and Debugger 181/181. Zero address drift; 1,223 still different.
**121** further accepted matches are needed for 80%; the wider goal stays active.

## Recovered interface and behavior

VA150DE32C..150DE458, ROM10B7DC..10B908. The correct interface is
`void(s32 x, s32 y, s32 z)`. The three coordinates are signed integers. They are
neither output pointers nor incoming floats. The whole-retail aligned-word
census found no direct J/JAL entry encoding and no aligned entry/interior
address value. Computed callers remain possible; no complete caller claim is made.

Before any helper, the routine snapshots both complete eight-byte tables:
D_80088950 =24,25,26,27,13,48,49,50 and
D_80088958 =246,243,240,237,0,0,0,0. The loop visits eight snapshotted unsigned
record IDs and tags, reloading D_800D3098 each iteration. Records have 52-byte
stride. The local record declaration copies the existing generated_CDE80.c
member layout/types, preserving cross-translation-unit compatibility.

func_150A32B4 receives the selected record address as s32 plus x/y/z. Any
nonzero result enters the status path. A nonzero unsigned tag is resolved by
func_151149AC(u8), then byte 0x73 has only its low two bits set. A zero tag calls
func_150A2864(identity,1). The second argument is required: it sets record
byte 0x14 and clears the matching bit in sixteen active-set rows. The lookup
helper takes one argument; retail's otherwise-live A1 is not a second parameter.
Names/comments describe recovered behavior, not asserted original retail names.

The point helper's original 31 words convert signed coordinates to float32,
initialize seven query fields, and invert the collision service's zero result.
The original 28-word lookup scans 160-byte actor records at tag byte 0x72.
The original 55-word status helper handles the record byte and 64-bit row masks.
All three are already byte-exact in the frozen production baseline. Connected
guest checks execute those original instructions; collision results/mutations
and the SDK split64 shift are bounded services. No hardware/FCSR claim is made.
Native fixtures supply valid records and successful nonzero-tag lookups.
There is no new NULL guard; portable-C fault behavior is not claimed.

## Compiler shape and normalization

All 75 words and original frame/saved-register lifetime align. The C compiler
places private index/tag snapshots at SP+0x58/SP+0x50, versus retail SP+0x50/SP+0x48.
Twenty-eight guarded words restore the private copy/layout schedule and a
closed temporary-register allocation cycle. Call sites, branches, loop extent,
and branch-delay pointer update already align. No words are inserted or omitted.
Alternative declaration/initializer/copy/profile screens did not improve the
natural match and remain private, uncredited experiments.

Every new guard requires the exact raw word and exact relocation annotations.
Both padders reject stale words and stale bindings. The entire inherited guard
manifest remains an identical byte prefix; exactly 28 rows are appended for this
function. Shared headers, compiler profiles and Makefile are unchanged.
The raw compiler body SHA-256 is
49f6822377acf4b42c171481fe17891ac81b446ca1bc1ce84491198511e91aa2.

## Qualification and whole-image audit

- Complete owner: eight raw and padded neighbor functions/bindings stay fixed;
  pools remain fixed; no compiler diagnostics. New general-register usage is
  recorded in the compact object's mask; all other register metadata is fixed.
  Both independent padders agree and yield the literal 75-word retail slot.
- Actual Make runs in an owned mirror with an identical Makefile, normal
  source path and proposed guard manifest. Its compiler/padder/assembler output
  is byte-identical to the independently qualified object. Production repeats
  the real recipe with one compiler invocation and no profile change.
- Guest: 480 cases per body, 1,440 executions, all 75 words visited, 173 access-cut
  prefix pairs including 16 delay-slot faults. Raw C public memory/calls match
  the independent contract; normalized/original complete literal state agrees.
  Six rebased layouts add 18 cases. Forty cases connect all three original
  helpers, including signed32-to-float boundaries and mutable-global providers.
- Native32 O0/O2/O3: 736 defined-domain cases per profile with strict aliasing
  and UBSan. Checks cover forwarded addresses/coordinates, table snapshots,
  unsigned tags, actor bytes, record status and active-set masks. Eleven
  compiled semantic mutations are effective in both native and IDO guest runs.
- Strict ELF prediction changes only the 300-byte target body, its symbol size
 12->300, and a named two-symbol GNU-ld bucket permutation. D_800A2110 and
 D_8009D740 exchange complete metadata records and equal-length string slots;
 their named values/types remain fixed. The permutation is predicted from the
 predecessor, never copied from the new image. **243 bytes change, zero
 exclusions**, including the 18 metadata bytes beyond body/extent changes.
 Six independent image corruptions are rejected.
- All 6,052 function addresses and every other function body remain fixed.
 Protected data matches exactly. Progress CSV bytes remain fixed. Production
 object/ELF match prediction; recount adds exactly one total/Game exact match.
 The inherited whole-ROM checksum mismatch still makes make all exit 2;
 overall retail-ROM equality is not claimed.

Five focused checks pass before and after installation in both tools
environments. The sibling uses an isolated five-module overlay with explicit
consumer roots and recorded dependency fingerprints/fallbacks. Its 2,434 inherited
dirty paths are preserved. Fresh shared smoke runs accompany three unchanged,
exactly fingerprinted regression reuses per copy; reuses are not fresh tests.
The package freezes 591 inputs. Receipts remain under
conker/build/game-route-record-update-150DE32C-match/.

Tools commit before consumer; no push. Root README gets aggregate rows only.
Graphify receives a scoped AST refresh with old-node retention, not a complete
corpus semantic extraction. No host-port Release artifact is touched.
Routine work uses zero Claude calls. Next: audit the adjacent func_150DE458
stub and its helper/caller contract; it remains uncredited.

Focused WSL check:
python3 -m unittest tools.tests.test_game_record_status_update_150de32c_match -v

Production ELF SHA-256: be47a7e6f1ef41f3d8113886fafd085ac0a0e5cfa2827979b7ede8f9b31098e5.
Guard SHA-256: 718c890ae443cc930f7b307e73fcb3dae942411728d10c3bc511670ea7095e04.
