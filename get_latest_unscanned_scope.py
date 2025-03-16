from db import Scope, session

def get_latest_unscanned_scope():
    """Retrieve the newest scope entry that has not been scanned."""
    latest_unscanned = session.query(Scope).filter_by(scanned=False).order_by(Scope.created_at.desc()).first()
    
    if latest_unscanned:
        print(f"LATEST_SCOPE_ID={latest_unscanned.id}")
        print(f"LATEST_SCOPE_NAME={latest_unscanned.name}")
        return latest_unscanned
    else:
        print("No unscanned scope entries found.")
        return None

if __name__ == "__main__":
    get_latest_unscanned_scope()