# Game view reset private recovery and prefix proof

Date: 2026-11-15. `func_15017640` is privately recovered as a complete
`void func_15017640(void)` view/projection reset. It remains **uninstalled,
unmatched and uncredited**. The live `conker/src/game_44A90.c` still contains
its original placeholder; no production source, headers, guards, objects,
progress rows or ELF change during this screen.

The routine occupies `0x15017640..0x15017788`, ROM `0x44AF0..0x44C38`:
**82 body words / 328 bytes**, followed by two zero alignment words to the
next entry at `0x15017790`. It has a conventional **0x28-byte frame**, saves
RA at SP+0x24, and calls `bzero` and `guPerspective` through the o32 interface.
The actual-Game JAL census finds one direct call, at ROM **0x355E0** /
VA **0x15008130**, in `func_15007B3C`. There are no aligned literal pointers
to this entry in the retained input. The next caller instruction after the
return is a JAL to `func_1501CC3C`; its complete window/use audit is still open.

## Recovered behavior and source ownership

The complete body resets the motion vector, copies three **signed 16-bit**
position defaults into floats, initializes six scale values, clears six
record flags at byte 13 of their 16-byte records, clears the 192-byte scratch
region, and submits the perspective matrix/normalization outputs with the
original 50.0, 60.6, 53.0, live far-plane, and 1.0 float arguments.

The old commented draft cleared only four record flags. Retail clears bytes
at **0x800D246D, 0x800D247D, 0x800D248D, 0x800D249D, 0x800D24AD,
0x800D24BD**. The recovered six-record loop preserves all six. The candidate
also replaces inaccurate local uses of the generic scalar declarations with
owner-local, correctly sized declarations for the Mtx, normalization halfword,
six-record table and 192-byte scratch array. The shared `variables.h` is not
edited. The other owner function retains its original declarations/meaning.

Two complete semantic forms compile under the current O2/g3 owner profile:

| Form | Body words | Frame | Binding rows | Real word differences |
| --- | ---: | ---: | ---: | ---: |
| Indexed scale loop | 82 | 0x28 | 36 | 20 |
| Pointer scale loop | 82 | 0x28 | 36 | 13 |

Both preserve the one other owner's complete function and normalized pools.
The best raw payload SHA-256 is
`49ca7bef582aee1c617ef230bef9a97ba6a54f28917b8213384cda86fd714d80`.
These are relocation-bound word comparisons at the retail addresses; they
are not GNU-link/rebase or padded-slot qualification.

## Fresh guest and semantic control evidence

The independent public-memory model agrees across retail and both compiled
forms for **3,456 cases / three streams**, with all **82 instructions** in
each stream visited. Cases cover the cross product of six signed coordinate
boundaries, eight provider-effect modes and two valid stack phases. Far-plane
values include zero, negative zero, finite values and a signaling-NaN bit
pattern for this bounded guest packet-copy screen.

Checks compare complete public bytes, provider argument packets and both
provider-entry snapshots. Bounded providers can mutate the far-plane after
the scratch clear, overwrite position/scale/flag state, clobber outgoing homes
and caller-saved registers/FPRs, and produce observable matrix/normalization
outputs. The far-plane is read after bzero, and provider changes are retained.
These hooks qualify the caller's interface and sequencing; they do not execute
the actual SDK projection routine.

Five **compiled C source controls** complete guest execution and fail the
independent public-state/packet checks:

- The old four-record flag reset.
- Unsigned coordinate defaults.
- A truncated 0x40-byte scratch clear.
- A far-plane value captured before the first provider.
- An incorrect projection aspect constant.

The controls must fail the comparisons; an unsupported instruction or executor
assertion is not accepted as their semantic rejection.

## Closed prefix schedule proof

The pointer-loop form has only **13 differing words**, all within the first
34 instructions. An independent straight-line symbolic executor proves that
prefix for arbitrary symbolic input halfwords and incoming register/FPR
values **at the fixed retail addresses**:

- Identical ordered public reads, stores and saved-RA access.
- Identical memory results and all FPRs.
- Identical GPRs except A2, which retains unpassed input junk in the raw form
  and holds the no-longer-needed motion-vector address in retail.
- An identical **48-instruction suffix**. A suffix use scan proves A2 is not
  explicitly read before its constant overwrite; the intervening bzero takes
  only A0/A1. The provider contract excludes inspection of unpassed register
  junk. Three effective controls reject a changed motion destination, unsigned
  input load or incorrect motion store.

No normalizer or word guards are installed. This certificate closes the
observed prefix schedule at the present data layout; it does not substitute
for relocation/rebase, native C or production-image gates.

## Retained state and next gates

**817 production inputs** were frozen after the committed Huffman restoration
and remain unchanged before and after the private suite. Source/profile,
object, layout, original assembly, compiler, protected headers and ELF are
retained in `conker/build/game-view-reset-15017640-private/production-baseline/`.
The mounted suite runs four tests: raw owner forms, independent guest state,
compiled source controls and the closed prefix proof. All four pass freshly
in **29.598 seconds** mounted and **35.540 seconds** in the sibling overlay.
Exact task-source hashes are retained in `mounted-suite.json` and
`sibling-suite.json`. The sibling retains HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all **2,434 Windows-Git dirty
paths** byte for byte, with before/after status SHA-256
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify extraction of the four tools files retains all **61,356 old
node IDs**, producing **61,396 nodes / 115,275 links**; no full-corpus
re-extraction is claimed.

Next work remains on this same routine:

1. Qualify native32 C at O0/O2/O3 with correctly sized storage and meaningful
   source controls; distinguish finite C packets from guest-only NaN bit tests.
2. Execute the original caller window, prove the ignored return convention,
   and qualify relevant actual SDK/bzero behavior or state explicit limits.
3. Encode the 13 checked relocation-aware schedule guards and independently
   audit the prefix proof against those exact raw/normalized fingerprints.
4. Run both full-owner padders, independent data/code rebases and GNU links,
   actual Make, strict full-image and protected-data/neighbor audits.
5. Only then install the C source, rebuild, rerun the focused installed suite,
   recount the real ELF and assign C-match credit.

Production remains **4,498 / 5,514 exact C functions (81.57%)**, Game
**3,825 / 4,841 (79.01%)**, zero drift, **189** further C matches to 85%.
The root README aggregate rows remain unchanged for this private recovery.
The wider 85% goal is active. Host source/Release and private inputs are
untouched. Commit tools first, then this note/index handoff and consumer pin;
do not push.

Tools commit: `4550aa5c82a38866935578ae727726530e989c5d`.
The installed production baseline is the preceding
[handwritten Huffman restoration](2461-game-handwritten-huffman-pair-restoration-20261115.md),
consumer commit `7e62df2b5b217e3ab600b731f374b69b96ee44ae`.
