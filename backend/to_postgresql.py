from sqlalchemy import create_engine
import pandas as pd
import webscrape as ws

# PostgreSQL database URI using default 'postgres' user
postgres_uri = "postgresql://newuser:password@localhost:5433/usports"

# Create an SQLAlchemy engine connected to 'postgres' database
engine = create_engine(postgres_uri)

team_table = ws.TeamUpdateAtk(2024)
player_table = ws.PlayerUpdateAtk(2024)

team_table.to_sql("Teams", engine, if_exists='replace', index=False)

# df.to_sql(table_name, engine, if_exists='replace', index=False)
# Establish a connection and execute the SQL command
# with engine.connect() as connection:
#     connection.execute(create_db_sql)
