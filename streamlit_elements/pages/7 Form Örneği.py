import streamlit as st # 1.29.0
from vega_datasets import data # 0.9.0
from time import sleep


TITLE = 'Form Örneği'

st.set_page_config(
    page_title=TITLE,
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)
st.title(TITLE)


def ulke_listesi_al() -> list:
    with st.spinner('Ulke listesi aliniyor....'):
        df = data('countries')
        sleep(3)
        countries = df.country.unique().tolist()
        return countries

cols = st.columns(2)


with cols[0]:
    with st.form('kayit-formu'):
        st.subheader('Form ile')
        isim_formsuz = st.text_input('İsim')
        soyisim_formsuz = st.text_input('Soy İsim')
        ulke_formsuz = st.selectbox('Ulke seçiniz', options=ulke_listesi_al())

        if  st.form_submit_button('Gönder'):
            st.success('Bilgileri form aracılığıyla gönderildi.....') 

with cols[1]:
    st.subheader('Form olmadan')
    isim_formsuz = st.text_input('İsim (Formsuz)')
    soyisim_formsuz = st.text_input('Soy İsim (Formsuz)')
    ulke_formsuz = st.selectbox('Ulke seçiniz', options=ulke_listesi_al())

    if st.button('Gönder (Form olmadan)'):
        st.success('Bilgiler Gönderildi')
