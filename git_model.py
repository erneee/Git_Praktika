from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
