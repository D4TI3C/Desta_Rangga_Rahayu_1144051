print("Wlayah A : Harimau, Ayam, Gabah")
print("Manusia harus memindahkan semuanya dengan benar ke Wilayah B")
a = raw_input('Pindahkan siapa ? : ')
if a == "ayam":
        print("\nWilayah A : Harimau, Gabah")
        print("Wilayah B : Ayam")
        b = raw_input('Lanjutkan, Pindahkan siapa ? : ')
        if b == "gabah":
                print("\nWilayah A : Harimau")
		print("Wilayah B : Ayam, Gabah")
                c = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                if c == "ayam":
                        print("\nWilayah A : Harimau, Ayam ")
                        print("Wilayah B : Gabah")
                        d = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                        if d == "harimau":
                                print("\nWlayah A : Ayam ")
                                print("Wilayah B : Gabah, Harimau")
                                e = raw_input('Lanjutkan, Pindahkan siapa ? : ')
                                if e == "ayam":
                                        print("\nWilayah B : Gabah, Harimau, Ayam")
                                        print("Selamat, Anda berhasil")
                                else:
                                        print('Maaf, Anda gagal')
                        else:
                                print('Maaf, Anda gagal')
                else:
                        print('Maaf, Anda gagal')
        else:
                print('Maaf, Anda gagal')
else:
print('Maaf, Anda gagal')