import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HOST:YOUR_PORT_NUMBER/YOUR_DATABASE_NAME'
db = create_engine(conn_string)
conn = db.connect()

files = ['customer','credit_card']

for file in files:
        df = pd.read_csv(f'YOUR_DIRECTORY_OF_CSV_FILES/{file}.csv')
        df.to_sql(file, con=conn, if_exists='replace', index=False)
