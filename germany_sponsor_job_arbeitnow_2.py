import streamlit as st
import requests
res = requests.get('https://arbeitnow.com/api/job-board-api')
if res.status_code == 200:
        res = res.json()
        jobs = res["data"]
        cols = st.columns([9,0.1,0.1])
        with cols[0]:
            st.subheader('Germany Sponser / Remote Jobs')
            search = st.text_input('Search for drink:',placeholder='🔍 Search for a Job / Country / Remote:',label_visibility='collapsed')
            search = search.title()
            for job in jobs:
                 if search in job['title'] or search in job['location']:
                      with st.container(border = True):
                        cols1 = st.columns([3,2])
                        with cols1[0]:
                            formatted_title = ' '.join(job["slug"].split('-')[:-1]).title()
                            st.markdown(f'##### {formatted_title}')
                            if job["tags"] != []:
                                st.markdown(f'###### Dep: {job["tags"][0]}')
                            else:
                                st.markdown(f'###### Dep: N/A')
                            if job["job_types"] != []:
                                st.markdown(f'###### Type: {job["job_types"][0]}')
                            else:
                                st.markdown(f'###### Type: N/A')
                            st.write(f'Company Name: {job["company_name"]}')
                            # st.markdown(f'###### Dep: {job["tags"]}')
                            # st.write(f'Company Name: {job["company_name"]}')
                        with cols1[1]:
                            st.link_button('Visit Job Website',job["url"],type='primary')
                            st.markdown(f'###### City: {job["location"]}')
                            if 'Remote' in job["tags"] or  job["remote"] == 'true':
                                job_location = 'No Sponsorship \n[Remote Work]'
                                
                                
                            else:
                                 job_location = 'Sponsored \n[On-Premises]'
                            st.markdown(f'###### Work Type: {job_location} ')#
                            
                            


