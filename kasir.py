def hitung_harga_akhir(total):
    # Diskon 10% jika belanja minimal 100.000

    if total < 0:
        raise ValueError("Total tidak boleh negatif")

    if total >= 100000:
        return total * 0.9

    return total