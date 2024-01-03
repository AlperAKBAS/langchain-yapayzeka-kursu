import streamlit as st
from vega_datasets import data
import pandas as pd
# vega_datasets # pip install vega_datasets
# pip install pandas 
TITLE = "Data Elemanları"

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

mevcut_setler= data.list_datasets()
# st.write(mevcut_setler)
veri_seti_ismi =st.selectbox(
    label='Veri setini seçiniz',
    options=mevcut_setler
)
btn = st.button('Veri setini seç.')
if btn:
    st.write(f'Seçtiğiniz veri seti: **{veri_seti_ismi}**')
    try:
        df = data(veri_seti_ismi) 
        st.caption(f'Satır sayısı: {len(df)}')
        st.data_editor(df, use_container_width=True)
    except Exception as e:
        st.error('Veri seti yüklenemedi.')
        # st.write(str(e)) 


st.subheader('ST METRIC')
st.metric(label="Hava Sıcaklığı", value="25 °C", delta="5 °C")

st.subheader('ST JSON')
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
}, expanded=False)