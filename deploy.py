import streamlit as st

kerusakan = {
    "Motherboard Rusak": ["Komputer tidak menyala", "Kipas tidak berputar","Beberapa port USB tidak bekerja"],
    "VGA Rusak": ["Layar hitam saat booting","Artefak/garis pada layar"],
    "RAM Rusak": ["BSOD", "Program crash", "Komputer lambat"], 
    "HDD Rusak": ["Boot looping","Blue screen", "Suara click pada HDD"],
    "Overheating": ["Komputer shutdown sendiri","PC Fans berputar kencang"],
    "Power Supply Rusak": ["Komputer tidak menyala", "Restart sendiri", "Layar berkedip"],
    "Processor Rusak": ["Bluescreen", "Freeze", "Restart sendiri"],
    "Sound Card Rusak": ["Tidak ada suara", "Suara kotor", "Noise pada speaker"]   
}

rekomendasi = {
    "Motherboard Rusak": "Ganti motherboard dengan yang baru atau bawa ke service center", 
    "VGA Rusak": "Ganti VGA dengan yang baru, atau bersihkan VGA dari debu",
    "RAM Rusak": "Ganti RAM dengan yang baru, pastikan kapasitas dan jenis RAM cocok",
    "HDD Rusak": "Ganti HDD dengan SSD, atau clone data ke HDD baru",
    "Overheating": "Bersihkan debu pada CPU fan, heatsink, dan case PC, aplikasikan thermal paste baru pada CPU",
    "Power Supply Rusak": "Ganti power supply yang baru dengan daya sesuai kebutuhan",
    "Processor Rusak": "Ganti processor dengan yang baru, atau bawa ke service center",
    "Sound Card Rusak": "Ganti sound card USB/PCI, atau gunakan headphone/speaker USB"  
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
    if len(diagnosis) == 1:
        st.write(f"Rekomendasi perbaikan: {rekomendasi[diagnosis[0]]}") 
    else:
        st.write("Beberapa kemungkinan kerusakan ditemukan. Mohon bawa ke service center untuk diagnosa lebih lanjut.")
else:
    st.write("Maaf, tidak ditemukan kerusakan")

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
    if len(diagnosis) == 1:
        st.write(f"Rekomendasi perbaikan: {rekomendasi[diagnosis[0]]}") 
    else:
        st.write("Beberapa kemungkinan kerusakan ditemukan. Mohon bawa ke service center untuk diagnosa lebih lanjut.")
else:
    st.write("Maaf, tidak ditemukan kerusakan")
