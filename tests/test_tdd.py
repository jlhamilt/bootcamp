import pytest
import tdd
import imp

# Make sure the tdd file is the most recent
tdd = imp.reload(tdd)

# Write test functions
def test_n_neg():
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('') == 0
    assert tdd.n_neg('ACKlwteAE') == 2
    assert tdd.n_neg('DedEDDEE') == 8

    pytest.raises(RuntimeError, "tdd.n_neg('Z')")

    return None

def test_find_codon():
    assert tdd.find_codon('ATG', 'ATG') == 0
    assert tdd.find_codon('AAT', 'AAT') == 0
    assert tdd.find_codon('TGT', 'TGT') == 0
    assert tdd.find_codon('TGC', 'TGC') == 0
    assert tdd.find_codon('ATGGAGAACAACGA', 'CCC') == -1
