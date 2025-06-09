from patterns import pii_patterns

def redact_text(text):
    for label, pattern in pii_patterns.items():
        if label == "CREDIT CARD":
            matches = pattern.findall(text)
            for match in matches:
                if luhn_check(match):
                    text = text.replace(match, f"[REDACTED {label}]")
        # replace all matches of a pattern with a [REDACTED] label
        text = pattern.sub(f"[REDACTED {label}]", text)
    return text

# validates a credit card number using the Luhn algorithm
def luhn_check(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    checksum = 0
    parity = len(digits) % 2
    for i, digit in enumerate(digits):
        if i % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0