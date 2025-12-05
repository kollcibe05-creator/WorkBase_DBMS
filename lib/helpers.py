# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")


# def exit_program():
#     print("Goodbye!")
#     exit()
# lib/helpers.py
from sqlalchemy import select
from lib.models.__init__ import Session
# Import the models to use them in the functions
from lib.models.department import Department
from lib.models.employee import Employee
from lib.models.review import Review

## --- Department CRUD ---

def create_department(name, location):
    """Creates and saves a new Department record."""
    with Session() as session:
        new_dept = Department(name=name, location=location)
        session.add(new_dept)
        session.commit()
        print(f"✅ Department '{name}' created with ID {new_dept.id}")
        return new_dept

def get_all_departments():
    """Retrieves all departments from the database."""
    with Session() as session:
        # Using SQLAlchemy 2.0 style select() statement
        statement = select(Department)
        departments = session.scalars(statement).all()
        return departments

## --- Employee CRUD ---

def create_employee(first_name, last_name, salary, dept_id):
    """Creates and saves a new Employee record."""
    with Session() as session:
        # Check if department exists
        dept = session.get(Department, dept_id)
        if not dept:
            print(f"❌ Error: Department with ID {dept_id} not found.")
            return None
            
        new_employee = Employee(
            first_name=first_name, 
            last_name=last_name, 
            salary=salary, 
            department_id=dept_id
        )
        session.add(new_employee)
        session.commit()
        print(f"✅ Employee '{first_name} {last_name}' added to {dept.name}.")
        return new_employee

def get_employee_by_id(employee_id):
    """Retrieves a single employee by their ID."""
    with Session() as session:
        return session.get(Employee, employee_id)

## --- Review CRUD ---

def add_review(reviewee_id, reviewer_id, rating, content):
    """Adds a review from one employee (reviewer) to another (reviewee)."""
    with Session() as session:
        # It's good practice to ensure both employees exist
        reviewee = session.get(Employee, reviewee_id)
        reviewer = session.get(Employee, reviewer_id)
        
        if not reviewee or not reviewer:
            print("❌ Error: One or both employee IDs are invalid.")
            return None

        new_review = Review(
            reviewee_id=reviewee_id,
            reviewer_id=reviewer_id,
            rating=rating,
            content=content
        )
        session.add(new_review)
        session.commit()
        print(f"✅ Review added for {reviewee.first_name} by {reviewer.first_name}.")
        return new_review

# Example of a common utility function
def get_employee_reviews(employee_id):
    """Retrieves all reviews received by a specific employee."""
    with Session() as session:
        employee = session.get(Employee, employee_id)
        if employee:
            # Access the relationship attribute defined in the Employee model
            return employee.received_reviews
        return []