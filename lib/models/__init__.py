

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


database = 'sqlite:///workbase.db' 


engine = create_engine(database)


Base = declarative_base()

Session = sessionmaker(bind=engine)

def recreate_db():
    """Drops all tables and creates them based on the new Base metadata."""

    Base.metadata.drop_all(engine)        
    Base.metadata.create_all(engine)