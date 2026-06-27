from agents import function_tool
import random

MENU_DATA = [
    {
        "name": "핑크 김치 크림 브루스케타 💗",
        "category": "starter",
        "price": 12000,
        "description": "바삭한 바게트 위에 부드러운 크림치즈와 한국식 김치 감칠맛을 더한 시그니처 타파스",
        "taste": ["creamy", "slightly_spicy"],
        "ingredients": ["bread", "cream cheese", "kimchi"],
        "gyaru_comment": "첫 방문이면 이거 추천 💅 한국 느낌도 있고 가볍게 시작하기 좋아",
    },
    {
        "name": "명란 감자 구름 타파스 ☁️",
        "category": "starter",
        "price": 13000,
        "description": "부드러운 감자와 짭짤한 명란, 은은한 버터 풍미가 어우러진 메뉴",
        "taste": ["savory", "rich"],
        "ingredients": ["potato", "pollock roe", "butter"],
        "gyaru_comment": "은근 계속 손 가는 메뉴야 ㅎㅎ",
    },
    {
        "name": "서울 불고기 미니 타코 🌮",
        "category": "main",
        "price": 16000,
        "description": "달콤한 한국식 불고기와 타코 쉘을 조합한 퓨전 메뉴",
        "taste": ["sweet", "savory"],
        "ingredients": ["beef", "soy sauce", "taco shell"],
        "gyaru_comment": "익숙한데 살짝 새로운 느낌이라 재밌어 ✨",
    },
    {
        "name": "갸루 치킨 바이트 🍗",
        "category": "popular",
        "price": 15000,
        "description": "바삭한 닭강정 스타일 치킨과 상큼한 소스 조합",
        "taste": ["crispy", "sweet_spicy"],
        "ingredients": ["chicken", "flour"],
        "gyaru_comment": "우리 인기 메뉴야. 실패 없는 픽 💖",
    },
    {
        "name": "된장 버터 쉬림프 🦐",
        "category": "main",
        "price": 18000,
        "description": "된장의 깊은 감칠맛과 버터 풍미를 살린 새우 요리",
        "taste": ["rich", "umami"],
        "ingredients": ["shrimp", "butter", "miso"],
        "gyaru_comment": "고소한 거 좋아하면 이거 진짜 좋아할 듯 🍤",
    },
    {
        "name": "시부야 고추장 라구 파스타 ❤️",
        "category": "main",
        "price": 19000,
        "description": "토마토 라구 소스에 한국식 고추장 풍미를 더한 매콤한 파스타",
        "taste": ["spicy", "deep"],
        "ingredients": ["pasta", "tomato", "gochujang"],
        "gyaru_comment": "매콤한 거 좋아하면 이거 찐이야 🔥",
    },
]

WINE_DATA = [
    {
        "name": "Pink Tokyo Sparkle ✨",
        "type": "Sparkling Rosé",
        "price": 14000,
        "taste": "상큼하고 가벼움",
        "level": "beginner",
        "pairing": ["명란 감자 타파스", "김치 크림 브루스케타"],
        "gyaru_comment": "입문용으로 완전 좋아 💗 탄산감 있어서 분위기 내기 딱!",
    },
    {
        "name": "Shibuya Cloud White ☁️",
        "type": "Natural White",
        "price": 16000,
        "taste": "과일향, 깔끔함",
        "level": "beginner",
        "pairing": ["된장 버터 쉬림프", "해산물 메뉴"],
        "gyaru_comment": "화이트 처음이면 이거 추천! 부담 없이 넘어가 ✨",
    },
    {
        "name": "Seoul Night Red 🌙",
        "type": "Natural Red",
        "price": 17000,
        "taste": "부드럽고 과일 느낌",
        "level": "intermediate",
        "pairing": ["불고기 미니 타코", "라구 파스타"],
        "gyaru_comment": "밤 분위기랑 잘 어울리는 내 최애 픽 🍷",
    },
    {
        "name": "Black Glitter Funky 🍒",
        "type": "Orange Wine",
        "price": 19000,
        "taste": "개성 있고 독특함",
        "level": "expert",
        "pairing": ["치즈", "강한 맛 음식"],
        "gyaru_comment": "취향 타는데 좋아하는 사람은 완전 빠져 ㅎㅎ",
    },
]


