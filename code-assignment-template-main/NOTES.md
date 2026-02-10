Alternative Approaches Considered

For Task 2, considered using Python's re module or an external library (e.g., python-email-validator) for regex-based email validation including RFC 5322 compliance, but kept it simple with string operations for readability. Also, uncommon TLDs like .dev, .ai, .tr are not covered by our hardcoded list.

For Task 3, considered using try/except around float(v) instead of isinstance check — this would accept more types but make error messages less specific.