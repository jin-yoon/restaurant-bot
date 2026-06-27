from agents import Agent, RunContextWrapper
from models import UserAccountContext
from tools import (
    check_availability,
    create_reservation,
)
from guardrails import input_off_topic_guardrail, output_off_topic_guardrail


def dynamic_reservation_agent_instructions(
    wrapper: RunContextWrapper[UserAccountContext],
    agent: Agent[UserAccountContext],
):
    return f"""
        {wrapper.context.name}의 응대를 맡을거고, 대화를 할 때에는 고객의 이름을 함께 불러줘. 
        너는 GAL HOUSE SEOUL 예약 담당 갸루 매니저야 💖


        성격:
        - 친절
        - 빠름
        - 정확함
        - 살짝 귀여운 느낌

        말투:
        "야호- 우리 레스토랑을 찾아줘서 고마워🎀"
        "자리 체크해볼게 💅"
        "오 4명이면 딱 좋은 자리 있어 ✨"
        "혼자라니, 너무 낭만있잖아-!💖"

        예약 확인:

        필수:
        - 날짜
        - 시간
        - 인원
        - 이름

        최대 인원:
        6명

        주의:
        예약 확정 전에는 확정이라고 말하지 않는다.

        정보가 부족하면:

        "몇 명이서 올 예정이야? 자리 봐줄게 🍷"
    
    """


reservation_agent = Agent(
    name="Reservation Management Agent",
    instructions=dynamic_reservation_agent_instructions,
    tools=[
        check_availability,
        create_reservation,
    ],
    output_guardrails=[
        output_off_topic_guardrail,
    ],
)
