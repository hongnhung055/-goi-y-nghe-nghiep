
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ==========================================
# 1. CAU HINH
# ==========================================

st.set_page_config(
    page_title="Định hướng nghề nghiệp CNTT",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_model():
    model = joblib.load(
        BASE_DIR / "models/best_model_tuan7.pkl"
    )
    encoder = joblib.load(
        BASE_DIR / "models/label_encoder_tuan7.pkl"
    )
    features = joblib.load(
        BASE_DIR / "models/feature_columns_tuan7.pkl"
    )
    return model, encoder, features


try:
    model, encoder, feature_columns = load_model()
except Exception as e:
    st.error("Không thể tải mô hình Machine Learning.")
    st.exception(e)
    st.stop()


# ==========================================
# 2. GIAO DIEN CSS
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #0f2747;
    --primary: #1f5fbf;
    --primary-soft: #e8f0fc;
    --accent: #14a38b;
    --ink: #1c2a3a;
    --muted: #64748b;
    --line: #e3e9f1;
    --bg: #f4f7fb;
    --card: #ffffff;
}

html, body, [class*="css"], .stApp, .stMarkdown, button, input, textarea, select {
    font-family: 'Be Vietnam Pro', 'Segoe UI', system-ui, sans-serif !important;
}

.stApp { background: var(--bg); }

#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }

