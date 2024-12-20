#Bai 8
import math

x = float(input("Nhập giá trị x (x > 0): "))

#Dieu kien
if x > 0:
    ket_qua = math.log(x, 4) + math.log(2, x)
    print(f"Giá trị của f(x): {ket_qua:.2f}")
else:
    print("Giá trị x phải lớn hơn 0.")