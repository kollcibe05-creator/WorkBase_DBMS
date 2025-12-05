
import ipdb
from .models.__init__ import recreate_db
from .models.department import Department
from .models.employee import Employee
from .models.review import Review 


def seed_database():
    """Drops tables, recreates schema, and adds sample data."""
    print("Seeding database...")
    recreate_db()
    
    hr = Department.create("Human Resources", "Headquarters")
    eng = Department.create("Engineering", "West Coast Office")
    sales = Department.create("Sales", "East Coast Office")
    print("Departments created.")


    alice = Employee.create("Alice", "Kegoya", 60000, hr)
    bob = Employee.create("Bob", "Burundi", 62000, hr)
    

    wafula = Employee.create("Wafula", "Black", 120000, eng)
    nekesa = Employee.create("Nekesa", "Purity", 130000, eng)
    
    eva = Employee.create("Evalyne", "Mumbi", 95000, sales)
    print("Employees created.")


    # Wafula reviews Nekesa
    Review.create(reviewee_id=nekesa, reviewer_id=wafula, rating=4, content="Excellent technical skills.")
    
    # Alice reviews Bob
    Review.create(reviewee_id=bob, reviewer_id=alice, rating=3, content="Needs improved time management.")
    
    # Nekesa reviews Wafula
    Review.create(reviewee_id=wafula, reviewer_id=nekesa, rating=5, content="Highly valuable team lead.")
    print("Reviews created.")


if __name__ == '__main__':
    seed_database()
    ipdb.set_trace()