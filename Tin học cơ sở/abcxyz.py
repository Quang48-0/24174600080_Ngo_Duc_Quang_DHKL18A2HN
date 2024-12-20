#Nhập hai số nguyên, kiểm tra xem là số lẻ hay chẵn
'''a = int(input("Nhập số nguyên a: "))
if a % 2:
    print("Đây là số lẻ")
else:
    print("Đây là số chẵn")
#Nhập 2 số nguyên kiểm tra xem cùng dấu hay trái dấu
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if a * b > 0:
    print("Cùng dấu")
else:
    print("Trái dấu")

#Nhập vào 2 số nguyên giải phương trình bậc nhất ax + b 

a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Phương trình có nghiệm duy nhất:", x)


# Giải phương trình bậc 2 với a!= 0
a = int(input("Nhập vào giá trị của a: "))
b = int(input("Nhập vào giá trị của b: "))
c = int(input("Nhập vào giá trị của c: "))
if a != 0:
    delta = b**2-4*a*c
    if delta > 0:
        x1 = (-b+(delta)**(1/2))/(2*a)
        x2 = (-b-(delta)**(1/2))/(2*a)
        print("Phương trình có nghiệm x1, x2", x1, x2)
    elif delta == 0:
            x = -b/(2*a)
            print("Phương trình có nghiệm kép", x)
    else:
            print("Phương trình vô nghiệm")
else:
    print("Đây không phải là phương trình bậc hai")

            
# Cho tọa độ 3 điểm A(x1, y1, z1), B(x2, y2, z2), C(x3, y3, z3). 
# Với các giá trị x1, x2, x3, y1, y2, y3, z1, z2, z3, tìm khoảng cách giữa các điểm này
print("Nhập toạ độ A: ")
x1 = float(input("x1 =: "))
x2 = float(input("x2 =: "))
x3 = float(input("x3 =: "))
print("Nhập toạ độ B: ")
y1 = float(input("y1 =: "))
y2 = float(input("y2 =: "))
y3 = float(input("y3 =: "))
print("Nhập toạ độ C: ")
z1 = float(input("z1 =: "))
z2 = float(input("z2 =: "))
z3 = float(input("z3 =: "))


#Giai phuong trinh bac nhat co su dung ham
def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phuong trinh co vo so nghiem"
        else:
            return "Phuong trinh vo nghiem"
    else:
        x = -b/a
        return f"Nghiem cua phuong trinh la: {x}"
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
ket_qua = giai_phuong_trinh_bac_nhat(a, b)
print(ket_qu


def nhap_thong_tin_cau_thu():
  ma_cau_thu = input("Nhập mã cầu thủ: ")
  ten_cau_thu = input("Nhập tên cầu thủ: ")
  tuoi = int(input("Nhập tuổi: "))
  vi_tri = input("Nhập vị trí: ")
  so_huy_chuong = int(input("Nhập số huy chương: "))
  return [ma_cau_thu, ten_cau_thu, tuoi, vi_tri, so_huy_chuong]

def tinh_thuong(so_huy_chuong):
  if so_huy_chuong > 10:
    return so_huy_chuong * 500000
  elif so_huy_chuong >= 5:
    return so_huy_chuong * 300000
  else:
    return so_huy_chuong * 200000

def sap_xep_theo_thuong(danh_sach_cau_thu):
  danh_sach_cau_thu.sort(key=lambda x: x[4], reverse=True)  # Sắp xếp giảm dần theo số huy chương (index 4)

# Khởi tạo danh sách cầu thủ
danh_sach_cau_thu = []

while True:
  print("\nChọn chức năng:")
  print("1. Xem danh sách cầu thủ")
  print("2. Nhập thông tin cầu thủ")
  print("3. Tính thưởng")
  print("4. Tìm kiếm và xóa cầu thủ")
  print("5. Tìm kiếm và chỉnh sửa")
  print("6. Sắp xếp theo số huy chương")
  print("0. Thoát")

  chon = int(input("Nhập lựa chọn: "))

  if chon == 1:
    if len(danh_sach_cau_thu) == 0:
      print("Danh sách hiện đang trống.")
    else:
      print("Danh sách cầu thủ:")
      for cau_thu in danh_sach_cau_thu:
        print(cau_thu)
  elif chon == 2:
    cau_thu_moi = nhap_thong_tin_cau_thu()
    danh_sach_cau_thu.append(cau_thu_moi)
    print("Đã thêm cầu thủ mới.")
  elif chon == 3:
    for cau_thu in danh_sach_cau_thu:
      thuong = tinh_thuong(cau_thu[4])
      cau_thu.append(thuong)
      print(f"Thưởng của {cau_thu[1]}: {thuong} đồng")
  elif chon == 4:
    ma_cau_thu_xoa = input("Nhập mã cầu thủ cần xóa: ")
    for i in range(len(danh_sach_cau_thu)):
      if danh_sach_cau_thu[i][0] == ma_cau_thu_xoa:
        del danh_sach_cau_thu[i]
        print("Đã xóa cầu thủ.")
        break
    else:
      print("Không tìm thấy cầu thủ.")
  elif chon == 5:
    # Tương tự như xóa, chỉ thay vì xóa thì cập nhật thông tin
    pass
  elif chon == 6:
    sap_xep_theo_thuong(danh_sach_cau_thu)
    print("Danh sách cầu thủ sau khi sắp xếp:")
    for cau_thu in danh_sach_cau_thu:
      print(cau_thu)
  elif chon == 0:
    break
  else:
    print("Lựa chọn không hợp lệ.")

'''
       
