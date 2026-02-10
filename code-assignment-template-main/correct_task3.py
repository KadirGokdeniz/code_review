# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    # Input validation
    if not isinstance(values, list):
        raise TypeError(f"values must be a list, got {type(values).__name__}.")

    total = 0
    valid_count = 0

    for i, v in enumerate(values):
        # Skip None values
        if v is None:
            continue

        # Ensure value is numeric
        if not isinstance(v, (int, float)):
            raise ValueError(f"values[{i}] must be numeric or None, got {type(v).__name__}.")

        total += float(v)
        valid_count += 1

    # Zero division protection
    try:
        return total / valid_count
    except ZeroDivisionError:
        raise ZeroDivisionError("No valid measurements found, cannot calculate average.")