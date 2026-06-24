from agents import function_tool
import random


# =============================================================================
# MENU AGENT TOOLS
# =============================================================================


@function_tool
def search_tapas_menu(category: str = "all") -> str:
    """
    Search tapas bar food menu.

    Args:
        category: tapas category such as seafood, meat, cheese
    """

    menus = {
        "seafood": [
            "🦐 Gambas al Ajillo - Garlic Shrimp (€12)",
            "🐙 Grilled Octopus with Paprika (€16)",
        ],
        "meat": ["🥩 Iberico Ham Platter (€18)", "🍖 Chorizo in Red Wine Sauce (€13)"],
        "cheese": ["🧀 Manchego Cheese Plate (€14)"],
    }

    if category == "all":
        items = sum(menus.values(), [])
    else:
        items = menus.get(category, [])

    return f"🍽️ Tapas Menu\n" + "\n".join(f"• {item}" for item in items)


@function_tool
def get_menu_details(menu_item: str) -> str:
    """
    Get ingredient and description information.

    Args:
        menu_item: Name of tapas menu item
    """

    details = {
        "gambas": "Garlic shrimp cooked with olive oil and chili. A Spanish classic.",
        "iberico": "Premium aged Iberico pork ham served with bread.",
        "octopus": "Grilled octopus with paprika and olive oil.",
    }

    for key, value in details.items():
        if key in menu_item.lower():
            return f"🥘 {menu_item}\n{value}"

    return "No menu information found."


@function_tool
def check_food_allergy(menu_item: str, allergy: str) -> str:
    """
    Check allergy information.

    Args:
        menu_item: Food name
        allergy: Ingredient user is allergic to
    """

    possible = random.choice([True, False])

    if possible:
        return f"⚠️ Allergy Warning\n" f"{menu_item} may contain {allergy}."

    return f"✅ Allergy Check\n" f"{menu_item} does not contain {allergy}."


# =============================================================================
# ORDER AGENT TOOLS
# =============================================================================


@function_tool
def create_tapas_order(items: list[str]) -> str:
    """
    Create customer order.

    Args:
        items: Ordered food and drinks
    """

    order_id = f"ORDER-{random.randint(1000,9999)}"

    return (
        f"🧾 Order Created\n"
        f"Order ID: {order_id}\n\n"
        f"Items:\n" + "\n".join(f"• {item}" for item in items) + "\n\nStatus: Preparing"
    )


@function_tool
def add_item_to_order(order_id: str, item: str) -> str:
    """
    Add item to existing order.

    Args:
        order_id: Current order id
        item: Additional item
    """

    return f"➕ Added to Order\n" f"Order ID: {order_id}\n" f"Added item: {item}"


@function_tool
def confirm_customer_order(order_id: str) -> str:
    """
    Confirm order.

    Args:
        order_id: Order ID
    """

    return (
        f"✅ Order Confirmed\n"
        f"Order ID: {order_id}\n"
        f"Your tapas and drinks will be served soon."
    )


# =============================================================================
# RESERVATION AGENT TOOLS
# =============================================================================


@function_tool
def check_table_availability(date: str, time: str, guests: int) -> str:
    """
    Check table availability.

    Args:
        date: Reservation date
        time: Reservation time
        guests: Number of guests
    """

    available = random.choice([True, True, False])

    if available:
        return (
            f"🪑 Table Available\n"
            f"Date: {date}\n"
            f"Time: {time}\n"
            f"Guests: {guests}"
        )

    return "❌ No availability.\n" "Please choose another time."


@function_tool
def make_reservation(name: str, date: str, time: str, guests: int) -> str:
    """
    Create reservation.

    Args:
        name: Customer name
        date: Reservation date
        time: Reservation time
        guests: Number of guests
    """

    reservation_id = f"RES-{random.randint(1000,9999)}"

    return (
        f"🎉 Reservation Confirmed\n"
        f"Reservation ID: {reservation_id}\n"
        f"Name: {name}\n"
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Guests: {guests}"
    )


@function_tool
def lookup_reservation(reservation_id: str) -> str:
    """
    Lookup reservation.

    Args:
        reservation_id: Reservation ID
    """

    return (
        f"📅 Reservation Details\n"
        f"ID: {reservation_id}\n"
        f"Status: Confirmed\n"
        f"Seat: Window table"
    )


# =============================================================================
# WINE AGENT (SOMMELIER) TOOLS
# =============================================================================


@function_tool
def recommend_wine(preference: str, food_pairing: str = "") -> str:
    """
    Recommend wine based on taste and food.

    Args:
        preference: User preference such as sweet, dry, light, strong
        food_pairing: Food user plans to eat
    """

    wines = {
        "sweet": "🍷 Moscato - Sweet and fruity",
        "dry": "🍷 Albariño - Crisp and refreshing",
        "strong": "🍷 Rioja Reserva - Rich and full-bodied",
        "light": "🍷 Pinot Noir - Light and smooth",
    }

    recommendation = wines.get(
        preference.lower(), "🍷 Cava Brut - Great with various tapas"
    )

    return (
        f"🍷 Sommelier Recommendation\n"
        f"Preference: {preference}\n"
        f"Food: {food_pairing}\n\n"
        f"Recommended: {recommendation}"
    )


@function_tool
def wine_pairing_for_tapas(tapas: str) -> str:
    """
    Recommend wine pairing for tapas.

    Args:
        tapas: Tapas dish name
    """

    pairings = {
        "shrimp": "Albariño White Wine",
        "ham": "Rioja Reserva",
        "cheese": "Tempranillo",
        "octopus": "Cava Brut",
    }

    for key, wine in pairings.items():
        if key in tapas.lower():
            return f"🍷 Pairing Suggestion\n" f"{tapas} + {wine}"

    return "🍷 Pairing Suggestion\n" "Cava Brut is a safe choice for most tapas."


@function_tool
def describe_wine(wine_name: str) -> str:
    """
    Explain wine characteristics.

    Args:
        wine_name: Wine name
    """

    return (
        f"🍷 Wine Profile\n"
        f"{wine_name}\n"
        f"Flavor: Balanced acidity, fruity aroma\n"
        f"Pairs well with Spanish tapas."
    )


@function_tool
def check_refund_policy(order_id: str) -> str:
    """
    Check whether an order is eligible for refund.

    Args:
        order_id: Customer order ID
    """

    # mock data
    refund_available = True

    if refund_available:
        return (
            f"Order {order_id} is eligible for refund. "
            "Refund can be processed within 3 business days."
        )

    return (
        f"Order {order_id} is not eligible for refund " "according to current policy."
    )


@function_tool
def offer_discount(customer_id: str) -> str:
    """
    Provide a compensation discount for unhappy customers.

    Args:
        customer_id: Customer ID
    """

    return f"Customer {customer_id} received a 20% apology discount coupon."


@function_tool
def request_manager_callback(customer_id: str, reason: str) -> str:
    """
    Request a manager callback for serious complaints.

    Args:
        customer_id: Customer ID
        reason: Reason for escalation
    """

    return (
        f"Manager callback requested for customer {customer_id}. " f"Reason: {reason}"
    )


@function_tool
def escalate_issue(customer_id: str, severity: str) -> str:
    """
    Escalate critical customer complaints.

    Args:
        customer_id: Customer ID
        severity: low, medium, high, critical
    """

    return f"Issue escalated. " f"Customer: {customer_id}, " f"Severity: {severity}"
