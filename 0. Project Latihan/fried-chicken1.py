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
        JumlahHarga.append(banyakPotong[i] * int(2500)) 
    elif (kodePotong[i] == "P" or kodePotong[i] == "p"):
        JumlahHarga.append(banyakPotong[i] * int(2000))
    elif (kodePotong[i] == "S" or kodePotong[i] == "s"):
        JumlahHarga.append(banyakPotong[i] * int(1500))
    else :
        print("salah input Kode")
    i+=1
    
print(JumlahHarga)
        