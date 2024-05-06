import streamlit as st

st.write("# AHOJ! 😊 ") 
st.write("## Ak chceš vedieť, ktoré povolanie je práve pre teba, tak si správne.")
st.write ("##### Prefrč touto webstránkou a dozvieš sa zujímavé informácie")

st.write("#### Pre viac informácií KLIKNI NIŽŠIE 👇")

#st.button("MOJE BUDÚCE POVOLANIE")
#st.button("ZÍSKANÉ DÁTA")


st.sidebar.write(" Moja bakalárska práca:")
st.sidebar.write("link")

st.sidebar.write(" Dotazník Google Forms:")
st.sidebar.write("https://docs.google.com/forms/d/1KYRqHZtgQeU5wSXzi1nsgGdUhxtYfZ71QEBy3RtzL5c/viewform?edit_requested=true")

st.sidebar.write(" Užitočné odkazy:")
st.sidebar.write("https://www.trexima.sk/portfolio/aktivne-a-profesionalne-prepojenie-ucastnikov-trhu-prace/")
st.sidebar.write("https://www.trexima.sk/portfolio/uplatnenie-absolventov-v-zamestnani/")

if st.button("MOJE BUDÚCE POVOLANIE"):
    # Redirect to "/grafy" when the button is clicked
    st.markdown('<meta http-equiv="refresh" content="0; URL=/MOJE_BUDÚCE_POVOLANIE" />', unsafe_allow_html=True)

if st.button("ZÍSKANÉ DÁTA"):
    # Redirect to "/grafy" when the button is clicked
    st.markdown('<meta http-equiv="refresh" content="0; URL=/ZÍSKANÉ_DÁTA" />', unsafe_allow_html=True)







