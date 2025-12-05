# WorkBase_DBMS

##### Welcome to WorkBase_DBMS!!!

WorkBase_DBMS is a CLI + SQL + ORM  backend project aimed at resolving the complexity of organizing employees' data with consistency and persisting the changes to the Database. It implements sqlalchemy, SQL and OOP to model the database and ensure accuracy while accessing the data

The ideological business requirements are:

1. An Employee can only be in `one` Department.
2. A Department can have `many` Employees.
3. A Review belongs to `one` Employee and one employee can have `many` Reviews.
_______


### Tech Stack
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
└── lib
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── models
        ├── __init__.py
        ├── department.py
        ├── employee.py
        └── review.py
        
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

This project template has the CLI in `lib/cli.py` that looks like this:

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

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with:
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





# Author
*Collins Kibet*

## [License](LICENSE)

MIT License
Copyright (c) 2025 Collins Kibet


# Contact info
* Email : kollcibe05@gmail.com


