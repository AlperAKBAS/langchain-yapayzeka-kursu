import streamlit as st # 1.29.0
from vega_datasets import data  # pip install vega-datasets 
import pandas as pd  # pip install pandas 
from time import time, sleep


st.set_page_config(
    page_title= 'Data Caching',
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


##### session state öğelerimiz 
### Sayfa sonunda her bir fonksiyonun kaç kere çalıştığını görüntüleyeceğiz...
if not 'sayfa_yukleme_sayisi' in st.session_state:
    st.session_state.sayfa_yukleme_sayisi = 0
if not 'liste_yukleme_sayisi' in st.session_state:
    st.session_state.liste_yukleme_sayisi = 0
if not 'veri_yukleme_sayisi' in st.session_state:
    st.session_state.veri_yukleme_sayisi = 0



st.session_state.sayfa_yukleme_sayisi += 1


#### FONKSİYONLARIM
@st.cache_data
def veri_seti_listesi() -> list:
    st.session_state.liste_yukleme_sayisi += 1
    with st.spinner('Liste alınıyor...'):
        sleep(2) # Veri setini çekmemiz biraz zaman alırsa....
        return data.list_datasets() 


def veri_yukle(veri_seti_adi:str) -> pd.DataFrame:
    st.session_state.veri_yukleme_sayisi += 1
    try: 
        df = data(veri_seti_adi)
        if isinstance(df, pd.DataFrame):
            return df 
        else:
            raise Exception(f'Saçma sapan bir şeyler döndü: {str(type(df))}')
    except Exception as e:
        st.error('Veri yüklenirken birşeyler oldu.')
        st.caption(f':red[{str(e)}]') 


### SAYFA İÇERİĞİ
st.title('Data Caching')
st.subheader('Veri seti görüntüleme..')


input_container = st.container(border=True)
with input_container:
    secilen_veri_seti = st.selectbox(
        'Lütfen bir veri seti seçiniz.', 
        options=veri_seti_listesi()
        )
    
    btn = st.button('Veri setini yükle', help='Lütfen kutucuktan veri setini seçip, tıklayın...')
    if btn:
        df = veri_yukle(veri_seti_adi=secilen_veri_seti)
        if isinstance(df, pd.DataFrame):
            st.data_editor(df, use_container_width=True)
        else:
            st.error('Veri seti yüklenemedi....')



st.subheader(':grey[Ne kaç kez çalıştı?]', divider='grey')
cols = st.columns(3)
cols[0].metric(':red[Sayfa Yüklenmesi]', st.session_state.sayfa_yukleme_sayisi)
cols[1].metric(':red[Liste Yüklenmesi]', st.session_state.liste_yukleme_sayisi)
cols[2].metric(':red[Veri Yüklenmesi]', st.session_state.veri_yukleme_sayisi)
