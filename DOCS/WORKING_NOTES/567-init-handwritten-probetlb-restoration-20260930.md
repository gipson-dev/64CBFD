# Init handwritten __osProbeTLB restoration

Date: 2026-09-30

## Result

`__osProbeTLB` is restored from a false zero-return C placeholder to its
original handwritten CP0/TLB assembly. The complete 48-word, 192-byte slot at
`0x100273D0..0x10027490` is byte-exact: 46 instruction words followed by two
retail padding words.

The row is now correctly classified as raw assembly. The fresh linked matcher
reports `3,069 / 5,461 (56.20%)` exact C functions overall and
`398 / 492 (80.89%)` in Init, with 2,392 genuinely different C rows overall
and 94 in Init. The exact-C numerator is unchanged; this is an ownership and
denominator correction, not a newly matching C function.

## Ownership

The routine saves CP0 EntryHi, installs the probed virtual page with the
current ASID, executes `tlbp`, rejects a failed probe, then executes `tlbr`.
It reads PageMask and the selected EntryLo half, validates the mapping, forms
the physical address, and restores EntryHi before returning. Its privileged
`mfc0`, `mtc0`, `tlbp`, and `tlbr` instructions and mandatory hazard nops are
not representable as ordinary IDO C.

The generated slice now uses `GLOBAL_ASM` with a dedicated extracted body at
`asm/nonmatchings/generated_probetlb/__osProbeTLB.s`. The existing
`asm/libultra/os/probetlb.s` remains the layout authority, allowing
`pad_generated_object.py` to preserve the final two padding words. No
expected-word guards are used.

## Verification

The focused generated-slice object, complete replacement link, outer
`NON_MATCHING=1` ROM build, project tool checks, whitespace check, and fresh
matcher pass. The rebuilt Init slot at
`build/conker.us.init.code.bin+0x263D0` and pristine retail slot at
`conker.us.bin+0x273D0` compare equal across all 192 bytes. Both have SHA-256:

`349227b84b51cb246abaf9de4bf56eba78054d85575e1bfb09acfdb8d1bc0c28`

## Next boundary

Keep the five documented ownership/compiler-boundary rows parked. Resume with
44-word Game `func_15013D38`, the next ordinary C matcher row.
