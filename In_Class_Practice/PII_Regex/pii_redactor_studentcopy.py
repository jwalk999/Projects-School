"""
Week 11-2 Practice: PII Scanner and Redactor
CIS 3680, Prof. Taylor

Ungraded, no submission.
"""

import re

# Regex matching
# xxx-xx-xxxx
SSN_PATTERN = r"\d{3}-\d{2}-\d{4}"
# 9xx-xx-xxxx
ITIN_PATTERN = r"9\d{2}-\d{3}-\d{4}"
# xxxx(- )xxxx(- )xxxx(- )(xxxxxxx)
CC_PATTERN = r"\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{1,7}"
# (xxx)[-. ]xxx[-. ]xxxx
PHONE_PATTERN = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"


def find_matches(pattern: str, text: str) -> list[str]:
    """Return every match of pattern found in text."""
    return re.findall(pattern, text)


def redact(text: str, pattern: str, label: str) -> str:
    """Replace every match of pattern in text with [REDACTED-{label}]."""
    return re.sub(pattern, f"[REDACTED-{label}]", text)


def main() -> None:
    with open("leaked_memo.txt", encoding="utf-8") as f:
        text = f.read()

    # Find and print each category before redacting.
    print("--- Scan results ---")
    ssn_matches = find_matches(SSN_PATTERN, text)
    itin_matches = find_matches(ITIN_PATTERN, text)
    cc_matches = find_matches(CC_PATTERN, text)
    phone_matches = find_matches(PHONE_PATTERN, text)

    print(f"SSNs found: {ssn_matches}")
    print(f"ITINs found: {itin_matches}")
    print(f"Credit card numbers found: {cc_matches}")
    print(f"Phone numbers found: {phone_matches}")

    # Redact the matches.
    redacted_text = text
    redacted_text = redact(redacted_text, SSN_PATTERN, "SSN")
    redacted_text = redact(redacted_text, ITIN_PATTERN, "ITIN")
    redacted_text = redact(redacted_text, CC_PATTERN, "CC")
    redacted_text = redact(redacted_text, PHONE_PATTERN, "PHONE")

    print("\n--- Redacted memo ---")
    print(redacted_text)

    print("\n--- Summary ---")
    # TODO: print how many of each type were redacted, and the total


if __name__ == "__main__":
    main()
