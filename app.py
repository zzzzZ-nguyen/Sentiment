import streamlit as st

# ==========================
# ⚙️ CẤU HÌNH TRANG
# ==========================
st.set_page_config(
    page_title="Topic 5 – Sentiment Analysis for E-Commerce",
    page_icon="https://cdn-icons-png.flaticon.com/512/263/263142.png",
    layout="wide"
)

# ==========================
# 🌈 CUSTOM CSS
# ==========================
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(135deg, #f0f4f8, #d9e4ec);
}

/* Card style */
.card {
    background: #ffffff;
    border-radius: 15px;
    padding: 18px 22px;
    margin: 15px auto;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    max-width: 900px;
    font-size: 15px;
    line-height: 1.6;
}

/* Title inside card */
.card-title {
    font-weight: bold;
    font-size: 16px;
    color: #2b6f3e;
    margin-bottom: 8px;
}

/* Footer */
.footer {
    text-align:center;
    margin-top:20px;
    font-size:13px;
    color:#555;
}
</style>
""", unsafe_allow_html=True)

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
page = st.sidebar.radio("Go to:", [
    "Home – Giới thiệu đề tài",
    "Analysis – Sentiment Analysis",
    "Training Info – Thông tin mô hình"
])

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
