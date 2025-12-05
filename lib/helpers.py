# lib/helpers.py

from .models.department import Department # Use relative imports
from .models.employee import Employee
from .models.review import Review # Include Review for completeness
from sqlalchemy.exc import IntegrityError 

# --- EXIT FUNCTION ---

def exit_program():
    print("Goodbye!")
    exit()

# ----------------------------------------------------------------------
## Department Functions
# ----------------------------------------------------------------------

def list_departments():
    departments = Department.get_all()
    if departments:
        print("\n--- All Departments ---")
        for department in departments:
            print(department)
        print("-----------------------")
    else:
        print("No departments found.")


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department "{name}" not found')


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    try:
        department = Department.find_by_id(id_)
        print(department) if department else print(f'Department {id_} not found')
    except ValueError:
        print("Invalid ID format. Please enter a number.")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'✅ Success: {department}')
    except IntegrityError as exc:
        print(f"❌ Error: Department '{name}' already exists or data invalid.")
    except Exception as exc:
        print("❌ Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    
    if department:
        try:
            name = input(f"Enter the department's new name (Current: {department.name}): ") or department.name
            location = input(f"Enter the department's new location (Current: {department.location}): ") or department.location

            department.name = name
            department.location = location

            department.update() 
            print(f'✅ Success: {department}')
        except Exception as exc:
            print("❌ Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    
    if department:
        try:
            department.delete()
            print(f'🗑️ Department {id_} deleted (Employees cascaded).')
        except Exception as exc:
            print("❌ Error deleting department: ", exc)
    else:
        print(f'Department {id_} not found')

# ----------------------------------------------------------------------
## Employee Functions
# ----------------------------------------------------------------------

def list_employees():
    employees = Employee.get_all()
    if employees:
        print("\n--- All Employees ---")
        for employee in employees:
            print(employee)
        print("---------------------")
    else:
        print("No employees found.")


def find_employee_by_name():
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    employee = Employee.find_by_full_name(first_name, last_name)
    if employee:
        print(employee)
    else:
        print(f"Employee {first_name} {last_name} not found.")

def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    try:
        employee = Employee.find_by_id(id_)
        print(employee) if employee else print(f'Employee {id_} not found')
    except ValueError:
        print("Invalid ID format. Please enter a number.")

def create_employee():
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    salary_str = input("Enter employee's salary: ")
    dept_id_str = input("Enter department ID: ")
    try:
        salary = int(salary_str)
        dept_id = int(dept_id_str)
        
        # Check if department exists (best handled in the model create method or here)
        if not Department.find_by_id(dept_id):
            print(f"❌ Error: Department ID {dept_id} not found.")
            return

        employee = Employee.create(first_name, last_name, salary, dept_id)
        print(f'✅ Success: {employee}')
    except ValueError:
        print("❌ Error: Salary and Department ID must be numbers.")
    except Exception as exc:
        print("❌ Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    
    if employee:
        try:
            new_salary_str = input(f"Enter new salary (Current: {employee.salary}): ")
            if new_salary_str:
                employee.salary = int(new_salary_str)
            
            # Example: Update department ID
            new_dept_id_str = input(f"Enter new department ID (Current: {employee.department_id}): ")
            if new_dept_id_str:
                new_dept_id = int(new_dept_id_str)
                if not Department.find_by_id(new_dept_id):
                    print(f"❌ Error: Department ID {new_dept_id} not found. Update cancelled.")
                    return
                employee.department_id = new_dept_id

            employee.update() 
            print(f'✅ Success: {employee}')
        except ValueError:
            print("❌ Error: Salary or Department ID must be a number.")
        except Exception as exc:
            print("❌ Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        try:
            employee.delete()
            print(f'🗑️ Employee {id_} deleted (Reviews cascaded).')
        except Exception as exc:
            print("❌ Error deleting employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def list_department_employees():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        print(f"\n--- Employees in {department.name} ---")
        if department.employees:
            for employee in department.employees:
                print(employee)
        else:
            print(f"No employees found in {department.name}.")
        print("-----------------------------------")
    else:
        print(f'Department {id_} not found')

def list_all_reviews():
    """Lists all reviews."""
    reviews = Review.get_all()
    if reviews:
        print("\n--- All Reviews ---")
        for review in reviews:
            # Note: The Review.__repr__ should be descriptive
            print(review) 
        print("-------------------")
    else:
        print("No reviews found.")

def find_review_by_id():
    """Finds a review by its ID."""
    id_ = input("Enter the review's id: ")
    try:
        review = Review.find_by_id(id_)
        print(review) if review else print(f'Review {id_} not found')
    except ValueError:
        print("Invalid ID format. Please enter a number.")

def create_review():
    """Prompts user for details to create a new review."""
    reviewee_id = input("Enter the ID of the employee being reviewed (Reviewee ID): ")
    reviewer_id = input("Enter the ID of the employee writing the review (Reviewer ID): ")
    rating_str = input("Enter rating (1-5): ")
    content = input("Enter review content/notes: ")
    
    try:
        reviewee = Employee.find_by_id(reviewee_id)
        reviewer = Employee.find_by_id(reviewer_id)
        rating = int(rating_str)
        
        if not reviewee:
            print(f"❌ Error: Reviewee ID {reviewee_id} not found.")
            return
        if not reviewer:
            print(f"❌ Error: Reviewer ID {reviewer_id} not found.")
            return

        review = Review.create(reviewee.id, reviewer.id, rating, content)
        print(f'✅ Success: Review added for {reviewee.first_name} by {reviewer.first_name}.')
    except ValueError:
        print("❌ Error: Rating and IDs must be numbers.")
    except Exception as exc:
        print("❌ Error creating review: ", exc)        