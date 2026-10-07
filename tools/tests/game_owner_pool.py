"""Compare copied-owner pools by actual relocation ownership, not packed PCs."""

import hashlib
import json
import struct

from tools.experiments.game_actor_classifier_candidates import sections
from tools.experiments import game_texture_resolver_candidates as resolver
from tools.experiments import game_point_transform_candidates as point
from tools.experiments import game_range_clamp_candidates as clamp
from tools.experiments import game_actor_gated_packet_candidates as packet
from tools.experiments import game_cursor_updater_candidates as cursor
from tools.experiments import game_output_mode_candidates as output_mode
from tools.experiments import game_secondary_output_candidates as secondary_output
from tools.experiments import game_projection_schedule_candidates as projection
from tools.experiments import game_sphere_callee_allocation_candidates as sphere
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
    test.assertEqual(len(guards), 11006)
    digest = hashlib.sha256(json.dumps(guards[:10809], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(digest, 'e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a')
    test.assertEqual(guards[10809:10811], resolver.owner_guards())
    prior = hashlib.sha256(json.dumps(guards[:10811], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior, '9e8f11db1c07370f470888d62e63b3b8ced846afa67a1db81ca94f0c44e601da')
    test.assertEqual(guards[10811:10842], point.owner_guards())
    checkpoint = hashlib.sha256(json.dumps(guards[:10842], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(checkpoint, '500b722e15c6ce30c740e6b55bc6feb0afe0a24e46df571c8aa94955b7b94639')
    test.assertEqual(guards[10842:10855], clamp.owner_guards())
    prior_packet = hashlib.sha256(json.dumps(guards[:10855], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior_packet, '07904caf0a4b949a8e5b39f87e8aad4c0a1cc62cb92b3e999dd8d9c6b90211a4')
    test.assertEqual(guards[10855:10866], packet.owner_guards())
    prior_cursor = hashlib.sha256(json.dumps(guards[:10866], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior_cursor, 'cb153350711c5eac3aa8190db9e59d6ef48f5c989b5013be34ff5ddb8af50a53')
    test.assertEqual(guards[10866:10912], cursor.owner_guards())
    prior_output = hashlib.sha256(json.dumps(guards[:10912], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior_output, 'a90ff5ac4d082cca33348659463aaba19ad93741c7efc0c085ec35cfb2f27f13')
    test.assertEqual(guards[10912:10914], output_mode.owner_guards())
    prior_secondary = hashlib.sha256(json.dumps(guards[:10914], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior_secondary, 'f2d0df124fdbc693c980d574463aca4b495160acfc37374fea3d4ae3a2482446')
    test.assertEqual(guards[10914:10916], secondary_output.owner_guards())
    prior_projection = hashlib.sha256(json.dumps(guards[:10916], sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    test.assertEqual(prior_projection, '274d281be870d4ace85151c43ea73aa28044e182ac5d68d1ba4db5a02b3a0dfd')
    test.assertEqual(guards[10916:10953], projection.owner_guards())
    test.assertEqual(guards[10953:], sphere.owner_guards())
    return hashlib.sha256(json.dumps(guards, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
