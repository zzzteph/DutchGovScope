from db import Scope, session

def get_latest_unscanned_or_oldest_scanned():
    """Retrieve the latest unscanned scope entry or, if none, the oldest scanned entry."""
    latest_unscanned = session.query(Scope).filter_by(scanned=False).order_by(Scope.created_at.desc()).first()
    
    if latest_unscanned:
        print(f"LATEST_SCOPE_ID={latest_unscanned.id}")
        print(f"LATEST_SCOPE_NAME={latest_unscanned.name}")
        print(f"LATEST_SCOPE_TYPE ={latest_unscanned.type}")
        return latest_unscanned
    
    oldest_scanned = session.query(Scope).filter_by(scanned=True).order_by(Scope.created_at.asc()).first()

    if oldest_scanned:
        print(f"LATEST_SCOPE_ID={oldest_scanned.id}")
        print(f"LATEST_SCOPE_NAME={oldest_scanned.name}")
        print(f"LATEST_SCOPE_TYPE ={oldest_scanned.type}")
        
        return oldest_scanned
    else:
        print("LATEST_SCOPE_ID=None")
        print("LATEST_SCOPE_NAME=None")
        print("LATEST_SCOPE_TYPE=None")
        return None

if __name__ == "__main__":
    get_latest_unscanned_or_oldest_scanned()