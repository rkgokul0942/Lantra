import psycopg2
conn=psycopg2.connect(database="postgres",user="postgres",password="12345")
print("Your db is now connected")
cursor=conn.cursor()

insert="""insert into productlines(productline,textDescription,htmlDescription,image) values (one, bottle,bottle_cap,square bottle"""
cursor.execute(insert)
update="""update table productlines set productline = 'two' where productline = 'one'"""
conn.commit()
