#Functions
# A function is named, reusable block of code that does one job

def greet():
    print("Hello, welcome to my AI Program")

greet()

def greet(name):
    print(f"Hello {name}! Welcome.")
greet("Hema")
greet("Anudeep")
greet("Sahithi")

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    print(f"You are {age} years old.")
calculate_age(2026, 1998)
calculate_age(2026, 1992)

def introduce(name, job):
    print(f"Hi, I'm {name} and I work in {job}.")
introduce("Hema", "Marketing")
introduce("Sahithi", "Oracle")
introduce("Anudeep", "SAP")

#return
def add(a,b):
    return a + b
result = add(5,3)
print(result)

def add(a,b):
    return a + b
total = add(5,3)
doubled = add(total,total)
print(doubled)

#student report card

students = [{"name" : "Hema", "marks" : 85},
           {"name" : "Sahithi", "marks" : 90},
           {"name" : "Anudeep", "marks" : 75},
           {"name" : "nandu", "marks" : 32}
]

def count_passed(students):
    counter = 0
    for student in students:
        if student['marks'] >= 35:
            counter+=1
    return counter
result = count_passed(students)
print(f"{result}- students passed")