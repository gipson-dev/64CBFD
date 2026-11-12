# Colored-dispatch Make warning fix

Date: 2026-11-12. The `generated_12DAB0` mixed-profile object is now listed
among mixed-profile generated slices. Its explicit Make rule is selected once
instead of overriding the generic rule. The warning introduced in
[Note 2305](2305-game-actor-colored-dispatch-direct-match-20261112.md) is gone;
the unrelated pre-existing `generated_12D630` override warning remains.

The target-specific primary and no-constant-reuse compiles, function override,
retail table binding and assembler step remain the same. Actual production
rebuilds retained the exact target and caller object hashes and the complete
ELF and binary hashes. Fresh match progress remains **3,703 / 4,840 (76.51%)**
Game and **4,376 / 5,513 (79.38%)** overall, with zero address drift. The
existing whole-ROM checksum mismatch was not retested in this build-routing
change; the binary hash was unchanged.

The tools experiment and manifest accept the verified previous and corrected
Makefile states and now test that the target warning is absent while both
compiler profiles and the function override remain present. Focused pre-change
checks passed against the mounted and standalone tools environments. Seven
unchanged target-test files and 318 loaded dependencies per environment were
fingerprinted against the preceding installed-suite receipts; the unchanged
semantic checks were reused with those exact fingerprints. Tools commit
`7b9cdb9b38c9221b0ff20b0911d3e7dba2e5940b` precedes the consumer change.
