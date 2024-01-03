import streamlit as st # 1.29.0
from vega_datasets import data  # pip install vega-datasets 
import pandas as pd  # pip install pandas 
from time import time, sleep
from ydata_profiling import ProfileReport 
# https://github.com/ydataai/ydata-profiling - pip install ydata-profiling
from streamlit_pandas_profiling import st_profile_report 
# https://pypi.org/project/streamlit-pandas-profiling/ - pip install streamlit-pandas-profiling
import os 


st.set_page_config(
    page_title= 'Dosya Profilleme',
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)

if  not 'dataframe' in st.session_state:
    st.session_state.dataframe = None
if  not 'uploaded_file' in st.session_state:
    st.session_state.uploaded_file = None

@st.cache_resource
def create_profile(df: pd.DataFrame, minimal: bool = True, title: str = "Veri Profili") -> ProfileReport:
    profile = ProfileReport(df, title=title, minimal=minimal)
    return profile


def parse_file(file_obj) -> None:
    _, extension = os.path.splitext(uploaded_file.name)
    
    if not extension in ('.csv', '.txt', '.txt.gz','.xlsx', '.xls' ):
        st.error('Lütfen doğru düzgün bir dosya seçer misin ama?')
        return 
    
    st.session_state.uploaded_file = file_obj
    try:
        if extension in ('.csv', '.txt', '.txt.gz'):
            df =  pd.read_csv(uploaded_file)
            st.session_state.dataframe = df
        elif extension in ('.xlsx', '.xls'):
            df = pd.read_excel(uploaded_file)
            st.session_state.dataframe = df
    except Exception as e:
        st.error('Birşeyler ters gitmiş olabilir...')
        st.caption(f':red[{str(e)}]')


st.title('Dosya Profilleme')

# The UploadedFile class is a subclass of BytesIO, and therefore it is "file-like". This means you can pass them anywhere where a file is expected.
uploaded_file = st.file_uploader(
    label='Veri dosyasını seçin.', 
    type=['csv', 'txt', 'csv.gz', 'txt.gz', 'xlsx', 'xls'], 
    accept_multiple_files=False, 
    key='file_obj', help=None, 
    on_change=None, 
    args=None, kwargs=None,  disabled=False, label_visibility="collapsed")


if uploaded_file:
    parse_btn = st.button('Parse file', on_click=parse_file, kwargs={
        'file_obj': uploaded_file})

                 
result_container = st.container(border=True)
df = st.session_state.get('dataframe')
if isinstance(df, pd.DataFrame):
    with result_container:
        tabs = st.tabs(['Veri Seti', 'Profil'])
        file_obj = st.session_state.uploaded_file
        with tabs[0]:
            st.markdown(f'**Dosya Adı:** {file_obj.name}')
            st.data_editor(df, use_container_width=True)
        with tabs[1]:
            st.markdown(f'**Veri Profili:** {file_obj.name}')
            profil_tipi = st.toggle(
            'Detaylı Profil', value=False, key='profil-tipi', 
            help='Minimal rapor mu?')
            profile_btn = st.button('Veri Profili Oluştur.', key='profil-btn')
            if profile_btn:
                if profil_tipi:
                    profile = create_profile(df, minimal=False, title=f'Veri Profili ({file_obj.name})')
                else:
                    profile = create_profile(df, minimal=True, title=f'Veri Profili ({file_obj.name})')
                st_profile_report(profile)