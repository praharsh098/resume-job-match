import streamlit as st
import requests
from PyPDF2 import PdfReader

API_URL = "http://localhost:8000"   # hardcoded for local dev

st.set_page_config(page_title='Resume → Job Matcher', layout='centered')
st.title('AI Resume → Job Matcher')

st.markdown('Upload your resume (PDF or TXT) or paste it below to find matching jobs.')

uploaded = st.file_uploader('Upload resume (PDF or TXT)', type=['txt', 'pdf'])

text = ""
if uploaded is not None:
    if uploaded.type == "application/pdf":
        pdf = PdfReader(uploaded)
        text = "\n".join([page.extract_text() or "" for page in pdf.pages])
    else:  # txt
        text = uploaded.read().decode('utf-8')
else:
    text = st.text_area('Paste resume text here', height=300)

if st.button('Find Matches'):
    if not text.strip():
        st.error('Please provide resume text')
    else:
        with st.spinner('Querying API...'):
            try:
                resp = requests.post(f'{API_URL}/match', json={'resume_text': text, 'top_k': 5}, timeout=30)
                resp.raise_for_status()
                jobs = resp.json()
                if not jobs:
                    st.info('No matches found.')
                else:
                    for j in jobs:
                        st.subheader(f"{j['title']} — {j['company']}")
                        st.write(f"**Location:** {j['location']}  ")
                        st.write(f"**Score:** {j['score']:.3f}")
                        st.write(j['description'])
                        st.markdown('---')
            except requests.RequestException as e:
                st.error(f'Failed to query API: {e}')

st.markdown('---')
st.caption('This demo uses Sentence-BERT to compute semantic similarity between resumes and job descriptions.')
