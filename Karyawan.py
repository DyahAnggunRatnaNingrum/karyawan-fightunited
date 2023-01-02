import calendar

class karyawan():
    """Data karyawan dan pendapatan"""
    gaji_pokok = 3000000
    gaji_lembur = 500000

    def __init__(self, nama, gaji_pokok, gaji_lembur):
        """Menghitung total pendapatan karyawan"""
        self.nama = nama
        self.gaji_pokok = gaji_pokok
        self.gaji_lembur = gaji_lembur

    def total_pendapatan(self):
        pendapatan = self.gaji_pokok + self.gaji_lembur
        return total_pendapatan
    
