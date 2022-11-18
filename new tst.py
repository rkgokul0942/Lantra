import psycopg2
conn = psycopg2.connect(
    database = "",
    user = "postgres",
    password = "12345"
)
print("successfully")