import streamlit as st

# Data penyakit dan gejalanya
penyakit_gejala = {
  "Konjungtivitis": ["Mata merah","Mata berair","Mata gatal"],
  "Katarak": ["Penglihatan buram","Silau berlebih","Sering berkedip"],
  "Glaukoma": ["Penglihatan sempit","Sakit mata","Mata merah","Pusing"],
}

# Fungsi diagnosa
def diagnosa(gejala):   

  hasil = []
  
  for penyakit, gejala_penyakit in penyakit_gejala.items():  
     if set(gejala_penyakit).issubset(set(gejala)):  
        hasil.append(penyakit)
        
  if hasil:
     return f"Kemungkinan penyakit: {', '.join(hasil)}"
  else:   
     return "Tidak dapat mendiagnosis penyakit"
  

# Aplikasi      
st.header("Sistem Pakar Penyakit Mata")
  
gejala = st.multiselect("Pilih gejala yang dialami", ["Mata merah","Mata berair","Penglihatan buram","Pusing", "Sakit Mata"])

if st.button("Diagnosa"):  

  hasil_diagnosa = diagnosa(gejala)  
  
  st.text(hasil_diagnosa)
