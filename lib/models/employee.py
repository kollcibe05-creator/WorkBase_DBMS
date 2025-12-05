from sqlalchemy import Column, Integer, String, Date, ForeignKey, select, func
from sqlalchemy.orm import relationship
from datetime import date
from .__init__ import Base, Session

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    hire_date = Column(Date, default=date.today)
    salary = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates="employees")
    

    received_reviews = relationship(
        "Review", foreign_keys="[Review.reviewee_id]", back_populates="reviewee", cascade="all, delete-orphan"
    )
    given_reviews = relationship(
        "Review", foreign_keys="[Review.reviewer_id]", back_populates="reviewer", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Employee ID: {self.id}, Name: {self.first_name} {self.last_name}, Dept ID: {self.department_id}>"


    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.scalars(select(cls)).all()

    @classmethod
    def find_by_id(cls, id_):
        with Session() as session:
            return session.get(cls, int(id_)) 

    @classmethod
    def find_by_full_name(cls, first_name, last_name):
        with Session() as session:
            stmt = select(cls).where(
                cls.first_name == first_name, 
                cls.last_name == last_name
            )
            return session.scalar(stmt)

    @classmethod
    def create(cls, first_name, last_name, salary, department_id):
        with Session() as session:
            employee = cls(
                first_name=first_name, 
                last_name=last_name, 
                salary=salary, 
                department_id=department_id
            )
            session.add(employee)
            session.commit()
            return employee

    def update(self):
        with Session() as session:
            session.merge(self)
            session.commit()
            return self

    def delete(self):
        with Session() as session:
            session.delete(session.merge(self))
            session.commit()