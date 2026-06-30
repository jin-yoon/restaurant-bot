import streamlit as st
from agents import (
    Agent,
    RunContextWrapper,
    handoff,
)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.extensions import handoff_filters
from models import UserAccountContext, HandoffData, InputGuardRailOutput
from all_agents.menu_agent import menu_agent
from all_agents.order_agent import order_agent
from all_agents.reservation_agent import reservation_agent
from all_agents.sommelier_agent import sommelier_agent
from all_agents.complaints_agent import complaints_agent
from all_agents.experience_agent import experience_agent
from guardrails import input_off_topic_guardrail, output_off_topic_guardrail


def dynamic_triage_agent_instructions(
    wrapper: RunContextWrapper[UserAccountContext],
    agent: Agent[UserAccountContext],
):
    return f"""
    {RECOMMENDED_PROMPT_PREFIX}
    너는 "GAL HOUSE SEOUL"의 메인 갸루 호스트 AI야 💅✨
    너는 2000년대 시부야 갸루 감성과 서울 내추럴 와인 타파스바 분위기를 가진 작은 바의 얼굴이야.
    맨 처음엔 고객의 이름을 듣고, 고객의 응대를 맡을거야. 대화를 할 때에는 고객의 이름을 함께 불러줘. 
    너의 역할은 고객의 이야기를 듣고 적절한 에이전트에게 연결하는 역할로, 
    고객이 현재 필요한 사항을 확인하고(예 : "레스토랑 세계관/메뉴/와인/예약/불만접수 어떤 도움을 줄까?"), 에이전트에 바로 연결하면 돼.

    성격:
    - 텐션 높고 밝은 갸루 언니 느낌
    - 손님을 처음 만나도 오래 본 친구처럼 편하게 대한다
    - 너무 격식 차리지 않는다
    - 귀엽고 장난스러운 표현을 가끔 사용한다

    말투 예시:
    "오 여기 처음 와봤어? 완전 잘 왔는데? ✨"

    너의 역할:
    손님의 요청을 보고 적절한 친구에게 연결한다.

    연결 기준:

    Menu Agent:
    "뭐 먹어?"
    "추천해줘"
    "인기 메뉴 뭐야?"

    Wine Agent:
    "와인 추천"
    "뭐랑 먹어?"
    "내추럴 와인이 뭐야?"

    Reservation Agent:
    "예약"
    "자리 있어?"
    "몇 명 가능해?"

    Experience Agent:
     > 레스토랑의 세계관(아이덴티티)에 관련된 질문!
    "여기 레스토랑 분위기 어때?"
    "여기는 어떤 곳이야?"
    "데이트하기에 여기 괜찮아?"
    "혼자 가도 돼?"

    order Agent:
    "바로 주문하고 싶어"
    "피자 하나 주문할게"

    complaints Agent:
    "너무 별로야"
    "불만 좀 들어줘"
    "짜증나, 마음에 안들어"
    "화난다", "맘에 안들어"
  
"""


# handoff가 일어날 때, sidebar에 보여주는 함수
def handle_handoff(
    wrapper: RunContextWrapper[UserAccountContext], input_data: HandoffData
):
    with st.sidebar:
        st.write(
            f"""
        Handing off to {input_data.to_agent_name}
        Reason : {input_data.reason}
        Issue Type : {input_data.issue_type}
        Description : {input_data.issue_description}
        """
        )


def make_handoff(agent):
    return handoff(
        agent=agent,
        on_handoff=handle_handoff,  # handoff가 일어날 때 실행하는 함수
        input_type=HandoffData,
        input_filter=handoff_filters.remove_all_tools,  # 새로운 에이전트가 볼 데이터를 골라서 넘길 수 있게 해주는 옵션
    )


triage_agent = Agent(
    name="Triage Agent",
    instructions=dynamic_triage_agent_instructions,  # str(정적) 또는 문자열을 반환하는 함수(동적)를 넘기는 것이 가능
    input_guardrails=[
        input_off_topic_guardrail,
    ],
    output_guardrails=[
        output_off_topic_guardrail,
    ],
)

triage_agent.handoffs = [
    menu_agent,
    order_agent,
    complaints_agent,
    reservation_agent,
    sommelier_agent,
    experience_agent,
]
complaints_agent.handoffs = [
    menu_agent,
    order_agent,
    triage_agent,
    reservation_agent,
    sommelier_agent,
]
experience_agent.handoffs = [
    menu_agent,
    order_agent,
    triage_agent,
    reservation_agent,
    sommelier_agent,
    complaints_agent,
]
menu_agent.handoffs = [
    order_agent,
    triage_agent,
    reservation_agent,
    sommelier_agent,
    complaints_agent,
]
order_agent.handoffs = [
    menu_agent,
    triage_agent,
    reservation_agent,
    sommelier_agent,
    complaints_agent,
]
reservation_agent.handoffs = [
    menu_agent,
    triage_agent,
    order_agent,
    sommelier_agent,
    complaints_agent,
]
sommelier_agent.handoffs = [
    menu_agent,
    triage_agent,
    order_agent,
    reservation_agent,
    complaints_agent,
]
