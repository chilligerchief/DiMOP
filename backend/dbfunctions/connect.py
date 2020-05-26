from sqlalchemy import create_engine

def connect_db():
    db_connection_str = 'mysql+pymysql://milena:ALAQsM8W@132.187.102.201/dimop'
    db_connection = create_engine(db_connection_str)

    return db_connection
