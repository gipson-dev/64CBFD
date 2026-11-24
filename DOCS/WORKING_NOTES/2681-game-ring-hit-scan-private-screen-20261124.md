# Ring actor scan private screen - 2026-11-24

`func_150C9BDC` remains its original production placeholder. No C body or guards
were installed and matching credit is zero. Production counts stay unchanged by
this experiment; the adjacent callback adopted in Note 2682 is separate.

Retail VA 150C9BDC..150C9DC4, ROM F708C..F7274: 122 words, frame 104. The original
code scans 25 records from D_800CC2D0 to exclusive D_800D121C with stride 0x32C.
It requires nonzero state, a +0x28 float <20, zero immune and a supported
state/type combination. Unordered floats fail. Ordered predicates select the ring's trailing
250-unit band; type 0x53 gets state writes and an indexed owner-byte check, while
other eligible actors receive func_1505D024(actor,0x6000E,angle,-1).
The SDK struct127 fields and helper's struct127*/s32/u16/s32 declaration agree
with the inspected instructions. Full caller/guest/native qualification is open.

Private folder: `conker/build/game-ring-hit-scan-150c9bdc-private`.
The initial complete C for-loop emits 122 words/frame104 but introduces an empty
loop check and different branch-delay updates. A bottom-tested do/while emits
121 words/frame104 and recovers the retail branch geometry after a one-word
opening shift. It is not installable. Its literal position comparison reports
119 differences including the missing word; that is not an aligned semantic
comparison and must not be presented as matching credit.

The measured residual is narrow: retail independently materializes the table
base twice; the compiler shares it and moves it to the induction register.
After aligning the body by one word, the integer register cycle S3->S6, S4->S3,
S5->S4, S6->S5 leaves four floating register-use differences (raw words 69,71,72,
76, final gap F14 instead of F0). All 17 epilogue words are identical after the
shift. Body relocation offsets likewise move by four bytes. This diagnosis is
not a validated instruction rewrite, ABI proof or semantic equivalence claim.

Twenty-four bounded source forms were compiled across screen.py, fit.py,
fit_address.py, fit_lifetimes.py, fit_declarations.py and fit_review.py. Pointer
views, initializer address spelling, declarations, explicit stages and a named
gap did not solve the deficit. Repeated inline gap comparison regresses to
118 words/frame96. One read-only Claude Code Pro advisory completed in 147.625s,
with no built-in tools, MCP servers or tool calls; packet SHA256:
`0a66b1a78ceaab1e475fc3fdd942358101d7f6a9ef0925db8794a8ccf06298cb`.
Its three proposed source experiments were compiled and gave unchanged
121-word/frame104 results. They were not adopted. No second call was made.

`residual_audit.py` verifies all 18 raw neighbors, unchanged raw pools and the
existing 212-word updater/16-byte pool checker against the complete candidate
owner. It records the exact four residuals and register cycle in
`residual-audit.json`. Padded/image/caller/guest/native gates remain open for
this target. Do not promote it from a length/frame or allocation observation.

The initial freeze uses the committed fb58b27d consumer/e45a0051 tools baseline,
3528 inputs / 2120 copies. Old whole-owner drafts predate later recoveries: graft
only this target's body onto a fresh baseline if revisiting. Preserve all adopted
ring bodies, prior guards, the updater pool checker and private evidence.
The wider 85% matching goal remains active.