.block-container {
    max-width: 1180px;
    padding-top: 1.2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 { color: var(--navy); letter-spacing: -0.01em; }

/* ---------- Thanh dieu huong tren cung ---------- */
.topbar {
    display: flex; align-items: center; justify-content: space-between;
    gap: 12px; flex-wrap: wrap;
    padding: 6px 2px 18px 2px;
}
.brand { display: flex; align-items: center; gap: 12px; }
.brand-logo {
    width: 42px; height: 42px; border-radius: 12px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    display: grid; place-items: center; color: #fff; font-size: 22px;
    box-shadow: 0 6px 16px rgba(31, 95, 191, .25);
}
.brand-name { font-weight: 800; color: var(--navy); font-size: 17px; line-height: 1.1; }
.brand-sub { color: var(--muted); font-size: 12.5px; }
.badge-pill {
    background: #fff; border: 1px solid var(--line); color: var(--muted);
    padding: 6px 12px; border-radius: 999px; font-size: 12.5px; font-weight: 500;
}
.badge-pill b { color: var(--accent); }

/* ---------- Hero ---------- */
.hero {
    position: relative; overflow: hidden;
    background: radial-gradient(circle at 85% 20%, rgba(20,163,139,.35), transparent 40%),
                linear-gradient(125deg, #0f2747 0%, #173f78 55%, #1f5fbf 100%);
    border-radius: 22px;
    padding: 40px 42px;
    color: #fff;
    margin-bottom: 22px;
    box-shadow: 0 18px 40px rgba(15, 39, 71, .18);
}
.hero .eyebrow {
    display: inline-block; font-size: 12px; font-weight: 600; letter-spacing: .08em;
    text-transform: uppercase; background: rgba(255,255,255,.12);
    border: 1px solid rgba(255,255,255,.2); padding: 5px 12px; border-radius: 999px;
}
.hero h1 { color: #fff; font-size: 38px; font-weight: 800; margin: 14px 0 10px 0; line-height: 1.2; }
.hero p { color: #d6e4fb; font-size: 16.5px; max-width: 680px; margin: 0; }
.hero-stats { display: flex; gap: 14px; margin-top: 26px; flex-wrap: wrap; }
.hero-stat {
    background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.18);
    border-radius: 14px; padding: 12px 18px; min-width: 130px;
}
.hero-stat .num { font-size: 24px; font-weight: 800; color: #fff; }
.hero-stat .lbl { font-size: 12.5px; color: #c7d8f5; }

/* ---------- The quy trinh (bam de nhay toi phan tuong ung) ---------- */
a.step-card, a.step-card:hover { text-decoration: none !important; color: inherit !important; }
.step-card {
    position: relative; display: block;
    background: var(--card); border: 1px solid var(--line); border-radius: 16px;
    padding: 18px 20px; height: 100%;
    box-shadow: 0 1px 2px rgba(15,39,71,.04);
    transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
}
.step-card:hover {
    transform: translateY(-3px); border-color: #c5d6f0;
    box-shadow: 0 14px 28px rgba(15,39,71,.09);
}
.step-card::after {
    content: "→"; position: absolute; top: 18px; right: 20px;
    color: #b6c4d8; font-weight: 700; transition: transform .15s ease, color .15s ease;
}
.step-card:hover::after { color: var(--primary); transform: translateX(3px); }
.step-num {
    width: 32px; height: 32px; border-radius: 10px;
    background: linear-gradient(135deg, var(--primary), var(--accent));
    color: #fff; font-weight: 700; display: grid; place-items: center; font-size: 14px;
    box-shadow: 0 4px 10px rgba(31,95,191,.25);
}
.step-card h4 { margin: 12px 0 4px 0; font-size: 15.5px; }
.step-card p { margin: 0; color: var(--muted); font-size: 13.5px; }

.section-title { margin: 32px 0 4px 0; font-size: 24px; font-weight: 800; color: var(--navy); }
.section-sub { color: var(--muted); font-size: 14.5px; margin-bottom: 6px; }

/* ---------- Tieu de tung phan (1 trang) ---------- */
.step-heading {
    display: flex; align-items: center; gap: 14px;
    margin: 34px 0 14px 0; scroll-margin-top: 16px;
}
.step-heading .step-num { flex-shrink: 0; width: 40px; height: 40px; border-radius: 12px; font-size: 17px; }
.step-heading .sh-title { font-size: 20px; font-weight: 800; color: var(--navy); line-height: 1.2; }
.step-heading .sh-sub { font-size: 13.5px; color: var(--muted); margin-top: 2px; }
.step-heading::after {
    content: ""; flex: 1; height: 1px; margin-left: 8px;
    background: linear-gradient(90deg, var(--line), transparent);
}

/* ---------- Khung noi dung ---------- */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--card);
    border-radius: 18px !important;
    border-color: var(--line) !important;
    box-shadow: 0 1px 3px rgba(15,39,71,.04), 0 8px 24px rgba(15,39,71,.04);
}
.panel-head { display: flex; align-items: center; gap: 12px; margin-bottom: 4px; }
.panel-icon {
    width: 38px; height: 38px; border-radius: 11px; background: var(--primary-soft);
    display: grid; place-items: center; font-size: 18px;
}
.panel-title { font-weight: 700; color: var(--navy); font-size: 17px; }
.panel-sub { color: var(--muted); font-size: 13.5px; margin: 4px 0 12px 0; }

/* ---------- O nhap lieu ---------- */
div[data-baseweb="input"], div[data-baseweb="select"] > div {
    background: #fff !important; border-radius: 10px !important;
}
div[data-testid="stNumberInputContainer"] { border-radius: 10px; }
div[data-testid="stWidgetLabel"] p { font-weight: 500; color: var(--ink); }
div[data-testid="stSlider"] { padding-bottom: 4px; }
div[data-testid="stSliderThumbValue"] { font-weight: 700; }
span[data-baseweb="tag"] {
    background: var(--primary-soft) !important; color: var(--primary) !important;
    border-radius: 999px !important; font-weight: 600;
}
span[data-baseweb="tag"] svg { fill: var(--primary) !important; }

.note {
    border-radius: 12px; padding: 11px 14px; font-size: 13.5px; margin-top: 8px;
    background: #f1f5fa; color: #475569; border: 1px dashed #cdd8e6;
}
.note.warn { background: #fff8eb; color: #8a5a00; border: 1px solid #f6dfae; }

/* ---------- Nut bam ---------- */
.stButton > button[kind="primary"] {
    background: linear-gradient(120deg, var(--primary), #2b7be0);
    border: none; border-radius: 12px; padding: 0.8rem 1rem;
    font-weight: 700; letter-spacing: .02em;
    box-shadow: 0 10px 22px rgba(31,95,191,.28);
}
.stButton > button[kind="primary"]:hover { filter: brightness(1.06); }

/* ---------- Ket qua ---------- */
.result-hero {
    background: linear-gradient(130deg, #0f2747, #1f5fbf);
    color: #fff; border-radius: 20px; padding: 30px 32px; margin: 8px 0 18px 0;
    box-shadow: 0 16px 36px rgba(15,39,71,.2);
}
.result-hero .label { font-size: 12.5px; letter-spacing: .1em; text-transform: uppercase; color: #bcd2f5; font-weight: 600; }
.result-hero .role { font-size: 32px; font-weight: 800; margin: 6px 0 2px 0; color: #fff; }
.result-hero .role-en { color: #c7d8f5; font-size: 14.5px; }
.result-hero .desc {
    margin-top: 16px; background: rgba(255,255,255,.1); border-radius: 12px;
    padding: 12px 16px; color: #eaf2ff; font-size: 14.5px;
}
.result-hero .score { font-size: 40px; font-weight: 800; color: #fff; line-height: 1; }
.result-hero .score-lbl { font-size: 12.5px; color: #bcd2f5; }

.rank-row { display: flex; align-items: center; gap: 14px; padding: 12px 0; border-bottom: 1px solid var(--line); }
.rank-row:last-child { border-bottom: none; }
.rank-badge {
    width: 34px; height: 34px; border-radius: 10px; display: grid; place-items: center;
    font-weight: 800; font-size: 15px; flex-shrink: 0;
}
.r1 { background: #fff4d6; color: #a86b00; }
.r2 { background: #eef1f5; color: #52606d; }
.r3 { background: #fbeadf; color: #a3542a; }
.rank-body { flex: 1; min-width: 0; }
.rank-name { font-weight: 700; color: var(--ink); font-size: 15px; }
.rank-en { color: var(--muted); font-size: 12.5px; }
.bar { height: 8px; background: #edf2f8; border-radius: 99px; margin-top: 8px; overflow: hidden; }
.bar > span { display: block; height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--primary), var(--accent)); }
.rank-pct { font-weight: 800; color: var(--primary); font-size: 16px; min-width: 64px; text-align: right; }
.bar > .stack { display: flex; height: 100%; border-radius: 99px; overflow: hidden; }
.bar > .stack > span { display: block; height: 100%; }
.s-ml { background: var(--primary) !important; }
.s-ng { background: var(--accent) !important; }
.s-st { background: #f0a43a !important; }
.rank-src { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 6px; font-size: 12px; color: var(--muted); }
.rank-src .dot { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 5px; vertical-align: 0; }

.mini-bar-row { margin: 9px 0; }
.mini-bar-top { display: flex; justify-content: space-between; font-size: 13.5px; color: var(--ink); }
.mini-bar-top span:last-child { color: var(--muted); font-weight: 600; }

.chip {
    display: inline-block; background: var(--primary-soft); color: var(--primary);
    border-radius: 999px; padding: 4px 11px; font-size: 12.5px; font-weight: 600; margin: 3px 4px 3px 0;
}

div[data-testid="stMetric"] {
    background: #f8fafd; padding: 14px 16px; border-radius: 12px; border: 1px solid var(--line);
}
div[data-testid="stMetricLabel"] p { color: var(--muted); font-size: 13px; font-weight: 600; }
div[data-testid="stMetricValue"] > div {
    font-size: 21px !important; font-weight: 700; color: var(--navy);
    white-space: normal !important; line-height: 1.3;
}

.footer { text-align: center; color: var(--muted); font-size: 13px; margin-top: 36px; }

@media (max-width: 640px) {
    .hero { padding: 28px 22px; }
    .hero h1 { font-size: 28px; }
    .result-hero .role { font-size: 25px; }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# 3. DU LIEU NGANH HOC
# ==========================================


nganh_hoc = {
    "Công nghệ thông tin": [
        "Nhập môn lập trình",
        "Lập trình hướng đối tượng",
        "Cấu trúc dữ liệu và giải thuật",
        "Cơ sở dữ liệu",
        "Mạng máy tính",
        "Hệ điều hành",
        "Công nghệ phần mềm",
        "Lập trình Web",
        "Phân tích thiết kế hệ thống",
        "An toàn thông tin"
    ],

    "Trí tuệ nhân tạo": [
        "Nhập môn trí tuệ nhân tạo",
        "Lập trình Python",
        "Toán cao cấp",
        "Xác suất thống kê",
        "Cấu trúc dữ liệu và giải thuật",
        "Học máy",
        "Học sâu",
        "Khoa học dữ liệu",
        "Xử lý ngôn ngữ tự nhiên",
        "Thị giác máy tính"
    ],

    "An ninh mạng": [
        "Mạng máy tính",
        "Hệ điều hành",
        "An toàn thông tin",
        "Mật mã học",
        "Bảo mật mạng",
        "Bảo mật hệ điều hành",
        "An ninh ứng dụng Web",
        "Phân tích mã độc",
        "Kiểm thử xâm nhập",
        "Điều tra số"
    ],

    "Khoa học máy tính": [
        "Nhập môn lập trình",
        "Toán rời rạc",
        "Cấu trúc dữ liệu và giải thuật",
        "Lập trình hướng đối tượng",
        "Cơ sở dữ liệu",
        "Hệ điều hành",
        "Trí tuệ nhân tạo",
        "Học máy",
        "Lý thuyết tính toán",
        "Phân tích thuật toán"
    ],

    "Kỹ thuật phần mềm": [
        "Nhập môn lập trình",
        "Lập trình hướng đối tượng",
        "Cấu trúc dữ liệu và giải thuật",
        "Cơ sở dữ liệu",
        "Công nghệ phần mềm",
        "Phân tích thiết kế hệ thống",
        "Kiểm thử phần mềm",
        "Quản lý dự án phần mềm",
        "Phát triển ứng dụng Web",
        "Phát triển ứng dụng di động"
    ],

    "Kỹ thuật máy tính": [
        "Kiến trúc máy tính",
        "Kỹ thuật điện tử",
        "Điện tử số",
        "Kỹ thuật vi xử lý",
        "Lập trình C/C++",
        "Hệ điều hành",
        "Hệ thống nhúng",
        "Thiết kế mạch số",
        "Mạng máy tính",
        "Internet vạn vật (IoT)"
    ]
}


ky_nang_khac = [
    "Tư duy logic",
    "Sáng tạo",
    "Làm việc nhóm",
    "Giải quyết vấn đề"
]

so_thich_options = [
    "Lập trình phần mềm",
    "Trí tuệ nhân tạo",
    "An ninh mạng",
    "Thiết kế đồ họa",
    "Quản lý dự án",
    "Phân tích dữ liệu",
    "Mạng máy tính",
    "Phần cứng",
    "Kiểm thử phần mềm",
    "Nghiên cứu công nghệ"
]

# 4 thuoc tinh goc co thang 0-6
nang_luc = {
    "Computer Architecture": "Kiến trúc máy tính",
    "Programming Skills": "Kỹ năng lập trình",
    "Project Management": "Quản lý dự án",
    "Communication skills": "Kỹ năng giao tiếp"
}

# 10 thuoc tinh goc co thang 0-1
tinh_cach = {
    "Openness": "Tính cởi mở",
    "Conscientousness": "Tính tận tâm",
    "Extraversion": "Tính hướng ngoại",
    "Agreeableness": "Tính hòa đồng",
    "Emotional_Range": "Biến động cảm xúc",
    "Conversation": "Khả năng hội thoại",
    "Openness to Change": "Sẵn sàng thay đổi",
    "Hedonism": "Xu hướng tận hưởng",
    "Self-enhancement": "Phát triển bản thân",
    "Self-transcendence": "Quan tâm cộng đồng"
}

# ==========================================
# 4. TEN NGHE VA MO TA
# ==========================================

ten_nghe = {
    "AI ML Specialist": "Chuyên gia AI và học máy",
    "API Specialist": "Chuyên gia API",
    "Application Support Engineer": "Kỹ sư hỗ trợ ứng dụng",
    "Business Analyst": "Chuyên viên phân tích nghiệp vụ",
    "Customer Service Executive": "Chuyên viên chăm sóc khách hàng",
    "Cyber Security Specialist": "Chuyên gia an ninh mạng",
    "Database Administrator": "Quản trị viên cơ sở dữ liệu",
    "Graphics Designer": "Chuyên viên thiết kế đồ họa",
    "Hardware Engineer": "Kỹ sư phần cứng",
    "Helpdesk Engineer": "Kỹ sư hỗ trợ kỹ thuật",
    "Information Security Specialist": "Chuyên gia bảo mật thông tin",
    "Networking Engineer": "Kỹ sư mạng",
    "Project Manager": "Quản lý dự án",
    "Software Developer": "Lập trình viên phần mềm",
    "Software tester": "Kiểm thử viên phần mềm",
    "Technical Writer": "Chuyên viên tài liệu kỹ thuật"
}

mo_ta = {
    "AI ML Specialist": "Xây dựng mô hình trí tuệ nhân tạo và học máy.",
    "API Specialist": "Phát triển và tích hợp giao diện lập trình API.",
    "Application Support Engineer": "Hỗ trợ vận hành và xử lý sự cố ứng dụng.",
    "Business Analyst": "Phân tích yêu cầu nghiệp vụ và đề xuất giải pháp.",
    "Customer Service Executive": "Hỗ trợ khách hàng và giải quyết yêu cầu dịch vụ.",
    "Cyber Security Specialist": "Phát hiện và phòng chống các cuộc tấn công mạng.",
    "Database Administrator": "Quản trị, sao lưu và tối ưu cơ sở dữ liệu.",
    "Graphics Designer": "Thiết kế hình ảnh và sản phẩm đồ họa.",
    "Hardware Engineer": "Thiết kế, kiểm tra và bảo trì phần cứng.",
    "Helpdesk Engineer": "Hỗ trợ người dùng xử lý sự cố kỹ thuật.",
    "Information Security Specialist": "Bảo vệ dữ liệu và hệ thống thông tin.",
    "Networking Engineer": "Triển khai và quản trị hệ thống mạng.",
    "Project Manager": "Lập kế hoạch và điều phối các dự án.",
    "Software Developer": "Thiết kế, lập trình và bảo trì phần mềm.",
    "Software tester": "Kiểm thử và đánh giá chất lượng phần mềm.",
    "Technical Writer": "Biên soạn tài liệu kỹ thuật và hướng dẫn sử dụng."
}


# ==========================================
# 4b. LUAT KET HOP NGANH HOC VA SO THICH
# ==========================================
# Mo hinh ML chi dung 14 thuoc tinh (nang luc + tinh cach) va khong biet
# nganh hoc. Phan nay bo sung diem theo luat chuyen gia:
#   Diem cuoi = w_ml * mo hinh ML + w_nganh * nganh hoc + w_st * so thich
# w_ml toi da 50% va giam theo do tu tin cua mo hinh: khi nguoi dung de
# cac nang luc ngang nhau, mo hinh chi doan mo (nghe cao nhat ~30%) nen
# phan ML gan nhu khong tinh; phan con lai chia cho nganh/so thich theo 3:2.
# Trong so 1.0 = nghe dung chuyen nganh, 0.5 = nghe lien quan.

TRONG_SO = {"ml": 0.5, "nganh": 0.3, "so_thich": 0.2}


def tinh_trong_so(xac_suat_ml):
    """Tra ve (w_ml, w_nganh, w_so_thich, do_tin_cay) cong lai bang 1."""
    n = len(xac_suat_ml)
    do_tin_cay = max(0.0, (max(xac_suat_ml) - 1 / n) / (1 - 1 / n))
    w_ml = TRONG_SO["ml"] * do_tin_cay
    con_lai = 1 - w_ml
    ti_le_nganh = TRONG_SO["nganh"] / (TRONG_SO["nganh"] + TRONG_SO["so_thich"])
    return w_ml, con_lai * ti_le_nganh, con_lai * (1 - ti_le_nganh), do_tin_cay

nganh_nghe = {
    "Công nghệ thông tin": {
        "Software Developer": 1.0, "Database Administrator": 1.0,
        "Networking Engineer": 0.5, "Application Support Engineer": 0.5,
        "Helpdesk Engineer": 0.5, "API Specialist": 0.5,
        "Business Analyst": 0.5, "Software tester": 0.5,
    },
    "Trí tuệ nhân tạo": {
        "AI ML Specialist": 1.0, "Software Developer": 0.5,
        "Business Analyst": 0.5, "Database Administrator": 0.3,
    },
    "An ninh mạng": {
        "Cyber Security Specialist": 1.0, "Information Security Specialist": 1.0,
        "Networking Engineer": 0.5,
    },
    "Khoa học máy tính": {
        "Software Developer": 1.0, "AI ML Specialist": 1.0,
        "API Specialist": 0.5, "Database Administrator": 0.5,
    },
    "Kỹ thuật phần mềm": {
        "Software Developer": 1.0, "Software tester": 1.0,
        "API Specialist": 0.5, "Project Manager": 0.5,
        "Application Support Engineer": 0.5, "Technical Writer": 0.3,
    },
    "Kỹ thuật máy tính": {
        "Hardware Engineer": 1.0, "Networking Engineer": 1.0,
        "Helpdesk Engineer": 0.5, "Application Support Engineer": 0.3,
    },
}

so_thich_nghe = {
    "Lập trình phần mềm": {"Software Developer": 1.0, "API Specialist": 0.7},
    "Trí tuệ nhân tạo": {"AI ML Specialist": 1.0},
    "An ninh mạng": {"Cyber Security Specialist": 1.0, "Information Security Specialist": 1.0},
    "Thiết kế đồ họa": {"Graphics Designer": 1.0},
    "Quản lý dự án": {"Project Manager": 1.0, "Business Analyst": 0.5},
    "Phân tích dữ liệu": {"Business Analyst": 1.0, "AI ML Specialist": 0.5,
                          "Database Administrator": 0.5},
    "Mạng máy tính": {"Networking Engineer": 1.0},
    "Phần cứng": {"Hardware Engineer": 1.0},
    "Kiểm thử phần mềm": {"Software tester": 1.0},
    "Nghiên cứu công nghệ": {"AI ML Specialist": 0.5, "Technical Writer": 0.5},
}


def phan_bo_theo_luat(danh_sach_nghe, cac_luat):
    """Cong trong so cua cac luat cho tung nghe roi chuan hoa tong = 1."""
    diem = pd.Series(0.0, index=danh_sach_nghe)
    for luat in cac_luat:
        for nghe, w in luat.items():
            if nghe in diem.index:
                diem[nghe] += w
    tong = diem.sum()
    return diem / tong if tong > 0 else diem


# ==========================================
# HAM TIEN ICH GIAO DIEN
# ==========================================

def panel_header(icon, title, sub=""):
    st.markdown(
        f"""
        <div class="panel-head">
            <div class="panel-icon">{icon}</div>
            <div class="panel-title">{title}</div>
        </div>
        {f'<div class="panel-sub">{sub}</div>' if sub else ''}
        """,
        unsafe_allow_html=True
    )


def note(text, warn=False):
    cls = "note warn" if warn else "note"
    st.markdown(f'<div class="{cls}">{text}</div>', unsafe_allow_html=True)


def mini_bars(items, max_value=10.0):
    html = ""
    for label, value in items:
        pct = max(0.0, min(100.0, value / max_value * 100))
        html += f"""
        <div class="mini-bar-row">
            <div class="mini-bar-top"><span>{label}</span><span>{value:g}/{max_value:g}</span></div>
            <div class="bar"><span style="width:{pct:.1f}%"></span></div>
        </div>
        """
    st.markdown(html, unsafe_allow_html=True)


# ==========================================
# 5. BANNER
# ==========================================

st.markdown("""
<div class="topbar">
    <div class="brand">
        <div class="brand-logo">🎓</div>
        <div>
            <div class="brand-name">CareerPath IT</div>
            <div class="brand-sub">Hệ thống định hướng nghề nghiệp cho sinh viên</div>
        </div>
    </div>
    <div class="badge-pill">Mô hình <b>●</b> sẵn sàng</div>
</div>

<div class="hero">
    <span class="eyebrow">Machine Learning · Định hướng nghề nghiệp</span>
    <h1>Khám phá nghề nghiệp CNTT<br>phù hợp với bạn</h1>
    <p>Trả lời vài câu hỏi về năng lực và tính cách. Hệ thống sẽ phân tích và đề xuất
    những vị trí công việc Công nghệ thông tin phù hợp nhất với hồ sơ của bạn.</p>
    <div class="hero-stats">
        <div class="hero-stat"><div class="num">16</div><div class="lbl">Nghề nghiệp CNTT</div></div>
        <div class="hero-stat"><div class="num">14</div><div class="lbl">Thuộc tính phân tích</div></div>
        <div class="hero-stat"><div class="num">4</div><div class="lbl">Bước đánh giá</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

steps = [
    ("1", "Học tập", "Ngành học, GPA và điểm các môn chuyên ngành."),
    ("2", "Năng lực", "Tự đánh giá kỹ năng chuyên môn và kỹ năng mềm."),
    ("3", "Tính cách", "Sở thích và các đặc điểm cá nhân."),
    ("4", "Kết quả", "Nhận đề xuất nghề nghiệp và top 3 phù hợp."),
]

step_cols = st.columns(4)
for col, (num, title, desc) in zip(step_cols, steps):
    with col:
        st.markdown(
            f"""
            <a class="step-card" href="#buoc-{num}" target="_self">
                <div class="step-num">{num}</div>
                <h4>{title}</h4>
                <p>{desc}</p>
            </a>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="section-title">Bắt đầu đánh giá</div>'
    '<div class="section-sub">Điền lần lượt các phần bên dưới, '
    'sau đó nhấn <b>Xem kết quả dự đoán</b> ở cuối trang.</div>',
    unsafe_allow_html=True
)


# ==========================================
# 6. NHAP THONG TIN
# ==========================================

def step_heading(num, title, sub=""):
    st.markdown(
        f'<div class="step-heading" id="buoc-{num}">'
        f'<div class="step-num">{num}</div>'
        f'<div><div class="sh-title">{title}</div>'
        f'{f"<div class=sh-sub>{sub}</div>" if sub else ""}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ------------------------------------------
# PHAN 1: HOC TAP
# ------------------------------------------

step_heading(1, "📚 Học tập", "Ngành học, GPA và điểm các môn chuyên ngành")
with st.container():
    with st.container(border=True):
        panel_header("🎓", "Thông tin học tập", "Chọn ngành học hiện tại và nhập GPA của bạn.")

        c1, c2 = st.columns([2, 1])
        with c1:
            nganh = st.selectbox(
                "Ngành học hiện tại",
                list(nganh_hoc.keys()),
                key="chon_nganh"
            )
        with c2:
            gpa = st.number_input(
                "Điểm GPA (thang 4.0)",
                min_value=0.0,
                max_value=4.0,
                value=3.0,
                step=0.1,
                format="%.2f",
                key="gpa"
            )

    with st.container(border=True):
        panel_header("📘", "Điểm các môn chuyên ngành", f"Ngành <b>{nganh}</b> · thang điểm 10")

        diem_mon = {}
        cols = st.columns(3)
        danh_sach_mon = nganh_hoc[nganh]

        for i, mon in enumerate(danh_sach_mon):
            with cols[i % 3]:
                diem_mon[mon] = st.number_input(
                    mon,
                    min_value=0.0,
                    max_value=10.0,
                    value=7.0,
                    step=0.5,
                    key=f"mon_{nganh}_{i}"
                )

        note("ℹ️ GPA và điểm môn học được ghi nhận nhưng chưa tham gia dự đoán.")


# ------------------------------------------
# PHAN 2: NANG LUC
# ------------------------------------------

step_heading(2, "💡 Năng lực", "Kéo thanh trượt để tự đánh giá kỹ năng của bạn")
with st.container():
    col_a, col_b = st.columns(2, gap="medium")

    with col_a:
        with st.container(border=True):
            panel_header("🛠️", "Năng lực chuyên môn", "Tự đánh giá từ 0 (thấp nhất) đến 10 (cao nhất).")

            diem_nang_luc = {}
            for feature, label in nang_luc.items():
                diem_nang_luc[feature] = st.slider(
                    label,
                    min_value=0.0,
                    max_value=10.0,
                    value=5.0,
                    step=0.5,
                    key=f"nl_{feature}"
                )
            note("✅ Bốn năng lực này được mô hình sử dụng để dự đoán.")

    with col_b:
        with st.container(border=True):
            panel_header("🤝", "Kỹ năng bổ sung", "Các kỹ năng mềm hỗ trợ công việc.")

            diem_ky_nang_khac = {}
            for i, label in enumerate(ky_nang_khac):
                diem_ky_nang_khac[label] = st.slider(
                    label,
                    min_value=0.0,
                    max_value=10.0,
                    value=5.0,
                    step=0.5,
                    key=f"other_{i}"
                )
            note("ℹ️ Kỹ năng bổ sung chỉ dùng để hiển thị trong hồ sơ.")


# ------------------------------------------
# PHAN 3: TINH CACH
# ------------------------------------------

step_heading(3, "🧭 Tính cách", "Sở thích và các đặc điểm cá nhân")
with st.container():
    with st.container(border=True):
        panel_header("❤️", "Lĩnh vực quan tâm", "Chọn ít nhất một lĩnh vực bạn yêu thích.")

        so_thich = st.multiselect(
            "Bạn quan tâm đến lĩnh vực nào?",
            so_thich_options,
            key="so_thich",
            placeholder="Chọn một hoặc nhiều lĩnh vực..."
        )

    with st.container(border=True):
        panel_header("🧠", "Đặc điểm cá nhân", "Đánh giá từ 0 đến 10 theo cảm nhận của bản thân.")

        diem_tinh_cach = {}
        cols = st.columns(2, gap="large")

        for i, (feature, label) in enumerate(tinh_cach.items()):
            with cols[i % 2]:
                diem_tinh_cach[feature] = st.slider(
                    label,
                    min_value=0.0,
                    max_value=10.0,
                    value=5.0,
                    step=0.5,
                    key=f"tc_{feature}"
                )

        note(
            "⚠️ Các đặc điểm cá nhân đang được tự đánh giá theo cách thử nghiệm, "
            "chưa phải thang đo tâm lý được kiểm chứng.",
            warn=True
        )


# ------------------------------------------
# PHAN 4: DU DOAN
# ------------------------------------------

step_heading(4, "🎯 Dự đoán", "Kiểm tra lại hồ sơ và xem kết quả")
with st.container():
    with st.container(border=True):
        panel_header("🎯", "Sẵn sàng khám phá nghề nghiệp?",
                     "Kiểm tra nhanh hồ sơ của bạn trước khi xem kết quả.")

        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Ngành học", nganh)
        with m2:
            st.metric("GPA", f"{gpa:.2f} / 4.00")
        with m3:
            st.metric("Lĩnh vực quan tâm", f"{len(so_thich)} đã chọn")

        note(
            "Điểm phù hợp được kết hợp từ 3 nguồn: <b>mô hình ML</b> "
            "(4 năng lực + 10 đặc điểm cá nhân, tối đa 50% tùy độ tự tin), "
            "<b>ngành học</b> và <b>lĩnh vực quan tâm</b>. Hãy đánh giá năng lực có "
            "điểm mạnh, điểm yếu rõ ràng để mô hình ML có căn cứ. GPA, điểm môn học "
            "và kỹ năng bổ sung chưa ảnh hưởng đến kết quả."
        )

        st.write("")
        submitted = st.button(
            "🔍  XEM KẾT QUẢ DỰ ĐOÁN",
            type="primary",
            width="stretch"
        )


# ==========================================
# 7. XU LY DU DOAN
# ==========================================

# Ghi nho da bam nut: ket qua van hien va tu cap nhat khi nguoi dung
# chinh lai thanh truot, thay vi bien mat sau moi lan thay doi.
if submitted:
    st.session_state["da_du_doan"] = True

if st.session_state.get("da_du_doan") and not so_thich:
    st.warning(
        "Vui lòng chọn ít nhất một lĩnh vực quan tâm ở bước 3 (Tính cách)."
    )

elif st.session_state.get("da_du_doan"):

    # Quy doi ve thang du lieu goc
    input_data = {}

    for feature, score in diem_nang_luc.items():
        input_data[feature] = score * 6.0 / 10.0

    for feature, score in diem_tinh_cach.items():
        input_data[feature] = score / 10.0

    # Kiem tra du 14 thuoc tinh
    missing = [
        f for f in feature_columns
        if f not in input_data
    ]

    if missing:
        st.error(
            "Thiếu thuộc tính mô hình: "
            + ", ".join(missing)
        )
        st.stop()

    input_df = pd.DataFrame(
        [[input_data[f] for f in feature_columns]],
        columns=feature_columns
    )

    try:
        # ----------------------------------
        # KET HOP 3 NGUON DIEM CHO 16 NGHE
        # ----------------------------------

        nghe_anh = encoder.inverse_transform(model.classes_.astype(int))

        xac_suat_ml = model.predict_proba(input_df)[0]
        w_ml, w_nganh, w_st, do_tin_cay = tinh_trong_so(xac_suat_ml)

        diem_nghe = pd.DataFrame({
            "Nghe_anh": nghe_anh,
            "Diem_ML": xac_suat_ml,
        })
        diem_nghe["Diem_nganh"] = phan_bo_theo_luat(
            nghe_anh, [nganh_nghe.get(nganh, {})]
        ).to_numpy()
        diem_nghe["Diem_so_thich"] = phan_bo_theo_luat(
            nghe_anh, [so_thich_nghe.get(s, {}) for s in so_thich]
        ).to_numpy()
        diem_nghe["Diem"] = (
            w_ml * diem_nghe["Diem_ML"]
            + w_nganh * diem_nghe["Diem_nganh"]
            + w_st * diem_nghe["Diem_so_thich"]
        )
        diem_nghe["Nghe_viet"] = diem_nghe["Nghe_anh"].map(
            lambda x: ten_nghe.get(x, x)
        )

        top3 = diem_nghe.sort_values("Diem", ascending=False).head(3)

        role = top3.iloc[0]["Nghe_anh"]
        role_vi = top3.iloc[0]["Nghe_viet"]
        top_score = float(top3.iloc[0]["Diem"])

        st.markdown(
            '<div class="section-title">🎯 Kết quả định hướng nghề nghiệp</div>',
            unsafe_allow_html=True
        )

        # Mo hinh ML phan biet nghe chu yeu dua vao nang luc noi troi
        # (vd. Kien truc may tinh cao -> Ky su phan cung). Neu 4 nang luc
        # bang nhau thi phan ML khong co can cu ro rang.
        if len(set(diem_nang_luc.values())) == 1:
            note(
                "⚠️ <b>Bốn năng lực chuyên môn của bạn đang bằng nhau</b>, nên phần "
                "mô hình ML không có căn cứ rõ ràng; kết quả chủ yếu dựa vào ngành học "
                "và lĩnh vực quan tâm. Hãy quay lại <a href='#buoc-2' target='_self'>bước 2</a> "
                "và đánh giá điểm mạnh nổi bật của bạn để kết quả chính xác hơn.",
                warn=True
            )

        score_html = (
            f'<div style="text-align:right">'
            f'<div class="score">{top_score * 100:.1f}%</div>'
            f'<div class="score-lbl">Điểm phù hợp</div></div>'
        )

        st.markdown(
            f"""
            <div class="result-hero">
                <div style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:flex-start">
                    <div>
                        <div class="label">Nghề nghiệp được đề xuất</div>
                        <div class="role">{role_vi}</div>
                        <div class="role-en">{role}</div>
                    </div>
                    {score_html}
                </div>
                <div class="desc"><b>Mô tả công việc:</b> {mo_ta.get(role, "Chưa có mô tả.")}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        left, right = st.columns([3, 2], gap="medium")

        with left:
            if top3 is not None:
                with st.container(border=True):
                    panel_header("🏆", "Top 3 nghề nghiệp phù hợp")
                    rows_html = ""
                    for i, (_, row) in enumerate(top3.iterrows(), start=1):
                        pct = row["Diem"] * 100
                        ml = w_ml * row["Diem_ML"] * 100
                        ng = w_nganh * row["Diem_nganh"] * 100
                        st_ = w_st * row["Diem_so_thich"] * 100
                        w_ml, w_ng, w_st = (
                            (x / pct * 100 if pct > 0 else 0) for x in (ml, ng, st_)
                        )
                        rows_html += f"""
                        <div class="rank-row">
                            <div class="rank-badge r{i}">{i}</div>
                            <div class="rank-body">
                                <div class="rank-name">{row['Nghe_viet']}</div>
                                <div class="rank-en">{row['Nghe_anh']}</div>
                                <div class="bar"><div class="stack" style="width:{pct:.1f}%"><span class="s-ml" style="width:{w_ml:.1f}%"></span><span class="s-ng" style="width:{w_ng:.1f}%"></span><span class="s-st" style="width:{w_st:.1f}%"></span></div></div>
                                <div class="rank-src">
                                    <span><i class="dot s-ml"></i>ML {ml:.1f}</span>
                                    <span><i class="dot s-ng"></i>Ngành {ng:.1f}</span>
                                    <span><i class="dot s-st"></i>Sở thích {st_:.1f}</span>
                                </div>
                            </div>
                            <div class="rank-pct">{pct:.1f}%</div>
                        </div>
                        """
                    st.markdown(rows_html, unsafe_allow_html=True)
                    note(
                        f"Lần này: <b>{w_ml * 100:.0f}%</b> mô hình ML "
                        f"(độ tự tin {do_tin_cay * 100:.0f}%) + <b>{w_nganh * 100:.0f}%</b> ngành học + "
                        f"<b>{w_st * 100:.0f}%</b> lĩnh vực quan tâm. Mô hình ML được tối đa 50% "
                        "khi nó tự tin; nếu năng lực của bạn chưa có điểm nổi bật, phần ML sẽ nhỏ lại. "
                        "Các số ML / Ngành / Sở thích là điểm mỗi nguồn đóng góp."
                    )

            with st.container(border=True):
                panel_header("🛠️", "Hồ sơ năng lực", "Điểm tự đánh giá (thang 10)")
                mini_bars(
                    [(nang_luc[f], v) for f, v in diem_nang_luc.items()]
                    + list(diem_ky_nang_khac.items())
                )

        with right:
            with st.container(border=True):
                panel_header("📋", "Thông tin sinh viên")
                st.metric("Ngành học", nganh)
                st.metric("GPA", f"{gpa:.2f} / 4.00")
                diem_tb = sum(diem_mon.values()) / len(diem_mon)
                st.metric("Điểm TB môn chuyên ngành", f"{diem_tb:.2f} / 10")
                st.markdown("**Lĩnh vực quan tâm**")
                st.markdown(
                    "".join(f'<span class="chip">{s}</span>' for s in so_thich),
                    unsafe_allow_html=True
                )

            with st.container(border=True):
                panel_header("🧠", "Đặc điểm cá nhân", "Điểm tự đánh giá (thang 10)")
                mini_bars([(tinh_cach[f], v) for f, v in diem_tinh_cach.items()])

        with st.expander("📄 Xem chi tiết toàn bộ thông tin đã nhập"):
            info = {
                "GPA": gpa,
                **diem_mon,
                **diem_ky_nang_khac,
                "Sở thích": ", ".join(so_thich)
            }

            bang = pd.DataFrame(
                info.items(),
                columns=["Thông tin", "Giá trị"]
            )

            # Tranh loi PyArrow voi du lieu hon hop
            bang["Giá trị"] = bang["Giá trị"].astype(str)

            st.dataframe(
                bang,
                width="stretch",
                hide_index=True
            )

        note(
            "⚠️ Kết quả chỉ mang tính tham khảo. Điểm phù hợp không phải xác suất chắc chắn "
            "sinh viên phù hợp với nghề. Phần ngành học và sở thích dựa trên luật gán thủ công, "
            "không do mô hình học từ dữ liệu. Việc quy đổi điểm tự đánh giá sang thang dữ liệu "
            "huấn luyện chưa được kiểm chứng. GPA, điểm môn học và kỹ năng bổ sung "
            "chưa tham gia dự đoán.",
            warn=True
        )

    except Exception as e:
        st.error("Có lỗi khi dự đoán nghề nghiệp.")
        st.exception(e)


# ==========================================
# 8. FOOTER
# ==========================================

st.markdown(
    '<div class="footer">© CareerPath IT · Hệ thống hỗ trợ định hướng nghề nghiệp '
    'cho sinh viên bằng Machine Learning</div>',
    unsafe_allow_html=True
)
