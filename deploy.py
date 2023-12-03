import streamlit as st

# Database penyakit
penyakit = {
    "Konjungtivitis": ["mata_merah","mata_berair","mata_gatal"],
    "Katarak": ["penglihatan_kabur","silau"],
    "Glaukoma": ["nyeri_mata","penglihatan_kabur","mata_merah","mual","sakit_kepala"],
    "Blefaritis": ["mata_merah","kelopak_mata_bengkak","krusta_mata"],
    "Rabun jauh": ["rabun_jauh","sakit_kepala"]
}

rules = []
for key,value in penyakit.items():
    for v in value:
        rules.append([v,key])

def diagnosis(gejala):  
    facts = gejala
    solutions = []
    target = "penyakit_mata"

    # Forward chaining code   

    return ", ".join(solutions)

st.title("Sistem Pakar Diagnosis Penyakit Mata")
gejala = [] 

# Checkbox gejala
# dst

diagnosis = diagnosis(gejala)  
st.write("Diagnosis:", diagnosis)

def main():
    st.title("Sistem Pakar Diagnosis Penyakit Mata")
    # dst

if __name__ == "__main__":
    main()

