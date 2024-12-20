#Bai 15
print("Chọn loại chuyển đổi:")
print("1. Từ hệ cơ số 10 sang hệ cơ số 2")
print("2. Từ hệ cơ số 2 sang hệ cơ số 10")
a = int(input("Nhập lựa chọn (1 hoặc 2): "))

if a == 1:
    b = int(input("Nhập số thập phân: "))
    binary = bin(b)[2:]  
    print(f"Số nhị phân là: {binary}")

elif a == 2:
    b = input("Nhập số nhị phân: ")
    decimal = int(b, 2) 
    print(f"Số thập phân là: {decimal}")

else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
