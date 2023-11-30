import mysql.connector
from convert_data import convert_tuples_to_dicts


conn = mysql.connector.connect(host='localhost', username='root', password='Nida85203014', database='ehms(python)')
my_cursor = conn.cursor()

my_cursor.execute("SELECT * FROM admin")
a_data = my_cursor.fetchall()

# my_cursor.execute("SELECT * FROM patients")
# p_data = my_cursor.fetchall()

# my_cursor.execute("SELECT * FROM doctors")
# d_data = my_cursor.fetchall()

A_Data = convert_tuples_to_dicts(a_data)
# P_Data = convert_tuples_to_dicts(p_data)
# D_Data = convert_tuples_to_dicts(d_data)
