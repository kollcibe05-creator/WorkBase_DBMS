
import os
import platform 
import time

from .models.__init__ import recreate_db 
from .models.department import Department
from .models.employee import Employee
from .models.review import Review
from .debug import seed_database

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
    list_department_employees,
    create_review,        
    find_review_by_id,    
    list_all_reviews,
)
def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":    #contigency
        os.system('cls')
    else:
        os.system('clear')
def pause():
    """Pauses execution until the user presses Enter."""
    input("\nPress Enter to return to  menu...")        

def menu():
    print("--- Department----")
    print("1. List all departments")
    print("2. Find department by name")
    print("3. Find department by id")
    print("4. Create department")
    print("5. Update department")
    print("6. Delete department")
    print("--- Employee-------")
    print("7. List all employees")
    print("8. Find employee by name")
    print("9. Find employee by id")
    print("10. Create employee")
    print("11. Update employee")
    print("12. Delete employee")
    print("13. List all employees in a department")
    print("--- Review-------")
    print("14. Add a new review")
    print("15. Find review by id")
    print("16. List all reviews")
    print("0. Exit the program")




def main():
    try:
        recreate_db()
        seed_database()
        print("Database initialized successfully.")
    except Exception as Error:
        print(f"Error setting up database: {Error}")
        return 
        
    while True:
        clear_screen()
        menu()
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_departments()
            pause()
        elif choice == "2":
            find_department_by_name()
            pause()
        elif choice == "3":
            find_department_by_id()
            pause()
        elif choice == "4":
            create_department()
            pause()
        elif choice == "5":
            update_department()
            pause()
        elif choice == "6":
            delete_department()
            pause()
        elif choice == "7":
            list_employees()
            pause()
        elif choice == "8":
            find_employee_by_name()
            pause()
        elif choice == "9":
            find_employee_by_id()
            pause()
        elif choice == "10":
            create_employee()
            pause()
        elif choice == "11":
            update_employee()
            pause()
        elif choice == "12":
            delete_employee()
            pause()
        elif choice == "13":
            list_department_employees()
            pause()
        elif choice == "14":
            create_review()
            pause()
        elif choice == "15":
            find_review_by_id()
            pause()
        elif choice == "16":
            list_all_reviews()
            pause()
        else:
            print("Invalid choice.")
            pause()


if __name__ == "__main__":
    main()