@function_tool
def search_menu(category: str) -> str:
    f"""
    Search restaurant menu.
    {MENU_DATA}

    Args:
        category:
        - popular
        - starter
        - main
    """

    menus = [menu for menu in MENU_DATA if menu["category"] == category]

    if not menus:
        return "뿌엥ㅠ 메뉴를 못 찾았어"

    result = "✨ GAL HOUSE SEOUL MENU ✨\n\n"

    for menu in menus:

        result += (
            f"🍽 {menu['name']}\n"
            f"💰 {menu['price']}원\n"
            f"📝 {menu['description']}\n"
            f"💖 GARA Pick: {menu['gyaru_comment']}\n\n"
        )

    return result


@function_tool
def check_food_allergy(menu_item: str, allergy: str) -> str:
    """
    Check allergy information.

    Args:
        menu_item:
            확인할 음식 이름

        allergy:
            손님이 알레르기가 있는 재료

    Returns:
        Allergy information
    """

    ingredients = {
        "핑크 김치 크림 브루스케타": ["milk", "gluten"],
        "명란 감자 구름 타파스": ["fish", "milk"],
        "서울 불고기 미니 타코": ["gluten", "soy"],
        "갸루 치킨 바이트": ["gluten"],
        "된장 버터 쉬림프": ["shellfish", "milk"],
        "시부야 고추장 라구 파스타": ["gluten"],
    }

    menu_allergy = ingredients.get(menu_item, [])

    if allergy.lower() in menu_allergy:

        return (
            f"⚠️ 알레르기 확인\n"
            f"{menu_item}에는 {allergy} 성분이 포함될 가능성이 있어요.\n"
            f"헉ㅠㅠ 먹기 전에 꼭 확인해줘!"
        )

    return (
        f"✅ 알레르기 확인\n"
        f"{menu_item}에는 {allergy} 정보가 확인되지 않았어요.\n"
        f"그래도 안전하게 직원에게 한번 더 확인 추천해 💖"
    )


@function_tool
def recommend_wine(taste: str, food: str) -> str:
    """
    Recommend natural wine.

    Args:
        taste:
            손님 취향
            - sweet
            - fresh
            - rich

        food:
            같이 먹는 음식

    Returns:
        Wine recommendation
    """

    wines = {
        "sweet": "💗 Pink Tokyo Sparkle\n"
        "상큼하고 부담 없는 로제 스파클링\n"
        "첫 와인으로 완전 추천 ✨",
        "fresh": "☁️ Shibuya Cloud White\n"
        "과일 향과 깔끔한 느낌\n"
        "브루스케타랑 찰떡 🍷",
        "rich": "🌙 Seoul Night Red\n" "부드럽고 깊은 느낌\n" "불고기/라구랑 잘 맞아",
    }

    return "야호~ 오늘 와인 픽은 이거야 💅\n\n" + wines.get(
        taste, "✨ 오늘은 직원 추천 와인으로 가보자!"
    )


@function_tool
def wine_pairing_for_tapas(menu_item: str) -> str:
    """
    Recommend wine pairing for tapas menu.

    Args:
        menu_item:
            Pairing할 음식 이름

    Returns:
        Recommended wine and pairing reason
    """

    pairing_data = {
        "핑크 김치 크림 브루스케타": {
            "wine": "☁️ Shibuya Cloud White",
            "type": "Natural White",
            "reason": "크림의 부드러움과 김치의 감칠맛을 깔끔하게 잡아주는 조합",
        },
        "명란 감자 구름 타파스": {
            "wine": "💗 Pink Tokyo Sparkle",
            "type": "Sparkling Rosé",
            "reason": "짭짤한 명란과 탄산감 있는 와인이 만나서 입맛을 살려주는 조합",
        },
        "서울 불고기 미니 타코": {
            "wine": "🌙 Seoul Night Red",
            "type": "Natural Red",
            "reason": "불고기의 달콤한 풍미와 부드러운 레드 와인이 잘 어울림",
        },
        "갸루 치킨 바이트": {
            "wine": "💗 Pink Tokyo Sparkle",
            "type": "Sparkling Rosé",
            "reason": "바삭한 치킨의 느끼함을 상큼하게 잡아주는 조합",
        },
        "된장 버터 쉬림프": {
            "wine": "☁️ Shibuya Cloud White",
            "type": "Natural White",
            "reason": "버터의 고소함과 새우 풍미를 살려주는 와인",
        },
        "시부야 고추장 라구 파스타": {
            "wine": "🌙 Seoul Night Red",
            "type": "Natural Red",
            "reason": "매콤한 라구와 깊은 과일향 레드 와인의 밸런스",
        },
    }

    pairing = pairing_data.get(menu_item)

    if not pairing:

        return (
            "헉 이 메뉴는 아직 추천 데이터가 없어 ㅠㅠ\n" "직원 추천으로 골라볼까? 🍷"
        )
    return (
        "✨ 오늘의 와인 페어링 추천 ✨\n\n"
        f"🍽 메뉴: {menu_item}\n"
        f"🍷 와인: {pairing['wine']}\n"
        f"종류: {pairing['type']}\n\n"
        f"💖 이유:\n{pairing['reason']}\n\n"
        "이 조합 완전 분위기 좋아 ㅎㅎ"
    )


