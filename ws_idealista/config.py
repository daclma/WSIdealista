import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///ws_idealista.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True