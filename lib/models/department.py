from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import relationship
from .__init__ import Base, Session 

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
        return f"<Department ID: {self.id}, Name: {self.name}, Location: {self.location}>"


    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.scalars(select(cls)).all()

    @classmethod
    def find_by_id(cls, id_):
        with Session() as session:
            return session.get(cls, int(id_)) 

    # def find_by_name_raw(name):
    # connection = engine.connect()
    # result = connection.execute(text("SELECT * FROM departments WHERE name = :name"), {"name": name}).fetchone()
    # return result
    @classmethod
    def find_by_name(cls, name):
        with Session() as session:
            stmt = select(cls).where(cls.name == name)
            return session.scalar(stmt)

    @classmethod
    def create(cls, name, location):
        with Session() as session:
            dept = cls(name=name, location=location)
            session.add(dept)
            session.commit()
            dept_id = dept.id
            return dept_id


    def update(self):
        with Session() as session:
            session.merge(self) 
            session.commit()
            return self

    def delete(self):
        with Session() as session:
            session.delete(session.merge(self))
            session.commit()