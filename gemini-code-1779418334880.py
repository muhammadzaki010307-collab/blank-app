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