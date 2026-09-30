# Init single-node release recycler match

Date: 2026-09-30

`func_10009BE4` occupies 54 words and 216 bytes at
`0x10009BE4..0x10009CBC`. Its normal path returns the node's retained value
through the pointer at offset `0xC`, removes the node from the active doubly
linked list rooted at `D_800406A4`, and inserts it after the reusable-list
head rooted at `D_800406B0`. The recovered C repairs both active-list
directions, handles active-head removal, and distinguishes empty and nonempty
reusable lists.

An odd input pointer is a retail sentinel rather than a list node. That path
writes `0x0F000004` to `D_8003C8E0`, calls `func_150AD770`, and returns without
dereferencing the pointer.

Twenty-eight of the 54 words emit directly from semantic C. Twenty-six
stale-checked guards preserve two closed IDO schedules: twelve relocation-
aware words move the retained `D_800406A0` address around the sentinel value,
store, and call; three words retain the manager in retail's `a1` lifetime;
and eleven words restore the reusable-list successor and branch-likely splice
schedule. The 24-byte frame, active-list unlink, alias stores, epilogue, and
all behavior remain source-derived.

The focused object build, exhaustive guarded relink, authoritative matcher,
and direct section-span comparison pass. The linked Init section and pristine
image share SHA-256
`667204c47707c5e69f2314fde2be2e4f4afb0075e1e053824489d3e381190a67`
across all 216 bytes.

The matcher advances to `3,091 / 5,457 (56.64%)` overall and
`408 / 488 (83.61%)` in Init, with zero address drift and 80 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
