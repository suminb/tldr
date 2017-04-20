import os

import pytest

from tldr.utils import extract_text


@pytest.mark.parametrize('sample_file', os.listdir('tests/samples/test_utils'))
def test_extract_text(sample_file):
    path = os.path.join('tests', 'samples', 'test_utils', sample_file)
    with open(path, encoding='euc-kr') as fin:
        html = fin.read()
        text = extract_text(html)
        # NOTE: Not sure if this is good enough
        assert len(text) > 250
