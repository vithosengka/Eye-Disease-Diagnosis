import streamlit as st

st.title('Sistem Pakar Diagnosis Penyakit Mata')

st.subheader('Pilih Gejala yang Dialami')

# Database Penyakit Mata
database_penyakit_mata = {
    "Konjungtivitis": ["mata merah", "keluar lendir", "perih"],
    "Miopi": ["pandangan kabur", "sulit melihat jauh"],
    "Hipermetropi": ["sulit melihat dekat", "sakit kepala"],
    "Glaukoma": ["penglihatan sempit", "sakit mata", "mata merah"],
    "Katarak": ["penglihatan buram", "sensitivitas cahaya", "berkedip"],
    "Degenerasi Makula": ["penglihatan pusat kabur", "gangguan warna", "sulit membaca"],
    "Retinopati Diabetik": ["penglihatan buram", "sering pergantian resep kacamata", "kelopak mata bengkak"],
    # dan seterusnya
}

# Membuat list gejala dari database
list_gejala = [gejala for penyakit_gejala in database_penyakit_mata.values() for gejala in penyakit_gejala]

# Menggunakan multiselect untuk input gejala
gejala_terpilih = st.multiselect('Pilih Gejala yang Dialami', list_gejala)

st.write('Gejala yang Dipilih:', ', '.join(gejala_terpilih))

# Fungsi untuk Logika aturan forward chaining
def diagnosis_mata(gejala_terpilih):
    hasil_diagnosis = []
    
    for penyakit, gejala_penyakit in database_penyakit_mata.items():
        if all(gejala_penyakit in gejala_terpilih for gejala_penyakit in gejala):
           hasil_diagnosis.append(penyakit)

    return hasil_diagnosis

# Tombol "Diagnosa"
if st.button('Diagnosa'):
   hasil_diagnosis_mata = diagnosis_mata(gejala_terpilih)

   if hasil_diagnosis_mata:
      st.write('Penyakit mata yang mungkin: ', ', '.join(hasil_diagnosis_mata)) 
   else:
      st.write('Tidak dapat mendiagnosis penyakit mata.')


