import psycopg2
conn=psycopg2.connect(database="postgres",user="postgres",password="12345")
print("database is connected")
cursor=conn.cursor()
c1="""delete  from name where customer_name = 'Gokul' ;"""
cursor.execute(c1)
conn.commit()
