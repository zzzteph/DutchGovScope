import sys
import json
from db import Session, Scope, Resource, Endpoint
from datetime import datetime
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)


def import_endpoints(scope_id: int, file_path: str):
    session = Session()

    scope = session.query(Scope).filter_by(id=scope_id).first()
    if not scope:
        print(f"No scope found with ID {scope_id}")
        return

    with open(file_path, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            domain = data.get("input")
            if not domain or data.get("failed", False):
                continue 

            resource = (
                session.query(Resource)
                .filter_by(domain_id=scope_id, name=domain, type="domain")
                .first()
            )

            if resource:
                endpoint = Endpoint(
                                    resource_id=resource.id,
                                    name=data.get("url"),
                                    port=int(data.get("port", 0)),
                                    scheme=data.get("scheme"),                
                                    tech=",".join(data.get("tech", [])) if data.get("tech") else None,
                                    title=data.get("title"),
                                    response_code=int(data.get("status_code", 0)),
                                    content_length=int(data.get("content_length", 0)),
                                    words_count=int(data.get("words", 0)),
                                    data=json.dumps(data),
                                    created_at=utc_now(),
                                    updated_at=utc_now()
                                    )
                session.add(endpoint)
                print(f"Endpoint added")

    session.commit()
    print("Done importing endpoints.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python import_endpoints.py <scope_id> <file_path>")
        sys.exit(1)

    import_endpoints(int(sys.argv[1]), sys.argv[2])