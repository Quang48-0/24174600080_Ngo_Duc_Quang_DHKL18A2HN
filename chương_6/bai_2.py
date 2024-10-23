#Bai 2
import math

x = float(input("Nhập giá trị x: "))

#Dieu kien
if isinstance(x, (int, float)):  # Kiểm tra nếu x là số
    tu_so = -x + math.sqrt(x**2 + 4)
    mau_so = math.sqrt(x**2 + 1)
    ket_qua = tu_so / mau_so
    print(f"Giá trị của f(x): {ket_qua:.2f}")
else:
    print("Giá trị nhập vào không hợp lệ.")
