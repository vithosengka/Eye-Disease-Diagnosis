import streamlit as st

kerusakan = {
"Motherboard Rusak": ["Komputer tidak menyala", "Kipas tidak berputar","Beberapa port USB tidak bekerja"],  

"VGA Rusak":["Layar hitam saat booting","Artefak/garis pada layar"],

"RAM Rusak": ["BSOD", "Program crash", "Komputer lambat"],

"HDD Rusak":["Boot looping","Blue screen", "Suara click pada HDD"],

"Overheating":["Komputer shutdown sendiri","PC Fans berputar kencang"]   
}

semua_gejala = [gejala for gejala_list in kerusakan.values() for gejala in gejala_list]

st.header("Sistem Pakar Diagnosis Kerusakan PC")
pilihan_gejala = st.multiselect("Pilih gejala yang dialami:", semua_gejala)

diagnosis = []
for penyebab, gejala in kerusakan.items():
    if set(pilihan_gejala) & set(gejala):  
        diagnosis.append(penyebab)

hasil = ", ".join(diagnosis)  
if hasil:
    st.write(f"Kemungkinan kerusakan: {hasil}")
else: 
    st.write("Maaf, tidak ditemukan kerusakan")
