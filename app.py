import streamlit as st
import google.generativeai as genai

# ضبط إعدادات الصفحة
st.set_page_config(page_title="Rabbit Search", page_icon="🐇", layout="centered")

# العنوان واللوجو
st.markdown("<h1 style='text-align: center; color: #f472b6;'>Rabbit 🐇</h1>", unsafe_allow_html=True)

# شريط البحث
query = st.text_input("", placeholder="ابحث في Rabbit عن أي سؤال...")

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Rabbit Search", page_icon="🐇", layout="centered")

st.markdown("<h1 style='text-align: center; color: #f472b6;'>Rabbit 🐇</h1>", unsafe_allow_html=True)

query = st.text_input("", placeholder="ابحث في Rabbit عن أي سؤال...")

if query:
    with st.spinner("جاري القفز بالنتائج... 🐇"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # استخدام الموديل المتوافق تماماً مع المكتبة القديمة
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(query)
            
            st.markdown("---")
            st.subheader("نتيجة البحث الذكية:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء البحث: {e}")