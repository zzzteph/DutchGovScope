import sys
from db import Session, Scope, Resource

def get_subdomains(scope_id: int):
    session = Session()

    scope = session.query(Scope).filter_by(id=scope_id).first()
    if not scope:
        print(f"No scope found with ID {scope_id}")
        return

    subdomains = (
        session.query(Resource.name)
        .filter_by(scope_id=scope_id, type="domain")
        .all()
    )

    for name, in subdomains:
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python get_subdomains.py <scope_id>")
        sys.exit(1)

    get_subdomains(int(sys.argv[1]))