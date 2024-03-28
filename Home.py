import streamlit as st
import pandas as ps

st.set_page_config(layout='wide')



col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', width=300)
with col2:
    st.title('Antal Bako')
    content = 'this is me'
    st.info(content)

content2 = '''
Find some of my projects below.
'''
st.write(content2)

col3, spacer, col4 = st.columns([1.5, 0.5, 1.5])

df = ps.read_csv('data.csv', sep=';')

with col3:
    for i, row in df[0::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source code]({row["url"]})')
with col4:
    for i, row in df[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source code]({row["url"]})')



if __name__ == '__main__':
    print('main')