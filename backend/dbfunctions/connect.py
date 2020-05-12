from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://backend:backendpw123@localhost/dimop'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM user', con=db_connection)
print(df.head())
