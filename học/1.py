class HinhChuNhat:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def ChuVi (self,chieu_dai,chieu_rong):
        print(f"Chu vi của hình chữ nhât là {self.chieu_dai*2 + self.chieu_rong*2}")
    def DienTich (self,chieu_dai,chieu_rong):
        print(f"Diện tích của hình chữ nhât là {self.chieu_dai * self.chieu_rong}")
Hinh_A=HinhChuNhat
Hinh_A.chieu_dai = 10
Hinh_A.chieu_rong = 5
print(Hinh_A.DienTich())
print(Hinh_A.ChuVi())