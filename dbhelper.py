import mysql
import mysql.connector


class DB:
    def __init__(self):
        # connect to db
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database="flights_project"
            )
            self.my_cursor = self.conn.cursor()
            print("connection established")  # returns cursor object

        except:
            print("connection error")

    def fetch_city_names(self):
        city = []
        self.my_cursor.execute('''
        SELECT DISTINCT source FROM flights_project.flights
        UNION
        SELECT DISTINCT destination FROM flights_project.flights
        ''')
        data = self.my_cursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self, src, dest):
        rows = [("airline","route","dep_time","duration","price")]
        self.my_cursor.execute(f'''
        SELECT airline,route,dep_time,duration,price  from flights WHERE source = '{src}' and destination = '{dest}'
        
        ''')
        data = self.my_cursor.fetchall()

        for r in data:
            rows.append(r)
        # print(rows)
        return rows

    def fetch_airline_fr(self):
        airline = []
        fr = []
        self.my_cursor.execute('''
        SELECT airline, COUNT(*) FROM flights
        GROUP BY airline
        ''')
        data = self.my_cursor.fetchall()
        for d in data:
            airline.append(d[0])
            fr.append(d[1])
        return airline,fr

    def busy_airport(self):
        city = []
        fr = []
        self.my_cursor.execute('''
        with busy as (SELECT source FROM flights_project.flights union ALL SELECT destination FROM flights_project.flights)
        SELECT source , count(*) as "fr" FROM busy
        GROUP BY source 
        ORDER BY fr DESC
        ''')
        data = self.my_cursor.fetchall()
        for d in data:
            city.append(d[0])
            fr.append(d[1])

        return city,fr

    def daily_fr(self, airline):
        date = []
        fr = []
        self.my_cursor.execute(f'''
       SELECT date_of_journey ,COUNT(*) FROM flights 
       WHERE airline = '{airline}'
       GROUP BY Date_of_Journey''')
        data = self.my_cursor.fetchall()
        for d in data:
            date.append(d[0])
            fr.append(d[1])

        return date, fr

    def costly_airline(self):
        line = []
        price = []

        self.my_cursor.execute('''
        SELECT airline, round(AVG(price)) as price 
        FROM flights GROUP BY airline ORDER By price DESC''')
        data = self.my_cursor.fetchall()
        for d in data:
            line.append(d[0])
            price.append(d[1])

        return line[1:],price[1:]

    def duration_airlines(self):
        line = []
        time = []

        self.my_cursor.execute('''
        SELECT airline ,round(AVG(duration)) as duration 
        FROM flights GROUP BY airline ORDER By duration DESC''')
        data = self.my_cursor.fetchall()
        for d in data:
            line.append(d[0])
            time.append(d[1])

        return line[:], time[:]

        # my_cursor.execute('''
        # SELECT * from flights ORDER BY airline LIMIT 1
        # ''')
        # data = my_cursor.fetchall()
        # print(data)


if __name__ == "__main__":
    dbo = DB()
    dbo.fetch_city_names()
    dbo.fetch_all_flights(src="banglore",dest="delhi")
    dbo.fetch_airline_fr()
    dbo.busy_airport()
    dbo.daily_fr()