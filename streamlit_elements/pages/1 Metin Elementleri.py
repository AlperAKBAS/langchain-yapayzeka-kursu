import streamlit as st 

TITLE = 'Metin Elementleri'

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



st.title(TITLE)
st.write('Bu bir önek paragraf. bu da paragrafın devamı...')

'Bu da başka bir önek paragraf. bu da paragrafın devamı...'
'Hello, *World!* :sunglasses:'

'---'

"""
# H1
## H2
### H3
            
**bold text**
*italicized text*

1. First item
2. Second item
3. Third item
"""
'---'
st.subheader('Bu bir alt başlık')
st.caption('Bu bir caption daha küçük harfler, özellikle tablo altına gibi')

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python')
st.button(label='Bu bir BTN')
with st.echo():
    st.write('Burası açıklama olsun')
    def hello():
        print("Hello, Streamlit!")
    hello()
    st.write('Bu da son açıklama')

