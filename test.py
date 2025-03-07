import mysql.connector

try:
    print("🚀 Trying to connect to MySQL...")  # Debugging Step 1

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hit_db-demo",
        connect_timeout=5  # ✅ ৫ সেকেন্ড পর কানেকশন ব্যর্থ হবে
    )

    print("✅ Connection successful!")  # Debugging Step 2

    conn.close()
    print("🔄 Connection closed successfully.")  # Debugging Step 3

except mysql.connector.Error as err:
    print(f"❌ Connection failed: {err}")  # Debugging Step 4
