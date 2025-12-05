# # # lib/cli.py

# # from helpers import (
# #     exit_program,
# #     helper_1
# # )


# # def main():
# #     while True:
# #         menu()
# #         choice = input("> ")
# #         if choice == "0":
# #             exit_program()
# #         elif choice == "1":
# #             helper_1()
# #         else:
# #             print("Invalid choice")


# # def menu():
# #     print("Please select an option:")
# #     print("0. Exit the program")
# #     print("1. Some useful function")


# # if __name__ == "__main__":
# #     main()


# # lib/cli.py (Example Snippet)

# from  . import helpers as h
# from .models.__init__ import recreate_db

# from .models.department import Department
# from .models.employee import Employee
# from .models.review import Review

# def main():
#     # 1. Setup the database
#     recreate_db()
    
#     # 2. Add some initial data using the helper functions
#     engineering = h.create_department("Engineering", "4th Floor")
#     marketing = h.create_department("Marketing", "2nd Floor")
    
#     # Use the IDs of the newly created departments
#     emp1 = h.create_employee("Alice", "Smith", 95000, engineering.id)
#     emp2 = h.create_employee("Bob", "Johnson", 80000, engineering.id)
#     emp3 = h.create_employee("Charlie", "Brown", 75000, marketing.id)
    
#     # Add a review (Alice reviews Bob)
#     if emp1 and emp2:
#         h.add_review(emp2.id, emp1.id, 4, "Solid performance this quarter.")
        
#     # 3. Retrieve and display data
#     print("\n--- All Departments ---")
#     for dept in h.get_all_departments():
#         print(f"{dept.name} ({len(dept.employees)} employees)")
        
#     print("\n--- Bob's Reviews ---")
#     if emp2:
#         bob_reviews = h.get_employee_reviews(emp2.id)
#         for review in bob_reviews:
#             print(f"Rating: {review.rating}, Content: {review.content}")
        
# if __name__ == "__main__":
#     main()


















# lib/cli.py

# ----------------------------------------------------------------------
# 1. Database Setup Imports
# ----------------------------------------------------------------------
# Imports recreate_db() and ensures all models are registered with SQLAlchemy Base.
from .models.__init__ import recreate_db 
from .models.department import Department
from .models.employee import Employee
from .models.review import Review # Not used directly here, but ensures registration

# ----------------------------------------------------------------------
# 2. Helpers Imports (The CLI's Action Handlers)
# ----------------------------------------------------------------------
# FIX: Uses relative import 'from .helpers'
from .helpers import (
    exit_program,
    list_departments,
    find_department_by_name,
    find_department_by_id,
    create_department,
    update_department,
    delete_department,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees
)


# ----------------------------------------------------------------------
# 3. Menu Function
# ----------------------------------------------------------------------

def menu():
    print("\n" + "="*40)
    print("🏢 WORKBASE CLI MENU")
    print("="*40)
    print("--- Department Management ---")
    print("1. List all departments")
    print("2. Find department by name")
    print("3. Find department by id")
    print("4. Create department")
    print("5. Update department")
    print("6. Delete department")
    print("--- Employee Management ---")
    print("7. List all employees")
    print("8. Find employee by name")
    print("9. Find employee by id")
    print("10. Create employee")
    print("11. Update employee")
    print("12. Delete employee")
    print("13. List all employees in a department")
    # You could add Review management options here if needed (e.g., Add Review)
    print("-----------------------------")
    print("0. Exit the program")


# ----------------------------------------------------------------------
# 4. Main Loop
# ----------------------------------------------------------------------

def main():
    # Execute the database setup once
    try:
        recreate_db()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"❌ Error setting up database: {e}")
        return # Exit if setup fails
        
    while True:
        menu()
        choice = input("Enter your choice > ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
        elif choice == "2":
            find_department_by_name()
        elif choice == "3":
            find_department_by_id()
        elif choice == "4":
            create_department()
        elif choice == "5":
            update_department()
        elif choice == "6":
            delete_department()
        elif choice == "7":
            list_employees()
        elif choice == "8":
            find_employee_by_name()
        elif choice == "9":
            find_employee_by_id()
        elif choice == "10":
            create_employee()
        elif choice == "11":
            update_employee()
        elif choice == "12":
            delete_employee()
        elif choice == "13":
            list_department_employees()
        else:
            print("❗ Invalid choice. Please select a number from the menu.")


if __name__ == "__main__":
    main()
