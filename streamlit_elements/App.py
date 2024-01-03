import streamlit as st 

TITLE = 'İlk appimizi yapıyoruz....'

st.set_page_config(
    page_title=TITLE,
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.sidebar:
    st.subheader('Bu sidebarda yazılacak')
    st.write('Burada text yazabilirim')
    st.caption('Aslında buraya birçok yapı koyabilirim.')

st.title(TITLE)


