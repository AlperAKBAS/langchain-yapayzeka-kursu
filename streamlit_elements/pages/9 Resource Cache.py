import streamlit as st # 1.29.0
from vega_datasets import data  # pip install vega-datasets 
import pandas as pd  # pip install pandas 
from time import time, sleep
from ydata_profiling import ProfileReport 
# https://github.com/ydataai/ydata-profiling - pip install ydata-profiling
from streamlit_pandas_profiling import st_profile_report 
# https://pypi.org/project/streamlit-pandas-profiling/ - pip install streamlit-pandas-profiling

st.set_page_config(
    page_title= 'Resource Caching',
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
if not 'veri_paketi' in st.session_state:
    st.session_state.veri_paketi = None
if not 'profilleme' in st.session_state:
    st.session_state.profilleme = 0

st.session_state.sayfa_yukleme_sayisi += 1


#### FONKSİYONLARIM
@st.cache_data
def veri_seti_listesi() -> list:
    st.session_state.liste_yukleme_sayisi += 1
    with st.spinner('Liste alınıyor...'):
        sleep(2) # Veri setini çekmemiz biraz zaman alırsa....
        return data.list_datasets() 


def veri_yukle(veri_seti_adi:str) -> bool:
    st.session_state.veri_yukleme_sayisi += 1
    try: 
        st.caption('Veri seti aranıyor.....')
        df = data(veri_seti_adi)
        st.caption('Veri seti bulundu.....')
        st.caption('Toplam satır: {} Toplam Sütun: {}'.format(len(df), df.shape[1]))
        if isinstance(df, pd.DataFrame):
            st.session_state.veri_paketi = {
                'veri_seti_adi': veri_seti_adi,
                'dataframe': df
            }
            return True
        else:
            raise Exception(f'Saçma sapan bir şeyler döndü: {str(type(df))}')
    except Exception as e:
        st.error('Veri yüklenirken birşeyler oldu.')
        st.caption(f':red[{str(e)}]') 

@st.cache_resource
def create_profile(df: pd.DataFrame, minimal: bool = True, title: str = "Veri Profili") -> ProfileReport:
    st.session_state.profilleme += 1
    profile = ProfileReport(df, title=title, minimal=minimal)
    return profile



### SAYFA İÇERİĞİ
st.title('Resource Caching')
st.subheader('Veri seti profilleme..')

input_container = st.container(border=True)
with input_container:
    secilen_veri_seti = st.selectbox(
        'Lütfen bir veri seti seçiniz.', 
        options=veri_seti_listesi()
        )
    
    btn = st.button('Veri setini yükle', help='Lütfen kutucuktan veri setini seçip, tıklayın...')
    if btn:
        with st.status('Veri seti yükleniyor....', expanded=True) as status:
            is_success = veri_yukle(veri_seti_adi=secilen_veri_seti)
            if is_success:
                status.update(label='Veri yükleme tamamlandı...', state='complete', expanded=False)
            else:
                status.update(label=':red[Veri yükleme başarısız oldu...]', state='error', expanded=False)


#### Eğer veri yüklendiyse 
veri_paketi = st.session_state.get('veri_paketi') # dict döndürecek
if isinstance(veri_paketi, dict):
    df = veri_paketi.get('dataframe', None)
    veri_seti_adi = veri_paketi.get('veri_seti_adi', None)
    tabs = st.tabs([f'Veri Seti: **{veri_seti_adi}**', f'Profil **{veri_seti_adi}**'])
    with  tabs[0]:
        st.data_editor(df, use_container_width=True)

    with tabs[1]:
        profil_tipi = st.toggle(
            'Detaylı Profil', value=False, key='profil-tipi', 
            help='Minimal rapor mu?')
        profile_btn = st.button('Veri Profili Oluştur.', key='profil-btn')
        if profile_btn:
            if profil_tipi:
                profile = create_profile(df, minimal=False, title=f'Veri Profili ({veri_seti_adi})')
            else:
                profile = create_profile(df, minimal=True, title=f'Veri Profili ({veri_seti_adi})')
            st_profile_report(profile)

st.subheader(':grey[Ne kaç kez çalıştı?]', divider='grey')
cols = st.columns(4)
cols[0].metric(':red[Sayfa Yüklenmesi]', st.session_state.sayfa_yukleme_sayisi)
cols[1].metric(':red[Liste Yüklenmesi]', st.session_state.liste_yukleme_sayisi)
cols[2].metric(':red[Veri Yüklenmesi]', st.session_state.veri_yukleme_sayisi)
cols[3].metric(':red[Veri Profilleme]', st.session_state.profilleme)
