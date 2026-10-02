# Init meta-handler layout and assembly provenance correction

Date: 2026-10-02

Follow-up correction: Note 731 identifies Init `__sinf` as a second supported
compiler-generated C candidate. The blanket classification of all 23
separated assembly rows as handwritten, and the "one supported remaining"
conclusion below, are superseded. The audio layout repair and `init_5AB0`
shared-register findings remain valid.

This audit corrects two conclusions in Note 729 using direct guest assembly
and linked-body evidence.

## Audio layout repair

`__n_CSPHandleMetaMsg` was declared static, omitted from the padded object,
and masked by a legacy absolute assignment in `undefined_funcs.us.txt`.
Its retail span at `0x10015044..0x10015310` was zero-filled. The new C event
handler's local `.text` relocation landed at `0x10015000`, inside the MIDI
handler. The prior matcher called that address drift, but it did not prove
the callee body existed. This was a missing-body and relocation defect.

The meta handler now has external linkage and an explicit retail layout row.
The obsolete absolute assignment is removed. The one existing voice-handler
guard that consumed its old local relocation now expects the named external
relocation; its replacement instruction is unchanged. The event-handler call
resolves to the actual function definition at `0x10015044`. The object also
depends on Makefile so its rodata anchor settings trigger recompilation.

No new word guards are needed. Both linked bodies match the original binary:

| Routine | Address | Words | Bytes | Result |
| --- | --- | ---: | ---: | --- |
| `__n_CSPHandleNextSeqEvent` | `0x10014048` | 69 | 276 | Exact |
| `__n_CSPHandleMetaMsg` | `0x10015044` | 179 | 716 | Exact |

SHA-256 of the exact instruction spans:

```text
NextSeqEvent b08a8977a6f9626153d1ec90c415f99c83afd413839506c8613ac8f347e3fa4e
MetaMsg      1da08dd80bbe00d5f3485b883153b631eaba88c1c583249df2c74e21a3da2041
```

The exposed meta function adds one function to the measured denominator.
The MIDI handler's actual span is 3,816 bytes, rather than the old merged
4,532-byte row. Init is 489 / 539 C functions, with all 489 C rows exact.
Total is 5,458 / 6,042 C functions, with 3,237 exact, zero address-drift rows,
and 2,221 different C rows. The original total code-byte denominator is
unchanged. The source for the meta handler already existed; this change
restores its compiled body to the linked image and corrects its measurement.

## Assembly provenance correction

Ordinary instructions alone do not establish compiler-generated code.
`func_10006380` saves `$ra` at its caller's `sp+0xA68`, consumes and updates
live `$s7`, `$gp`, and `$fp`, and calls other fragments sharing that state.
It cannot be replaced independently by an ordinary ABI C function. The
cross-project description calling it non-handwritten was insufficient proof.

The ten decompressor rows from `func_10006240` through `func_1000709C` total
3,984 bytes. Their shared frame, register state, floating-register integer
storage, and extra arguments in temporary registers establish assembly
ownership for the chain. A semantic whole-decompressor implementation would
be a separate ABI-changing undertaking, rather than an isolated matching
function conversion.

`func_100079D8` and `func_10007A24` directly match handwritten
`__osEnqueueThread` and `__osPopThread` in local
`tools/ultralib/src/os/exceptasm.s`. Their combined span is 96 bytes.
`func_10007D28` is a 120-byte glyph helper that consumes live `$t1`, `$t2`,
`$t3`, and `$t4` from its handwritten caller, so it also retains assembly
ownership. The 76-byte `func_10005BE0` retains its documented handwritten
memory-fill ownership. These 14 rows account for the 4,276 bytes previously
called plain-instruction candidates.

Together with the 12 explicitly marked low-level rows, the evidence supports
retaining the complete `init_5AB0` segment as assembly. No segment split is
needed for the current matching queue. The other 23 separated handwritten
rows remain assembly. The one supported remaining Init C conversion is
`__n_CSPHandleMIDIMsg`, now correctly bounded to 954 words / 3,816 bytes.

## Verification and resume

The focused audio object and full non-matching code rebuild pass. A fresh
link with the obsolete absolute assignment removed passes the complete
matcher. Direct linked-byte comparison independently confirms both audio
spans. The rebuilt binary is regenerated; project tool checks and whitespace
checks pass. No fresh gameplay run was performed.

Resume with `__n_CSPHandleMIDIMsg`, using local libultra `csplayer.c` as the
reference and the guest assembly for Rare's custom behavior. Preserve the
new explicit meta-handler boundary and all existing voice-handler guards.
