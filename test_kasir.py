import pytest
from kasir import hitung_harga_akhir

@pytest.mark.parametrize("total, harapan", [
    (99999, 99999),
    (100000, 90000),
    (200000, 180000),
])

def test_harga_akhir(total, harapan):
    assert hitung_harga_akhir(total) == pytest.approx(harapan)

def test_total_negatif_melempar_error():
    with pytest.raises(ValueError):
        hitung_harga_akhir(-1)