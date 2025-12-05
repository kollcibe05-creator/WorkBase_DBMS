from sqlalchemy import Column, Integer, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import date
from .__init__ import Base

class Review(Base):
    __tablename__ = 'reviews'

    # Attributes defined using Column
    id = Column(Integer, primary_key=True)
    rating = Column(Integer) # e.g., 1-5
    content = Column(Text)
    review_date = Column(Date, default=date.today)

    # Foreign Keys for the two Many-to-One relationships
    reviewee_id = Column(Integer, ForeignKey('employees.id'))
    reviewer_id = Column(Integer, ForeignKey('employees.id'))

    # Relationships
    # Many-to-One: Review <-> Reviewee (Employee)
    reviewee = relationship(
        "Employee", 
        foreign_keys=[reviewee_id], 
        back_populates="received_reviews",
        # Use primaryjoin to distinguish the two relationships to 'Employee'
        primaryjoin="Review.reviewee_id == Employee.id" 
    )
    
    # Many-to-One: Review <-> Reviewer (Employee)
    reviewer = relationship(
        "Employee", 
        foreign_keys=[reviewer_id], 
        back_populates="given_reviews",
        primaryjoin="Review.reviewer_id == Employee.id"
    )

    def __repr__(self):
        return f"<Review(id={self.id}, rating={self.rating}, reviewee_id={self.reviewee_id})>"