from patterns import pii_patterns

def redact_text(text):
    for label, pattern in pii_patterns.items():
        # replace all matches of a pattern with a [REDACTED] label
        text = pattern.sub(f"[REDACTED {label}]", text)
    return text