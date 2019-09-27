import psycopg2
from fastapi import FastAPI
from schemas import Information
from math import radians, sin, cos, acos

app = FastAPI()


#Todo: Update the url params
@app.get("/get_location")
def get_location():
	conn = psycopg2.connect(user="postgres",
							password="postgres",
							host = "172.30.0.2",
							port = "5432",
							database = "postgres")
	cur = conn.cursor()
	cur.execute("""SELECT key, address, city
					FROM Information WHERE lat="+Info.lat+" AND 
					long="+Info.long+"
					;
				""")
	fetch = cur.fetchone()
	result = ""
	pin = pincode
	cur.close()
	conn.commit()
	return {"message": result}


#Todo: Update the Query
@app.post("/post_location")
def post_location(Info:Information):
	conn = psycopg2.connect(user="postgres",
							password="postgres",
							host = "172.30.0.2",
							port = "5432",
							database = "postgres")
	cur = conn.cursor()

	cur.execute("""SELECT * FROM Information WHERE key="+pincode+" OR 
					earth_distance(ll_to_earth("+lat+","+lng+"), ll_to_earth(Information.latitude, apitest.longitude)) <1000;
				""")
	fetch = cur.fetchone()

	if cur.rowcount>0:	
		result = "Entry alerady exists in database"
		print("Entry already exists in database or lat and lng nearly equal to some intial data")
	else:
		cur.execute("""INSERT INTO Information 
        				(key, place_name, admin_name1, latitude, longitude, accuracy) 
        				VALUES ('"+pin+"','"+address+"','"+city+"',"+lat+","+lng+",'')
        			""");
		result = "Data added to database"


#Todo: Update the url params
@app.get("/get_using_postgres")
def get_using_postgres():
	points = []
	conn = psycopg2.connect(user="postgres",
							password="postgres",
							host = "172.30.0.2",
							port = "5432",
							database = "postgres")
	cur = conn.cursor()

	#filter points withing range
	cursor.execute("SELECT * FROM Information WHERE earth_box(ll_to_earth(%s, %s), %s) @> ll_to_earth(Information.latitude, Information.longitude)"% (lat, lng, radius))
	res = cursor.fetchall()

	for row in res:
		points.append(row[0]) 


#Todo: Update the url params
@app.get("/get_using_self")
def get_using_self():
	conn = psycopg2.connect(user="postgres",
							password="postgres",
							host = "172.30.0.2",
							port = "5432",
							database = "postgres")
	cur = conn.cursor()
	cur.execute("select * from Information")
	rows = cursor.fetchall()
	points = []
	for row in rows:

		row_lat = row[3]
		row_lng = row[4]

		#calculating if point is within the given radius
		lat1 = radians(float(lat))
		lat2 = radians(float(row_lat))

		lat_diff = radians(float(row_lat) - float(lat))
		lng_diff = radians(float(row_lng) - float(lng))

		A = sin( lat_diff/2 )*sin( lat_diff/2 ) + cos(lat1)*cos(lat2) * sin( lng_diff/2 )*sin( lng_diff/2 )
		C = 2 * atan2(sqrt(A), sqrt((1 - A)))
		distance = R * C

		if distance < float(radius):
			points.append(row[0])
	return jsonify({'result': points})


    