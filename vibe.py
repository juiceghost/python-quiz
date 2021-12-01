from pathlib import Path


# Creates and appends a hash of the password entered in a "hash" file
def passwd(name, password):
    passwd_file = Path.home() / "My_company/employees/passwds/hash"
    passwd_file.parent.mkdir(exist_ok=True)
    passwd_file.touch(exist_ok=True)
    with passwd_file.open(mode="a", encoding="utf-8") as file:
        file.write(f"{name}\n" + str(hash(password)) + "\n")


# Function made to add the employee to the "employees.txt" file:
# Also creates and appends the information with a framed format
# Example:
# -----------------------------------------------------
# * Viktor Berg | 1996-09-30 | Viktor.Berg@chaffteam.se
# -----------------------------------------------------
def register(name, d8_of_birth, email):
    lst = [name + " | " + d8_of_birth + " | " + email]
    employee_file_path = Path.home() / "My_company/employees/employees.txt"
    if not employee_file_path.exists():
        employee_file_path.touch()
    else:
        print("File exists, adding employee...")
    with employee_file_path.open(mode="a", encoding="utf-8") as file:
        file.write(" " + ("-" * len(str(lst))) + "\n")
        file.write("*" + (str(lst)) + "\n")
        file.write(" " + ("-" * len(str(lst))) + "\n")


# Starting adding the employee with a simple input
employee = input(str("Name of employee: "))


# Straight after, enter loop to input date of birth:
# Controls how long the date of birth is to tailor the format,
# As either YYYY-MM-DD or YY-MM-DD
while True:
    date_of_birth = input(str("Employee's date of birth: "))
    try:
        if len(date_of_birth) == 8:
            date_of_birth = date_of_birth[0:4] + "-" + date_of_birth[4:6] + "-" + date_of_birth[6:8]
            break
        elif len(date_of_birth) == 6:
            date_of_birth = date_of_birth[0:2] + "-" + date_of_birth[2:4] + "-" + date_of_birth[4:6]
            break
        else:
            print("Date of birth entered in the wrong format...")
    except NameError:
        print("Wrong!")

# User gets to input a password for said employee (Only as an additional function of the script)
password = input(str("Enter a password for the employee: "))
passwd(employee, password)
# Converts the name of the employee entered prior, to create an email-address for said employee
if employee.find(" "):
    dot = employee.replace(" ", ".")
    employee_email = f"{dot}@chaffteam.se"
else:
    employee_email = f"{employee}@chaffteam.se"

# Converts the name of the employee to create a working directory for said employee:
employee_dir = employee.replace(" ", "_")
path = Path.home() / f"My_company/employees/{employee_dir}"
path.mkdir(parents=True, exist_ok=True)

# Creates an empty file with the employees name:
employee_file = path / f"{employee.replace(' ', '')}"
employee_file.touch()

# Prompts the User to input weather he/she wants to add the employee to the "employees.txt" file:
reg = input(str("Wish to add employee to files?: [Y/n]\n"))
if reg.upper() == "Y":
    register(employee, date_of_birth, employee_email)
else:
    print("Employee not added to files...")


