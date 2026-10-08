"""Checked owner table bindings across the original scalar gap, not installation."""

import csv
import json
import shutil
import struct
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from tools.experiments import game_node_selection_candidates as screen
from tools.experiments.game_actor_classifier_candidates import sections
from tools.pad_generated_object import emit_padded_assembly, parse_object
from tools.tests import test_game_node_action_match as action
from tools.tests.game_owner_pool import normalized_pools


class GameNodeSelectionBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root = Path(__file__).resolve().parents[2]
        cls.out = cls.root / 'conker/build/game-node-selection-binding-test'
        cls.out.mkdir(exist_ok=True)
        cls.owner = screen.measure_owner(cls.root, cls.out)
        cls.obj = cls.out / 'owner-candidate-postprocessed.o'
        cls.old_obj = cls.out / 'owner-stub-postprocessed.o'
        for name, obj in (('owner-stub',cls.old_obj),('owner-candidate',cls.obj)):
            shutil.copyfile(cls.out / (name+'.o'),obj)
            subprocess.run([sys.executable,str(cls.root / 'tools/asm-processor/asm_processor.py'),'-O2','-g3',
                str((cls.out / (name+'.c')).relative_to(cls.root / 'conker')),'--post-process',
                str(obj.relative_to(cls.root / 'conker')),'--assembler',
                'mips-linux-gnu-as -EB -mtune=vr4300 -march=vr4300 -mabi=32 -I include',
                '--asm-prelude','include/asm_processor_prelude.inc'],cwd=cls.root / 'conker',check=True,capture_output=True)
        cls.rows = screen.table_binding_guards(cls.obj)
        cls.record, cls.words, cls.pool = screen.compile_candidate(cls.root, cls.out, 'selected')
        with (cls.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            reader = csv.DictReader(stream)
            cls.fields, cls.history = reader.fieldnames, list(reader)
        cls.symbols = {'jtbl_%08X_game' % address:address for address,_ in screen.TABLE_LAYOUT}

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value, indent=2)+'\n')

    def padded(self, rows=None, name='binding'):
        rows = self.rows if rows is None else rows
        path = self.out / (name+'.csv')
        with path.open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows([*self.history, *rows])
        assembly = emit_padded_assembly(self.obj, self.root / 'conker/asm/5D2C0.s',
            word_patches_path=path, filename='generated_5D2C0', rodata_symbol=action.ANCHOR)
        start = assembly.index('.type %s, @function' % screen.FUNCTION)
        end = assembly.index('.size %s, . - %s' % (screen.FUNCTION,screen.FUNCTION), start)
        end = assembly.index('\n', end)+1
        body = assembly[start:end]
        asm, obj = self.out / (name+'.s'), self.out / (name+'.o')
        asm.write_text('.text\n.set noat\n.set noreorder\n.globl %s\n' % screen.FUNCTION+body)
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(asm)], check=True,capture_output=True)
        return obj, body

    def linked(self, obj, entry=screen.ENTRY, tables=None, name='linked'):
        symbols = {**screen.SYMBOLS, **(self.symbols if tables is None else tables), action.ANCHOR:0x80096F40}
        script, elf = self.out / (name+'.ld'), self.out / (name+'.elf')
        script.write_text('SECTIONS { .text 0x%X : SUBALIGN(4) { *(.text) } }\n' % entry)
        subprocess.run(['mips-linux-gnu-ld','-m','elf32btsmip','-T',str(script),'-e',screen.FUNCTION,
            *['--defsym=%s=0x%X' % item for item in symbols.items()],'-o',str(elf),str(obj)],check=True,capture_output=True)
        return list(struct.unpack_from('>1148I', sections(elf)['.text'][1]))

    def test_01_seven_checked_pairs_bind_only_address_addends_and_relocations(self):
        self.assertEqual((self.record['body_words'],self.record['frame'],self.record['differences']), (1148,0x48,319))
        retail = list(struct.unpack_from('>1148I', (self.root / 'conker/conker.us.bin').read_bytes(),screen.ROM))
        self.assertEqual(self.words[:19],retail[:19])
        self.assertEqual(self.words[-68:],retail[-68:])
        homes = {word>>16&31:word&65535 for word in self.words
            if word>>26 == 43 and word>>21&31 == 29 and word>>16&31 in (6,8,9,10)}
        self.assertEqual(homes,{6:0x40,8:0x44,9:0x24,10:0x30})
        field_forms = 0
        for name, source in screen.field_candidates():
            record, words, pool = screen.compile_candidate(self.root,self.out,'field-'+name,source)
            self.assertEqual((record['body_words'],record['frame'],record['differences']),(1148,0x48,319),name)
            self.assertEqual((words,pool),(self.words,self.pool),name)
            field_forms += 1
        self.assertEqual(field_forms,12)
        previous, words, pool = screen.compile_candidate(self.root,self.out,'previous-field-homes',screen.FRAME)
        self.assertEqual((previous['body_words'],previous['frame'],previous['differences']),(1148,0x48,321))
        self.assertEqual({i for i,(old,new) in enumerate(zip(words,self.words)) if old != new},{8,10})
        self.assertEqual((self.words[8],self.words[10]),(words[10],words[8]))
        self.assertEqual(pool,self.pool)
        self.assertEqual(len(self.rows),14)
        obj, body = self.padded()
        text, funcs, relocs = parse_object(obj)
        self.assertEqual(funcs[screen.FUNCTION]['size'],4592)
        self.assertNotIn('.space',body)
        for name in ('.rodata','.data','.bss'):
            self.assertEqual(len(sections(obj).get(name,(0,b''))[1]),0,name)
        for row in self.rows:
            offset = int(row['offset'],0)
            replacement = int(row['replacement'],0)
            self.assertEqual(struct.unpack_from('>I',text,offset)[0],replacement)
            self.assertEqual(int(row['expected'],0)&0xFFFF0000,replacement)
            relocation,symbol = row['replacement_relocations'].split(':',1)
            self.assertEqual(relocs[offset],[(relocation,symbol)])
            self.assertEqual((row['insert_after'],row['omit']),('', 'false'))
        self.assertFalse(any('.rodata' == s or s == action.ANCHOR for values in relocs.values() for _,s in values))
        self.assertEqual(self.linked(obj),self.words)
        old_text, old_functions, old_relocs = parse_object(self.old_obj)
        owner_text, owner_functions, owner_relocs = parse_object(self.obj)
        self.assertEqual(owner_functions.keys(),old_functions.keys())
        self.assertEqual(len(owner_functions),40)
        for name, current in owner_functions.items():
            if name == screen.FUNCTION:
                continue
            previous = old_functions[name]
            self.assertEqual(owner_text[current['value']:current['value']+current['size']],
                old_text[previous['value']:previous['value']+previous['size']],name)
            self.assertEqual({o-current['value']:r for o,r in owner_relocs.items()
                if current['value'] <= o < current['value']+current['size']},
                {o-previous['value']:r for o,r in old_relocs.items()
                if previous['value'] <= o < previous['value']+previous['size']},name)
        old_pool, new_pool = normalized_pools(self.old_obj)['.rodata'], normalized_pools(self.obj)['.rodata']
        self.assertEqual(old_pool[0][:412],new_pool[0][:412])
        self.assertEqual(old_pool[1],tuple(item for item in new_pool[1] if item[0] < 412))
        targets = {location:screen.ENTRY+offset for location,name,offset in new_pool[1] if name == screen.FUNCTION}
        base, data = sections(self.root / 'conker/build/conker.us.elf')['.game_data']
        offset, fit = 412, []
        for address, count in screen.TABLE_LAYOUT:
            retail = struct.unpack_from('>%dI' % count,data,address-base)
            compiled = [targets[offset+4*i] for i in range(count)]
            deltas = [new-old for old,new in zip(retail,compiled)]
            self.assertTrue(set(deltas) <= {0,4})
            fit.append(dict(symbol='jtbl_%08X_game' % address,entries=count,
                exact_target_PCs=deltas.count(0),target_PCs_four_bytes_late=deltas.count(4)))
            offset += count*4
        self.assertEqual([row['exact_target_PCs'] for row in fit],[0,0,23,16,463,78,10])
        self.receipt('target-pcs',dict(tables=fit,entries=674,exact_target_PCs=590,
            target_PCs_four_bytes_late=84,original_target_PC_compatibility=False,
            padded_C_execution_and_installation_not_claimed=True))
        self.receipt('binding',dict(body_words=1148,frame=0x48,differences=319,checked_rows=14,
            original_private_homes=True,final_68_words_direct_exact=True,
            first_19_words_direct_exact=True,opening_change_is_only_independent_words_8_and_10=True,
            field_forms_with_identical_text_and_pool=field_forms,
            seven_physical_symbols=True,only_address_immediates_and_relocations_changed=True,
            no_padding_insert_omit_or_generated_data=True,equals_isolated_C_linked_text=True,
            postprocessed_neighbors_unchanged=39,existing_useful_pools_unchanged=True,
            original_data_jump_target_PC_fit_and_installation_not_claimed=True))

    def test_02_each_table_rebases_independently_including_signed_LO_carries(self):
        obj, _ = self.padded(name='rebase')
        checked = 0
        for index,(symbol,address) in enumerate(self.symbols.items()):
            pair = [row for row in self.rows if row['replacement_relocations'].endswith(':'+symbol)]
            self.assertEqual(len(pair),2)
            for new_address in (address+4,0x90007FFC,0x90008004,0x9000FFFC):
                expected = self.words.copy()
                for row in pair:
                    offset = int(row['offset'],0)//4
                    imm = ((new_address+0x8000)>>16)&65535 if row['replacement_relocations'].startswith('R_MIPS_HI16') else new_address&65535
                    expected[offset] = expected[offset]&0xFFFF0000 | imm
                tables = {**self.symbols,symbol:new_address}
                for entry in (screen.ENTRY,screen.ENTRY+0x01000004):
                    self.assertEqual(self.linked(obj,entry,tables,'rebase-%d-%X-%X' % (index,new_address,entry)),expected)
                    checked += 1
        self.receipt('rebases',dict(links=checked,independent_tables=7,entry_phases=2,
            table_addresses_per_symbol=4,HI_LO_carry_boundaries=True,other_words_unchanged=True,
            narrow_relocation_binding_not_padded_C_execution=True))

    def test_03_stale_word_relocation_owner_and_topology_guards_fail_closed(self):
        for field,value,message in (('expected','0x00000000','stale word patch'),
                ('expected_relocations','R_MIPS_HI16:wrong','stale relocations')):
            rows = [dict(row) for row in self.rows]
            rows[0][field] = value
            with self.assertRaisesRegex(ValueError,message):
                self.padded(rows,'stale-'+field)
        original = parse_object(self.obj)
        text, functions, relocs = original
        location = functions[screen.FUNCTION]['value']+int(self.rows[1]['offset'],0)
        for bad_word in (0x8C380000,0xAC38019C):
            changed = bytearray(text)
            struct.pack_into('>I',changed,location,bad_word)
            with patch.object(screen,'parse_object',return_value=(bytes(changed),functions,relocs)):
                with self.assertRaisesRegex(ValueError,'addend changed|topology changed'):
                    screen.table_binding_guards(self.obj)
        bad = {key:list(value) for key,value in relocs.items()}
        bad[location-8] = [('R_MIPS_HI16','wrong')]
        with patch.object(screen,'parse_object',return_value=(text,functions,bad)):
            with self.assertRaisesRegex(ValueError,'HI/LO pair changed'):
                screen.table_binding_guards(self.obj)
        normalized = normalized_pools(self.obj)
        with patch.object(screen,'normalized_pools',return_value={**normalized,'.rodata':(normalized['.rodata'][0],())}):
            with self.assertRaisesRegex(ValueError,'ownership changed'):
                screen.table_binding_guards(self.obj)
        self.receipt('stale',dict(rejected_controls=6,expected_words_and_relocations_checked=True,
            exact_table_owner_extent_addend_pair_and_instruction_topology_checked=True))

    def test_04_missing_binding_and_wrong_symbol_are_effective_negatives(self):
        rows = [row for row in self.rows if row != self.rows[1]]
        obj, _ = self.padded(rows,'missing-low-binding')
        wrong = self.linked(obj,name='missing-low-linked')
        first_low = int(self.rows[1]['offset'],0)//4
        self.assertEqual(wrong[first_low]&65535,0x70DC)
        self.assertEqual(self.words[first_low]&65535,0x70E0)
        self.assertNotEqual(wrong,self.words)
        rows = [dict(row) for row in self.rows]
        for row in rows[:2]:
            row['replacement_relocations'] = row['replacement_relocations'].replace('800970E0','8009716C')
        obj, _ = self.padded(rows,'wrong-table')
        self.assertNotEqual(self.linked(obj,name='wrong-table-linked'),self.words)
        self.receipt('negatives',dict(effective_negatives=2,missing_LO_hits_original_scalar_not_table=True,
            wrong_symbol_changes_table_address=True,guards_remain_experimental=True))


if __name__ == '__main__':
    unittest.main()
