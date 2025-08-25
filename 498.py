def findDiagonalOrder(mat):
    m, n = len(mat), len(mat[0])
    hasil = []
    
    for d in range(m + n - 1):   # jumlah diagonal
        temp = []
        
        # cari semua elemen yang i+j = d
        for i in range(m):
            j = d - i
            if 0 <= j < n:
                temp.append(mat[i][j])
        
        # kalau diagonal genap → dibalik
        if d % 2 == 0:
            hasil.extend(temp[::-1])
        else:
            hasil.extend(temp)
    
    return hasil

print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
# [1,2,4,7,5,3,6,8,9]

'''
d = 0 (genap)

Coba i=0 → j=0 → ambil 1

i=1 → j=-1 (invalid), i=2 → j=-2 (invalid)
temp = [1] → genap → balik: [1]
hasil = [1]

d = 1 (ganjil)

i=0 → j=1 → 2

i=1 → j=0 → 4

i=2 → j=-1 (invalid)
temp = [2, 4] → ganjil → tetap: [2, 4]
hasil = [1, 2, 4]

d = 2 (genap)

i=0 → j=2 → 3

i=1 → j=1 → 5

i=2 → j=0 → 7
temp = [3, 5, 7] → genap → balik: [7, 5, 3]
hasil = [1, 2, 4, 7, 5, 3]

d = 3 (ganjil)

i=0 → j=3 (invalid)

i=1 → j=2 → 6

i=2 → j=1 → 8
temp = [6, 8] → ganjil → tetap: [6, 8]
hasil = [1, 2, 4, 7, 5, 3, 6, 8]

d = 4 (genap)

i=0 → j=4 (invalid)

i=1 → j=3 (invalid)

i=2 → j=2 → 9
temp = [9] → genap → balik: [9]
hasil = [1, 2, 4, 7, 5, 3, 6, 8, 9]
'''
