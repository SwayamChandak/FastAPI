from db import get_session

def get_db():
    db = get_session()
    if db is None:
        raise RuntimeError("Database session is not initialized. Ensure init_db() is called first.")
    try:
        yield db
    finally:
        db.close()