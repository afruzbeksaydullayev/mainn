import psycopg2

conn = None
cur = None

try:
    with psycopg2.connect(
        database='postgres',
        user='postgres',
        password='123',
        host='localhost',
        port=5432
    ) as conn:
        with conn.cursor() as cur:
            select_product_query = """ select * from Product7; """
            cur.execute(select_product_query)
            insert_into_query = """insert into Product7(name,price,color,image) values (%s,%s,%s,%s)"""
            insert_data_list = [('pen',2,'black','https://www.bing.com/search?q=pen&form=ANNTH1&refig=56ca3ae42d9a42f89c6fecaba873b36a&pc=HCTS'), ('car',300,'blue','https://th.bing.com/th/id/OIP.6Oes0YCJhykm-Te8wb4Q7AHaFj?w=243&h=182&c=7&r=0&o=5&dpr=1.3&pid=1.7'), ('soap',12,'white','https://www.bing.com/images/search?q=soap&qs=n&form=QBIR&sp=-1&lq=0&pq=soap&sc=10')]
            cur.executemany(insert_into_query, insert_data_list)
            # cur.execute(insert_into_query, insert_data)
            conn.commit()

except psycopg2.OperationalError as e:
    print(e)


else:
    print('Successfully inserted')
    pass


  CREATE TABLE
create_table_product7 = """create table if not exists Product7
(
    id serial PRIMARY KEY,
    name varchar(50) not null,
    price float not null,
    image varchar (35) not null
);
"""




       #VARIAN--2
    # INSERT PRODUCTS
def insert_query_product():
    insert_into_query = """insert into Product7 (name,price,color,image)
    values (%s,%s,%s,%s)
    """
    insert_multiple_rows = [('flower',22,'yellow','http/samirflowers'), ('water',5,'white,','http/water.com'), ('phone',300,'white','http/phone.net')]
    for record in insert_multiple_rows:
        cur.execute(insert_into_query,record)
    conn.commit()

    cur.close()
    conn.close()
    print("Product inserted successfully")

insert_query_product()


   #  DELETE

def delete_query_product(id):
    delete_into_query = """delete from Product7 where id = %s;"""

    cur.execute(delete_into_query, (id,))
    conn.commit()
    cur.close()
    conn.close()
    print('Product Deleted')

delete_query_product(7)

     # UPDATE


def update_query_product(id, name):
    update_query = """update Product7 set name = %s where id = %s;"""
    data = (name ,id )
    cur.execute(update_query, data)
    conn.commit()

update_query_product(1,'Toy')

   # SELECT ALL OR SELECT ONE

select_car_query = '''select * from Product7 ;'''
cur.execute(select_car_query)
for user in cur.fetchall(): #----> OR fetchone
    print(user)