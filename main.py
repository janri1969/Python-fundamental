"""
Membuat program beli susu dan telur
"""
jumlah_total_susu = 100
jumlah_telur = 100
print('Ibu berkata "pergi ke toko dan belikan susu 1 botol"')
print('jika di sana ada telur, "tolong belikan 7 butir"')
print('Adik menjawab, "baik bu"')
print('Adik Pergi ke toko')
if jumlah_total_susu > 0 :
    print('Adik mengecek harganya, dan ternyata uangnya cukup')
    print("Adik membeli susu 1 botol")
    print("Adik mengecek telur, dan ternyata uangnya cukup")
    if jumlah_telur >= 7:
        print(f"Adik membeli 7 butir telur")
    else :
        print(f"Adik membeli {jumlah_telur} butir")

print("Adik Pulang ke rumah dan melaporkan kegiatannya.")

