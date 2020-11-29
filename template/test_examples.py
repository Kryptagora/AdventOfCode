import json
from pathlib import Path

import pytest

from solutions import part_1, part_2

EXAMPLES = json.loads(Path('examples.json').read_text())

@pytest.mark.parametrize('example', EXAMPLES['part_1'])
def test_1(example):
     assert part_1(example['input']) == example['solution']

@pytest.mark.parametrize('example', EXAMPLES['part_2'])
def test_2(example):
     assert part_1(example['input']) == example['solution']