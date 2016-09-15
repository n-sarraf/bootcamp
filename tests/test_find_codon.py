import pytest
import find_codon


def test_find_codon():

    assert find_codon.find_codon_lesson6('ATG', 'ATGGAGAAC') == 0
    assert find_codon.find_codon_lesson6('ATG', 'GAATGCCA') == 2
    assert find_codon.find_codon_lesson6('atg', 'ATGGAGAAC') == 0

    pytest.raises(RuntimeError, "find_codon.find_codon_lesson6('Z', 'ATGCGCA')")
    pytest.raises(RuntimeError, "find_codon.find_codon_lesson6('Q', 'ATGCGCA')")
