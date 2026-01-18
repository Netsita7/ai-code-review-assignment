def calculate_average_order_value(orders):
    if not orders:
        raise ValueError("Cannot calculate average: orders list is empty")
    
    total = 0
    valid_count = 0
    
    for order in orders:
        if order.get("status") != "cancelled":
            amount = order.get("amount")
            if amount is not None:
                try:
                    total += float(amount)
                    valid_count += 1
                except (ValueError, TypeError):
                    pass
    
    if valid_count == 0:
        raise ValueError("Cannot calculate average: no valid non-cancelled orders")
    
    return total / valid_count
