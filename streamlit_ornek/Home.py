import streamlit as st 
from dotenv import load_dotenv, find_dotenv
import os 
from langchain.llms.openai import OpenAI
import json

TITLE = 'Basit LLM Örneği'


# Hazırlığımızı burada yapalım
load_dotenv(find_dotenv(), override=True) #  Whether to override the system environment variables with the variables
OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY')

# Session State
if not 'sorgular' in st.session_state:
    st.session_state['sorgular'] = []


st.subheader(TITLE)


soru = st.text_area(
    label='Basit bir prompt',
    value='İklim değişikliği hakkında bilgi verir misin?'
)

columns = st.columns(2)
with columns[0]:
    temperature = st.slider('Temperature', value=0.5, min_value=0.0, max_value=2.0, step=0.1)
    temperature
with columns[1]:
    max_tokens = st.slider('Max Tokens', value=1024, min_value=512, max_value=4096, step=128)
    max_tokens
model_name = st.selectbox('Model seçin', options=(
    'gpt-3.5-turbo-instruct', 'text-davinci-003'
))
btn = st.button('Gönder')
if btn:
    st.write(soru)
    st.write('Seçilen model: {}'.format(model_name))
    llm = OpenAI(
        api_key=OPENAI_APIKEY,
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        max_retries=3
    )
    prompt_token_sayisi = llm.get_num_tokens(soru)
    st.caption(f"Bu soru {prompt_token_sayisi} token'a mal oldu (cevap dahil değil!)")
    st.metric('Sorunun token maliyeti', prompt_token_sayisi)
    with st.spinner('Model çalışıyor....'):
        try:
            cevap = llm(soru)
            if cevap:
                st.markdown(
                    cevap
                )
        except Exception as e:
            st.error('Hata oluştu.')
            st.caption(str(e))
            cevap = ''

        st.session_state.sorgular.append({
            'soru': soru, 
            'cevap': cevap,
            'model': model_name,
            'temperature': temperature,
        })

sorgular = st.session_state.get('sorgular')
if sorgular:
    if len(sorgular) > 0:
        with st.expander('Geçmiş sorgularınız'):
            for s in sorgular:
                st.markdown('##### SORU')
                st.markdown(s.get('soru'))
                st.caption('Model: {}'.format(s.get('model')))
                st.caption('Temperature: {}'.format(s.get('temperature')))
                st.markdown('##### CEVAP')
                st.markdown(s.get('cevap'))
                st.divider()

        st.download_button('Cevapları indir', json.dumps(st.session_state.sorgular), file_name='sorgular.json')