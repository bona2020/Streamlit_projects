import streamlit as st
import requests
from datetime import datetime
res= requests.get('https://remoteok.com/api')
if res.status_code == 200:
    jobs = res.json()
    st.subheader('Remote Job Finder!')
    search = st.text_input('Search',placeholder='🔍 Search for a Job / Country / Remote',label_visibility='collapsed')
    search = search.title()
    for i in jobs:
     if "last_updated" in i :
         continue
     with st.container(border=True):
           cols = st.columns([3,1])
           for k,v in i.items():
                if k not in ["slug","id","epoch","date","company_logo","tags","description","apply_url","logo","verified"]:
                     with cols[0]:
                          if k == 'position':
                              st.write(f'##### {v}')
                          elif k == 'salary_min':
                              st.write(f'###### Min-Salary:',f'{v}')
                          elif k == 'salary_max':
                              st.write(f'###### Max-Salary:',f'{v}')
                          elif k == 'company':
                              st.write(f' {k}',f'{v}')
                     with cols[1]:
                          if k ==  "url":
                              st.link_button('Visit Job Website',k,type='primary')
                          elif k == 'location':                            
                              st.write(f'###### {k.title()}:',f'{v}')