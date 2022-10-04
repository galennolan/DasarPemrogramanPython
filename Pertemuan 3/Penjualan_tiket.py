#input
pembeli = input("Input Nama Pembeli :")
no_hp = input("Input no Hape anda :")
jurusan = input("Input Jurusan [SBY/BL/LMP] :")

#proses
if jurusan == "SBY":
    nama_jurusan = "Surabaya"
    harga =300000
elif jurusan == "BL":
    nama_jurusan = "Bali"
    harga = 350000
else :
    nama_jurusan = "Lampung"
    harga = 500000

#input jumlah Beli 
jumlah = int(input ("Masukkan Jumlah Beli "))

#proses potongan 
if jumlah >= 3 :
    potongan = (jumlah*harga)*0.1
else :
    potongan = 0

#Cetak Hasil
# Cetak Data Tiket
print("")
print("---------------------------------------------------")
print("                Penjualan Tiket Bus                ")
print("                        XYZ                        ")
print("---------------------------------------------------")
print("Nama Pembeli         : ", pembeli)
print("No. Handphone        : ", no_hp)
print("Kode Jurusan         : ", jurusan)
print("Nama Kota Tujuan     : ", nama_jurusan)
print("Harga per-Tiket      : ", harga)
print("Jumlah Pembelian     : ", jumlah)
print("---------------------------------------------------")
print("Potongan Harga       : ", potongan)
print("Total Pembayaran     : ", (harga*jumlah)-potongan)
uangBayar   = int(input("Masukkan Uang Bayar  :  Rp ")) 
uangKembali = uangBayar - ((harga*jumlah)-potongan)
print("Uang Kembali         : ", uangKembali)
print("---------------------------------------------------")
print("")
