# Bai 3
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
A = []
B = []
for i in range(1, n):
    if i % 2 != 0:
        A.append(i)
    else:
        B.append(i)
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
for i in range(len(B)):
    for j in range(i + 1, len(B)):
        if B[i] < B[j]:
            B[i], B[j] = B[j], B[i]
print("Danh sách A (số lẻ):", A)
print("Danh sách B (số chẵn):", B)
# Bài 1
n = int(input("Nhập số nguyên dương n: "))
prime = [True for i in range(n)]
for p in range(2, int(n**0.5) + 1):
    if (prime[p] == True):
        for i in range(p * p, n, p):
            prime[i] = False
print("Các số nguyên tố nhỏ hơn", n, "là:")
for p in range(2, n):
    if prime[p]:
        print(p, end=" ")
#Bài 2
n = int(input("Nhập số lượng phần tử của dãy: "))
A = []
print("Nhập các phần tử của dãy:")
for i in range(n):
    x = int(input())
    A.append(x)
tong = 0
for num in A:
    tong += num
print("Tổng các phần tử trong dãy là:", tong)
#Bài 4
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
#Bài 5
n = int(input("Nhap vao n = "))
ma_tran_don_vi = []
for i in range(n):
    phan_tu_trong_hang = [0]*i + [1] + [0]*(n-1-i)
    ma_tran_don_vi.append(phan_tu_trong_hang)
print(ma_tran_don_vi)
#Bài 6
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
        row.append(x)
    matrix.append(row)
print("Ma trận đã nhập:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
#Bài 7
i = int(input("Nhap vao hang i: "))
j = int(input("Nhap vao hang J: "))
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
temp = ma_tran_don_vi[i]
ma_tran_don_vi[i] = ma_tran_don_vi[j]
ma_tran_don_vi[j] = temp
print(ma_tran_don_vi)
#Bài 8
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
        row.append(x)
    matrix.append(row)
i = int(input("Nhập chỉ số cột thứ nhất (bắt đầu từ 0): "))
j = int(input("Nhập chỉ số cột thứ hai (bắt đầu từ 0): "))
for k in range(m):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
print("Ma trận sau khi đổi chỗ:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
#Bài 9
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
A = []
B = []
for i in range(m):
    row_A = []
    row_B = []
    for j in range(n):
        x = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1} của ma trận A: "))
        row_A.append(x)
        y = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1} của ma trận B: "))
        row_B.append(y)
    A.append(row_A)
    B.append(row_B)
k = int(input("Nhập số k: "))
C = []
for i in range(m):
    row_C = []
    for j in range(n):
        row_C.append(A[i][j] + B[i][j])
    C.append(row_C)
print("Tổng hai ma trận:")
for row in C:
    print(row)
D = []
E = []
F = []
is_symmetric = True
for i in range(m):
    for j in range(n):
        if A[i][j] != A[j][i]:
            is_symmetric = False
            break
if is_symmetric:
    print("Ma trận A là ma trận đối xứng")
else:
    print("Ma trận A không phải là ma trận đối xứng")
#Bài 10
ds_sinh_vien = []
n = int(input("Nhap so sinh vien n = "))
for sinh_vien in range(n):
    print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
    ten = input("Nhap ten sinh vien: ")
    diem = float(input("Nhap diem sinh vien: "))
    thong_tin_sinh_vien = {ten: diem}
    ds_sinh_vien.append(thong_tin_sinh_vien)
#Bài 11
sinh_vien = [
    {"ten": "Dung", "diem": 10.0},
    {"ten": "Quang", "diem": 5.3},
    {"ten": "Trang", "diem": 7.5}
]
do_dai_ten_max = max(len(sv['ten']) for sv in sinh_vien)
print(f"{'Tên':{do_dai_ten_max}} {'Điểm':>6}")
for sv in sinh_vien:
    print(f"{sv['ten']:{do_dai_ten_max}} {sv['diem']:>6.1f}")

