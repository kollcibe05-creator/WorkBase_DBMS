from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .__init__ import Base

class Department(Base):
    __tablename__ = 'departments'

    # Attributes defined using Column
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    location = Column(String(100))

    # Relationship: One-to-Many (Department has many Employees)
    employees = relationship(
        "Employee", 
        back_populates="department", 
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"