from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from .__init__ import Base

class Employee(Base):
    __tablename__ = 'employees'

    # Attributes defined using Column
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    hire_date = Column(Date, default=date.today)
    salary = Column(Integer)

    # Foreign Key for Many-to-One
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Relationships
    # Many-to-One: Employee belongs to one Department
    department = relationship("Department", back_populates="employees")
    
    # One-to-Many (Reviewee): Employee is reviewed many times
    received_reviews = relationship(
        "Review", 
        foreign_keys="[Review.reviewee_id]", 
        back_populates="reviewee", 
        cascade="all, delete-orphan"
    )
    
    # One-to-Many (Reviewer): Employee gives many reviews
    given_reviews = relationship(
        "Review", 
        foreign_keys="[Review.reviewer_id]", 
        back_populates="reviewer", 
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.first_name} {self.last_name}')>"