import streamlit as st


def apply_gyaru_style():

    gyaru_css = """

    <style>


    /* =========================
       FONT & GLOBAL BACKGROUND
    ========================= */

    @import url(
    'https://fonts.googleapis.com/css2?family=Jua&display=swap'
    );


    /* [강력 수정] html부터 실제 콘텐츠 영역, 하단 고정 컨테이너까지 싹 다 배경을 투명화하거나 그라데이션으로 덮어버림 */
    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .main {

        background:
        linear-gradient(
            135deg,
            #FF75B5 0%,
            #FFB7D6 45%,
            #D8B4FF 100%
        ) !important;

        font-family:
        'Jua',
        sans-serif !important;

        color:
        #4A2140;

    }

    /* 상단 Deploy 메뉴 영역 투명화 */
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }




    /* =========================
       SIDEBAR
    ========================= */


    [data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #FF66B2,
            #E0AAFF
        ) !important;

        border-right:
        3px solid white;

    }


    [data-testid="stSidebar"] * {

        color:
        inherit;

    }




    /* =========================
       BLOG CARD
    ========================= */


    .blog-card {

        background:
        rgba(
            255,
            255,
            255,
            0.9
        );

        border-radius:
        25px;

        padding:
        25px;

        border:
        3px solid
        #FF3399;

        box-shadow:
        0px 10px 25px
        rgba(
            255,
            0,
            127,
            0.15
        );

        margin-bottom: 25px;

    }





    /* =========================
       PROFILE CARD
    ========================= */


    .profile-card {

        background:
        rgba(
            255,
            255,
            255,
            0.25
        );

        border-radius:
        25px;

        padding:
        20px;

        text-align:
        center;

        border:
        2px solid white;

    }




    .profile-title {

        font-size:
        28px;

        font-weight:
        900;

        color:
        white;

    }





    .profile-tag {

        font-size:
        15px;

        color:
        #FFF0FA;

    }






    /* =========================
       BRAND TITLE
    ========================= */


    .brand {

        text-align:center;

        font-size:
        45px;

        font-weight:
        900;

        color:
        #FF007F;

        text-shadow:
        2px 2px white,
        0 0 15px #FF99CC;

    }




    .subtitle {

        text-align:center;

        font-size:
        18px;

        color:
        #7A3560;

    }






    /* =========================
       GARA TIP
    ========================= */


    .gara-tip {

        background:
        #FFF0F5;

        border-left:
        8px solid
        #FF1493;

        padding:
        18px;

        border-radius:
        15px;

        margin:
        15px 0;

        font-weight:
        bold;

        color:
        #4A2140;

    }






    /* =========================
       HIGHLIGHT
    ========================= */


    .gyaru-highlight {

        background:
        #FFFF00;

        color:
        #FF007F;

        font-weight:
        bold;

        padding:
        3px 7px;

        border-radius:
        8px;

    }





    /* =========================
       CHAT (모드 무관 강제 고정)
    ========================= */


    [data-testid="stChatMessage"] {

        background-color:
        rgba(
            255,
            255,
            255,
            0.85
        ) !important;

        border-radius:
        25px !important;

        border:
        2px solid
        #FFB7D6 !important;

        padding:
        15px !important;

    }


    [data-testid="stChatMessageAvatar"] {
        background-color: #4A2140 !important;
        color: white !important;
        border-radius: 50% !important;
    }


    [data-testid="stChatMessage"] p, 
    [data-testid="stChatMessage"] span, 
    [data-testid="stChatMessage"] div {
        color: #4A2140 !important;
    }



/* =========================
       CHAT INPUT FIELD & BOTTOM FIX (초강력 버전)
    ========================= */

    /* 1. 하단 전체를 감싸는 고정 컨테이너와 블러 영역을 투명화하여 배경 그라데이션이 비치게 만듦 */
    [data-testid="stChatInputBottomBlur"],
    div[data-testid="stChatInputContainer"],
    div[class*="stChatInputBottom"],
    form[data-testid="stChatInputForm"] {
        background-color: transparent !important;
        background: transparent !important;
        box-shadow: none !important;
        border: none !important;
    }

    /* 2. 다크모드가 하단 레이아웃에 강제로 집어넣는 검은색 그라데이션(빛 가림막) 제거 */
    div[class*="stChatInputBottom"]::before,
    div[class*="stChatInputBottom"]::after {
        display: none !important;
        background: transparent !important;
    }

    /* 3. 입력창 본체 디자인 (여기는 하얀색 박스로 이쁘게 유지!) */
    [data-testid="stChatInput"] {
        background: white !important;
        border-radius: 15px !important;
        border: 3px solid #FF66B2 !important;
        box-shadow: 0px 4px 10px rgba(255, 102, 178, 0.3) !important;
    }

    /* 4. 입력창 내부 실제 텍스트창 스타일 고정 */
    [data-testid="stChatInput"] textarea {
        color: #4A2140 !important;
        background-color: transparent !important;
    }
    
    [data-testid="stChatInput"] textarea::placeholder {
        color: #FF99CC !important;
    }





    /* =========================
       BUTTON
    ========================= */


    .stButton button {

        background:
        linear-gradient(
            90deg,
            #FF3399,
            #CC66FF
        );

        color:white;

        border:none;

        border-radius:
        25px;

        font-weight:
        bold;

    }





    </style>


    """

    st.markdown(gyaru_css, unsafe_allow_html=True)
