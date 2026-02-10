def calculate_average_order_value(orders):
    # Input validation
    if not isinstance(orders, list) or len(orders) == 0:
        raise ValueError("orders must be a non-empty list.")

    total = 0
    active_count = 0

    for i, order in enumerate(orders):
        if not isinstance(order, dict):
            raise TypeError(f"orders[{i}] must be a dict.")

        # Check required keys exist
        for key in ("status", "amount", "is_cancelled"):
            if key not in order:
                raise ValueError(f"orders[{i}] is missing '{key}'.")

        # Type checks
        if not isinstance(order["status"], str):
            raise ValueError(f"orders[{i}]['status'] must be a string.")
        if not isinstance(order["amount"], (int, float)):
            raise ValueError(f"orders[{i}]['amount'] must be a number.")
        if not isinstance(order["is_cancelled"], bool):
            raise ValueError(f"orders[{i}]['is_cancelled'] must be a bool.")

        # Sum only non cancelled orders
        if not order["is_cancelled"]:
            total += order["amount"]
            active_count += 1

    # Zero division protection
    try:
        return total / active_count
    except ZeroDivisionError:
        raise ZeroDivisionError("No active orders found, cannot calculate average.")