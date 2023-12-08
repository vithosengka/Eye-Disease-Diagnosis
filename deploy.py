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
    "Motherboard Rusak": "Ganti motherboard atau bawa ke service center",
    "VGA Rusak": "Ganti VGA atau bersihkan dari debu", 
    "RAM Rusak": "Ganti RAM dengan yang baru, cocokkan spesifikasinya",
    "HDD Rusak": "Ganti HDD atau clone ulang data ke HDD baru",
    "Overheating": "Bersihkan CPU fan, heatsink, aplikasikan thermal paste pada CPU",
    "Power Supply Rusak": "Ganti power supply dengan yang baru dan sesuai kebutuhan",
    "Processor Rusak": "Ganti processor atau bawa ke service center",
    "Sound Card Rusak": "Ganti sound card USB/PCI, gunakan headphone/speaker USB"  
}
    
urutan_gejala = ["Komputer tidak menyala", "Layar hitam", "BSOD", "Program crash", "Boot looping", "Suara klik HDD"]  

def hitung_cf(jumlah_gejala, jumlah_cocok):
    if jumlah_cocok == 0:
        return 0

    return jumlah_cocok / len(jumlah_gejala)

semua_gejala = [gejala for gejala_list in kerusakan.values() for gejala in gejala_list]  

pilihan_gejala = st.multiselect("Pilih gejala yang dialami:", semua_gejala)   

if st.button("Diagnosis Kerusakan"):
      
    ambang_cf = 0.3
    diagnosa_ditemukan = False
    
    for penyebab, gejala in kerusakan.items():
        cf = hitung_cf(len(gejala), len(set(gejala) & set(pilihan_gejala)))
        if (cf >= ambang_cf):
            diagnosa_ditemukan = True
            st.write(f"Kemungkinan kerusakan: {penyebab}")
            st.write(f"Rekomendasi perbaikan: {rekomendasi[penyebab]}")
               
    if not diagnosa_ditemukan:
       if set(pilihan_gejala) - set(semua_gejala):
          st.write("Maaf, beberapa gejala yang Anda pilih tidak dikenali oleh sistem") 
       else:
          st.write("Maaf, tidak ditemukan kerusakan")
              
st.write("---")
st.subheader("Tentang Aplikasi")
st.write("Aplikasi sistem pakar diagnosis kerusakan komputer dengan bahasa pemrograman Python dan framework Streamlit.")
