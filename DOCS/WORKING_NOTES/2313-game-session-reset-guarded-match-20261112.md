# Game session reset guarded match

Date: 2026-11-12. `func_1500E5C0` replaces its zero-return placeholder in
`conker/src/game_3BA70.c`. Its 83-word retail slot spans VA
`0x1500E5C0..0x1500E70C`, ROM `0x3BA70..0x3BBBC`. It calls three
initializers, clears the session's resource counters, paired byte ranges and
other state, calls `bzero` on a five-byte range, and clears the remaining
record pointers and flags. The original startup caller at `0x1500E534` invokes
it without consuming a return value.

The reset clears the 20 bytes at `D_800E0950` up to `D_800E0964`; the
associated retail resource-ID table also has 20 entries. The shared declaration
is now a 20-element byte array, and the two existing resource functions index
it as an array. This does not add bounds checks to those existing callers.
The resource-owner object rebuilt byte-for-byte unchanged. Local pointer
declarations for the other reset globals follow existing C consumers.

The candidate compiles with a target-only `-Wo,-loopunroll,0` profile; 54 of
83 linked positions match directly. Thirty-one expected-word/relocation guards
normalize the first loop's equivalent end-symbol binding, the paired loops'
register and store scheduling, and two later address-register selections. Nine
rows change relocation lists. The paired loops' original global addresses and
end address retain their measured relationship. The compact source layout is
intentional: the IDO schedule changed when those statements were reformatted.
Both padding implementations produced the same object; the generated-padder
screen used a synthetic slice based on the recorded layout. Each of 31 wrong
expected words and 12 wrong expected relocation lists was rejected; three
incorrect replacements were detected. Eight GNU links across four rebases agree
with independently assembled retail while preserving the relevant array/end
symbol relationships.

The original and candidate agree in 24 bounded guest cases with modeled
initialization helpers, including external write order. Twelve fixtures cover
882 external-access interruption prefixes. A deliberately reordered store
control fails. The original caller instruction window was executed with the
candidate. A 32-bit native screen passes 24 fixtures at O0/O2/O3 and with
trapping undefined-behavior sanitization; shortening the counter loop fails.
These checks do not establish hardware fault behavior, concurrent observer
behavior, or full startup/gameplay acceptance. Native C write order is not
claimed to be identical to the retail instruction order.

The private include-graph inventory found 207 existing source objects that
include `variables.h` directly or transitively. It scanned 780 files, found no
computed includes, and had one unresolved literal include (`PR/sptaskoff.h`);
the inventory does not prove the state of unbuilt or externally generated
sources. The Make plan contained 213 compiler invocations for those objects.
Before/after header overlay comparisons found no changed non-debug sections,
section metadata, diagnostics, function symbols, or named text relocations in
all 213 raw objects; all 27 assembly postprocessing invocations also agreed.
This is an object-level audit, not a claim that all 207 production objects were
rebuilt. The two affected production owners were rebuilt by Make.

The installed tests pass eight checks in each tools environment, using the
same staged test bytes and fingerprinted dependencies. The tools commits
`b043f61` and `3f174d6` precede this consumer change. The standalone tools
checkout's pre-existing work was preserved. Production Make reproduces the
independent linked-image prediction: **292 changed ELF bytes**, zero exclusions,
all function addresses fixed, only this function changed, and all **189,088**
protected data bytes unchanged. The ELF SHA-256 is
`d394e188a7ee80abf8f82f599789225864357f144933b0024c810af434a1ba9a`; the
rebuilt binary SHA-256 is
`547c54a3a6650823484218fd89abb2a24f83828c8126609250007d14c6b3079c` and
matches the independently generated binary. The pre-existing duplicate
`generated_12D630` Make warning and resource-owner compiler warnings remain.
The whole ROM is still not claimed to match retail.
The scoped Graphify refresh retained or relocated all 59,880 previous nodes
with no out-of-scope definition changes. A broad update refused to overwrite
the existing larger graph; no full-corpus extraction is claimed.

Fresh actual-ELF recount: **3,705 / 4,840 (76.55%)** Game and **4,378 / 5,513
(79.41%)** overall, with zero address drift. The Game 80% target needs **167**
more matches. See [Note 2312](2312-game-session-reset-array-and-matching-screen-20261112.md)
for the earlier private candidate and store-order control. The three callbacks
in [Note 2311](2311-game-callback-return-normalization-screen-20261112.md)
remain private and uncredited. A separate PC-port generated output inspected
for `func_1500E5C0` contains a placeholder; its active runtime applicability
was not established, and no host build or gameplay test was performed.
