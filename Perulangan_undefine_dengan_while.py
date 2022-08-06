"""
Perulangan undefined dengan while
"""
print('Ibu memerintahkan untuk membaca buku sampai mengerti')
jumlah_buku=10
jumlah_buku_sudah_dibaca_dimengerti = 0
banyak_baca = 0
print("Kemudian adik mulai membaca bukunya satu persatu :")
while jumlah_buku_sudah_dibaca_dimengerti < jumlah_buku :
    jumlah_buku_sudah_dibaca_dimengerti = jumlah_buku_sudah_dibaca_dimengerti + 1
    print(f'\nAdik sudah membaca buku yang ke {jumlah_buku_sudah_dibaca_dimengerti},')
    if banyak_baca < 1:
        print(f'Jika adik belum mengerti, adik membaca buku ke {jumlah_buku_sudah_dibaca_dimengerti} kembali sampai mengerti.')
        banyak_baca = banyak_baca + 1
    banyak_baca = 0
print(f'\nAdik sudah membaca dan mengerti sebanyak {jumlah_buku_sudah_dibaca_dimengerti} buku.')
