import streamlit as st
import datetime

st.set_page_config(page_title="Google Dork File Search Generator", page_icon="🔍")

st.title("Google Dork File Search Generator")

st.markdown("""
### Cara Penggunaan:
1. Pilih satu atau lebih ekstensi file dari daftar (misalnya: pdf, docx).
2. Masukkan kata kunci opsional untuk menyempurnakan pencarian.
3. Klik tombol "Cari di Google" untuk membuka hasil pencarian di tab baru.
4. Gunakan tombol "Reset" untuk menghapus semua input dan memulai ulang.
""")

st.write("Pilih ekstensi file dan masukkan kata kunci untuk menghasilkan query Google Dork.")

# Handle reset
if 'reset' in st.session_state and st.session_state.reset:
    st.session_state.exts = []
    st.session_state.keyword = ""
    st.session_state.reset = False

# Input untuk ekstensi file
exts = st.multiselect("Pilih ekstensi file", ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "jpg", "jpeg", "png", "gif", "mp3", "mp4", "avi", "zip", "rar", "exe"], key="exts")

# Input opsional untuk kata kunci
keyword = st.text_input("Kata kunci (opsional)", "", key="keyword")

# Tombol Reset
if st.button("Reset"):
    st.session_state.reset = True
    st.rerun()

if exts:
    # Bangun query
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
    st.markdown(f'<a href="{google_url}" target="_blank"><button style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Cari di Google</button></a>', unsafe_allow_html=True)
else:
    st.write("Pilih setidaknya satu ekstensi file untuk memulai.")

st.write("---")
tahun = datetime.datetime.now().year
st.write(f"Developed by Galuh Adi Insani © {tahun}")