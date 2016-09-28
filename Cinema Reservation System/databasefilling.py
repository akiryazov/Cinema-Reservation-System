import sqlite3
conn = sqlite3.connect('cinemasystem.db')

c = conn.cursor()
c.execute('''
CREATE TABLE Movies
(id int, name varchar, rating double)''')
c.execute("INSERT INTO Movies VALUES (1, 'The Hunger Games: Catching Fire', 7.9)")
c.execute("INSERT INTO Movies VALUES (2, 'Wreck-It Ralph', 7.8)")
c.execute("INSERT INTO Movies VALUES (3, 'Her', 8.3)")

c.execute('''
CREATE TABLE Projections
(id int, movie_id int, type varchar, date varchar, time varchar,
FOREIGN KEY(movie_id) REFERENCES movies(id))''')
c.execute("INSERT INTO Projections VALUES (1, 1, '3D', '2014-04-01', '19:10')")
c.execute("INSERT INTO Projections VALUES (2, 1, '2D', '2014-04-01', '19:00')")
c.execute("INSERT INTO Projections VALUES (3, 1, '4DX', '2014-04-02', '21:00')")
c.execute("INSERT INTO Projections VALUES (4, 3, '2D', '2014-04-05', '20:20')")
c.execute("INSERT INTO Projections VALUES (5, 2, '3D', '2014-04-02', '22:00')")
c.execute("INSERT INTO Projections VALUES (6, 2, '2D', '2014-04-02', '19:30')")
c.execute("INSERT INTO Projections VALUES (7, 3, '3D', '2014-04-03', '19:30')")

c.execute('''
CREATE TABLE Reservations
(id int, username varchar, projection_id int, row int, col int,
FOREIGN KEY(projection_id) REFERENCES projections(id))''')
c.execute("INSERT INTO Reservations VALUES (1, 'RadoRado', 1, 2, 1)")
c.execute("INSERT INTO Reservations VALUES (2, 'RadoRado', 1, 3, 5)")
c.execute("INSERT INTO Reservations VALUES (3, 'RadoRado', 1, 7, 8)")
c.execute("INSERT INTO Reservations VALUES (4, 'Ivo', 3, 1, 1)")
c.execute("INSERT INTO Reservations VALUES (5, 'Ivo', 3, 1, 2)")
c.execute("INSERT INTO Reservations VALUES (6, 'Mysterious', 5, 2, 3)")
c.execute("INSERT INTO Reservations VALUES (7, 'Mysterious', 5, 2, 4)")

conn.commit()
conn.close()
