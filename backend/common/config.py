import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

class Settings:
    
    DB_USERNAME : str = os.getenv("MARIADB_USERNAME")
    DB_PASSWORD : str = os.getenv("MARIADB_PASSWORD")
    DB_HOST     : str = os.getnenv("MARIADB_HOST", "localhost")
    DB_PORT     : str = os.getnenv("MARIADB_PORT", 3306)
    DB_DATABASE : str = os.getenv("MARIADB_DATABASE")

    DATABASE_URL = f"mariadb+pymysql:/{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"