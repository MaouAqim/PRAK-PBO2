from functools import wraps


class Bank:
    def __init__(self, nama, saldo):
        self._nama = nama
        self._saldo = saldo
        print(f"Nasabah bernama: {nama} memiliki saldo {saldo} telah ditambahkan!")

    def __del__(self):
        print(f"Nasabah bernama: {self._nama} dengan sisa saldo sekarang {self._saldo}!")

    # Decorator untuk validasi input angka
    def validasi_angka(func):
        @wraps(func)
        def wrapper(self, a):
            if not isinstance(a, (int, float)):
                raise ValueError("Input harus angka!")
            return func(self, a)
        return wrapper

    # Method setor tunai
    @validasi_angka
    def setor_tunai(self, nominal):
        self._saldo += nominal
        print(f"Nasabah dengan nama: {self._nama} telah melakukan setor tunai senilai {nominal}. Sehingga saldo sekarang: {self._saldo}")

    # Method tarik tunai
    @validasi_angka
    def tarik_tunai(self, nominal):
        if nominal > self._saldo:
            raise ValueError("Saldo tidak cukup!")
        self._saldo -= nominal
        print(f"Nasabah dengan nama: {self._nama} telah menarik tunai senilai {nominal}. Sehingga sisa saldo sekarang: {self._saldo}")


# Inisiasi object Bank
bank = Bank("Aqim", 1000000)

# Menjalankan operasi
bank.setor_tunai(500000)
bank.tarik_tunai(200000)

# Kode di bawah ini tidak akan dijalankan karena program telah selesai

print("TERIMAKASIH")
