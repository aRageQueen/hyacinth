# hyacinth
hyacinth scans plain text files for common forms of personally identifiable information (PII) — including emails, phone numbers, SSNs, DOB, Credit Card numbers, and Physical addresses — and redacts them securely using regex-based pattern matching. Designed for developers who need data hygiene without heavy dependencies.

## Features
Detects and redacts:
- Email addresses
- US phone numbers
- Social Security Numbers (SSNs)
- Date of Birth
- Credit Card numbers
- Physical addresses
- Simple CLI interface
- Lightweight and dependency-free (pure Python)
- Easily extensible with new patterns or input types

## Installation
Clone the repository:
```python
git clone https://github.com/your-username/hyacinth.git
cd hyacinth
```
## Usage
1. Run hyacinth from the command line:
    ```python
    python hyacinth.py
    ```
1. Choose option (1 to scrub file)
1. Add filepath to scrub data from (ex: `single_entry_test_redacted.txt`)

# Tool structure
```python
hyacinth/
├── hyacinth.py       # Main CLI script
├── patterns.py       # Regex definitions
├── utils.py          # Redaction logic
├── test.txt          # Example input file
└── README.md         # Project documentation
```
