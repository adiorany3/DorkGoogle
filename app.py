import streamlit as st
import datetime

st.set_page_config(page_title="Google Dork File Search Generator", page_icon="🔍")

st.title("Google Dork File Search Generator")

st.markdown("""
### How to Use:
1. Select one or more file extensions from the list (e.g., pdf, docx).
2. Enter optional keywords to refine the search.
3. Click the "Search on Google" button to open search results in a new tab.
4. Use the "Reset" button to clear all inputs and start over.
""")

st.write("Select file extensions and enter keywords to generate a Google Dork query.")

# Handle reset
if 'reset' in st.session_state and st.session_state.reset:
    st.session_state.exts = []
    st.session_state.keyword = ""
    st.session_state.reset = False

# Input for file extensions
exts = st.multiselect("Select file extensions", ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "jpg", "jpeg", "png", "gif", "mp3", "mp4", "avi", "zip", "rar", "exe"], key="exts")

# Optional input for keywords
keyword = st.text_input("Keywords (optional)", "", key="keyword")

# Tombol Reset
if st.button("Reset"):
    st.session_state.reset = True
    st.rerun()

if exts:
    # Build query
    if len(exts) == 1:
        query_parts = [f"filetype:{exts[0]}"]
    else:
        query_parts = [f"{' OR '.join([f'filetype:{e}' for e in exts])}"]
    if keyword:
        query_parts.append(keyword)
    query = " ".join(query_parts)
    
    st.code(query)
    
    # Tautan ke Google sebagai tombol
    google_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    st.markdown(f'<a href="{google_url}" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Search on Google</button></a>', unsafe_allow_html=True)
else:
    st.write("Select at least one file extension to start.")

st.write("---")
tahun = datetime.datetime.now().year
st.markdown(f"Developed by Galuh Adi Insani © {tahun} | [search book](https://caribuku.streamlit.app/)")