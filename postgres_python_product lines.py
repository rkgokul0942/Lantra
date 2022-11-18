import psycopg2
conn=psycopg2.connect(database="postgres",user="postgres",password="12345")
cursor=conn.cursor()

#creating a table
cursor.execute("""create table productlines(productline text,textDescription text,htmlDescription text, image text)""")

#inserting values
insert="""insert into productlines(productline,textDescription,htmlDescription,image) values ('one', 'bottle','bottle_cap','square_bottle'),
('two','three','four','five')"""
cursor.execute(insert)
cursor.execute("""select * from productlines """)
v=cursor.fetchall()
print(v)

#updating tables
update="""update  productlines set productline = 'ten' where productline = 'one'"""
cursor.execute(update)
cursor.execute("""select * from productlines """)
v=cursor.fetchall()
print(v)

#deleting column
del_det="""delete from productlines where productline='two'"""
cursor.execute(del_det)
cursor.execute("""select * from productlines """)
v=cursor.fetchall()
print(v)

#droping the table
cursor.execute("drop table productlines")
conn.commit()
print("Your code is now executed")