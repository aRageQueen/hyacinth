import os
import pathlib
from utils import redact_text

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
OUTPUT_DIR = os.path.join(ROOT_DIR, 'output')

def scrub_file():
    #get file paths from the user
    input_path = input("Enter path to input file: ")

    try:
        # read input file contents
        with open(input_path, "r") as f:
            content = f.read()

        # redact the PII
        redacted = redact_text(content)

        output = pathlib.Path(input_path)
        # generate the output file
        output_path = os.path.join(OUTPUT_DIR, f"{output.stem}_REDACTED{output.suffix}")

        # write the redacted content to the new output file
        with open(output_path, "w") as f:
            f.write(redacted)
        
        print(f"\n File is scrubbed and saved to {output_path}\n")

    except FileNotFoundError:
        print("\n File wasn't found. Please check your path and try again.\n")
    
    except Exception as e:
        print(f"\n An error has occurred: {e}\n")

def show_menu():
    print("Welcome to hyacinth: a lightweight PII scrubber")

    # menu loop
    while True:
        print("1. Scrub a file")
        print("2. Exit\n")

        # get the user's choice
        choice = input("Enter your choice: ")
        if choice == "1":
            scrub_file()
        elif choice == "2":
            print("\n Goodbye!\n")
            break
        else:
            print("\n Invalid choice. Please enter either 1 or 2.\n")

if __name__ == "__main__":
    show_menu()