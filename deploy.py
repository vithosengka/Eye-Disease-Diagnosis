import streamlit as st

st.set_page_config(page_title="Sistem Pakar Diagnosis PC")

st.header("Sistem Pakar Diagnosis Kerusakan Komputer")

# Tambah inputan pengguna
nama = st.text_input("Nama:")
alamat = st.text_input("Alamat:")
nomor_hp = st.text_input("Nomor HP:")

kerusakan = {
    "Motherboard Rusak": ["Komputer tidak menyala", "Kipas tidak berputar", "Beberapa port USB tidak berkerja"],
    "VGA Rusak": ["Layar hitam saat booting", "Artefak/garis pada layar"],
    "RAM Rusak": ["BSOD", "Program crash", "Komputer lambat"],
    "HDD Rusak": ["Boot looping", "Blue screen", "Suara click pada HDD"],
    "Overheating": ["Komputer shutdown sendiri", "PC Fans berputar kencang"],
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

# Ambil semua gejala dari setiap jenis kerusakan
semua_gejala = [gejala for gejala_list in kerusakan.values() for gejala in gejala_list]

# Pilih gejala yang dialami oleh pengguna
pilihan_gejala = st.multiselect("Pilih gejala yang dialami:", semua_gejala)

# Tampilkan tombol "Diagnosis Kerusakan"
if st.button("Diagnosis Kerusakan"):
    # Inisialisasi variabel diagnosa dan rekomendasi
    diagnosa_ditemukan = False
    jenis_kerusakan = ""
    rekomendasi_perbaikan = ""

    # Iterasi melalui setiap jenis kerusakan
    for jenis, gejala in kerusakan.items():
        cf = len(set(gejala) & set(pilihan_gejala)) / len(pilihan_gejala)
        if cf >= 0.3:  # Ambang CF
            diagnosa_ditemukan = True
            jenis_kerusakan = jenis
            rekomendasi_perbaikan = rekomendasi[jenis]
            break  # Keluar dari perulangan jika diagnosa ditemukan

    # Tampilkan hasil diagnosis
    st.write("---")
    st.subheader("Profil Pengguna:")
    st.write(f"Nama: {nama}")
    st.write(f"Alamat: {alamat}")
    st.write(f"Nomor HP: {nomor_hp}")

    if diagnosa_ditemukan:
        st.write("---")
        st.subheader("Hasil Diagnosis:")
        st.write(f"Jenis Kerusakan: {jenis_kerusakan}")
        st.write(f"Rekomendasi Perbaikan: {rekomendasi_perbaikan}")
    else:
        if set(pilihan_gejala) - set(semua_gejala):
            st.write("Maaf, beberapa gejala yang Anda pilih tidak dikenali oleh sistem")
        else:
            st.write("Maaf, tidak ditemukan kerusakan")
