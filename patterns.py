import re

#regex patterns for desired PII
email_regex = re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')
phone_regex = re.compile(r'(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
ssn_regex = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
dob_regex = re.compile(r'\b(?:\d{1,2}[-/])?\d{1,2}[-/]\d{2,4}\b')
credit_card_regex = re.compile(r'\b(?:\d[ -]*?){13,16}\b') # matches most 13-16 digit card numbers with optional separators

pii_patterns = {
    # dictionary mapping of PII labels to corresponding regex patterns
    "EMAIL": email_regex,
    "PHONE": phone_regex,
    "SSN": ssn_regex,
    "DOB": dob_regex,
    "CREDIT CARD": credit_card_regex
}