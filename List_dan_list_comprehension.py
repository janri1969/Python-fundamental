"""
List dan list comprehension
"""
print("latihan membuat list")

daftar_buku = ['Seven Habits', 'How to influence People', 'First things first']
print(daftar_buku)
for buku in daftar_buku:
    print(buku)
    print(daftar_buku[0])
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
daftar_buku = ['Seven Habits', 'first things first', 'how to influence people']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    print(f'\nbukunya adalah {daftar_buku[2]}')
daftar_buku = ['matematika', 'English Grammar', 'sejarah', 'ilmu sosial']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
    print(daftar_buku[1])
daftar_buku.append('fisika')
#for i in range(0, len(daftar_buku)):
print(daftar_buku)

"""
Menghapus List
"""
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('daftar')
print(daftar_buku)

daftar_buku = ['matematika', 'English Grammar', 'sejarah', 'ilmu sosial']
daftar_buku[0] = 'eight habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('fungsi pop')
buku=daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

"""
List Comprehension
"""
print('\nlist comprehension')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4DX']
del daftar_buku[-1]
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nlist comprehension dengan start,end, dan step')
daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['seven habits', 'how to influence people', 'first things first', '4DX']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])



