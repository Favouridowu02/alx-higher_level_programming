#!/usr/bin/python3
"""
    a script that prints all City objects from the
    database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id)):
        print(row[0] + ": (" + str(row[1]) + ") " + row[2])
