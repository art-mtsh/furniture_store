import os
import django
from django.db import connections

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()



# Check connection
try:
    connection = connections['default']
    cursor = connection.cursor()

    # Check if the test table exists, if not, create it
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """)


    print("Successfully connected to the database!")
    cursor.close()
except Exception as e:
    print(f"Failed to connect to the database: {e}")
