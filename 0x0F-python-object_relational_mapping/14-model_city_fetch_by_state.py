#!/usr/bin/python3
"""Start link class to table in database """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State.name, City.id, City.name).join(City).all()

    for p in res:
        print(f'{p[0]}: ({p[1]}) {p[2]}')
    session.commit()
