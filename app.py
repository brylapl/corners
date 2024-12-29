import streamlit as st
import psycopg2

# Wczytanie sekretnych danych z secrets.toml
db_config = st.secrets["postgresql"]

# Połączenie z bazą danych
conn = psycopg2.connect(
    dbname=db_config["dbname"],
    user=db_config["user"],
    password=db_config["password"],
    host=db_config["host"],
    port=db_config["port"]
)

# Przykład używania połączenia
cursor = conn.cursor()
cursor.execute("SELECT * FROM upcoming_match;")
rows = cursor.fetchall()

for row in rows:
    st.write(row)

# Zamknięcie połączenia
cursor.close()
conn.close()
