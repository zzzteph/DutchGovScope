from db import Scope, session
from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)

def get_latest_unscanned_or_oldest_scanned():
 
    oldest_scanned = session.query(Scope).order_by(Scope.updated_at.asc()).first()

    if oldest_scanned:
        print(f"LATEST_SCOPE_ID={oldest_scanned.id}")
        print(f"LATEST_SCOPE_NAME={oldest_scanned.name}")
        print(f"LATEST_SCOPE_TYPE ={oldest_scanned.type}")
        oldest_scanned.updated_at = utc_now()
        session.commit()
        return oldest_scanned
    else:
        print("LATEST_SCOPE_ID=None")
        print("LATEST_SCOPE_NAME=None")
        print("LATEST_SCOPE_TYPE=None")
        return None

if __name__ == "__main__":
    get_latest_unscanned_or_oldest_scanned()