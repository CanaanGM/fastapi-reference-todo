from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


env_values = dotenv_values(".env")

engine = create_engine(env_values.get("POSTGRES_CONNECTION"))


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as ex:
        print(ex)
    finally:
        db.close()
