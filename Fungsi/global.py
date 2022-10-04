# membuat variabel global
nama = "python"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print ("Nama: ", nama)
    print ("Versi: ", versi)

# mengakses variabel global
    print ("Nama: " , nama)
    print ("Versi: ", versi)

# memanggil fungsi help()
help()