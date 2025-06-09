# hyacinth
hyacinth scans plain text files for common forms of personally identifiable information (PII) — including emails, phone numbers, SSNs, DOB, Credit Card numbers, and Physical addresses — and redacts them securely using regex-based pattern matching. Designed for developers who need data hygiene without heavy dependencies.

## Features
Detects and redacts:
*Email addresses
*US phone numbers
*Social Security Numbers (SSNs)
*Date of Birth
*Credit Card numbers
*Physical addresses
*Simple CLI interface
*Lightweight and dependency-free (pure Python)
*Easily extensible with new patterns or input types

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
Example input: "Please contact Harry at harry.arnold@outlook.com or (232) 786-9982. His SSN is 321-09-3219 & his birthday is 03-21-1980. He paid with 4151 1110 2162 1951 and the backup was 5507-9823-0220-3304. His address is 10 Darington Ave, Springfield, IL 23157. Thanks!"
Example output: "Please contact Harry at [REDACTED EMAIL] or [REDACTED PHONE]. His SSN is [REDACTED SSN] & his birthday is [REDACTED DOB]. He paid with [REDACTED CREDIT CARD] and the backup was [REDACTED CREDIT CARD]. His address is [REDACTED ADDRESS]. Thanks!"
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
