import dotenv
import asyncio
import streamlit as st
from agents import (
    Runner,
    SQLiteSession,
    InputGuardrailTripwireTriggered,
    OutputGuardrailTripwireTriggered,
)
from openai import OpenAI
from models import UserAccountContext
from all_agents.triage_agent import triage_agent
from UI.style import apply_gyaru_style
from UI.sidebar import render_sidebar, active_agent_sidebar
import uuid

if "session" not in st.session_state:

    st.session_state["session"] = SQLiteSession(session_id=f"restaurant_{uuid.uuid4()}")

# CSS 적용

apply_gyaru_style()


# Header
st.markdown(
    """
<div class="blog-card">

<div class="brand">

💖 GAL HOUSE SEOUL

</div>


<div class="subtitle">

야-호 어서와✨ GARA가 취향 맞춰줄게 💅

</div>


</div>

""",
    unsafe_allow_html=True,
)


dotenv.load_dotenv()  # api key 자동으로 못 읽어올 때

client = OpenAI()

# 지금은 가상의 데이터 Input하지만, 실제로는 db에서 가져와서 매핑
user_account_ctx = UserAccountContext(
    name="칭구",
)

# if "session" not in st.session_state:
#     st.session_state["session"] = SQLiteSession(
#         "chat-history",
#         "restaurant-bot-memory.db",
#     )

session = st.session_state["session"]

st.set_page_config(page_title="GAL HOUSE SEOUL", page_icon="💖", layout="wide")

with st.sidebar:
    reset = st.button("대화 초기화")
    if reset:
        asyncio.run(session.clear_session())


if "agent" not in st.session_state:
    st.session_state["agent"] = triage_agent
    with st.chat_message("assistant", avatar="💖"):
        st.write("하잉-✨ 이름이 뭐야?")
# Sidebar
render_sidebar()

agent_placeholder = active_agent_sidebar(st.session_state["agent"].name)


async def paint_history():
    messages = await session.get_items()
    for message in messages:
        if "role" in message:
            with st.chat_message(message["role"]):
                if message["role"] == "user":
                    st.write(message["content"])
                else:
                    if message["type"] == "message":
                        st.write(message["content"][0]["text"])


asyncio.run(paint_history())


async def run_agent(message):

    with st.chat_message("assistant", avatar="💖"):
        text_placeholder = st.empty()
        response = ""

        st.session_state["text_placeholder"] = text_placeholder

        try:

            stream = Runner.run_streamed(
                st.session_state["agent"],
                message,
                session=session,
                context=user_account_ctx,
            )
            async for event in stream.stream_events():
                if event.type == "raw_response_event":
                    if event.data.type == "response.output_text.delta":
                        response += event.data.delta
                        text_placeholder.write(response)

                elif event.type == "agent_updated_stream_event":

                    if st.session_state["agent"].name != event.new_agent.name:

                        st.info(f"{event.new_agent.name}로 연결해줄게✌️")

                        st.session_state["agent"] = event.new_agent

                        agent_placeholder.markdown(
                            f"""

                            <div class="gara-tip">
                            <h3>
                            ✨ {event.new_agent.name}로 전환 ✨
                            </h3>

                            </div>

                            """,
                            unsafe_allow_html=True,
                        )

                        text_placeholder = st.empty()

                        response = ""

        except InputGuardrailTripwireTriggered as triggered:
            guardrail_result = triggered.guardrail_result.output
            st.write(
                "아아- 싫다😫 우리 레스토랑 관련된 이야기만 해줘💝! 레스토랑 분위기/메뉴/주문/예약/불만접수 말만해!"
            )

        except OutputGuardrailTripwireTriggered as triggered:
            guardrail_result = triggered.guardrail_result.output
            st.write(
                "미안🫢- 그건 내가 대답해 줄 수 없는데~. 우리 귀여운 레스토랑 이야기만 하자❤️"
            )


message = st.chat_input(
    "🎀레스토랑 : GAL HOUSE SEOUL🎀 - 어서와✌️ 궁금한게 뭐야?",
)

if message:
    with st.chat_message("human", avatar="😶"):
        st.write(message)
    asyncio.run(run_agent(message))
