import streamlit as st
import google.generativeai as genai

# إعدادات الصفحة
st.set_page_config(page_title="Rabbit Search", page_icon="🐇", layout="centered")

# العنوان واللوجو
st.markdown("<h1 style='text-align: center; color: #f472b6;'>Rabbit 🐇</h1>", unsafe_allow_html=True)

# شريط البحث بحجم ومعرف فريد
query = st.text_input("", placeholder="ابحث في Rabbit عن أي سؤال...", key="rabbit_search_input")

if query:
    with st.spinner("جاري القفز بالنتائج... 🐇"):
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # تجربة الموديل
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(query)
            
            st.markdown("---")
            st.subheader("نتيجة البحث الذكية:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء البحث: {e}")