@function_tool
def describe_wine(wine_name: str) -> str:
    """
    Describe wine information.

    Args:
        wine_name:
            Wine name

    Returns:
        Wine style, taste, pairing information
    """

    wine_data = {
        "Pink Tokyo Sparkle": {
            "type": "Sparkling Rosé",
            "taste": "딸기, 체리 느낌의 상큼한 과일향",
            "body": "가볍고 부담 없음",
            "level": "와인 처음 마시는 사람 추천",
            "pairing": "브루스케타, 치즈, 가벼운 타파스",
        },
        "Shibuya Cloud White": {
            "type": "Natural White",
            "taste": "화이트 과일 느낌 + 깔끔한 마무리",
            "body": "가볍고 산뜻함",
            "level": "입문자 추천",
            "pairing": "해산물, 크림 메뉴",
        },
        "Seoul Night Red": {
            "type": "Natural Red",
            "taste": "체리, 베리류 과일 느낌과 부드러운 풍미",
            "body": "중간 정도",
            "level": "레드 와인 좋아하는 사람 추천",
            "pairing": "고기, 라구 파스타",
        },
        "Black Glitter Funky": {
            "type": "Orange Wine",
            "taste": "독특하고 개성 있는 향",
            "body": "풍미가 강한 스타일",
            "level": "새로운 와인 좋아하는 사람 추천",
            "pairing": "치즈, 강한 맛 음식",
        },
    }

    wine = wine_data.get(wine_name)

    if not wine:

        return (
            "뿌엥ㅠㅠ 아직 그 와인은 정보가 없어.\n" "다른 와인 이름으로 한번 알려줘 🍷"
        )

    return (
        f"🍷 {wine_name} 소개 ✨\n\n"
        f"종류: {wine['type']}\n"
        f"맛 느낌: {wine['taste']}\n"
        f"느낌: {wine['body']}\n"
        f"추천 대상: {wine['level']}\n"
        f"잘 맞는 음식: {wine['pairing']}\n\n"
        "내 픽으로는 이거 분위기 내기 완전 좋아 💅"
    )


@function_tool
def check_availability(date: str, time: str, guests: int) -> str:
    """
    Check reservation availability.

    Args:
        date:
            방문 날짜

        time:
            방문 시간

        guests:
            인원수

    Returns:
        Availability result
    """

    available = random.choice([True, False])

    if guests > 6:
        return "🥺 예약 안내\n" "최대 6명까지 가능해!"

    if available:

        return f"✨ 자리 있어!\n" f"{date} {time}\n" f"{guests}명 예약 가능해 💖"

    return "뿌엥ㅠㅠ 해당 시간은 마감이야.\n" "다른 시간 한번 볼까?"


@function_tool
def create_reservation(name: str, date: str, time: str, guests: int) -> str:
    """
    Create reservation.

    Args:
        name:
            예약자 이름

        date:
            날짜

        time:
            시간

        guests:
            인원

    Returns:
        Reservation confirmation
    """

    reservation_id = random.randint(1000, 9999)

    return (
        "💖 예약 완료 ✨\n\n"
        f"예약번호: GH-{reservation_id}\n"
        f"이름: {name}\n"
        f"날짜: {date}\n"
        f"시간: {time}\n"
        f"인원: {guests}명\n\n"
        "야호~ 곧 만나자 🍷"
    )


