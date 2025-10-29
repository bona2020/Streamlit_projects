# To install streamlit Library:
    # pip install streamlit 
    #To Verify:
    #   python 'import streamlit; print(streamlit.__version__)'
    # or streamlit hello
# To install requests Library:
    # pip install requests
    # To Verify python 'import requests; print(requests.__version__)'
#==========================================================
import streamlit as st
import requests 
res = requests.get('http://answerbook.david888.com/?lang=en')
if res.status_code == 200:
    answer = res.json()
    title= st.title('The Magician')
    with st.container(border=True):
        cols =st.columns([4,1])
        with cols[1]: # why to put this first?
            but = st.button('Answer',type='primary')
        with cols[0]:
            st.write('You:')
            ques = st.text_input('My Question',placeholder='Ask any Question',label_visibility='collapsed')
            st.write('The Magician: ')
            with st.container(border=True):
                if ques == '':
                    st.write('Please Ask a Question')
                else:
                    if but :
                        for ans in answer:
                            st.write(answer[ans])
                    else:
                        st.write('Please Click [Answer] to get The Magician reply!')