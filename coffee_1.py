import streamlit as st
import requests
res = requests.get('https://api.sampleapis.com/coffee/hot')
if res.status_code == 200:
        coffee_list = res.json()
        cols = st.columns([0.3,3,0.3])
        with cols[1 ]:
            st.subheader('Popular Coffee Drinks')
            search = st.text_input('Search for drink:',placeholder='🔍 Search for a drink',label_visibility='collapsed')
            for coffee in coffee_list:
                 if search in coffee['title']:
                      with st.container(border = True):
                        cols1 = st.columns([3,2])
                        if coffee['title'] == "title":
                            continue
                        with cols1[0]:
                             st.markdown(f'#### ☕ {coffee["title"]}')
                             st.markdown('###### Description:')
                             st.write(coffee["description"][:70] + '...')
                             st.markdown('###### 🍵 Ingredients:')
                             for n , i in enumerate (coffee["ingredients"]):
                                  st.write(f'{n+1})-{i}')
                              #     st.markdown(coffee["ingredients"])
                        with cols1[1]:
                             st.image(coffee["image"])
