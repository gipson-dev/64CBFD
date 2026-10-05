"""Compile isolated volatile record views; never execute MMIO or relink production."""

import argparse
import hashlib
import json
import struct
import subprocess
from pathlib import Path


PROFILES = (('o2g3', ['-O2', '-g3']), ('o2', ['-O2']),
            ('o1', ['-O1']), ('o1g3', ['-O1', '-g3']))


def compile_trials(shapes=(1, 2, 3)):
    root = Path(__file__).resolve().parents[2]
    project = root / 'conker'
    output = project / 'build/init-mmio-record-20261004'
    output.mkdir(parents=True, exist_ok=True)
    reference = (project / 'conker.us.bin').read_bytes()[0x38E0:0x390C]
    report = []
    for shape in shapes:
        if shape not in (1, 2, 3):
            raise ValueError('unknown MMIO shape: %s' % shape)
        for profile, flags in PROFILES:
            name = 'shape%d-%s' % (shape, profile)
            obj = output / (name + '.o')
            obj.unlink(missing_ok=True)
            result = subprocess.run([
                str(root / 'ido/ido5.3_recomp/cc'), '-c', '-32', '-G', '0',
                '-Xfullwarn', '-Xcpluscomm', '-signed', '-nostdinc', '-non_shared',
                '-Wab,-r4300_mul', '-mips2', '-o32', '-DMMIO_SHAPE=%d' % shape,
                *flags, '-o', str(obj.relative_to(project)),
                '../tools/experiments/init_mmio_record.c'],
                cwd=project, capture_output=True, text=True)
            (output / (name + '.log')).write_text(result.stdout + result.stderr)
            if result.returncode or not obj.is_file():
                raise RuntimeError('guest compile failed: ' + name + '\n' +
                                   result.stdout + result.stderr)
            elf, binary = output / (name + '.elf'), output / (name + '.bin')
            layout = output / (name + '.layout.bin')
            subprocess.run(['mips-linux-gnu-ld', '-m', 'elf32btsmip',
                '-Ttext=0x100038E0', '-e', 'func_100038E0',
                '--defsym=D_80038070=0x80038070', '--defsym=D_80038074=0x80038074',
                '-o', str(elf), str(obj)], cwd=project, check=True)
            for section, target in (('.text', binary), ('.rodata', layout)):
                subprocess.run(['mips-linux-gnu-objcopy', '-O', 'binary',
                    '--only-section=' + section, str(elf), str(target)],
                    cwd=project, check=True)
            data, layout_data = binary.read_bytes(), layout.read_bytes()
            record_layout = struct.unpack_from('>3I', layout_data)
            if record_layout != (8, 0, 4) or any(layout_data[12:]):
                raise ValueError('guest record layout differs from the two scalar addresses')
            words = list(struct.iter_unpack('>I', data))
            end = max(index for index, (word,) in enumerate(words)
                      if word == 0x03E00008) + 2
            body = data[:end * 4]
            frames = [0x10000 - (word & 0xFFFF) for word, in
                      struct.iter_unpack('>I', body)
                      if word >> 16 == 0x27BD and word & 0x8000]
            if len(frames) > 1:
                raise ValueError('MMIO trial needs control-flow stack analysis')
            disassembly = subprocess.check_output(
                ['mips-linux-gnu-objdump', '-d', '-z', str(elf)],
                cwd=project, text=True)
            (output / (name + '.asm.txt')).write_text(disassembly)
            report.append({'shape': shape, 'profile': profile, 'body_words': end,
                'text_bytes': len(data), 'trailing_text_bytes': len(data) - len(body),
                'different_positions': sum(body[index:index + 4] != reference[index:index + 4]
                    for index in range(0, max(len(body), len(reference)), 4)),
                'frame_bytes': sum(frames), 'record_layout': record_layout,
                'exact': body == reference, 'text_sha256': hashlib.sha256(data).hexdigest()})
    (output / 'measurements.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--shapes', type=int, nargs='+', choices=(1, 2, 3),
                        default=(1, 2, 3))
    print(json.dumps(compile_trials(parser.parse_args().shapes), indent=2))


if __name__ == '__main__':
    main()
