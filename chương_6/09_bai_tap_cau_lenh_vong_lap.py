#In day so cac so le nho hon n
n = int(input("Nhap vao so nguyen duong n"))
for i in range(n): #-> chuoi tu 0 den  n-1
    if i%2 == 1:
        print(i)
        
#In n cac so Fibonnacci









# Tinh tong cac so hang tu 1 den n
tong_S = 0
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    tong_s = tong_s + i
    print(f"Tong_s = {tong_s}")
print(f"Tong cac so tu 1 den n {tong_s}")

# Tinh giai thua cua so n
tich_s = 1
n = int(input("Nhap vao gia tri nguyen duong n: "))
for i in range(n + 1):
    if i == 0:
        continue
    tich_s = tich_s*1

print(f"Tich giai thua cua so n {tich_s}")

# Nhap vao 2 so a, b tim uoc chung lon nhat cua hai so nay
a = int(input("Nhap vao so nguyen duong a: "))
b = int(input("Nhap vao so nguyen duong b: "))
so_nho_nhat = a
if b >= a :
    so_nho_nhat = b
k = so_nho_nhat
for i in range(so_nho_nhat):
    if a % k == 0 and b % k == 0:
        print(f"{k} la uoc chung lon nhat")
        break   
    k = k - 1

# Kiem tra so n co phai so nguyen to hay khong
# So nguyen to la so nguyen duong lon hon 1 va chi chia het cho 1 va chinh no
n = int(input("Nhập vào số nguyên dương cần kiểm tra: "))

# Kiểm tra các trường hợp đặc biệt
if n <= 1:
    print("Số này không phải là số nguyên tố")
elif n == 2:
    print("Số này là số nguyên tố")
elif n % 2 == 0:
    print("Số này không phải là số nguyên tố")
else:
    # Kiểm tra các số lẻ từ 3 đến n // 2
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            print("Số này không phải là số nguyên tố")
            break
    else:
        print("Số này là số nguyên tố")

# Kiểm tra các trường hợp đặc biệt




