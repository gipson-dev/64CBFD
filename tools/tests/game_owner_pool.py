"""Compare copied-owner pools by actual relocation ownership, not packed PCs."""

import hashlib
import json
import struct

from tools.experiments.game_actor_classifier_candidates import sections
from tools.experiments import game_texture_resolver_candidates as resolver
from tools.pad_generated_object import ELF_HEADER, SECTION_HEADER, SYMBOL, RELOCATION, parse_object, read_c_string


def normalized_pools(path):
    data = path.read_bytes()
    header = ELF_HEADER.unpack_from(data)
    headers = [SECTION_HEADER.unpack_from(data, header[6] + i * header[11]) for i in range(header[12])]
    names = headers[header[13]]
    strings = data[names[4]:names[4] + names[5]]
    named = {read_c_string(strings, h[0]): (i, h) for i, h in enumerate(headers)}
    text_index = named['.text'][0]
    symtab = named['.symtab'][1]
    symbols = [SYMBOL.unpack_from(data, offset) for offset in
        range(symtab[4], symtab[4] + symtab[5], symtab[9] or SYMBOL.size)]
    functions = parse_object(path)[1]
    pools, result = sections(path), {}
    for name in ('.rodata', '.data'):
        if name not in pools:
            result[name] = None
            continue
        raw = bytearray(pools[name][1])
        identities = []
        for h in headers:
            if h[1] != 9 or h[7] != named[name][0]:
                continue
            for offset in range(h[4], h[4] + h[5], h[9] or RELOCATION.size):
                location, info = RELOCATION.unpack_from(data, offset)
                symbol = symbols[info >> 8]
                if info & 255 != 2 or symbol[5] != text_index:
                    raise ValueError('unsupported pool relocation')
                value = struct.unpack_from('>I', raw, location)[0] + symbol[1]
                owners = [(n, value - f['value']) for n, f in functions.items()
                    if f['value'] <= value < f['value'] + f['size']]
                if len(owners) != 1:
                    raise ValueError('unowned pool target')
                identities.append((location, *owners[0]))
                struct.pack_into('>I', raw, location, 0)
        result[name] = (bytes(raw), tuple(sorted(identities)))
    return result


def assert_guard_history(test, guards):
    test.assertEqual(len(guards), 10811)
    digest = hashlib.sha256(json.dumps(guards[:10809], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(digest, 'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')
    test.assertEqual(guards[10809:], resolver.owner_guards())
    return hashlib.sha256(json.dumps(guards, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
