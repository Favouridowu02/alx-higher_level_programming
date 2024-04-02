#!/usr/bin/python3
"""
    This Module contains a script that prints the state object
    with the name passed as argument from the database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session=Session()
    
    substring = argv[4]
    row = session.query(State).filter(State.name.like(f"%{substring}%"))
    if row is None:
        print("Not found")
    else:
        print(row[0].id)
