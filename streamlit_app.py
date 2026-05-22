import streamlit as st

st.title("🎈 Jurnalika")
st.write(
    "Kami Bnagga Jadi PERS Kampus [jurnalika.com](https://www.jurnalikanews.com/)."
)
import streamlit as st
from chemlib import Compound

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Bobot Molekul", page_icon="🧪")

st.title("🧪 Kalkulator Bobot Molekul")
st.markdown("Hitung Massa Molar (Mr) senyawa kimia secara instan.")

# Input Rumus Kimia
formula_input = st.text_input("Masukkan Rumus Kimia (Contoh: H2SO4, C6H12O6, NaCl)", "")

if formula_input:
    try:
        # Menggunakan chemlib untuk parsing dan perhitungan
        comp = Compound(formula_input)
        molecular_weight = comp.molar_mass()
        
        # Tampilan Hasil
        st.success(f"**Bobot Molekul: {molecular_weight:.4f} g/mol**")
        
        # Detail Komposisi Unsur
        st.subheader("Rincian Komposisi:")
        details = comp.occurences
        
        # Membuat tabel rincian
        data = []
        for element, count in details.items():
            data.append({"Unsur": element, "Jumlah Atom": count})
        
        st.table(data)
        
    except Exception as e:
        st.error(f"Kesalahan: Pastikan rumus kimia benar (perhatikan huruf besar/kecil, misal: 'NaCl' bukan 'nacl').")

st.info("Database Ar diambil berdasarkan standar IUPAC terbaru melalui library chemlib.")
