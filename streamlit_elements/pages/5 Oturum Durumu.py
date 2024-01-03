import streamlit as st 

st.title('Neden State Eklememiz gerekiyor?')
st.markdown('*Problem* tam olarak nedir?')

if not 'count' in st.session_state:
    st.session_state['count'] = 0

'---'

input = st.number_input(
    label = 'Hesap Makinesi', placeholder='Numara gir', value=5,
    key='number-input'
    )
if st.button('Arttır'):
    st.markdown(f'Girilen Numara: **{input}**')
    st.session_state.count += input
    st.markdown(f'Sonuç: **{st.session_state.count}**')
    st.header(st.session_state.count)

'---'
st.session_state