# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
def count_valid_emails(emails):
    # Input validation
    if not isinstance(emails, list):
        raise TypeError(f"emails must be a list, got {type(emails).__name__}.")

    count = 0

    for email in emails:
        # Skip non-string entries
        if not isinstance(email, str):
            continue

        # Check x@x.valid_tlds format
        if "@" not in email:
            continue

        local, _, domain = email.partition("@")

        valid_tlds = {"com", "edu", "org", "net", "gov", "io", "co", "info"}

        parts = domain.split(".")
        if local and len(parts) >= 2 and all(parts) and parts[-1] in valid_tlds:
            count += 1

    return count