# Danh sách cầu thủ
ds_cau_thu = []

# Hàm nhập thông tin cầu thủ
def nhap_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ: ")
        ten_ct = input("Nhập tên cầu thủ: ")
        tuoi = int(input("Nhập tuổi: "))
        vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
        so_huy_chuong = int(input("Nhập số huy chương: "))
        
        # Tính thưởng
        if so_huy_chuong > 10:
            thuong = so_huy_chuong * 500000
        elif 5 <= so_huy_chuong <= 10:
            thuong = so_huy_chuong * 300000
        else:
            thuong = so_huy_chuong * 200000

        cau_thu = {
            "ma_ct": ma_ct,
            "ten_ct": ten_ct,
            "tuoi": tuoi,
            "vi_tri": vi_tri,
            "so_huy_chuong": so_huy_chuong,
            "thuong": thuong
        }
        ds_cau_thu.append(cau_thu)
        print("Đã thêm cầu thủ thành công!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho tuổi hoặc số huy chương!")

# Hàm hiển thị danh sách cầu thủ
def xem_danh_sach_cau_thu():
    if not ds_cau_thu:
        print("Danh sách cầu thủ trống!")
        return
    print(f"{'Mã CT':<10}{'Tên cầu thủ':<20}{'Tuổi':<10}{'Vị trí':<15}{'Số HC':<10}{'Thưởng':<15}")
    print("-" * 80)
    for ct in ds_cau_thu:
        print(f"{ct['ma_ct']:<10}{ct['ten_ct']:<20}{ct['tuoi']:<10}{ct['vi_tri']:<15}{ct['so_huy_chuong']:<10}{ct['thuong']:<15}")

# Hàm tìm kiếm và xóa cầu thủ theo mã
def xoa_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ cần xóa: ")
        for ct in ds_cau_thu:
            if ct["ma_ct"] == ma_ct:
                ds_cau_thu.remove(ct)
                print("Đã xóa cầu thủ thành công!")
                return
        print("Không tìm thấy cầu thủ!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Hàm tìm kiếm và chỉnh sửa thông tin cầu thủ
def sua_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ cần sửa: ")
        for ct in ds_cau_thu:
            if ct["ma_ct"] == ma_ct:
                print("Nhập thông tin mới (bỏ trống để giữ nguyên):")
                ten_ct = input("Tên cầu thủ: ")
                if ten_ct:
                    ct["ten_ct"] = ten_ct
                tuoi = input("Tuổi: ")
                if tuoi:
                    ct["tuoi"] = int(tuoi)
                vi_tri = input("Vị trí: ")
                if vi_tri:
                    ct["vi_tri"] = vi_tri
                so_huy_chuong = input("Số huy chương: ")
                if so_huy_chuong:
                    ct["so_huy_chuong"] = int(so_huy_chuong)
                    # Cập nhật thưởng
                    if ct["so_huy_chuong"] > 10:
                        ct["thuong"] = ct["so_huy_chuong"] * 500000
                    elif 5 <= ct["so_huy_chuong"] <= 10:
                        ct["thuong"] = ct["so_huy_chuong"] * 300000
                    else:
                        ct["thuong"] = ct["so_huy_chuong"] * 200000
                print("Đã cập nhật thông tin cầu thủ!")
                return
        print("Không tìm thấy cầu thủ!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho tuổi hoặc số huy chương!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Hàm sắp xếp danh sách theo số huy chương
def sap_xep_so_huy_chuong():
    try:
        ds_cau_thu.sort(key=lambda x: x["so_huy_chuong"])
        print("Danh sách đã được sắp xếp theo số huy chương!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Menu chương trình
def menu():
    while True:
        try:
            print("\nQuản lý đội bóng")
            print("1. Xem danh sách cầu thủ")
            print("2. Nhập thông tin cầu thủ")
            print("3. Tìm kiếm và xóa cầu thủ theo mã")
            print("4. Tìm kiếm và chỉnh sửa thông tin cầu thủ theo mã")
            print("5. Xem danh sách cầu thủ sắp xếp theo số huy chương")
            print("6. Thoát chương trình")
            chon = input("Chọn chức năng (1-6): ")
            if chon == "1":
                xem_danh_sach_cau_thu()
            elif chon == "2":
                nhap_cau_thu()
            elif chon == "3":
                xoa_cau_thu()
            elif chon == "4":
                sua_cau_thu()
            elif chon == "5":
                sap_xep_so_huy_chuong()
            elif chon == "6":
                print("Thoát chương trình!")
                break
            else:
                print("Chức năng không hợp lệ, vui lòng chọn lại!")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

# Chạy chương trình
menu()
