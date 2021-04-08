class User():
    def __init__(self, nama, noHp, jenis, pesanan, jumlah, mode):
        self.nama = nama
        self.noHp = noHp
        self.jenis = jenis
        self.pesanan = pesanan
        self.jumlah = jumlah
        self.mode = mode

    def get_nama(self):
        return self.nama
    def get_noHp(self):
        return self.noHp
    def get_jenis(self):
        return self.jenis
    def get_pesanan(self):
        return self.pesanan
    def get_jumlah(self):
        return self.jumlah
    def get_mode(self):
        return self.mode