@function_tool
def create_order(items: list[str]) -> str:
    """
    Create food order.

    Args:

        items:
            주문 메뉴 리스트

    Returns:
        Order result
    """

    order_id = random.randint(100, 999)

    return (
        "✨ 주문 완료 💅\n\n"
        f"주문번호: {order_id}\n"
        f"메뉴:\n"
        + "\n".join(f"- {item}" for item in items)
        + "\n\n완전 좋은 선택이야 🍷"
    )


@function_tool
def check_order_status(order_id: str) -> str:
    """
    Check order status.

    Args:
        order_id:
            주문번호

    Returns:
        Current order status
    """

    status = random.choice(["조리 중 🍳", "곧 나와 ✨", "준비 완료 💖"])

    return f"주문 상태 확인 💅\n" f"{order_id}: {status}"


@function_tool
def check_refund_policy(issue_type: str, order_status: str) -> str:
    """
    Check refund policy.

    Args:
        issue_type:
            불만 유형
            - food
            - service
            - reservation
            - payment

        order_status:
            주문/예약 상태
            - not_started
            - in_progress
            - completed

    Returns:
        Refund policy information
    """

    refund_rules = {
        "food": {
            "completed": "음식 문제 확인 후 부분 환불 또는 재제공 가능",
            "in_progress": "조리 중이면 메뉴 변경 가능 여부 확인",
            "not_started": "주문 취소 가능",
        },
        "service": {
            "completed": "상황 확인 후 보상 안내 가능",
            "in_progress": "즉시 직원 확인 요청 가능",
        },
        "reservation": {
            "completed": "예약 관련 상황 확인 후 안내",
            "not_started": "예약 변경 가능",
        },
        "payment": {"completed": "결제 내역 확인 후 처리"},
    }

    policy = refund_rules.get(issue_type, {}).get(order_status)

    if policy:

        return (
            "💳 환불/처리 안내 ✨\n\n"
            f"{policy}\n\n"
            "확인해서 최대한 빠르게 도와줄게."
        )

    return "🥺 해당 상황은 추가 확인이 필요해.\n" "매니저 확인 요청해볼게."


@function_tool
def offer_discount(issue_severity: str) -> str:
    """
    Offer compensation.

    Args:
        issue_severity:
            문제 심각도
            - minor
            - medium
            - serious

    Returns:
        Compensation offer
    """

    compensation = {
        "minor": "다음 방문 시 사용할 수 있는 10% 할인 쿠폰 제공",
        "medium": "다음 방문 음료 1잔 서비스 제공",
        "serious": "매니저 확인 후 맞춤 보상 진행",
    }

    result = compensation.get(issue_severity, "상황 확인 후 안내")

    return (
        "💖 고객 케어 안내\n\n"
        f"{result}\n\n"
        "기대하고 방문해준 만큼 더 좋은 경험 드리고 싶어."
    )


@function_tool
def create_complaint(customer_name: str, category: str, message: str) -> str:
    """
    Create customer complaint.

    Args:
        customer_name:
            고객 이름

        category:
            food/service/waiting/payment

        message:
            불편 내용

    Returns:
        Complaint ticket
    """

    ticket = random.randint(10000, 99999)

    return (
        "🥺 의견 접수 완료\n\n"
        f"접수번호: FB-{ticket}\n"
        f"분류: {category}\n"
        f"내용: {message}\n\n"
        "말해줘서 고마워.\n"
        "더 좋은 공간 만들 수 있게 꼭 확인할게 ✨"
    )


@function_tool
def get_restaurant_info() -> str:
    """
    Get restaurant information.

    Returns:
        Brand concept and atmosphere
    """

    return (
        "💖 GAL HOUSE SEOUL\n\n"
        "컨셉:\n"
        "Y2K 시부야 갸루 감성 × 서울 내추럴 와인 타파스바\n\n"
        "분위기:\n"
        "- 네온 감성\n"
        "- 프리쿠라 포토존\n"
        "- 작은 아지트 느낌\n"
        "- 와인과 퓨전 타파스\n\n"
        "최대 예약 인원: 6명"
    )
