from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Base de données
DATABASE_URL = "sqlite:///./test.db"  # Utilisation d'une base de données SQLite pour l'exemple
Base = declarative_base()

# Modèle de la table User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    identifiant = Column(String, unique=True, index=True, nullable=False)
    motdepasse = Column(String, nullable=False)
    scoreMax = Column(Integer, nullable=True)

# Modèle de la table PartieAmis
class PartieAmis(Base):
    __tablename__ = 'partie_amis'
    id_partie = Column(Integer, primary_key=True, index=True)
    idUser1 = Column(Integer, ForeignKey('users.id'), nullable=False)
    idUser2 = Column(Integer, ForeignKey('users.id'), nullable=False)
    pointsUser1 = Column(Integer, nullable=True)
    pointsUser2 = Column(Integer, nullable=True)

# Fonction pour initialiser la base de données
def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    return engine

# Fonction pour obtenir une session
def get_session(engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()
