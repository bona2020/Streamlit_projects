import streamlit as st
import requests
from datetime import datetime 
res = requests.get('https://remoteok.com/api')
if res.status_code ==200:
    jobs = res.json()
    st.subheader('Remote Ok Job Finder!')
    with st.container(border=True):
        cols = st.columns([5,1])
        with cols[0]:
            search = st.text_input('search',placeholder='🔍 Search for a Job',label_visibility='collapsed')
            search= search.title().strip()
            if search != '':
                st.write('Click [Search] to See Search Results!')
        with cols[1]:
            but = st.button('Search',type='primary')
# Search result:
#=====================
    if but and search :
        show = st.markdown('#### 🔍Search Result')
        with st.container(border=True):
            for ind , job_search in enumerate(jobs):
                if ind == 0:
                    continue
                else:
                 if search in job_search["position"]:
                  with st.container(border=True):
                     for k,v in job_search.items():
                        col = st.columns([5,3])
                        if k in ['date','position','company','location','salary_min','salary_max',"apply_url"]:
                                    if k in ['location',"apply_url",'company',]:
                                        with col[1]:
                                            if k == "apply_url":
                                                st.link_button(f'Visit Job Website to Apply',v,type='primary')
                                            elif k == 'company':
                                                st.write(f'{k.title()}:  {v}')
                                            else:
                                                st.write(f'{v}')
                                    else:
                                        with col[0]:
                                            if k == 'position':
                                                st.write(f'##### {v}')
                                            elif 'salary' in k:
                                                if v == 0:
                                                    st.write('Salary:  After Interview')
                                                    break
                                                else:
                                                    if 'min' in k:
                                                        st.write(f'Min-Salary: {v}')
                                                    elif 'max' in k:
                                                        st.write(f'Max-Salary: {v}')
                                                    elif k == 'date':
                                                        timetamp =v
                                                        dt = datetime.fromisoformat(timetamp)
                                                        st.write(f'Posted Time: {dt.strftime("%B %d, %Y at %H:%M")}')
                                                    else:
                                                        st.write(f'{k}: {v}')
                #  elif search not in job_search["position"]:
                #             st.write('#### Sorry No Matching Jobs!')
                #             break
#All jobs
#=======                                    
    else:
        show= st.markdown('#### All The Jobs') 
    with st.container(border=True):
        for ind , job in enumerate(jobs):
            if ind == 0:
                continue
            else:
                with st.container(border=True):
                    col = st.columns([5,3])
                    for item, value in job.items():
                        if item in ['date','position','company','location','salary_min','salary_max',"apply_url"]:
                            if item in ['location',"apply_url",'company',]:
                                with col[1]:
                                    if item == "apply_url":
                                        st.link_button(f'Visit Job Website to Apply',value,type='primary')
                                    elif item == 'company':
                                        st.write(f'{item.title()}:  {value}')
                                    else:
                                        st.write(f'{value}')
                            else:
                                with col[0]:
                                    if item == 'position':
                                        st.write(f'##### {value}')
                                    elif 'salary' in item:
                                        if value == 0:
                                            st.write('Salary:  After Interview')
                                            break
                                        else:
                                            if 'min' in item:
                                                st.write(f'Min-Salary: {value}')
                                            elif 'max' in item:
                                                st.write(f'Max-Salary: {value}')
                                    elif item == 'date':
                                        timestamp =value
                                        dt = datetime.fromisoformat(timestamp)
                                        st.write(f'Posted Time: {dt.strftime("%B %d, %Y at %H:%M")}')
                                    else:
                                        st.write(f'{item}: {value}')

                            
                            