import getpass
import oracledb

connection = oracledb.connect(
    user="GROUP2",
    password='4Z2bbVtVnt',
    dsn="140.117.69.60/ORCLPDB1")

print("Successfully connected to Oracle Database")
cursor = connection.cursor()