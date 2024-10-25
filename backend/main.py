from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from db_management import init_db, get_session, User as UserSQL, PartieAmis as PartieAmisSQL

# Initialiser l'application FastAPI
app = FastAPI()

# Initialiser la base de données et la session
engine = init_db()

# Modèles Pydantic pour les utilisateurs et les parties
class User(BaseModel):
    id: Optional[int] = None
    identifiant: str
    motdepasse: str
    scoreMax: Optional[int] = 0

class PartieAmis(BaseModel):
    id_partie: Optional[int] = None
    idUser1: int
    idUser2: int
    pointsUser1: Optional[int] = 0
    pointsUser2: Optional[int] = 0

# Dépendance pour obtenir une session de base de données
def get_db():
    db = get_session(engine)
    try:
        yield db
    finally:
        db.close()

# Routes pour les utilisateurs
@app.post("/users", response_model=User)
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = UserSQL(identifiant=user.identifiant, motdepasse=user.motdepasse, scoreMax=user.scoreMax)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Mettre à jour les attributs de l'utilisateur
    db_user.identifiant = user.identifiant
    db_user.motdepasse = user.motdepasse
    db_user.scoreMax = user.scoreMax

    db.commit()  # Valider les changements dans la base de données
    db.refresh(db_user)  # Rafraîchir l'instance de l'utilisateur pour inclure les changements
    return db_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserSQL).filter(UserSQL.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session =Depends(get_db)):
    user = db.query(UserSQL).filter(UserSQL. id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}

# Routes pour les parties
@app.post("/parties", response_model=PartieAmis)
def create_partie(partie: PartieAmis, db: Session = Depends(get_db)):
    db_partie = PartieAmisSQL(
        idUser1=partie.idUser1,
        idUser2=partie.idUser2,
        pointsUser1=partie.pointsUser1,
        pointsUser2=partie.pointsUser2
    )
    db.add(db_partie)
    db.commit()
    db.refresh(db_partie)
    return db_partie

@app.get("/parties/{partie_id}", response_model=PartieAmis)
def get_partie(partie_id: int, db: Session = Depends(get_db)):
    partie = db.query(PartieAmisSQL).filter(PartieAmisSQL.id_partie == partie_id).first()
    if not partie:
        raise HTTPException(status_code=404, detail="Partie not found")
    return partie

@app.delete("/parties/{partie_id}")
def delete_partie(partie_id: int, db: Session = Depends(get_db)):
    partie = db.query(PartieAmisSQL).filter(PartieAmisSQL.id_partie == partie_id).first()
    if not partie:
        raise HTTPException(status_code=404, detail="Partie not found")
    db.delete(partie)
    db.commit()
    return {"message": "Partie deleted successfully"}
