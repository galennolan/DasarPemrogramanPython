import penjumlahan
penjumlahan.tambah(5,2)
penjumlahan.kurang(10,3)
penjumlahan.kali(5,6)

#rename
import penjumlahan as mtk
mtk.tambah(5,2)
mtk.kurang(10,3)
mtk.kali(5,6)

#menggambil sebagian fungsi
from penjumlahan import kali #mengambil fungsi kali dari penjumlahan.py
kali(4,6)

from penjumlahan import tambah, kurang # import fungsi 1 dan fungsi 2
tambah(5,3)
kurang(5,2)

#menampilkan keseluruhan file dengan *
from penjumlahan import *
tambah(3,6)
kali(2,8)
kurang(8,3)

