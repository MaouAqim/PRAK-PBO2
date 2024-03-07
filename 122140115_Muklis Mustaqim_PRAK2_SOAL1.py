class Mahasiswa:
    # Properties (atribut)
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self._nim = nim
        self._nama = nama
        self.angkatan = angkatan
        self.isMahasiswa = isMahasiswa

    # Setter dan getter untuk nim
    def get_nim(self):
        return self._nim

    def set_nim(self, new_nim):
        self._nim = new_nim

    # Setter dan getter untuk nama
    def get_nama(self):
        return self._nama

    def set_nama(self, new_nama):
        self._nama = new_nama

    # Method 1: Menyapa
    def sapa(self):
        print(f"Perkenalkan Nama saya {self.get_nama()}!")

    # Method 2: Cek Status
    def cek_status(self):
        status = "Mahasiswa Aktif" if self.isMahasiswa else "Mahasiswa Tidak Aktif"
        return f"Status        : {status}"

    # Method 3: Cetak Informasi
    def info(self):
        print(f"NAMA          : {self.get_nama()}")
        print(f"NIM           : {self.get_nim()}")
        print(f"angkatan      : {self.angkatan}")
        print(self.cek_status())
        print(f"========================================")

# Inisiasi object pertama
mhs1 = Mahasiswa("122140115", "Aqim", 2022)

# Inisiasi object kedua tanpa parameter isMahasiswa (default True)
mhs2 = Mahasiswa("122140114", "Daniel", 2022)

# Menyapa object pertama
mhs1.sapa()

# Mengubah nama object pertama
mhs1.set_nama("Muklis Mustaqim")

# Menampilkan informasi object pertama
mhs1.info()

# Menampilkan informasi object kedua
mhs2.info()
