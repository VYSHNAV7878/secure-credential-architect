import secrets
import string
import argparse

def generate_secure_password(length=16, use_symbols=True, use_numbers=True):
    """Generates a cryptographically secure random password."""
    
    # Define the character pool
    chars = string.ascii_letters  # ABC...xyz
    if use_numbers:
        chars += string.digits    # 0123456789
    if use_symbols:
        chars += "!@#$%^&*()-_=+" # Special characters

    # The 'secrets' module ensures the choice is not predictable
    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def main():
    # Adding a CLI interface makes this look like a pro tool!
    parser = argparse.ArgumentParser(description="Cryptographically Secure Credential Architect")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the credential")
    parser.add_argument("-ns", "--no-symbols", action="store_true", help="Exclude symbols")
    
    args = parser.parse_args()

    password = generate_secure_password(length=args.length, use_symbols=not args.no_symbols)
    
    print("\n" + "="*40)
    print("🛡️  SECURE CREDENTIAL GENERATED")
    print("="*40)
    print(f"\nYour Secure Key: \033[96m{password}\033[0m")
    print("\n" + "="*40)

if __name__ == "__main__":
    main()
