#Tupples : A list that cant be changed
coordinates = (17.3, 17.4, 17.5)
print(coordinates)
print(coordinates[0])
#coordinates[0] = 99 this change is not supported in tuple

#sets- A list with no duplicates and no order
emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print(unique_emails)

#conditionals
#if something is true then do this condition
age = 33
if age>=18:
    print("You are an adult")
else:
    print("You are a minor")