#!/usr/bin/python3
"""
    This module contains a script that prints the first State object
    from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    name = session.query(State).first()
    if name is None:
        print("Nothing")
    else:
        print(name.id, name.name, sep=": ")
