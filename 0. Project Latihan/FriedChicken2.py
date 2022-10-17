print("=" * 52)
print(" " * 14, "Chicken Setulus Hati", " " * 20)
print("=" * 52)
print("Kode  Jenis    Harga")
print("-" * 23)
print("D     Dada     Rp 2500")
print("P     Paha     Rp 2000")
print("S     Sayap    Rp 1500")
banyakJenis = int(input("Berapa Jenis yang akan anda beli :  "))
i= 0
kodePotong      = []
banyakPotong    = []
jenisPotong     = []
hargaPerPotong  = []
JumlahHarga     = []
while (i<banyakJenis):
    print('jenis ke', i)
    kodePotong.append(str(input("Kode Potong [D/P/S] : ")))

    # Tambahkan banyakPotong D/P/S ke list banyakPotong
    banyakPotong.append(int(input("Banyak Potong   : ")))
    if(kodePotong[i] == "D" or kodePotong[i] == "d"):
        hargaPerPotong.append(2500)
        JumlahHarga.append(banyakPotong[i] * int(2500)) 
    elif (kodePotong[i] == "P" or kodePotong[i] == "p"):
        hargaPerPotong.append(2000)
        JumlahHarga.append(banyakPotong[i] * int(2000))
    elif (kodePotong[i] == "S" or kodePotong[i] == "s"):
        hargaPerPotong.append(1500)
        JumlahHarga.append(banyakPotong[i] * int(1500))
    else :
        print("salah input Kode")
    i+=1
print("=" * 52)
print(" " * 14, "Chicken Setulus Hati", " " * 20)
print("=" * 52)
print(" No    Harga        Jumlah    Jumlah")
print("       PerPotong    Beli      Harga ")
print("-" * 52)
a = 0
while a < banyakJenis:
    c = a + 1
    print(" ",c,"    ",hargaPerPotong[a],"        ",banyakPotong[a], JumlahHarga[a] )
    a = a + 1
    
print(JumlahHarga)
TotalHarga = sum(JumlahHarga)
print("Total Bayar     : ",TotalHarga)
        
