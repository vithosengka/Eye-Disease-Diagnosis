import streamlit as st

st.title('Sistem Pakar Diagnosis Penyakit Mata')

st.subheader('Masukkan Gejala yang Dialami')

gejala = []
gejala1 = st.text_input('Gejala 1') 
if gejala1:
    gejala.append(gejala1)
    
gejala2 = st.text_input('Gejala 2')
if gejala2:
    gejala.append(gejala2)

gejala3 = st.text_input('Gejala 3')
if gejala3:
    gejala.append(gejala3) 
    
st.write('Gejala yang Dialami:', ', '.join(gejala))

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

# Logika aturan forward chaining
def diagnosis(gejala):
    hasil_diagnosis = []
    
    for penyakit, gejala_penyakit in database_penyakit_mata.items():
        if all(symptom in gejala for symptom in gejala_penyakit):
            hasil_diagnosis.append(penyakit)

    return hasil_diagnosis

hasil_diagnosis = diagnosis(gejala)
st.subheader('Hasil Diagnosis:')
if hasil_diagnosis:
    st.write('Penyakit mata yang mungkin: ', ', '.join(hasil_diagnosis))
else:
    st.write('Tidak dapat mendiagnosis penyakit mata.')
