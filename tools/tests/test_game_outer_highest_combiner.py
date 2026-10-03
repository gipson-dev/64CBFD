import re
from pathlib import Path

from tools.tests import test_game_entity_terrain_highest_combiner as inner


class GameOuterHighestCombinerTests(inner.GameEntityTerrainHighestCombinerTests):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        source = (Path(__file__).resolve().parents[2] /
                  "conker/src/game/generated_71820.c").read_text()
        body = re.search(r"s32 func_15046D00\([^;{]*\{\n.*?\n\}", source, re.S)
        if body is None:
            raise AssertionError("outer highest combiner definition is missing")
        cls.source = re.sub(r"s32 func_1504697C\([^;{]*\{\n.*?\n\}",
                            lambda _: body.group(0), cls.source, count=1, flags=re.S)
        cls.source = cls.source.replace("func_15046460", "func_1504697C")
        cls.source = cls.source.replace("func_150450CC", "func_1504554C")

    def run_case(self, body):
        body = body.replace("func_15046460(", "func_15046D00(")
        body = body.replace("func_1504697C(", "func_15046D00(")
        super().run_case(body)
