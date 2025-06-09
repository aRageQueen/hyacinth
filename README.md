# hyacinth
Hyacinth scans plain text files for common forms of personally identifiable information (PII) — including emails, phone numbers, SSNs, and DOB — and redacts them securely using regex-based pattern matching. Designed for developers who need data hygiene without heavy dependencies.

## Features
Detects and redacts:
    Email addresses
    US phone numbers
    Social Security Numbers (SSNs)
    Date of Birth
    Simple CLI interface
    Lightweight and dependency-free (pure Python)
    Easily extensible with new patterns or input types

## Installation
Clone the repository:
```python
git clone https://github.com/your-username/hyacinth.git
cd hyacinth
```
## Usage
Run hyacinth from the command line:
```python
python hyacinth.py
input.txt: Path to the file containing sensitive text
Example input: "Please contact Harry at harry.arnold@outlook.com or (232) 786-9982. His SSN is 321-09-3219 & his birthday is 03-21-1980. Thanks!"
Example output: Please contact Harry at [REDACTED EMAIL] or [REDACTED PHONE]. His SSN is [REDACTED SSN] & his birthday is [REDACTED DOB]. Thanks!
```

# Tool structure
```python
hyacinth/
├── hyacinth.py       # Main CLI script
├── patterns.py       # Regex definitions
├── utils.py          # Redaction logic
├── test.txt          # Example input file
└── README.md         # Project documentation
```
