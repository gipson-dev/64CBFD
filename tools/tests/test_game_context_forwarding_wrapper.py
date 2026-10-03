import re
from pathlib import Path

from tools.tests import test_game_actor_context_dispatch as dispatch


class GameContextForwardingWrapperTests(dispatch.GameActorContextDispatchTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_13BB20.c").read_text()
        wrapper = re.search(r"void func_1510F800\(s32 context\) \{\n.*?\n\}",
                            source, re.S)
        if wrapper is None:
            raise AssertionError("explicit context forwarding wrapper missing")
        cls.source = cls.source.replace("void func_1510F800(s32 context) {",
                                        "void func_150A49F4(s32 context) {", 1)
        location = cls.source.index("s32 func_150AB1F0(")
        cls.source = cls.source[:location] + wrapper.group(0) + "\n" + cls.source[location:]
        cls.wrapper = wrapper.group(0)

    def test_complete_argument_bits_are_forwarded_without_validation(self):
        fixture = r'''
static s32 calls, received;
void func_150A49F4(s32 context) { calls++; received = context; }
''' + self.wrapper + r'''
static void initialize(void) { calls = received = 0; }
'''
        full = self.source
        try:
            self.source = "typedef int s32;\n" + fixture
            self.run_case(r'''
s32 i;
s32 values[] = {0, 1, 2, 3, -1, 0x7FFFFFFF, (s32)0x80000000u, 0x12345678};
initialize();
for (i = 0; i < 8; i++) {
    func_1510F800(values[i]);
    if (received != values[i] || calls != i + 1) return 1;
}
''')
        finally:
            self.source = full
