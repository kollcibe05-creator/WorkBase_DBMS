# WorkBase_DBMS

##### Welcome to WorkBase_DBMS!!!

WorkBase_DBMS is a CLI + SQL + ORM  backend project aimed at resolving the complexity of organizing employees' data with consistency and persisting the changes to the Database. It implements sqlalchemy, SQL and OOP to model the database and ensure accuracy while accessing the data

The ideological business requirements are:

1. An Employee can only be in `one` Department.
2. A Department can have `many` Employees.
3. A Review belongs to `one` Employee and `one` employee can have `many` Reviews.
_______


## Tech Stack
- Python
- Markdown
- SQL

## File Structure

Take a look at the directory structure:

```console
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── lib
│   ├── __init__.py
│   ├── cli.py
│   ├── debug.py
│   ├── helpers.py
│   └── models
│       ├── __init__.py
│       ├── department.py
│       ├── employee.py
│       └── review.py
└── workbase.db

        
```


## Generating Your Environment

You might have noticed in the file structure- there's  a Pipfile!

Install  the dependencies  you'll need to navigate the file by 
adding them to the `Pipfile`. Run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

This project template has the CLI in `lib/cli.py`, `sample`:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`, `Sample`:

```py
# lib/helpers.py



from .models.department import Department
from .models.employee import Employee
from .models.review import Review 
from sqlalchemy.exc import IntegrityError 



def exit_program():
    print("Goodbye!")
    exit()

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

```

You can run the template CLI with:
```
python -m lib.cli

```

```
 python lib/cli.py
 ```
Or include the shebang and make it executable with:
```
chmod +x lib/cli.py

```

Which afterwards you'll run the CLI with:

```
./lib/cli.py

```
in the root directory.Alternatively you can change directory into the *lib* directory and use:

```
./cli.py

```
The template CLI will ask for input, manipulate your dabatase to do some work, and accomplish your sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the requirements.

## Functionality
# Department.py
It contains the model `Department` which has the following functionalitites.
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
   Below it are the constraints that restricts some field inputs to be of certain data types and length.
3. *get_all()*: A class method that returns all the departments mapped into the departments table.
4. *find_by_id()*: A class method that returns a department instance in the database of the id given.
5. *find_by_name()*: A class method that returns a department instance in the database of the name given.
6. *create()*: A class method that creates a new department instance and persists it to the database using sessions.
5. *update()*: A class method that updates the department instance and persists it to the database using sessions.
8. *delete()*: A class method that deletes a department instance and from the database using sessions.


# Employee.py
It contains the model `Employee` which has the functionalities:
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
    Below it are the constraints that restricts some field inputs to be of certain data types and length.
    Fields such as *received_reviews*, *given_reviews* and *department* have been used to create the relationship with the departments and reviews Models and tables. 
3. *get_all()*: A class method that returns all the employees mapped into the departments table.
4. *find_by_id()*: A class method that returns an employee instance in the database of the id given.
5. *find_by_full_name()*: A class method that returns an employee instance in the database of the names given.
6. *create()*: A class method that creates a new employee instance and persists it to the database using sessions.
5. *update()*: A class method that updates the employee instance details and persists it to the database using sessions.
8. *delete()*: A class method that deletes an employee instance and from the database using sessions.

# Review.py
It contains the model `Review` which has the functionalitites:
1. *__repr__*: In it is the modified output of a class instance to improve clarity.
2. *__tablename__*: Species the table in the database that the objects will be mapped to.
    Below it are the constraints that restricts some field inputs to be of certain data types and length.
    Fields *reviewee* and *reviewer*  have been used to create  relationship with the employee Model and table in the database. 
3. *get_all()*: A class method that returns all the reviews mapped into the departments table.
4. *find_by_id()*: A class method that returns a review instance in the database of the id given.
5. *create()*: A class method that creates a new review instance and persists it to the database using sessions.
6. *update()*: A class method that updates the review instance details and persists it to the database using sessions.
7. *delete()*: A class method that deletes a review instance and from the database using sessions.
<!-- 5. *find_by_name()*: A class method that returns a review instance in the database of the names given. -->







# Author
*Collins Kibet*

## [License](LICENSE)

MIT License
Copyright (c) 2025 Collins Kibet


# Contact info
* Email : kollcibe05@gmail.com


`(**Thank you**)`


