# Game unique-asset loading lifetime screen

Date: 2026-11-13. This is a private screen of `func_15016850`, not a
production match. The retail function occupies 84 words at
`0x15016850..0x150169A0` in `generated_43D00`. It scans 0x30-byte source
records, skips IDs already present in the halfword list, optionally calls the
resource helper for IDs below `0xBB`, and appends an ID and resource pointer
only when the persistent helper-output slot is nonzero. The count byte is
reloaded after the helper, but not when an ID skips that call. These access
and lifetime distinctions are part of the pending qualification.

A new 24-shape screen varied the ID type, count access, initialization and
loop shape. The earlier direct-global shape retains the retail 84-word extent
but saves eight registers, versus retail's seven. Referencing the count at the
adjacent address `D_800D20FC + 4` gives a seven-register shape: the `while`
variant emits 84 words and has 71 same-position word differences; the `do`
variant emits 80 words and has 74. The raw byte-difference totals include
register allocation, scheduling, branches and relocations; they do not prove
the mismatches are independently movable or guardable.

The byte-pointer expression crosses the declared pointer object's boundary,
so it is only an experiment and must not be promoted as portable C. A separate
proposal names the adjacent pointer and count as fields of a grouped global;
its ownership, type and alias relationship to the actual program have not yet
been established. Both grouped proposals compile in the complete owner with
the other two functions, pools and diagnostics unchanged. Their output pointer
is at `sp+0x48` in a `0x60` frame, while retail uses `sp+0x50` in the same
frame. A further 24 local-layout shapes did not solve the physical stack-slot
offset: shifting the output to `sp+0x50` also increased the frame to `0x68`.

A bounded guest screen compared retail, two byte-pointer variants, and the two
complete-owner grouped variants against an independent model for 63
disjoint-memory cases each. It exercises duplicates, IDs above the helper
threshold, null and non-null modeled helper outputs, and helper mutations of
the live count. This is not alias, fault-prefix, original-caller, native,
padder, full-image, or runtime qualification. In particular, the different
stack slot and the hypothesized grouped declaration remain unresolved.

The screen scripts, object files and receipts are retained in the ignored
`conker/build/game-unique-asset-load-15016850-screen/` directory. A separate
retail duplicate census found no additional nonexact Game C functions with an
already-exact C donor under its exact instruction layout after masking direct
jump targets, among functions of 20 to 500 words. It does not rule out other
similar code or shorter/longer candidates.

Both grouped owner shapes were also compiled at `-O1`, `-O2` and `-O3`.
`-O1` changed the frame to `0x30` and increased the extent to 91 or 94 words;
`-O3` produced the same target word counts and positional differences as
`-O2`, with an additional tool warning. Neither profile resolved the screen.

Production source and match counts are unchanged. Game remains
**3,772 / 4,843 (77.89%)**, with **103** further matches needed for 80%.
Next, establish a valid shared declaration and the retail output-slot lifetime,
then qualify access order and aliases before considering instruction guards.
