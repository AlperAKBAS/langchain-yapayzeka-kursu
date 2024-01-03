import streamlit as st
from vega_datasets import data
import pandas as pd
# vega_datasets # pip install vega_datasets
# pip install pandas 
TITLE = "Chart Örnekleri"

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

df = data('cars')
with st.expander("Grafikler", expanded=False):
    columns = st.columns(2)
    columns[0].subheader('Bar Chart')
    columns[1].subheader('Scatter Chart')
    with columns[0]:
        st.bar_chart(
            data=df,  
            x='Horsepower', 
            y='Cylinders', 
            color='Origin', 
            use_container_width=True
            )

    with columns[1]:
        st.scatter_chart(
            data=df,
            x='Miles_per_Gallon', 
            y='Acceleration',
            color='Origin'
            )


with st.expander('Veri seti', expanded=False):
    st.dataframe(df)
    st.caption(f'{len(df)} satır bulundu.')

container = st.container()


tabs = st.tabs(['Grafikler', 'Veri Seti'])
with tabs[0]:
    columns = st.columns(2)
    columns[0].subheader('Bar Chart')
    columns[1].subheader('Scatter Chart')
    with columns[0]:
        st.bar_chart(
            data=df,  
            x='Horsepower', 
            y='Cylinders', 
            color='Origin', 
            use_container_width=True
            )

    with columns[1]:
        st.scatter_chart(
            data=df,
            x='Miles_per_Gallon', 
            y='Acceleration',
            color='Origin'
            )
        
with tabs[1]:
    st.data_editor(df, use_container_width=True)
    d_btn = st.button('Veriyi İndir')
    if d_btn:
        st.balloons()
        st.snow()
        # st.success('Veri indirildi.')
        container.success('Veri indirildi.')
        container.error('Veri indirilemedi')
        container.caption('Bu da ek olsun')