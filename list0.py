import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# движок, отвечающий за передачу команд от Python к ДБ и обратно
engine = create_engine(os.getenv("DATABASE_URL"))
# создает сессию
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == '__main__':
    main()        
