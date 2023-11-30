import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='Nida85203014', database='ehms')
my_cursor = conn.cursor()

my_cursor.execute("SELECT * FROM admin")
data = my_cursor.fetchall()

def convert_Atuples_to_dicts(data):
    # Create an empty list to store the dictionaries
    dicts = []

    # Iterate through the list of tuples
    for info in data:
        # Create a dictionary from the current tuple
        dict = {}
        for i, value in enumerate(info):
            dict[headers[i]] = value

        # Add the dictionary to the list of dictionaries
        dicts.append(dict)
    return dicts
    
def convert_tuples_to_dicts(data):
    # Create an empty list to store the dictionaries
    dicts = []

    # Iterate through the list of tuples
    for info in data:
        # Create a dictionary from the current tuple
        dict = {}
        for i, value in enumerate(info):
            dict[header[i]] = value

        # Add the dictionary to the list of dictionaries
        dicts.append(dict)

    return dicts
def find(dicts, username, email, pw):
    for x in dicts:
        if x['Email'] != email:
            return "email"
        elif x['Email'] == email:
            if x['Username'] == username and x['Password'] == pw:
            # print(x)
                return True
            return "username"
    # return False
            # return x
# Example usage
headers = ["ID", "Username","Email", "Password"]
header = ["ID", "Username", "Gender", "Email", "Password", "Age", "Department", "Phone_Number", "Pic"]
# tuples = [("John", 30, "New York"), ("Jane", 25, "Los Angeles")]
# dicts = convert_tuples_to_dicts(data)