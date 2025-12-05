# # lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()


# lib/cli.py (Example Snippet)

import lib.helpers as h
from lib.models.__init__ import recreate_db

def main():
    # 1. Setup the database
    recreate_db()
    
    # 2. Add some initial data using the helper functions
    engineering = h.create_department("Engineering", "4th Floor")
    marketing = h.create_department("Marketing", "2nd Floor")
    
    # Use the IDs of the newly created departments
    emp1 = h.create_employee("Alice", "Smith", 95000, engineering.id)
    emp2 = h.create_employee("Bob", "Johnson", 80000, engineering.id)
    emp3 = h.create_employee("Charlie", "Brown", 75000, marketing.id)
    
    # Add a review (Alice reviews Bob)
    if emp1 and emp2:
        h.add_review(emp2.id, emp1.id, 4, "Solid performance this quarter.")
        
    # 3. Retrieve and display data
    print("\n--- All Departments ---")
    for dept in h.get_all_departments():
        print(f"{dept.name} ({len(dept.employees)} employees)")
        
    print("\n--- Bob's Reviews ---")
    if emp2:
        bob_reviews = h.get_employee_reviews(emp2.id)
        for review in bob_reviews:
            print(f"Rating: {review.rating}, Content: {review.content}")
        
if __name__ == "__main__":
    main()