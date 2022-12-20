class karyawan():
    """Data dan proses karyawan"""
    nama_perusahaan = "Fight United"
    lembur = 150000

    def __init__(self, nama, pendapatan, insentif_proyek):
        """Menghitung pendapatan karyawan"""
        self.nama = nama
        self.pendapatan = pendapatan
        self.insentif_proyek = insentif_proyek
        self.pendapatan_tambahan = 0
        
    def pdptn(self):
        pendapatan = self.pendapatan + self.lembur
        return pendapatan

    def total(self, insentif_proyek):
        jumlah = self.pendapatan + self.insentif_proyek + self.lembur
        return jumlah
        
