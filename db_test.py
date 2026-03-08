from sqlalchemy import create_engine

username = "system"
password = "cscorner"
host = "localhost"
port = 1521
service_name = "orclpdb"

engine = create_engine(
    f"oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}"
)

with engine.connect() as connection:
    print("✅ Connected successfully to Oracle!")
    