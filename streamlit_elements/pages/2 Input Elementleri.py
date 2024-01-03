import streamlit as st 

TITLE = 'Input Örnekleri'

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
st.title(TITLE)


'---'

st.subheader('Buttonlar')
btn = st.button(label='Bu bir button')

if btn:
    st.write(f'Butona bastın....e')

'---'
st.subheader('Toggle')
on = st.toggle('Activate feature')

if on:
    st.write('Aktive edildi.!')

'---'
st.subheader('Select Box')
secim = st.selectbox(
    'Ne şekilde iletişim kurulsun?',
    ('Email', 'Şahsi Telefon', 'Mobile Telefon'))

btn_sbmit = st.button('Sec', key='secim-btn', help='Burası yardım metini olacak..')
if btn_sbmit:
    st.write('Şunu Seçtiniz:', secim)

'---'
st.subheader('Slider')
age = st.slider('Boyunuz kaç cm?', min_value=100.0, max_value=220.00, value=150.00, step=0.5)
st.write(f'{age} cm boyundayım...')