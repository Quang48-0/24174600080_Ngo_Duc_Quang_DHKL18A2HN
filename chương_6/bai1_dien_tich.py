#Bai1
import math

r = float(input("Nhập bán kính (r > 0): "))
h = float(input("Nhập chiều cao (h > 0): "))

#Dieu kien
if r > 0 and h > 0:
    pi = 3.14
    dien_tich_xq = 2 * pi * r * h
    dien_tich_tp = 2 * pi * r * (r + h)
    the_tich = pi * r**2 * h
    print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")
    print(f"Diện tích toàn phần: {dien_tich_tp:.2f}")
    print(f"Thể tích: {the_tich:.2f}")
else:
    print("Bán kính và chiều cao phải lớn hơn 0.")