from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import relationship
from .__init__ import Base, Session # Import Session and Base

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    location = Column(String(100))
    employees = relationship(
        "Employee", 
        back_populates="department", 
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        # Adjusted for clearer output in the CLI
        return f"<Department ID: {self.id}, Name: {self.name}, Location: {self.location}>"

    # --- CRUD CLASS METHODS (Query/Create) ---

    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.scalars(select(cls)).all()

    @classmethod
    def find_by_id(cls, id_):
        with Session() as session:
            # session.get() handles primary key lookups
            return session.get(cls, int(id_)) 

    @classmethod
    def find_by_name(cls, name):
        with Session() as session:
            stmt = select(cls).where(cls.name == name)
            return session.scalar(stmt) # scalar returns one result or None

    @classmethod
    def create(cls, name, location):
        with Session() as session:
            dept = cls(name=name, location=location)
            session.add(dept)
            session.commit()
            return dept

    # --- CRUD INSTANCE METHODS (Update/Delete) ---

    def update(self):
        with Session() as session:
            # Use merge to attach the detached instance to the new session
            session.merge(self) 
            session.commit()
            return self

    def delete(self):
        with Session() as session:
            # Use merge to attach before deleting
            session.delete(session.merge(self))
            session.commit()