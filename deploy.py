import streamlit as st

# Definisikan Basis Pengetahuan
kerusakan = {
    "Motherboard Rusak": ["Komputer tidak menyala", "Kipas tidak berputar","Beberapa port USB tidak bekerja"],
    "VGA Rusak":["Layar hitam saat booting","Artefak/garis pada layar"], 
    "RAM Rusak":["BSOD", "Program crash", "Komputer lambat"],
    "HDD Rusak":["Boot looping","Blue screen", "Suara click pada HDD"],  
    "Overheating":["Komputer shutdown sendiri","PC Fans berputar kencang"]  
}

# List semua gejala
semua_gejala = [gejala for penyebab in kerusakan.values() for gejala in penyebab]

st.header("Sistem Pakar Diagnosis Kerusakan Komputer")
selected = st.multiselect("Pilih gejala yang dialami", semua_gejala)

if st.button("Diagnosa"):   
    hasil_diagnosa = []
    
    for penyebab, gejala in kerusakan.items():
        if all(g in selected for g in gejala):
            hasil_diagnosa.append(penyebab)

    if hasil_diagnosa:
        st.subheader("Hasil Diagnosa")
        st.write(f"Kemungkinan Kerusakan: {', '.join(hasil_diagnosa)}")
        st.write("Rekomendasi: Bawa ke teknisi komputer untuk pengecekan lebih lanjut") 
    else:
        st.write("Maaf, sistem tidak dapat menemukan kerusakan")
