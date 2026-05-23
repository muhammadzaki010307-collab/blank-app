import streamlit as st

# Judul Aplikasi
st.title("🧪 Kalkulator Bobot Molekul (BM)")
st.write("Masukkan rumus kimia untuk menghitung total Bobot Molekul secara otomatis.")

# Data Ar Lengkap untuk 118 Unsur Kimia
AR_DATA = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078,
    "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798, "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224,
    "Nb": 92.906, "Mo": 95.95, "Tc": 98, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
    "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Pm": 145, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50, "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05,
    "Lu": 174.97, "Hf": 178.49, "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08, "Au": 196.97, "Hg": 200.59,
    "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209, "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.04,
    "Pa": 231.04, "U": 238.03, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257,
    "Md": 258, "No": 259, "Lr": 262, "Rf": 267, "Db": 268, "Sg": 271, "Bh": 272, "Hs": 270, "Mt": 276, "Ds": 281,
    "Rg": 280, "Cn": 285, "Nh": 284, "Fl": 289, "Mc": 288, "Lv": 293, "Ts": 294, "Og": 294
}

def hitung_bm(rumus):
    # Menggunakan regex untuk memisahkan Unsur dan Jumlahnya (contoh: H2O -> H:2, O:1)
    # Regex ini mendeteksi Huruf Kapital diikuti huruf kecil (jika ada) dan angka opsional
    pattern = r'([A-Z][a-z]*)(\d*)'
    matches = re.findall(pattern, rumus)
    
    total_bm = 0.0
    rincian = []
    
    for unsur, jumlah in matches:
        jumlah = int(jumlah) if jumlah else 1
        if unsur in AR_DATA:
            ar_unsur = AR_DATA[unsur]
            subtotal = ar_unsur * jumlah
            total_bm += subtotal
            rincian.append({"Unsur": unsur, "Ar": ar_unsur, "Jumlah": jumlah, "Subtotal": round(subtotal, 4)})
        else:
            return None, unsur  # Mengembalikan error jika unsur tidak ditemukan
            
    return round(total_bm, 4), rincian

# Input dari pengguna
rumus_input = st.text_input("Masukkan Rumus Kimia (Contoh: H2O, H2SO4, C6H12O6):", "H2O")

if rumus_input:
    # Bersihkan spasi jika ada
    rumus_bersih = rumus_input.replace(" ", "")
    
    bm, data_proses = hitung_bm(rumus_bersih)
    
    if bm is None:
        st.error(f"⚠️ Unsur **'{data_proses}'** tidak dikenali dalam tabel periodik. Pastikan besar kecil hurufnya benar (Contoh: 'Na', bukan 'na').")
    else:
        st.success(f"### 🧮 Bobot Molekul (BM) dari {rumus_bersih} adalah: **{bm} g/mol**")
        
        # Menampilkan rincian perhitungan dalam bentuk tabel
        st.write("#### Rincian Perhitungan:")
        st.table(data_proses)

---
st.info("💡 **Tips Penulisan:** Perhatikan huruf kapital. Karbon monoksida ditulis **CO**, sedangkan Kobal ditulis **Co**.")
