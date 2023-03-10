import sqlite3

db_connection = sqlite3.connect('ejecicio11.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Estudiantes(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Estudiantes VALUES(1,'Juan', 'de Dios')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(2,'Aniel', 'Ramirez')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(3,'Victor', 'Peñar')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(4,'Sandro', 'mosquea')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(5,'Mell', 'garcias')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(6,'Carla', 'Garvan')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(7,'Rafael', 'tavarez')")
db_cursor.execute("INSERT INTO Estudiantes VALUES(8,'Sambel', 'cometoto')")

db_connection.commit()
db_cursor.execute("SELECT * FROM Estudiantes")

todo = db_cursor.fetchall()
print(todo)
db_connection.close()