from sqlalchemy import Column, Integer, Date, ForeignKey, Text, select
from sqlalchemy.orm import relationship
from datetime import date
from .__init__ import Base, Session

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer) 
    content = Column(Text)
    review_date = Column(Date, default=date.today)
    reviewee_id = Column(Integer, ForeignKey('employees.id'))
    reviewer_id = Column(Integer, ForeignKey('employees.id'))

    # Relationships remain the same for ambiguity resolution
    reviewee = relationship(
        "Employee", foreign_keys=[reviewee_id], back_populates="received_reviews", 
        primaryjoin="Review.reviewee_id == Employee.id" 
    )
    reviewer = relationship(
        "Employee", foreign_keys=[reviewer_id], back_populates="given_reviews", 
        primaryjoin="Review.reviewer_id == Employee.id"
    )

    def __repr__(self):
        return f"<Review ID: {self.id}, Rating: {self.rating}, Reviewee: {self.reviewee_id}>"
    
    # --- CRUD CLASS METHODS (Query/Create) ---

    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.scalars(select(cls)).all()

    @classmethod
    def find_by_id(cls, id_):
        with Session() as session:
            return session.get(cls, int(id_)) 

    @classmethod
    def create(cls, reviewee_id, reviewer_id, rating, content):
        with Session() as session:
            review = cls(
                reviewee_id=reviewee_id, 
                reviewer_id=reviewer_id, 
                rating=rating, 
                content=content
            )
            session.add(review)
            session.commit()
            return review

    # --- CRUD INSTANCE METHODS (Update/Delete) ---

    def update(self):
        with Session() as session:
            session.merge(self)
            session.commit()
            return self

    def delete(self):
        with Session() as session:
            session.delete(session.merge(self))
            session.commit()