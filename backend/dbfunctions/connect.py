from sqlalchemy import create_engine

def connect_db():
    db_connection_str = 'mysql+pymysql://backend:backendpw123@localhost/dimop'
    db_connection = create_engine(db_connection_str)

    return db_connection
