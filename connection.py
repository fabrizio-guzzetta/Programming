from mysql import connector

connect = connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
    )


# cursor = connect.cursor()

# product_id = 1

# # test = cursor.execute(f"SELECT * FROM prodotti WHERE id ={product_id}")

# # prodotti = cursor.fetchall()
# # prodotti = cursor.fetchone()

# # print('prodotti', prodotti)

# # query = """UPDATE prodotti SET prezzo = %s WHERE id = %s"""
# # values = (56, 3)
# # cursor.execute(query, values)

# # connection.commit()
# # last_id = cursor.lastrowid
# # test = cursor.execute("SELECT * FROM prodotti WHERE id = 3")
# # prodotto = cursor.fetchone()
# # print('prodotto', prodotto)

# query = "DELETE FROM prodotti WHERE id = %s"
# values = [2]
# cursor.execute(query, values)

# connect.commit()
# last_id = cursor.lastrowid
# test = cursor.execute("SELECT * FROM prodotti WHERE id = 3")
# prodotto = cursor.fetchone()
# print('prodotto', prodotto)
# cursor.close()
# connect.close()
