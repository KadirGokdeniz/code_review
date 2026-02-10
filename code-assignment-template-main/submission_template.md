# AI Code Review Assignment (Python)

## Candidate
- Name: Kadir Gokdeniz
- Approximate time spent: 90 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- If orders is empty, count becomes zero and the function raises a ZeroDivisionError.
- The total is calculated only for non-cancelled orders, but the divisor (count) includes all orders, may be lead to an incorrect average 
because of only trusting "cancelled" keyword.
- Count number counts every order in the data, however we wanted to know only about noncancelled items.

### Edge cases & risks
- Orders with missing or invalid amount values (e.g. None or non-numeric types) can cause exceptions or incorrect calculations.
- Orders with unexpected or missing status fields may be incorrectly included or excluded from the calculation.
- The logic assumes that cancelled orders are identified by status == "cancelled", which may not match the actual data model.

### Code quality / design issues
- The function assumes orders is a list of dictionaries with specific keys, but this input structure is neither validated nor documented.
- The code assumes order["amount"] is always present and numeric, instead of handling this defensively.
- There is no clear contract or documentation describing the expected input structure or behavior.

## 2) Proposed Fixes / Improvements
### Summary of changes
- "cancelled" string is coverted to is_cancelled bool. Order filtering now uses a boolean value instead of string comparison. (This is more understandable.)
- len(orders) is coverted to active_count. Average is calculated by dividing only by non-cancelled orders, not all orders.
- Added try/except ZeroDivisionError. Raises a meaningful error message when all orders are cancelled.
- Checks that orders is a non-empty list, each element is a dict, required keys (status, amount, is_cancelled) exist, and their types are correct.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Valid input with mixed orders: Some cancelled, some active, verifies correct average calculation.
- All orders cancelled (is_cancelled=True): Should raise ZeroDivisionError.
- Empty list / non-list input: Should raise ValueError or TypeError.
- Missing keys: e.g. order without amount — should raise ValueError.
- Wrong types: e.g. amount="abc" or is_cancelled="yes", should raise ValueError.
- Single active order: Edge case to confirm average equals that order's amount.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation says "dividing by the number of orders" — this is wrong. The original code divides by len(orders) (all orders), not just non-cancelled ones, which produces an incorrect average.
- It claims the function "correctly excludes cancelled orders" but the denominator still includes them, so the exclusion is only partial.
### Rewritten explanation
- This function calculates the average order value by summing the amounts of non-cancelled orders and dividing by the count of non-cancelled orders only.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The original code had a wrong denominator (len(orders) instead of noncancelled count), no input validation, and used string comparison instead of a boolean. The corrected version fixes all three.
- Confidence & unknowns: High confidence in the core logic — averaging non-cancelled orders. The main unknown is that we assume the input is a list of dicts with specific keys (status, amount, is_cancelled), but the original specification doesn't explicitly define the expected data structure.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Only checks "@" in email — strings like "user@domain", "@domain.com" are counted as valid. Should require x@x.valid_tlds format.

### Edge cases & risks
- Non-string elements (e.g., None, 123) cause TypeError crash because in operator doesn't work on non-string types.

### Code quality / design issues
- No input validation to check whether emails is actually a list.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added x@x.valid_tlds format validation: local part must be non-empty, domain must contain at least one "." with non-empty parts on both sides.
- Non-string entries are skipped instead of crashing.
- Added type check to ensure emails is a list.

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Valid emails in x@x.valid_tlds format, should be counted.
- Missing dot in domain (user@domain) — should not be counted.
- Empty local or domain (@domain.com, user@) — should not be counted.
- Non-string elements (None, 123) — should be skipped without crash.
- Empty list, should return 0.
- Non-list input — should raise TypeError.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- "Safely ignores invalid entries" is incorrect; it counts most invalid emails as valid and crashes on non-string inputs.
- "Handles empty input correctly" is true but misleading; it implies the function is robust, when it's not.

### Rewritten explanation
- This function counts emails matching the x@x.valid_tlds format. Non-string entries are safely skipped. A TypeError is raised if the input is not a list.

## 4) Final Judgment
- Decision: Request Changes
- Justification:The "@" in email check is too weak and counts most invalid emails as valid. Non-string inputs cause a crash. The corrected version validates the x@x.valid_tlds format and handles edge cases properly.
- Confidence & unknowns: Mid-High confidence. We use x@x.valid_tlds format where valid_tlds covers common extensions (com, edu, org, etc.) but the list may not be comprehensive enough for all real-world cases. Also, single-character local and domain parts (e.g., a@b.com) are technically accepted, though such emails are rarely used in practice.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- count = len(values) includes None entries in the denominator, producing a wrong average.
- No ZeroDivisionError protection — empty list or all-None list causes a crash.

### Edge cases & risks
- float(v) doesn't guarantee v is numeric — strings like "abc" would crash with ValueError.

### Code quality / design issues
- No input validation to check whether values is actually a list.

## 2) Proposed Fixes / Improvements
### Summary of changes
- len(values) replaced with valid_count that only counts non-None numeric entries.
- Added try/except ZeroDivisionError for empty or all-None inputs.
- Added type check — non-numeric, non-None values raise ValueError instead of crashing on float().
- Added input validation to ensure values is a list.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- Mixed valid and None values — should average only non-None values.
- All None values — should raise ZeroDivisionError.
- Non-numeric entries (e.g., "abc") — should raise ValueError.
- All numeric values - should not give any error.
- Non-list input — should raise TypeError.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- "Ignoring missing values and averaging the remaining" is misleading — None values are skipped in the sum but still included in the denominator, so the average is wrong.
- "Safely handles mixed input types" is incorrect — non-numeric strings crash the function.

### Rewritten explanation
- This function calculates the average of valid numeric measurements. None entries are skipped in both the sum and the count. Non-numeric and non-None values raise a ValueError. If no valid measurements exist, a ZeroDivisionError is raised.

## 4) Final Judgment
- Decision: Request Changes
- Justification: The denominator incorrectly includes None entries, there is no zero division protection, and float(v) blindly converts without type checking. The corrected version fixes all three issues.
- Confidence & unknowns: High confidence. The main assumption is that valid measurements are only int or float types — if other numeric types (e.g., Decimal) are expected, the type check would need to be extended.
