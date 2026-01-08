import streamlit as st

# ==========================
# ⚙️ CẤU HÌNH TRANG
# ==========================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.markdown("## 🧭 Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Home – Giới thiệu đề tài",
        "Analysis – Sentiment Analysis",
        "Training Info – Thông tin mô hình"
    ]
)

# ==========================
# 🎨 SIDEBAR – NAVIGATION + THEME
# ==========================
st.sidebar.markdown("## 🧭 Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Home – Giới thiệu đề tài",
        "Analysis – Sentiment Analysis",
        "Training Info – Thông tin mô hình"
    ]
)

theme = st.sidebar.selectbox("🎨 Theme", ["🌞 Light", "🌙 Dark"])

# ==========================
# 🌈 CUSTOM CSS
# ==========================
light_css = """
<style>
body {
    background: linear-gradient(135deg, #fdfcfb, #e2d1c3);
    color: #333;
}
div.stMarkdown, div.stText, div.stRadio, div.stSelectbox {
    background: #ffffffcc;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}
</style>
"""

dark_css = """
<style>
body {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: #f0f0f0;
}
div.stMarkdown, div.stText, div.stRadio, div.stSelectbox {
    background: #2c2c2ccc;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
    color: #f0f0f0;
}
</style>
"""

if theme == "🌞 Light":
    st.markdown(light_css, unsafe_allow_html=True)
else:
    st.markdown(dark_css, unsafe_allow_html=True)

# ==========================
# 🎨 HEADER
# ==========================
col1, col2 = st.columns([1, 9])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/263/263142.png", width=70)
with col2:
    st.markdown(
        """
        <h2 style="color:#2b6f3e; margin-bottom:0;">
        Topic 5: Developing a Sentiment Analysis Application for Product Reviews
        </h2>
        <h4 style="color:#555; margin-top:4px;">
        Supporting E-Commerce Business Decision Making (Open-source + Streamlit)
        </h4>
        """,
        unsafe_allow_html=True
    )

st.write("---")

# ==========================
# 📦 ROUTING
# ==========================
if page == "Home – Giới thiệu đề tài":
    from pages.Home import show
    show()
elif page == "Analysis – Sentiment Analysis":
    from pages.Analysis import show
    show()
elif page == "Training Info – Thông tin mô hình":
    from pages.Training_Info import show
    show()


# ==========================
# 👣 FOOTER – CARDS
# ==========================
st.markdown("---")

# -------- STUDENTS CARD --------
st.markdown(
    """
    <div class="card">
        <div class="card-title">👨‍🎓 Students</div>
        <ul style="margin:0; padding-left:18px;">
            <li>Bui Duc Nguyen – 235053154 – nguyenbd23@uef.edu.vn</li>
            <li>Huynh Ngoc Minh Quan – 235052863 – quanhnm@uef.edu.vn</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# -------- INSTRUCTOR CARD --------
st.markdown(
    """
    <div class="card">
        <div class="card-title">👨‍🏫 Instructor</div>
        <div style="display:flex; align-items:center; gap:10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" width="22">
            <div>
                <b>Bùi Tiến Đức</b> – 
                <a href="https://orcid.org/0000-0001-5174-3558" target="_blank" style="text-decoration:none; color:#1a73e8;">
                    ORCID: 0000-0001-5174-3558
                </a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------- COPYRIGHT --------
st.markdown(
    """
    <div class="footer">
        © 2025 – Topic 5: Sentiment Analysis for E-Commerce
    </div>
    """,
    unsafe_allow_html=True
)
