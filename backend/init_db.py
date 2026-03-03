from sqlalchemy import create_engine, text
from models import Base

engine = create_engine("sqlite:///homestack.db", echo=True)

# Enable foreign key enforcement for SQLite
with engine.connect() as conn:
    conn.execute(text("PRAGMA foreign_keys=ON"))

Base.metadata.create_all(engine)

print("Database tables created successfully.")