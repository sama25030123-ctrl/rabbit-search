import streamlit as st
from google import genai

# إعدادات الصفحة
st.set_page_config(page_title="Rabbit Search", page_icon="🐇", layout="centered")

# CSS لتنسيق الواجهة
st.markdown("""
    <style>
    .stApp {
        background-color: #1f1b24;
        color: white;
    }
    .stTextInput input {
        border-radius: 30px !important;
        padding: 12px 20px !important;
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

# اللوجو والعنوان
st.markdown("<h1 style='text-align: center; color: #f2a6d0; font-size: 72px;'>Rabbit 🐇</h1>", unsafe_allow_html=True)


query = st.text_input("", placeholder="ابحث في Rabbit أو اسأل أي سؤال...")

if query:
    with st.spinner("جاري القفز بالنتائج... 🐇"):
        try:
            client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=query
            )
            
            st.markdown("---")
            st.subheader("نتيجة البحث الذكية:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء البحث: {e}")