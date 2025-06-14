import re

#regex patterns for desired PII
email_regex = re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')
phone_regex = re.compile(r'(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
ssn_regex = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
dob_regex = re.compile(r'\b(?:\d{1,2}[-/])?\d{1,2}[-/]\d{2,4}\b')
credit_card_regex = re.compile(r'\b(?:\d[ -]*?){13,16}\b') # matches most 13-16 digit card numbers with optional separators
address_regex = re.compile(r'\b\d{1,5}\s[\w\s]+\s(?:Street|St|Avenue|Ave|Boulevard|Blvd|Road|Rd|Lane|Ln|Drive|Dr|Court|Ct|Way)'
    r'(?:,\s[\w\s]+)?,\s[A-Z]{2}\s\d{5}(?:-\d{4})?\b',
    re.IGNORECASE) #basic address regex

pii_patterns = {
    # dictionary mapping of PII labels to corresponding regex patterns
    "EMAIL": email_regex,
    "CREDIT CARD": credit_card_regex,
    "SSN": ssn_regex,
    "PHONE": phone_regex,
    "DOB": dob_regex,
    "ADDRESS": address_regex
}