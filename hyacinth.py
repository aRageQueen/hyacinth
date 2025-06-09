import argparse
from utils import redact_text

def main():
    parser = argparse.ArgumentParser(description="Hyacinth: PII Scrubbing Tool")
    parser.add_argument("input_file", help="Path to input text file")
    parser.add_argument("output_file", help="Path to save redacted output")
    args = parser.parse_args()

    # read input file
    with open(args.input_file, "r") as f:
        content = f.read()

    # redact the PII
    redacted = redact_text(content)

    # write the redacted information to an output file
    with open(args.output_file, "w") as f:
        f.write(redacted)

    print(f"Redacted output saved to {args.output_file}")

if __name__ == "__main__":
    main()