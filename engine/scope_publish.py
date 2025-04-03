import os
from db import Session, Scope

SCOPE_ROOT = "scope"

def export():
    session = Session()
    scopes = session.query(Scope).all()

    tag_map = {}
    for scope in scopes:
        tag = scope.tag or "untagged"
        tag_map.setdefault(tag.lower(), set()).add(scope.name)

    for tag, entries in tag_map.items():
        scope_file = os.path.join(SCOPE_ROOT, f"{tag}.txt")
        existing = set()
        if os.path.exists(scope_file):
            with open(scope_file, "r") as f:
                existing = set(line.strip() for line in f if line.strip())
        combined = existing.union(entries)
        with open(scope_file, "w") as f:
            f.write("\n".join(sorted(combined)) + "\n")

    print("Scope sync completed")

if __name__ == "__main__":
    export()