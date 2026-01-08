import streamlit as st

# ==========================
# 1. CẤU HÌNH TRANG (Luôn ở đầu)
# ==========================
st.set_page_config(
    page_title="Topic 5 – Sentiment Analysis | UEF Project",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# 2. SIDEBAR & THEME SELECTION
# ==========================
with st.sidebar:
    st.markdown(
        '<div style="text-align: center;">'
        '<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="100" style="border-radius: 50%; border: 4px solid #fff; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">'
        '<h2 style="color: #1a73e8; margin-top: 10px;">Topic 5</h2>'
        '<p style="font-size: 14px; color: gray;">Sentiment Analysis App</p>'
        '</div>', 
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Menu điều hướng
    page = st.radio(
        "📂 NAVIGATION",
        ["🏠 Home (Giới thiệu)", "📊 Analysis (Phân tích)", "ℹ️ Training Info (Mô hình)"],
    )
    
    st.markdown("---")
    
    # Chọn giao diện
    theme_mode = st.selectbox("🎨 Giao diện", ["🌊 Ocean Blue (Light)", "🌌 Midnight (Dark)"])

# ==========================
# 3. ADVANCED CSS (SIÊU CẤP)
# ==========================

# Định nghĩa màu sắc dựa trên theme
if theme_mode == "🌊 Ocean Blue (Light)":
    # Gradient xanh dương nhẹ nhàng + mây trắng
    bg_gradient = "linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab)" # Colorful
    bg_gradient = "linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%)" # Blue Sky
    main_bg = """
        background: linear-gradient(-45deg, #a18cd1, #fbc2eb, #a6c1ee, #96e6a1);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    """
    text_color = "#333"
    card_bg = "rgba(255, 255, 255, 0.85)"
    card_border = "1px solid rgba(255, 255, 255, 0.6)"
    
else: # Midnight Dark
    # Gradient tím than + đen huyền bí
    main_bg = """
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #243b55);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    """
    text_color = "#f0f0f0"
    card_bg = "rgba(30, 30, 30, 0.80)" # Màu đen mờ
    card_border = "1px solid rgba(255, 255, 255, 0.1)"

# CSS Injection
st.markdown(f"""
<style>
/* 1. ANIMATED BACKGROUND */
@keyframes gradient {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

.stApp {{
    {main_bg}
    color: {text_color};
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}

/* 2. CARD DESIGN (GLASSMORPHISM) */
div.css-1r6slb0, div.stMarkdown, div.stDataFrame, div[data-testid="stMetricValue"] {{
    /* Không style trực tiếp các div mặc định quá nhiều để tránh vỡ layout, 
       thay vào đó ta dùng class .custom-card bên dưới */
}}

/* Tạo class thẻ bài (Card) riêng để bọc nội dung */
.custom-card {{
    background: {card_bg};
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    border: {card_border};
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}

.custom-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.25);
}}

/* 3. HEADERS & TITLES */
h1, h2, h3 {{
    color: {text_color} !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}}

h1 {{
    font-weight: 800;
    background: -webkit-linear-gradient(45deg, #FF512F, #DD2476);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

/* 4. BUTTONS STYLING */
.stButton > button {{
    background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 10px 25px;
    font-weight: bold;
    transition: all 0.3s;
}}
.stButton > button:hover {{
    transform: scale(1.05);
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}}

/* 5. SIDEBAR STYLING */
[data-testid="stSidebar"] {{
    background-color: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255,255,255,0.1);
}}

</style>
""", unsafe_allow_html=True)

# Hàm tiện ích để tạo Card
def card_start():
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)

def card_end():
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================
# 4. NỘI DUNG TRANG (ROUTING)
# ==========================

if page == "🏠 Home (Giới thiệu)":
    # --- HEADER SECTION ---
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>SENTIMENT ANALYSIS</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: {text_color}; opacity: 0.8;'>Developing a Sentiment Analysis Application for E-Commerce</h3>", unsafe_allow_html=True)
    st.write("") # Spacer

    # --- INFO CARDS ROW 1 ---
    col1, col2 = st.columns(2)
    
    with col1:
        card_start()
        st.markdown("### 🏫 University Info")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/UEF_Logo.png/320px-UEF_Logo.png", width=100)
        st.markdown("""
        **University of Economics & Finance (UEF)** *Faculty of Information Technology* **Course:** Application Development of AI  
        **Class:** 251.ITE1174E.B01E
        """)
        card_end()

    with col2:
        card_start()
        st.markdown("### 👨‍🏫 Instructor")
        st.markdown("""
        <div style="display: flex; align-items: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3429/3429587.png" width="60" style="margin-right: 15px;">
            <div>
                <h4 style="margin:0;">MSc. Bùi Tiến Đức</h4>
                <p style="margin:0; font-size: 0.9em; opacity: 0.8;">ORCID: 0000-0001-5174-3558</p>
                <p style="margin:0; font-size: 0.9em; color: #4CAF50;">Supervising Lecturer</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        card_end()

    # --- STUDENTS SECTION ---
    st.write("")
    card_start()
    st.markdown("### 👨‍🎓 Student Team")
    c1, c2 = st.columns(2)
    with c1:
        st.success("**Huỳnh Ngọc Minh Quan**\n\nID: 235052863")
    with c2:
        st.info("**Bùi Đức Nguyên**\n\nID: 235053154")
    card_end()
    
    # --- ABSTRACT ---
    card_start()
    st.markdown("### 📝 Abstract")
    st.markdown("""
    > "In the rapidly expanding e-commerce sector, customer reviews serve as a vital indicator of product quality... This study aims to design and develop a lightweight, bilingual Sentiment Analysis Application..."
    
    **Keywords:** *Sentiment Analysis, Machine Learning, Logistic Regression, Python, Streamlit.*
    """)
    card_end()

elif page == "📊 Analysis (Phân tích)":
    st.title("📊 Live Sentiment Analysis")
    
    card_start()
    st.markdown("### 💬 Input Text")
    user_input = st.text_area("Nhập bình luận sản phẩm (Tiếng Việt hoặc Tiếng Anh):", height=100)
    
    col_act, col_res = st.columns([1, 2])
    with col_act:
        analyze_btn = st.button("🚀 Analyze Sentiment")
    
    if analyze_btn and user_input:
        with st.spinner("Analyzing..."):
            # Giả lập xử lý (Bạn thay thế bằng model thực tế ở đây)
            import time
            time.sleep(1) 
            sentiment = "Positive" # Thay bằng kết quả model
            score = 0.86
            
        with col_res:
            if sentiment == "Positive":
                st.success(f"**Result:** {sentiment} 😊 (Confidence: {score})")
            elif sentiment == "Negative":
                st.error(f"**Result:** {sentiment} 😡 (Confidence: {score})")
            else:
                st.warning(f"**Result:** {sentiment} 😐 (Confidence: {score})")
                
            st.progress(score)
    card_end()

    # Ví dụ biểu đồ
    card_start()
    st.markdown("### 📈 Batch Analysis Visualization")
    # Fake chart
    st.bar_chart({"Positive": 50, "Negative": 30, "Neutral": 20})
    card_end()

elif page == "ℹ️ Training Info (Mô hình)":
    st.title("ℹ️ Model Architecture")
    
    col1, col2 = st.columns(2)
    with col1:
        card_start()
        st.markdown("### 🇬🇧 English Model")
        st.markdown("""
        * [cite_start]**Algorithm:** Logistic Regression [cite: 32]
        * **Feature Extraction:** TF-IDF Vectorization
        * **Accuracy:** 86%
        * **F1-Score:** 0.84
        """)
        card_end()
        
    with col2:
        card_start()
        st.markdown("### 🇻🇳 Vietnamese Model")
        st.markdown("""
        * [cite_start]**Approach:** Rule-Based (Dictionary) [cite: 33]
        * **Logic:** Positive - Negative Keyword Counting
        * **Libraries:** Python Built-in, RegEx
        """)
        card_end()
        
    card_start()
    st.markdown("### 🚀 Performance Comparison")
    st.table({
        "Model": ["Logistic Regression", "SVM", "XGBoost"],
        "Accuracy": ["86%", "87%", "88%"],
        "Training Time": ["0.5s (Fastest)", "4.2s", "15.6s"]
    })
    [cite_start]st.caption("Table 1: Performance Comparison [cite: 112]")
    card_end()

# ==========================
# 5. FOOTER CHUYÊN NGHIỆP
# ==========================
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 0.8rem;">
        © 2025 Topic 5: Sentiment Analysis for E-Commerce.<br>
        Báo cáo cuối kỳ môn Application Development of AI - UEF.
    </div>
    """, 
    unsafe_allow_html=True
)
