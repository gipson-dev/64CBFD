"""Closed instruction permutation, retained table PCs and actual padded execution."""

import csv
import json
import struct
import subprocess
import unittest
from unittest.mock import patch

from tools.experiments import game_node_selection_candidates as screen
from tools.experiments import game_node_selection_schedule as schedule
from tools.experiments.game_actor_classifier_candidates import sections
from tools.pad_generated_object import parse_object, parse_retail_slice
from tools.tests.game_owner_pool import normalized_pools
from tools.tests import test_game_node_selection_binding as binding
from tools.tests import test_game_node_selection_recovery as recovery


class GameNodeSelectionScheduleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        binding.GameNodeSelectionBindingTests.setUpClass()
        cls.binding = binding.GameNodeSelectionBindingTests()
        cls.root = cls.binding.root
        cls.out = cls.root / 'conker/build/game-node-selection-schedule-test'
        cls.out.mkdir(exist_ok=True)
        cls.raw = cls.binding.words
        cls.normalized = schedule.normalize_words(cls.raw)
        cls.rows = screen.schedule_guards(cls.binding.obj)
        cls.all_rows = [*cls.binding.rows, *cls.rows]
        cls.obj, cls.body = cls.binding.padded(cls.all_rows,'schedule-qualified')
        cls.words = cls.binding.linked(cls.obj,name='schedule-qualified-linked')
        cls.retail = list(struct.unpack_from('>1148I',
            (cls.root / 'conker/conker.us.bin').read_bytes(),screen.ROM))

    def receipt(self, name, value):
        (self.out / (name+'.json')).write_text(json.dumps(value,indent=2)+'\n')

    def test_01_actual_padder_exact_slot_and_every_retained_table_target(self):
        self.assertEqual(self.words,self.retail)
        self.assertEqual(self.normalized['words'],self.retail)
        text, functions, _ = parse_object(self.obj)
        self.assertEqual(functions[screen.FUNCTION]['size'],4592)
        self.assertNotIn('.space',self.body)
        for name in ('.rodata','.data','.bss'):
            self.assertEqual(len(sections(self.obj).get(name,(0,b''))[1]),0)
        base, data = sections(self.root / 'conker/build/conker.us.elf')['.game_data']
        targets = sorted({target for address,count in screen.TABLE_LAYOUT
            for target in struct.unpack_from('>%dI' % count,data,address-base)})
        _,_,_,labels = parse_retail_slice(self.root / 'conker/asm/5D2C0.s')
        # Resolve label differences in a test-only section; GAS discards .L symbols.
        asm, obj = self.out / 'label-receipt.s',self.out / 'label-receipt.o'
        asm.write_text('.text\n.set noat\n.set noreorder\n'+self.body+
            '\n.section .selection_label_receipt,"a"\n'+''.join(
                '.word %s - %s\n' % (labels[target][0],screen.FUNCTION) for target in targets))
        subprocess.run(['mips-linux-gnu-as','-EB','-march=vr4300','-o',str(obj),str(asm)],
            check=True,capture_output=True)
        offsets = struct.unpack_from('>%dI' % len(targets),sections(obj)['.selection_label_receipt'][1])
        symbols = dict(zip(targets,offsets))
        owners = {location:offset//4 for location,name,offset in
            normalized_pools(self.binding.obj)['.rodata'][1] if name == screen.FUNCTION}
        offset, count = 412, 0
        for address, entries in screen.TABLE_LAYOUT:
            targets = struct.unpack_from('>%dI' % entries,data,address-base)
            for index,target in enumerate(targets):
                source = owners[offset+4*index]
                self.assertEqual(screen.ENTRY+4*self.normalized['labels'][source],target)
                self.assertEqual(symbols[target],target-screen.ENTRY)
                count += 1
            offset += entries*4
        self.assertEqual(count,674)
        self.assertEqual(len(self.rows),67)
        self.assertEqual(sum(row['omit'] == 'true' for row in self.rows),1)
        self.assertEqual(sum(bool(row['insert_after']) for row in self.rows),1)
        self.receipt('slot',dict(raw_words=1148,raw_differences=304,padded_words=1148,
            padded_differences=0,frame=0x48,table_binding_rows=14,scheduling_rows=67,
            inserted_existing_node_home_load=1,omitted_relocated_model_copy=1,
            all_original_table_targets_exact=count,actual_assembled_label_offsets_exact=True,
            generated_padding_or_data=False))

    def test_02_each_instruction_origin_once_and_checked_branch_destinations(self):
        normalized = self.normalized
        self.assertEqual(sorted(normalized['tokens']),list(range(1148)))
        moves, branch_changes, model_changes = [], 0, 0
        for output,source in enumerate(normalized['tokens']):
            old,new = self.raw[source],normalized['words'][output]
            if output != source:
                moves.append((source,output))
            if schedule.is_branch(old):
                displacement = new&65535
                displacement -= 65536 if displacement&0x8000 else 0
                original = old&65535
                original -= 65536 if original&0x8000 else 0
                self.assertEqual(output+1+displacement,normalized['labels'][source+1+original])
                expected_upper = old&0xFFFF0000
                if source in schedule.MODEL_USES:
                    expected_upper = expected_upper & ~(31<<21) | 3<<21
                    model_changes += 1
                self.assertEqual(new&0xFFFF0000,expected_upper)
                branch_changes += displacement != original
            else:
                self.assertEqual(new,old)
        self.assertEqual(model_changes,4)
        self.assertEqual(normalized['tokens'][19:21],[20,19])
        self.assertEqual(normalized['labels'][schedule.CASE99],normalized['positions'][schedule.NODE_HOME])
        self.assertEqual(normalized['words'][:19],self.raw[:19])
        self.assertEqual(normalized['words'][-68:],self.raw[-68:])
        self.receipt('permutation',dict(instruction_origins=1148,all_origins_once=True,
            relocated_origins=moves,branch_displacements_changed=branch_changes,
            cached_model_reads_retargeted=model_changes,first19_final68_unchanged=True,
            no_retail_word_blob_used_by_transform=True))

    def test_03_stale_topology_words_relocations_and_branch_targets_fail_closed(self):
        rejected = 0
        anchors = (19,20,21,302,305,321,322,*schedule.MODEL_USES)
        for index in anchors:
            words = self.raw.copy()
            words[index] ^= 1
            with self.assertRaisesRegex(ValueError,'topology changed'):
                schedule.normalize_words(words)
            rejected += 1
        with self.assertRaisesRegex(ValueError,'extent changed'):
            schedule.normalize_words(self.raw[:-1])
        rejected += 1
        index = next(i for i,word in enumerate(self.raw[:1080])
            if schedule.is_branch(word) and i not in anchors and word>>21&31 not in (4,))
        words = self.raw.copy()
        words[index] = words[index]&~(31<<21) | 4<<21
        with self.assertRaisesRegex(ValueError,'cached-model uses changed'):
            schedule.normalize_words(words)
        rejected += 1
        for target in (21,32700):
            words = self.raw.copy()
            words[index] = words[index]&0xFFFF0000 | (target-index-1)&65535
            with self.assertRaisesRegex(ValueError,'branch target changed'):
                schedule.normalize_words(words)
            rejected += 1
        text, functions, relocs = parse_object(self.binding.obj)
        bad = dict(relocs)
        bad[functions[screen.FUNCTION]['value']+76] = [('R_MIPS_26','unexpected')]
        with patch.object(screen,'parse_object',return_value=(text,functions,bad)):
            with self.assertRaisesRegex(ValueError,'scheduling relocation changed'):
                screen.schedule_guards(self.binding.obj)
        rejected += 1
        for field,value,message in (('expected','0x00000000','stale word patch'),
                ('expected_relocations','R_MIPS_26:unexpected','stale relocations')):
            rows = [dict(row) for row in self.all_rows]
            rows[14][field] = value
            with self.assertRaisesRegex(ValueError,message):
                self.binding.padded(rows,'schedule-stale-'+field)
            rejected += 1
        self.receipt('stale',dict(rejected_controls=rejected,
            extent_topology_cached_uses_branch_destinations_words_relocations_checked=True))

    def test_04_transformation_does_not_repair_semantic_negatives(self):
        changed = self.raw.copy()
        index = next(i for i,word in enumerate(changed) if word == 0x240600F0)
        changed[index] ^= 1
        transformed = schedule.normalize_words(changed)['words']
        self.assertNotEqual(transformed,self.retail)
        self.assertEqual(transformed[self.normalized['positions'][index]],changed[index])
        checked = 0
        for name,source in screen.candidates():
            if not name.startswith('negative-'):
                continue
            _,words,_ = screen.compile_candidate(self.root,self.out,name,source)
            try:
                transformed = schedule.normalize_words(words)['words']
            except ValueError:
                pass
            else:
                self.assertNotEqual(transformed,self.retail,name)
            checked += 1
        self.assertEqual(checked,5)
        self.receipt('negatives',dict(compiled_semantic_negatives_not_repaired=checked,
            unrelated_word_mutation_preserved=True))

    def test_05_normalized_padded_execution_uses_original_tables(self):
        Recovery = recovery.GameNodeSelectionRecoveryTests
        Recovery.setUpClass()
        self.addCleanup(Recovery.doClassCleanups)
        check = Recovery()
        check.out = self.out
        check.words, check.pool = self.words,check.retail_pool
        check.coverage,check.cases = set(),0
        check.test_03_callback_mutations_state_gate_and_binary32_clamp()
        check.test_04_absent_attachment_lazy_reads_early_returns_and_required_fault_prefixes()
        check.test_06_valid_object_aliases_and_store_induced_pointer_reload()
        check.test_09_original_table_domains_and_retail_word_coverage()
        self.receipt('execution',dict(cases=check.cases,original_tables_used=True,
            actual_padded_object_executed=True,all674_table_keys=True,
            callbacks_fault_prefixes_aliases_float_boundaries=True,
            full_FCSR_callees_hardware_runtime_not_claimed=True))

    def test_06_symbolic_table_carry_rebases_preserve_closed_schedule(self):
        checked = 0
        for index,(symbol,address) in enumerate(self.binding.symbols.items()):
            pair = [row for row in self.binding.rows if row['replacement_relocations'].endswith(':'+symbol)]
            for new_address in (address+4,0x90007FFC,0x90008004,0x9000FFFC):
                expected = self.words.copy()
                for row in pair:
                    source = int(row['offset'],0)//4
                    output = self.normalized['positions'][source]
                    imm = ((new_address+0x8000)>>16)&65535 if row['replacement_relocations'].startswith('R_MIPS_HI16') else new_address&65535
                    expected[output] = expected[output]&0xFFFF0000 | imm
                tables = {**self.binding.symbols,symbol:new_address}
                for entry in (screen.ENTRY,screen.ENTRY+0x01000004):
                    self.assertEqual(self.binding.linked(self.obj,entry,tables,
                        'schedule-rebase-%d-%X-%X' % (index,new_address,entry)),expected)
                    checked += 1
        with (self.root / 'conker/retail_word_patches.us.csv').open(newline='') as stream:
            installed = [row for row in csv.DictReader(stream) if row['function'] == screen.FUNCTION]
        if installed:
            self.assertEqual(installed,self.all_rows)
        self.receipt('rebases',dict(links=checked,independent_tables=7,entry_phases=2,
            table_addresses_per_symbol=4,closed_schedule_unchanged=True,
            installed_rows_equal_measured_expected_rows=bool(installed)))


if __name__ == '__main__':
    unittest.main()
