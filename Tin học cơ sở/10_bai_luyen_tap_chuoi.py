# Bai 1:
chuoi_nhap = input("Nhập vào chuỗi ký tự: ")
cac_tu = chuoi_nhap.split()
so_tu = len(cac_tu)
print("Số từ trong chuỗi là: ", so_tu)

# Bai 3:
ho_ten = input("Nhap vao ho ten cua ban: ")
so_tu = ho_ten.split()
ho = so_tu[0]
ten = so_tu[-1]
print(f"Ho: {ho}, Ten: {ten}")

# Bai 2
a = input("Nhập vào chuỗi: ")
words = a.split()
new_a = " ".join(words)
print("Chuỗi sau khi loại bỏ dấu cách thừa:", new_a)

#Bai 4
a = input("Nhập vào chuỗi: ")
b = 0
c = 0
d = 0

for char in a:
    if char.isalpha():
        b += 1
    elif char.isdigit():
        c += 1
    else:
        d += 1

print("Số ký tự chữ:", b)
print("Số ký tự số:", c)
print("Số ký tự đặc biệt:", d)

# Bai 5
a = input("Nhập vào chuỗi: ")
b = 0
c = 0

for char in a:
    if char.isupper():
        b += 1
    elif char.islower():
        c += 1

print("Số chữ hoa:", b)
print("Số chữ thường:", c)

# Bai 6
a = input("Nhập vào chuỗi: ")
try:
    b = float(a)
    if b < 0:
        print(f"{a} là số âm.")
    else:
        print(f"{a} không phải là số âm.")
except ValueError:
    print(f"{a} không phải là số.")

# Bai 7
a = input("Nhập vào chuỗi: ")
try:
    b = float(a)
    print(f"{a} là số thập phân.")
except ValueError:
    print(f"{a} không phải là số thập phân.")

# Bai 8
a = input("Nhập xâu a: ")
b = input("Nhập xâu b: ")

if b in a:
    print("b có trong a.")
else:
    print("b không có trong a.")

if a in b:
    print("a có trong b.")
else:
    print("a không có trong b.")

# Bai 9
a = input("Nhập vào chuỗi nhị phân: ")
b = True

for char in a:
    if char not in '01':
        b = False
        break

if b:
    c = int(a, 2)
    print(f"{a} là số nhị phân, chuyển sang thập phân: {c}")
else:
    print(f"{a} không phải là số nhị phân.")


