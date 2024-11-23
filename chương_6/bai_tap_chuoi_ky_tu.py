#Bai tap ve chuoi ky tu
#Dang thu nhat: ap dung xu ky tu bang cac phuong thuc co san
#Bai 1: Nhan vao mot chuoi ky tu bat ky, dem so ky tu trong chuoi.
#Cach 1:

print(f"So ky tu trong chuoi la {so_ky_tu_trong_chuoi}")
#Cach 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem = 0
for chu in chuoi_nhap_vao:
    print(chu)
    dem = dem + 1
print(f"So ky tu trong chuoi la {dem}")

#Bai 2: Nhap vao 1 chuoi bat ky. Xoa cac khoang trong o dau va cuoi chuoi
# Cach 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
chuoi_da_xoa_khoang_trong = chuoi_nhap_vao.strip()
print(f"Chuoi sau khi xoa khoang trong {chuoi_da_xoa_khoang_trong}")
# Cach 2:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
#"    Chuoi nhap vao         "
chuoi_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " "and kiem_tra_dau == False:
        continue 
    else:
        kiem_tra_dau == True
        chuoi_xu_ly_dau = chuoi_xu_ly_dau + chu

chuoi_dao_nguoc = chuoi_xu_ly_dau[::-1]
chuoi_dao_nguoc_xu_ly_dau = ""
kiem_tra_dau = False
for chu in chuoi_nhap_vao:
    if chu == " "and kiem_tra_dau == False:
        continue 
    else:
        kiem_tra_dau == True
        chuoi_dao_nguoc_xu_ly_dau = chuoi_dao_nguoc_xu_ly_dau + chu

chuoi_ket_qua = chuoi_dao_nguoc_xu_ly_dau[::-1]
print(f"Chuoi sau khi xoa khoang trong {chuoi_ket_qua}")

# Bai 3: Nhap vao mot chuoi bat ky, xoa tat ca cac khoang trong thua trong chuoi
# Vi du: "      chuoi     nhap      vao    "
# Cach 1:
chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
tach_chuoi = chuoi_nhap_vao.split()
chuoi_ket_qua = " ".join(tach_chuoi)
#"chuoi nhap vao"
print(f"Chuoi ket qua: {chuoi_ket_qua}")
#Cach 2: BTVN: xu ly yeu cau ma khong su dung cac phuong thuc



#Dang thu hai: ap dung ket hop xu ly vong lap va xu  ly chuoi ky tu
# Bai 1: Nhap vao mot chuoi ky tu bat ky. Dem xem co bao nhieu ky tu la chu, bao nhieu ky tu dac biet
# isalpha(): kiem tra chu cai 
# isdigit(): kiem tra so

chuoi_nhap_vao = input("Nhap vao chuoi bat ky: ")
dem_chu = 0
dem_so = 0
dem_ky_tu_dac_biet = 0
for chu in chuoi_nhap_vao:
    if chu.isalpha() == True:
        dem_chu = dem_chu + 1
    else:
        if chu.isdigit() == True:
            dem_so = dem_so + 1
        else:
            dem_ky_tu_dac_biet = dem_ky_tu_dac_biet + 1

print(f"So chu cai: {dem_chu}")
print(f"So so: {dem_so}")
print(f"So ky tu dac biet: {dem_ky_tu_dac_biet}")

# Bai 2: Nhap vao 1 so bat ky kiem tra xem so nay co phai so nguyen to hay khong?
while True:
    n = input("Nhap vao so nguyen duong can kiem tra: ")
    if n.isdigit() == False:
        print("Gia tri nhap vao khong phai gia tri so nguyen duong")
    else: 
        break

n = int(n)

# Bai 3: Nhap vao 2 so thuc bat ky, tinh tong 2 so thuc do
while True:
    
    so_kiem_tra = a.replace(".","")
    so_kiem_tra = so_kiem_tra.replace("-","")
    if a.isdigit() == False:
         print("Gia tri nhap vao khong phai gia tri so")
    else:
        dem_dau_cham = a.count(".")
        dem_dau_gach = a.count("-")
        if dem_dau_cham > 1 or dem_dau_gach > 1:
            print("Gia tri nhap vao khong phai gia tri so")
        else:
            vi_tri_dau_gach = a.find("-")

b = input("Nhap vao so thuc b: ")
tong 

