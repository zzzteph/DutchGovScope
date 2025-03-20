import sys
import tldextract
from sqlalchemy.orm import sessionmaker
from db import engine, Scope

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
            domain = line.strip()
            if not domain:
                continue  # Skip empty lines

            extracted_tld = get_top_level_domain(domain)
            match_status = "✅ Match" if extracted_tld == scope_name else "❌ No Match"
            print(f"{domain} -> {extracted_tld} ({match_status})")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python validate_tlds.py <scope_id> <file_path>")
        sys.exit(1)

    scope_id = int(sys.argv[1])
    file_path = sys.argv[2]
    validate_domains(scope_id, file_path)