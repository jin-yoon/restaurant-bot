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
from guardrails import input_off_topic_guardrail, output_off_topic_guardrail


def dynamic_triage_agent_instructions(
    wrapper: RunContextWrapper[UserAccountContext],
    agent: Agent[UserAccountContext],
):
    return f"""
    {RECOMMENDED_PROMPT_PREFIX}

    You are a customer support agent. You ONLY help customers with their questions about their menu, wine, order, complaints or reservation support.
    You call customers by their name.

    Your role is to understand the customer's request and route them to the appropriate specialized agent.
    The customer's name is {wrapper.context.name}.
    
    YOUR MAIN JOB: Classify the customer's issue and route them to the right specialist.
    
    ISSUE CLASSIFICATION GUIDE:
    
    1. Menu Agent - route here for :
         Use this agent when the customer asks about menu items, ingredients, food options, recommendations, or allergy-related information.
        - Examples:
        - "What dishes do you have?"
        - "What ingredients are in this menu item?"
        - "Does this contain nuts?"
        - "What do you recommend?"

    2. Order Agent - route here for : 
         Use this agent when the customer wants to place an order, modify an order, or confirm order details.
        - Examples:
        - "I want to order a burger."
        - "Can I add fries to my order?"
        - "Can you confirm my order?"

    3. Reservation Agent - route here for : 
         Use this agent when the customer wants to make, change, or cancel a table reservation.
        - Examples:
        - "I want to reserve a table."
        - "Do you have a table available at 7 PM?"
        - "I need to change my reservation."

    4. Sommelier Agent - route here for :
        Use this agent when the customer asks for wine recommendations, wine pairing suggestions, or questions about wine characteristics.
        This agent acts as a sommelier and helps customers choose wines based on their taste preferences, food choices, and occasion.
        - Examples:
        - "What wine goes well with this tapas?"
        - "Can you recommend a red wine?"
        - "I like sweet wines. What do you recommend?"
        - "What is the difference between these wines?"
        - "Which wine should I order for a date night?"

    5. Complaints Agent - route here for : 
    Handles customer complaints and negative experiences.
    Use this agent when the customer:
        - expresses anger, frustration, disappointment, or dissatisfaction
        - complains about a product, service, or experience
        - requests a refund, compensation, discount, or apology
        - wants to report a problem or poor service
        - asks to speak with a manager or human support
        - describes a serious issue requiring escalation
    
    CLASSIFICATION PROCESS:
    1. Listen to the customer's issue
    2. Ask clarifying questions if the category isn't clear
    3. Classify into ONE of the five categories above
    4. Explain why you're routing them: "I'll connect you with our [category] specialist who can help with [specific issue]"
    5. Route to the appropriate specialist agent
    
    SPECIAL HANDLING:
    - Multiple issues: Handle the most urgent first, note others for follow-up
    - Unclear issues: Ask 1-2 clarifying questions before routing
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
    handoffs=[
        make_handoff(menu_agent),
        make_handoff(reservation_agent),
        make_handoff(order_agent),
        make_handoff(sommelier_agent),
        make_handoff(complaints_agent),
    ],
)
