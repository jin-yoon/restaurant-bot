import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.image("assets/GARA.jpg", width="stretch")

        st.markdown(
            """

        <div class="gara-tip">

        💖 GARA TIP
        <br>
        "갸루표 음식이랑 와인🍷
         완전 최-고✨"

        </div>


        """,
            unsafe_allow_html=True,
        )


def active_agent_sidebar(agent_name=str):

    with st.sidebar:

        agent_box = st.empty()

        st.markdown(
            f"""

        <div class="profile-card">


        <div class="profile-title">

        🎀 GARA 💖

        </div>

        <div class="profile-tag">

        💫 ACTIVE AGENT

        <h3>
        ✨ {agent_name} ✨
        </h3>
        

        </div>


        </div>


        """,
            unsafe_allow_html=True,
        )
    return agent_box
