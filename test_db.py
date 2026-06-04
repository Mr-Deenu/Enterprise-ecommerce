from src.database.database import engine

try:
    connection = engine.connect()
    print("✅ Database connected successfully!")
except Exception as e:
    print("❌ Connection failed")
    print(e)