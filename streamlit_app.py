import streamlit as st

st.title("🎈 Jurnalika")
st.write(
    "Kami Bnagga Jadi PERS Kampus [jurnalika.com](https://www.jurnalikanews.com/)."
)
-- Membuat Tabel Unsur
CREATE TABLE tabel_periodik (
    nomor_atom INTEGER PRIMARY KEY,
    simbol VARCHAR(3) NOT NULL,
    nama VARCHAR(25) NOT NULL,
    massa_atom DECIMAL(10, 4),
    golongan INTEGER,
    periode INTEGER
);

-- Mengisi Data (Sampel Unsur Utama)
INSERT INTO tabel_periodik (nomor_atom, simbol, nama, massa_atom, golongan, periode) VALUES
(1, 'H', 'Hidrogen', 1.008, 1, 1),
(2, 'He', 'Helium', 4.0026, 18, 1),
(3, 'Li', 'Litium', 6.94, 1, 2),
(4, 'Be', 'Berilium', 9.0122, 2, 2),
(5, 'B', 'Boron', 10.81, 13, 2),
(6, 'C', 'Karbon', 12.011, 14, 2),
(7, 'N', 'Nitrogen', 14.007, 15, 2),
(8, 'O', 'Oksigen', 15.999, 16, 2),
(9, 'F', 'Fluorine', 18.998, 17, 2),
(10, 'Ne', 'Neon', 20.180, 18, 2),
(11, 'Na', 'Natrium', 22.990, 1, 3),
(12, 'Mg', 'Magnesium', 24.305, 2, 3),
(13, 'Al', 'Aluminium', 26.982, 13, 3),
(14, 'Si', 'Silikon', 28.085, 14, 3),
(15, 'P', 'Fosfor', 30.974, 15, 3),
(16, 'S', 'Sulfur', 32.06, 16, 3),
(17, 'Cl', 'Klorin', 35.45, 17, 3),
(18, 'Ar', 'Argon', 39.948, 18, 3);

import chemparse
from mendeleev import element

def hitung_bobot_molekul(formula):
    """
    Menghitung total massa molar berdasarkan formula string.
    Contoh: 'H2O', 'C6H12O6', 'Al2(SO4)3'
    """
    try:
        # Parsing formula menjadi dict, misal: {'Al': 2, 'S': 3, 'O': 12}
        komposisi = chemparse.parse_formula(formula)
        total_massa = 0.0
        rincian = []

        for simbol, jumlah in komposisi.items():
            unsur = element(simbol)
            massa_atom = unsur.atomic_weight
            massa_total_unsur = massa_atom * jumlah
            total_massa += massa_total_unsur
            
            rincian.append({
                "unsur": simbol,
                "jumlah": jumlah,
                "massa_satuan": round(massa_atom, 4),
                "subtotal": round(massa_total_unsur, 4)
            })

        return round(total_massa, 4), rincian

    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    print("--- Kalkulator Bobot Molekul ---")
    senyawa = input("Masukkan formula kimia (contoh: H2O atau Mg(OH)2): ")
    
    hasil, detail = hitung_bobot_molekul(senyawa)
    
    if hasil:
        print(f"\nSenyawa: {senyawa}")
        print(f"Total Bobot Molekul: {hasil} g/mol")
        print("-" * 30)
        for d in detail:
            print(f"{d['unsur']}: {d['jumlah']} x {d['massa_satuan']} = {d['subtotal']}")
    else:
        print(f"Error: Terjadi kesalahan saat memproses formula. Pastikan penulisan benar.")
