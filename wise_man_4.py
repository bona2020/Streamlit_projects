import streamlit as st ##
import requests ##
res = requests.get('http://answerbook.david888.com/?lang=en') ##
if res.status_code == 200: ##
    ans = res.json() ##
    name = st.subheader('Welcome to the [Wise Man] Replier!') ##
    with st.container(border = True): ##
        cols = st.columns([4,1]) ##
        with cols[1]: ##
            but = st.button('Answer!',type='primary') ##
        with cols[0]: ##
            st.write('You:') ##
            with st.container(border = True): ##
                ques = st.text_input('Ask',placeholder = 'Ask any Question!',label_visibility='collapsed') 
            st.write('Wise-Man:')##
            with st.container(border=True):
                if ques == '':
                    st.write('Please Ask Your Question!')
                else:
                    if but:
                        for an in ans:
                            st.write(ans[an])
                    else:
                        st.write('Please Click Answer')


    