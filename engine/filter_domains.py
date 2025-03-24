import sys
import tldextract
from sqlalchemy.orm import sessionmaker
from db import engine, Scope,Resource
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)


def get_top_level_domain(domain):
    """Extracts the top-level domain (TLD) from a given domain."""
    extracted = tldextract.extract(domain)
    return f"{extracted.domain}.{extracted.suffix}" if extracted.suffix else extracted.domain

def validate_domains(scope_id, file_path):
    """Checks if extracted TLDs match the scope name."""
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get scope
    scope = session.query(Scope).filter_by(id=scope_id).first()
    if not scope:
        print(f"Error: Scope with ID {scope_id} not found.")
        return

    scope_name = get_top_level_domain(scope.name)
    print(f"Scope Name (TLD): {scope_name}")

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(f"{line}")
            domain = line.strip()
            if not domain:
                continue  # Skip empty lines

            extracted_tld = get_top_level_domain(domain)
            if extracted_tld == scope_name:
                print(f"Filtered:{domain}")
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_new_subdomains.py <scope_id> <file_path>")
        sys.exit(1)

    scope_id = int(sys.argv[1])
    file_path = sys.argv[2]
    validate_domains(scope_id, file_path)