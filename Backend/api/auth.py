from fastapi import Depends, HTTPException, Security
from sqlalchemy.orm import Session
from api.dependencies import get_db
from api.services import get_admin_user

def verify_admin(db: Session = Depends(get_db)):
    admin_user = get_admin_user(db)
    if not admin_user:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return admin_user
