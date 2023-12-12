import streamlit as st

# Definisikan basis pengetahuan
gejala = [
    "Komputer tidak menyala",
    "Kipas tidak berputar",
    "Beberapa port USB tidak berkerja",
    "Layar hitam saat booting",
    "Artefak/garis pada layar",
    "BSOD (Blue Screen of Death)",
    "Program crash",
    "Komputer lambat",
    "Boot looping",
    "Blue screen",
    "Suara click pada HDD",
    "Komputer shutdown sendiri",
    "PC Fans berputar kencang",
    "Restart sendiri",
    "Layar berkedip",
    "Freeze",
    "Tidak ada suara",
    "Suara kotor",
    "Noise pada speaker",
]

bobot_gejala = [
    5, 4, 3, 5, 4, 5, 4, 3, 5, 5, 5, 5, 4, 5, 4, 5, 5, 5, 4,
]

diagnosa = [
    "Motherboard Rusak",
    "VGA Rusak",
    "RAM Rusak",
    "HDD Rusak",
    "Overheating",
    "Power Supply Rusak",
    "Processor Rusak",
    "Sound Card Rusak",
]

rekomendasi_perbaikan = [
    "Ganti motherboard atau bawa ke service center",
    "Bersihkan VGA dari debu, ganti VGA, atau bawa ke service center",
    "Ganti RAM dengan yang baru, cocokkan spesifikasinya",
    "Ganti HDD atau clone ulang data ke HDD baru",
    "Bersihkan CPU fan, heatsink, aplikasikan thermal paste pada CPU",
    "Ganti power supply dengan yang baru dan sesuai kebutuhan",
    "Ganti processor atau bawa ke service center",
    "Ganti sound card USB/PCI, gunakan headphone/speaker USB",
]

# Definisikan rule
rule = [
    ["Komputer tidak menyala", "Kipas tidak berputar", "Beberapa port USB tidak berkerja"],  # Rule untuk Motherboard Rusak
    ["Layar hitam saat booting", "Artefak/garis pada layar"],  # Rule untuk VGA Rusak
    ["BSOD (Blue Screen of Death)", "Program crash", "Komputer lambat"],  # Rule untuk RAM Rusak
    ["Boot looping", "Blue screen", "Suara click pada HDD"],  # Rule untuk HDD Rusak
    ["Komputer shutdown sendiri", "PC Fans berputar kencang"],  # Rule untuk Overheating
    ["Komputer tidak menyala", "Restart sendiri", "Layar berkedip"],  # Rule untuk Power Supply Rusak
    ["Bluescreen", "Freeze", "Restart sendiri"],  # Rule untuk Processor Rusak
    ["Tidak ada suara", "Suara kotor", "Noise pada speaker"],  # Rule untuk Sound Card Rusak
]

# Fungsi untuk memeriksa gejala
def cek_gejala(gejala, bobot_gejala, jawaban):
    if jawaban == "ya":
        return bobot_gejala[gejala]
    else:
        return 0

# Fungsi untuk menghitung kemungkinan kerusakan
def hitung_kemungkinan(selected_gejala, bobot_gejala):
    kemungkinan = [0] * len(diagnosa)
    for i, rule_gejala in enumerate(rule):
        for j, gejala in enumerate(selected_gejala):
            if gejala in rule_gejala:
                kemungkinan[i] += cek_gejala(j, bobot_gejala, "ya")
    return kemungkinan

# Fungsi untuk mendapatkan diagnosa
def get_diagnosa(kemungkinan, diagnosa):
    index_tertinggi = kemungkinan.index(max(kemungkinan))
    return diagnosa[index_tertinggi], rekomendasi_perbaikan[index_tertinggi]

# Tampilkan checkbox untuk gejala
selected_gejala = st.multiselect("Pilih gejala yang dialami:", gejala)

# Tampilkan tombol untuk diagnosis
if st.button("Diagnosis Kerusakan"):
    # Hitung kemungkinan kerusakan
    kemungkinan_kerusakan = hitung_kemungkinan(selected_gejala, bobot_gejala)

    # Dapatkan diagnosa
    hasil_diagnosa, rekomendasi = get_diagnosa(kemungkinan_kerusakan, diagnosa)

    # Tampilkan hasil
    st.write("---")
    st.subheader("Hasil Diagnosis:")
    st.write(f"Jenis Kerusakan: {hasil_diagnosa}")
    st.write(f"Rekomendasi Perbaikan: {rekomendasi}")
