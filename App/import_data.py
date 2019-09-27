import csv
import json
import psycopg2
from config import config



def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
	        CREATE TABLE Information (
				key varchar(15) NOT NULL,
				place_name varchar(35) NOT NULL,
				admin_name1 varchar(35) NOT NULL,
				latitude real,
				longitude real,
				accuracy varchar(5));
		""",
        """
	        CREATE TABLE Boundary (
				name varchar(35),
				type varchar(35),
				parent varchar(35),
				latitude double precision,
				longitutde double precision);
		"""

        )
    conn = None
    try:
    	# read the connection params
    	params = config()
    	# connecting to postgreSQL server
    	conn = psycopg2.connect(user="postgres",
							password="postgres",
							host = "172.30.0.2",
							port = "5432",
							database = "postgres")
    	curr = conn.cursor()
    	for command in commands:
    		curr.execute(command)
    	curr.close()
    	conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		# if conn is not None:
		conn.close()

def import_csv():
	"""Imports the CSV files into the database"""

	with open('data.csv', 'r') as f:
		reader = csv.reader(f)
		next(reader) # Skip the header row.
		for row in reader:
			curr.execute(
			"INSERT INTO Information VALUES (%s, %s, %s, %s)",
			row
			)
		conn.commit()


def import_json():
	"""Imports the Json files into the database"""

	with open('geojson.json') as file:
    	json_data = json.load(file)

    for data in json_data['features']:

    	name = data['properties']['name']
    	parent = data['properties']['parent']
    	loc_type = data['properties']['type']

    	for coordinate in data['geometry']['coordinates'][0]:
    		longitutde = coordinate[0]
    		latitude = coordinate[1]

    		cur.execute("INSERT INTO boundary (name,type,parent,latitude,longitude) VALUES ('"+name+"','"+loc_type+"','"+parent+"',"+str(lat)+","+str(lng)")




 if __name__ == '__main__':
 	create_tables()
 	import_csv()
 	import_json()