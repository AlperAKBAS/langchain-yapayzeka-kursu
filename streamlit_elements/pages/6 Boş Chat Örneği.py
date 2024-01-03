import streamlit as st 
from vega_datasets import data
import numpy as np


TITLE = 'Chat Örneği'

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

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state['messages']:
    role = message.get('role')
    content = message.get('content')
    with st.chat_message(role):
        st.markdown(content)



prompt = st.chat_input('Lütfen sorunuzu sorun...')
if prompt:
    with st.chat_message('user'):
        st.markdown(prompt)
        st.session_state.messages.append({
            'role': 'user',
            'content': prompt
        })
    with st.chat_message('asistan'):
        cevap = f'{prompt} dediniz....'
        st.markdown(cevap)
        # st.line_chart(np.random.randn(30, 3))
        st.session_state.messages.append({
            'role': 'asistan',
            'content': cevap
        })

