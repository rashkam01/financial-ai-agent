def calculate_growth(current_value, previous_value):
    """
    Generic growth calculation.
    """

    print("\n[TOOL] calculate_growth() called")

    growth = ((current_value - previous_value) / previous_value) * 100

    result = round(growth, 2)

    print(f"[TOOL] Inputs -> current: {current_value}, previous: {previous_value}")
    print(f"[TOOL] Result -> {result}%\n")

    return result