# Paired randomized effect constructor matches

Date: 2026-11-12. `func_151AF388` in `conker/src/game/generated_1D92F0.c`
and `func_151B50F4` in `conker/src/game/generated_1E2180.c` replace
zero-return placeholders. Their executable bodies are each 82 words at VA
`0x151AF388..0x151AF4D0` and `0x151B50F4..0x151B523C`; the second layout
slot also contains a padding word through `0x151B5240`.

The bodies reverse and scale three incoming velocity values, consume five
random samples in the original order, then pass the constructed fields to
`func_151D9014`. Their retail instructions differ at only four constant
references, and the two referenced four-float tables contain the same bits.
Their respective original adapters are `func_151AF338` and `func_151B50A4`.

Each IDO output has 82 words. Ten expected-word guards per body normalize the
opening instruction schedule and a byte temporary's stack placement; neither
adds words. Both padders reproduce independently assembled retail code and
relocations. Twelve GNU rebases, 102 bounded access-cut triples and twenty
corrupted-guard rejections pass for each body.

Each retail body and C candidate agree in 416 modeled-helper guest cases,
including the actual constant values, with all 82 retail words reached. Each
native SDK32 O0/O2/O3 run passes 416 cases and twelve effective negative
controls under UBSan. Each original wrapper window passes 416 modeled-helper
cases. These checks cover valid modeled inputs; they do not establish full
gameplay, hardware fault behavior, or the complete callers and helpers.

The combined actual Make and independent linked-image audit agree: 707 changed
bytes, ten verified symbol-order groups, zero exclusions. All 6,050 function
addresses, 32 and five other functions in the respective owners, and 189,088
protected Game-data bytes remain unchanged. Actual ELF SHA-256:
`24dfde3eac3e4aac3c714d582f5e35e6f15ac36336d3c74b84a64c7d7bf5924f`. The existing whole-ROM checksum mismatch remains.

Fresh ELF recount: **3,690 / 4,840 (76.24%)** Game and **4,363 / 5,513
(79.14%)** overall, zero drift. The Game 80% target needs 182 more functions.
Tools commit `e639d1d8c08d19e189c3e0d3eebc9834c202d678` precedes this consumer change.

A separate candidate-selection caution: the recorded `func_150AE280` slot
starts with a stack switch and branches into the earlier `func_150ADAF0`
epilogue; a second routine begins at `0x150AE2A0` within the same recorded
slot. Retail code calls the first entry at `0x1509F9A8` and `0x1509FBB4`,
and ROM data at `0x22E39C` contains the second address. Do not replace the
whole slot as one ordinary C function; resolve ownership and both entries
before conversion. This observation does not change the matching count.
