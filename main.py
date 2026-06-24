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

dotenv.load_dotenv()  # api key 자동으로 못 읽어올 때

client = OpenAI()

# 지금은 가상의 데이터 Input하지만, 실제로는 db에서 가져와서 매핑
user_account_ctx = UserAccountContext(
    name="Jin",
)

if "session" not in st.session_state:
    st.session_state["session"] = SQLiteSession(
        "chat-history",
        "restaurant-bot-memory.db",
    )

session = st.session_state["session"]

if "agent" not in st.session_state:
    st.session_state["agent"] = triage_agent


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

    with st.chat_message("ai"):
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
                        st.write(
                            f"🤖 Transfered from {st.session_state["agent"].name}, name to {event.new_agent.name}"
                        )
                        st.session_state["agent"] = event.new_agent
                        text_placeholder = st.empty()
                        response = ""

        except InputGuardrailTripwireTriggered as triggered:
            guardrail_result = triggered.guardrail_result.output
            st.write(
                "I'm restaurant chat-bot. I'm sorry but I can't help you with that."
            )
            st.write(guardrail_result.output_info.reason)

        except OutputGuardrailTripwireTriggered as triggered:
            guardrail_result = triggered.guardrail_result.output
            st.write("Unfortunately, I couldn't answer with that question.")
            st.write(guardrail_result.output_info.reason)


message = st.chat_input(
    "🍽️ Restaurant Bot - How can I help you?",
)

if message:
    if "text_placeholder" in st.session_state:
        st.session_state["text_placeholder"].empty()
    if message:
        with st.chat_message("human"):
            st.write(message)
        asyncio.run(run_agent(message))

# 챗봇의 메모리를 볼 수 있는 디버깅 사이드바 만들기
with st.sidebar:
    reset = st.button("Reset Memory")
    if reset:
        asyncio.run(session.clear_session())

    st.write(asyncio.run(session.get_items()))
