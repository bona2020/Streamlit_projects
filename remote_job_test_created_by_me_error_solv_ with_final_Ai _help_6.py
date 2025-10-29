import streamlit as st
import requests

res = requests.get('https://remoteok.com/api')
if res.status_code == 200:
    jobs = res.json()

    st.subheader("Remote Ok Job Finder")

    # Search UI
    with st.container(border=True):
        cols = st.columns([5, 1])
        with cols[0]:
            search = st.text_input(
                'Search',
                placeholder='Search for a Job',
                label_visibility='collapsed'
            ).title().strip()
        with cols[1]:
            clc_search = st.button('Search', type='primary')

    # Filter jobs
    filtered_jobs = []
    for ind, job in enumerate(jobs):
        if ind == 0:
            continue  # Skip metadata
        if clc_search and search:
            if search in job.get('position', ''):
                filtered_jobs.append(job)

    # Show search results in a dedicated container
    if clc_search and search:
        if filtered_jobs:
            st.markdown("### 🔍 Search Results")
            for job in filtered_jobs:
                with st.container(border=True):
                    cols = st.columns([3, 2])
                    with cols[0]:
                        st.markdown(f"**{job.get('position', 'No title')}**")
                        st.write(f"Company: {job.get('company', 'Unknown')}")
                        st.write(f"Location: {job.get('location', 'Remote')}")
                        st.write(f"Min Salary: {job.get('salary_min', 'N/A')}")
                        st.write(f"Max Salary: {job.get('salary_max', 'N/A')}")
                    with cols[1]:
                        apply_url = job.get("apply_url") or job.get("url")
                        if apply_url:
                            st.link_button("Apply Now", apply_url, type="primary")
        else:
            st.warning("No jobs matched your search.")
    else:
        st.markdown("### 🧭 All Jobs")
        for ind, job in enumerate(jobs):
            if ind == 0:
                continue
            with st.container(border=True):
                cols = st.columns([3, 2])
                with cols[0]:
                    st.markdown(f"**{job.get('position', 'No title')}**")
                    st.write(f"Company: {job.get('company', 'Unknown')}")
                    st.write(f"Location: {job.get('location', 'Remote')}")
                    st.write(f"Min Salary: {job.get('salary_min', 'N/A')}")
                    st.write(f"Max Salary: {job.get('salary_max', 'N/A')}")
                with cols[1]:
                    apply_url = job.get("apply_url") or job.get("url")
                    if apply_url:
                        st.link_button("Apply Now", apply_url, type="primary")



# import streamlit as st
# import requests 
# res = requests.get('https://remoteok.com/api')
# if res.status_code == 200:
#     jobs = res.json()
#     with st.container(border=True):
#         cols = st.columns([5,1])
#         with cols[0]:
#             search = st.text_input('Search',placeholder='🔍Search for a Job',label_visibility='collapsed')
#             search = search.title().strip()
#         with cols[1]:
#             clc_search = st.button('Search',type='primary')
#         for ind , job in enumerate(jobs):
#             if ind == 0:
#                 continue
#             else:
#                 if clc_search :
#                     if search in job['position'] :
#                         if search not in job['slug','id','epoch','company_logo','tags','description','logo','url']:
#                              with st.container(border=True):
#                                 for item in job:
#                                     if item in ['slug','id','epoch','company_logo','tags','description','logo','url']:
#                                         continue
#                                     else:
#                                         st.write(f'{item}: {job[item]}')
#                 else:
#                     with st.container(border=True):
#                             for item in job:
#                                 if item in ['slug','id','epoch','company_logo','tags','description','logo','url']:
#                                     continue
#                                 else:
#                                     st.write(f'{item}: {job[item]}')
#                     # else:
#                     #     with st.container(border=True):
#                     #         for item in job:
#                     #             if item in ['slug','id','epoch','company_logo','tags','description','logo','url']:
#                     #                 continue
#                     #             else:
#                     #                 st.write(f'{item}: {job[item]}')