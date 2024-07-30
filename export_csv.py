import pandas as pd
import pymysql

# Database connection parameters
host = '192.168.0.101'
user = 'egt209'
password = 'egt209'
database = 'mydb'

# Establish connection to the database
connection = pymysql.connect(host=host, user=user, password=password, database=database)

# SQL query you want to export
query = "SELECT * FROM t4g1"

# Using pandas to read the query result into a DataFrame
df = pd.read_sql(query, connection)

# Specify the path and name of the CSV file to write to
csv_file_path = 'output_data.csv'

# Write DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)  # Set index=False to exclude row indices in the CSV file

# Close the database connection
connection.close()

print("Data exported to CSV successfully.")
