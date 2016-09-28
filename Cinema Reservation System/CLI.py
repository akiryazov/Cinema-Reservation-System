import sqlite3
import sys

conn = sqlite3.connect('cinemasystem.db')
c = conn.cursor()
hall = [['.' for x in range(10)] for y in range(10)]
dictionary = {}


class CLI():

    def __init__(self):
        self._command1 = sys.argv[1]

    def show_movies(self):
        if self._command1 == "show_movies":
            for row in c.execute("""SELECT * FROM Movies ORDER BY rating DESC"""):
                print(row)
        else:
            return "Invalid command!"

    def make_halls(self):
        for row in c.execute("""SELECT a.name, b.time
                                    FROM movies AS a
                                    JOIN projections AS b
                                    ON a.id = b.movie_id
                                    """):
            dictionary[row] = hall

    def show_movie_projections(self):
        if self._command1 == "show_movie_projections":
            arguments = (sys.argv[2], sys.argv[3],)
            for row in c.execute("""SELECT a.name,b.date, b.time, b.type
                                    FROM movies AS a
                                    JOIN projections AS b
                                    ON a.id = b.movie_id
                                    WHERE a.id = ?
                                    AND b.date = ?
                                    """, arguments):
                print(row)
                dictionary[row] = hall
                for row_number in range(0, len(dictionary[row])):
                    print(dictionary[row][row_number])
        else:
            return "Invalid command!"

    def make_reservation(self):
        if self._command1 == "make_reservation":
            name = input("Choose name: ")
            tickets = input("Choose the number of tickets: ")
            for row in c.execute("""SELECT * FROM Movies"""):
                print(row)
            chosen_movie = input("Choose the movie number: ")
            arguments = (chosen_movie,)
            for row in c.execute("""SELECT a.name,b.date, b.time, b.type
                                    FROM movies AS a
                                    JOIN projections AS b
                                    ON a.id = b.movie_id
                                    WHERE a.id = ?
                                    """, arguments):
                print(row)
                movie = row
            self.make_halls()
            hour = input("Choose an hour: ")
            for key in dictionary:
                if hour in key:
                    for element in range(0,len(dictionary[key])):
                        print(dictionary[key][element])
                    reserved_tickets = 0
                    seats = []
                    while reserved_tickets < int(tickets):
                        seat = input("Choose a seat: ")
                        if dictionary[key][int(seat[1]) - 1][int(seat[3]) - 1] == 'X':
                            print("Seat is taken! Choose another one")
                            continue
                        else:
                            seats.append(seat)
                            dictionary[key][    
                                int(seat[1]) - 1][int(seat[3]) - 1] = 'X'
                            reserved_tickets += 1
            print("This is your reservation:")
            print("Movie: " + movie[0])
            print("Date and time: " + movie[1] + " " + movie[2] + " " + str((movie[3])))
            for seat in seats:
                print(seat)
            finalize = input("Confirm - type 'finalize': ")
            print("Thanks!")


interface = CLI()
# print(interface.show_movies())
# print(interface.show_movie_projections())
print(interface.make_reservation())
