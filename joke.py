import streamlit as st
import requests
import time
res = requests.get('https://teehee.dev/api/joke')
if res.status_code == 200:
    jok_bank = res.json()
    title= st.subheader('Welcome to The Comedy Club App')
    question = st.text_input('Joke',placeholder='Do you want to hear a Joke? Yes/NO',label_visibility='collapsed')
    question = question.lower().strip()
    if question in ['yes','y']:
        with st.container(border=True):
            for joke in jok_bank:
                if joke not in ['id','permalink','permalink_html']:
                    if joke == 'question':
                        st.write(f'###### {jok_bank[joke]}')
                    elif joke == 'answer':
                        st.write('##### 😎 Joker: ')
                        with st.spinner('🤔Hmmm...'):
                         time.sleep(4)
                         with st.container(border=True):
                                st.write(f' {jok_bank[joke]} 🤣')
    but = st.button('Next',type='primary')
        
