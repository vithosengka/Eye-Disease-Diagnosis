import streamlit as st

st.set_page_config(page_title="Sistem Pakar Diagnosis PC")
st.header("Sistem Pakar Diagnosis Kerusakan Komputer")

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

# Aturan asosiasi
asosiasi_gejala = {
    "BSOD": ["Program crash", "Komputer lambat"],
    "Suara klik HDD": ["Boot looping","Blue screen"]  
}

# Urutan prioritas gejala
urutan_gejala = ["Komputer tidak menyala", "Layar hitam", "BSOD", "Program crash", "Boot looping", "Suara klik HDD"]

# Fungsi hitung certainty factor
def hitung_cf(jumlah_gejala, jumlah_cocok): 
    if jumlah_cocok == 0:
        return 0
    return jumlah_cocok / jumlah_gejala

# Kode Utama
semua_gejala = [gejala for gejala_list in kerusakan.values() for gejala in gejala_list]  

pilihan_gejala = st.multiselect("Pilih gejala yang dialami:", semua_gejala)   

if st.button("Diagnosis Kerusakan"):
      
    diagnosis = []
    
    for penyebab, gejala in kerusakan.items():
        jumlah_cocok = len(set(gejala) & set(pilihan_gejala))
        cf = hitung_cf(len(gejala), jumlah_cocok)  
        if (cf >= 0.6):
            diagnosis.append(penyebab)
            
    if diagnosis:
        diagnosis = sorted(diagnosis, key=lambda x: hitung_cf(len(kerusakan[x]), len(set(kerusakan[x]) & set(pilihan_gejala))), reverse=True)[0]
        st.write(f"Kemungkinan kerusakan: {diagnosis}") 
        st.write(f"Rekomendasi perbaikan: {rekomendasi[diagnosis]}")
    else:
        st.write("Maaf, tidak ditemukan kerusakan")
        
st.write("---")
st.subheader("Tentang Aplikasi")
st.write("Aplikasi sistem pakar diagnosis kerusakan komputer ini dibuat oleh Claude dengan bahasa pemrograman Python dan framework Streamlit.")
