import json
import streamlit as st

from utils.i18n import pick_language, lang
from utils.ui import (
    style,
    html,
    tr,
    get_doctor_data_uri,
    get_eiu_logo_data_uri,
    get_eiu_logo_bilingual_svg,
    EIU_LOGO_TRANSPARENT_SVG,
    DOCTOR_SVG,
    HEART_PULSE_SVG,
    SHIELD_PLUS_SVG,
)

if "lang" not in st.session_state:
    st.session_state["lang"] = "vi"
if "app_mode" not in st.session_state:
    st.session_state["app_mode"] = "user"

st.set_page_config(
    page_title="GlucoGuide",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

style()


def home_view():
    """Home Page matching Image 1 design with doctor photo & 3-step How It Works."""
    doctor_uri = get_doctor_data_uri()
    cur_l = st.session_state.get("lang", "vi")
    speech_script = tr(
        "Xin chào! Hãy cùng tôi dành 2 phút đánh giá nguy cơ để chủ động bảo vệ sức khỏe trước bệnh tiểu đường nhé!",
        "Hello! Spend 2 minutes with me to assess your risk and proactively protect your health against diabetes!"
    )
    bubble_title = tr("Bác sĩ Trợ lý GlucoGuide", "GlucoGuide Doctor Assistant")
    listen_lbl = tr("Nghe nói", "Listen")
    stop_lbl = tr("Dừng", "Stop")
    script_json = json.dumps(speech_script)

    doctor_img_tag = (
        f'<img src="{doctor_uri}" alt="Doctor" class="hero-doctor-img"/>'
        if doctor_uri
        else f'<div style="padding-bottom:1.2rem;">{DOCTOR_SVG}</div>'
    )

    doctor_html = f'''
    <div class="hero-doctor-container">
        <div class="doctor-speech-bubble" id="heroDoctorBubble" onclick="speakDoctorBubble()" title="{tr("Bấm để nghe bác sĩ nói", "Click to hear doctor speak")}">
            <div class="bubble-header">
                <span class="bubble-title">🩺 {bubble_title}</span>
                <span class="bubble-sound-btn" id="bubbleSoundIcon">🔊 {listen_lbl}</span>
            </div>
            <p class="bubble-text">“{speech_script}”</p>
        </div>
        <div class="hero-doctor-wrap">
            {doctor_img_tag}
        </div>
    </div>
    <script>
    function speakDoctorBubble() {{
        if (!('speechSynthesis' in window)) {{
            alert('Trình duyệt không hỗ trợ Web Speech API.');
            return;
        }}
        const icon = document.getElementById('bubbleSoundIcon');
        if (window.speechSynthesis.speaking) {{
            window.speechSynthesis.cancel();
            if (icon) icon.innerText = '🔊 {listen_lbl}';
            return;
        }}
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance({script_json});
        utterance.lang = '{cur_l}' === 'vi' ? 'vi-VN' : 'en-US';
        utterance.pitch = 1.18; // Female voice
        utterance.rate = 0.95;

        const voices = window.speechSynthesis.getVoices();
        let femaleVoice = null;
        if ('{cur_l}' === 'vi') {{
            femaleVoice = voices.find(v => v.lang.startsWith('vi') && 
                (v.name.toLowerCase().includes('hoa') || 
                 v.name.toLowerCase().includes('my') || 
                 v.name.toLowerCase().includes('linh') || 
                 v.name.toLowerCase().includes('female') || 
                 v.name.toLowerCase().includes('nu')));
            if (!femaleVoice) femaleVoice = voices.find(v => v.lang.startsWith('vi'));
        }} else {{
            femaleVoice = voices.find(v => v.lang.startsWith('en') && 
                (v.name.toLowerCase().includes('female') || 
                 v.name.toLowerCase().includes('zira') || 
                 v.name.toLowerCase().includes('jenny') || 
                 v.name.toLowerCase().includes('samantha')));
            if (!femaleVoice) femaleVoice = voices.find(v => v.lang.startsWith('en'));
        }}
        if (femaleVoice) utterance.voice = femaleVoice;

        if (icon) icon.innerText = '⏹️ {stop_lbl}';
        utterance.onend = () => {{ if (icon) icon.innerText = '🔊 {listen_lbl}'; }};
        utterance.onerror = () => {{ if (icon) icon.innerText = '🔊 {listen_lbl}'; }};

        window.speechSynthesis.speak(utterance);
    }}
    </script>
    '''

    with st.container(key="home_hero"):
        c_hero_l, c_hero_r = st.columns([1.25, 0.95], vertical_alignment="center", gap="large")

        with c_hero_l:
            html(f"""
            <h1 class="brand-title">GlucoGuide</h1>
            <div class="brand-subtitle">
                {tr("Thấu hiểu Nguy cơ. Chủ động Bảo vệ Sức khỏe.", "Know Your Risk. Take Control of Your Health.")}
            </div>
            <div class="brand-lead">
                {tr(
                    "Công cụ sàng lọc nguy cơ tiểu đường thông minh, giúp bạn hiểu rõ các yếu tố sức khỏe và đưa ra quyết định chăm sóc sức khỏe chủ động.",
                    "A smart diabetes risk screening tool designed to help you understand your health factors and make proactive health decisions."
                )}
            </div>
            """)

            if st.button(tr("Bắt đầu Đánh giá Nguy cơ", "Start Risk Assessment"), type="primary"):
                st.session_state["assess_step"] = 1
                st.switch_page("pages/1_Risk_Assessment.py")

        with c_hero_r:
            html(doctor_html)

    st.write("")

    # How It Works 3-Step Banner (matching Image 1)
    with st.container(key="how_card"):
        html(f"""
        <div class="how-layout">
            <div class="how-shield-box">{SHIELD_PLUS_SVG}</div>
            <div>
                <div class="how-title">{tr("Quy trình Hoạt động?", "How It Works?")}</div>
                <div class="how-steps">
                    <div class="how-step-box">
                        <div class="flow-num-badge">1</div>
                        <div class="how-step-txt">{tr("Trả lời vài câu hỏi đơn giản", "Answer a few simple questions")}</div>
                    </div>
                    <div class="how-arrow"><span class="flow-ch-1">›</span><span class="flow-ch-2">›</span><span class="flow-ch-3">›</span></div>
                    <div class="how-step-box">
                        <div class="flow-num-badge">2</div>
                        <div class="how-step-txt">{tr("Nhận kết quả nguy cơ của bạn", "Get your risk result")}</div>
                    </div>
                    <div class="how-arrow"><span class="flow-ch-1">›</span><span class="flow-ch-2">›</span><span class="flow-ch-3">›</span></div>
                    <div class="how-step-box">
                        <div class="flow-num-badge">3</div>
                        <div class="how-step-txt">{tr("Tìm hiểu thêm cùng Trợ lý AI", "Learn more with our AI Assistant")}</div>
                    </div>
                </div>
            </div>
        </div>
        """)


# Determine Mode before building navigation
mode = st.session_state.get("app_mode", "user")

home_title = tr("Trang chủ", "Home")
assess_title = tr("Khảo sát Nguy cơ", "Risk Assessment")
results_title = tr("Kết quả của tôi", "My Results")
about_title = tr("Về GlucoGuide", "About GlucoGuide")
teacher_title = tr("Tổng quan Dự án", "Project Overview")

home_page = st.Page(
    home_view,
    title=home_title,
    default=(mode == "user"),
)
assess_page = st.Page(
    "pages/1_Risk_Assessment.py",
    title=assess_title,
)
results_page = st.Page(
    "pages/2_My_Results.py",
    title=results_title,
)
about_page = st.Page(
    "pages/3_About_GlucoGuide.py",
    title=about_title,
)
teacher_page = st.Page(
    "pages/4_Teacher_Overview.py",
    title=teacher_title,
    default=(mode == "teacher"),
)

if mode == "user":
    nav_items = [
        ("nav_home", home_title, home_page),
        ("nav_assess", assess_title, assess_page),
        ("nav_results", results_title, results_page),
        ("nav_about", about_title, about_page),
    ]
else:
    nav_items = [
        ("nav_teacher", teacher_title, teacher_page),
    ]

pages = [p for _, _, p in nav_items]
nav = st.navigation(pages, position="hidden")

# ============ CUSTOM SIDEBAR (LOGO AT VERY TOP) ============
cur_lang = st.session_state.get("lang", "vi")
logo_markup = get_eiu_logo_bilingual_svg(cur_lang)

with st.sidebar:
    st.markdown(
        f'''
        <div class="sb-logo-wrap">
            {logo_markup}
        </div>
        <div class="sb-brand-row">
            {HEART_PULSE_SVG}
            <div class="sb-brand-name">GlucoGuide</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    for slug, label, page_obj in nav_items:
        state_cls = "active" if page_obj == nav else "idle"
        with st.container(key=f"{slug}_{state_cls}"):
            st.page_link(page_obj, label=label, use_container_width=True)

    st.markdown('<div style="height:0.5rem;"></div>', unsafe_allow_html=True)
    pick_language()

    mode_lbl = tr("CHẾ ĐỘ", "MODE")
    st.markdown(
        f'<div class="sb-section-lbl">{mode_lbl}</div>',
        unsafe_allow_html=True,
    )
    with st.container(key="sb_mode_seg"):
        cur_mode = st.session_state.get("app_mode", "user")
        selected_mode = st.radio(
            "sb_mode_select_hidden",
            options=["user", "teacher"],
            format_func=lambda val: tr(
                "Người dùng" if val == "user" else "Giảng viên",
                "User" if val == "user" else "Teacher",
            ),
            index=0 if cur_mode == "user" else 1,
            horizontal=True,
            key="sb_mode_radio",
            label_visibility="collapsed",
        )
        if selected_mode != cur_mode:
            st.session_state["app_mode"] = selected_mode
            st.rerun()

    st.markdown(
        f"""
        <div class="sb-note">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#93C5FD" stroke-width="2" style="flex:0 0 16px;margin-top:2px">
                <circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>
            </svg>
            <span>{tr(
                "Công cụ phục vụ mục đích giáo dục, không dùng trong chẩn đoán lâm sàng.",
                "Educational tool, not for clinical diagnosis."
            )}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

nav.run()
