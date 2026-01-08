import streamlit as st

st.set_page_config(
    page_title="Topic 5 – Sentiment Analysis for E-Commerce",
    page_icon="https://cdn-icons-png.flaticon.com/512/263/263142.png",
    layout="wide"
)

# ==========================
# 🌈 CUSTOM CSS CHỈNH MÀU
# ==========================
st.markdown("""
<style>
/* Avatar khung tròn + màu viền */
.sidebar-avatar {
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
}
.sidebar-avatar img {
    border-radius: 50%;
    border: 3px solid #2b6f3e;   /* viền xanh lá */
    box-shadow: 0 4px 10px rgba(0,0,0,0.25);
    width: 90px;
}

/* Tiêu đề Navigation */
.sidebar-title {
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    color: #1a73e8;   /* xanh dương nổi bật */
    margin-bottom: 12px;
}

/* Radio button màu đẹp */
div[role="radiogroup"] > label {
    background: #f0f8ff;
    border-radius: 8px;
    padding: 6px 10px;
    margin: 4px 0;
}
div[role="radiogroup"] > label:hover {
    background: #d6eaf8;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# 📌 SIDEBAR – NAVIGATION
# ==========================
st.sidebar.markdown(
    '<div class="sidebar-avatar"><img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"></div>',
    unsafe_allow_html=True
)
st.sidebar.markdown('<div class="sidebar-title">🧭 Navigation</div>', unsafe_allow_html=True)

page = st.sidebar.radio(
    "Go to:",
    [
        "Home – Giới thiệu đề tài",
        "Analysis – Sentiment Analysis",
        "Training Info – Thông tin mô hình"
    ]
)

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
