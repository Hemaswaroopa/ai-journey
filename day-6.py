#if else conditions

marks = 33
if marks >= 35:
    print ("Pass")
else:
    print("Fail")

#elif
marks = 23

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 35:
    print("Grade: D- Pass")
else:
    print("Grade: F- Fail")

#Two conditions

age = 15
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")


aadhar = False
passport = False

if aadhar or passport:
    print("Logged in")
else:
    print("Cannot enter")

#Library access Checker
Student = {"name" : "Hema", "age" : 27, "has_membership" : False, "books_borrowed" : 2}

if Student["has_membership"] and Student["books_borrowed"] < 5:
    print(f"Hi {Student['name']} , You can borrow another book")
elif Student["has_membership"] and Student["books_borrowed"] >= 5:
    print(f"Hi {Student['name']} , Borrow limit has reached")
else:
    print(f"Hi {Student['name']} , please signup first")

#Movie Ticket Pricing 

customer = {"name" : "Hema", "age" : 18, "is_member" : True, "day" : "Tuesday" }

if customer["age"] < 12 :
    print(f"Hi {customer['name']}, child ticket : Rs.100")
elif customer["age"] >= 60:
    print(f"Hi {customer['name']}, Senior ticket : Rs.120")
elif customer['is_member'] and customer["day"] == "Tuesday":
    print(f"Hi {customer['name']}, member Tuesday discount : Rs.150")
else:
    print(f"Hi {customer['name']}, regular ticket : Rs. 250")